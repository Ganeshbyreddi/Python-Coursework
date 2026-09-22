'''class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2:
    def extramessages(self):
        print("You can add emojis, stickers and gifts")        

class whatsappv3(whatsappv1,whatsappv2):
    def calls(self):
        print("You can audio and video calls")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can add the status for 24 hours")        

a = whatsappv1()
a.messaging()

b = whatsappv2()
b.extramessages()

c = whatsappv3()
c.messaging()
c.extramessages()
c.calls()

d = whatsappv4()
d.messaging()
d.extramessages()
d.calls()
d.status()

'''



'''class whatsappv1:
    def status(self):
        print("you can add images and videos")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can add music and stickers")

class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("You can like and you can add reaction")

a = whatsappv3()
a.status()'''


'''class whatsappv1:
    def status(self):
        print("you can add images and videos")

class whatsappv2:
    def status(self):
        print("You can add music and stickers")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can like and you can add reaction")

a = whatsappv3()
a.status()'''


