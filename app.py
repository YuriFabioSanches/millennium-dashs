import streamlit as st
from services.api_service import get_vendas
from utils.charts import (
    vendas_bar_chart,
    produtos_mais_vendidos_chart,
    vendas_familia_pie_chart,
    vendas_vendedor_chart,
    rentabilidade_bar_chart
)
from utils.tables import vendas_table
from utils.data_cleaning import normalize_dataframe
import pandas as pd
from datetime import datetime, timedelta, timezone

st.set_page_config(page_title="Dashboard de Vendas", layout="wide", initial_sidebar_state="collapsed")

st.title("📊 Dashboard de Vendas")

# ⚡ Data automática: dia anterior
data_inicial = (datetime.now(timezone.utc) - timedelta(days=1)).date()
data_final = data_inicial

@st.cache_data
def carregar_dados(data_inicial, data_final):
    vendas = get_vendas(data_inicial, data_final)
    if vendas:
        df = pd.DataFrame(vendas)
        return normalize_dataframe(df)
    return pd.DataFrame()

df_vendas = carregar_dados(data_inicial, data_final)

if not df_vendas.empty:
    with st.container():
        data_texto = data_inicial.strftime("%d/%m/%Y")
        st.subheader(f"Resumo de Vendas - Data: {data_texto}")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Vendas", f"R$ {df_vendas['ValorTotal'].sum():,.2f}")
        col2.metric("Quantidade Vendida", f"{df_vendas['Quantidade'].sum():,.0f} itens")
        ticket_medio = df_vendas['ValorTotal'].sum() / df_vendas['Quantidade'].sum()
        col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")

    st.divider()

    with st.container():
        st.subheader("Gráficos de Análise")

        rentabilidade_bar_chart(df_vendas)
        produtos_mais_vendidos_chart(df_vendas)
        vendas_familia_pie_chart(df_vendas)
        vendas_vendedor_chart(df_vendas)
        vendas_bar_chart(df_vendas)

    st.divider()

    vendas_table(df_vendas)
else:
    st.warning("Nenhuma venda encontrada para o dia anterior.")
