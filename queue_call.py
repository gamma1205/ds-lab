call_queue=[]
def add_call():
    customerID=input("Enter customer ID:")
    callTime=input("Enter call time (in minutes)")
    call=(customerID,callTime)
    call_queue.append(call)
    print(f"Your customer id:{customerID}, and call time{callTime}")
    
def answer_call():
    if len(call_queue)==0:
        print("NO call found")
    else:
        call=call_queue.pop(0)
        print(f"Answer call is {call[0]} and call time is {call[1]}")
def viewQueue():
    if len(call_queue)==0:
        print("NO call found")
    else:
        print("Answering call")
        for i in range(len(call_queue)):
            print(f"{i+1} customer id:{call_queue[i][0]} and call time :{call_queue[i][1]}")

def isQueueEmpty():
    if len(call_queue)==0:
        print("NO call found")
    else:
        print(f"Queue is not empty.Total calls in queue:{len(call_queue)}")
        
while True:
    print("1.Add call")
    print("2.Answer call")
    print("3.view Queue")
    print("4.Check if queue is empty")
    print("5.Exit")
    
    choice=input("Enter your choice")
    
    if choice=="1":
        add_call()
    elif choice=="2":
        answer_call()
    elif choice=="3":
        viewQueue()
    elif choice=="4":
        isQueueEmpty()
    elif choice=="5":
        print("Exiting...")
    else:
        print("Invalid choice")
