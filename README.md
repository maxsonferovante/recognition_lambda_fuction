# Lambda Function - Extrator de Texto PDF

[![Publish Docker image in Docker Hub](https://github.com/maxsonferovante/recognition_lambda_fuction/actions/workflows/workflow_build.yaml/badge.svg)](https://github.com/maxsonferovante/recognition_lambda_fuction/actions/workflows/workflow_build.yaml)

## Sobre

Função AWS Lambda que processa PDFs através de eventos SQS, extraindo texto e salvando em JSON no S3.

## Funcionalidades

- Processamento assíncrono via SQS
- Extração de texto página por página
- Armazenamento estruturado em JSON
- Upload automático para S3

## Requisitos

- Python 3.x
- Dependências:
  - boto3
  - pdfplumber
  - requests

## Estrutura de Dados

### Entrada (SQS Message)

```json
{
  "recognition_id": "679d796b6795b4c2a8396eab",
  "file_name": "documento.pdf",
  "path_file": "https://TempLinkShare.s3.us-east-005.backblazeb2.com/tempLinkShape/679d7aa60879b7d112f7ba32/001_451_2024_edital_gratuidade_tecnico_(1).pdf"
}
```

### Testes Locais

Para criar a lambda localmente usando Docker:

```
docker compose up --build --watch
```

Para testar localmente usando o runtime da AWS Lambda:

```bash
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{\"recognition_id\": \"679ff8dfc96fad021724501a\", \"file_name\": \"profile_(3).pdf\", \"extension\": \"pdf\", \"path_file\": \"https://TempLinkShare.s3.us-east-005.backblazeb2.com/tempLinkShape/679ff8dfc96fad021724501a/profile_(3).pdf\"}'
```

Isso simula uma invocação da função Lambda em ambiente local.
