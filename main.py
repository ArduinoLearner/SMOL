
from kivy.app import App
from kivy.lang.builder import Builder

import kivy
from kivy.uix.boxlayout import BoxLayout
kivy.require("2.0.0")


code1 = """
BoxLayout:
    orientation: 'vertical'
    
    Button:
        text: "abrir segundo diseño"
        on_press: app.run2()

      
  
"""

code2 = """
BoxLayout:
    orientation: 'vertical'
    
    Button: 
        text: "Lo hiciste n.n"
    
    BoxLayout:
        Button:
            text: "Home"
        Button: 
            text: "X"
            on_press: functions.stahp()
"""



class functions():
    def stahp():
            App._running_app.stop()

class Aptitude2App(App): #Codigo secundario ejecutable
    def build(self):
        return Builder.load_string(code2)
    def run2(self):
        App._running_app.stop()
        AptitudeApp().run()
    
   



class AptitudeApp(App): #Codigo principal de la ventana principal
    def build(self):
        return Builder.load_string(code1)
    
    def run2(self): #Metodo del botón ubicado en principal que correrá secundario 
        App._running_app.stop() #cerrar la app que corre actualmente
        Aptitude2App().run() # Correr la segunda app osi





AptitudeApp().run()

 
