def Array_Create(arr):
    print(arr)

def access(arr):
    i = int(input("Enter index."))
    print(arr[i])

def insert_in_Array(arr):
    i = int(input("Enter index Where you want insert. "))
    element = input("Enter Items . ")
    arr.insert(i,element)
    print(arr)
def reverse_array_element(arr):
    arr.reverse()
    print(arr)
def remove_list(arr):
    element = input("Enter Element in Array for remove. ")
    arr.remove(element)
    print(arr)

if __name__ == '__main__':
    arr = []
    n = int(input("Enter array size"))
    for i in range(0,n):
        l = input("Enter Element.")
        arr.append(l)
    Array_Create(arr)
    access(arr)
    insert_in_Array(arr)
    reverse_array_element(arr)
    remove_list(arr)
# Array







