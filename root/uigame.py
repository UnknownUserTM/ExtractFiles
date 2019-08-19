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
	OPTION_GAME_PVP = 2
	OPTION_GAME_BLOCK_TRADE = 3
	OPTION_GAME_BLOCK_PARTY	= 4
	OPTION_GAME_BLOCK_GUILD = 5
	OPTION_GAME_BLOCK_WHISPER = 6
	OPTION_GAME_BLOCK_FRIENDS = 7
	OPTION_GAME_BLOCK_REQUEST = 8
	OPTION_GAME_CAMERA = 9

	# Welt
	OPTION_SHOP_NAME = 10
	OPTION_WORLD_COSTUME = 11
	OPTION_WORLD_COSTUME_WEAPON = 12
	# OPTION_WORLD_

	# Interface
	OPTION_INTERFACE_NAME_COLOR = 13 
	OPTION_INTERFACE_HIT = 14
	OPTION_INTERFACE_MONSTER_LEVEL = 15
	OPTION_INTERFACE_MONSTER_AGGRESSIVE = 16
	
	OPTION_INTERFACE_BIND_MULTISHOP = 17
	OPTION_INTERFACE_CURRENCY_TOOLTIP = 18
	OPTION_INTERFACE_TASKBAR_INFO_TOOLTIP = 19
	OPTION_INTERFACE_SHOPNAME = 20	
	OPTION_INTERFACE_ATTRIBUTE_TOOLTIP = 21

	OPTION_TYPE_TOGGLE = 0
	OPTION_TYPE_SOUND = 1
	OPTION_TYPE_MUSIC = 2
	OPTION_TYPE_PVP = 3
	OPTION_TYPE_TITLE = 4
	
	#####################
	
	# Ton einstellungen
	
		# Effekte
		# Musik
		
		
	# Spiel einstellungen
		# PVP							Frieden		Feindlich		Gilde		Frei
		# Camera						Nah			Fern			Sehr Fern
		# Abblocken						Blocken		Nicht Blocken
		
		
	# Welt einstellungen
		# ShopName						An			Aus
		# Kostüm ausblenden				An			Aus
		# Waffenkostüm ausblenden		An			Aus
		
	# Interface einstellungen
		# Namensfarbe					Normal		Reichsfarbe
		# Trefferanzeige				Anzeigen	Ausblenden
		# Monsterlevel					Anzeigen	Ausblenden
		# Monsteraggressivität			Anzeigen	Ausblenden
		# BIND Multishop				Binden		Nicht binden
		# Währeungs ToolTips			An			Aus
		# Taskbar Button ToolTips		An			Aus
		# ToolTip Bonus Auflistung		Neu			Alt

	MAX_ITEM = 16
	
	optionDict = [
		# ------------------------------------ #
		{
			"name" : "Ton einstellungen",
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : "Effekte",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_AUDIO_SOUND,
		},
		{
			"name" : "Musik",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_AUDIO_MUSIC,
		},
		# ------------------------------------ #
		{
			"name" : "Spieleinstellungen",
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : "PVP",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_PVP,
		},
		{
			"name" : "Kamera",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_CAMERA,
		},
		{
			"name" : "Handeln abblocken",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_TRADE,
		},
		{
			"name" : "Gruppeneinladungen abblocken",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_PARTY,
		},
		{
			"name" : "Gildeneinladungen abblocken",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_GUILD,
		},
		{
			"name" : "Flüstern abblocken",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_WHISPER,
		},
		{
			"name" : "Freundschaftsanfragen abblocken",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_FRIENDS,
		},	
		{
			"name" : "Shop Namenskarte anzeigen",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_SHOP_NAME,
		},		
		{
			"name" : "Kostüm ausblenden",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_WORLD_COSTUME,
		},	
		{
			"name" : "Waffenkostüm ausblenden",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_WORLD_COSTUME,
		},			
		# ------------------------------------ #
		{
			"name" : "Interface Einstellungen",
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : "Namensfarbe",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_NAME_COLOR,
		},
		{
			"name" : "Trefferanzeige",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_NAME_COLOR,
		},	
		{
			"name" : "Monsterlevel anzeigen",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_MONSTER_LEVEL,
		},			
		{
			"name" : "Monsteraggressivität anzeigen",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_MONSTER_AGGRESSIVE,
		},		
		
		{
			"name" : "Multishop an Inventar Binden",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_BIND_MULTISHOP,
		},
		{
			"name" : "WährungsToolTip",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_CURRENCY_TOOLTIP,
		},
		{
			"name" : "Taskbar ToolTip",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_TASKBAR_INFO_TOOLTIP,
		},
		{
			"name" : "Bonus ToolTip Sortierung",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_ATTRIBUTE_TOOLTIP,
		},
	]

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.optionList = {}
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
		self.scrollBar = self.GetChild("scrollBar")
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		
		
		self.devTextLine = self.GetChild("devTextLine")
		
		
		y = 5
		for i in xrange(len(self.optionDict)):
			option = self.optionDict[i]
			if option["type"] == self.OPTION_TYPE_TITLE:
				self.optionList[i] = OptionTitleItem()
				self.optionList[i].SetParent(self.background)
				self.optionList[i].SetPosition(5,y)
				self.optionList[i].SetTitle(option["name"])
				self.optionList[i].Show()
				
			elif option["type"] == self.OPTION_TYPE_TOGGLE:
				self.optionList[i] = OptionToggleItem()
				self.optionList[i].SetParent(self.background)
				self.optionList[i].SetPosition(5,y)
				self.optionList[i].SetTitle(option["name"])
				self.optionList[i].Show()
				
			 		
				
				
		
			y = y + 25
		
				
		self.HideAllItems()
		self.RenderOptionList()
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"LoadWindow GameOptionWindow!")
			
		
		
		self.Show()
		
		
		
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.scrollBar.OnUp()
		else:
			self.scrollBar.OnDown()
	
	
	def RenderOptionList(self):
		pos = int(self.scrollBar.GetPos() * (len(self.optionDict) - self.MAX_ITEM)) 
		start_height = 5
		for i in xrange(self.MAX_ITEM):
			realPos = pos + i
			self.optionList[realPos].SetPosition(5,start_height)
			self.optionList[realPos].Show()
			start_height = start_height + 25			

		
	def OnScroll(self):
		self.HideAllItems()
		self.RenderOptionList()
		
	def HideAllItems(self):
		for i in xrange(len(self.optionList)):
			self.optionList[i].Hide()
	
	def OnUpdate(self):
		pos = int(self.scrollBar.GetPos() * (len(self.optionDict) - self.MAX_ITEM)) 
		self.devTextLine.SetText(str(pos))
	
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
		self.title.SetText(title)
		
		
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
		