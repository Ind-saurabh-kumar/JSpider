class CharSearch:

    def linearSearch(self, arr, key):

        for i in range(len(arr)):
            arr[i]=arr[i].lower()
            if arr[i] == key:
                return i
            else:
                continue
        return False


arr=['k', 'a', 'B', 'c', 'd', 'E', 'f', 'g', 'h']
key=input("Enter the character \n")
key=key.lower()

l=CharSearch()
res=l.linearSearch(arr, key)

if res== False:
    print("Not Found")
else:
    print(f"{key} is found at the index {res}")

