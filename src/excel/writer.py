def write_to_excel(file_path, data):
    import pandas as pd

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file
    df.to_excel(file_path, index=False)

def append_to_excel(file_path, data):
    import pandas as pd

    # Load existing data
    try:
        existing_data = pd.read_excel(file_path)
    except FileNotFoundError:
        existing_data = pd.DataFrame()

    # Create a DataFrame from the new data
    new_data = pd.DataFrame(data)

    # Append new data to existing data
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Write the updated DataFrame back to the Excel file
    updated_data.to_excel(file_path, index=False)