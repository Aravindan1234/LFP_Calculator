def calculate_pack_info(series, parallel, cell_capacity=3.2, cell_voltage=3.2):
    """
    Calculate the pack information based on the number of cells in series and parallel,
    as well as the capacity and voltage of individual cells.

    Args:
        series (int): Number of cells in series.
        parallel (int): Number of cells in parallel.
        cell_capacity (float): Capacity of a single cell in Ah (default is 3.2 Ah).
        cell_voltage (float): Voltage of a single cell in V (default is 3.2 V).

    Returns:
        str: Pack capacity and voltage information.
    """
    pack_capacity = parallel * cell_capacity  # Total capacity in Ah
    pack_voltage = series * cell_voltage  # Total voltage in V
    return f"Capacity: {pack_capacity} Ah, Voltage: {pack_voltage} V"