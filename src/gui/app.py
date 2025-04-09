import tkinter as tk
from tkinter import ttk
from calculations.pack_calculator import calculate_pack_info

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LFP Pack Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Input fields for series and parallel
        ttk.Label(self.root, text="Number of Cells in Series:").grid(row=0, column=0, padx=10, pady=5)
        self.series_entry = ttk.Entry(self.root)
        self.series_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Number of Cells in Parallel:").grid(row=1, column=0, padx=10, pady=5)
        self.parallel_entry = ttk.Entry(self.root)
        self.parallel_entry.grid(row=1, column=1, padx=10, pady=5)

        # Input fields for cell capacity and voltage
        ttk.Label(self.root, text="Cell Capacity (Ah):").grid(row=2, column=0, padx=10, pady=5)
        self.cell_capacity_entry = ttk.Entry(self.root)
        self.cell_capacity_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Cell Voltage (V):").grid(row=3, column=0, padx=10, pady=5)
        self.cell_voltage_entry = ttk.Entry(self.root)
        self.cell_voltage_entry.grid(row=3, column=1, padx=10, pady=5)

        # Output field
        self.output_label = ttk.Label(self.root, text="Pack Info: ")
        self.output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Calculate button
        calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate_pack)
        calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate_pack(self):
        try:
            # Get inputs from the user
            series = int(self.series_entry.get())
            parallel = int(self.parallel_entry.get())
            cell_capacity = float(self.cell_capacity_entry.get())
            cell_voltage = float(self.cell_voltage_entry.get())

            # Calculate pack info
            pack_info = calculate_pack_info(series, parallel, cell_capacity, cell_voltage)
            self.output_label.config(text=f"Pack Info: {pack_info}")
        except ValueError:
            self.output_label.config(text="Invalid input. Please enter valid numbers.")

    def run(self):
        self.root.mainloop()