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
blockMode = 0

class GameOptionWindow(ui.ScriptWindow):
	# AUDIO
	OPTION_AUDIO_SOUND = 0	
	# Spiel
	OPTION_GAME_PVP = 1
	OPTION_GAME_CAMERA = 2
	OPTION_GAME_BLOCK_TRADE = 5
	OPTION_GAME_BLOCK_PARTY	= 6
	OPTION_GAME_BLOCK_GUILD = 7
	OPTION_GAME_BLOCK_WHISPER = 8
	OPTION_GAME_BLOCK_FRIENDS = 9
	# OPTION_GAME_BLOCK_REQUEST = 8
	
	# Welt
	OPTION_SHOP_NAME = 10
	OPTION_WORLD_COSTUME = 11
	OPTION_WORLD_COSTUME_WEAPON = 12
	# OPTION_WORLD_

	# Interface
	OPTION_INTERFACE_NAME_COLOR = 13 
	OPTION_INTERFACE_HIT = 14
	OPTION_INTERFACE_MONSTER_LEVEL = 16
	OPTION_INTERFACE_MONSTER_AGGRESSIVE = 17
	
	OPTION_INTERFACE_BIND_MULTISHOP = 18
	OPTION_INTERFACE_CURRENCY_TOOLTIP = 19
	OPTION_INTERFACE_TASKBAR_INFO_TOOLTIP = 20
	OPTION_INTERFACE_ATTRIBUTE_TOOLTIP = 21

	OPTION_TYPE_TOGGLE = 0
	OPTION_TYPE_SLIDER = 1
	OPTION_TYPE_PVP_GROUP = 2
	OPTION_TYPE_CAMERA_GROUP = 3
	OPTION_TYPE_TITLE = 4
	
	OPTION_PICKUP_WEAPON		= 23
	OPTION_PICKUP_ARMOR			= 24
	OPTION_PICKUP_JEWELRY		= 25
	OPTION_PICKUP_MATERIAL		= 26
	OPTION_PICKUP_GHOSTSTONE	= 27
	OPTION_PICKUP_SKILLBOOK		= 28
	
	
	OPTION_MINIMAP_MAPNAME	= 29
	OPTION_MINIMAP_TIME_FPS = 30
	OPTION_MINIMAP_LOCAL_POS = 31
	OPTION_MINIMAP_SAFEZONE = 32
	
	
	MAX_ITEM = 16
	
	optionDict = [
		# ------------------------------------ #
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_AUDIO,
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_SOUND,
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
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_GAMEOPTION,
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_PVP,
			"type" : OPTION_TYPE_PVP_GROUP,
			
			"id" : OPTION_GAME_PVP,
			
			"button_peace"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_PVP_PEACE,
			"button_revenge"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_PVP_REVENGE,
			"button_guild"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_PVP_GUILD,
			"button_free" 		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_PVP_FREE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_CAMERA,
			"type" : OPTION_TYPE_CAMERA_GROUP,
			
			"id" : OPTION_GAME_CAMERA,
			
			"button_short"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_CAMERA_SHORT,
			"button_long"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_CAMERA_LONG,
			"button_verylong"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_CAMERA_VERYLING,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_BLOCK_TRADE,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_TRADE,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_ON,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_OFF,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_BLOCK_GROUP,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_PARTY,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_ON,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_OFF,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_BLOCK_GUILD,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_GUILD,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_ON,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_OFF,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_BLOCK_WHISPER,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_WHISPER,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_ON,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_OFF,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_BLOCK_FRIEND,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_GAME_BLOCK_FRIENDS,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_ON,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_OFF,
		},	
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_SHOP_NAMECARD,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_SHOP_NAME,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},		
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_COSTUME_HIDE,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_WORLD_COSTUME,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},	
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_WEAPON_COSTUME_HIDE,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_WORLD_COSTUME,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},			
		# ------------------------------------ #
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_INTERFACE,
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_NAMECOLOR,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_NAME_COLOR,
			
			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_NAME_COLOR_NORMAL,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_NAME_COLOR_EMPIRE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_HIT,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_NAME_COLOR,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},	
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_MONSTER_LEVEL,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_MONSTER_LEVEL,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},			
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_MONSTER_AGGRESSIVITY,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_MONSTER_AGGRESSIVE,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},		
		
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_BIND_MULTISHOP,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_BIND_MULTISHOP,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_CURRENCY_TOOLTIP,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_CURRENCY_TOOLTIP,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_TASKBAR_TOOLTIP,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_TASKBAR_INFO_TOOLTIP,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},
		{
			"name" : localeInfo.NEW_GAME_OPTION_TITLE_BONUS_TOOLTIP,
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_INTERFACE_ATTRIBUTE_TOOLTIP,

			"button_on"		: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_SHOW,
			"button_off"	: localeInfo.NEW_GAME_OPTION_DIALOG_BUTTON_HIDE,
		},
		# ------------------------------------ #
		{
			"name" : "PickUp-Filter",
			"type" : OPTION_TYPE_TITLE,
		},
		{
			"name" : "Waffen",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_PICKUP_WEAPON,
			
			"button_on"		: "Aufheben",
			"button_off"	: "Liegen lassen",
		},
		{
			"name" : "Rüstungen",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_PICKUP_ARMOR,
			
			"button_on"		: "Aufheben",
			"button_off"	: "Liegen lassen",
		},
		{
			"name" : "Schmuck",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_PICKUP_JEWELRY,
			
			"button_on"		: "Aufheben",
			"button_off"	: "Liegen lassen",
		},
		{
			"name" : "Upp-Items",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_PICKUP_MATERIAL,
			
			"button_on"		: "Aufheben",
			"button_off"	: "Liegen lassen",
		},
		{
			"name" : "Geiststeine",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_PICKUP_GHOSTSTONE,
			
			"button_on"		: "Aufheben",
			"button_off"	: "Liegen lassen",
		},
		{
			"name" : "Fertigkeitsbücher",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_PICKUP_SKILLBOOK,
			
			"button_on"		: "Aufheben",
			"button_off"	: "Liegen lassen",
		},
		
		# ------------------------------------ #
		{
			"name" : "MiniMap Informationen",
			"type" : OPTION_TYPE_TITLE,
		},		
		{
			"name" : "Map Name und Channel",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_MINIMAP_MAPNAME,
			
			"button_on"		: "Anzeigen",
			"button_off"	: "Ausblenden",
		},	
		{
			"name" : "Lokale Uhrzeit und FPS",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_MINIMAP_TIME_FPS,
			
			"button_on"		: "Anzeigen",
			"button_off"	: "Ausblenden",
		},			
		{
			"name" : "Lokale Spielerposition",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_MINIMAP_LOCAL_POS,
			
			"button_on"		: "Anzeigen",
			"button_off"	: "Ausblenden",
		},			
		{
			"name" : "Safezone (Wird nur in der Safezone angezeigt)",
			"type" : OPTION_TYPE_TOGGLE,
			
			"id" : OPTION_MINIMAP_SAFEZONE,
			
			"button_on"		: "Anzeigen",
			"button_off"	: "Ausblenden",
		},		
	]
	

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.optionList = {}
		self.blockMode = 0
		self.LoadWindow()

	def __del__(self):
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
				self.optionList[i].SetOnButtonText(option["button_on"])
				self.optionList[i].SetOffButtonText(option["button_off"])
				self.optionList[i].SetIndex(i)
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
				self.optionList[i].SetButtonText(option["button_peace"],option["button_revenge"],option["button_guild"],option["button_free"])
				self.optionList[i].Show()
				
			elif option["type"] == self.OPTION_TYPE_CAMERA_GROUP:
				self.optionList[i] = OptionCameraGroupItem()
				self.optionList[i].SetParent(self.background)
				self.optionList[i].SetPosition(5,y)
				self.optionList[i].SetTitle(option["name"])
				self.optionList[i].SetButtonText(option["button_short"],option["button_long"],option["button_verylong"])
				self.optionList[i].Show()

			y = y + 25

		self.optionList[self.OPTION_GAME_BLOCK_TRADE].LinkEvent(self.ToggleBlockMode, self.OPTION_GAME_BLOCK_TRADE)
		self.optionList[self.OPTION_GAME_BLOCK_PARTY].LinkEvent(self.ToggleBlockMode, self.OPTION_GAME_BLOCK_PARTY)
		self.optionList[self.OPTION_GAME_BLOCK_GUILD].LinkEvent(self.ToggleBlockMode, self.OPTION_GAME_BLOCK_GUILD)
		self.optionList[self.OPTION_GAME_BLOCK_WHISPER].LinkEvent(self.ToggleBlockMode, self.OPTION_GAME_BLOCK_WHISPER)
		self.optionList[self.OPTION_GAME_BLOCK_FRIENDS].LinkEvent(self.ToggleBlockMode, self.OPTION_GAME_BLOCK_FRIENDS)



		self.optionList[self.OPTION_INTERFACE_MONSTER_LEVEL].LinkEvent(self.ToggleMonsterLevel)
		
		# PickUPFilter
		self.optionList[self.OPTION_PICKUP_WEAPON].LinkEvent(self.TogglePickUpFilter, 1)
		self.optionList[self.OPTION_PICKUP_ARMOR].LinkEvent(self.TogglePickUpFilter, 2)
		self.optionList[self.OPTION_PICKUP_JEWELRY].LinkEvent(self.TogglePickUpFilter, 3)
		self.optionList[self.OPTION_PICKUP_MATERIAL].LinkEvent(self.TogglePickUpFilter, 4)
		self.optionList[self.OPTION_PICKUP_GHOSTSTONE].LinkEvent(self.TogglePickUpFilter, 5)
		self.optionList[self.OPTION_PICKUP_SKILLBOOK].LinkEvent(self.TogglePickUpFilter, 6)

		self.HideAllItems()
		self.RenderOptionList()
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"LoadWindow GameOptionWindow!")
	
	def TestLinkEvent(self):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Hallo Welt!")
		
	# ################################
	def ToggleMonsterLevel(self):
		if app.WJ_SHOW_MOB_INFO:
			if systemSetting.IsShowMobLevel():
				systemSetting.SetShowMobLevel(False)
			else:
				systemSetting.SetShowMobLevel(True)


	def ToggleBlockMode(self, index):
		# status = self.optionList[self.OPTION_GAME_BLOCK_TRADE].GetStatus()
		# index = self.optionList[self.OPTION_GAME_BLOCK_TRADE].GetIndex()
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"status: " + str(status))
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"index: " + str(index))
		
		blockDict = {
			self.OPTION_GAME_BLOCK_TRADE	: player.BLOCK_EXCHANGE,
			self.OPTION_GAME_BLOCK_PARTY	: player.BLOCK_PARTY,
			self.OPTION_GAME_BLOCK_GUILD	: player.BLOCK_GUILD,
			self.OPTION_GAME_BLOCK_WHISPER	: player.BLOCK_WHISPER,
			self.OPTION_GAME_BLOCK_FRIENDS	: player.BLOCK_FRIEND,
		}
		
		global blockMode
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"/setblockmode " + str(blockMode ^ blockDict[index]))	
		net.SendChatPacket("/setblockmode " + str(blockMode ^ blockDict[index]))	

	def TogglePickUpFilter(self, index):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"/change_pickup_filter " + str(index))	
		net.SendChatPacket("/change_pickup_filter " + str(index))
		
	def GAME_InitPickUpFilter(self,index):
		blockDict = {
			1 : self.OPTION_PICKUP_WEAPON,
			2 : self.OPTION_PICKUP_ARMOR,
			3 : self.OPTION_PICKUP_JEWELRY,
			4 : self.OPTION_PICKUP_MATERIAL,
			5 : self.OPTION_PICKUP_GHOSTSTONE,
			6 : self.OPTION_PICKUP_SKILLBOOK,
		}
	
		idx = blockDict[index]
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"GAME_InitPickUpFilter: " + str(index) + ", " + str(idx))
		self.optionList[idx].SetStatus(False)

		

	def OnBlockMode(self, mode):
		global blockMode
		blockMode = mode		
	# ################################
	
	def Destroy(self):
		self.Hide()
		
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
		
	def OnBlockMode(self, mode):
		# global blockMode
		self.blockMode = mode


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
		self.cameraMode = systemSetting.GetCameraDistance()
		
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
		self.shortText = self.GetChild("OptionTitle01")
		self.longText = self.GetChild("OptionTitle02")
		self.veryLongText = self.GetChild("OptionTitle03")

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

		self.__SetCameraMode(systemSetting.GetCameraDistance())
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
		systemSetting.SetCameraDistance(index)
	
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
		
	def SetButtonText(self,button_short,button_long,button_verylong):
		self.shortText.SetText(button_short)
		self.longText.SetText(button_long)
		self.veryLongText.SetText(button_verylong)
		
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
		self.buttonPeaceText = self.GetChild("OptionTitle01")
		self.buttonRevengeText = self.GetChild("OptionTitle02")
		self.buttonGuildText = self.GetChild("OptionTitle03")
		self.buttonFreeText = self.GetChild("OptionTitle04")
		
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
		
	def SetButtonText(self,button_peace,button_revenge,button_guild,button_free):
		self.buttonPeaceText.SetText(button_peace)
		self.buttonRevengeText.SetText(button_revenge)
		self.buttonGuildText.SetText(button_guild)
		self.buttonFreeText.SetText(button_free)	

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
		self.index = 0
		self.eventFunc = None
		self.eventArgs = None
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
		self.onTextLine = self.GetChild("enableOptionTitle")
		self.offTextLine = self.GetChild("disableOptionTitle")
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
	
	def SetOnButtonText(self,text):
		self.onTextLine.SetText(text)
		
	def SetOffButtonText(self,text):
		self.offTextLine.SetText(text)
	
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

	def LinkEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args
	
	def GetStatus(self):
		return self.status

	def SetIndex(self,index):
		self.index = int(index)
		
	def SetStatus(self,status):
		self.status = status
		if status:
			self.greenBar.Show()
			self.redBar.Hide()		
		
		else:
			self.greenBar.Hide()
			self.redBar.Show()			
		
	def GetIndex(self):
		return self.index
	
	def Enable(self):
		if self.status == True:
			return
		
		self.status = True
		self.greenBar.Show()
		self.redBar.Hide()
		try:
			if self.eventFunc:
				snd.PlaySound("sound/ui/click.wav")
				apply(self.eventFunc, self.eventArgs)
		
		except:
			return		
			
	def Disable(self):
		if self.status == False:
			return
		
		self.status = False
		self.greenBar.Hide()
		self.redBar.Show()		
		try:
			if self.eventFunc:
				snd.PlaySound("sound/ui/click.wav")
				apply(self.eventFunc, self.eventArgs)
		
		except:
			return		