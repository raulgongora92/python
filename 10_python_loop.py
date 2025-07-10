str = "Looping"

for item in str:
    print(item)

###########################

for i in range(10):
    print("looping...", i)

###########################

favorites =['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for item in favorites:
    print("I like this desert:", item)

for idx, item in enumerate(favorites):
    print(idx, item)



###########################
favoritess =['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

count = 0

while count < len(favoritess):
    print("I like this desert:", favoritess[count])
    count += 1

