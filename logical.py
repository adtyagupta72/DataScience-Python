for count in range(1,8):
    a=""
    for count_1 in range(count,7):
        a=a+" "
    # if(count==1):
    #     a=a+"*"
    # else:
    for count_2 in range(0,(count*2-1)):
        a=a+"*"
    print(a)