print("here")
import pandas as pd

df = pd.DataFrame({
    'date': pd.date_range('2023-01-01', '2023-12-31'),
    'value': range(1, 366)
})

print(df)
