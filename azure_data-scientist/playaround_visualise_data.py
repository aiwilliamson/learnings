import pandas as pd
import requests
# Load data from a text file

#df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')

# load data from the following CSV file
# https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv
csv_data = requests.get('https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv').text
#store csv_data as a file
with open("grades.csv", "w") as f:
    f.write(csv_data)

df_students = pd.read_csv("grades.csv",delimiter=',',header='infer')

# remove any rows with missing data
df_students = df_students.dropna(axis = 0, how='any')

#THIS WAS DONE WITH THE HELP OF GITHUB COPILOT - VERY GOOD!

# print a funny joke
print("Why did the chicken cross the road?")
print("To get to the other side!")

