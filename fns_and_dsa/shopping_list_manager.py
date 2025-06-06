def display_menu():
  print ("Shopping List Manager")
  print ("1. Add Item")
  print ("2. Remove Item")
  print ("3. View List")
  print ("4. Exit")
shopping_list = []
while true:
  display_menu()
  choice = input("Enter your choice:")
  if choice == "1":
    item_name = input("Type item to add:")
    shopping_list.append(item_name)
  elif choice == "2":
    item_name = input("Type item to remove:")
    if item_name in shopping_list:
      shopping_list.remove(item_name)
    else:
      print("Item entered is not in the shopping list")
  elif choice == "3":
    print (shopping_list)
  elif choice == "4":
    print ("Goodbye")
    break
  else:
    print("You have entered an invalid choice, try again:")
    
  
  
  
