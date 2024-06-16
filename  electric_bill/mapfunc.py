#map function
map(lambda x: x * 2, [1, 2, 3, 4, 5]) 
# Output: [2, 4, 6, 8, 10] 

# The map function takes two arguments: 
# a function and an iterable.
# It applies the function to each element of the iterable and 
# returns a new iterable with the results. In this example, the lambda function multiplies each element of the list by 2.


# how to use the map function to calculate the average income of female
map(lambda x: x.income, [employee for employee in employees if employee.gender=="female"])

# how to create a dictionary 
dict(map(lambda x: (x.name, x.income), employees)) 
dict(a=1, b=2, c=3)