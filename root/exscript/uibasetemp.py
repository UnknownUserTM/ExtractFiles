import ui
import chat
import app
import player
import snd
import item
import net
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo



class CalenderWindow(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		#constInfo.CALOPEN = 1
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/calenderwindow.py")
		except:
			import exception
			exception.Abort("CalenderWindow.LoadWindow.LoadObject")

		
		self.Open()
		# self.eventDayImage[12].Show()
	
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
		
		
	def Close(self):
		self.Hide()

