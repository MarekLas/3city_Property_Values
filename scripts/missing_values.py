# Easy function for quick checkin missing values
def missing_values(target_column):
    print(df[target_column].isnull().sum())
