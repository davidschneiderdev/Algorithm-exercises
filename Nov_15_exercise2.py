
list1 = [1,2,3,4]
list2 = [1,16,9,4]

def make_dict_squares(list):
    new_dict = {}
    for num in list:
        new_dict[(num*num)] = list.count(num)
    return new_dict

def make_dict(lst):
    new_dict = {}
    for num in lst:
        new_dict[num] = lst.count(num)
    return new_dict

new_dict1 = make_dict_squares(list1)
new_dict2 = make_dict(list2)

print(new_dict1, new_dict2)


square_count = 0
for square in new_dict1:
    for item in new_dict2:
        if square == item:
            print("square exists")
            square_count += 1
if square_count == len(list1):
    print("True")
else: 
    print("False")





