# baozi
# print("hello")
a = [2,4,1,5,67,3,7]
# print(a)
for i in range(7):
    print(i)
    j = i+1
    while(j < 7):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
        j = j + 1
print(a)
# print("hello")


