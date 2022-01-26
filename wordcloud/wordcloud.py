#Wordcloud é um tipo de visualização que enriquece com imagens,
#das palavras mais preponentes nos site de AirBnB, para as cidades mais procurados,
import pandas as pd
import matplotlib.pyplot as plt
import wordcloud 
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

data_london = 'http://data.insideairbnb.com/united-kingdom/england/london/2021-12-07/data/listings.csv.gz'

df = pd.read_csv (data_london)

#realizar a quantidade de valores null ou ausentes
print("Esses são valores ausentes ou null:",df.summary.isnull().sum())
#função para eliminar as colunas com valores ausentes
summary = df.dropna(subset=['summary'], axis = 0) ['summary']
#para poder formar a wordcloud é preciso concatenar todas strings
#como se fosse uma única linha.
all_summary= " ".join(s for s in summary)
#Para wordcloud em português é preciso acrescentar palavras na lista STOPWORDS
stopwords=set(STOPWORDS)
stopwords.update(["da","meu","em","você","de","ao","os","as","e","que","como"])
#Agora é necessário criar uma lista para tirar as palavras mais repetidas..STOPWORDS
stopwords = set(STOPWORDS)

#Agora é só chamar a função para gerar a wordcloud
wordcloud = WordCloud(stopwords=stopwords, background_color = "white").generate(all_summary)
#Abaixo a formatação da imagem final
fig, ax = plt.subplots(figsize=(12,6))
ax.imshow(wordcloud, Interpolation = 'bilinear')
plt.tight_layout()
#Para salvar a imagem obtida
wordcloud.to_file("img/first_review.png")