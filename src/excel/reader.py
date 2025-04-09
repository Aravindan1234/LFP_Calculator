import pandas as pd

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_cell_data(self):
        try:
            data = pd.read_excel(self.file_path)
            return data
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None