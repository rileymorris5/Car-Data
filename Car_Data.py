#use data structure {dictionary} to store car info
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
    }
#ask for data
x = input("brand, year or color?\n")
#compare input to data to find same word
for info in car.keys():
    if info == x:
        #pull related data point and print
        print(car.get("{}".format(x)))

#.keys returns all x values {x:y}
#.get returns a y value for a x value {x:y}
#no clue how .format works in this