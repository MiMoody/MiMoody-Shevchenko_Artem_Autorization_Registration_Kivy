from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout


class myApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation = 'vertical', size_hint = [.50,.50])

        bl.add_widget(Button(
            text="Первая кнопка",
            font_size=20,
            background_color=[.94,.50,.50,1],
            background_normal=''))

        bl.add_widget(Button(
            text="Вторая кнопка",
            font_size=20,
            background_color=[1,.63,.48,1],
            background_normal=''))

        al.add_widget(bl)
        return al
        
if __name__=="__main__":
    myApp().run()
 
