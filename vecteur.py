class V2:
    _count = 0

    def __init__(self, X, Y):
        self.__X = X
        self.__Y = Y
        V2._count += 1

    def getX(self) :
        return self.__X
    def getY(self) :
        return self.__Y

    def setX(self,X) :
        self.__X = X
    def setY(self,Y) :
        self.__Y = Y
    
    def out(self) :
        print (f"X = {(self.getX())}")
        print (f"Y = {(self.getY())}\n")
    
    def ex(self,V2) :
        X1,Y1 = self.getX() , self.getY()
        X2,Y2 = V2.getX() , V2.getY()

        if (X1==X2) and (Y1==Y2) :
            return True
        else:
            return False
    
    def Norme(self) :
           return (((self.__X)**2+ (self.__Y)**2))**0.5

class V3(V2):
    def __init__(self, X, Y, Z):
        super().__init__(X, Y)
        self.__Z = Z

    def getZ(self):
        return self.__Z

    def setZ(self, Z):
        self.__Z = Z

    def out(self):
        print(f"X = {self.getX()}")
        print(f"Y = {self.getY()}")
        print(f"Z = {self.getZ()}\n")

    def ex(self, new):
        X2, Y2, Z2 = self.getX(), self.getY(), self.getZ()
        X3, Y3, Z3 = new.getX(), new.getY(), new.getZ()

        return X2 == X3 and Y2 == Y3 and Z2 == Z3

    def Norme(self):
        return (((self.getX()) ** 2 + (self.getY()) ** 2 + (self.getZ()) ** 2)) ** 0.5
