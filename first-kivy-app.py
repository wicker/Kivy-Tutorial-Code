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
		# top level root widget, aligns children horizontally from the left automatically
		b = BoxLayout()		

		# set up the first child widget
		t = TextInput(font_size=50)

		# set up the second child widget
		f = FloatLayout()
		s = Scatter()
		l = Label(text='Hello!', font_size=50)
		f.add_widget(s)
		s.add_widget(l)

		# now add the sub-widgets to b
		b.add_widget(f)
		b.add_widget(t)
		return b  # return b since it contains everything else

# instantiate the PotholeApp class and call its run method
if __name__ == '__main__':
	PotholeApp().run()

