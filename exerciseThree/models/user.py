class User:
    """Colleague: representa un usuario en la sala de chat."""
    def __init__(self, name: str):
        self.name: str = name
        self.chatroom: 'ChatRoom' = None

    def send(self, message: str) -> None:
        """Envía un mensaje al chatroom."""
        if self.chatroom:
            print(f"{self.name} envía: {message}")
            self.chatroom.send(message, self)
        else:
            print(f"{self.name} no está en ninguna sala.")

    def receive(self, message: str, sender: 'User') -> None:
        """Recibe un mensaje de otro usuario."""
        print(f"{self.name} recibe de {sender.name}: {message}")
