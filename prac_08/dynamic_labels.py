"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
Elijah Walker
11/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """ Dynamic Labels is a Kivy app that dynamically displays a list of names"""
    def __init__(self, **kwargs):
        """ Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Hailey", "Phil", "Claire", "Cameron", "Mitch", "Jay"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates a label for every name in list. """
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main_box.add_widget(temp_label)

DynamicLabelsApp().run()



