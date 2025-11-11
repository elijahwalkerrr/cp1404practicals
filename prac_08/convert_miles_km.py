"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
Elijah Walker
Started 11/11/2025
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKilometres(App):
    """ ConvertMilesToKilometres is a Kivy App for changing miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 400)
        self.title = "Convert Miles To Kilometres"
        self.root = Builder.load_file('convert_miles_km.py')
        return self.root

    def handle_conversions(self, mile):
        """ handle conversion of miles to kilometres, output kilometre to label widget """
        try:
            kilometre = float(mile) * 1.609344
            self.root.ids.output_label.text = str(kilometre)
        except ValueError:
            pass


ConvertMilesToKilometres().run()
