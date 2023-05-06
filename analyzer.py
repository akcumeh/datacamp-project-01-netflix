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

## FILTER FOR CONTENT
# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]
# Select only the columns of interest: title, country, genre, year, duration
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]

## VISUALIZE THE DATA, 1: SCATTERPLOT
# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))
# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset[["release_year"]], netflix_movies_col_subset[["duration"]])
# Create a title
plt.title("Movie Duration by Year of Release")

## VISUALIZE THE DATA, 2: PLOT WITH COLOR
# Make a list of colors based on genre
colors = []
# Iterate over rows of netflix_movies_col_subset
for key, value in netflix_movies_col_subset.iterrows():
    if value["genre"] == "Children":
        colors.append("red")
    elif value["genre"] == "Documentaries":
        colors.append("blue")
    elif value["genre"] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# MAKE THE COLOR SCATTERPLOT:
# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset[["release_year"]], netflix_movies_col_subset[["duration"]], c=colors)
# Create a title and label the axes
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release Year")
plt.ylabel("Duration (min)")

# Show the plots
plt.show()