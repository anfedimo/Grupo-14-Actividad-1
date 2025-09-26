from abc import ABC, abstractmethod


class PlataformaVisualizacion(ABC):
    @abstractmethod
    def mostrar_notificacion(self, tipo_notificacion: str) -> str:
        pass


class VisualizacionWeb(PlataformaVisualizacion):
    def mostrar_notificacion(self, tipo_notificacion: str) -> str:
        return f"Mostrando notificación de {tipo_notificacion} en plataforma Web."


class VisualizacionMovil(PlataformaVisualizacion):
    def mostrar_notificacion(self, tipo_notificacion: str) -> str:
        return f"Mostrando notificación de {tipo_notificacion} en plataforma Móvil."


class VisualizacionEscritorio(PlataformaVisualizacion):
    def mostrar_notificacion(self, tipo_notificacion: str) -> str:
        return f"Mostrando notificación de {tipo_notificacion} en plataforma Escritorio."