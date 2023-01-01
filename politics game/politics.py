#!/usr/bin/env python3
'''
Minimal Kivy program example
'''
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty, ListProperty

kivy.require('2.0.0')

class Policies(BoxLayout):

    def gas_tax(self, value):
        self.ids['gas_tax_label_id'].text = "Gas Tax at " + str(int(value)) + '%'

class Outcomes(BoxLayout):
    pass

class Popularity(BoxLayout):
    pass

class Main(BoxLayout):
    pass

class PoliticsApp(App):
    def build(self):
        return Main()

PoliticsApp().run()
