result = 1 
x = 1 

while result < 1000000:
    x = x + 1 
    result = x * result
    if ((x + 1) * result) > 1000000:
        break
    
print(f"Factor integer: {x}")
print(result)



# print("Highest possible is" + int(result))
# print("Factor integer: " + int(x))