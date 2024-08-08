class LinearSearch:
    def search(self):
        key = int(input("Enter the element \n"))

        for i in range(len(a)):
            if a[i] == key:
                f=f"Found {key} at {i}"
                return f
            else:
                continue

        return False

a = [1, 3, 4, 5, 6, 8, 9, 10]
l=LinearSearch()
print(l.search())








