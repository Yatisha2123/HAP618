# This program is to Analyze and Compute the data for the Final Project Submission: Data Analysis Report.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_size(12)
colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#FFE4B5']

# Open the Final Project: Datasheet.
df = pd.read_csv("C:\\Users\\yatis\\OneDrive\\Desktop\\HAP 618\\Yatisha Rajanala HAP 618 Project\\HAP-618-003 Final Project Data.csv")

# Part 2: Data Analysis based on Extent of Glycaemic Control, using the HbA1c Measured Values.

# Part 2.A: Data Analysis for Males.

df5 = df.loc[df['Sex']=='Male']
df5 = df5.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1)
df5 = df5.groupby('Year').mean()

Y1=np.array([2015,2016,2017,2018])
X1 = df5["1st HbA1c"]
X2 = df5["2nd HbA1c"]
X3 = df5["Extent of Glycaemic Control"]

fig, ax1 = plt.subplots()
ax1.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax1.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax1.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax1.set_title('Extent of Glycaemic Control over the Years in Males', fontproperties=font)
ax1.set_ylabel('HbA1c Values', fontproperties=font)
ax1.set_xlabel('Years', fontproperties=font)

for label in ax1.xaxis.get_ticklabels() + ax1.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax1.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.B: Data Analysis for Females.

df6 = df.loc[df['Sex']=='Female']
df6 = df6.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1)
df6 = df6.groupby('Year').mean()

Y1=np.array([2015,2016,2017,2018])
X1 = df6["1st HbA1c"]
X2 = df6["2nd HbA1c"]
X3 = df6["Extent of Glycaemic Control"]

fig, ax2 = plt.subplots()
ax2.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax2.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax2.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax2.set_title('Extent of Glycaemic Control over the Years in Females', fontproperties=font)
ax2.set_ylabel('HbA1c Values', fontproperties=font)
ax2.set_xlabel('Years', fontproperties=font)

for label in ax2.xaxis.get_ticklabels() + ax2.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax2.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.C: Data Analysis for Whites.

df7 = df.loc[df['Race']=='White']
df7 = df7.drop('Race', axis=1).drop('Sex', axis=1).drop('Medical Status', axis=1)
df7 = df7.groupby('Year').mean()

Y1=np.array([2015,2016,2017,2018])
X1 = df7["1st HbA1c"]
X2 = df7["2nd HbA1c"]
X3 = df7["Extent of Glycaemic Control"]

fig, ax3 = plt.subplots()
ax3.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax3.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax3.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax3.set_title('Extent of Glycaemic Control over the Years in Whites', fontproperties=font)
ax3.set_ylabel('HbA1c Values', fontproperties=font)
ax3.set_xlabel('Years', fontproperties=font)

for label in ax3.xaxis.get_ticklabels() + ax3.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax3.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.D: Data Analysis for African-Americans.

df8 = df.loc[df['Race']=='African-American']
df8 = df8.drop('Race', axis=1).drop('Sex', axis=1).drop('Medical Status', axis=1)
df8 = df8.groupby('Year').mean()

Y1=np.array([2015,2016,2017,2018])
X1 = df8["1st HbA1c"]
X2 = df8["2nd HbA1c"]
X3 = df8["Extent of Glycaemic Control"]

fig, ax4 = plt.subplots()
ax4.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax4.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax4.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax4.set_title('Extent of Glycaemic Control over the Years in African-Americans', fontproperties=font)
ax4.set_ylabel('HbA1c Values', fontproperties=font)
ax4.set_xlabel('Years', fontproperties=font)

for label in ax4.xaxis.get_ticklabels() + ax4.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax4.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.E: Data Analysis for Hispanics.

df9 = df.loc[df['Race']=='Hispanic']
df9 = df9.drop('Race', axis=1).drop('Sex', axis=1).drop('Medical Status', axis=1)
df9 = df9.groupby('Year').mean()

Y1=np.array([2015,2016,2017,2018])
X1 = df9["1st HbA1c"]
X2 = df9["2nd HbA1c"]
X3 = df9["Extent of Glycaemic Control"]

fig, ax5 = plt.subplots()
ax5.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax5.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax5.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax5.set_title('Extent of Glycaemic Control over the Years in Hispanics', fontproperties=font)
ax5.set_ylabel('HbA1c Values', fontproperties=font)
ax5.set_xlabel('Years', fontproperties=font)

for label in ax5.xaxis.get_ticklabels() + ax5.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax5.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.F: Data Analysis for different Federal Poverty Levels.

def FPL_Group5(Federal_Poverty_Level):
    if Federal_Poverty_Level <299:
        return '< 200%'
    elif Federal_Poverty_Level <399:
        return '201-300%'
    else:
        return '> 300%'

df['FPL_Group5'] = df['Federal Poverty Level'].apply(FPL_Group5)

# Part 2.F.1: Data Analysis for Federal Poverty Level <200%.

df10 = df.loc[df['FPL_Group5']=='< 200%']
df10 = df10.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1).drop('FPL_Group5', axis=1)

df10 = df10.groupby(['Year']).mean()
df10 = df10.reset_index()

Y1=np.array([2015,2016,2017,2018])

X1 = df10["1st HbA1c"]
X2 = df10["2nd HbA1c"]
X3 = df10["Extent of Glycaemic Control"]

fig, ax6 = plt.subplots()
ax6.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax6.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax6.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax6.set_title('Extent of Glycaemic Control over the Years for Federal Poverty Level <200%', fontproperties=font)
ax6.set_ylabel('HbA1c Values', fontproperties=font)
ax6.set_xlabel('Years', fontproperties=font)

for label in ax6.xaxis.get_ticklabels() + ax6.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax6.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.F.2: Data Analysis for Federal Poverty Level 201-300%.

df11 = df.loc[df['FPL_Group5']=='201-300%']
df11 = df11.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1).drop('FPL_Group5', axis=1)

df11 = df11.groupby(['Year']).mean()
df11 = df11.reset_index()

Y1=np.array([2015,2016,2017,2018])

X1 = df11["1st HbA1c"]
X2 = df11["2nd HbA1c"]
X3 = df11["Extent of Glycaemic Control"]

fig, ax7 = plt.subplots()
ax7.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax7.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax7.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax7.set_title('Extent of Glycaemic Control over the Years for Federal Poverty Level 201-300%', fontproperties=font)
ax7.set_ylabel('HbA1c Values', fontproperties=font)
ax7.set_xlabel('Years', fontproperties=font)

for label in ax7.xaxis.get_ticklabels() + ax7.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax7.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.F.2: Data Analysis for Federal Poverty Level >300%.

df12 = df.loc[df['FPL_Group5']=='> 300%']
df12 = df12.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1).drop('FPL_Group5', axis=1)

df12 = df12.groupby(['Year']).mean()
df12 = df12.reset_index()

Y1=np.array([2015,2016,2017,2018])

X1 = df12["1st HbA1c"]
X2 = df12["2nd HbA1c"]
X3 = df12["Extent of Glycaemic Control"]

fig, ax8 = plt.subplots()
ax8.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax8.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax8.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax8.set_title('Extent of Glycaemic Control over the Years for Federal Poverty Level > 300%', fontproperties=font)
ax8.set_ylabel('HbA1c Values', fontproperties=font)
ax8.set_xlabel('Years', fontproperties=font)

for label in ax8.xaxis.get_ticklabels() + ax8.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax8.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.G: Data Analysis for different Age Groups.

def Age_Group5(Age):
    if Age < 40:
        return '20-40 Years'
    elif Age < 60:
        return '41-60 Years'
    else:
        return '> 60 Years'

df['Age_Group5'] = df['Age'].apply(Age_Group5)

# Part 2.G.1: Data Analysis for Age 20-40 Years.

df13 = df.loc[df['Age_Group5']=='20-40 Years']
df13 = df13.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1).drop('Age_Group5', axis=1).drop('FPL_Group5', axis=1)

df13 = df13.groupby(['Year']).mean()
df13 = df13.reset_index()

Y1=np.array([2015,2016,2017,2018])

X1 = df13["1st HbA1c"]
X2 = df13["2nd HbA1c"]
X3 = df13["Extent of Glycaemic Control"]

fig, ax9 = plt.subplots()
ax9.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax9.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax9.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax9.set_title('Extent of Glycaemic Control over the Years for Age 20-40 Years', fontproperties=font)
ax9.set_ylabel('HbA1c Values', fontproperties=font)
ax9.set_xlabel('Years', fontproperties=font)

for label in ax9.xaxis.get_ticklabels() + ax9.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax9.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.G.1: Data Analysis for Age 41-60 Years.

df14 = df.loc[df['Age_Group5']=='41-60 Years']
df14 = df14.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1).drop('Age_Group5', axis=1).drop('FPL_Group5', axis=1)

df14 = df14.groupby(['Year']).mean()
df14 = df14.reset_index()

Y1=np.array([2015,2016,2017,2018])

X1 = df14["1st HbA1c"]
X2 = df14["2nd HbA1c"]
X3 = df14["Extent of Glycaemic Control"]

fig, ax10 = plt.subplots()
ax10.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax10.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax10.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax10.set_title('Extent of Glycaemic Control over the Years for Age 41-60 Years', fontproperties=font)
ax10.set_ylabel('HbA1c Values', fontproperties=font)
ax10.set_xlabel('Years', fontproperties=font)

for label in ax10.xaxis.get_ticklabels() + ax10.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax10.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()

# Part 2.G.1: Data Analysis for Age >60 Years.

df15 = df.loc[df['Age_Group5']=='> 60 Years']
df15 = df15.drop('Sex', axis=1).drop('Race', axis=1).drop('Medical Status', axis=1).drop('Age_Group5', axis=1).drop('FPL_Group5', axis=1)

df15 = df15.groupby(['Year']).mean()
df15 = df15.reset_index()

Y1=np.array([2015,2016,2017,2018])

X1 = df15["1st HbA1c"]
X2 = df15["2nd HbA1c"]
X3 = df15["Extent of Glycaemic Control"]

fig, ax11 = plt.subplots()
ax11.bar(Y1-0.2, X1, width=0.2, color='#FFB6C1', align='center')
ax11.bar(Y1, X2, width=0.2, color='#ADD8E6', align='center')
ax11.bar(Y1+0.2, X3, width=0.2, color='#90EE90', align='center')

ax11.set_title('Extent of Glycaemic Control over the Years for Age >60 Years', fontproperties=font)
ax11.set_ylabel('HbA1c Values', fontproperties=font)
ax11.set_xlabel('Years', fontproperties=font)

for label in ax11.xaxis.get_ticklabels() + ax11.yaxis.get_ticklabels():
    label.set_fontproperties(font)
    
ax11.legend(['1st HbA1c', '2nd HbA1c', 'Extent of Glycaemic Control'], prop={'family': 'Times New Roman', 'size': 12})

plt.show()