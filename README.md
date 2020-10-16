# TitanicPassenger
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

note : The above hypothesis will be rejected based on the confidence interval of the tests done of the data.
       Confidence interval used is 0.95 thus the pvalue of the tests should be less than 0.05 to be rejected.

Tests Used:

- chi square for testing weather socioeconomic status and gender of passenger was somehow related to the survival of the passenger
- ANOVA (f test) and chi square for testing weather age of passenger was somehow related to the survival of the passenger

Conclusion:
  There are 177 missing values in the Age column. Assuming these values are missing at random for now we can conclude by help of preforming ANOVA test that :    

  <h2>- age did matter for survival</h2>

  We can further solidify this conclusion by taking the title (ex. Mr,Mrs etc.) of the passanger as a hint for which age group they belong to
    1) Mr and Mrs - Adult
    2) Miss and Master - Young
    3) Dr etc - Other
    
  Note : The graph showing the distribution of ages according to the passenger's title is saved in "agegroup.png". 
         This graph clearly shows seperation between ages of different titles accordingly thus we can say that title acts as proxy for age

  Now by preforming chi square test we can infer the following.  

  <h2>- age and survival are dependent</h2> 

  By preforming chi square test on our data we can conclude : 

  <h2>- gender and survival are dependent</h2>
  <h2>- socioeconomic status and survival are dependent</h2>


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




