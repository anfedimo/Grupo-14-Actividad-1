import pytest
from models.chatroom import ChatRoom
from models.user import User

class TestChatRoomMediator:

    def test_user_registration(self):
        chat = ChatRoom()
        alice = User("Alice")
        chat.register(alice)
        assert alice in chat.users
        assert alice.chatroom is chat

    def test_no_duplicate_registration(self):
        chat = ChatRoom()
        alice = User("Alice")
        chat.register(alice)
        chat.register(alice)  # intentar registrar dos veces
        assert chat.users.count(alice) == 1

    def test_send_message_to_all(self, capsys):
        chat = ChatRoom()
        alice = User("Alice")
        bob = User("Bob")
        chat.register(alice)
        chat.register(bob)
        alice.send("¡Hola Bob!")
        captured = capsys.readouterr()
        # Bob debe recibir el mensaje, Alice no
        assert "Bob recibe de Alice: ¡Hola Bob!" in captured.out
        assert "Alice recibe de" not in captured.out

    def test_user_send_without_chatroom(self, capsys):
        alice = User("Alice")
        alice.send("¿Hay alguien ahí?")
        captured = capsys.readouterr()
        assert "Alice no está en ninguna sala." in captured.out

    def test_multiple_users_receive_messages(self, capsys):
        chat = ChatRoom()
        alice = User("Alice")
        bob = User("Bob")
        carol = User("Carol")
        chat.register(alice)
        chat.register(bob)
        chat.register(carol)
        bob.send("¡Buenos días!")
        captured = capsys.readouterr()
        assert "Alice recibe de Bob: ¡Buenos días!" in captured.out
        assert "Carol recibe de Bob: ¡Buenos días!" in captured.out
        assert "Bob recibe de" not in captured.out