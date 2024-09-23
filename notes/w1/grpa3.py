def odd_one(L):
    int_cnt = 0
    float_cnt = 0
    str_cnt = 0
    bool_cnt = 0

    for i in L:
        if type(i) is int:
            int_cnt += 1
        elif type(i) is float:
            float_cnt += 1
        elif type(i) is str:
            str_cnt += 1
        else:
            bool_cnt += 1
    if int_cnt == 1:
        return 'int'
    elif float_cnt == 1:
        return 'float'
    elif str_cnt == 1:
        return 'str'
    else:
        return 'bool'


print(odd_one(eval(input().strip())))
