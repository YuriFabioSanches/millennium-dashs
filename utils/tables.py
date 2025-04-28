import streamlit as st
from utils.filters import aplicar_filtros
from datetime import datetime, timedelta, timezone

def vendas_table(df):
    data_texto = (datetime.now(timezone.utc) - timedelta(days=1)).date().strftime("%d/%m/%Y")
    st.subheader(f"📋 Tabela de Vendas - Data: {data_texto}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        cliente_filtro = st.multiselect("Cliente", options=df["Cliente_NomeFantasia"].unique())
    with col2:
        vendedor_filtro = st.multiselect("Vendedor", options=df["Vendedor"].unique())
    with col3:
        familia_filtro = st.multiselect("Família", options=df["Familia"].unique())
    with col4:
        valor_minimo = st.number_input("Valor Mínimo (R$)", value=0.0, step=10.0)

    df_filtered = aplicar_filtros(df, cliente_filtro, vendedor_filtro, familia_filtro, valor_minimo)

    st.caption(f"🔎 {len(df_filtered)} registros encontrados.")

    colunas = [
        "DataVenda", "Cliente_NomeFantasia", "Vendedor", "Produto_Descricao",
        "Familia", "Quantidade", "ValorUnitario", "ValorTotal"
    ]

    if not df_filtered.empty:
        df_show = df_filtered[colunas].copy()
        df_show["ValorUnitario"] = df_show["ValorUnitario"].map("R$ {:.2f}".format)
        df_show["ValorTotal"] = df_show["ValorTotal"].map("R$ {:.2f}".format)
        df_show["Quantidade"] = df_show["Quantidade"].astype(int)
        st.dataframe(df_show, use_container_width=True)
    else:
        st.warning("Nenhum registro encontrado para os filtros aplicados.")
