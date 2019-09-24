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
import uimainquest
import uimultishop
import settinginfo
from uiGuild import MouseReflector

GM_PANEL_DICT = {
	"qid" : {},
	"event_qid" : {},

}

class GMPanel(ui.ScriptWindow):
	
	BUTTON_SUPPORT_PANEL = 0
	BUTTON_ANNOUNCEMENT = 1
	BUTTON_EVENT = 2
	BUTTON_INVINCIBILITY = 3
	BUTTON_BIG_DAMAGE = 4
	BUTTON_DEBUG = 5
	BUTTON_SYSTEM = 6
	BUTTON_REGEN = 7
	BUTTON_QUEST = 8
	BUTTON_QUEST_TEXT_TOOL = 9
	BUTTON_MULTISHOP_EDITOR = 10
	BUTTON_ITEM_MAKER = 11
	
	BUTTON_MAX = 12

	gm_permission_list = []
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/gmpanel.py")
		except:
			import exception
			exception.Abort("GMPanel.LoadWindow.LoadObject")
		
		self.supportPanel = SupportWindow(self.BUTTON_SUPPORT_PANEL) 
		self.systemPanel = SystemManagePanel(self.BUTTON_SYSTEM)
		self.eventPanel = EventPanel(self.BUTTON_EVENT)
		
		self.regenMaker = RegenMaker(self.BUTTON_REGEN) 
		self.questMaker = uimainquest.QuestMaker(self.BUTTON_QUEST)
		self.questTextMaker = uimainquest.QuestTextTool(self.BUTTON_QUEST_TEXT_TOOL)
		self.multiShopEditor = uimultishop.MultiShopEditorWindow()
		
		self.itemMaker = ItemMakerWindow(self.BUTTON_ITEM_MAKER)
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		self.gmPanelButtons = []
		for i in xrange(self.BUTTON_MAX):
			self.gmPanelButtons.append(self.GetChild("gm_panel_" + str(i)))

		self.gmPanelButtons[self.BUTTON_SUPPORT_PANEL].SetEvent(self.ToggleSupportWindow)
		self.gmPanelButtons[self.BUTTON_EVENT].SetEvent(self.ToggleEventPanelWindow)
		self.gmPanelButtons[self.BUTTON_ANNOUNCEMENT].SetEvent(self.ToggleAnnouncementWindow)
		self.gmPanelButtons[self.BUTTON_INVINCIBILITY].SetEvent(self.ToggleGMToggle,self.BUTTON_INVINCIBILITY)
		self.gmPanelButtons[self.BUTTON_BIG_DAMAGE].SetEvent(self.ToggleGMToggle,self.BUTTON_BIG_DAMAGE)
		self.gmPanelButtons[self.BUTTON_DEBUG].SetEvent(self.ToggleGMToggle,self.BUTTON_DEBUG)
		self.gmPanelButtons[self.BUTTON_SYSTEM].SetEvent(self.ToggleSystemPanel)
		self.gmPanelButtons[self.BUTTON_REGEN].SetEvent(self.ToggleRegenMaker)
		self.gmPanelButtons[self.BUTTON_QUEST].SetEvent(self.ToggleQuestMaker)
		self.gmPanelButtons[self.BUTTON_QUEST_TEXT_TOOL].SetEvent(self.ToggleQuestTextMaker)
		self.gmPanelButtons[self.BUTTON_MULTISHOP_EDITOR].SetEvent(self.ToggleMultiShopEditor)
		self.gmPanelButtons[self.BUTTON_ITEM_MAKER].SetEvent(self.ToggleItemMaker)
		
		# self.ActivateButton(self.BUTTON_INVINCIBILITY)
		# self.InsertGMPermission(self.BUTTON_MULTISHOP_EDITOR)
		
		# self.InsertGMPermission(self.BUTTON_ITEM_MAKER)
		
	def InsertGMPermission(self,permission):
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "InsertGMPermission : " + str(permission) + "!")
		self.gm_permission_list.append(permission)
		# self.RefreshButtonList()
		
	def RefreshButtonList(self):
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "permission_list : " + str(len(self.gm_permission_list)) + " Enable!")
		for i in xrange(self.BUTTON_MAX):
			if i in self.gm_permission_list:
				# chat.AppendChat(chat.CHAT_TYPE_INFO, "button : " + str(i) + " Enable!")
				# chat.AppendChat(chat.CHAT_TYPE_INFO, "gm_permission_list : " + str(self.gm_permission_list[i]) + " Enable!")
				self.gmPanelButtons[i].Enable()
			else:
				# chat.AppendChat(chat.CHAT_TYPE_INFO, "button : " + str(i) + " Disable!")
				self.gmPanelButtons[i].Disable()

	def ActivateButton(self,button):
		self.gmPanelButtons[button].SetUpVisual("yamato_button/wide_button_a_n.tga")
		self.gmPanelButtons[button].SetOverVisual("yamato_button/wide_button_a_h.tga")
		self.gmPanelButtons[button].SetDownVisual("yamato_button/wide_button_a_p.tga")
	
	def DeactivateButton(self,button):
		self.gmPanelButtons[button].SetUpVisual("yamato_helpboard/wide_button_n.tga")
		self.gmPanelButtons[button].SetOverVisual("yamato_helpboard/wide_button_h.tga")
		self.gmPanelButtons[button].SetDownVisual("yamato_helpboard/wide_button_p.tga")		
			
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
		
	def Destroy(self):
		self.gm_permission_list = None
		self.gmPanelButtons = None
		self.supportPanel.Destroy()
		self.eventPanel.Destroy()
		self.regenMaker.Destroy()
		self.systemPanel.Destroy()
		self.questMaker.Destroy()
		self.__del__()	
	
	def ToggleSupportWindow(self):
		self.supportPanel.Open()
	
	def ToggleEventPanelWindow(self):
		self.eventPanel.Open()
	
	def ToggleAnnouncementWindow(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/announcement")
	
	def ToggleGMToggle(self,button):
		constInfo.INPUT_CMD = str(button) + "#"
		event.QuestButtonClick(GM_PANEL_DICT["qid"][button])		
	
	def ToggleSystemPanel(self):
		self.systemPanel.Open()
	
	def ToggleRegenMaker(self):
		self.regenMaker.Open()

	def ToggleQuestMaker(self):
		self.questMaker.Open()
		
	def ToggleQuestTextMaker(self):
		self.questTextMaker.Open()
		
	def ToggleMultiShopEditor(self):
		self.multiShopEditor.Open()
		
	def ToggleItemMaker(self):
		self.itemMaker.Open()
		
class SupportWindow(ui.ScriptWindow):
	

	SYSTEM_INDEX = 0
	
	requestContent = []
	lastRefresh = 0
	forceUpdate = 60
		
	def __init__(self, systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/supportwindow.py")
		except:
			import exception
			exception.Abort("AdventWindow.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.updateButton = self.GetChild("updateButton")
		self.updateTextLine = self.GetChild("lastUpdateTextLine")
		self.listBox = self.GetChild("playerListBox")
		self.scrollBar = self.GetChild("scrollBar")
		
		self.acceptButton = self.GetChild("messageButton")
		self.deleteButton = self.GetChild("deleteButton")
				
		self.updateButton.SetEvent(self.Clear)
		
		self.AppendSupportInfo("[SA]Exterminatus","Deutsch",0)
		self.AppendSupportInfo("[SA]Exterminatus","Deutsch",1)
		self.BuildSupportList()
		##################
		## DEV SPÄTER LÖSCHEN!!!
		# self.Open()
	
		self.lastRefresh = app.GetTime()
	
	def Clear(self):
		self.listBox.ClearItem()
		self.scrollBar.Hide()
		self.acceptButton.Disable()
		self.deleteButton.Disable()
		self.requestContent = []
		self.lastRefresh = app.GetTime()
		
	def BuildSupportList(self):
		for i in xrange(len(self.requestContent)):
			
			self.listBox.InsertSupportItem(0,"[SA]Exterminatus","Deutsch",0)
	

	def AppendSupportInfo(self,name,language,status):
		item = {
			"name" : str(name),
			"language" : str(language),
			"status" : int(status),
		
		}
		
		self.requestContent.append(item)
		
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
			return
			
		self.Show()

	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.__del__()	
		
	def OnUpdate(self):
		if self.IsShow():
			sec = int(app.GetTime() - self.lastRefresh)
			if sec < self.forceUpdate:
				self.updateTextLine.SetText("Letztes Update: Vor " + str(sec) + " Sek.")
			
			else:
				self.Clear()
	
class EventPanel(ui.ScriptWindow):

	SYSTEM_INDEX = 0

	EVENT_TEMP_DROP = 0
	EVENT_OX = 1
	EVENT_TREASURE_HUNT = 2
	EVENT_MOONLIGHT = 3
	EVENT_FISH = 4
	EVENT_CASTLE_SIEGE = 5
	EVENT_EMPIRE_PILLAGE = 6
	
	EVENT_MAX = 7
	main_page = 0
	sub_page = 0
	
	def __init__(self,systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/eventpanel.py")
		except:
			import exception
			exception.Abort("EventPanelWindow.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.eventNavigationButtons = []
		for i in xrange(self.EVENT_MAX):
			self.eventNavigationButtons.append(self.GetChild("event_button_" + str(i)))
		
		self.eventMainPages = []
		self.eventMainPages.append(self.GetChild("temp_event_window"))	
		

		self.eventNavigationButtons[self.EVENT_TEMP_DROP].SetEvent(self.LoadPage,self.EVENT_TEMP_DROP)
		
		# Load Event Windows
		self.LoadTempEventWindow()
		
		self.LoadPage(self.EVENT_TEMP_DROP)
		
		
		
	##########################################################################################
	## Temp. Drop Event Configuration Menu
	##########################################################################################
	
	def LoadTempEventWindow(self):
		self.eventTempDropSubPage01 = self.GetChild("addNewEventWindow")
		self.eventTempDropSubPage02 = self.GetChild("manageEventWindow")
	
		# AddNewEvent
		self.eventTempDrop_NameEditLine = self.GetChild("tempDropEvent_Add_NameEditLine")
		self.eventTempDrop_TargetEditLine = self.GetChild("tempDropEvent_Add_TargetEditLine")
		self.eventTempDrop_TargetEditLineBoard = self.GetChild("tempDropEvent_Add_TargetEditLineBoard")
		self.eventTempDrop_VnumEditLine = self.GetChild("tempDropEvent_Add_VnumEditLine")
		self.eventTempDrop_DurationEditline = self.GetChild("tempDropEvent_Add_TimeEditLine")
		self.eventTempDrop_DropChanceEditLine = self.GetChild("tempDropEvent_Add_ChanceEditLine")
		
		self.eventTempDrop_MinLevelEditLine = self.GetChild("tempDropEvent_Add_MinLevelEditLine")
		self.eventTempDrop_MaxLevelEditLine = self.GetChild("tempDropEvent_Add_MaxLevelEditLine")
		
		self.eventTempDrop_AddButton = self.GetChild("tempDropEvent_Add_SendButton")
		self.eventTempDrop_ClearButton = self.GetChild("tempDropEvent_Add_ClearButton")
		self.eventTempDrop_DropTypeButton = self.GetChild("tempDropEvent_Add_DropTypeButton")

		self.eventTempDrop_TargetTextLine = self.GetChild("tempDropEvent_Add_TargetVnumTextLine")
		# ManageEvents
		self.eventTempDrop_TabButton_Add = self.GetChild("addTempEventButton")
		self.eventTempDrop_TabButton_Manage = self.GetChild("manageTempEventButton")
		
		self.eventTempDrop_Manage_ListBox = self.GetChild("tempDropEvent_MANAGE_ListBox")
		self.eventTempDrop_Manage_Scrollbar = self.GetChild("tempDropEvent_MANAGE_Scrollbar")
		self.eventTempDrop_Manage_LoadButton = self.GetChild("tempDropEvent_MANAGE_LoadButton")
		self.eventTempDrop_Manage_DeleteButton = self.GetChild("tempDropEvent_MANAGE_DeleteButton")
		
		self.eventTempDropNameList = {}
		self.eventTempDrop_Manage_ListBox.ClearItem()
		self.eventTempDrop_Manage_DeleteButton.Disable()
		
		self.eventTempDrop_Manage_LoadButton.SetEvent(self.LoadTempDropEventList)
		self.eventTempDrop_Manage_Scrollbar.SetScrollEvent(self.ScrollTempDropEventList)
		# 10
		self.eventTempDrop_AddButton.SetEvent(self.OnSendTempEventForm)
		self.eventTempDrop_ClearButton.SetEvent(self.OnClearTempEventForm)
		
		self.eventTempDrop_TabButton_Add.Disable()
		self.eventTempDrop_TabButton_Add.SetEvent(self.OnChangeTempDropEventSubPage,0)
		self.eventTempDrop_TabButton_Manage.SetEvent(self.OnChangeTempDropEventSubPage,1)
		
		self.TEMP_DROP_TYPE_SINGLE	= 0
		self.TEMP_DROP_TYPE_MAP		= 1
		self.TEMP_DROP_TYPE_DUNGEON = 2
		self.TEMP_DROP_TYPE_ALL		= 3
		
		self.TEMP_DROP_TYPE_STRING_DICT = {
			self.TEMP_DROP_TYPE_SINGLE	: localeInfo.EVENT_TEMP_DROP_TYPE_SINGLE,
			self.TEMP_DROP_TYPE_MAP		: localeInfo.EVENT_TEMP_DROP_TYPE_MAP,
			self.TEMP_DROP_TYPE_DUNGEON : localeInfo.EVENT_TEMP_DROP_TYPE_DUNGEON,
			self.TEMP_DROP_TYPE_ALL		: localeInfo.EVENT_TEMP_DROP_TYPE_ALL,
		}
		
		self.dropType = self.TEMP_DROP_TYPE_SINGLE
		self.eventTempDrop_DropTypeButton.SetText(self.TEMP_DROP_TYPE_STRING_DICT[self.dropType])
		self.eventTempDrop_DropTypeButton.SetEvent(self.ChangeTempDropType)
		
		self.eventTempDrop_HelpButton_Title = exterminatus.HelpButtonWindow()
		self.eventTempDrop_HelpButton_Title.SetParent(self.eventMainPages[self.EVENT_TEMP_DROP])
		self.eventTempDrop_HelpButton_Title.SetPosition(215,6)
		self.eventTempDrop_HelpButton_Title.DefineToolTipContent(localeInfo.EVENT_TEMP_DROP_HELP_TITLE)
		self.eventTempDrop_HelpButton_Title.Show()		

		self.eventTempDrop_HelpButton_EventName = exterminatus.HelpButtonWindow()
		self.eventTempDrop_HelpButton_EventName.SetParent(self.eventTempDropSubPage01)
		self.eventTempDrop_HelpButton_EventName.SetPosition(220,15)
		self.eventTempDrop_HelpButton_EventName.DefineToolTipContent(localeInfo.EVENT_TEMP_DROP_HELP_NAME)
		self.eventTempDrop_HelpButton_EventName.Show()	

		self.eventTempDrop_HelpButton_Target = exterminatus.HelpButtonWindow()
		self.eventTempDrop_HelpButton_Target.SetParent(self.eventTempDropSubPage01)
		self.eventTempDrop_HelpButton_Target.SetPosition(220,15 + 30)
		self.eventTempDrop_HelpButton_Target.DefineToolTipContent(localeInfo.EVENT_TEMP_DROP_HELP_TARGET)
		self.eventTempDrop_HelpButton_Target.Show()

		self.eventTempDrop_HelpButton_ItemVnum = exterminatus.HelpButtonWindow()
		self.eventTempDrop_HelpButton_ItemVnum.SetParent(self.eventTempDropSubPage01)
		self.eventTempDrop_HelpButton_ItemVnum.SetPosition(220,15 + 30 + 30)
		self.eventTempDrop_HelpButton_ItemVnum.DefineToolTipContent(localeInfo.EVENT_TEMP_DROP_HELP_ITEMVNUM)
		self.eventTempDrop_HelpButton_ItemVnum.Show()		

		self.eventTempDrop_HelpButton_Duration = exterminatus.HelpButtonWindow()
		self.eventTempDrop_HelpButton_Duration.SetParent(self.eventTempDropSubPage01)
		self.eventTempDrop_HelpButton_Duration.SetPosition(220,15 + 30 + 30 + 30)
		self.eventTempDrop_HelpButton_Duration.DefineToolTipContent(localeInfo.EVENT_TEMP_DROP_HELP_DURATION)
		self.eventTempDrop_HelpButton_Duration.Show()
		
		self.eventTempDrop_HelpButton_DropChance = exterminatus.HelpButtonWindow()
		self.eventTempDrop_HelpButton_DropChance.SetParent(self.eventTempDropSubPage01)
		self.eventTempDrop_HelpButton_DropChance.SetPosition(220,15 + 30 + 30 + 30 + 30)
		self.eventTempDrop_HelpButton_DropChance.DefineToolTipContent(localeInfo.EVENT_TEMP_DROP_HELP_DROP_CHANCE)
		self.eventTempDrop_HelpButton_DropChance.Show()

		self.eventTempDrop_HelpButton_LevelRange = exterminatus.HelpButtonWindow()
		self.eventTempDrop_HelpButton_LevelRange.SetParent(self.eventTempDropSubPage01)
		self.eventTempDrop_HelpButton_LevelRange.SetPosition(220,15 + 30 + 30 + 30 + 30 + 30)
		self.eventTempDrop_HelpButton_LevelRange.DefineToolTipContent(localeInfo.EVENT_TEMP_DROP_HELP_LEVEL_RANGE)
		self.eventTempDrop_HelpButton_LevelRange.Show()
	
	def LoadTempDropEventList(self):
		self.eventTempDropNameList = {}
		self.eventTempDrop_Manage_ListBox.ClearItem()
		constInfo.INPUT_CMD = "load#"
		event.QuestButtonClick(GM_PANEL_DICT["event_qid"][self.EVENT_TEMP_DROP])
	
	def ScrollTempDropEventList(self):
		return
	
	
	def AppendTempDropEventList(self,name):
		self.eventTempDropNameList[len(self.eventTempDropNameList)] = name
		self.eventTempDrop_Manage_DeleteButton.Enable()
		self.eventTempDrop_Manage_ListBox.InsertItem(i,name)		
	
	
	def DeleteTempDropEventItem(self):
		return
	
	
	def ChangeTempDropType(self):
		self.dropType = self.dropType + 1
		if self.dropType > self.TEMP_DROP_TYPE_ALL:
			self.dropType = self.TEMP_DROP_TYPE_SINGLE
		
		self.eventTempDrop_DropTypeButton.SetText(self.TEMP_DROP_TYPE_STRING_DICT[self.dropType])
		
		if self.dropType == self.TEMP_DROP_TYPE_SINGLE:
			self.eventTempDrop_TargetTextLine.SetText(localeInfo.EVENT_TEMP_DROP_TARGET_MOB)
			self.eventTempDrop_TargetTextLine.Show()
			self.eventTempDrop_TargetEditLineBoard.Show()
			self.eventTempDrop_HelpButton_Target.Show()
		
		elif self.dropType == self.TEMP_DROP_TYPE_MAP:
			self.eventTempDrop_TargetTextLine.SetText(localeInfo.EVENT_TEMP_DROP_TARGET_MAP)
			self.eventTempDrop_TargetTextLine.Show()
			self.eventTempDrop_TargetEditLineBoard.Show()
			self.eventTempDrop_HelpButton_Target.Show()
		
		elif self.dropType == self.TEMP_DROP_TYPE_DUNGEON:
			self.eventTempDrop_TargetTextLine.SetText(localeInfo.EVENT_TEMP_DROP_TARGET_MAP)
			self.eventTempDrop_TargetTextLine.Show()
			self.eventTempDrop_TargetEditLineBoard.Show()
			self.eventTempDrop_HelpButton_Target.Show()
		
		elif self.dropType == self.TEMP_DROP_TYPE_ALL:
			self.eventTempDrop_TargetTextLine.Hide()
			self.eventTempDrop_TargetEditLineBoard.Hide()
			self.eventTempDrop_HelpButton_Target.Hide()

	
	def OnSendTempEventForm(self):
		eventName = self.eventTempDrop_NameEditLine.GetText()
		if len(eventName) <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EVENT_TEMP_DROP_ERROR_NO_NAME)
			return

		eventTarget = self.eventTempDrop_TargetEditLine.GetText()
		if len(eventTarget) <= 0 and self.dropType != self.TEMP_DROP_TYPE_ALL:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EVENT_TEMP_DROP_ERROR_NO_TARGET)
			return
			
		eventItemVnum = self.eventTempDrop_VnumEditLine.GetText()
		if len(eventItemVnum) <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EVENT_TEMP_DROP_ERROR_NO_ITEMVNUM)
			return	

		eventDuration = self.eventTempDrop_DurationEditline.GetText()
		if len(eventDuration) <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EVENT_TEMP_DROP_ERROR_NO_DURATION)
			return

		eventDropChance = self.eventTempDrop_DropChanceEditLine.GetText()
		if len(eventDropChance) <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EVENT_TEMP_DROP_ERROR_NO_DROPCHANCE)
			return
			
		minLevel = self.eventTempDrop_MinLevelEditLine.GetText()
		if len(minLevel) <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EVENT_TEMP_DROP_ERROR_NO_MIN_LEVEL)
			return
			
		maxLevel = self.eventTempDrop_MaxLevelEditLine.GetText()
		if len(maxLevel) <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EVENT_TEMP_DROP_ERROR_NO_MAX_LEVEL)
			return
		
		# FIX!
		if self.dropType == self.TEMP_DROP_TYPE_ALL:
			eventTarget = "0"
		
		constInfo.INPUT_CMD = "add#" + str(eventName) + "#" + str(eventTarget) + "#" + str(eventItemVnum) + "#" + str(eventDuration) + "#" + str(eventDropChance) + "#" + str(minLevel) + "#" + str(maxLevel) + "#" + str(self.dropType)
		chat.AppendChat(chat.CHAT_TYPE_INFO,"add#" + str(eventName) + "#" + str(eventTarget) + "#" + str(eventItemVnum) + "#" + str(eventDuration) + "#" + str(eventDropChance) + "#" + str(minLevel) + "#" + str(maxLevel) + "#" + str(self.dropType))
		event.QuestButtonClick(GM_PANEL_DICT["event_qid"][self.EVENT_TEMP_DROP])
		self.OnClearTempEventForm()
		
	def OnClearTempEventForm(self):
		self.eventTempDrop_NameEditLine.SetText("")
		self.eventTempDrop_TargetEditLine.SetText("")
		self.eventTempDrop_VnumEditLine.SetText("")
		self.eventTempDrop_DurationEditline.SetText("")
		self.eventTempDrop_DropChanceEditLine.SetText("")	
		self.eventTempDrop_MinLevelEditLine.SetText("")
		self.eventTempDrop_MaxLevelEditLine.SetText("")

		
	def OnChangeTempDropEventSubPage(self,subPage):
		self.sub_page = subPage
		if subPage == 0:
			self.eventTempDropSubPage01.Show()
			self.eventTempDropSubPage02.Hide()			
			self.eventTempDrop_TabButton_Add.Disable()
			self.eventTempDrop_TabButton_Manage.Enable()
		else:
			self.eventTempDropSubPage01.Hide()
			self.eventTempDropSubPage02.Show()			
			self.eventTempDrop_TabButton_Manage.Disable()			
			self.eventTempDrop_TabButton_Add.Enable()			
			
	##########################################################################################
	## Event Panel Navigation
	##########################################################################################	
	def LoadPage(self,page):
		self.main_page = page
		self.sub_page = 0
		for i in xrange(self.EVENT_MAX):
			if i == page:
				self.eventNavigationButtons[i].Disable()
			else:
				self.eventNavigationButtons[i].Enable()
		
		for i in xrange(len(self.eventMainPages)):
			self.eventMainPages[i].Hide()
		
		
		# HIDE_SUB_WINDOWS
		# self.eventTempDropSubPage01.Hide()
		# self.eventTempDropSubPage02.Hide()
			
		# EVENT_TEMP_DROP INIT
		if page == self.EVENT_TEMP_DROP:
			self.eventMainPages[self.EVENT_TEMP_DROP].Show()
			self.eventTempDropSubPage01.Show()
			self.eventTempDropSubPage02.Hide()
			

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
		
	def Destroy(self):
		self.__del__()	
	
class SystemManagePanel(ui.ScriptWindow):

	SYSTEM_INDEX = 0
	
	
	def __init__(self,systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/systempanel.py")
		except:
			import exception
			exception.Abort("SystemPanelWindow.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)

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
		
	def Destroy(self):
		self.__del__()			
	
class RegenMaker(ui.ScriptWindow):

	SYSTEM_INDEX = 0
	
	ROTATION_RANDOM		= 0
	ROTATION_SOUTH		= 1
	ROTATION_SOUTHEAST	= 2
	ROTATION_EAST		= 3
	ROTATION_NORTHEAST	= 4
	ROTATION_NORTH		= 5
	ROTATION_NORTHWEST	= 6
	ROTATION_WEST		= 7
	ROTATION_SOUTHWEST	= 8
	
	MOB_TYPE_SINGLE			= 0
	MOB_TYPE_GROUP			= 1
	MOB_TYPE_RANDOM_GROUP	= 2
	
	
	rotation = ROTATION_RANDOM
	mob_type = MOB_TYPE_SINGLE
	def __init__(self, systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/regenmaker.py")
		except:
			import exception
			exception.Abort("RegenMaker.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.fileNameEditLine = self.GetChild("fileNameEditLine")
		self.mobVnumEditLine = self.GetChild("vnumEditLine")
		
		self.mobTypeButton = []
		self.mobTypeButton.append(self.GetChild("m_button"))
		self.mobTypeButton.append(self.GetChild("g_button"))
		self.mobTypeButton.append(self.GetChild("r_button"))
		
		self.mobTypeButton[self.MOB_TYPE_SINGLE].SetEvent(self.OnChangeMobType,self.MOB_TYPE_SINGLE)
		self.mobTypeButton[self.MOB_TYPE_GROUP].SetEvent(self.OnChangeMobType,self.MOB_TYPE_GROUP)
		self.mobTypeButton[self.MOB_TYPE_RANDOM_GROUP].SetEvent(self.OnChangeMobType,self.MOB_TYPE_RANDOM_GROUP)		
		
		self.rotationButton = []
		for i in xrange(9):
			self.rotationButton.append(self.GetChild("rotation_button_" + str(i)))
			self.rotationButton[i].SetEvent(self.OnChangeRotation,i)
		self.rotationButton[self.rotation].Disable()
		self.mobTypeButton[self.mob_type].Disable()
		
		self.randomValueEditLine = self.GetChild("randomEditLine")
		self.respawnTimeEditLine = self.GetChild("respawnTimeEditLine")
		self.placeButton = self.GetChild("place_button")
		self.placeButton.SetEvent(self.OnClickPlaceButton)
		
	def OnChangeRotation(self,rotation):
		self.rotation = rotation
		for i in xrange(9):
			if i == self.rotation:
				self.rotationButton[i].Disable()
			else:
				self.rotationButton[i].Enable()
				
	def OnChangeMobType(self,mobType):
		self.mob_type = mobType
		for i in xrange(3):
			if i == self.mob_type:
				self.mobTypeButton[i].Disable()
			else:
				self.mobTypeButton[i].Enable()		
	
	def OnClickPlaceButton(self):
		fileName = self.fileNameEditLine.GetText()
		mobValue = self.mobVnumEditLine.GetText()
		randomValue = self.randomValueEditLine.GetText()
		respawnTime = self.respawnTimeEditLine.GetText()
		constInfo.INPUT_CMD = str(fileName) + "#" + str(mobValue) + "#" + str(self.mob_type) + "#" + str(self.rotation) + "#" + str(randomValue) + "#" + str(respawnTime) + "#"
		event.QuestButtonClick(GM_PANEL_DICT["qid"][self.SYSTEM_INDEX])
		
		
	# def OnPressEscapeKey(self):
		# self.Close()
		# return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
		
		
	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.__del__()
			
class BioQuestMaker(ui.ScriptWindow):

	SYSTEM_INDEX = 0

	def __init__(self,systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/questmaker.py")
		except:
			import exception
			exception.Abort("QuestMakerWindow.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)

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
		
	def Destroy(self):
		self.__del__()
		
class ItemMakerWindow(ui.ScriptWindow):

	class ItemMakerSocketItem(ui.ScriptWindow):
	
		SOCKET_TYPE_NONE = 0
		SOCKET_TYPE_STONE = 1
		SOCKET_TYPE_TIME = 2
		SOCKET_TYPE_VALUE = 3

		def __init__(self, wndItemMaker):
			ui.ScriptWindow.__init__(self)
			self.wndItemMaker = wndItemMaker
			self.socketType = self.SOCKET_TYPE_NONE
			self.socketNumber = 0
			self.socketValue = 0
			self.socketValue2 = 0
			self.LoadWindow()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def LoadWindow(self):
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "exscript/itemmaker_socketitem.py")
			except:
				import exception
				exception.Abort("ItemMakerSocketItem.LoadWindow.LoadObject")
			
			self.background = self.GetChild("board")
			self.textLine = self.GetChild("socketTextLine")
			self.mouseReflector = MouseReflector(self.background)
			self.mouseReflector.SetSize(350 - 30 + 20 - 20, 20)
			self.mouseReflector.UpdateRect()	
			self.UpdateTextLine()
		
		def OnUpdate(self):
			if self.background.IsIn():
				self.mouseReflector.Show()
			else:
				self.mouseReflector.Hide()
			
			# self.UpdateTextLine()
			
		def UpdateTextLine(self):
			if self.socketType == self.SOCKET_TYPE_NONE:
				self.textLine.SetText("0")
			elif self.socketType == self.SOCKET_TYPE_STONE:
				item.SelectItem(self.socketValue)
				self.textLine.SetText(item.GetItemName())
			elif self.socketType == self.SOCKET_TYPE_TIME:
				self.textLine.SetText("+ " + str(self.socketValue) + " Min.")
			elif self.socketType == self.SOCKET_TYPE_VALUE:
				self.textLine.SetText(str(self.socketValue))
				
				
		def SetSocketType(self,type):
			self.socketType = int(type)
			self.UpdateTextLine()
		
		def SetSocketValue(self,value):
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(value))
			self.socketValue = int(value)
			self.UpdateTextLine()
			
		def SetSocketValue2(self,value):
			self.socketValue2 = int(value)			
		
		def SetSocketNumber(self,slot):
			self.socketNumber = int(slot)
			self.background.SetOnClickEvent(self.OnClick,slot)
		
		def OnClick(self,slot):
			self.wndItemMaker.ShowSocketTypeSelectBoard(slot)
		
	class ItemMakerAttributeItem(ui.ScriptWindow):

		def __init__(self, wndItemMaker):
			ui.ScriptWindow.__init__(self)
			self.wndItemMaker = wndItemMaker
			self.attrNumber = 0
			self.attrIndex = 0
			self.attrValue = 0
			self.LoadWindow()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def LoadWindow(self):
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "exscript/itemmaker_attritem.py")
			except:
				import exception
				exception.Abort("ItemMakerSocketItem.LoadWindow.LoadObject")
			
			self.background = self.GetChild("board")
			self.attrBackground = self.GetChild("attrValueBoard")
			self.attrIndexTextLine = self.GetChild("attrIndexTextLine")
			self.attrValueTextLine = self.GetChild("attrValueTextLine")
			
			self.mouseReflector = MouseReflector(self.background)
			self.mouseReflector.SetSize(350 - 30 + 20 - 20 - 60, 20)
			self.mouseReflector.UpdateRect()			
			
			self.mouseReflector1 = MouseReflector(self.attrBackground)
			self.mouseReflector1.SetSize(60, 20)
			self.mouseReflector1.UpdateRect()	
		
		
		def SetAttributeIndex(self,name,index):
			self.attrIndexTextLine.SetText(name)
			self.attrIndex = int(index)
			
		def SetAttributeValue(self,value):
			self.attrValueTextLine.SetText(str(value))
			self.attrValue = int(value)			
		
		def SetAttributeNumber(self,slot):
			self.attrNumber = int(slot)
			self.background.SetOnClickEvent(self.OnClick,slot)
			self.attrBackground.SetOnClickEvent(self.OnClick2,slot)
		
		def OnClick(self,slot):
			self.wndItemMaker.ShowAttributeSelectBoard(slot)

		def OnClick2(self,slot):
			self.wndItemMaker.ShowAttributeValueChangeBoard(slot)
			
		def OnUpdate(self):
			if self.background.IsIn():
				self.mouseReflector.Show()
			else:
				self.mouseReflector.Hide()
				
			if self.attrBackground.IsIn():
				self.mouseReflector1.Show()
			else:
				self.mouseReflector1.Hide()				
				
	
	SOCKET_TYPE_NONE = 0
	SOCKET_TYPE_STONE = 1
	SOCKET_TYPE_TIME = 2
	SOCKET_TYPE_VALUE = 3
	
	STONE_LIST = [28030,28430,28431,28432,28433,28434,28435,28436,28437,28438,28439,28440,28441,28442,28443]
		
	def __init__(self,systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.socketItemList = {}
		self.attrItemList = {}
		self.is67attrList = False
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/itemmaker.py")
		except:
			import exception
			exception.Abort("SystemPanelWindow.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.background = self.GetChild("itemMakerBackground")
		
		self.vnumInputEditLine = self.GetChild("vnumInputEditLine")
		self.ItemNameTextLine = self.GetChild("itemVnumInfoTextLine")
		self.socketTypeSelectBoard = self.GetChild("socketTypeSelectBoard")
		self.socketTypeSelectBoard.Hide()
		
		self.socketTypeSelectButtonStone = self.GetChild("socket_ghostStoneButton")
		self.socketTypeSelectButtonTime = self.GetChild("socket_timeButton")
		self.socketTypeSelectButtonValue = self.GetChild("socket_valueButton")
		self.socketTypeSelectButtonClose = self.GetChild("socket_closeButton")
		
		self.socketTypeSelectButtonStone.SetEvent(self.SetSocketType,self.SOCKET_TYPE_STONE)
		self.socketTypeSelectButtonTime.SetEvent(self.SetSocketType,self.SOCKET_TYPE_TIME)
		self.socketTypeSelectButtonValue.SetEvent(self.SetSocketType,self.SOCKET_TYPE_VALUE)
		self.socketTypeSelectButtonClose.SetEvent(self.CloseSocketTypeSelectBoard)
		
		self.stoneVnumSelectBoard = self.GetChild("socketVnumSelectBoard")
		self.stoneVnumCloseButton = self.GetChild("socket_vnumCloseButton")
		self.stoneVnumAddButton = self.GetChild("socket_AddButton")
		self.stoneVnumCloseButton.SetEvent(self.CloseStoneVnumSelectBoard)
		self.stoneVnumAddButton.SetEvent(self.AddStoneToSocket)
		
		self.stoneVnumSelectBoard.Hide()
		self.stoneListBox = self.GetChild("stoneListBox")
		self.stoneListBoxScrollBar = self.GetChild("stoneListBoxScrollBar")
		self.stoneListBoxScrollBar.SetScrollEvent(ui.__mem_func__(self.OnStoneListScroll))
		self.InitStoneListBox()

		self.socketTimeBoard = self.GetChild("socketTimeBoard")
		self.socketTimeBoard.Hide()
		self.socketTimeEditLine = self.GetChild("socketTimeEditLine")
		self.socketTimeAddButton = self.GetChild("socket_addTimeButton")
		self.socketTimeCloseButton = self.GetChild("socket_closeTimeButton")

		self.socketTimeAddButton.SetEvent(self.AddTimeToSocket)
		self.socketTimeCloseButton.SetEvent(self.CloseSocketTimeBoard)

		self.socketValueBoard = self.GetChild("socketValueBoard")
		self.socketValueBoard.Hide()
		self.socketValueEditLine = self.GetChild("socketValueEditLine")
		self.socketValueAddButton = self.GetChild("socket_addValueButton")
		self.socketValueCloseButton = self.GetChild("socket_closeValueButton")

		self.socketValueAddButton.SetEvent(self.AddValueToSocket)
		self.socketValueCloseButton.SetEvent(self.CloseSocketValueBoard)
		
		self.attrBoard = self.GetChild("attributeSelectBoard")
		self.attrBoard.Hide()
		self.attrListBox = self.GetChild("attrListBox")
		
		self.attrListBoxBackground = self.GetChild("attrListBoxBackground")
		self.attrListBoxScrollBar = self.GetChild("attrListBoxScrollBar")
		self.attrListBoxScrollBar.SetScrollEvent(ui.__mem_func__(self.OnAttrListScroll))
		self.InitAttrListBox()
		
		self.attrAddButton = self.GetChild("attr_AddButton")
		self.attrCloseButton = self.GetChild("attr_CloseButton")
		
		self.attrAddButton.SetEvent(self.AddAttr)
		self.attrCloseButton.SetEvent(self.CloseAttrBoard)
		
		self.specialAttrListBoxBackground = self.GetChild("specialAttrListBoxBackground")
		self.specialAttrListBox = self.GetChild("specialAttrListBox")
		self.specialAttrListBoxScrollBar = self.GetChild("specialAttrListBoxScrollBar")
		self.specialAttrListBoxScrollBar.SetScrollEvent(ui.__mem_func__(self.OnSpecialAttrListScroll))
		self.InitSpecialAttrListBox()
		self.specialAttrListBoxBackground.Hide()
		
		self.switchTo67Button = self.GetChild("attr_SwitchTo67AttrButton")
		self.backTo15Button = self.GetChild("attr_BackTo15AttrButton")
		
		self.backTo15Button.Hide()

		self.switchTo67Button.SetEvent(self.OnSwitchTo67List)
		self.backTo15Button.SetEvent(self.BackTo15List)
		
		
		self.changeAttrValueBoard = self.GetChild("attrChangeValueBoard")
		self.changeAttrEditLine = self.GetChild("attrChangeEditLine")
		self.changeAttrButton = self.GetChild("attrChange_addValueButton")
		self.changeAttrCloseButton = self.GetChild("attrChange_closeValueButton")
		
		self.changeAttrValueBoard.Hide()
		
		self.changeAttrButton.SetEvent(self.ChangeAttrValue)
		self.changeAttrCloseButton.SetEvent(self.CloseAttributeValueChangeBoard)
		
		self.makeItemButton = self.GetChild("makeItemButton")
		self.makeItemButton.SetEvent(self.MakeItem)
		
		y = 52
		for i in xrange(6):	
			self.socketItemList[i] = self.ItemMakerSocketItem(self)
			self.socketItemList[i].SetParent(self.background)
			self.socketItemList[i].SetPosition(10,y)
			self.socketItemList[i].SetSocketNumber(i)
			self.socketItemList[i].Show()
			y = y + 22


		y = 22 + 4 + 180 -18 + 24
		for i in xrange(7):	
			self.attrItemList[i] = self.ItemMakerAttributeItem(self)
			self.attrItemList[i].SetParent(self.background)
			self.attrItemList[i].SetPosition(10,y)
			self.attrItemList[i].SetAttributeNumber(i)
			self.attrItemList[i].Show()
			y = y + 22
	
	def InitStoneListBox(self):
		for i in xrange(len(self.STONE_LIST)):
			item.SelectItem(self.STONE_LIST[i])
			self.stoneListBox.InsertItem(i,item.GetItemName())
			
	def InitAttrListBox(self):
		bonusList = settinginfo.Switchbot_BonusList
		for i in xrange(len(bonusList)):
			self.attrListBox.InsertItem(i,bonusList[i][0][1])

	def InitSpecialAttrListBox(self):
		bonusList = settinginfo.ItemMaker_BonusList67
		for i in xrange(len(bonusList)):
			self.specialAttrListBox.InsertItem(i,bonusList[i][0][1])		

	def OnStoneListScroll(self):
		viewItemCount = self.stoneListBox.GetViewItemCount()
		itemCount = self.stoneListBox.GetItemCount()
		pos = self.stoneListBoxScrollBar.GetPos() * (itemCount - viewItemCount)
		self.stoneListBox.SetBasePos(int(pos))	

	def OnAttrListScroll(self):
		viewItemCount = self.attrListBox.GetViewItemCount()
		itemCount = self.attrListBox.GetItemCount()
		pos = self.attrListBoxScrollBar.GetPos() * (itemCount - viewItemCount)
		self.attrListBox.SetBasePos(int(pos))	

	def OnSpecialAttrListScroll(self):
		viewItemCount = self.specialAttrListBox.GetViewItemCount()
		itemCount = self.specialAttrListBox.GetItemCount()
		pos = self.specialAttrListBoxScrollBar.GetPos() * (itemCount - viewItemCount)
		self.specialAttrListBox.SetBasePos(int(pos))

	def OnSwitchTo67List(self):
		self.attrListBoxBackground.Hide()
		self.specialAttrListBoxBackground.Show()
		self.switchTo67Button.Hide()
		self.backTo15Button.Show()
		self.is67attrList = True

	def BackTo15List(self):
		self.attrListBoxBackground.Show()
		self.specialAttrListBoxBackground.Hide()
		self.switchTo67Button.Show()
		self.backTo15Button.Hide()
		self.is67attrList = False
			
	def ShowSocketTypeSelectBoard(self,slot):
		self.currentSocketSlot = slot
		self.socketTypeSelectBoard.Show()
		
	def ShowAttributeSelectBoard(self,slot):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"ShowAttributeSelectBoard")
		self.currentSocketSlot = slot
		self.attrBoard.Show()
		
	def ShowAttributeValueChangeBoard(self,slot):
		self.currentSocketSlot = slot
		self.changeAttrValueBoard.Show()
		
	def CloseAttributeValueChangeBoard(self):
		self.changeAttrValueBoard.Hide()
		
	def ChangeAttrValue(self):
		self.changeAttrValueBoard.Hide()
		self.attrItemList[self.currentSocketSlot].SetAttributeValue(self.changeAttrEditLine.GetText())
		
	def SetSocketType(self,type):
		self.socketItemList[self.currentSocketSlot].SetSocketType(type)
		
		if type == self.SOCKET_TYPE_STONE:
			self.stoneVnumSelectBoard.Show()
		elif type == self.SOCKET_TYPE_TIME:
			self.socketTimeBoard.Show()
		elif type == self.SOCKET_TYPE_VALUE:
			self.socketValueBoard.Show()
			
		self.CloseSocketTypeSelectBoard()
	
	def CloseStoneVnumSelectBoard(self):
		self.stoneVnumSelectBoard.Hide()
		self.socketItemList[self.currentSocketSlot].SetSocketType(self.SOCKET_TYPE_NONE)
		
	def AddStoneToSocket(self):
		self.stoneVnumSelectBoard.Hide()
		self.socketItemList[self.currentSocketSlot].SetSocketValue(self.STONE_LIST[self.stoneListBox.GetSelectedItem()])
		self.socketItemList[self.currentSocketSlot].SetSocketValue2(self.stoneListBox.GetSelectedItem())
	
		
	def CloseSocketTypeSelectBoard(self):
		self.socketTypeSelectBoard.Hide()
		
	
	def CloseSocketTimeBoard(self):
		self.socketTimeBoard.Hide()
		self.socketItemList[self.currentSocketSlot].SetSocketType(self.SOCKET_TYPE_NONE)
		
	def AddTimeToSocket(self):
		self.socketTimeBoard.Hide()
		self.socketItemList[self.currentSocketSlot].SetSocketValue(int(self.socketTimeEditLine.GetText()))


	def CloseSocketValueBoard(self):
		self.socketValueBoard.Hide()
		self.socketItemList[self.currentSocketSlot].SetSocketType(self.SOCKET_TYPE_NONE)
		
	def AddValueToSocket(self):
		self.socketValueBoard.Hide()
		self.socketItemList[self.currentSocketSlot].SetSocketValue(int(self.socketValueEditLine.GetText()))
	
	
	
	def CloseAttrBoard(self):
		self.attrBoard.Hide()
		
		
	def AddAttr(self):
		self.attrBoard.Hide()
		
		
		if self.is67attrList == False:
			attrListIndex = self.attrListBox.GetSelectedItem()
			bonusList = settinginfo.Switchbot_BonusList
		else:
			attrListIndex = self.specialAttrListBox.GetSelectedItem()
			bonusList = settinginfo.ItemMaker_BonusList67
		self.attrItemList[self.currentSocketSlot].SetAttributeIndex(bonusList[attrListIndex][0][1],bonusList[attrListIndex][0][0])
		valueList = len(bonusList[attrListIndex][2]) - 1
		value = bonusList[attrListIndex][2][valueList]
		self.attrItemList[self.currentSocketSlot].SetAttributeValue(value)
	
	
	def MakeItem(self):
		makeItemString = str(self.vnumInputEditLine.GetText()) + "#"
		
		for i in xrange(6):
			type = self.socketItemList[i].socketType
			if type == self.SOCKET_TYPE_TIME:
				value = (self.socketItemList[i].socketValue*60) + app.GetGlobalTimeStamp()
			elif type == self.SOCKET_TYPE_STONE:
				value = self.socketItemList[i].socketValue2 
			else:
				value = self.socketItemList[i].socketValue
				
				
			makeItemString = makeItemString + str(value) + "#"
	
		for i in xrange(7):
			index = self.attrItemList[i].attrIndex
			value = self.attrItemList[i].attrValue
			merge = str(index) + "#" + str(value)
			
			makeItemString = makeItemString + str(merge) + "#"
		
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,makeItemString)
		constInfo.INPUT_CMD = makeItemString
		event.QuestButtonClick(GM_PANEL_DICT["qid"][self.SYSTEM_INDEX])

	def OnUpdate(self):
		self.CheckForItemName()
		
	def CheckForItemName(self):
		try:
			vnum = int(self.vnumInputEditLine.GetText())
			item.SelectItem(vnum)
			self.ItemNameTextLine.SetText(item.GetItemName())	
		except:
			self.ItemNameTextLine.SetText("No item found...")
			
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
		
	def Destroy(self):
		self.__del__()	

		