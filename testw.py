import kivy

from kivy.app import App

from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Label, Button

from kivy.graphics import Line, Rectangle, Color

from kivy.uix.widget import Widget
from kivy.uix.stencilview import StencilView
from kivy.uix.floatlayout import FloatLayout

from kivy.properties import NumericProperty, StringProperty

from kivy.core.window import Window
from kivy.uix.widget import Widget
from functools import partial
'''
class TestW(FloatLayout):
	bVisible=NumericProperty(0)
	iVisible=0
	def cVisible(self):
		print('tada')
		iVisible=1



class TestApp(App):


	def build(self):

		root = FloatLayout		

		self.txt = StringProperty('		)
		self.Players = 		

		lbl_Players = Label(text= str(self.Players) 		

		btn_p1 = ToggleButton(text='1 Player', size_hint=[.1, .1], pos=[Window.width*.5,Window.height*.2], group='pl')
		btn_p1.bind(on_press=partial(self.modPl, 1, lbl_Players))

		btn_p2 = ToggleButton(text='2 Player', size_hint=[.1, .1], pos=[Window.width*.5,Window.height*.3], group='pl')
		btn_p2.bind(on_press=partial(self.modPl, 2, lbl_Players))

		btn_p3 = ToggleButton(text='3 Player', size_hint=[.1, .1], pos=[Window.width*.5,Window.height*.4], group='pl')
		btn_p3.bind(on_press=partial(self.modPl, 3, lbl_Players))

		btn_ready = Button(text='Ready!', size_hint=[.1,.1], pos=[Window.width*.5,Window.height*.1])
		btn_ready.bind(on_press=partial(self.readyPl, root, lbl_Players))

		root.add_widget(btn_p1)
		root.add_widget(btn_p2)
		root.add_widget(btn_p3)
		root.add_widget(lbl_Players)
		root.add_widget(btn_ready)

		return root

	def modPl(self, *args):
		self.Players = args[0]
		args[1].text=str(args[0])

	def readyPl(self, *args):
		if self.Players>0:
			args[0].canvas.clear()
		else:
			args[1].text='Choose n Players'
'''

class InterfaceManager(FloatLayout):
	def __init__(self, **kwargs):
		super(InterfaceManager, self).__init__(**kwargs)
		self.FirstWidget()


	def modPl(self, *args):
		'''This is the player changing method'''
		self.Players = args[0]
		args[1].text=str(args[0])

	def readyPl(self, *args):
		'''When number of players are chosen switch widget'''
		if self.Players>0:
			self.SecondWidget()
		else:
			args[1].text='Choose n Players'

	def FirstWidget(self, *args):
		'''Here is the changing Players widget'''
		self.Players = 2

		self.lbl_Players = Label(text= str(self.Players) )

		self.btn_p1 = ToggleButton(text='1 Player', size_hint=[.1, .1], pos=[Window.width*.5,Window.height*.2], group='pl')
		self.btn_p1.bind(on_press=partial(self.modPl, 1, self.lbl_Players))

		self.btn_p2 = ToggleButton(text='2 Player', size_hint=[.1, .1], pos=[Window.width*.5,Window.height*.3], group='pl')
		self.btn_p2.bind(on_press=partial(self.modPl, 2, self.lbl_Players))

		self.btn_p3 = ToggleButton(text='3 Player', size_hint=[.1, .1], pos=[Window.width*.5,Window.height*.4], group='pl')
		self.btn_p3.bind(on_press=partial(self.modPl, 3, self.lbl_Players))

		self.btn_ready = Button(text='Ready!', size_hint=[.1,.1], pos=[Window.width*.5,Window.height*.1])
		self.btn_ready.bind(on_press=partial(self.readyPl, self, self.lbl_Players))

		self.add_widget(self.btn_p1)
		self.add_widget(self.btn_p2)
		self.add_widget(self.btn_p3)
		self.add_widget(self.lbl_Players)
		self.add_widget(self.btn_ready)

	def SecondWidget(self, *args):
		'''Switch to this widget when number of players are chosen
		'''
		self.canvas.clear()
		#args[0].add_widget(args[0].second)
		'''with self.canvas:
			Color(.2,0,0)
			Rectangle(size= [Window.width*.6,Window.height*.6], pos=[Window.width*.2, Window.height*.2])
		'''
		self.lbl_Y = Label(text='y:', pos=[100,100])
		self.Cbutton = tButton(instance=self, background_color=[.1,.1,.1,1], background_normal='', background_down='')
		self.lbl_X  = Label(text=str('x:'))
		#self.lbl_X.bind(text=self.pxLabel)
		'''background_color=[.1,.1,.1,1], background_normal='', background_down='''

		self.add_widget(self.Cbutton)
		self.add_widget(self.lbl_X)	
		self.add_widget(self.lbl_Y)	

	def UpdateXY(self, *args):
		'''Update xy labels'''
		self.lbl_X.text='x: ' + str(args[0]['x'])
		self.lbl_Y.text='y: ' + str(args[0]['y'])
		#self.lbl_X.text=args[0][0]

class tButton(Button):
	'''This button is actually a background, and lets players place other 
	buttons that is drawn on
	'''
	def __init__(self, instance, **xargs):
		super(tButton, self).__init__(**xargs)
		self.instance = instance
	def on_touch_down(self, touch):
		#self.instance.UpdateXY(touch)
		#self.instance.StencilDraw = StencilTestWidget(instance=self.instance, pos=[touch.x, touch.y], size_hint=[.1, .1], color=(.6, .6, .6, 1))
		self.instance.StencilDraw = Button( pos=[touch.x, touch.y], size_hint=[.1, .1], color=(.6, .6, .6, 1))
		self.instance.add_widget(self.instance.StencilDraw)
	def on_touch_move(self, touch):
		if touch.x > Window.width /2:
			self.xDiff = Window.width-touch.x
			self.xNull = Window.width*.9
		else:
			self.xDiff = touch.x
			self.xNull = 0

		if touch.y > Window.height /2:
			self.yDiff = Window.width-touch.y
			self.yNull = Window.height*.9
		else:
			self.yDiff = touch.y
			self.yNull = 0

		if self.xDiff <=  self.yDiff:
			self.touchx=self.xNull
			self.touchy=touch.y
		else:
			self.touchx=touch.x
			self.touchy=self.yNull

		self.instance.StencilDraw.pos=[self.touchx, self.touchy]
		self.touch={'x':self.touchx, 'y':self.touchy}
		self.instance.UpdateXY(self.touch)

	'''self.points = [touch.pos]
	if touch.x > 200:
		with self.canvas:
			Color=[1.,0,0]
			self.rect = Rectangle(pos=[touch.x, touch.y], size_hint=[.1, .1])
	'''



class DrawButton(Button):
	'''This button shall be drawn on
	'''
	def __init__(self, instance, **xargs):
		super(tButton, self).__init__(**xargs)
		self.instance = instance


class StencilTestWidget(StencilView):
	'''Drag to define stencil area
	'''
	def __init__(self, instance, **xargs):
		super(StencilTestWidget, self).__init__(**xargs)
		self.instance = instance

	def on_touch_down(self, touch):
		with self.canvas:
			Color=[.1, .1, .1, 1]
			Line(pos=(touch.x, touch.y))
	def on_touch_move(self, touch):
		with self.canvas:
			Line.points += [touch.x, touch.y]

		#self.points += [touch.pos]
		#self.line.points += [touch.x, touch.y]




class TestApp(App):
	def build(self):
		return InterfaceManager()

if __name__ == '__main__':
	TestApp().run()