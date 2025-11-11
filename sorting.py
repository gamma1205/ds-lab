def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[j],arr[min_index]=arr[min_index],arr[j]
    return arr
    
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
    
def display_top_five(sorted_salaries):
    print("\nTop 5 highest salaries")
    for rank,salary in enumerate(sorted_salaries[-5:][::-1],start=1):
        print(f"{rank}.{salary:.2f}")
n=int(input("no of employees:"))
salaries=[]
for i in range(n):
    sal=int(input("Enter salary of employee"))
    salaries.append(sal)
    
while True:
    print("1.Sort using selection sort")
    print("2.sort using bubble sort")
    print("3.Exit")
    
    choice=input("Enter your choice:")
    
    if choice=="1":
        sorted_salaries=selection_sort(salaries.copy())
        print("\nSorted salaries are:",sorted_salaries)
        display_top_five(sorted_salaries)
         
    elif choice=="2":
        sorted_salaries=bubble_sort(salaries.copy())
        print("\nSorted salaries are:",sorted_salaries)
        display_top_five(sorted_salaries)
        
    elif choice=="3":
        print("Exiting..")
    
    else:
        print("invalid choice")
