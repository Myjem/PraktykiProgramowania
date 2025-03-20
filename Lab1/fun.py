def Add(a):
    a = a.replace("\n", ",")
    num_list = a.split(",")
    sum = 0
    for num in num_list:
        if num:
            sum = sum + int(num)
    return sum


