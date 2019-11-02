import ui
import chat
import app
import GFHhg54GHGhh45GHGH as net
import snd
import item
import fgGHGjjFHJghjfFG1545gGG as player
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import localeInfo

class DungeonMakerToolBar(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Hallo?")
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/dungeonmaker_toolbar.py")
		except:
			import exception
			exception.Abort("DungeonMakerToolBar.LoadWindow.LoadObject")
		
		self.stageTextLine = self.GetChild("stageTextLine")
		
		# self.Show()
		
		
	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
		
	def Close(self):
		self.Hide()

# DungeonMakerToolBar().Show()