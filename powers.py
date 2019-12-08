# coding = utf-8 
def power(x, n):
    if x == 0:
        return None
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
print(power(3, 3))