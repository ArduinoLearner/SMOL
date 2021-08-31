from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.tabbedpanel import TabbedPanel
import kivy
kivy.require("2.0.0")


code = """

<menu@GridLayout>:
    padding: 10
    cols: 3
    
    Button: 
        text: "Save"
        on_press: app.seiv()
  
    Button:
        text: "Open"
        on_press: app.gitopen()
    
    Button:
        text: "Run"
        on_press:  app.seiv(), app.run2()
    

    Button: 
        text: "DelAll"
        on_press: app.deleite()
    Button:
        text: "Tab"
        on_press: app.tabu()
    
    Button: 
        text: "Tab2"
        on_press: app.tabu() , app.tabu()

    

<menu2@GridLayout>:
    cols: 2
    Button:
    Button:
    Button:
    Button:
    Button:
    Button:

                        


BoxLayout:

    spacing: 20
    padding: 20
    TextInput: 
        id: txin1
    menu:
	    pos_hint: {"y": .7}
        size_hint_y: .3
        size_hint_x: .5

"""

class AptitudeApp(App): #Codigo principal de la ventana principal
    def build(self):
        return Builder.load_string(code)
        
    def seiv(self):
        f = open("test.txt","w")
        text = self.root.ids.txin1.text 
        print(text)
        f.write(text)
        f.close()
    
    def run2(self):
        AptitudeApp._running_app.stop()
        AptitudeApp2().run()

    def gitopen(self):
        f = open("test.txt","r")
        stringa = f.read()
        self.root.ids.txin1.text = stringa
    
    def tabu(self):
        self.root.ids.txin1.text =  self.root.ids.txin1.text + "    "
    
    
    def deleite(self):
        self.root.ids.txin1.text = ""
    



class AptitudeApp2(App):
    def build(self):
        f = open("test.txt","r")
        return Builder.load_string(str(f.read())); f.close()






AptitudeApp().run()

 
