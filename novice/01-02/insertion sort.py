list = [12, 23, 34, 52, 8, 44, 43, 45, 78]
for i in range(1,len(list)):
    currentvalue=list[i]
    possition=i
    while(possition>0 and list[possition-1]>currentvalue):
        list[possition]=list[possition-1]
        possition=possition-1
    list[possition]=currentvalue
    print(list)
