import pandas as pd
from pathlib import Path

def load_transactions(file_path: str, limit: int | None = None): 

    # Convert the file path into a Path object
    path = Path(file_path) 

    # Check whether the file exists 
    if not path.is_file():
        raise FileNotFoundError(
            f"Transaction dataset not found: {file_path}"
        )

    # Validate the row limit 
    if limit is not None and limit <= 0: 
        raise ValueError(
            "The row limit must be a positive integer."
        )

    # Load transactions from the CSV file 
    df = pd.read_csv(path, nrows = limit) 

    return df

