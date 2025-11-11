event_queue=[]
def add_event():
    event=input("Add event name:")
    event_queue.append(event)
    print(f"Event {event} added successfully")
    
def process_event():
    if len(event_queue)==0:
        print("NO event")
    else:
        event=event_queue.pop(0)
        print(f"Processing an event:{event}")
        
def display_event():
    if len(event_queue)==0:
        print("NO event")
    else:
        print("Pending event:")
        for i in range(len(event_queue)):
            print(f"{i+1}.{event_queue[i]}")

def cancel_event():
    if len(event_queue)==0:
        print("NO event")
    else:
        event = input("Enter event name to cancel: ")
        if event in event_queue:
            event_queue.remove(event)
            print(f"event {event} has been cancelled")
        else:
            print(f"event {event} not found")
            
while True:
    print("\n====== EVENT PROCESSING MENU ======")
    print("1. Add an Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")
    print("===================================")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_event()
    elif choice == '2':
        process_event()
    elif choice == '3':
        display_event()
    elif choice == '4':
        cancel_event()
    elif choice == '5':
        print("\nExiting Event Processing System...")
        break
    else:
        print("Invalid choice! Please enter 1 to 5.")
