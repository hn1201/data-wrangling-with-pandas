# --------------
import numpy as np
import pandas as pd
# Read the data. Data is already loaded in the variable `path` use the `delimeter = ';'`.
df=pd.read_csv(path, delimiter = ';')
#print(df)
# Replace the `unknown` values with the `Nan` and check the value count of missing values and drop the missing rows
#print((df=='unknown').sum())
df=df.replace('unknown',np.nan)
#print(df.isnull().sum())
df.dropna(inplace=True)
#print(df.shape)
# Replace the column name from `loan` to `previous_loan_status` and `y` to `loan_status` 
df.rename(columns={'loan':'previous_loan_status','y':'loan_status'},inplace=True)
#print(df.columns)
# Find out the information of the `job` column.
#print(len(df['job']))
#print(df['job'].nunique())
#print(df['job'].unique())
#print(df['job'].value_counts())
# Check the `loan_status`  approval rate by `job`
#print(df.groupby('job')['loan_status'].value_counts(normalize=True))
# Check the percentage of loan approved by `education`
loan_approved_mask=(df['loan_status']=='yes')
#print(df[loan_approved_mask]['education'].value_counts(normalize=True))
# Check the percentage of loan approved by `previous loan status`
#print(df[loan_approved_mask]['previous_loan_status'].value_counts(normalize=True))
# Create a pivot table between `loan_status` and `marital ` with values form `age`
pivot=df.pivot_table(index='marital', values='age', columns='loan_status')
#print(pivot)
# Loan status based on marital status whose status is married
mask=(df['marital'].apply(lambda x: x=='married'))
#print(df[mask]['loan_status'].value_counts())

#Create a  Dataframes

# Create a dataframe `df_branch_1` where keys are `'customer_id','first_name','last_name'` you can take any value 
branch_1 = {
        'customer_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Andrew', 'Alex', 'Sabestian', 'Hilary', 'Jack'],
        'last_name': ['Ng', 'Hales', 'Rachaska', 'Masan', 'Anthony']}
df_branch_1 = pd.DataFrame(branch_1, columns = ['customer_id', 'first_name', 'last_name'])
#print(df_branch_1)
# Create a dataframe `df_branch_2` where keys are `'customer_id','first_name','last_name'` you can take any value
branch_2 = {
        'customer_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Brain', 'Steve', 'Kim', 'Steve', 'Ben'],
        'last_name': ['Alexander', 'Jobs', 'Jonas', 'Fleming', 'Richardsan']}
df_branch_2 = pd.DataFrame(branch_2, columns = ['customer_id', 'first_name', 'last_name'])
#print(df_branch_2)
# Create a dataframe `df_credit_score` where keys are `'customer_id','score'` you can take any value
credit_score = {
        'customer_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'score': [513, 675, 165, 961, 1080, 1654, 415, 900, 610, 1116]}
df_credit_score = pd.DataFrame(credit_score, columns = ['customer_id','score'])
#print(df_credit_score)
# Concatenate the dataframe `df_branch_1` and `df_branch_2` along the rows
df_new=pd.concat([df_branch_1, df_branch_2])
#print(df_new)
# Merge two dataframes `df_new` and `df_credit_score` with both the left and right dataframes using the `customer_id` key
#print(pd.merge(df_new, df_credit_score, left_on='customer_id', right_on='customer_id',how='right'))







