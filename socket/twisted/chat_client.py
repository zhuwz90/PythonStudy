import sys
import threading

from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from twisted.python import log

log.startLogging(sys.stdout)

def send_msg(cf):
    while True:
        msg = input(">")
        if msg == 'quit':
            break
        cf.protocol.sendLine(msg.encode('utf-8'))


class ChatClient(LineReceiver):
    def connectionMade(self):
        log.msg("New connection", self.transport.getPeer())

    def connectionLost(self, reason):
        print("Connection lost")

    def lineReceived(self, line):
        print(line.decode('utf-8'))


class ChatFactory(ClientFactory):
    def __init__(self):
        self.protocol = ChatClient()
        t = threading.Thread(target=send_msg, args=(self,))
        t.start()

    def buildProtocol(self, addr):
        return self.protocol

    def startFactory(self):
        print("Enter chat room")

    def stopFactory(self):
        print("Exit chat room")


reactor.connectTCP('localhost', 9091, ChatFactory())
reactor.run()
