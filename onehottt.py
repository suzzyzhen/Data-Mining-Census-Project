import pandas as pd
import numpy as np
from sklearn import preprocessing
import csv
feature_names = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','50k']
pd.set_option('display.max_row', 1000)
pd.set_option('display.max_columns', 50)
dataset = pd.read_csv("census-income.data.csv",names = feature_names)

#######################################################################
file = open("dictionery.txt","w")
le = preprocessing.LabelEncoder()
########################################################################

#workclass
workclass = dataset.workclass
#workclassUNI = dataset.workclass.unique()  #check the unique elements under this column
le.fit(workclass)
le_workclass_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
workclass_encoded = le.transform(workclass)
repr(le_workclass_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_workclass_mapping) + '\n' + "###########################" + '\n')

###########################################################################

#education
education = dataset.education
#educationUNI = dataset.education.unique()  #check the unique elements under this column
le.fit(education)
le_education_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
education_encoded = le.transform(education)
repr(le_education_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_education_mapping) + '\n' + "###########################" + '\n')

########################################################################

#marital_status
marital_status = dataset.marital_status
#marital_statusUNI = dataset.marital_status.unique()  #check the unique elements under this column
le = preprocessing.LabelEncoder()
le.fit(marital_status)
le_marital_status_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
marital_status_encoded = le.transform(marital_status)
repr(le_marital_status_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_marital_status_mapping) + '\n' + "###########################" + '\n')

########################################################################

#occupation
occupation = dataset.occupation
#occupationUNI = dataset.occupation.unique()  #check the unique elements under this column
le.fit(occupation)
le_occupation_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
occupation_encoded = le.transform(occupation)
repr(le_occupation_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_occupation_mapping) + '\n' + "###########################" + '\n')

########################################################################

#relationship
relationship = dataset.relationship
#relationshipUNI = dataset.relationship.unique()  #check the unique elements under this column
le.fit(relationship)
le_relationship_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
relationship_encoded = le.transform(relationship)
repr(le_relationship_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_relationship_mapping) + '\n' + "###########################" + '\n')

########################################################################

#race
race = dataset.race
#raceUNI = dataset.race.unique()  #check the unique elements under this column
le.fit(race)
le_race_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
race = le.transform(race)
repr(le_race_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_race_mapping) + '\n' + "###########################" + '\n')

########################################################################

#sex
sex = dataset.sex
#sexUNI = dataset.sex.unique()  #check the unique elements under this column
le.fit(sex)
le_sex_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
sex_encoded = le.transform(sex)
repr(le_sex_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_sex_mapping) + '\n' + "###########################" + '\n')

########################################################################

#native_country
native_country = dataset.native_country
#native_countryUNI = dataset.native_country.unique()  #check the unique elements under this column
le.fit(native_country)
le_native_country_mapping = dict(zip(le.classes_,le.transform(le.classes_))) #making a dictionery of label and original categorical values
native_country_encoded = le.transform(native_country)
repr(le_native_country_mapping)
file.write( 'dictionary for corresponding numerical labeling of each categorical value  = ' + repr(le_native_country_mapping) + '\n' + "###########################" + '\n')

########################################################################
file.close()
#####################################################################################'workclass','education','marital_status','occupation','relationship','race','sex','native_country'

column_list = [workclass_encoded, education_encoded, marital_status_encoded, occupation_encoded, relationship_encoded, race, sex_encoded, native_country_encoded]

census_list = []

for (workclass_1, education_1, marital_1, occupation_1, relationship_1, race_1, sex_1, native_1) in zip(workclass_encoded, education_encoded, marital_status_encoded, occupation_encoded, relationship_encoded, race, sex_encoded, native_country_encoded):
    census_list.append((workclass_1, education_1, marital_1, occupation_1, relationship_1, race_1, sex_1, native_1))

with open ('encoding.csv','w') as f:
    thewriter = csv.writer(f, delimiter =",")
    thewriter.writerow(('workclass', 'education', 'marital status', 'occupation', 'relationship', 'race', 'sex', 'native country'))
    for row in census_list:
        thewriter.writerow(row)


