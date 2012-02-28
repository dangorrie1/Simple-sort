list1 = []
x = 0

count = 0

limit = int(input("How many numbers would you like to sort?"))

while x < limit:
    if x == 0:
        num = float(input("Please input your numbers"))
        list1.append(num)
        x = x + 1
    else:
        num = float(input())
        list1.append(num)
        x = x + 1


while count < limit:
    n = 1
    while n < limit:
        x = list1[n-1] - list1[n]
        if x < 0:
            pass
        else:
            temp = list1[n]
            list1.remove(temp)
            list1.insert(n-1, temp)
                     
        n = n+1
    count = count + 1
    
print(list1)
    
    
