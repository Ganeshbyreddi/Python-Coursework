#Single inheritance
class whatsappV1:
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - V1 {self.name}!")
    def messaging(self):
        print("YOu can send messages")

class whatsappV2(whatsappV1):
    def __init__(self,name):
        self.name = name
        print(f"Welcome to the whatsapp - V2 {self.name}!")
    def calls(self):
        print("You can audio and video calls")

krishna = whatsappV1('krishna')
krishna.messaging()

sai = whatsappV2('sai')
sai.messaging()
sai.calls()