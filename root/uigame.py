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
import constInfo
import event
import localeInfo
from uiGuild import MouseReflector
import systemSetting

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
	OPTION_TYPE_SLIDER = 1
	OPTION_TYPE_PVP_GROUP = 2
	OPTION_TYPE_CAMERA_GROUP = 3
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
			"name" : "Soundeffekte",
			"type" : OPTION_TYPE_SLIDER,
			
			"id" : OPTION_AUDIO_SOUND,
		},
		# {
			# "name" : "Musik",
			# "type" : OPTION_TYPE_SLIDER,
			
			# "id" : OPTION_AUDIO_MUSIC,
		# },
		# ------------------------------------ #
		{
			"name" : "Spieleinstellungen",
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : "PVP",
			"type" : OPTION_TYPE_PVP_GROUP,
			
			"id" : OPTION_GAME_PVP,
		},
		{
			"name" : "Kamera",
			"type" : OPTION_TYPE_CAMERA_GROUP,
			
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
			
		self.GetChild("TitleBar").SetCloseEvent(self.Close)	
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
			elif option["type"] == self.OPTION_TYPE_SLIDER:
				self.optionList[i] = OptionSlideItem()
				self.optionList[i].SetParent(self.background)
				self.optionList[i].SetPosition(5,y)
				self.optionList[i].SetTitle(option["name"])
				self.optionList[i].Show()
			elif option["type"] == self.OPTION_TYPE_PVP_GROUP:
				self.optionList[i] = OptionPVPGroupItem()
				self.optionList[i].SetParent(self.background)
				self.optionList[i].SetPosition(5,y)
				self.optionList[i].SetTitle(option["name"])
				self.optionList[i].Show()
			elif option["type"] == self.OPTION_TYPE_CAMERA_GROUP:
				self.optionList[i] = OptionCameraGroupItem()
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
		
		
class OptionSlideItem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/gameoption_slideritem.py")
		except:
			import exception
			exception.Abort("GameOptionWindow.LoadWindow.LoadObject")

		self.title = self.GetChild("titleTextLine")
		self.slider = self.GetChild("slideBar")
		
		
		
		self.slider.SetSliderPos(float(float(systemSetting.GetSoundVolume()) / 5.0))
		self.slider.SetEvent(ui.__mem_func__(self.OnChangeVolume))
		self.Show()
	
	
	def OnChangeVolume(self):
		pos = self.slider.GetSliderPos()
		snd.SetSoundVolumef(pos)
		systemSetting.SetSoundVolumef(pos)		
	
	def SetTitle(self,title):
		self.title.SetText(title)
		
class OptionCameraGroupItem(ui.ScriptWindow):
	
	CAMERA_MODE_SHORT = 0
	CAMERA_MODE_FAR = 1
	CAMERA_MODE_VERY_FAR = 2
	
	COLOR_INACTIVE = grp.GenerateColor(1.0, 0.0, 0.0, 0.3)
	COLOR_ACTIVE   = grp.GenerateColor(0.0, 1.0, 0.0, 0.2)
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.cameraMode = 0
		
		self.redBar = []
		self.greenBar = []
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/gameoption_cameragroupitem.py")
		except:
			import exception
			exception.Abort("GameOptionWindow.LoadWindow.LoadObject")

		self.title = self.GetChild("titleTextLine")
		self.toggleButtonBG01 = self.GetChild("toggleButton01BG")
		self.toggleButtonBG02 = self.GetChild("toggleButton02BG")
		self.toggleButtonBG03 = self.GetChild("toggleButton03BG")
		
		self.toggleButtonBG01.SetOnClickEvent(self.__OnClickCameraShort)
		self.toggleButtonBG02.SetOnClickEvent(self.__OnClickCameraFar)
		self.toggleButtonBG03.SetOnClickEvent(self.__OnClickCameraVeryFar)

		for i in xrange(3):
			nr = i + 1
			self.redBar.append(self.GetChild("redBar0" + str(nr)))
			self.greenBar.append(self.GetChild("greenBar0" + str(nr)))
		
			self.redBar[i].Hide()
			self.greenBar[i].SetColor(self.COLOR_ACTIVE)
		
		self.RefreshButtonGroup()
		
		self.mouseReflector01 = MouseReflector(self.toggleButtonBG01)
		self.mouseReflector01.SetSize(60, 22)
		self.mouseReflector01.UpdateRect()
		
		self.mouseReflector02 = MouseReflector(self.toggleButtonBG02)
		self.mouseReflector02.SetSize(60, 22)
		self.mouseReflector02.UpdateRect()
		
		self.mouseReflector03 = MouseReflector(self.toggleButtonBG03)
		self.mouseReflector03.SetSize(60, 22)
		self.mouseReflector03.UpdateRect()
		
		self.Show()
		
	def __SetCameraMode(self, index):
		constInfo.SET_CAMERA_MAX_DISTANCE_INDEX(index)
	
	def __OnClickCameraShort(self):
		self.cameraMode = 0
		self.__SetCameraMode(0)
		self.RefreshButtonGroup()
		
	def __OnClickCameraFar(self):
		self.cameraMode = 1
		self.__SetCameraMode(1)
		self.RefreshButtonGroup()

	def __OnClickCameraVeryFar(self):
		self.cameraMode = 2
		self.__SetCameraMode(2)
		self.RefreshButtonGroup()
	
	def RefreshButtonGroup(self):
		for i in xrange(3):
			if i == self.cameraMode:
				self.greenBar[i].Show()
			else:
				self.greenBar[i].Hide()	
	
	def SetTitle(self,title):
		self.title.SetText(title)
		
	def OnUpdate(self):
		if self.toggleButtonBG01.IsIn():
			self.mouseReflector01.Show()
		else:
			self.mouseReflector01.Hide()
		
		if self.toggleButtonBG02.IsIn():
			self.mouseReflector02.Show()
		else:
			self.mouseReflector02.Hide()

		if self.toggleButtonBG03.IsIn():
			self.mouseReflector03.Show()
		else:
			self.mouseReflector03.Hide()
			
class OptionPVPGroupItem(ui.ScriptWindow):

	COLOR_INACTIVE = grp.GenerateColor(1.0, 0.0, 0.0, 0.3)
	COLOR_ACTIVE   = grp.GenerateColor(0.0, 1.0, 0.0, 0.2)
	
	
	PVP_PEACE = 0
	PVP_REVENGE = 1
	PVP_GUILD = 2
	PVP_FREE = 3
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.redBar = []
		self.greenBar = []
		self.pvpMode = 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/gameoption_pvpgroupitem.py")
		except:
			import exception
			exception.Abort("GameOptionWindow.LoadWindow.LoadObject")

		self.title = self.GetChild("titleTextLine")
		
		self.toggleButtonBG01 = self.GetChild("toggleButton01BG")
		self.toggleButtonBG02 = self.GetChild("toggleButton02BG")
		self.toggleButtonBG03 = self.GetChild("toggleButton03BG")
		self.toggleButtonBG04 = self.GetChild("toggleButton04BG")
		
		self.toggleButtonBG01.SetOnClickEvent(self.__OnClickPvPModePeaceButton)
		self.toggleButtonBG02.SetOnClickEvent(self.__OnClickPvPModeRevengeButton)
		self.toggleButtonBG03.SetOnClickEvent(self.__OnClickPvPModeGuildButton)
		self.toggleButtonBG04.SetOnClickEvent(self.__OnClickPvPModeFreeButton)

		for i in xrange(4):
			nr = i + 1
			self.redBar.append(self.GetChild("redBar0" + str(nr)))
			self.greenBar.append(self.GetChild("greenBar0" + str(nr)))
		
			self.redBar[i].Hide()
			self.greenBar[i].SetColor(self.COLOR_ACTIVE)

		self.mouseReflector01 = MouseReflector(self.toggleButtonBG01)
		self.mouseReflector01.SetSize(60, 22)
		self.mouseReflector01.UpdateRect()
		
		self.mouseReflector02 = MouseReflector(self.toggleButtonBG02)
		self.mouseReflector02.SetSize(60, 22)
		self.mouseReflector02.UpdateRect()
		
		self.mouseReflector03 = MouseReflector(self.toggleButtonBG03)
		self.mouseReflector03.SetSize(60, 22)
		self.mouseReflector03.UpdateRect()
		
		self.mouseReflector04 = MouseReflector(self.toggleButtonBG04)
		self.mouseReflector04.SetSize(60, 22)
		self.mouseReflector04.UpdateRect()

		self.__SetPeacePKMode()
		self.RefreshButtonGroup()
		self.Show()
	
	def RefreshButtonGroup(self):
		for i in xrange(4):
			if i == self.pvpMode:
				self.greenBar[i].Show()
			else:
				self.greenBar[i].Hide()
	
	def SetTitle(self,title):
		self.title.SetText(title)

	def OnUpdate(self):
		if self.toggleButtonBG01.IsIn():
			self.mouseReflector01.Show()
		else:
			self.mouseReflector01.Hide()
		
		if self.toggleButtonBG02.IsIn():
			self.mouseReflector02.Show()
		else:
			self.mouseReflector02.Hide()

		if self.toggleButtonBG03.IsIn():
			self.mouseReflector03.Show()
		else:
			self.mouseReflector03.Hide()
			
		if self.toggleButtonBG04.IsIn():
			self.mouseReflector04.Show()
		else:
			self.mouseReflector04.Hide()
			
			
			
	def __SetPKMode(self, mode):
		self.pvpMode = mode
		self.RefreshButtonGroup()

	def __SetPeacePKMode(self):
		self.__SetPKMode(player.PK_MODE_PEACE)

	def __RefreshPVPButtonList(self):
		self.__SetPKMode(player.GetPKMode())

	def __CheckPvPProtectedLevelPlayer(self):	
		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__SetPeacePKMode()
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return 1

		return 0

	def __OnClickPvPModePeaceButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 0", chat.CHAT_TYPE_TALKING)
			self.__SetPKMode(0)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeRevengeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 1", chat.CHAT_TYPE_TALKING)
			self.__SetPKMode(1)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeFreeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 2", chat.CHAT_TYPE_TALKING)
			self.__SetPKMode(3)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeGuildButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if 0 == player.GetGuildID():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
			self.__SetPKMode(2)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def OnChangePKMode(self):
		self.__RefreshPVPButtonList()
			
		
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
		