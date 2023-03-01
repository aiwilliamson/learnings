import pandas as pd
import matplotlib.pyplot as plt
import requests
# Load data from a text file

# CO PILOT USED THROGUHOUT!

# load data from the following CSV file
# https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv
csv_data = requests.get('https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv').text
#store csv_data as a file
with open("grades.csv", "w") as f:
    f.write(csv_data)

df_students = pd.read_csv("grades.csv",delimiter=',',header='infer')

# remove any rows with missing data
df_students = df_students.dropna(axis = 0, how='any')

# the pass grade is 60, who passed?
passes = pd.Series(df_students['Grade'] >= 60)

# save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

def show_distribution(var_data):
    #get the statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    median_val = var_data.median()
    mode_val = var_data.mode()[0]

    #print the statistics, in 1 command
    print(f"Min: {min_val}, Max: {max_val}, Mean: {mean_val}, Median: {median_val}, Mode: {mode_val}")

    # create a figure for 2 subplots (2 rows, 1 column)
    fig, ax = plt.subplots(2,1, figsize=(10,4))

    #plot the histogram
    ax[0].hist(var_data)
    ax[0].set_title("Frequency")

    # Add lines for the mean, median, mode, max, and min
    # the lines should be dashed, different coulours, and of linewidth=2
    ax[0].axvline(mean_val, color='r', linestyle='dashed', linewidth=2)
    ax[0].axvline(median_val, color='g', linestyle='dashed', linewidth=2)
    ax[0].axvline(mode_val, color='b', linestyle='dashed', linewidth=2)
    ax[0].axvline(min_val, color='grey', linestyle='dashed', linewidth=2)
    ax[0].axvline(max_val, color='grey', linestyle='dashed', linewidth=2)

    # Plot the boxplot   
    ax[1].boxplot(var_data, vert=False)
    ax[1].set_xlabel('Value')

    # Add a title to the Figure
    fig.suptitle('Data Distribution')

    # Show the figure
    fig.show()


show_distribution(df_students['Grade'])


def show_density(var_data):
    fig = plt.figure(figsize=(10,4))

    # Plot density
    var_data.plot.density()

    # Add titles and labels
    plt.title('Data Density')

    # Show the mean, median, and mode
    plt.axvline(x=var_data.mean(), color = 'cyan', linestyle='dashed', linewidth = 2)
    plt.axvline(x=var_data.median(), color = 'red', linestyle='dashed', linewidth = 2)
    plt.axvline(x=var_data.mode()[0], color = 'yellow', linestyle='dashed', linewidth = 2)

    # Show the figure
    plt.show()



col = df_students[df_students.StudyHours>1]['StudyHours']
show_density(col)

#now, I've authenticacated with SSH keys