import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

print(names_1[0])

# put them both inside two hash maps and check for every name inside map one to exist in the map 2 and then put them inside duplicates
s_1 = set(names_1)
s_2 = set(names_2)

duplicates = []

for name in s_1:
    if name in s_2:
        duplicates.append(name)


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
