import numpy as np
import pandas as pd

dataset = pd.read_csv('~/Path_to_/Admission_Predict.csv')
dataset1= dataset.iloc[51:81, [0, 1,5,8]]

#print dataset
df = dataset1[["GRE Score", "TOEFL Score", "CGPA", "Chance_of_Admit_Y_N"]]
print(df)

chance_of_admit = df["Chance_of_Admit_Y_N"]

print("Total columns: " + str(len(chance_of_admit)))

probability_of_True = float(np.sum(chance_of_admit) / float(len(chance_of_admit)))

probability_of_False = 1 - probability_of_True

print("Probability of True: " + str(probability_of_True))

print ( "Probability of False: "  + str(probability_of_False))

test_value = ["Medium", "Medium", "Medium"]

df_True_values = df.loc[df['Chance_of_Admit_Y_N'] == True]

df_False_values = df.loc[df['Chance_of_Admit_Y_N'] == False]

print("Test data for GRE Score, TOEFL Score, CGPA")
print (test_value)

gre_medium_in_True = df_True_values.loc[(df_True_values['GRE Score'] == test_value[0])]
probability_of_gre_medium_in_True = len(gre_medium_in_True) / float(len(df_True_values))

toefl_medium_in_True = df_True_values.loc[ (df_True_values['TOEFL Score'] == test_value[1]) ]
probability_of_toefl_medium_in_True = len(toefl_medium_in_True) / float(len(df_True_values))

cgpa_medium_in_True = df_True_values.loc[(df_True_values['CGPA'] == test_value[2])]
probability_of_cgpa_medium_in_True = len(cgpa_medium_in_True) / float(len(df_True_values))


gre_medium_in_False = df_False_values.loc[(df_False_values['GRE Score'] == test_value[0])]
probability_of_gre_medium_in_False = len(gre_medium_in_False) / float(len(df_False_values))

toefl_medium_in_False = df_False_values.loc[ (df_False_values['TOEFL Score'] == test_value[1]) ]
probability_of_toefl_medium_in_False = len(toefl_medium_in_False) / float(len(df_False_values))

cgpa_medium_in_False = df_False_values.loc[(df_False_values['CGPA'] == test_value[2])]
probability_of_cgpa_medium_in_False = len(cgpa_medium_in_False) / float(len(df_False_values))


probability_of_True_in_test = probability_of_gre_medium_in_True * probability_of_toefl_medium_in_True * probability_of_cgpa_medium_in_True * probability_of_True

probability_of_False_in_test = probability_of_gre_medium_in_False * probability_of_toefl_medium_in_False * probability_of_cgpa_medium_in_False * probability_of_False


print("Probability of True for given test: " + str(probability_of_True_in_test))

print("Probability of False for given test: " + str(probability_of_False_in_test))

if probability_of_True_in_test >= probability_of_False_in_test:
    print("The tuple is classified as True")
else:
    print("The tuple is classified as False")
