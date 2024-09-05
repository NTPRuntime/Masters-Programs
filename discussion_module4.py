# class Robot:
#     def __init__(self):
#         pass

#     def pick_part(self):
#         pass

#     def place_part(self):
#         pass

# discrete_io_input_1 = True
# discrete_io_input_2 = True

# def check_discrete_io():
#     pass

# while True:
#     #proximity sensor is high (part in location)
#     if discrete_io_input_1 == True: 
#         Robot.pick_part()
#         while discrete_io_input_2 == True:
#             #part exists in place location
#             #wait until clear
#             check_discrete_io()
#         if discrete_io_input_2 == False:
#             Robot.place_part()

num_list = [1, 3, 0, 2]
sorted_list = [0, 1, 2, 3]
sorted = False
while not sorted:
    for num in range(len(num_list)):
        if num_list == sorted_list:
            sorted = True
            break
        try:
            if num_list[num] > num_list[num+1]:
                temp = num_list[num+1]
                num_list[num+1] = num_list[num]
                num_list[num] = temp
        except IndexError:
            pass


