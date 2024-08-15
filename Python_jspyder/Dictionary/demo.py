

a=[19,9,2,8,20,1]

for i in range(len(a)):

    mini=i

    for j in range(i+1, len(a)):

        if a[mini]>a[j]:
            mini=j

        a[mini], a[i] = a[i], a[mini]

    print(a)
