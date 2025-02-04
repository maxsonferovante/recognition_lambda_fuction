# syntax=docker/dockerfile:1

# Usando a imagem base da AWS Lambda para Python
FROM public.ecr.aws/lambda/python:3.13

# Evita que o Python escreva arquivos pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Impede o Python de fazer buffer no stdout e stderr
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho
WORKDIR /app

# Cria um usuário não privilegiado para executar o aplicativo
ARG UID=10001
RUN useradd \
    --no-create-home \
    --home-dir "/nonexistent" \
    --shell "/sbin/nologin" \
    --uid "${UID}" \
    appuser

# Instala as dependências
# Utiliza um cache mount para /root/.cache/pip para acelerar builds subsequentes
# Utiliza um bind mount para requirements.txt para evitar copiá-lo nesta camada
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Altera para o usuário não privilegiado
USER appuser

# Copia o código-fonte para o container
COPY . .

# Define o handler da função Lambda
CMD ["lambda_function.lambda_handler"]
