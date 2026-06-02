print("=== Tool Tracker ===")
name = input("Enter your name: ")
tool_type = input("type of tools you are interested in: ") 
print(f"Welcome {name}, Select one of the options below")
tools = []
while True:
  print("1. Add Tool")
  print("2. View Tools")
  print("3. Search Tool")
  print("4. Remove Tool")
  print("5. Save Tools")
  print("6. Load Tools")
  print("7. Exit")
  print("8. Update Tool")
  choice = input("Enter you choice: ")
  print("Proccesing...")

  if choice == "1":
      tool_name = input("Enter tool to add: ")
      tool_category = input("Enter tool category: ")
      tool_level = input("Enter level: ")

      tool = {
          "Name" : tool_name ,
          "Category" : tool_category ,
          "Level" : tool_level 
      }

      tools.append(tool)
      print("Tool added successfully!")
      print("Total tools: ", len(tools))

  elif choice == "2":
   if len(tools) == 0:
      print("No tools found")
   else:
    for tool in tools:
      print("Name: " , tool["Name"])
      print("Category: " , tool["Category"])
      print("Level: " , tool["Level"])
      print()

  elif choice == "3":
    search = input("Enter tool to search: ")
    found = False
    for tool in tools:
      if tool["Name"] == search:
        found = True
        print("\nTool found")
        print("Name: ", tool["Name"])
        print("Category: " , tool["Category"])
        print("Level: " , tool["Level"])

    if not found:
          print("Tool not found")

  elif choice == "4":
    search = input("Enter tool to remove: ")
    found = False
    for tool in tools:
      if tool["Name"] == search:
        found = True
        tools.remove(tool)
        print("Tool removed successfully")
    if not found:
      print("Tool not found")
 
  elif choice == "5":
    file = open("tools.txt" , "w")
    for tool in tools: 
      file.write(tool["Name"] + "," + tool["Category"] + "," + tool["Level"] + "\n")
    print("Tool saved successfully")
    file.close()

  elif choice == "6":
    tools.clear()
    file = open("tools.txt" , "r")
    for line in file:
      data = line.strip().split(",")
      tool = {
          "Name": data[0],
          "Category": data[1],
          "Level": data[2]
      }
      tools.append(tool)
    print("Loading Successful")
    print("Tools loaded:", len(tools))
    file.close()
  elif choice == "7":
    print("Exiting program...\nGood bye 👋")
    break
  elif choice == "8":
    tool_update = input("Enter tool to update: ")
    found = False
    for tool in tools:
      if tool["Name"] == tool_update:
        found = True
        new_category = input("Enter new category: ")
        new_level = input("Enter new level: ")
    tool["Category"] = new_category
    tool["Level"] = new_level
    tools.append(tool)
    print("Tool updated successfully!")
    if not found:
      print("Tool not found")
