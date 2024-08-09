class CharSearch:
    def linearSearch(self, arr, key):
        for i in range(len(arr)):
            arr[i]=arr[i].lower()
            if arr[i] == key:
                return i
            else:
                continue
        print("second return")
        return False


arr=['Z', 't', 'B', 'c', 'd', 'E', 'f', 'g', 'h']
key=input("Enter the character \n")
key=key.lower()

l=CharSearch()
res=l.linearSearch(arr, key)

if res == False:
    print("Element Not Found")
else:
    print(f"{key} is found at the index {res}")

