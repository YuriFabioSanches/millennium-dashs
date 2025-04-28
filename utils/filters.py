import pandas as pd

def aplicar_filtros(df, cliente_filtro, vendedor_filtro, familia_filtro, valor_minimo):
    if cliente_filtro:
        df = df[df["Cliente_NomeFantasia"].isin(cliente_filtro)]
    if vendedor_filtro:
        df = df[df["Vendedor"].isin(vendedor_filtro)]
    if familia_filtro:
        df = df[df["Familia"].isin(familia_filtro)]
    if valor_minimo > 0:
        df = df[df["ValorTotal"] >= valor_minimo]
    return df
