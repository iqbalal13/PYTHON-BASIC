fruits = ["apple", "banana", "cherry"]

while True:
    try:
        search = input("Enter a fruit to search for (or type 'exit' to quit): ")
        
        if search.lower() == 'exit':
            break
        
        if search in fruits:
            print(f"{search} is in the list.")
        else:
            print(f"{search} is not in the list.")
    except Exception as e:
        print(f"An error occurred: {e}")