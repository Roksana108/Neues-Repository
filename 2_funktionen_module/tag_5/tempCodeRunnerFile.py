sam_count = 0
for sentence in sentences:
    sam_count = sam_count + sentence.count("Sam")

print(reduce(lambda sam_count , "sam_count"))