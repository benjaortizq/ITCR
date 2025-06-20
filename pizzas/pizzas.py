#CLASES
import pygame as pg 
import time as t
import threading as th


class Pizza : 
    def __init__( self, tamano,tipo ) : 
        self.tamano = tamano
        self.tipo = tipo
        self.estado="crudo"
    
class Horno (th.thread) : 
    def init(self,temperatura) : 
        self.temperatura=temperatura
        self.pizza_actual=None
        self.lock = th.Lock()
        self.horneando= th.Event()
        self.start()
    def meter_pizza(self, pizza ) : 
        if self.pizza_actual is None : 
            self.pizza_actual= pizza 
            self.tiempo_total = pizza.tamano
            self.tiempo_inicio = t.time()
            self.horneando.set()
            return True 
        return False
    def obtener_estado(self):
        with self.lock:
            if self.pizza_actual and self.tiempo_inicio:
                transcurrido = t.time() - self.tiempo_inicio
                porcentaje = min(transcurrido / self.tiempo_total, 1.0)
                return int(porcentaje * 100)
            return 0
    def hornear(self):
        while True:
            self.horneando.wait()
            while True:
                with self.lock:
                    if not self.pizza_actual:
                        break
                    transcurrido = t.time() - self.tiempo_inicio
                    if transcurrido >= self.tiempo_total:
                        self.pizza_actual.estado = "horneada"
                        self.horneando.clear()
                        return True
                t.sleep(0.1)
