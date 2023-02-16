import requests
import bs4

def pilotos_socio():

    pagina = requests.get("https://www.dazn.com/es-ES/news/deportes-de-motor/quienes-son-todos-los-campeones-del-mundo-de-motogp-de-la-historia/1nyxedlewzyu419r7bufqucum4")

    soup = bs4.BeautifulSoup(pagina.content,"html.parser")

    pilotos = soup.find_all("tr")[1:]

    motogp = {
        "temporada": None,
        "categoria": None,
        "nombre": None,
        "pais" : None,
        "marca_moto" : None
    }
    list_pilotos = []



    for piloto in pilotos:

        dic_piloto = motogp.copy()

        # Metemos la temporada
        temporada =  piloto.find("th").text
        dic_piloto["temporada"] = int(temporada)



       #Metemos la categoria
        categoria = piloto.find_all("td")[0].text
        dic_piloto["categoria"] = categoria


        #Metemos el nombre
        nombre = piloto.find_all("td")[1].text
        dic_piloto["nombre"] = nombre

        #Metemos el pais
        pais = piloto.find_all("td")[2].text
        dic_piloto["pais"] = pais

        #metemos la marca de moto
        marca_moto= piloto.find_all("td")[3].text
        dic_piloto["marca_moto"] = marca_moto

        list_pilotos.append(dic_piloto)

    print("Scraping completo")

    return list_pilotos






