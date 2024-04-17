import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for i in range (1,51):

    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    p_get = requests.get(url)

    soup = BeautifulSoup(p_get.content,'html.parser')

    ol = soup.find('ol')
    articles = ol.find_all('article',class_ = 'product_pod')

    for article in articles:

        ##Tútulo
        img = article.find('img')
        title = img.attrs['alt'] #Pega o atributo alt da classe img

        #Estrelas
        stars = article.find('p')['class'][1]
        if stars == "One":
            stars = 1
        elif stars == "Two":
            stars = 2
        elif stars == "Three":
            stars = 3
        elif stars == "Four":
            stars = 4
        else:
            stars = 5

        #Preço
        price = article.find('p',class_ = 'price_color').text[1:]
        price = float(price)

        #Faz um append criando uma lista de vetores de Livros
        books.append([title,stars,price])

df = pd.DataFrame(books,columns=['Titulo','Avaliacao','Preco'])
df.to_csv('books.csv')




