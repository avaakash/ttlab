def series(n): 
    sum = 0
    j = 1
    for i in range(1, n + 1): 
        sum = sum + j 
        j = (j * 10) + 1
    return sum
          

n = int(input("Enter number of terms: "))

print(series(n)) 