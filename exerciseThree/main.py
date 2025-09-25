from models.chatroom import ChatRoom
from models.user import User

if __name__ == "__main__":
    chat = ChatRoom()
    alice = User("Alice")
    bob = User("Bob")
    carol = User("Carol")

    chat.register(alice)
    chat.register(bob)
    chat.register(carol)

    alice.send("Hola a todos!")
    bob.send("Hola Alice!")
    carol.send("¿Qué tal?")