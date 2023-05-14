# DataCamp Projects Series: 01 - Investigating Netflix Movies

_DataCamp Project Series_ is a series of the major projects I completed under the DataCamp [**Data Scientist with Python**](https://app.datacamp.com/learn/career-tracks/data-scientist-with-python) track.

## Table of contents
- [Introduction](#introduction)
    - [About](#about-the-project)
    - [Prerequisites](#prerequisites)
    - [Goals](#goals)
- [The Project](#the-project)
    - [Data Used In This Project](#datasets)
    - [The Code](#code)
    - [Findings](#what-i-learned)
    - [Conclusion](#conclusion)
- [Relevant Links](#links)

## Introduction

### About the project

> **"** In this project, you’ll apply the skills you learned in Introduction to Python and Intermediate Python to discover if Netflix’s movies are getting shorter over time using everything from lists and loops to `pandas` and `matplotlib`. You’ll also gain experience in an essential data science skill — exploratory data analysis. This will allow you to perform critical tasks such as manipulating raw data and drawing conclusions from plots you create of the data. **"**

### Prerequisites

**Technology:**
> Python

To be able to take on this project, I needed to have learned:

1. **Courses:**
    - [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)
    - [Intermediate Python](https://www.datacamp.com/courses/intermediate-python)

2. **Concepts:**
    - Data Manipulation
    - Data Visualization
    - Python Basics & Programming

### Goals

In taking on this project, I was trying to:
- use the provided data to investigate a trend
- visualize the data and any trends

## The Project

### Datasets

The following datasets were used in the project:

- Raw data from my "friend": `movie-dict`, a dictionary; eventually converted to a `pandas` DataFrame `durations_df`, a DataFrame.
- `netflix_df`, a DataFrame imported from [`netflix_data`](datasets/netflix_data.csv).

### Code

The code used for investigation and visualization was written in simple Python, starting by importing `pandas` and `matplotlib.pyplot` modules to provide the needed functionality.

The raw code can be found [here](analyzer.py).

### What I learned

From this project, I was able to gain:

- A short revision of the simple procedure of **creating a DataFrame from scratch**.
- A revision of simple data manipulation tricks like **filtering**.
- A revision of simple data visualization, for example, **plotting using different colors**.

### Conclusion

The project was carried out to find out if Netflix movies and series are indeed getting shorter.
The answer, which is visible from the short analysis and the graphs plotted, is **YES.** - Yes, the movies on Netflix ARE getting shorter.

![Color Plot Screenshot](plots/Fig%203%20-%20Movie%20Durations%20by%20Year%20of%20Release%20\(Color-coded\).png)

## Links

Relevant links to the project:

- [Project Home](https://app.datacamp.com/learn/projects/entertainment-data)
- [Track Home](https://app.datacamp.com/learn/career-tracks/data-scientist-with-python)
- [DataCamp Workspace](https://app.datacamp.com/workspace/w/cebc9246-d229-4516-9037-b2d1c8665ce4)

Thanks for reading this far! Follow me:
- [Twitter](https://twitter.com/akcumeh)
- [GitHub](https://github.com/akcumeh)