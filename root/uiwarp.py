from __future__ import division
import ui
import app
import fgGHGjjFHJghjfFG1545gGG
import item
import uiToolTip  
import wndMgr 
import grp
import constInfo
import event
import localeInfo
import mouseModule
import interfacemodule
import uiCommon
import ime
import chat


WINDOW_COUNT = 8

WARP_EMPIRE_A1 	= 0
WARP_EMPIRE_A3 	= 1
WARP_DUNGEON 	= 2
WARP_FARM		= 4
WARP_LEVEL		= 5
WARP_BOSS		= 6
WARP_OTHER		= 3
WARP_EVENT		= 7

WARP_COUNT = 8


MAP_UNAVAILABLE = 0
MAP_AVAILABLE = 1

class WarpWindow(ui.ScriptWindow):

	page = 0
	sub_page = 0
	sub_page_count = 0
	
	shortcut_mode = 0
	quest_index = 0
	
	button_name_dict = {
		WARP_EMPIRE_A1 : localeInfo.WARP_EMPIRE_A1,
		WARP_EMPIRE_A3 : localeInfo.WARP_EMPIRE_A3,
		WARP_DUNGEON : localeInfo.WARP_DUNGEON,
		WARP_FARM : localeInfo.WARP_FARM,
		WARP_LEVEL : localeInfo.WARP_LEVEL,
		WARP_BOSS : localeInfo.WARP_BOSS,
		WARP_OTHER : localeInfo.WARP_OTHER,
		WARP_EVENT : localeInfo.WARP_EVENT,
	}
	
	
	def SetDefaultWarpDict(self):
		self.warpList = {
			
			WARP_EMPIRE_A1 : [
				{
					"name" : localeInfo.WARP_MAP_NAME_C1,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_3",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_A1,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_1",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_B1,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_2",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				}

			],
		
		WARP_EMPIRE_A3 : [
				{
					"name" : localeInfo.WARP_MAP_NAME_C3,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_A3,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_30",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_B3,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_31",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},

			],
		
		WARP_DUNGEON : [
			
				{
					"name" : localeInfo.WARP_MAP_NAME_SPIDERD,
					"min_level" : 20,
					"max_level" : 0,
					"default_image" : "map_4",
					"disable_image" : "map_4_d",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_DEVILTOWER,
					"min_level" : 40,
					"max_level" : 0,
					"default_image" : "map_6",
					"disable_image" : "Map_6_d",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_DRAGON,
					"min_level" : 75,
					"max_level" : 0,
					"default_image" : "map_7",
					"disable_image" : "map_7_d",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_CATACOMB,
					"min_level" : 90,
					"max_level" : 0,
					"default_image" : "map_33",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_RUNE,
					"min_level" : 100,
					"max_level" : 0,
					"default_image" : "map_10",
					"disable_image" : "map_10_d",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_FIRE,
					"min_level" : 110,
					"max_level" : 0,
					"default_image" : "map_11",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_ICE,
					"min_level" : 130,
					"max_level" : 0,
					"default_image" : "map_34",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				}
			],
			
		WARP_FARM : [
				
				{
					"name" : localeInfo.WARP_MAP_NAME_FARM1,
					"min_level" : 10,
					"max_level" : 55,
					"default_image" : "map_18",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_FARM2,
					"min_level" : 55,
					"max_level" : 75,
					"default_image" : "map_24",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_FARM3,
					"min_level" : 55,
					"max_level" : 90,
					"default_image" : "map_20",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_FARM4,
					"min_level" : 90,
					"max_level" : 105,
					"default_image" : "map_fm4",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_FARM5,
					"min_level" : 105,
					"max_level" : 115,
					"default_image" : "map_fm5",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_FARM6,
					"min_level" : 115,
					"max_level" : 125,
					"default_image" : "map_fm6",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
			],
			
		WARP_LEVEL : [
				{
					"name" : localeInfo.WARP_MAP_NAME_LEVELMAP,
					"min_level" : 90,
					"max_level" : 0,
					"default_image" : "map_27",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				
			],
			
		WARP_BOSS : [
				{
					"name" : localeInfo.WARP_MAP_NAME_BOSS_START,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_28",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
				{
					"name" : localeInfo.WARP_MAP_NAME_BOSS_RANDOM,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_28",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},
			],
			
		WARP_OTHER : [
				{
					"name" : localeInfo.WARP_MAP_NAME_SD1,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_13",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},		
				{
					"name" : localeInfo.WARP_MAP_NAME_SD2,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_13",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},		
				{
					"name" : localeInfo.WARP_MAP_NAME_GHOST,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_15",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},		
				{
					"name" : localeInfo.WARP_MAP_NAME_RED,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_16",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},		
				{
					"name" : localeInfo.WARP_MAP_NAME_TEMPLE,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_17",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				},					
				{
					"name" : localeInfo.WARP_MAP_NAME_YONGBI,
					"min_level" : 0,
					"max_level" : 0,
					"default_image" : "map_21",
					"disable_image" : "",
					
					"item" : [],
					
					"is_avail" : MAP_AVAILABLE,
					
					"f_key" : 0,
				}
			],
		
		WARP_EVENT : [],
			
		}
	
	

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/warpboard.py")
		except:
			import exception
			exception.Abort("WarpWindow.LoadWindow.LoadObject")
			
		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()

		self.pageButtons = []
		for i in xrange(WARP_COUNT):
			self.pageButtons.append(self.GetChild("nav_button_" + str(i)))
			self.pageButtons[i].SetText(self.button_name_dict[i])
			self.pageButtons[i].SetEvent(lambda arg=i: self.SetPage(arg))		
		
		self.MapBoards			= []
		self.MapImages			= []
		self.MapNames			= []
		self.ItemSlots			= []
		self.LevelText			= []
		self.WarpButtons		= []
		self.ShortcutButtons	= []
		for i in xrange(WINDOW_COUNT):
			self.MapImages.append(self.GetChild("warp_box_" + str(i)))
			self.MapBoards.append(self.GetChild("warp_box_frame_" + str(i)))
			self.MapNames.append(self.GetChild("map_name_text_" + str(i)))
			self.ItemSlots.append(self.GetChild("itemSlot_" + str(i)))
			self.LevelText.append(self.GetChild("map_level_text_" + str(i)))
			self.WarpButtons.append(self.GetChild("warp_button_" + str(i)))
			self.ShortcutButtons.append(self.GetChild("shortcut_button_" + str(i)))
			self.ShortcutButtons[i].SetEvent(lambda arg=i: self.OpenKeyWindow(arg))	
			self.WarpButtons[i].SetEvent(lambda arg=i: self.OnClickWarpButton(arg))	
			self.WarpButtons[i].SetText(localeInfo.WARP_BUTTON_WARP)
			self.ShortcutButtons[i].SetText(localeInfo.WARP_BUTTON_ADD_SHORTCUT)
			
		self.subPageTextLine = self.GetChild("pageNumber_Text")
		self.subPageButtonLeft = self.GetChild("page_button_left")
		self.subPageButtonRight = self.GetChild("page_button_right")

		self.subPageButtonLeft.SetEvent(self.OnPressLeftSubPageButton)
		self.subPageButtonRight.SetEvent(self.OnPressRightSubPageButton)

		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.shortcut_ToggleButton = self.GetChild("nav_button_save")
		self.shortcut_Board = self.GetChild("shortcut_background")
		self.shortcut_CloseButton = self.GetChild("shortcut_close_button")
		self.shortcut_DescTextLine = self.GetChild("shortcut_desc")

		self.shortcut_ToggleButton.SetToggleDownEvent(self.OnBeginShortcutMode)
		self.shortcut_ToggleButton.SetToggleUpEvent(self.OnEndShortcutMode)
		self.shortcut_ToggleButton.SetText(localeInfo.WARP_MANAGE_SHORTCUT)
		self.shortcut_DescTextLine.SetText(localeInfo.WARP_SHORTCUT_DESC)
		self.shortcut_CloseButton.SetText(localeInfo.WARP_SHORTCUT_CLOSE)
		self.shortcut_CloseButton.SetEvent(self.CloseKeyWindow)
		
		self.shortcut_Board.Hide()
		
		
		self.SetDefaultWarpDict()
		
		# self.GetChild("nav_board").HideBottom()
		# self.pageButtons[0].SetText(str(self.warpList[WARP_EMPIRE_A1][0]["item"][0]))
		self.SetPage(0)	
		# self.Open()
	
	def Destroy(self):
		self.__del__()
			
	def SetQuestIndex(self,idx):
		self.quest_index = int(idx)
		
	def OnClickWarpButton(self,idx):
		if self.quest_index == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[WARP]: NO QIDX")
			return
			
		a = self.start_idx + idx
		warpInfo = self.warpList[self.page][a]["name"]
		constInfo.INPUT_CMD = "WARP#" + str(self.page) + "#" + str(a) + "#"
		event.QuestButtonClick(self.quest_index)
		
		# chat.AppendChat(chat.CHAT_TYPE_INFO,"OnClickWarpButton: " + str(warpInfo))
	
	def CloseShortcutBoard(self):
		self.shortcut_Board.Hide()
			
	def SetPage(self,idx):
		for i in xrange(WARP_COUNT):
			if i == idx:
				self.pageButtons[i].Disable()
			else:
				self.pageButtons[i].Enable()
			
			
		self.page = int(idx)
		self.sub_page = 1
		self.sub_page_count = 0
		self.start_idx = 0
		
		self.BuildWarpBox()
		
	def BuildWarpBox(self):
		warpCount = len(self.warpList[self.page])
		self.sub_page_count = self.ToPageCount(warpCount)
		self.subPageTextLine.SetText(str(self.sub_page) + " / " + str(self.ToPageCount(warpCount)))
		self.BuildSubPage()
		
	def BuildSubPage(self):
		self.ClearSubPage()
		
		subPageMapInfo = self.warpList[self.page]
		
		a = self.start_idx
		for i in xrange(WINDOW_COUNT):
			if a < len(self.warpList[self.page]):
				subPageMapInfo = self.warpList[self.page][a]
				
				if subPageMapInfo["default_image"] != "":
					self.MapImages[i].LoadImage("images_warp/" + str(subPageMapInfo["default_image"]) + ".tga")
				else:
					self.MapImages[i].LoadImage("images_warp/unknown.tga")
				
				self.MapNames[i].SetText(subPageMapInfo["name"])
				
				if len(subPageMapInfo["item"]) > 0:
					self.ItemSlots[i].SetItemSlot(0,subPageMapInfo["item"][0],subPageMapInfo["item"][1])
				
				if subPageMapInfo["min_level"] == 0:
					self.LevelText[i].SetText("")
					
				else:
					if subPageMapInfo["max_level"] == 0:
						self.LevelText[i].SetText("[ Lv." + str(subPageMapInfo["min_level"]) + " ]")
				
					else:
						self.LevelText[i].SetText("[ Lv." + str(subPageMapInfo["min_level"]) + " - Lv." + str(subPageMapInfo["max_level"]) + " ]")
						
				self.MapImages[i].Show()
				a = a + 1
				
		self.CheckSubPage()		
			
	
	def CheckSubPage(self):
		subPageMapInfo = self.warpList[self.page]
		
		a = self.start_idx
		for i in xrange(WINDOW_COUNT):
			if a < len(self.warpList[self.page]):
				subPageMapInfo = self.warpList[self.page][a]
				isAvail = True
				self.MapNames[i].SetText(subPageMapInfo["name"] + self.GetFKeyName(subPageMapInfo["f_key"]))

				player_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
				if subPageMapInfo["min_level"] > 0:
					if subPageMapInfo["max_level"] > 0:
						if player_level < subPageMapInfo["min_level"] or player_level > subPageMapInfo["max_level"]:
							isAvail = False
					
					else:
						if player_level < subPageMapInfo["min_level"]:
							isAvail = False
						
				if subPageMapInfo["is_avail"] == MAP_UNAVAILABLE:
					isAvail = False
					
					
				if not isAvail:
					if subPageMapInfo["disable_image"] != "":
						self.MapImages[i].LoadImage("images_warp/" + str(subPageMapInfo["disable_image"]) + ".tga")
					
					self.WarpButtons[i].Disable()
				else:
					if subPageMapInfo["default_image"] != "":
						self.MapImages[i].LoadImage("images_warp/" + str(subPageMapInfo["default_image"]) + ".tga")
					
					self.WarpButtons[i].Enable()					
				# self.MapImages[i].Show()
				a = a + 1	
				
	# def OnUpdate(self):
		# self.CheckSubPage()
	
	def GetFKeyName(self,key):
		if key == 0:
			return ""
		else:
			return " [F" + str(key) + "]"
	
	def ClearSubPage(self):
		for i in xrange(WINDOW_COUNT):
			self.MapImages[i].Hide()
	
	def ToPageCount(self,count):
		i = count
		c = 1
		while i > 7:
			c = c + 1
			i = i - 8
			
		return c
		
	def OnPressLeftSubPageButton(self):
		if self.sub_page == 1:
			# self.sub_page = (self.sub_page_count * 8) - 1
			return
		else:
			self.sub_page = self.sub_page - 1
			self.start_idx = self.start_idx - 8
			if self.start_idx < 0:
				self.start_idx = 0
			
		self.subPageTextLine.SetText(str(self.sub_page) + " / " + str(self.sub_page_count))
		self.BuildSubPage()
	
	def OnPressRightSubPageButton(self):
		if self.sub_page == self.sub_page_count:
			# self.start_idx = 0
			return
		else:
			self.sub_page = self.sub_page + 1	
			self.start_idx = self.start_idx + 8
			if self.start_idx < 0:
				self.start_idx = 0

			
		self.subPageTextLine.SetText(str(self.sub_page) + " / " + str(self.sub_page_count))
		self.BuildSubPage()
		
			
	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def OnBeginShortcutMode(self):
		self.shortcut_mode = 1
		
		for i in xrange(WARP_COUNT):
			self.pageButtons[i].Disable()
		
		subPageMapInfo = self.warpList[self.page]
		a = self.start_idx	
		for i in xrange(WINDOW_COUNT):
			self.WarpButtons[i].Hide()
			if a < len(self.warpList[self.page]):
				subPageMapInfo = self.warpList[self.page][a]
				if subPageMapInfo["f_key"] > 0:
					self.ShortcutButtons[i].SetText(localeInfo.WARP_BUTTON_DEL_SHORTCUT)
				else:
					self.ShortcutButtons[i].SetText(localeInfo.WARP_BUTTON_ADD_SHORTCUT)
			a = a + 1
		self.subPageButtonLeft.Hide()
		self.subPageButtonRight.Hide()
		
	def OnEndShortcutMode(self):
		self.shortcut_mode = 0
		for i in xrange(WARP_COUNT):
			if i != self.page:
				self.pageButtons[i].Enable()
			
		for i in xrange(WINDOW_COUNT):
			self.WarpButtons[i].Show()	
			
		self.subPageButtonLeft.Show()
		self.subPageButtonRight.Show()
		self.CloseKeyWindow()
		self.shortcut_ToggleButton.SetUp()
			
	def OpenKeyWindow(self,idx):
		a = self.start_idx + idx
		subPageMapInfo = self.warpList[self.page][a]
		if subPageMapInfo["f_key"] > 0:
			
			constInfo.INPUT_CMD = "SHORTDEL#" + str(subPageMapInfo["f_key"]) + "#"
			event.QuestButtonClick(self.quest_index)	

			
		
		else:
			self.shortcut_Config = int(idx)
			self.shortcut_Board.Show()

	def CloseKeyWindow(self):
		self.shortcut_Board.Hide()
	
	def PressFKey(self, key):
		chat.AppendChat(chat.CHAT_TYPE_INFO,"[WARP]: PressFKey")

		fKeyIndex = {}
		fKeyIndex[63] = 5
		fKeyIndex[64] = 6
		fKeyIndex[65] = 7
		fKeyIndex[66] = 8
		
		if self.shortcut_Board.IsShow():
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[WARP]: shortcut_Board.IsShow()")
			
			a = self.start_idx + self.shortcut_Config
			warpInfo = self.warpList[self.page][a]["name"]			
			
			
			chat.AppendChat(chat.CHAT_TYPE_INFO,"F" + str(fKeyIndex[key]))
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Shortcut for Map: " + str(warpInfo))

			self.shortcut_Board.Hide()
			
			constInfo.INPUT_CMD = "SHORTSET#" + str(fKeyIndex[key]) + "#" + str(self.page) + "#" + str(a) + "#"
			event.QuestButtonClick(self.quest_index)
			
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Warp to Shortcut F" + str(fKeyIndex[key]))
			
			constInfo.INPUT_CMD = "SHORTWARP#" + str(fKeyIndex[key]) + "#"
			event.QuestButtonClick(self.quest_index)

	def SetFKey(self,page,idx,key):
		self.warpList[page-1][idx-1]["f_key"] = int(key)
		self.Refresh()
		
	def Refresh(self):
		self.CheckSubPage()
		a = 0
		if self.shortcut_mode == 1:
			subPageMapInfo = self.warpList[self.page]
			a = self.start_idx	
			for i in xrange(WINDOW_COUNT):
				self.WarpButtons[i].Hide()
				if a < len(self.warpList[self.page]):
					subPageMapInfo = self.warpList[self.page][a]
					if subPageMapInfo["f_key"] > 0:
						self.ShortcutButtons[i].SetText(localeInfo.WARP_BUTTON_DEL_SHORTCUT)
					else:
						self.ShortcutButtons[i].SetText(localeInfo.WARP_BUTTON_ADD_SHORTCUT)
				a = a + 1
		
		
	def Open(self):
		if self.IsShow():
			self.Close()
			return
			
		self.Show()
		self.SetPage(0)

		
	def Close(self):
		self.OnEndShortcutMode()
		self.Hide()
		

		
		
# LuckTreasufreWindow().Show()		
		
						
