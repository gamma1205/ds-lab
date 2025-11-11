def input_customer_ids():
    n=int(input("Enter no. of customers"))
    ids=[]
    for i in range(n):
        cid=int(input("Enter customer id"))
        ids.append(cid)
    return ids
    
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
    
def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    return -1
            
def display_ids(arr):
    print("current customer ids are:",arr)
    
customer_ids=[]
while True:
    print("1.Input customer id")
    print("2.Display customer id")
    print("3.Linear search")
    print("4.Binary search")
    print("5.Exit")
    
    choice=input("Enter your choice:")
    
    if choice=="1":
        customer_ids=input_customer_ids()
        print("id added successfully")
    elif choice=="2":
        if len(customer_ids)==0:
            print("No id to display")
        else:
            display_ids(customer_ids)
    elif choice=="3":
        if len(customer_ids)==0:
            print("No id to display")
        else:
            key=int(input("enter id first"))
            pos=linear_search(customer_ids,key)
            if pos!=-1:
                print(f"Linear search customer id {key} found at position{pos}")
            else:
                print(f"Linear search customer id {key} not found")
    elif choice=="4":
        
        if len(customer_ids)==0:
            print("No id to display")
        else:
            key=int(input("enter id first"))
            sorted_list=sorted(customer_ids)
            pos=binary_search(sorted_list,key)
            if pos!=-1:
                print(f"binary search customer id {key} found at position{pos}")
            else:
                print(f"Linear search customer id{key} not found0")
                
    elif choice=="5":
        print("Exiting..")
        break
    else:
        print("invalid choice")
