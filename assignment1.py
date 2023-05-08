class rectangle:
    def __init__(self, len, wid):

        self.length=len
        self.width=wid
    def change_dim(self,len,wid):
        self.length=len
        self.width=wid
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def report_dimensions(self):
        print("the length is",self.length)
        print("the width is",self.width)

rectu=rectangle(2,3)
print("the area is ",rectu.area())
print("the perimeter is",rectu.perimeter())
print("******************************")
print("the dimensions are")
rectu.report_dimensions()
print("*******************************")
print("after using the change dimensions function")
rectu.change_dim(3,4)
rectu.report_dimensions()

