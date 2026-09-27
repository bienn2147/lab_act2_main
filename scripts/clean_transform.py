import pandas as pd

def clean_orders_table(orders:pd.DataFrame)-> pd.DataFrame:
    # Convert date columns to datetime
    orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
    orders['ship_date'] = pd.to_datetime(orders['ship_date'], errors='coerce')

    # Convert numeric columns to appropriate types
    orders['quantity'] = pd.to_numeric(orders['quantity'], errors='coerce')
    orders['sales'] = pd.to_numeric(orders['sales'], errors='coerce')
    orders['discount'] = pd.to_numeric(orders['discount'], errors='coerce')
    orders['profit'] = pd.to_numeric(orders['profit'], errors='coerce')

    # Trim whitespace from string columns
    str_cols = orders.select_dtypes(include=['object']).columns
    for col in str_cols:
        orders[col] = orders[col].str.strip()

    # Fix postal code issues (ensure 5 digits)
    orders['postal_code'] = orders['postal_code'].astype(str).str.zfill(5)

    # Check quantity, drop rows where quantity is less than or equal to 0
    if len(orders[orders['quantity'].astype(int) > 0]) != len(orders):
        orders.drop(orders[orders['quantity'].astype(int) <= 0].index, inplace=True)

    # restict segment to either consumer, corporate or home office
    valid_segments = ['Consumer', 'Corporate', 'Home Office']
    orders = orders[orders['segment'].isin(valid_segments)]

    # restrict region to either central, east, south or west
    valid_regions = ['Central', 'East', 'South', 'West']
    orders = orders[orders['region'].isin(valid_regions)]

    #restrict ship_mode to either Standard Class, Second Class, First Class or Same Day
    valid_ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']
    orders = orders[orders['ship_mode'].isin(valid_ship_modes)]

    # Drop rows with missing critical values (e.g., order_id, product_id)
    orders.dropna(subset=['order_id', 'product_id'], inplace=True)

    return orders

def clean_returns_table(returns_df: pd.DataFrame) -> pd.DataFrame:
    valid_returns = ['Yes', 'No']
    returns_df = returns_df[returns_df['returned'].isin(valid_returns)]

    #map return status to boolean
    returns_df['returned'] = returns_df['returned'].map({'Yes': True, 'No': False})
    returns_df['returned'].astype(bool)

    #drop duplicates
    returns_df = returns_df.drop_duplicates()

    return returns_df 

def clean_people_table(people: pd.DataFrame) -> pd.DataFrame:
    #title case for regional_manager
    people['regional_manager'] = people['regional_manager'].str.title()

    #strip leading whitespaces in regional_manager
    people['regional_manager'] = people['regional_manager'].str.strip()

    #drop duplicates 
    people = people.drop_duplicates()

    #ensure region is within [West, East, Central, South]
    valid_regions = ['West', 'East', 'Central', 'South']
    people = people[people['region'].isin(valid_regions)]

    return people 

