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
  "recognition_id": "abc123",
  "file_name": "documento.pdf",
  "path_file": "https://url-do-arquivo.pdf"
}
```
