from processor import main

# Calls main function from processor.py to return the dictionary.
data = main()
print(data)

# Adding all IDs to a list
id_list = []

for entry in data["entity"]:
    for id in entry:
        print(id)
        id.append(id_list)
print(id_list)




