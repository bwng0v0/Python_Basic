class Time:
    def __init__(self,sec):
        self.s = sec

    def print_info(self):
        tmp = self.s
        print(f"Hour : {tmp//3600}")
        tmp %= 3600
        print(f"Minute : {tmp//60}")
        tmp %= 60
        print(f"Second : {tmp}")

second = int(input())
t1 = Time(sec=second)
t1.print_info()
