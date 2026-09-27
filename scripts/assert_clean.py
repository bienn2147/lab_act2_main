import pandas as pd

def check_orders_data(clean: pd.DataFrame) -> bool:
    try:
        #row_id uniqueness
        assert clean["row_id"].is_unique 

        #check datatypes
        assert pd.api.types.is_datetime64_any_dtype(clean['order_date']) == True 
        assert pd.api.types.is_datetime64_any_dtype(clean['ship_date']) == True
        assert pd.api.types.is_numeric_dtype(clean['quantity']) == True
        assert pd.api.types.is_numeric_dtype(clean['sales']) == True
        assert pd.api.types.is_numeric_dtype(clean['discount']) == True
        assert pd.api.types.is_numeric_dtype(clean['profit']) == True

        #all postal code entries are 5 digits
        assert len(clean['postal_code'] == 5) == len(clean)

        #quantity must be greater than zero for all rows
        assert len(clean[clean['quantity'].astype(int) > 0]) == len(clean)

        #no missing values 
        assert (clean.isna().sum().sum() == 0) and (clean.isnull().sum().sum() == 0)

        #segment must be either consumer, corporate or home office
        valid_segments = ['Consumer', 'Corporate', 'Home Office']
        assert clean['segment'].isin(valid_segments).all()

        #region must be either central, east, south or west
        valid_regions = ['Central', 'East', 'South', 'West']
        assert clean['region'].isin(valid_regions).all()

        #ship_mode must be either Standard Class, Second Class, First Class or Same Day
        valid_ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']
        assert clean['ship_mode'].isin(valid_ship_modes).all()

    except AssertionError as e:
        print(e)
        return False
    return True 

def check_returns_data(returns_df: pd.DataFrame) -> bool:
    try:
        assert pd.api.types.is_bool_dtype(returns_df['returned'])
        assert returns_df.duplicated().sum().sum() == 0

    except AssertionError as e:
        print(e)
        return False
    return True

def check_people_data(people:pd.DataFrame) -> bool:
    try:
        assert people.duplicated().sum().sum() == 0
        assert people['region'].isin(['West', 'East', 'Central', 'South']).all()
    except AssertionError as e:
        print(e)
        return False
    return True