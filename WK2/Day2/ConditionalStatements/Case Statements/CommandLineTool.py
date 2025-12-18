command = input("Enter action CREATE/READ/UPDATE/LIST")
match command.strip().lower():
 case "create": print("Creating new file...")
 case "read": print("Reading file contents...")
 case "update": print("Updating file...")
 case "delete": print("Deleting file...")
 case "list": print("Files: file1.txt, file2.py")
 case _ if command.startswith("help"): print("Available: create, read...")
 case _: print("Unknown command. Type 'help'")
