print("--------LIST EXAMPLES--------")
list_example = [234, 20, 39, 987, 1, 96]
list_example_master = [234, 20, 39, 987, 1, 96]

#List Insert
list_example.append(2) #Inserts 2 at the end of the list
list_example.insert(0, 233) #Inserts 233 at the beginning of the list
print(f"After Insert: {list_example}")

#List Remove
list_example.remove(233) #removes 233 from the list
list_example.pop() #removes the last entry from the list
print(f"After remove: {list_example}")
if list_example == list_example_master: print("Lists match")

#List Update
list_example.sort()
print(f"After Sort: {list_example}") #sorts the list from smallest to largest

print("--------DICTIONARY EXAMPLES--------")
dict_example = {"entry_1": 1, "entry_2": {"entry_3": 2}, "entry_4": list_example, "entry_5": "something"}

#Dict Insert
dict_example["entry_6"] = 100 #creates a new entry called entry_6 and sets it equal to 100
print(f"After insert: {dict_example}")

#Dict Update
dict_2 = {"entry_6": 10, "entry_7": 200} 
dict_example.update(dict_2) #Merges dict_example with dict_2 and any duplicates are overwritten from dict_2
print(f"After update: {dict_example}")

#Dict Remove
dict_example.pop("entry_1")
print(f"After remove: {dict_example}")
dict_example.clear()
print(f"After clear: {dict_example}")
