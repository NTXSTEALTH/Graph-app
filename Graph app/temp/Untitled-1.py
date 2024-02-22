# def bsort(a):
#     n = len(a)
#     for i in range(n-1):
#       for j in range(n-1-i):
#           if a[j] > a[j +1]:
#               a[j], a[j+1] = a[j+1], a[j]

# def ssort(a):
#     n = len(a)
#     for i in range(n):
#         min = i
#         for j in range(i+1,n):
#             if a[j] < a[min]:
#                 min = j
#         a[i], a[min] = a[min], a[i]

def lsearch(a,key):
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i+1
    return -1
        
a =[10,53,69,85,46,932,65,48,52,63,79,52,69,420,89,68,54]
#bsort(a)
#ssort(a)
l = lsearch(a,int(input("enter the key:")))
if l == -1:
    print(f"search for element was unsucessfull")
else:
    print(f"yes yes yes found at {l}")
#print(a)