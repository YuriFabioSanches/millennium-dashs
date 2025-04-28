import streamlit as st
import plotly.express as px

# Paleta de cores segura e bonita
PALETA_CORES = px.colors.qualitative.Safe

def vendas_bar_chart(df):
    top_clientes = df.groupby("Cliente_NomeFantasia")["ValorTotal"].sum().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(
        top_clientes,
        x="ValorTotal",
        y="Cliente_NomeFantasia",
        orientation='h',
        labels={"ValorTotal": "Valor Total (R$)", "Cliente_NomeFantasia": "Cliente"},
        title="Top 10 Clientes - Valor Total de Vendas (R$)",
        color="Cliente_NomeFantasia",
        color_discrete_sequence=PALETA_CORES
    )
    fig.update_layout(
        xaxis_tickprefix='R$ ',
        xaxis_tickformat=',.2f',
        yaxis=dict(title='Cliente', automargin=True),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

def produtos_mais_vendidos_chart(df):
    top_produtos = df.groupby("Produto_Descricao")["Quantidade"].sum().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(
        top_produtos,
        x="Quantidade",
        y="Produto_Descricao",
        orientation='h',
        labels={"Quantidade": "Quantidade Vendida", "Produto_Descricao": "Produto"},
        title="Top 10 Produtos Mais Vendidos",
        color="Produto_Descricao",
        color_discrete_sequence=PALETA_CORES
    )
    fig.update_layout(
        xaxis_tickformat=',.0f',
        yaxis=dict(title='Produto', automargin=True),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

def vendas_familia_pie_chart(df):
    vendas_familia = df.groupby("Familia")["ValorTotal"].sum().sort_values(ascending=False)

    fig = px.pie(
        values=vendas_familia.values,
        names=vendas_familia.index,
        title="Distribuição de Vendas por Família de Produto (%)",
        hole=0.4,  # rosquinha
        color_discrete_sequence=PALETA_CORES
    )
    fig.update_layout(
        showlegend=True,
        legend_title_text="Família"
    )
    st.plotly_chart(fig, use_container_width=True)

def vendas_vendedor_chart(df):
    vendas_vendedor = df.groupby("Vendedor")["ValorTotal"].sum().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(
        vendas_vendedor,
        x="Vendedor",
        y="ValorTotal",
        labels={"ValorTotal": "Valor Total (R$)", "Vendedor": "Vendedor"},
        title="Top Vendedores - Valor Total de Vendas (R$)",
        color="Vendedor",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig.update_layout(
        yaxis_tickprefix='R$ ',
        yaxis_tickformat=',.2f',
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

def rentabilidade_bar_chart(df):
    df['Rentabilidade'] = df['ValorTotal'] - df['CustoTotal']
    top_rentabilidade = df.groupby("Produto_Descricao")["Rentabilidade"].sum().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(
        top_rentabilidade,
        x="Rentabilidade",
        y="Produto_Descricao",
        orientation='h',
        labels={"Rentabilidade": "Rentabilidade (R$)", "Produto_Descricao": "Produto"},
        title="Top 10 Produtos por Rentabilidade (R$)",
        color="Produto_Descricao",
        color_discrete_sequence=PALETA_CORES
    )
    fig.update_layout(
        xaxis_tickprefix='R$ ',
        xaxis_tickformat=',.2f',
        yaxis=dict(title='Produto', automargin=True),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
