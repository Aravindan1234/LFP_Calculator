# LFP Pack Calculator

## Overview
The LFP Pack Calculator is a GUI application designed to assist users in managing and calculating information related to Lithium Iron Phosphate (LFP) cells. Users can input data such as capacity and voltage of individual cells, and the application will automatically compute the pack output information, including total pack capacity and cell configuration.

## Features
- User-friendly interface for inputting LFP cell data.
- Automatic calculations for pack capacity and configuration.
- Ability to read from and write to Excel sheets for data management.
- Data validation and formatting utilities to ensure accurate inputs.

## Project Structure
```
lfp-pack-calculator
├── src
│   ├── main.py               # Entry point of the application
│   ├── gui                   # Contains GUI related files
│   │   ├── __init__.py
│   │   └── app.py            # Main GUI class
│   ├── excel                 # Contains Excel file handling
│   │   ├── __init__.py
│   │   ├── reader.py         # Functions to read Excel data
│   │   └── writer.py         # Functions to write Excel data
│   ├── calculations           # Contains calculation logic
│   │   ├── __init__.py
│   │   └── pack_calculator.py # Class for calculating pack information
│   └── utils                 # Utility functions
│       ├── __init__.py
│       └── helpers.py        # Helper functions for various tasks
├── requirements.txt          # Project dependencies
├── .gitignore                # Files to ignore in version control
└── README.md                 # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd lfp-pack-calculator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/main.py
   ```
2. Input the LFP cell data in the provided fields.
3. View the calculated pack output information displayed in the GUI.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.