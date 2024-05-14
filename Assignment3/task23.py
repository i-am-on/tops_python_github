class Rect:
    def area(self,width,length):

        self.w=width
        self.l=length

        a=self.w*self.l

        print("Area of Rectangle is : ",a)

R1=Rect()
R1.area(100,30)
