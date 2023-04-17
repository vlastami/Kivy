from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#TODO: ošetřit desetinnou čárku


class Kalkulacka(App):
    def stisk_tlacitka(self, instance):
        if instance.text == "CE":
            self.displej.text = ""
        elif not self.displej.text and instance.text in self.operatory:
            return
        elif instance.text in self.operatory and self.displej.text[-1] in self.operatory:
            symboly_displeje = list(self.displej.text)
            symboly_displeje[-1] = instance.text
            novy_text_displeje = "".join(symboly_displeje)
            self.displej.text = novy_text_displeje
        else:
            self.displej.text += instance.text


    def vypocet(self, instance):
        zadani = self.displej.text
        if zadani and zadani[-1] not in self.operatory:
            self.displej.text = str(eval(zadani))


    def build(self):
        self.operatory = ["+", "-", "*", "/"]
        tlacitka = [["7", "8", "9", "/",],
                    ["4", "5", "6", "*"],
                    ["1", "2", "3", "-"],
                    [".", "0", "CE", "+"]]
        hlavni_rozlozeni = BoxLayout(
            orientation = "vertical",
            spacing = 0
        )

        self.displej = TextInput(
            multiline = False,
            readonly = True,
            halign = "right",
            font_size = 55,
            background_color = [0,2,0.4,1]
        )

        hlavni_rozlozeni.add_widget(self.displej)

        for iradek in range(len(tlacitka)):
            vnitrni_rozlozeni = BoxLayout(orientation = "horizontal")
            for isloupec in range(len(tlacitka[iradek])):
                tlacitko = Button(text = tlacitka[iradek][isloupec])
                tlacitko.bind(on_press = self.stisk_tlacitka)
                vnitrni_rozlozeni.add_widget(tlacitko)
            hlavni_rozlozeni.add_widget(vnitrni_rozlozeni)
        tlacitko_rovnitko = Button(text = "=")
        tlacitko_rovnitko.bind(on_press = self.vypocet)



        hlavni_rozlozeni.add_widget(tlacitko_rovnitko)
        return hlavni_rozlozeni


if __name__ == '__main__':
    Kalkulacka().run()
