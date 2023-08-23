data = [50,10,15,62,74,12]
result = data[0]
 
for num in data:
    if num < result:
        result = num
 
print(result)