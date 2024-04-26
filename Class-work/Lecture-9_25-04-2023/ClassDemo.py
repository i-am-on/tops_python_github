class Student:

    def getData(self,fname,lname):
        print("getData Called")
        self.f = fname
        self.l = lname

    def putData(self):
        print("putData Called")
        print("First Name : ",self.f)
        print("Last Name : ",self.l)

s1=Student()
s1.getData("Nirmal","Oza")
s1.putData()
