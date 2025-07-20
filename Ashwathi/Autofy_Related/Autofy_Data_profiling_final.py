#Data profiling for Autofy
# 1. Import all necessary modules
import pandas as pd
from pathlib import Path

# 2. Get the input folder path
folder_path = Path("C:/Users/ASUS/Desktop/ProjFiles")

# 3. Declare the output file name and location
output_file = folder_path / 'summary_of_data_profiling_for_all_files.xlsx'

# 4. Write profiling summary for each CSV file to different sheets
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for file_path in folder_path.glob('*.csv'):
        print("Processing file:", file_path.name)

        # Load the CSV
        df = pd.read_csv(file_path)

        # Create a summary of the columns
        summary = []
        for col in df.columns:
            data_type = df[col].dtype
            null_count = df[col].isnull().sum()
            unique_count = df[col].nunique()

            if pd.api.types.is_numeric_dtype(df[col]):
                col_min = df[col].min()
                col_max = df[col].max()
            else:
                col_min = ""
                col_max = ""

            summary.append({
                'Column': col,
                'Null_Count': null_count,
                'Unique_Count': unique_count,
                'Data_Type': str(data_type),
                'Min': col_min,
                'Max': col_max
            })

        # Convert to DataFrame and write to Excel sheet
        summary_df = pd.DataFrame(summary)
        sheet_name = file_path.stem[:31]  # Excel allows max 31 characters in sheet name
        summary_df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Summary Excel file created successfully!")
