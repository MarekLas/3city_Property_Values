# Change data types to category type
def change_to_category_type(target_column, data_type='category'):
    df[target_column] = df[target_column].astype(data_type)
