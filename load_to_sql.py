from sqlalchemy import create_engine
import pandas as pd

# Database connection string
username = 'username' 
password = 'passowrd' 
host = ''
port = ''  # Default MySQL port
database = ''

# Connection string
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(connection_string)

# Load cleaned data into SQL tables
cleaned_file_names = [
    'data/cleaned/Cleaned_PurchasePricesDec.csv',
    'data/cleaned/Cleaned_BeginvFINAL12312016.csv',
    'data/cleaned/Cleaned_EndinvFINAL12312016.csv',
    'data/cleaned/Cleaned_InvoicePurchases12312016.csv',
    'data/cleaned/Cleaned_PurchasesFINAL12312016.csv',
    'data/cleaned/Cleaned_SalesFINAL12312016.csv'
]


for file_name in cleaned_file_names:
    try:
        df = pd.read_csv(file_name)
        table_name = file_name.split('/')[-1].replace('Cleaned_', '').replace('.csv', '').lower()
        
        # Insert into SQL
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"{table_name} table has been created and populated successfully.")
    except Exception as e:
        print(f"Error loading {file_name}: {e}")        