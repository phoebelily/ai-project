import os
from openai import AzureOpenAI




client = AzureOpenAI(
    api_key=os.getenv("API-KEY"),
    api_version="2024-02-01",
    azure_endpoint = os.getenv("ENDPOINT")
    )
deployment_name=os.getenv("DEPLOYMENT-NAME")
print('Sending a question to azure-openai')
start_phrase = ('whats the capital of france' )
response = client.chat.completions.create(model=deployment_name, messages=[{"role": "user", "content": start_phrase}])
print(response.choices[0].message.content)

