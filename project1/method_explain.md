# fillna method
df.fillna(value, inplace=True)

# MAP() function
# Define a function to square a number
def square(x):
    return x ** 2

# Apply the square function to each element in a list using map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Print the squared numbers
print(list(squared_numbers))

# Convert to a dictionary 
dictionary = dict(zip(numbers, squared_numbers))
print(dictionary)

# Map the dictionary to missing values
df['column_name'] = df['column_name'].map(dictionary)
