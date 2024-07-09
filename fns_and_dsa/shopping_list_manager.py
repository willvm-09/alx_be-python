shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            new_item = input("Enter item to add: ")
            shopping_list.append(new_item)
            pass
        elif choice == '2':
            remove_item = input("Enter item to remove: ")
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
                else:
                    print("Item not found")
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
