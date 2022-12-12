def romanToInt():

    romanstring = input("Write a string of roman numerals: ")

    values = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    prev_num = 0
    res = []

    for i,j in enumerate(romanstring):
        curr_num = values[j]
        if prev_num < curr_num:
            res.append(curr_num - (prev_num*2))
        else: # prev_num == 0, curr_num > prev_num, curr_num == prev_num
            res.append(curr_num)
        prev_num = curr_num
    return f"{romanstring} is: {sum(res)}"


print(romanToInt())