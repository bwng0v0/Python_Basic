class Number:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getMin(self):
        if self.x < self.y:
            return self.x
        else:
            return self.y
    def getMax(self):
        if self.x > self.y:
            return self.x
        else:
            return self.y
        
    def getGCD(self):
        a = self.x
        b = self.y
        while b > 0:
            a, b = b, a % b
            print(f"{a} {b}")
        return a

    def getLCM(self):
        return self.x*self.y//self.getGCD()

x,y = map(int,input().split())
number = Number(x=x,y=y)
print(f"Max Num : {number.getMax()}")
print(f"Min Num : {number.getMin()}")
print(f"GCD Num : {number.getGCD()}")
print(f"LCM Num : {number.getLCM()}")