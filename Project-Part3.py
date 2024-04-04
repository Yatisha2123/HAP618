# This program is to Analyze and Compute the data for the Final Project Submission: Data Analysis Report.

import pandas as pd

# Open the Final Project: Datasheet.
df = pd.read_csv("C:\\Users\\yatis\\OneDrive\\Desktop\\HAP 618\\Yatisha Rajanala HAP 618 Project\\HAP-618-003 Final Project Data.csv")

# Part 3: Data Analysis based on Correlation.

# Part 3.A: Correlation based on Age and Hba1c Levels.

C1 = df['Age'].corr(df['1st HbA1c'])
Rounded_C1 = round(C1, 2)
C2 = df['Age'].corr(df['2nd HbA1c'])
Rounded_C2 = round(C2, 2)
C3 = df['Age'].corr(df['Extent of Glycaemic Control'])
Rounded_C3 = round(C3, 2)

print("The Correlation between Age and 1st HbA1c Value is", Rounded_C1)
print("The Correlation between Age and 2nd HbA1c Value is", Rounded_C2)
print("The Correlation between Age and Extent of Glycaemic Control is", Rounded_C3)

# Part 3.B: Correlation based on Federal Poverty Level and Hba1c Levels.

C4 = df['Federal Poverty Level'].corr(df['1st HbA1c'])
Rounded_C4 = round(C4, 2)
C5 = df['Federal Poverty Level'].corr(df['2nd HbA1c'])
Rounded_C5 = round(C5, 2)
C6 = df['Federal Poverty Level'].corr(df['Extent of Glycaemic Control'])
Rounded_C6 = round(C6, 2)

print("The Correlation between Federal Poverty Level and 1st HbA1c Value is", Rounded_C4)
print("The Correlation between Federal Poverty Level and 2nd HbA1c Value is", Rounded_C5)
print("The Correlation between Federal Poverty Level and Extent of Glycaemic Control is", Rounded_C6)