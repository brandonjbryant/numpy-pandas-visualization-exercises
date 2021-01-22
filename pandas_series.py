#Use pandas to create a Series from the following data:
import pandas as pd
import matplotlib.pyplot as plt

# a. Name the variable that holds the series fruits.
fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
fruits = pd.Series(fruits)
fruits.head()


#b. Run .describe() on the series to see what describe returns for a series of strings.

fruits.describe()

#c. Run the code necessary to produce only the unique fruit names.

fruits.unique()

#d. Determine how many times each value occurs in the series.

fruits.value_counts()

#e. Determine the most frequently occurring fruit name from the series.

#f. Determine the least frequently occurring fruit name from the series.

#e.Write the code to get the longest string from the fruits series.

Find the fruit(s) with 5 or more letters in the name.

Capitalize all the fruit strings in the series.

Count the letter "a" in all the fruits (use string vectorization)

Output the number of vowels in each and every fruit.

Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

Write the code to get only the fruits containing "berry" in the name

Write the code to get only the fruits containing "apple" in the name

Which fruit has the highest amount of vowels?