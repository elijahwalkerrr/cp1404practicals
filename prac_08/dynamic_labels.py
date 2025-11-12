"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
Elijah Walker
11/11/2025
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    """"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """ Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Hailey", "Phil", "Claire", "Cameron", "Mitch", "Jay"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root


