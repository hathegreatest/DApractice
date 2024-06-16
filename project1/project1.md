# Print a summary of non-missing values and data types
df.info()

# Print summary statistics for numerical columns in unemployment
df.describe()

# Count the values associated with each column in the dataframe
df.nameofcolumn.value_counts()


# Draw a histogram of a numerical column in the dataframe
import matplotlib.pyplot as plt
plt.hist(df['nameofcolumn'])
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of nameofcolumn')
plt.show()

# Draw a histogram using seaborn lib
import seaborn as sns

sns.histplot(df['nameofcolumn'])
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of nameofcolumn')
plt.show()

# Change datatype of a column 
df['column_name'] = df['column_name'].astype(new_data_type)

# Draw a boxplot
plt.boxplot(df['column_name'])
plt.xlabel('Column Name')
plt.ylabel('Values')
plt.title('Boxplot of Column Name')
plt.show()

# Draw a barplot
sns.barplot(x='column_name', y='values', data=df)
plt.xlabel('Column Name')
plt.ylabel('Values')
plt.title('Barplot of Column Name')
plt.show()

# Count missing value
missing_values = df.isnull().sum()
print(missing_values)

# Drop missing value
# Drop missing values for particular columns
df.dropna(subset=['column1', 'column2'], inplace=True)

# Filter the DataFrame for object columns
object_columns = df.select_dtypes(include='object')

# Print the number of unique values
print(object_columns.nunique())

