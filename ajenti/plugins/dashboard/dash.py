import os
import re

from ajenti.api import *

from ajenti.ui import *
from ajenti.ui.standard import *
from ajenti.plugins.main.api import SectionPlugin


@plugin
class Dash (SectionPlugin): 
	def init(self):
		self.title = 'Dashboard'
		l = Label(text = '123')
		self.append(l)

		self.append(Button(text='test'))