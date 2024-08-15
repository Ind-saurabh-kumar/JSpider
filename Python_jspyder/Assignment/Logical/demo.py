a = [1, 12, 11, 45, 2]
l = len(a)

# Bubble sort algorithm
for i in range(l):
    for j in range(0, l-i-1):
        if a[j] > a[j+1]:
            # Swap if the element found is greater than the next element
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            # a[j], a[j+1] = a[j+1], a[j]

print(a)