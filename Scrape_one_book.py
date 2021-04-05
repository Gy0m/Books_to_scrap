import requests
# import ipdb
from bs4 import BeautifulSoup
import csv
# links = []
# for i in range(51):
# url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
url = 'http://books.toscrape.com/catalogue/page-1.html'

response = requests.get(url)
print(response)

if response.ok:
    # print('Page: ' + str(i))
    links = []
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.findAll('div', class_="image_container")
    for div in divs:
        a = div.find('a')
        link = a['href']
        links.append('http://books.toscrape.com/' + link)  # récupère les liens des images
    print(len(links))  # compte le nombre de liens

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')  # copie les liens dans un fichier csv et retour à la ligne

with open('urls.csv', 'r') as file:

    for url in file:

        url = url.strip()
        response = requests.get(url)
        if response.ok:
            def scrape():
                soup = BeautifulSoup(response.text, 'lxml')
                title = soup.find('div', {'class': 'product_main'}).find('h1')  # récupère les titres des livres
                stars = soup.get('p', {'class': 'star-rating'}).get('class')
                category = soup.find('ul', {'class': 'breadcrumb'}).find('a')
                image_url = soup.find('div', {'class': 'item'}).find('img')
                # def get_book_info(book_url):
                table = soup.find('table', {'class': 'table table-striped'})  # identifie la classe du tableau
                table_ths = table('th')  # crée une variable avec les infos de th
                table_tds = table.find_all('td')  # crée une variable avec les infos de td

                ths = []

                for i, th in enumerate(table_ths):  # itère les informations du tableau th
                    ths.append(th.text)  # les ajoutes au dict ths

                tds = []

                for i, td in enumerate(table_tds):
                    tds.append(td.text)

                csv_columns = ['Titre', 'Intitulé', 'Informations', 'Stars', 'Category', 'Image']
                dict = [
                    {
                        'Titre': title.text, 'Intitulé': ths, 'Informations': tds, 'Stars': stars, 'Category': category, 'Image': image_url
                    }
                ]

                csv_file = "product_information.csv"
                with open(csv_file, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                    writer.writeheader()
                    for data in dict:
                        writer.writerow(data)
                        print(data)
                        # writer.writerow(get_book_info(book_url))

# for category in categories:
#     with open('product_information.csv', 'r') as books:  #ouvrir le fichier csv
# for books in get_books(url_books):
# #ecrire dans le csv
