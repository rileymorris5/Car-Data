#use data structure {dictionary} to store car info
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
    }
#ask for data
x = input("brand, year or color?\n")
#pull related data point and print
print(car.get("{}".format(x)))

#function not needed to find related data, input gives x anyways