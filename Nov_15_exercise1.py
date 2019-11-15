
list1 = "pie"
list2 = "eip"

def dictionary_maker(list):
    new_dict = {}
    for letter in list:
        new_dict[letter] = list.count(letter)
    return new_dict

# def compare(dict1, dict2):
#     final = True
#     for item in dict1:
#         if dict2[item] == dict1[item]:
#             final = False
#     return final     

a = sorted(dictionary_maker(list1).items())
b = sorted(dictionary_maker(list2).items())

print()

if a == b:
    print("arrays are equal")
else: 
    print("not equal")

print(a, b)

