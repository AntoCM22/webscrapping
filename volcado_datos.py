import mysql.connector as bbdd
from we_scrapping import *


def insertar_datos():

    lista_pilotos = pilotos_socio()

    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="motos",
                            user="root",
                            password="1234",
                            autocommit=True
                            )

    cursor = conexion.cursor()



    cursor.execute("delete from motogp where id is not null")

    cursor.execute("alter table motogp auto_increment=1")

    script_insert = "insert into motogp (temporada,categoria,nombre,pais,marca_moto)" "values (%s,%s,%s,%s,%s)"


    for piloto in lista_pilotos:

        cursor.execute(script_insert,(piloto["temporada"],
                                      piloto["categoria"],
                                      piloto["nombre"],
                                      piloto["pais"],
                                      piloto["marca_moto"]))

    print("Datos volcados correctamente")




def consultar_datos():


    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="motos",
                            user="root",
                            password="1234",
                            autocommit=True
                            )

    cursor = conexion.cursor()

    cursor.execute("select * from motogp ")

    list_pilotos=[]

    for dato in cursor.fetchall():
        pilotos = tuple([dato[0], dato[1], dato[2], dato[3], dato[4] , dato[5]])
        list_pilotos.append(pilotos)

    return list_pilotos



def insertar(nuevo_piloto):

    conexion = bbdd.connect(host="localhost",
                            port=3306,
                            database="motos",
                            user="root",
                            password="1234",
                            autocommit=True
                            )

    cursor = conexion.cursor()

    script_insert = "insert into motogp (temporada,categoria,nombre,pais,marca_moto)" "values (%s,%s,%s,%s,%s)"

    cursor.execute(script_insert, (nuevo_piloto["temporada"],
                                   nuevo_piloto["categoria"],
                                   nuevo_piloto["nombre"],
                                   nuevo_piloto["pais"],
                                   nuevo_piloto["marca_moto"]))











