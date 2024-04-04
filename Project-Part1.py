# This program is to Analyze and Compute the data for the Final Project Submission: Data Analysis Report.

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_size(12)
colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFE4B5']

# Open the Final Project: Datasheet.
df = pd.read_csv("C:\\Users\\yatis\\OneDrive\\Desktop\\HAP 618\\Yatisha Rajanala HAP 618 Project\\HAP-618-003 Final Project Data.csv")

# Part 1: Data Analysis based on Occurrence and Prevalance of Diabetes Mellitus.

# Part 1.A: Data Analysis for the Year 2015.

df1 = df.loc[df['Year']==2015]

# Chart 1: Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Sex.

chart1 = df1.groupby(['Sex']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Sex', fontproperties=font)
for text in chart1.texts:
    text.set_fontproperties(font)
chart1.legend().set_visible(False)
chart1.set_ylabel('')
plt.show()

# Chart 2: Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Race.

chart2 = df1.groupby(['Race']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Race', fontproperties=font)
for text in chart2.texts:
    text.set_fontproperties(font)
chart2.legend().set_visible(False)
chart2.set_ylabel('')
plt.show()

# Chart 3: Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Federal Poverty Level.

def FPL_Group1(Federal_Poverty_Level):
    if Federal_Poverty_Level <299:
        return '< 200%'
    elif Federal_Poverty_Level <399:
        return '201-300%'
    else:
        return '> 300%'

df1.loc[:, 'FPL_Groups1'] = df1['Federal Poverty Level'].apply(FPL_Group1)

chart3 = df1.groupby(['FPL_Groups1']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Federal Poverty Level', fontproperties=font)
for text in chart3.texts:
    text.set_fontproperties(font)
chart3.legend().set_visible(False)
chart3.set_ylabel('')
plt.show()

# Chart 4: Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Age.

def Age_Group1(Age):
    if Age < 40:
        return '20-40 Years'
    elif Age < 60:
        return '41-60 Years'
    else:
        return '> 60 Years'

df1.loc[:, 'Age_Groups1'] = df1['Age'].apply(Age_Group1)

chart4 = df1.groupby(['Age_Groups1']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2015 based on Age', fontproperties=font)
for text in chart4.texts:
    text.set_fontproperties(font)
chart4.legend().set_visible(False)
chart4.set_ylabel('')
plt.show()

# Part 1.B: Data Analysis for the Year 2016.

df2 = df.loc[df['Year']==2016]

# Chart 5: Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Sex.

chart5 = df2.groupby(['Sex']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Sex', fontproperties=font)
for text in chart5.texts:
    text.set_fontproperties(font)
chart5.legend().set_visible(False)
chart5.set_ylabel('')
plt.show()

# Chart 6: Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Race.

chart6 = df2.groupby(['Race']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Race', fontproperties=font)
for text in chart6.texts:
    text.set_fontproperties(font)
chart6.legend().set_visible(False)
chart6.set_ylabel('')
plt.show()

# Chart 7: Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Federal Poverty Level.

def FPL_Group2(Federal_Poverty_Level):
    if Federal_Poverty_Level <299:
        return '< 200%'
    elif Federal_Poverty_Level <399:
        return '201-300%'
    else:
        return '> 300%'

df2.loc[:, 'FPL_Groups2'] = df2['Federal Poverty Level'].apply(FPL_Group2)

chart7 = df2.groupby(['FPL_Groups2']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Federal Poverty Level', fontproperties=font)
for text in chart7.texts:
    text.set_fontproperties(font)
chart7.legend().set_visible(False)
chart7.set_ylabel('')
plt.show()

# Chart 8: Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Age.

def Age_Group2(Age):
    if Age < 40:
        return '20-40 Years'
    elif Age < 60:
        return '41-60 Years'
    else:
        return '> 60 Years'

df2.loc[:, 'Age_Groups2'] = df2['Age'].apply(Age_Group2)

chart8 = df2.groupby(['Age_Groups2']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2016 based on Age', fontproperties=font)
for text in chart8.texts:
    text.set_fontproperties(font)
chart8.legend().set_visible(False)
chart8.set_ylabel('')
plt.show()

# Part 1.C: Data Analysis for the Year 2017.

df3 = df.loc[df['Year']==2017]

# Chart 9: Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Sex.

chart9 = df3.groupby(['Sex']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Sex', fontproperties=font)
for text in chart9.texts:
    text.set_fontproperties(font)
chart9.legend().set_visible(False)
chart9.set_ylabel('')
plt.show()

# Chart 10: Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Race.

chart10 = df3.groupby(['Race']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Race', fontproperties=font)
for text in chart10.texts:
    text.set_fontproperties(font)
chart10.legend().set_visible(False)
chart10.set_ylabel('')
plt.show()

# Chart 11: Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Federal Poverty Level.

def FPL_Group3(Federal_Poverty_Level):
    if Federal_Poverty_Level <299:
        return '< 200%'
    elif Federal_Poverty_Level <399:
        return '201-300%'
    else:
        return '> 300%'

df3.loc[:, 'FPL_Groups3'] = df3['Federal Poverty Level'].apply(FPL_Group3)

chart11 = df3.groupby(['FPL_Groups3']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Federal Poverty Level', fontproperties=font)
for text in chart11.texts:
    text.set_fontproperties(font)
chart11.legend().set_visible(False)
chart11.set_ylabel('')
plt.show()

# Chart 12: Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Age.

def Age_Group3(Age):
    if Age < 40:
        return '20-40 Years'
    elif Age < 60:
        return '41-60 Years'
    else:
        return '> 60 Years'

df3.loc[:, 'Age_Groups3'] = df3['Age'].apply(Age_Group3)

chart12 = df3.groupby(['Age_Groups3']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2017 based on Age', fontproperties=font)
for text in chart12.texts:
    text.set_fontproperties(font)
chart12.legend().set_visible(False)
chart12.set_ylabel('')
plt.show()

# Part 1.D: Data Analysis for the Year 2018.

df4 = df.loc[df['Year']==2018]

# Chart 13: Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Sex.

chart13 = df4.groupby(['Sex']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Sex', fontproperties=font)
for text in chart13.texts:
    text.set_fontproperties(font)
chart13.legend().set_visible(False)
chart13.set_ylabel('')
plt.show()

# Chart 14: Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Race.

chart14 = df4.groupby(['Race']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Race', fontproperties=font)
for text in chart14.texts:
    text.set_fontproperties(font)
chart14.legend().set_visible(False)
chart14.set_ylabel('')
plt.show()

# Chart 15: Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Federal Poverty Level.

def FPL_Group4(Federal_Poverty_Level):
    if Federal_Poverty_Level <299:
        return '< 200%'
    elif Federal_Poverty_Level <399:
        return '201-300%'
    else:
        return '> 300%'

df4.loc[:, 'FPL_Groups4'] = df4['Federal Poverty Level'].apply(FPL_Group4)

chart15 = df4.groupby(['FPL_Groups4']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Federal Poverty Level', fontproperties=font)
for text in chart15.texts:
    text.set_fontproperties(font)
chart15.legend().set_visible(False)
chart15.set_ylabel('')
plt.show()

# Chart 4: Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Age.

def Age_Group4(Age):
    if Age < 40:
        return '20-40 Years'
    elif Age < 60:
        return '41-60 Years'
    else:
        return '> 60 Years'

df4.loc[:, 'Age_Groups4'] = df4['Age'].apply(Age_Group4)

chart16 = df4.groupby(['Age_Groups4']).count().plot(kind="pie", y="Year", autopct='%1.1f%%', colors=colors)
plt.title('Occurrence and Prevalance of Diabetes Mellitus in 2018 based on Age', fontproperties=font)
for text in chart16.texts:
    text.set_fontproperties(font)
chart16.legend().set_visible(False)
chart16.set_ylabel('')
plt.show()