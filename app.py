import requests
import json

api_url = "http://www.integre.net.br/iwa/Api/NFSe/Consultar"
headers = {'Content-Type': 'application/json', 'Authorization': 'Basic MzdhM2E4NzItMjU5OS00NjA2LThkNzktYjRjMzZkM2VkODZjOmE2YWQ3OTM3LTcxYTMtNDIzNy05MDAwLWMzMDBhMmI3NGIzMg=='}
body = {"nNF": "84", "serie": "3", "nomChaveAcesso": "VJmLpmCrYlrOw34YuHZtZdBYIO75I0l9"}
response = requests.post(api_url, json=body, headers=headers)
dados = json.dumps(response.json())

dadosjson = json.loads(dados[1:-1])

print(dadosjson["DocNumero"] + " - " + dadosjson["DocSitDescricao"])
print(dadosjson["Resumo"]["DocNomeDestinatario"])
print(dadosjson["NFSe"]["NFSeNumero"] + " - " + dadosjson["NFSe"]["NFSeCodVerificacao"])


nome = input("Escreva seu nome: ")

print('Seu nome é:', nome)
