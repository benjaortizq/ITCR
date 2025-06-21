import threading as th
import time as t
import random
from pathlib import Path
import json
import random
import pygame

RUTA_PEDIDOS = (Path(__file__).parent / "pedidos").resolve()
print("Ruta absoluta esperada:", RUTA_PEDIDOS)
print("¿Existe?", RUTA_PEDIDOS.exists())
# --- Definición de Clases ---

class Pizza:
    TOPPINGS = ["pepperoni", "hawaiana", "vegetariana"]
    
    def __init__(self, tamano, tipo):
        if tipo not in self.TOPPINGS:
            raise ValueError(f"Tipo inválido. Opciones: {', '.join(self.TOPPINGS)}")
        
        self.tamano = tamano  # Tiempo de horneado en segundos
        self.tipo = tipo
        self.estado = "crudo"  # Estados: crudo, cocinando, listo
        
    def __str__(self):
        return f"{self.tipo} ({self.tamano}s) - {self.estado}"

class Pedido(th.Thread):
    def __init__(self, id_pedido, pizzas, direccion, cliente):
        super().__init__()
        self.id_pedido = id_pedido
        self.pizzas = pizzas
        self.ubicacion = direccion  # Tupla (x, y) o dirección
        self.cliente = cliente 
        self.tiempo_registro = t.time()
        self.estado = "recibido"  # Estados: recibido, procesando, horneando, en_camino, entregado
        self.tiempo_entrega = None
        self.tiempo_salida = None
        self.eta = None
        self.daemon = True
        self.lock = th.Lock()
        self.start()
    
    def run(self):
        self.actualizar_estado("procesando")
        
        # Simular tiempo de preparación antes de hornear
        t.sleep(random.uniform(1.0, 3.0))
        
        # Pasar al sistema de horneado
        self.actualizar_estado("horneando")
        HornoManager.agregar_pedido(self)
        
        # Esperar hasta que todas las pizzas estén listas
        while not self.todas_pizzas_listas():
            t.sleep(0.1)
        
        # Pasar al sistema de delivery
        self.actualizar_estado("en_camino")
        DeliveryManager.agregar_pedido(self)
        
        # Esperar hasta que se entregue
        while self.estado != "entregado":
            t.sleep(0.1)
    
    def actualizar_estado(self, nuevo_estado):
        with self.lock:
            self.estado = nuevo_estado
            if nuevo_estado == "en_camino":
                self.tiempo_salida = t.time()
                # misma fórmula que en el Repartidor
                distancia = random.uniform(3.0, 8.0)
                self.eta = distancia * 2
    
    def todas_pizzas_listas(self):
        return all(pizza.estado == "listo" for pizza in self.pizzas)
    
    def obtener_estado(self):
        with self.lock:
            return {
                "id": self.id_pedido,
                "estado": self.estado,
                "ubicacion": self.ubicacion,
                "tiempo_espera": t.time() - self.tiempo_registro,
                "pizzas": [str(p) for p in self.pizzas]
            }
    def to_dict(self):
        return {
            "id_pedido": self.id_pedido,
            "cliente": self.cliente,
            "pizzas": [
                {"tamano": p.tamano, "tipo": p.tipo, "estado": p.estado}
                for p in self.pizzas
            ],
            "direccion": self.ubicacion,
            "tiempo_registro": self.tiempo_registro,
            "estado": self.estado,
            "tiempo_entrega": self.tiempo_entrega,
            "tiempo_salida": self.tiempo_salida,
            "eta": self.eta,
        }
    @classmethod
    def from_dict(cls, data):
        pizzas = []
        for pd in data.get("pizzas", []):
            pizza = Pizza(pd["tamano"], pd["tipo"])
            pizza.estado = pd.get("estado", pizza.estado)
            pizzas.append(pizza)

        pedido = cls( id_pedido=data["id_pedido"],cliente=data["cliente"],pizzas=pizzas,direccion=data["direccion"])
        pedido.tiempo_registro = data.get("tiempo_registro", pedido.tiempo_registro)
        pedido.estado          = data.get("estado", pedido.estado)
        pedido.tiempo_entrega  = data.get("tiempo_entrega", pedido.tiempo_entrega)
        pedido.tiempo_salida   = data.get("tiempo_salida", pedido.tiempo_salida)
        pedido.eta             = data.get("eta", pedido.eta)
        return pedido
class HornoManager:
    hornos = []
    cola_pedidos = []
    lock = th.Lock()
    evento_nuevo_pedido = th.Event()
    
    @classmethod
    def iniciar_hornos(cls, cantidad):
        cls.hornos = [Horno(i) for i in range(cantidad)]
    
    @classmethod
    def agregar_pedido(cls, pedido):
        with cls.lock:
            cls.cola_pedidos.append(pedido)
            cls.evento_nuevo_pedido.set()
    
    @classmethod
    def obtener_progreso_hornos(cls):
        return [h.obtener_estado() for h in cls.hornos]

class Horno(th.Thread):
    def __init__(self, id_horno):
        super().__init__()
        self.id_horno = id_horno
        self.pizza_actual = None
        self.tiempo_inicio = None
        self.tiempo_total = None
        self.lock = th.Lock()
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            # Esperar hasta que haya pedidos
            while not HornoManager.cola_pedidos:
                HornoManager.evento_nuevo_pedido.wait(0.1)
            
            # Tomar el próximo pedido
            with HornoManager.lock:
                if HornoManager.cola_pedidos:
                    pedido = HornoManager.cola_pedidos.pop(0)
                    if not HornoManager.cola_pedidos:
                        HornoManager.evento_nuevo_pedido.clear()
                else:
                    continue
            
            # Hornear cada pizza del pedido
            for pizza in pedido.pizzas:
                with self.lock:
                    self.pizza_actual = pizza
                    pizza.estado = "cocinando"
                    self.tiempo_inicio = t.time()
                    self.tiempo_total = pizza.tamano
                
                # Simular tiempo de horneado
                while t.time() - self.tiempo_inicio < self.tiempo_total:
                    t.sleep(0.1)
                
                with self.lock:
                    pizza.estado = "listo"
                    self.pizza_actual = None
    
    def obtener_estado(self):
        with self.lock:
            if self.pizza_actual:
                transcurrido = t.time() - self.tiempo_inicio
                porcentaje = min(transcurrido / self.tiempo_total, 1.0) * 100
                return {
                    "id_horno": self.id_horno,
                    "pizza": str(self.pizza_actual),
                    "progreso": porcentaje
                }
            return {
                "id_horno": self.id_horno,
                "pizza": None,
                "progreso": 0
            }

class DeliveryManager:
    repartidores = []
    cola_entregas = []
    lock = th.Lock()
    
    @classmethod
    def iniciar_repartidores(cls, cantidad):
        cls.repartidores = [Repartidor(i) for i in range(cantidad)]
    
    @classmethod
    def agregar_pedido(cls, pedido):
        with cls.lock:
            cls.cola_entregas.append(pedido)
    
    @classmethod
    def obtener_estado_repartidores(cls):
        return [r.obtener_estado() for r in cls.repartidores]

class Repartidor(th.Thread):
    def __init__(self, id_repartidor):
        super().__init__()
        self.id_repartidor = id_repartidor
        self.pedido_actual = None
        self.lock = th.Lock()
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            # Buscar trabajo
            with DeliveryManager.lock:
                if DeliveryManager.cola_entregas:
                    self.pedido_actual = DeliveryManager.cola_entregas.pop(0)
                else:
                    self.pedido_actual = None
            
            if self.pedido_actual:
                # Simular tiempo de entrega (depende de distancia)
                distancia = self.calcular_distancia(self.pedido_actual.ubicacion)
                tiempo_viaje = distancia * 2  # 2 segundos por unidad de distancia
                t.sleep(tiempo_viaje)
                
                # Marcar como entregado
                self.pedido_actual.actualizar_estado("entregado")
                self.pedido_actual.tiempo_entrega = t.time()
                self.pedido_actual = None
            else:
                t.sleep(1)  # Esperar antes de revisar nuevamente
    
    def calcular_distancia(self, ubicacion):
        # Simular cálculo de distancia (podría usar coordenadas reales)
        return random.uniform(3.0, 8.0)
    
    def obtener_estado(self):
        with self.lock:
            if self.pedido_actual:
                return {
                    "id_repartidor": self.id_repartidor,
                    "estado": f"Entregando pedido {self.pedido_actual.id_pedido}",
                    "pedido_id": self.pedido_actual.id_pedido
                }
            return {
                "id_repartidor": self.id_repartidor,
                "estado": "Disponible",
                "pedido_id": None
            }


#VARIABELES GLOBALES
pedidos = []

# Funciones para manejar pedidos desde archivos
def crear_pedido():
    return
def get_pedidos_from_folder():
    global pedidos, RUTA_PEDIDOS
    archivos = list(RUTA_PEDIDOS.glob("pedido*.json"))

    archivos.sort(key=lambda p: int(p.stem.replace("pedido", "")))
    for archivo in archivos:
        data = json.loads(archivo.read_text(encoding="utf-8"))
        pedidos.append(Pedido.from_dict(data))

get_pedidos_from_folder()

#pantallas 
HornoManager.iniciar_hornos(2)       # por ejemplo, 2 hornos
DeliveryManager.iniciar_repartidores(2)  #
def pizza_tracker(surface, font):
    global pedidos

    x, y = 10, 10
    ancho_barra, alto_barra = 200, 12
    padding = 6
    ahora = t.time()

    for pedido in pedidos:
        if pedido.estado == "entregado":
            continue

        # Texto: ID y estado
        texto = f"#{pedido.id_pedido} – {pedido.estado}"
        txt_surf = font.render(texto, True, (255,255,255))
        surface.blit(txt_surf, (x, y))
        y += txt_surf.get_height() + 4

        # 1) Progreso HORNO (% pizzas listas)
        total = len(pedido.pizzas)
        listas = sum(1 for p in pedido.pizzas if p.estado == "listo")
        prog_horno = listas / total if total else 0

        # dibujar fondo y barra
        pygame.draw.rect(surface, (50,50,50), (x, y, ancho_barra, alto_barra))
        pygame.draw.rect(surface, (200,100,0),
                         (x, y, int(ancho_barra * prog_horno), alto_barra))
        y += alto_barra + 2

        # 2) Progreso REPARTO (solo si ya salió)
        if pedido.estado == "en_camino" and pedido.tiempo_salida and pedido.eta:
            delta = ahora - pedido.tiempo_salida
            prog_reparto = min(delta / pedido.eta, 1.0)
        else:
            prog_reparto = 0

        pygame.draw.rect(surface, (50,50,50), (x, y, ancho_barra, alto_barra))
        pygame.draw.rect(surface, (0,200,100),
                         (x, y, int(ancho_barra * prog_reparto), alto_barra))
        y += alto_barra + padding

        # Si ya está completo, salto un poco más
        if pedido.estado == "entregado":
            y += padding

# Inicialización
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)



# Bucle principal
running = True
while running:
    if event := pygame.event.poll():
        if event.type == pygame.QUIT:
            running = False 
    screen.fill((30, 30, 30))  # Fondo oscuro
    pizza_tracker(screen, font)     
    pygame.display.flip()  # Actualizar pantalla

    clock.tick(60)

pygame.quit()