# Data_analysis_TitanicPassenger
# Data Analysis:
Data analysis is a process of inspecting, cleansing, transforming and modeling data with the goal of discovering useful information, informing conclusions and supporting decision-making<br><br>
Two methods are used for analysis in this project:<br> <br>
ANOVA : Analysis of variance is a collection of statistical models and their associated estimation procedures used to analyze the differences among group means in a sample<br><br>
Chi-squared :  Pearson's chi-squared test is used to determine whether there is a statistically significant difference between the expected frequencies and the observed frequencies in one or more categories of a contingency table

<br><h1>Prerequisites:</h1><br>
You will need the following programmes properly installed on your computer.<br>
Python 3.7+ <br>

<br><h1>Installation and Running :</h1><br><br>
git clone https://github.com/ongraphpythondev/TitanicPassenger.git <br>
cd TitanicPassenger<br>

python3 -m venv venv #if using linux(for python 3 and above)

venv\Scripts\activate # for windows or source venv/bin/activate # for linux

<br><h1>install required packages for the project to run</h1>
pip install -r requirements.txt

python3 -W ignore titanic_da.py


<br><h1>Objective : </h1><br>

To find if any pattern for the survival of the passengers of the titanic
 
Hypothesis : 
  1) socioeconomic status affects the survival rate of passenger
  2) age group affects the survival rate of passenger
  3) gender affects the survival rate of passenger

Note : The above hypothesis will be rejected based on the confidence interval of the tests done of the data.
       Confidence interval used is 0.95 thus the pvalue of the tests should be less than 0.05 to be rejected.

Tests Used:

- chi square for testing weather socioeconomic status and gender of passenger was somehow related to the survival of the passenger
- ANOVA (f test) and chi square for testing weather age of passenger was somehow related to the survival of the passenger

<br><h1>Conclusion:</h1><br>
  There are 177 missing values in the Age column. Assuming these values are missing at random for now we can conclude by help of preforming ANOVA test that :    

  - age did matter for survival

  We can further solidify this conclusion by taking the title (ex. Mr,Mrs etc.) of the passanger as a hint for which age group they belong to<br>
    1) Mr and Mrs - Adult<br>
    2) Miss and Master - Young<br>
    3) Dr etc - Other<br>

  Note : The graph showing the distribution of ages according to the passenger's title is saved in "agegroup.png". 
         This graph clearly shows seperation between ages of different titles accordingly thus we can say that title acts as proxy for age

  Now by preforming chi square test we can infer the following.  

  - age and survival are dependent 

  By preforming chi square test on our data we can conclude : 

  - gender and survival are dependent
  - socioeconomic status and survival are dependent


</h2>Data Dictonary:</h2>

Variable   |	Definition				   |	Key
:---:|:---:|:---:|
survival   |	Survival				   |	0 = No, 1 = Yes
pclass	   |	Ticket class				   |	1 = 1st, 2 = 2nd, 3 = 3rd
sex	   |	Sex
Age	   |	Age in years
sibsp	   |	# of siblings / spouses aboard the Titanic	
parch	   |	# of parents / children aboard the Titanic	
ticket	   |	Ticket number	
fare	   |	Passenger fare	
cabin	   |	Cabin number	
embarked   |	Port of Embarkation			   |	C = Cherbourg, Q = Queenstown, S = Southampton


data source : https://www.kaggle.com/c/titanic/data




