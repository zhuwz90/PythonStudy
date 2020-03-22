from twisted.internet import protocol, reactor

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b"Hello, Twisted!")

    def dataReceived(self, data):
        print("Server response: ", data)
        #self.transport.loseConnection()

    def connectionLost(self, reason):
        print("Connection lost")

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - byebye!")
        reactor.stop()

reactor.connectTCP("localhost", 9091, EchoFactory())
reactor.run()