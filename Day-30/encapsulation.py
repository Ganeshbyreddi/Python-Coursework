class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)    

Viswa = Instagram('Viswa','Viswa@123')
Viswa.display()
print(Viswa.username)
print(Viswa.getpassword())
print(Viswa.accesspost)

Viswa.username = 'cherry'
Viswa.setpassword("cherry@123")
Viswa.accesspost = "sunrise.png"
Viswa.accesspost = "beach.png"
Viswa.accesspost = "forest.png"

print(Viswa.username)
print(Viswa.getpassword())
print(Viswa.accesspost)




       