def rise_to_power(base_num,pow_num):
    result = 1
    for var in range (pow_num):
        result = result * base_num
        print(var, result)
    return result

print(rise_to_power(2,8))