## Different sorting algorythm with graph ##

#//imports\\#

import numpy as np
import time 
import matplotlib.pyplot as plt 

#//defining functions\\#

#---linear search ---#
def linearsearch(a,k):
    n = len(a)
    for i in range(n):
        if a[i] == k:
            return  i + 1
    return -1
        

#---bubble sort ---#
def bubblesort(a):
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    

#---Selection sort ---#
def selectionsort(a):
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


#--binary search ---#
def binarysearch(a,k):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == k:
            return mid
        elif  k < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


#//Graphs\\#

#--graph for bubble sort--#
def graph_b():
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        bubblesort(a)
        end = time.time()
        times.append(end - start)
    print("Sorted in", end - start, " seconds")

    elements = np.array([i * 100 for i in range(1,20)])
    plt.plot(elements,times,label = "Bubble sort")
    plt.legend()
    ansg = input("do you want to save the graph?(yes/no):\n")
    if ansg == "yes":
        plt.savefig("bubble sort graph.png")
    plt.tight_layout()
    plt.show()

#--graph for selection sort--#
def graph_s():
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        selectionsort(a)
        end = time.time()
        times.append(end - start)
    print("Sorted in", end - start, " seconds")
    
    elements = np.array([i * 100 for i in range(1,20)])
    plt.plot(elements,times,label = "Selection sort")
    plt.legend()
    ansg = input("do you want to save the graph?(yes/no):\n")
    if ansg == "yes":
        plt.savefig("selection sort graph.png")
    plt.tight_layout()
    plt.show()

#--graph for linear search--#
def graph_l():
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(1000, size = i * 1000)
        linearsearch(a,1)
        end = time.time()
        times.append(end - start)
    print("Sorted in", end - start, " seconds")
    
    elements = np.array([i * 100 for i in range(1,20)])
    plt.plot(elements,times,label = "liner search")
    plt.grid()
    plt.legend()
    ansg = input("do you want to save the graph?(yes/no):\n")
    if ansg == "yes":
        plt.savefig("linear search graph.png")
    plt.tight_layout()
    plt.show()

#--Graph for all--#
def graph_a():
    times1 = list()
    for i in range(1,10):
        start = time.time()
        a = np.random.randint(1000, size = i * 1000)
        linearsearch(a,1)
        end = time.time()
        times1.append(end - start)
    print("lineat search in", end - start, " seconds")
#----------------------------------------------------------------#
    times2 = list()
    for j in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = j * 100)
        bubblesort(a)
        end = time.time()
        times2.append(end - start)
    print("bubble Sorted in", end - start, " seconds")
#----------------------------------------------------------------#
    times3 = list()
    for k in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = k * 100)
        selectionsort(a)
        end = time.time()
        times3.append(end - start)
    print("selection Sorted in", end - start, " seconds")
#----------------------------------------------------------------#
    times4 = list()
    a.sort()
    for k in range(1,20):
        start = time.time()
        a = np.random.randint(1000, size = k * 1000)
        binarysearch(a,1)
        end = time.time()
        times4.append(end - start)
    print("selection Sorted in", end - start, " seconds")
#----------------------------------------------------------------#
    elements1 = np.array([i * 100 for i in range(1,10)])
    elements2 = np.array([i * 100 for i in range(1,20)])
    elements3 = np.array([i * 200 for i in range(1,20)])
    elements4 = np.array([i * 200 for i in range(1,20)])
#----------------------------------------------------------------#
    ax = plt.subplot(2,2,1)
    ax.set_title("linear search",fontsize=10)
    
    ax1 = plt.subplot(2,2,2)
    ax1.set_title("Bubble sort",fontsize=10)
    
    ax2 = plt.subplot(2,2,3)
    ax2.set_title("Selection sort",fontsize=10)
    
    ax3 = plt.subplot(2,2,4)
    ax3.set_title("Selection sort",fontsize=10)
    
    ax.plot(elements1,times1,label = "Linear search")
    ax1.plot(elements2,times2,label = "Bubble sort")
    ax2.plot(elements3,times3,label = "Selection sort")
    ax3.plot(elements4,times4,label = "binary search")
    
    ax.legend()
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ansg = input("do you want to save the graph?(yes/no):\n")
    plt.tight_layout()
    if ansg == "yes":
        plt.savefig("all in one graph.png")
    plt.show()
#----------------------------------------------------------------#


# //main code\\*


#---randdom array generation---#
#----------------------------------------------------------------#
while True:
    a = np.random.randint(100, size = 20)
    print("\n\nOriginal list", a)
    sort = int(input("\n\nSelect sorting methord \n\n 1 | Bublesort \n 2 | Selectionsort\n 3 | Linear search \n 4 | Use all sorting options \n\nchoice:"))
#----------------------------------------------------------------#
#---sorting options selection---#
    match sort:
            #---Bubble sort case---#
            case 1:
                    print("\nBubble sort")
                    bubblesort(a)
                    print(a)
                    print("Generating Graph.....")
                    graph_b()
            
            #---Selection sort case---#
            case 2:
                    print("\nSelection sort")
                    selectionsort(a)
                    print(a)
                    print("Generating Graph")
                    graph_s()
            
            #---Linear search case---#       
            case 3:
                    print("\nlinear search"),print(a)
                    ls = linearsearch(a,k = int(input("Enter the number to be searched: ")))
                    print(ls)
                    if ls == -1:
                        print("search unsucessful ")
                    else:
                        pass
                    print("Generating Graph.....")
                    graph_l()
            
            #---All sorting case---#        
            case 4:
                    print("\nBubble sort")
                    bubblesort(a),print(a)
                    print("\nSelection sort")
                    selectionsort(a),print(a)
                    print("\nlinear search"),print(a)
                    ls = linearsearch(a,k = int(input("Enter the number to be searched: ")))
                    print(ls)
                    if ls == -1:
                        print("search unsucessful ")
                    else:
                        pass
                    print("\nbinary search"),print(a)
                    bs = binarysearch(a,k = int(input("Enter the number to be searched: ")))
                    if bs == -1:
                        print("search unsucessful ")
                    else:
                        print("Element fount at" ,bs)
                    print("Generating Graph.....")
                    graph_a()
            
            #---default case---#
            case default:
                    print("invalid option")
    #----------------------------------------------------------------#


