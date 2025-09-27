from models.plataforma import VisualizacionWeb, VisualizacionMovil, VisualizacionEscritorio
from models.notificacion import NotificacionMensaje, NotificacionAlerta, NotificacionAdvertencia, NotificacionConfirmacion


def imprimir_notificacion(notificacion) -> None:
    print(notificacion.mostrar())


if __name__ == "__main__":
    plataforma_web = VisualizacionWeb()
    imprimir_notificacion(NotificacionMensaje(plataforma_web))
    imprimir_notificacion(NotificacionAlerta(plataforma_web))

    plataforma_movil = VisualizacionMovil()
    imprimir_notificacion(NotificacionAdvertencia(plataforma_movil))
    imprimir_notificacion(NotificacionConfirmacion(plataforma_movil))

    plataforma_escritorio = VisualizacionEscritorio()
    imprimir_notificacion(NotificacionMensaje(plataforma_escritorio))