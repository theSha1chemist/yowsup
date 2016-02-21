from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
from yowsup.layers.protocol_receipts.protocolentities  import OutgoingReceiptProtocolEntity
from yowsup.layers.protocol_acks.protocolentities      import OutgoingAckProtocolEntity

import modules
import os

#########################################################################
# begin stolen code for listing possible functions in the modules directory. 
# The idea is any new function put in the modules directory will get picked up here...
#########################################################################
def module_names(package):
    folder = os.path.split(package.__file__)[0]
    for name in os.listdir(folder):
        if name.endswith(".py") and not name.startswith("__"):
            yield name[:-3]


def import_submodules(package):
    names = list(module_names(package))
    m = __import__(package.__name__, globals(), locals(), names, -1)
    return dict((name, getattr(m, name)) for name in names)
#########################################################################
#  end stolen code 
#########################################################################

def possible_commands():
    commands = import_submodules(modules)
    return commands.keys()


class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        # self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        cmds = possible_commands()
        message = messageProtocolEntity.getBody()
        receipt = OutgoingReceiptProtocolEntity(messageProtocolEntity.getId(), messageProtocolEntity.getFrom(), 'read', messageProtocolEntity.getParticipant())

        if message[0] == "!": 
           #  self.response(messageProtocolEntity)
            command = message[1:].split(" ")
            if command[0] in cmds:
                query = ' '.join(command[1:])
                print query
                function = "modules.%s.%s('%s')" % (command[0], command[0], query) 
                print function
                try:
                    reply  = eval(function)
                except Exception, e:
                    reply = e
                    pass

            else:
                reply  = "Command not found. Try: \n!%s" % ('\n!'.join(cmds))

            outgoingMessageProtocolEntity = TextMessageProtocolEntity(reply, to = messageProtocolEntity.getFrom())
            self.toLower(receipt)
            self.toLower(outgoingMessageProtocolEntity)


        
        print("Sending %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))


    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
