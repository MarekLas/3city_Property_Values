# Change data types to category type
def change_to_category_type(target_column, data_type='category'):
    df[target_column] = df[target_column].astype(data_type)

# Easy function for quick checkin missing values
def missing_values(target_column):
    print(df[target_column].isnull().sum())

'''
Function to show which features are most important in the model.
::df_in:: Which data frame? (ex. df)
::col_name:: Which column? (ex. 'Rooms_sum')
::quantil_1:: How much for the first quantil? (ex. 0.15)
::quantil_2:: How muvch for the third quantil? (ex. 0.80)
'''

def remove_outlier(df_in, col_name, quantil_1, quantil_3):
    q1 = df_in[col_name].quantile(quantil_1)
    q3 = df_in[col_name].quantile(quantil_3)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out = df_in.loc[(df_in[col_name] > fence_low) & (df_in[col_name] < fence_high)]
    return df_out
