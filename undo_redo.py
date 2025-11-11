undo_stack=[]
redo_stack=[]
document=""

def make_change(change):
    global document
    undo_stack.append(document)
    document+=change
    redo_stack.clear()
    print("Changes made:",change)
    
def undo_action():
    global document
    if undo_stack:
        redo_stack.append(document)
        document=undo_stack.pop()
        print("Undo performed")
    else:
        print("Not performed")
        
def redo_action():
    global document
    if redo_stack:
        undo_stack.append(document)
        document=redo_stack.pop()
        print("redu performed")
    else:
        print("Not performed")
        
def display_document():
    print("Current document state",document if document else "(empty)")
    
while True:
    print("1.Make a change")
    print("2.Undo last change")
    print("3.Redo last change")
    print("4.Display document")
    print("5.Exit")
    
    choice=input("enter your choice:")
    
    if choice=="1":
        change=input("Enter text to add")
        make_change(change)
    elif choice=="2":
        undo_action()
    elif choice=="3":
        redo_action()
    elif choice=="4":
        display_document()
    elif choice=="5":
        print("Exiting..")
    else:
        print("Invalid choice")
