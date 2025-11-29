"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
Elijah Walker
11/11/2025
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_IN_KM = 1.609344

class ConvertMilesToKilometres(App):
    """ ConvertMilesToKilometres is a Kivy App for changing miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (800, 400)
        self.title = "Convert Miles To Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversions(self, mile):
        """ handle conversion of miles to kilometres, output kilometre to label widget """
        try:
            kilometre = float(mile) * MILES_IN_KM
            self.root.ids.output_label.text = str(kilometre)
        except ValueError:
            pass

    def handle_increment(self, increment):
        try:
            mile = int(self.root.ids.input_number.text)
            mile += increment
            self.root.ids.input_number.text = str(mile)
        except ValueError:
            self.root.ids.input_number.text = "0"

ConvertMilesToKilometres().run()
