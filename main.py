from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivymd.uix.list import MDList,OneLineAvatarListItem,ImageLeftWidget
import time


Window.size = (350,900)

Builder.load_file("homescreen.kv")
class Homescreen(MDScreen):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)

		# GET SELECTOR FROM KV FILE CAMERA 
		self.mycamera = self.ids.camera
		self.myimage = Image()
		self.resultbox = self.ids.resultbox
		self.mybox = self.ids.mybox



	def captureyouface(self):
		# CREATE TIMESTAMP NOT FOR YOU FILE IMAGE
		# THIS SCRIPT GET TIME MINUTES AND DAY NOW
		timenow = time.strftime("%Y%m%d_%H%M%S")

		# AND EXPORT YOU CAMERA CAPTURE TO PNG IMAGE
		self.mycamera.export_to_png("myimage_{}.png".format(timenow))
		self.myimage.source = "myimage_{}.png".format(timenow)
		self.resultbox.add_widget(
			OneLineAvatarListItem(
				ImageLeftWidget(
					source="myimage_{}.png".format(timenow),
					size_hint_x=0.3,
					size_hint_y=1,

					# AND SET YOU WIDHT AND HEIGT YOU PHOTO
					size=(300,300)

					),
				text=self.ids.name.text
				)

			)


class MyApp(MDApp):
	def build(self):
		return Homescreen()

if __name__ == "__main__":
	MyApp().run()

