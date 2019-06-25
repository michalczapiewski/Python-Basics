num1 = input("Num1:")
num2 = input("Num2:")
num3 = input("Num3:")

def max_num():
    if  num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    elif num1==num2 or num1==num3:
        print("Sa 2 te same cyfry")
    elif num1 == num2 and num2 == num3:
        print("Sa 3 te same cyfry")
    else:
        return num3

print(max_num())