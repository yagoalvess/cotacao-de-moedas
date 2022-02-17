import requests
import json
from tkinter import *


## Pegar a cotação por meio de uma API ##
def cotacao_btc():
    moeda = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
    moeda = moeda.json()
    texto_resultado = """
    Moedas: {} para {}
    High: {}
    Low: {}
    Bid: {}
    Ask: {}
    Create Date: {}
        
    """.format(moeda["BTCBRL"]['code'],
               moeda["BTCBRL"]['codein'],
               moeda["BTCBRL"]['high'],
               moeda["BTCBRL"]['low'],
               moeda["BTCBRL"]['bid'],
               moeda["BTCBRL"]['ask'],
               moeda["BTCBRL"]['create_date'])

    texto_btc["text"] = texto_resultado



def cotacao_usd():
    moeda = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    moeda = moeda.json()
    texto_resultado = """
        Moedas: {} para {}
        High: {}
        Low: {}
        Bid: {}
        Ask: {}
        Create Date: {}

        """.format(moeda["USDBRL"]['code'],
                   moeda["USDBRL"]['codein'],
                   moeda["USDBRL"]['high'],
                   moeda["USDBRL"]['low'],
                   moeda["USDBRL"]['bid'],
                   moeda["USDBRL"]['ask'],
                   moeda["USDBRL"]['create_date'])
    texto_usd["text"] = texto_resultado


def cotacao_eur():
    moeda = requests.get("https://economia.awesomeapi.com.br/last/EUR-BRL")
    moeda = moeda.json()
    texto_resultado = """
            Moedas: {} para {}
            High: {}
            Low: {}
            Bid: {}
            Ask: {}
            Create Date: {}

            """.format(moeda["EURBRL"]['code'],
                       moeda["EURBRL"]['codein'],
                       moeda["EURBRL"]['high'],
                       moeda["EURBRL"]['low'],
                       moeda["EURBRL"]['bid'],
                       moeda["EURBRL"]['ask'],
                       moeda["EURBRL"]['create_date'])
    texto_eur["text"] = texto_resultado





## Interface grafica ##

janela = Tk()
janela.configure(background="#dde")
janela.title('Cotação')
janela.geometry('500x600')

texto_btc = Label(janela, text="")
texto_btc.grid(padx=150,pady=10,row=0,column=0)

texto_usd = Label(janela,text="")
texto_usd.grid(padx=150,pady=10,row=1,column=0)

texto_eur = Label(janela,text="")
texto_eur.grid(padx=150,pady=10,row=2,column=0)


botao_btc = Button(janela, text="Cotação BTC", command=cotacao_btc)
botao_btc.grid(column=0,row=3,padx=200)

botao = Button(janela, text="Cotação USD", command=cotacao_usd)
botao.grid(column=0,row=4)

botao = Button(janela,text="Cotacao EUR", command=cotacao_eur)
botao.grid(column=0,row=5)


janela.mainloop()
