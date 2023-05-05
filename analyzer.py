# Import the relevant modules/libraries
import pandas as pd
import matplotlib.pyplot as plt


## CREATE A DF FROM THE RAW DATA FROM FRIEND
# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
# Create a dictionary with the two lists
movie_dict = {"years": years, "durations": durations}
# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

## MAKE A LINE PLOT OF RAW DATA DF
fig = plt.figure()
# Draw a line plot of release_years and durations
plt.plot(durations_df[["years"]], durations_df[["durations"]])
# Create a title
plt.title("Netflix Movie Durations 2011-2020")

## CREATE THE MAIN DATA DF
# Read in the netflix_data CSV as a DataFrame
netflix_df = pd.read_csv("datasets/netflix_data.csv")

## FILTERING FOR CONTENT

## 