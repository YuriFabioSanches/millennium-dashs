import pandas as pd

def normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    colunas_numericas = ['ValorTotal', 'Quantidade', 'CustoTotal', 'ValorUnitario', 'DescontoTotal', 'AcrescimoTotal', 'CustoUnitario']
    for col in colunas_numericas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(",", ".").astype(float)
    return df
