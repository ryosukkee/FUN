def variencethreshhold(*kwargs):
    arr = []
    count = 0
    for i in kwargs:
        arr.append(i)
        count += 1

    mean = sum(arr)/count

    arr2 = []
    count2 = 0
    
    for i in kwargs:
        arr2.append((i-mean)**2)
        count2 += 1

        varience = sum(arr2)/count2

    print(varience)

variencethreshhold(2,4,6,8)