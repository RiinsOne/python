# from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config


Config.set('kivy', 'keyboard_mode', 'systemanddock')


from kivymd.app import MDApp


# Window.size = (720, 1280)
Window.size = (480, 853)


def get_ingridients(m):
    nitro = str(10 * m / 1000)
    salt = str(15 * m / 1000)
    starts = str(0.5 * m / 1000)
    dextrose = str(5 * m / 1000)
    salting_time = str(round(m / 500 * 2))

    return {'nitro': nitro, 'salt': salt, 'starts': starts, 'dextrose': dextrose, 'time': salting_time}


class Container(GridLayout):

    def calculate(self):
        try:
            mass = int(self.text_input.text)
        except:
            mass = 0

        ingridients = get_ingridients(mass)

        self.salt.text = ingridients.get('salt') + ' + 5'
        self.nitro.text = ingridients.get('nitro')
        self.sugars.text = ingridients.get('dextrose')
        self.starts.text = ingridients.get('starts')
        self.time.text = ingridients.get('time')



class MyApp(MDApp):
    # title = 'Coppa app'

    def build(self):
        # return Container()
        return MDLabel(text='Riins', haling='center')


if __name__ == '__main__':
    MyApp().run()
