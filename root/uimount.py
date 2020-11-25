# Developed by Exterminatus!!! 
import ui
import chat
import app
import fgGHGjjFHJghjfFG1545gGG
import snd
import item
import GFHhg54GHGhh45GHGH
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo
import exterminatus
import settinginfo

class MountWindow(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/mountwindow.py")
		except:
			import exception
			exception.Abort("MountWindow.LoadWindow.LoadObject")
		
		
		self.rune0 = self.GetChild("runeNameTextLine") # blau
		self.rune1 = self.GetChild("runeQuestTextLine") # Gelb
		self.rune2 = self.GetChild("runeName2TextLine") # Rot

		self.rune0.SetFontColor(0.0, 0.5019, 1.0)
		self.rune1.SetFontColor(1.0, 0.7843, 0.0)
		self.rune2.SetFontColor(0.9, 0.4745, 0.4627)
		
	def Open(self):
		if self.IsShow():
			self.Close()
			return
			
		self.Show()

	def Close(self):
		self.Hide()

