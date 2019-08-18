import ui
import chat
import app
import GFHhg54GHGhh45GHGH as player
import snd
import item
import fgGHGjjFHJghjfFG1545gGG as net
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo
from uiGuild import MouseReflector



class GameOptionWindow(ui.ScriptWindow):
	# AUDIO
	OPTION_AUDIO_MUSIC = 0
	OPTION_AUDIO_SOUND = 1
	
	# Spiel
	OPTION_GAME_PVP = 0
	OPTION_GAME_BLOCK = 0
	OPTION_GAME_CAMERA = 0
	
	
	
	# Welt
	OPTION_SHOP_NAME = 0
	OPTION_WORLD_COSTUME = 0
	OPTION_WORLD_COSTUME_WEAPON = 0
	# OPTION_WORLD_
	
	
	# Interface
	OPTION_INTERFACE_NAME_COLOR = 0 
	OPTION_INTERFACE_HIT = 0
	OPTION_INTERFACE_MONSTER_LEVEL = 0
	OPTION_INTERFACE_MONSTER_AGGRESSIVE = 0
	
	OPTION_INTERFACE_BIND_MULTISHOP = 0
	OPTION_INTERFACE_CURRENCY_TOOLTIP = 0
	OPTION_INTERFACE_TASKBAR_INFO_TOOLTIP = 0
	OPTION_INTERFACE_SHOPNAME = 0	
	
	
	
	
	OPTION_TYPE_TOGGLE = 0
	OPTION_TYPE_SOUND = 1
	OPTION_TYPE_MUSIC = 2
	OPTION_TYPE_PVP = 3
	OPTION_TYPE_TITLE = 4
	
	
	
	optionDict = [
		{
			"name" : "Interface Einstellungen",
			"type" : OPTION_TYPE_TITLE,
		
		
		},
		{
			"name" : "Multishop an Inventar Binden",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_BIND_MULTISHOP,
		},
	]
	
	
	
	
	
	
	
	
	
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		#constInfo.CALOPEN = 1
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/gameoption.py")
		except:
			import exception
			exception.Abort("GameOptionWindow.LoadWindow.LoadObject")
			
			
		self.background = self.GetChild("background")
		
		self.testItem = OptionTitleItem()
		self.testItem.SetParent(self.background)
		self.testItem.SetPosition(5,5)
		self.testItem.Show()
		
		self.testItem2 = OptionToggleItem()
		self.testItem2.SetParent(self.background)
		self.testItem2.SetPosition(5,5 + 25)
		
		self.testItem2.SetTitle("Namensfarbe")
		self.testItem2.SetEnableText("Normal")
		self.testItem2.SetDisableText("Reichsfarbe")

		self.testItem2.Show()		
		self.testItem3 = OptionToggleItem()
		self.testItem3.SetParent(self.background)
		self.testItem3.SetPosition(5,5 + 25 + 25)
		self.testItem3.SetTitle("Globaler Chat")
		self.testItem3.SetEnableText("Einblenden")
		self.testItem3.SetDisableText("Ausblenden")
		
		
		self.testItem3.Show()		
		self.testItem4 = OptionToggleItem()
		self.testItem4.SetParent(self.background)
		self.testItem4.SetPosition(5,5 + 25 + 25 + 25)
		self.testItem4.SetTitle("Ladenname")
		self.testItem4.SetEnableText("Anzeigen")
		self.testItem4.SetDisableText("Ausblenden")
		self.testItem4.Show()		
		self.testItem5 = OptionToggleItem()
		self.testItem5.SetParent(self.background)
		self.testItem5.SetPosition(5,5 + 25 + 25 + 25 + 25)
		
		self.testItem5.SetTitle("Shop binden")
		self.testItem5.SetEnableText("Binden")
		self.testItem5.SetDisableText("Nicht binden")
		
		self.testItem5.Show()		
		self.testItem6 = OptionToggleItem()
		self.testItem6.SetParent(self.background)
		self.testItem6.SetPosition(5,5 + 25 + 25 + 25 + 25 + 25)
		self.testItem6.Show()		
		self.testItem7 = OptionToggleItem()
		self.testItem7.SetParent(self.background)
		self.testItem7.SetPosition(5,5 + 25 + 25 + 25 + 25 + 25 + 25)
		self.testItem7.Show()


		self.testItem8 = OptionTitleItem()
		self.testItem8.SetParent(self.background)
		self.testItem8.SetPosition(5,5 + 25 + 25 + 25 + 25 + 25 + 25 + 25)
		self.testItem8.Show()		
		
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"LoadWindow GameOptionWindow!")
			
		
		
		self.Show()
	
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
		


class OptionTitleItem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/gameoption_title.py")
		except:
			import exception
			exception.Abort("GameOptionWindow.LoadWindow.LoadObject")

		self.title = self.GetChild("titleTextLine")
		self.Show()

	def SetTitle(self,title):
		self.title = title
		
		
class OptionToggleItem(ui.ScriptWindow):

	COLOR_INACTIVE = grp.GenerateColor(1.0, 0.0, 0.0, 0.3)
	COLOR_ACTIVE   = grp.GenerateColor(0.0, 1.0, 0.0, 0.2)
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.status = True
		self.LoadWindow()
		

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/gameoption_toggleitem.py")
		except:
			import exception
			exception.Abort("GameOptionWindow.LoadWindow.LoadObject")

		self.title = self.GetChild("titleTextLine")
		self.toggleButtonBG01 = self.GetChild("toggleButton01BG")
		self.toggleButtonText01 = self.GetChild("enableOptionTitle")
		self.toggleButtonBG02 = self.GetChild("toggleButton02BG")
		self.toggleButtonText02 = self.GetChild("disableOptionTitle")

		self.toggleButtonBG01.SetOnClickEvent(self.Enable)
		self.toggleButtonBG02.SetOnClickEvent(self.Disable)
		self.greenBar = self.GetChild("greenBar")
		self.greenBar.SetColor(self.COLOR_ACTIVE)
		self.greenBar.Show()
		
		self.redBar = self.GetChild("redBar")
		self.redBar.SetColor(self.COLOR_INACTIVE)
		self.redBar.Hide()
		
		self.mouseReflector01 = MouseReflector(self.toggleButtonBG01)
		self.mouseReflector01.SetSize(60, 22)
		self.mouseReflector01.UpdateRect()
		
		self.mouseReflector02 = MouseReflector(self.toggleButtonBG02)
		self.mouseReflector02.SetSize(60, 22)
		self.mouseReflector02.UpdateRect()

		self.Show()

	def SetTitle(self,title):
		self.title.SetText(title)
	
	def SetEnableText(self,text):
		self.toggleButtonText01.SetText(text)
		
	def SetDisableText(self,text):
		self.toggleButtonText02.SetText(text)
		
	def OnUpdate(self):
		if self.toggleButtonBG01.IsIn():
			self.mouseReflector01.Show()
		else:
			self.mouseReflector01.Hide()
		
		if self.toggleButtonBG02.IsIn():
			self.mouseReflector02.Show()
		else:
			self.mouseReflector02.Hide()		
		
		
	def Enable(self):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OptionToggleItem: Enable")
		
		if self.status == True:
			return
		
		self.status = True
		self.greenBar.Show()
		self.redBar.Hide()
		
		
		
	def Disable(self):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OptionToggleItem: Disable")
		
		if self.status == False:
			return
		
		self.status = False
		self.greenBar.Hide()
		self.redBar.Show()		
		