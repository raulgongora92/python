import time
start_time = time.time()

#outer loop
for i in range(100):
    #inner loop
    for j in range(1000):
        print(j, end=" ")
    print()

print(round(time.time() - start_time, 2), "seconds")

'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#outer loop
for x in list1:
    #inner loop
    for y in list2:
        print(y, end=" ")
    print()  # New line after inner loop completes
'''