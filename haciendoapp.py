import kivy
import kivymd
import os
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.button import Button
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.button.button import MDRoundFlatIconButton
from volcado_datos import *
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel


def obtener_datos_tabla(tabla):

    list_pilotos = consultar_datos()

    for piloto in list_pilotos:
        tabla.row_data.append(piloto)

def mostrar_formulario(panel_informacion):

    panel_informacion.clear_widgets()

    formulario = GridLayout(rows=5, cols=1)
    temporada = MDTextField(hint_text="Temporada",
                            helper_text="En que año fue campeón",
                            helper_text_mode="on_focus")
    formulario.add_widget(temporada)

    categoria = MDTextField(hint_text="Categoría",
                            helper_text="En que categoría corre"
                                        ,
                            helper_text_mode="on_focus")
    formulario.add_widget(categoria)

    nombre = MDTextField(hint_text="Nombre",
                         helper_text="Nombre del piloto",
                         helper_text_mode="on_focus")
    formulario.add_widget(nombre)

    pais = MDTextField(hint_text="País",
                       helper_text="Mete un país churra",
                       helper_text_mode="on_focus")
    formulario.add_widget(pais)

    marca_moto = MDTextField(hint_text="Marca de moto",
                             helper_text="Mete motito (la marca en)",
                             helper_text_mode="on_focus")
    formulario.add_widget(marca_moto)
    panel_informacion.add_widget(formulario)

def guardar_en_bbdd(panel_informacion):

    nuevo_piloto = dict()
    nuevo_piloto["temporada"] = panel_informacion.children[0].children[4].text
    nuevo_piloto["categoria"] =  panel_informacion.children[0].children[3].text
    nuevo_piloto["nombre"] =  panel_informacion.children[0].children[2].text
    nuevo_piloto["pais"] =  panel_informacion.children[0].children[1].text
    nuevo_piloto["marca_moto"] =  panel_informacion.children[0].children[0].text

    insertar(nuevo_piloto)

class Aplicacion(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        ventana = Screen(name="Pilotos APP")

        panel_principal = BoxLayout(orientation="vertical")

        panel_botones_arriba = BoxLayout(size=(100,80),
                                         size_hint=(None, None),
                                         padding= (90,10),
                                         spacing=30)



        panel_informacion = BoxLayout(padding=(50,20)
                                      )



        tabla = MDDataTable(
            column_data=[
                ("Id", dp(20)),
                ("Temporada", dp(20)),
                ("Categoría",dp(20)),
                ("Nombre", dp(30)),
                ("País", dp(20)),
                ("Marca moto", dp(20)),
            ],use_pagination=True,
            check=True

        )




        boton1 =  MDRoundFlatIconButton(text="Cargar",
                                        md_bg_color="white",
                                        size=(50,50),
                                        text_color="black",
                                        icon="motorbike",
                                        line_color="black",
                                        icon_color="black"
        )
        boton1.bind(on_press=lambda a: insertar_datos())

        boton2 = MDRoundFlatIconButton(text="Borrar",
                                       md_bg_color="white",
                                       text_color="black",
                                       icon="delete",
                                       line_color="black",
                                       icon_color="black"
                                       )


        boton3 = MDRoundFlatIconButton(text="Añadir",
                                       md_bg_color="white",
                                       text_color="black",
                                       icon="account-plus",
                                       line_color="black",
                                       icon_color="black"
                                       )
        boton3.bind(on_press=lambda a: mostrar_formulario(panel_informacion))
        boton4 = MDRoundFlatIconButton(text="Mostrar",
                                       md_bg_color="white",
                                       text_color="black",
                                       icon="eye",
                                       line_color="black",
                                       icon_color="black" )

        boton4.bind(on_press=lambda a: obtener_datos_tabla(tabla))

        boton5 = MDRoundFlatIconButton(text="Guardar",
                                       md_bg_color="white",
                                       text_color="black",
                                       icon="plus",
                                       line_color="black",
                                       icon_color="black"
                                       )

        boton5.bind(on_press=lambda a: guardar_en_bbdd(panel_informacion))

        panel_botones_arriba.add_widget(boton1)
        panel_botones_arriba.add_widget(boton2)
        panel_botones_arriba.add_widget(boton3)
        panel_botones_arriba.add_widget(boton4)
        panel_botones_arriba.add_widget(boton5)
        panel_principal.add_widget(panel_botones_arriba)

        panel_informacion.add_widget(tabla)
        panel_principal.add_widget(panel_informacion)

        ventana.add_widget(panel_principal)




        return ventana




Aplicacion().run()