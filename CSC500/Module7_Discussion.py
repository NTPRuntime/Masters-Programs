example_list = [1, 2, 3, 4, 5, 6, 7, "something", {"Hello": 0, "World": 1}]
print(f"Pre-defined length function: {len(example_list)}")

def length_of_each_item(object:iter):
    length_dict = {}
    main_counter = 0
    for item in object:
        counter = 0
        if type(item) == int:
            counter += 1
            length_dict[str(main_counter)] = counter
        else:
            for _ in item:
                counter += 1
            length_dict[str(main_counter)] = counter
        main_counter += 1
    return main_counter, length_dict

print(f"User-defined length function: {length_of_each_item(example_list)}")