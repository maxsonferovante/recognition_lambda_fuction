import json
import boto3
import pdfplumber
import requests

# Inicializa o cliente do S3
s3_client = boto3.client('s3')

def download_file(url, local_path):
    """ Baixa o arquivo PDF do link S3 e salva localmente. """
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, "wb") as file:
            file.write(response.content)
    else:
        raise Exception(f"Erro ao baixar o arquivo: {response.status_code}")

def extract_text_from_pdf(file_path):
    """ Extrai o texto de um PDF página por página. """
    extracted_text = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            extracted_text.append({"page": i, "text": page.extract_text() or ""})
    return extracted_text

def lambda_handler(event, context):
    try:
        # Extrai os dados do evento SQS
        record = event["Records"][0]
        body = json.loads(record["body"])
        
        recognition_id = body["recognition_id"]
        file_name = body["file_name"]
        file_url = body["path_file"]
        
        # Define o caminho do arquivo local
        local_pdf_path = f"/tmp/{file_name}"
        local_json_path = f"/tmp/{recognition_id}.json"
        
        # Baixa o arquivo PDF
        download_file(file_url, local_pdf_path)
        
        # Extrai o texto do PDF
        extracted_text = extract_text_from_pdf(local_pdf_path)
        
        # Salva os dados extraídos em um JSON
        result_data = {"recognition_id": recognition_id, "pages": extracted_text}
        with open(local_json_path, "w") as json_file:
            json.dump(result_data, json_file)
        
        # Define o bucket e o nome do arquivo JSON no S3
        bucket_name = "meu-bucket-de-destino"
        s3_key = f"extracted-data/{recognition_id}.json"
        
        # Envia o JSON extraído para o S3
        s3_client.upload_file(local_json_path, bucket_name, s3_key)
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Arquivo processado e salvo com sucesso!", "s3_key": s3_key})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
