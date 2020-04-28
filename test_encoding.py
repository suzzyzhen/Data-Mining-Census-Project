#test data encode
workclass1 = test_df_nan.workclass
le.fit(workclass1)
workclass1_encoded = le.transform(workclass1)

marital_status1 = test_df_nan.marital_status
le.fit(marital_status1)
marital_status1_encoded = le.transform(marital_status1)

occupation1 = test_df_nan.occupation
le.fit(occupation1)
occupation1_encoded = le.transform(occupation1)

relationship1 = test_df_nan.relationship
le.fit(relationship1)
relationship1_encoded = le.transform(relationship1)

race1 = test_df_nan.race
le.fit(race1)
race1_encoded = le.transform(race1)

sex1 = test_df_nan.sex
le.fit(sex1)
sex1_encoded = le.transform(sex1)

native_country1 = test_df_nan.native_country
le.fit(native_country1)
native_country1_encoded = le.transform(native_country1)

column_list = [workclass1_encoded, marital_status1_encoded, occupation1_encoded, relationship1_encoded, race1_encoded, sex1_encoded, native_country1_encoded]

census_list = []

for (workclass_2, marital_2, occupation_2, relationship_2, race_2, sex_2, native_2) in zip(workclass1_encoded, marital_status1_encoded, occupation1_encoded, relationship1_encoded, race1_encoded, sex1_encoded, native_country1_encoded):
    census_list.append((workclass_2, marital_2, occupation_2, relationship_2, race_2, sex_2, native_2))

with open ('encoding_test.csv','w') as f:
    thewriter = csv.writer(f, delimiter =",")
    thewriter.writerow(('workclass', 'marital status', 'occupation', 'relationship', 'race', 'sex', 'native country'))
    for row in census_list:
        thewriter.writerow(row)
