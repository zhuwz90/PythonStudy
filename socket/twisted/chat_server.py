from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


class Chat(LineReceiver):
    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self.sendLine(b"What's your name?")

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine(b"Name taken, please choose another.")
            return
        self.sendLine(b"Welcome, %s!" % (name,))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = b"[%s] %s" % (self.name, message)
        for name, protocol in self.users.items():
            # if protocol != self:
            protocol.sendLine(message)


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}  # maps user names to Chat instances

    def buildProtocol(self, addr):
        print("Chat service for %s" % str(addr))
        return Chat(self.users)

    def startFactory(self):
        print('Chat server started')

    def stopFactory(self):
        print('Chat server stopped')


reactor.listenTCP(9091, ChatFactory())
reactor.run()
