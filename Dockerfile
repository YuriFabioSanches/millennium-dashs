# Use a imagem oficial do Python
FROM python:3.12-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia o arquivo requirements para dentro do container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o restante da aplicação
COPY . .

# Ajuste de configurações do Streamlit
# Vamos criar um config.toml dentro do container também, se precisar

# Expor a porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar o app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
