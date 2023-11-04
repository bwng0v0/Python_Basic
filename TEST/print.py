my_int = int(input())
my_float = float(input())
my_str = input()

# print 연습

print(f"my int : {my_int}, my float : {my_float:.2f}, my str : {my_str}")
print("my int : {}, my float : {:.2f}, my str : {}".format(my_int , my_float , my_str))
print("my int : %d, my float : %.2f, my str : %s" % (my_int , my_float , my_str))