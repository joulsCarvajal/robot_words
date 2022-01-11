import urllib.request
import requests
from collections import Counter
from http.client import HTTPConnection

copy = input("Ingresa o copia la url: ")
url = requests.get(copy) 
with open("index.html", "wb") as f:
    f.write(url.content)
url.close()
# conection = urllib.request.urlopen(url).read().decode('utf_8')


print(url.content)

# text = "Hoy me pregunto qué será de ti Te tuve cerca y ahora estás tan lejos Pero prohibirme recordar lo nuestro es imposible Es imposible No me perdono, sé que te perdí Pero expiraron los remordimientos Fui dictador, y el no dejarte ir Debió haber sido mi primer decreto"

# words = text.split()
# count = Counter(words)
# frec_word = count.most_common()[0][0]

# print('La palabra mas frecuente es: %s' % frec_word)


# def run():
#     pass


# def text_repeat(url):
#     data = urllib.request.urlopen(url).read().decode('utf_8')
#     return data





# if __name__ == '__main__':
#     run()