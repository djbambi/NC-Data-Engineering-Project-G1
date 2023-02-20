import pandas as pd

def csv_to_parquet(file_name):
    idx = file_name.rfind(".")
    name_prefix=file_name[0:idx]
    parq_name = name_prefix + ".parquet"
    df = pd.read_csv(file_name)
    df.to_parquet(parq_name, engine="pyarrow")
    df = pd.read_parquet(parq_name, engine="pyarrow")
    print(df.head(3))
    pass

f_name = input('specify filename: ')
csv_to_parquet(f_name)