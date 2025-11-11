class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # each index holds a list (chain)

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print("Value updated for existing key!")
                return
        self.table[index].append([key, value])
        

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Key {key} found with Value: {pair[1]}")
                return
        print("Key not found in hash table.")

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print("Key deleted successfully!")
                return
        print("Key not found. Cannot delete.")

    # Display entire hash table
    def display(self):
        print("\nHash Table State:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

hash_table = HashTable()

while True:
    print("\n====== HASH TABLE OPERATIONS ======")
    print("1. Insert Key-Value")
    print("2. Search by Key")
    print("3. Delete by Key")
    print("4. Display Table")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter key (integer): "))
        value = input("Enter value: ")
        hash_table.insert(key, value)

    elif choice == '2':
        key = int(input("Enter key to search: "))
        hash_table.search(key)

    elif choice == '3':
        key = int(input("Enter key to delete: "))
        hash_table.delete(key)

    elif choice == '4':
        hash_table.display()

    elif choice == '5':
        print("Exiting program... ")
        break

    else:
        print("Invalid choice! Try again.")
