import requests
import json

#Lendo o api de clima para minha cidade

site = requests.get("https://api.hgbrasil.com/weather?woeid=457431")
site = site.json()
print("="*35)
print("Previsão de Tempo João Pinheiro MG")
print("="*35)
resultados = site["results"] 
print("Data: ",resultados["date"])
print("Horário: ",resultados["time"])
print("Cidade: ", resultados["city"])
print("Temperatura: ",resultados["temp"],"°C")
print("Condição do Tempo: ",resultados["description"])
print("="*35)
print("Previsão para os próximos dias: ")
resultados_proximos = resultados["forecast"]
for i in range(1,len(resultados_proximos)):
    print("="*35)
    print("Data: ",resultados_proximos[i]["date"])

    if resultados_proximos[i]["weekday"] == "Seg":
        print("Dia: Segunda")
    elif resultados_proximos[i]["weekday"] == "Ter":
        print("Dia: Terça")
    elif resultados_proximos[i]["weekday"] == "Qua":
        print("Dia: Quarta")
    elif resultados_proximos[i]["weekday"] == "Qui":
        print("Dia: Quinta")
    elif resultados_proximos[i]["weekday"] == "Sex":
        print("Dia:  Sexta")
    elif resultados_proximos[i]["weekday"] == "Sab":
        print("Dia: Sábado")
    elif resultados_proximos[i]["weekday"] == "Dom":
        print("Dia: Domingo")

    print("Máximo de Temperatura: ",resultados_proximos[i]["max"],"°C")
    print("Mínimo de Temperatura: ",resultados_proximos[i]["min"],"°C")
    print("Descrição do Tempo: ",resultados_proximos[i]["description"])
print("="*35)