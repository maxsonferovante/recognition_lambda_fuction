# 📄 Lambda Function - Extrator de Texto PDF

## 📋 Sobre

Função AWS Lambda que processa PDFs através de eventos SQS, extraindo texto e salvando em JSON no S3.

## 🚀 Funcionalidades

- Processamento assíncrono via SQS
- Extração de texto página por página
- Armazenamento estruturado em JSON
- Upload automático para S3

## 🛠️ Requisitos

- Python 3.x
- Dependências:
  - boto3
  - pdfplumber
  - requests

## 📊 Estrutura de Dados

### Entrada (SQS Message)

```json
{
  "recognition_id": "abc123",
  "file_name": "documento.pdf",
  "path_file": "https://url-do-arquivo.pdf"
}
```
