import kivy

from kivy.app import App

from kivy.uix.button import Label, Button


from kivy.graphics import Line, Rectangle

from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.uix.floatlayout import FloatLayout

from functools import partial

class GestureRecorder(FloatLayout):
	def __init__(self, **kwargs):
		super(GestureRecorder, self).__init__(**kwargs)
		self.line = Line()
		self.Color=[.2,0,0]

	def on_touch_down(self, touch):
		self.points = [touch.pos]
		if touch.x > 200:
			self.canvas.Color=(.2, 1, 1, mode='hsv')
			with self.canvas:
				#Color(.2, 1, 1, mode='hsv')
				self.line = Line(pos=[touch.x, touch.y], size_hint=[.1, .1])
	
	def on_touch_move(self, touch):
		self.points += [touch.pos]
		self.line.points += [touch.x, touch.y]

	def on_touch_up(self, touch):
		self.points+=[touch.pos]


	def Printa(self):
		print(str(self.line.points))
	def build(self):
		self.btn = Button(text='Print!')
		self.btn.bind(on_touch_down=Printa())

		self.add_widget(self.btn())



	'''
	def AddRek(self, touch):
		with self.canvas:
			self.rect = Rectangle(pos=[touch.x, touch.y], size_hint=[.1, .1])

	def ClearRek(self):
		self.canvas.rect = None
	'''
class PosRecorder(FloatLayout):
	pass


class MyWidget(Widget):
	pass

class DrawwApp(App):
	'''
	def on_touch_down(self, touch):
		self.points = [touch.pos]
		if touch.x > 200:
			with self.canvas:
				Color=[1.,0,0]
				self.line = Line(pos=[touch.x, touch.y], size_hint=[.1, .1])
	
	def on_touch_move(self, touch):
		self.points += [touch.pos]
		self.line.points += [touch.x, touch.y]

	def on_touch_up(self, touch):
		self.points+=[touch.pos]
	'''

	def Printa(self, *kwargs):
		print('!!!')
		print(str(self.GR.line.points))
	def Printa2(self, *kwargs):
		print('!!!')

	def build(self):
		root = FloatLayout()




		self.btn = Button(text='Print!', size_hint=[.1,.1])
		self.btn.bind(on_touch_down=partial(self.Printa))
		self.btn2 = Button(text='Print2!', size_hint=[.1,.1], pos=[100, 100])
		self.btn2.bind(on_touch_down=partial(self.Printa2))

		self.GR = GestureRecorder()
		self.GR.Color=[.2,0,0,1]
		root.add_widget(self.GR)
		root.add_widget(self.btn)
		root.add_widget(self.btn2)


		return root


if __name__ == '__main__':
	DrawwApp().run()