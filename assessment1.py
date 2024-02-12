import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""!!!!!I got my dataset from UCI, and i tried to import it to python but it didn't work. 
    please download the dataset from UCI and replace the below path with yours, it's called 'Adult'. 
    i imported the data file from excel because it wasn't a csv file but a DATA file.!!!!!"""

ds = pd.read_excel('C:\\Users\\Mia\\Desktop\\uni\\Semestre 4\\Data Analysis\\Book1.xlsx')

print("Length of the 'Adult' DataFrame: ", ds.__len__())

#
grouped_data = ds.groupby(['age', 'education_level']).size().unstack(fill_value=0)
grouped_data.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Distribution of Education Levels Among Different Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Education Level', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
ds_numeric = ds.select_dtypes(include='number')

#
avg_hours_per_week = ds.groupby('marital_status')['hours_per_week'].mean()
plt.figure(figsize=(10, 6))
avg_hours_per_week.plot(kind='bar', color='pink')
plt.title('Average Hours per Week by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Average Hours per Week')
plt.xticks(rotation=45)
plt.show()

#
correlation_matrix = ds_numeric.corr()
plt.figure(figsize=(10, 8))
plt.matshow(correlation_matrix, cmap='plasma')
plt.title('Correlation Matrix')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation='vertical')
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.show()

#
x_variable = 'education_number'
y_variable = 'hours_per_week'
x = ds[x_variable]
y = ds[y_variable]
m, c = np.polyfit(x, y, 1)
regression_line = m * x + c
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Data Points')
plt.plot(x, regression_line, color='red', label='Linear Regression')
plt.xlabel(x_variable)
plt.ylabel(y_variable)
plt.title(f'Linear Regression: {y_variable} vs. {x_variable}')
plt.legend()
plt.grid(True)
plt.show()


