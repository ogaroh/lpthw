# available cars
cars = 100
# car capacity
space_in_a_car = 4
# vailable drivers
drivers = 30
# totoal passengers
passengers = 90
# cars without drivers
cars_not_driven = cars - drivers
# cars with drivers
cars_driven = drivers
# carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# aprroximate number of passengers per car
average_passengers_per_car = int(passengers / cars_driven)

# output
print("We have ", cars, " cars available today.")
print("There are only", drivers, " drivers avaiable.")
print("There will be ", cars_not_driven, " empty cars today.")
print("We can transport ", carpool_capacity, " people today.")
print("We have ", passengers, " passengers to carpool.")
print("We need to put about ", average_passengers_per_car, "passengers in each car.")