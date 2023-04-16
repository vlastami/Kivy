from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import random

class Kalkulačka(App):
    def build(self):
        hlavni_rozlozeni = BoxLayout(orientation = "vertical")

        for iradek in range(3):
            vnitrni_rozlozeni = BoxLayout(orientation="horizontal")

            for isloupec in range(1,4):
                nahodna_barva = [random.random() for _ in range(3)]
                nahodna_barva.append(1)
                vnitrni_rozlozeni.add_widget(Button(text= f"{iradek*3+isloupec}",
                                                    background_color= nahodna_barva))
            hlavni_rozlozeni.add_widget(vnitrni_rozlozeni)

        return hlavni_rozlozeni


if __name__ == "__main__":
    app = Kalkulačka()
    app.run()
