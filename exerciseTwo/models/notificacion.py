from __future__ import annotations
from abc import ABC, abstractmethod
from .plataforma import PlataformaVisualizacion


class Notificacion(ABC):
    def __init__(self, plataforma: PlataformaVisualizacion) -> None:
        self.plataforma = plataforma

    @abstractmethod
    def obtener_tipo(self) -> str:
        pass

    def mostrar(self) -> str:
        return self.plataforma.mostrar_notificacion(self.obtener_tipo())


class NotificacionMensaje(Notificacion):
    def obtener_tipo(self) -> str:
        return "mensaje"


class NotificacionAlerta(Notificacion):
    def obtener_tipo(self) -> str:
        return "alerta"


class NotificacionAdvertencia(Notificacion):
    def obtener_tipo(self) -> str:
        return "advertencia"


class NotificacionConfirmacion(Notificacion):
    def obtener_tipo(self) -> str:
        return "confirmación"