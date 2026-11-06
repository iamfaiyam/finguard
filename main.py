from src.ingestion import load_transactions

file_path = "data/raw/PS_20174392719_1491204439457_log.csv"

df = load_transactions(file_path, limit = 1000)

print("Transactions loaded:", len(df))
print("Columns:", df.columns.to_list())
print("\nFirst five transactions:")
print(df.head())

