#!/usr/bin/env python
# coding: utf-8

# Objective : 
# To find if any pattern for the survival of the passengers of the titanic
# 
# Hypothesis : 
#  1) socioeconomic status affects the survival rate of passenger
#  2) age group affects the survival rate of passenger
#  3) gender affects the survival rate of passenger

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

titanic_data_csv = 'titanic_data.csv'
titanic_data_df = pd.read_csv(titanic_data_csv)

_titanic_data = titanic_data_df.copy()
_titanic_data = _titanic_data.drop('PassengerId',axis=1)

def data_summary(x):
    return pd.Series([x.count(),x.std(),
                      x.isnull().sum(),
		      x.isnull().sum()/x.count(),
                      x.min(),
                      x.quantile(0.01),x.quantile(0.05),
                      x.quantile(0.1),x.quantile(0.25),
                      x.quantile(0.50),x.quantile(0.75),
                      x.quantile(0.9),x.quantile(0.95),
                      x.quantile(0.99),x.max()],
                    index = [
                        'count','std',
                        'null_count','null_percent',
                        'min','q_0.01',
                        'q_0.05','q_0.10',
                        'q_0.25','q_0.50',
                        'q_0.75','q_0.90',
                        'q_0.95','q_0.99',
                        'max',
                    ])

descript = _titanic_data.select_dtypes(['int64','float64']).apply(data_summary).T

Survived_data = _titanic_data[_titanic_data['Survived'] == 1]
deceased_data = _titanic_data[_titanic_data['Survived'] == 0]

f_res = stats.f_oneway(Survived_data['Age'].dropna(), deceased_data['Age'].dropna())

print(f"""
There are {_titanic_data.Age.isna().sum()} missing values in the Age column. Assuming these values are missing at random for now we can conclude that :    
""")

if f_res.pvalue > 0.05:
    print('age did not matter for survival') # failed to reject the null hypothysis
else:
    print('age did matter for survival') # reject the null hypothysis

print("""
We can further solidify our conclusion by taking the title (ex. Mr,Mrs etc.) of the passanger as a hint for which age group they belong to and then we can infer the following.  
""")


# Assuming the value missing in age columns were at random, for now we can say that the age did not matter in survival of the passenger.
# To confirm the above result we can do another check using the title of the passenger to determine there age group to reduce the missing info. reguarding the age of passanger

adult = _titanic_data[(_titanic_data.Name.str.contains('Mr.')) | (_titanic_data.Name.str.contains('Mrs.'))].index
young = _titanic_data[(_titanic_data.Name.str.contains('Master.')) | (_titanic_data.Name.str.contains('Miss.'))].index

_titanic_data.loc[_titanic_data.index.isin(adult),'agegroup'] = 1
_titanic_data.loc[_titanic_data.index.isin(young),'agegroup'] = 2
_titanic_data.loc[_titanic_data.agegroup.isna(),'agegroup'] = 3

sns.kdeplot(_titanic_data[_titanic_data.agegroup==1.0]['Age'])
sns.kdeplot(_titanic_data[_titanic_data.agegroup==2.0]['Age'])
sns.kdeplot(_titanic_data[_titanic_data.agegroup==3.0]['Age'])
plt.legend(['adult','young','other'])
plt.savefig('agegroup.png')


# the above graph shows seperation between ages of different titles accordingly thus we can say that title acts as proxy for age

# For the statistical test we are going to use a confidance interval of 0.95 (i.e alpha = 0.05). Thus we will reject the null hypothysis of the tests if the pvalue <= 0.05 

conteng_table_age_group = pd.crosstab(_titanic_data['Survived'],_titanic_data['agegroup'])
chi_stat = stats.chi2_contingency(conteng_table_age_group)

if chi_stat[1] > 0.05:
    print('- age and survival are independent') # failed to reject the null hypothysis
else:
    print('- age and survival are dependent\n') # reject the null hypothysis

print("""Note : The graph showing the distribution of ages according to the passenger's title is saved in agegroup.png. 
          This graph clearly shows seperation between ages of different titles accordingly thus we can say that title acts as proxy for age \n""")


conteng_table_gender = pd.crosstab(_titanic_data['Survived'],_titanic_data['Sex'])
chi_stat = stats.chi2_contingency(conteng_table_gender)

if chi_stat[1] > 0.05:
    print('- gender and survival are independent') # failed to reject the null hypothysis
else:
    print('- gender and survival are dependent') # reject the null hypothysis


conteng_table_Pclass = pd.crosstab(_titanic_data['Survived'],_titanic_data['Pclass'])
chi_stat = stats.chi2_contingency(conteng_table_Pclass)

if chi_stat[1] > 0.05:
    print('- socioeconomic status and survival are indipendent')  # failed to reject the null hypothysis
else:
    print('- socioeconomic status and survival are dependent') # reject the null hypothysis

