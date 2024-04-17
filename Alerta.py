import requests
import smtplib
import email.message


api_get = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
dict = api_get.json()


cotacao = float(dict['USDBRL']['bid'])
maxima = dict['USDBRL']['high']
minima = dict['USDBRL']['low']
data_verificacao = dict['USDBRL']['create_date']

#Mandar email
def enviar_email(cotacao,maxima,minima):  
    corpo_email = f"""
    <p>Dolar está abaixo de R$ 5,10. Cotação atual: R${cotacao}</p>
    <p>Valor da máxima de R${maxima}</p>
    <p>Valor da mínima R${minima}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Cotação do Dolar"
    msg['From'] = 'teste@gmail.com'
    msg['To'] = 'teste@gmail.com'
    password = 'senha_teste' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.25:
    enviar_email(cotacao,maxima,minima)
else:
    print(cotacao)

