from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        bl = BoxLayout()
        button1 = Button(text="Og btn1")
        button2 = Button(text="Riins btn2")
        bl.add_widget(button1)
        bl.add_widget(button2)
        return bl


if __name__ == '__main__':
    MyApp().run()
