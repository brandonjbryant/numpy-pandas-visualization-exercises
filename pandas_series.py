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

fruits.value_counts().index[0]

#f. Determine the least frequently occurring fruit name from the series.

fruits.value_counts().index[-1]

#g. Write the code to get the longest string from the fruits series.

longest_string = fruits.apply(len).argmax()
fruits[longest_string]

#h. Find the fruit(s) with 5 or more letters in the name.

fruits[fruits.str.len() >= 5]

#i. Capitalize all the fruit strings in the series.

fruits.str.title()

#j. Count the letter "a" in all the fruits (use string vectorization)

fruits.str.count("a").sum()

#k. Output the number of vowels in each and every fruit.

fruits = fruits.str.lower()

(fruits.str.count("a") 
     + fruits.str.count("e") 
     + fruits.str.count("i") 
     + fruits.str.count("o") 
     + fruits.str.count("u"))

#l. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

fruits[fruits.apply(lambda x: x.count("o") >= 2)]

#m. Write the code to get only the fruits containing "berry" in the name

fruits[fruits.str.contains("berry")]

#n. Write the code to get only the fruits containing "apple" in the name

Write the code to get only the fruits containing "apple" in the name
fruits[fruits.str.contains("apple")] 

#o. Which fruit has the highest amount of vowels?

fruits[(fruits.str.count("a") 
     + fruits.str.count("e") 
     + fruits.str.count("i") 
     + fruits.str.count("o") 
     + fruits.str.count("u")).argmax()]


# 2. Use pandas to create a Series from the following data:
panda_salaries = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

panda_salaries = pd.Series(panda_salaries)

# What is the data type of the series?
panda_salaries.head()


# Use series operations to convert the series to a numeric data type.
panda_salaries = panda_salaries.str.replace('$',"")
panda_salaries = panda_salaries.str.replace(",", "")
panda_salaries = panda_salaries.astype(float)


#What is the maximum value? 
panda_salaries.max()

#The minimum?
panda_salaries.min()

#Bin the data into 4 equally sized intervals and show how many values fall into each bin.
bins = pd.cut(panda_salaries,4)
bins.value_counts()

#Plot a histogram of the data. Be sure to include a title and axis labels.
plt.title("Panda Salaries Bins")
plt.xlabel("$")
plt.ylabel("# occurences")
plt.hist(pandas_salaries, bins=4)
plt.show()


# 3. Use pandas to create a Series from the following exam scores: 
grades = [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

grades = pd.Series(grades)
grades.head()

#What is the minimum exam score? The max, mean, median?
grades.min()

grades.max()

grades.median()

# Plot a histogram of the scores.
x = grades.hist()

# Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
def grade_convert(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
grades.apply(grade_convert)

# Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.
top_score = grades.max()
difference = 100 - top_score
implement_curve = grades + difference
implement_curve


#Use pandas to create a Series from the following string:

string = 'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

scrabble = pd.Series(list(string))
scrabble.head()

#. What is the most frequently occuring letter? Least frequently occuring?
scrabble.value_counts().index[0]


scrabble.value_counts().index[-1]

# How many vowels are in the list?
# How many vowels are in the list?
(scrabble.str.count("a") 
    + scrabble.str.count("e") 
    + scrabble.str.count("i")
    + scrabble.str.count("o")
    + scrabble.str.count("u")).sum() 

    # How many consonants are in the list?
consonants = "bcdfghjklmnpqrstvwxyz"
scrabble.isin(list(consonants)).sum()

######################################################################################
########################## LIST COMPREHENSION WITH PANDAS SERIES #####################
######################################################################################

# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# Exercise 5 - make a list that contains each fruit with more than 5 characters

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
 