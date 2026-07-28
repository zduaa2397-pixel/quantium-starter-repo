import pandas as pd
import glob

# Step 1: Find and read all three CSV files in the data folder
all_files = glob.glob("data/*.csv")
df_list = [pd.read_csv(f) for f in all_files]

# Step 2: Combine them into one big DataFrame
combined = pd.concat(df_list, ignore_index=True)

# Step 3: Keep only Pink Morsel rows
pink_only = combined[combined['product'].str.lower() == 'pink morsel'].copy()

# Step 4: Clean the price column (remove '$' and convert to float)
pink_only['price'] = pink_only['price'].replace(r'[\$,]', '', regex=True).astype(float)

# Step 5: Create the Sales column (quantity * price)
pink_only['Sales'] = pink_only['quantity'] * pink_only['price']

# Step 6: Keep only the required columns, and rename to match expected output
output = pink_only[['Sales', 'date', 'region']]
output.columns = ['Sales', 'Date', 'Region']

# Step 7: Save to a new CSV file
output.to_csv('data/formatted_sales_data.csv', index=False)

print("Done! Output saved to data/formatted_sales_data.csv")
print(output.head())