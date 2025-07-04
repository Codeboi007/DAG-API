import pandas as pd
import numpy as np


def augment(file_path, method):
    df = pd.read_csv(file_path)

    if method == "noise":
        df_aug = df.copy()
        numeric_cols = df_aug.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df_aug[col] += np.random.normal(0, 0.1, size=len(df_aug))
    elif method == "duplicate":
        df_aug = pd.concat([df, df.sample(frac=0.2)], ignore_index=True)
    else:
        df_aug = df

    output_path = file_path.replace(".csv", "_augmented.csv")
    df_aug.to_csv(output_path, index=False)
    return output_path
