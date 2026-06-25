# for count in range(1,8):
#     a=""
#     for count_1 in range(count,7):
#         a=a+" "
#     # if(count==1):
#     #     a=a+"*"
#     # else:
#     for count_2 in range(0,(count*2-1)):
#         a=a+"*"
#     print(a)

for count in range(1,8):
    a=""
    for count_1 in range(1,7):
        # a=a+"*"
        if(count == 1 or count == 7):
            a=a+"*"
        elif(count_1 > 1 and count_1 < 6):
            a=a+" "
        elif(count != 1 and count != 7 and (count_1 == 6 or count_1 == 1)):
            a=a+"*"
    print(a)

'''
count       1   2
count_1     1   1
op          ******
            *
'''