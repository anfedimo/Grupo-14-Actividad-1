from typing import List
from .user import User

class ChatRoom:
    """Mediator: centraliza la comunicación entre usuarios."""
    def __init__(self):
        self.users: List[User] = []

    def register(self, user: User) -> None:
        """Registra un nuevo usuario, evitando duplicados."""
        if user not in self.users:
            self.users.append(user)
            user.chatroom = self

    def send(self, message: str, sender: User) -> None:
        """Envía un mensaje de un usuario a todos los demás."""
        for user in self.users:
            if user != sender:
                user.receive(message, sender)
