#Graph App

#---IMPORTS---#
import customtkinter as ctk
import tkinter as tkk
import time
import numpy as np
import matplotlib.pyplot as plt

#DECLARING VARIABLES---#
savegraph = False
selection = "Bubble Sort "

# --- DEFINING FUNCTIONS --- #
def mains(choice):
    global selection
    match choice:
        case "Bubble Sort ":
                selection = choice
            
        case "Linear Search ":
                selection = choice
            
        case "Selection sort ":
                selection = choice
        
        case "Insertion sort ":
                selection = choice
                
        case "Binary search ":
                selection = choice
            
        case "Select All(seperated) ":
                selection = choice
                
        case "Selected all(Sorting) ":
                selection = choice

def graphsavestate(choice):
    global savegraph
    match choice:
        case "Yes":
            savegraph = True
        case "No":
            savegraph = False

def testing_fun():
    print(selection)


def Confirmed():
    print(selection)
    match selection:
        case "Bubble Sort ":
                print(selection)
                graph_b()
        case "Linear Search ":
                print(selection)
                graph_l()
        case "Selection sort ":
                print(selection)
                graph_s()
        case "Insertion sort ":
                print(selection)
                graph_i()
        case "Binary search ":
                print(selection)
                graph_bi()
        case "Select All(seperated) ":
                print(selection)
                graph_a_sep()
        case "Selected all(Sorting) ":
                print(selection)
                graph_a()
                
                
                
#---GRAPH_FUNCTIONS---#

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


def insertionsort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key


#--binary search ---#
def binarysearch(a, low, high, k):
    if low <= high:
        mid = (low + high) // 2
        if a[mid] == k:
            return mid
        elif a[mid] > k:
            return binarysearch(a, k, low, mid - 1)
        else:
            return binarysearch(a, k, mid + 1, high)
    else:
        print("search unsuccessful")      
      
        
#__GRAPHS__#

#--graph for bubble sort--#
def graph_b():
    plt.close('all')
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        bubblesort(a)
        end = time.time()
        times.append(end - start)
    timer = str(end - start) + " seconds"
    label_2.configure(text = timer)
    print("Sorted in", end - start, " seconds")

    elements = np.array([i * 100 for i in range(1,20)])
    plt.plot(elements,times,label = "Bubble sort")
    plt.legend()
    print(savegraph)
    if savegraph == True:
       plt.savefig("bubble sort graph.png")
       print("graph saved")
    plt.tight_layout()
    plt.show()


#--graph for selection sort--#
def graph_s():
    plt.close('all')
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        selectionsort(a)
        end = time.time()
        times.append(end - start)
    timer = str(end - start) + " seconds"
    label_2.configure(text = timer)
    print("Sorted in", end - start, " seconds")
    
    elements = np.array([i * 100 for i in range(1,20)])
    plt.plot(elements,times,label = "Selection sort")
    plt.legend()
    print(savegraph)
    if savegraph == True:
        plt.savefig("selection sort graph.png")
    plt.tight_layout()
    plt.show()


#--Graph for insertion sort---#
def graph_i():
    plt.close('all')
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        insertionsort(a)
        end = time.time()
        times.append(end - start)
    timer = str(end - start) + " seconds"
    label_2.configure(text = timer)
    print("Sorted in", end - start, " seconds")
    
    elements = np.array([i * 100 for i in range(1,20)])
    plt.plot(elements,times,label = "insertion sort")
    plt.legend()
    print(savegraph)
    if savegraph == True:
        plt.savefig("insertion sort graph.png")
    plt.tight_layout()
    plt.show()



#--graph for linear search--#
def graph_l():
    plt.close('all')
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = i * 1000)
        linearsearch(a,1)
        end = time.time()
        times.append(end - start)
    timer = str(end - start) + " seconds"
    label_2.configure(text = timer)
    print("Sorted in", end - start, " seconds")
    
    elements = np.array([i * 1000 for i in range(1,20)])
    plt.plot(elements,times,label = "liner search")
    plt.legend()
     
    if savegraph == True:
        plt.savefig("linear search graph.png")
    plt.tight_layout()
    plt.show()


def graph_bi():
    plt.close('all')
    times = list()
    for i in range(1,20):
        start = time.time()
        a = np.random.randint(100, size = i * 1000)
        binarysearch(a,0,len(a)-1,1)
        end = time.time()
        times.append(end - start)
    timer = str(end - start) + " seconds"
    label_2.configure(text = timer)
    print("Sorted in", end - start, " seconds")
    
    elements = np.array([i * 1000 for i in range(1,20)])
    plt.plot(elements,times,label = "binary search")
    plt.legend()
     
    if savegraph == True:
        plt.savefig("binary search graph.png")
    plt.tight_layout()
    plt.show()


#---Graph for all Seperated---#
def graph_a_sep():
    plt.close('all')
    
    x = np.array([i * 1000 for i in range(1,10)])
    times1 = list()
    times2 = list()
    times3 = list()
    times4 = list()
    
    for i in range(1,10):
        
        start = time.time()
        a = np.random.randint(200, size = i * 200)
        linearsearch(a,1)
        end = time.time()
        times1.append(end - start)
        
        start = time.time()
        a = np.random.randint(200, size = i * 200)
        bubblesort(a)
        end = time.time()
        times2.append(end - start)
        
        start = time.time()
        a = np.random.randint(200, size = i * 200)
        insertionsort(a)
        end = time.time()
        times3.append(end - start)
        
        start = time.time()
        a = np.random.randint(200, size = i * 200)
        selectionsort(a)
        end = time.time()
        times4.append(end - start)
    
#----------------------------------------------------------------#
    ax = plt.subplot(2,2,1)
    ax.set_title("linear search",fontsize=10)
    
    ax1 = plt.subplot(2,2,2)
    ax1.set_title("Bubble sort",fontsize=10)
    
    ax2 = plt.subplot(2,2,3)
    ax2.set_title("Selection sort",fontsize=10)
    
    ax3 = plt.subplot(2,2,4)
    ax3.set_title("Binary sort",fontsize=10)
#----------------------------------------------------------------#  
    ax.plot(x,times1,label = "Linear search")
    ax1.plot(x,times2,label = "Bubble sort")
    ax2.plot(x,times3,label = "Selection sort")
    ax3.plot(x,times4,label = "Binary search")
#----------------------------------------------------------------# 
 
    ax.legend()
    ax1.legend()
    ax2.legend()
    ax3.legend()
     
    plt.tight_layout()
    label_2.configure(text ="Cannot Compute Time for this option")
    print(savegraph)
    if savegraph == True:
        print("graph saved")
        plt.savefig("all in one graph.png")
    plt.show()              


#---Graph for all Combined---#
def graph_a():
    plt.close('all')
    x = np.array([i * 1000 for i in range(1,10)])
    times1 = list()
    times2 = list()
    times3 = list()
    for i in range(1,10):
        
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        bubblesort(a)
        end = time.time()
        times1.append(end - start)
        
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        selectionsort(a)
        end = time.time()
        times2.append(end - start)
        
        start = time.time()
        a = np.random.randint(100, size = i * 100)
        insertionsort(a)
        end = time.time()
        times3.append(end - start)
        
    print("Insertion sorted in", end - start, " seconds")
#----------------------------------------------------------------#
    ax = plt.subplot(1,1,1)
    ax1 = plt.subplot(1,1,1)
    ax2 = plt.subplot(1,1,1)
    ax.set_title("All Graphes in one",fontsize=10)
#----------------------------------------------------------------#  
    ax.plot(x,times1,label = "Insertion sort")
    ax1.plot(x,times2,label = "Bubble sort")
    ax2.plot(x,times3,label = "Selection sort")
#----------------------------------------------------------------#   
    ax.legend()
    ax1.legend()
    ax2.legend()
     
    plt.tight_layout()
    label_2.configure(text ="Cannot Compute Time for this option")
    print(savegraph)
    if savegraph == True:
        print("graph saved")
        plt.savefig("all in one graph.png")
    plt.show()                
    

#---APP CONFIGS---#
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x500")
app.minsize(400,500)
app.maxsize(400,500)
app.title("Sorting Algorithms")
#app.iconbitmap('icon.ico')


#---Framework---#
frame_1 = ctk.CTkFrame(app,
                       width = 400,
                       height = 500,
                       bg_color = "black",
                       fg_color = "black",
                       border_width = 2,
                       border_color = "white",
                       corner_radius = 16)

frame_1.pack(anchor = tkk.CENTER,
              fill = tkk.BOTH,
              expand = True)

frame_2 = ctk.CTkFrame(frame_1,
                       width = 310,
                       height = 75,
                       fg_color= "white",
                       corner_radius = 30)

frame_2.place(relx = .5, rely = .30, anchor = tkk.CENTER)
    
                       
#---UI Elements---#
title_1 = ctk.CTkLabel(frame_1,
                       text = "Sorting Algorithms",
                       font = ("roboto", 25),
                       anchor = tkk.CENTER)

title_1.place(relx = .5,rely = .1,anchor = tkk.CENTER)


label_1 = ctk.CTkLabel(frame_2,
                       text = "Time Complexity",
                       text_color = "black",
                       font = ("Roboto Mono", 17),
                       anchor = tkk.CENTER)

label_1.place(relx = .5,rely = .15,anchor = tkk.CENTER)


label_2 = ctk.CTkLabel(frame_2,
                       text = "",
                       text_color = "black",
                       font = ("Roboto", 18),
                       anchor = tkk.CENTER)

label_2.place(relx = .5,rely = .60,anchor = tkk.CENTER)                 


label_3 = ctk.CTkLabel(frame_1,
                       text = "Select algorithm",
                       text_color = "white",
                       font = ("Roboto", 20),
                       anchor = tkk.CENTER)

label_3.place(relx = .35, rely =.50 , anchor = tkk.CENTER)


label_4 = ctk.CTkLabel(frame_1,
                       text = "Save graph",
                       text_color = "white",
                       font = ("Roboto",20),
                       anchor = tkk.CENTER)

label_4.place(relx = .30 ,rely = .65, anchor = tkk.CENTER)
            
                       
options_1 = ctk.CTkOptionMenu(frame_1,
                              height = 30,
                              width = 60,
                              font = ("Roboto", 12),
                              values = ["Bubble Sort ","Linear Search ","Selection sort ","Insertion sort ","Binary search ", "Select All(seperated) ","Selected all(Sorting) "],
                              #values = ["1","2"],
                              anchor = tkk.CENTER,
                              dynamic_resizing = True,
                              command = mains
                              )

options_1.place(relx =.75,
                rely =.50,
                anchor = tkk.CENTER)


options_2 = ctk.CTkOptionMenu(frame_1,
                              height = 30,
                              width = 60,
                              font = ("Roboto", 15),
                              values = ["No","Yes"],
                              anchor = tkk.CENTER,
                              dynamic_resizing = True,
                              command=graphsavestate
                              )

options_2.place(relx =.80, rely = .65, anchor = tkk.CENTER)


button_1 = ctk.CTkButton(frame_1,
                         text = "Confirm",
                         font = ("Roboto",20),
                         width = 80,
                         height = 40,
                         anchor = tkk.CENTER,
                         command = Confirmed
                         )

button_1.place(relx =.5, rely =.80, anchor = tkk.CENTER)


#---MAIN---#
app.mainloop()
