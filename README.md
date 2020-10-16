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


Objective : 
 To find if any pattern for the survival of the passengers of the titanic
 
Hypothesis : 
  1) socioeconomic status affects the survival rate of passenger
  2) age group affects the survival rate of passenger
  3) gender affects the survival rate of passenger

note : The above hypothesis will be rejected based on the confidence interval of the tests done of the data.
       Confidence interval used is 0.95 thus the pvalue of the tests should be less than 0.05 to be rejected.

Data Dictonary:

Variable   |	Definition				   |	Key
__________________________________________________________________________________________
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




