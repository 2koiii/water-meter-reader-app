from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (360, 640)

class MainLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        Builder.load_file("main.kv")
        return MainLayout()

    def import_action(self, instance):
        print("Import button pressed")
        self.root.ids.title_label.text = "Import Action Performed"


if __name__ == '__main__':
    MyApp().run()
