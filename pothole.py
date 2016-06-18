import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

def callback(instance):
	print('The button <%s> is being pressed' % instance.text)

# define the class
class PotholeApp(App):
	def build(self):
		# top level root widget
		# BoxLayout() aligns children horizontally from the left automatically
		b = BoxLayout()		

		# set up the first button widget
		btn1 = Button(text='Button1', font_size=52)
		btn1.bind(on_press=callback)

		# set up the second button widget
		btn2 = Button(text='Button2', font_size=50)
		btn2.bind(on_press=callback)

		# now add the sub-widgets to b
		b.add_widget(btn1)
		b.add_widget(btn2)
		return b  # return b since it contains everything else

# instantiate the PotholeApp class and call its run method
if __name__ == '__main__':
	PotholeApp().run()

