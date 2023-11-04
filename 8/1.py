class Person:
    def __init__(self, h, w):
        self.w = weight
        self.h = height

    def print_info(self):
        print(f"Height : {height} cm")
        print(f"Weight : {weight} kg")
        print(f"BMI : {weight/((height/100)**2):.2f}")

height,weight = map(int,input().split())
p1 = Person(h=height,w=weight)
p1.print_info()