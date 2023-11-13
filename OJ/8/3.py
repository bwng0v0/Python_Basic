class Student:
    def __init__(self,name,kor,eng,math,sci):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sci = sci

    def getName(self):
        return self.name

    def getTotalScore(self):
        return self.kor+self.eng+self.math+self.sci
    
    def getAvgScore(self):
        return ((self.kor+self.eng+self.math+self.sci)/4)

name = input()
kor, eng, math, sci = map(int,input().split())
s = Student(name,kor,eng,math,sci)
print(f"[{s.getName()}] Total : {s.getTotalScore()}, Average : {s.getAvgScore():.1f}")