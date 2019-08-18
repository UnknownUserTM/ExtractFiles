import ui
import chat
import app
import GFHhg54GHGhh45GHGH
import snd
import item
import fgGHGjjFHJghjfFG1545gGG
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo
import nonplayer



class UserEventButtonWindow(ui.ScriptWindow):
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/usereventbutton.py")
		except:
			import exception
			exception.Abort("UserEventButton.LoadWindow.LoadObject")
		
		self.eventGuide = EventGuide()
		self.eventGuide.Close()
		
		self.eventButton = self.GetChild("event_button")
		self.eventButton.SetEvent(self.OpenEventGuide)
		self.Open()

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
	
	def Destroy(self):
		self.eventGuide.Destroy()
		self.eventGuide = None
		
		self.__del__()
		
	def Close(self):
		self.Hide()

	def OpenEventGuide(self):
		self.eventGuide.Open()
		
		
class EventGuide(ui.ScriptWindow):
	
	refreshTimer = app.GetTime() + 30
	
	EVENT_TEMP_DROP = 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/eventguide.py")
		except:
			import exception
			exception.Abort("EventGuideWindow.LoadWindow.LoadObject")
		
		
		
		self.close_button = self.GetChild("close_button")
		self.close_button.SetEvent(self.Close)
		
		self.eventButtons = []
		for i in xrange(2):
			self.eventButtons.append(self.GetChild("event_button_" + str(i)))

		self.eventButtons[self.EVENT_TEMP_DROP].SetEvent(self.LoadTempDropGuide)
		self.eventButtons[self.EVENT_TEMP_DROP].Disable()
		
		self.tempDropEventGuide = EventTempDropGuide(self)
		# self.Open()
		
	def Destroy(self):
		self.tempDropEventGuide.Destroy()
		self.__del__()
		
		
	def ActivateButton(self,button):
		self.eventButtons[button].SetUpVisual("yamato_button/wide_button_a_n.tga")
		self.eventButtons[button].SetOverVisual("yamato_button/wide_button_a_h.tga")
		self.eventButtons[button].SetDownVisual("yamato_button/wide_button_a_p.tga")
	
	def DeactivateButton(self,button):
		self.eventButtons[button].SetUpVisual("yamato_helpboard/wide_button_n.tga")
		self.eventButtons[button].SetOverVisual("yamato_helpboard/wide_button_h.tga")
		self.eventButtons[button].SetDownVisual("yamato_helpboard/wide_button_p.tga")	
		
	# def AddTempDropEventCount(self,count):
		# return
		
		
	def AppendTeampDropEventInformation(self,eventName,itemVnum,target,dropType,timeStamp):
		
		chat.AppendChat(chat.CHAT_TYPE_INFO, "AppendTeampDropEventInformation: " + str(eventName) + ", " + str(itemVnum) + ", " + str(target) + ", " + str(dropType) +", " + str(timeStamp))
		
		self.tempDropEventGuide.AppendEventInformation(eventName,itemVnum,target,dropType,timeStamp)
		
		
	def DisableOXEventButton(self):
		self.eventButtons[1].Disable()
	
	def EnableOXEventButton(self):
		self.eventButtons[1].Enable()

	def LoadTempDropGuide(self):
		self.tempDropEventGuide.Open()

	def LoadEventDialog(self,idx):
		return
	
	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
		
		
	def Close(self):
		self.Hide()

class EventTempDropGuide(ui.ScriptWindow):
	
	eventListBox = {}
	eventCount = 0
	
	baseHeight = 10
	
	def __init__(self,eventGuide):
		ui.ScriptWindow.__init__(self)
		self.eventGuide = eventGuide
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/tempdropeventguide.py")
		except:
			import exception
			exception.Abort("TempDropEventGuide.LoadWindow.LoadObject")
			
			
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.board = self.GetChild("board")
		self.errorLine = self.GetChild("errorTextLine")
		self.errorLine.Show()
		
		# Test!
		# self.AppendEventInformation(27001,101,0,app.GetGlobalTimeStamp() + 60)
		# self.AppendEventInformation(27002,1,1,app.GetGlobalTimeStamp() + 8600)
		# self.AppendEventInformation(27003,360,2,app.GetGlobalTimeStamp() + 8600)
		# self.AppendEventInformation(27005,0,3,app.GetGlobalTimeStamp() + (30 * 60))

		
	def AppendEventInformation(self,eventName,itemVnum,target,targetType,runTime):
		if self.eventCount > 0:
			for i in xrange(self.eventCount):
				if eventName == self.eventListBox[i+1].eventName:
					return
		
		chat.AppendChat(chat.CHAT_TYPE_INFO, "AppendEventInformation: " + str(itemVnum) + ", " + str(target) + ", " + str(targetType) +", " + str(runTime))
		
		self.eventCount = self.eventCount + 1
		self.errorLine.Hide()
				
		self.eventGuide.eventButtons[self.eventGuide.EVENT_TEMP_DROP].SetText("Drop-Event (" + str(self.eventCount) + ")")
		self.eventGuide.eventButtons[self.eventGuide.EVENT_TEMP_DROP].Enable()
		
		self.eventListBox[self.eventCount] = EventTempDropGuideItemBox()
		self.eventListBox[self.eventCount].SetParent(self.board)
		self.eventListBox[self.eventCount].SetPosition(25,35 + (45 * self.eventCount) - 45)
		self.eventListBox[self.eventCount].SetData(eventName,itemVnum,target,targetType,runTime)		
		self.eventListBox[self.eventCount].Show()		
		
		self.SetWindowSize(400,self.baseHeight + (self.eventCount * 45) + 10)
		
	def SetWindowSize(self,x,y):
		self.SetSize(x+30,y+50+30)
		self.board.SetSize(x+30,y+30)


	
	def Destroy(self):
		self.__del__()
		
			
	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
		
		
	def Close(self):
		self.Hide()

class EventTempDropGuideItemBox(ui.ScriptWindow):
	
	itemVnum = 0
	target = 0
	runTime = 0
	dropType = 0
	
	TEMP_DROP_TYPE_SINGLE = 0
	TEMP_DROP_TYPE_MAP	= 1
	TEMP_DROP_TYPE_DUNGEON = 2
	TEMP_DROP_TYPE_ALL = 3
		
	mapNames = {
		1	: localeInfo.WARP_MAP_NAME_A1,
		21	: localeInfo.WARP_MAP_NAME_B1,
		41	: localeInfo.WARP_MAP_NAME_C1,
		
		3	: localeInfo.WARP_MAP_NAME_A3,
		23	: localeInfo.WARP_MAP_NAME_B3,
		43	: localeInfo.WARP_MAP_NAME_C3,
		
		360	: localeInfo.WARP_MAP_NAME_SPIDERD,
		66	: localeInfo.WARP_MAP_NAME_DEVILTOWER,
		208	: localeInfo.WARP_MAP_NAME_DRAGON,
		380	: localeInfo.WARP_MAP_NAME_CATACOMB,
		359	: localeInfo.WARP_MAP_NAME_RUNE,
		
		104	: localeInfo.WARP_MAP_NAME_SD1,
		71	: localeInfo.WARP_MAP_NAME_SD2,
		# 41	: localeInfo.WARP_MAP_NAME_GHOST,
		# 41	: localeInfo.WARP_MAP_NAME_RED,
		# 41	: localeInfo.WARP_MAP_NAME_TEMPLE,
		# 41	: localeInfo.WARP_MAP_NAME_ORC,
		# 41	: localeInfo.WARP_MAP_NAME_SOHAN,
		# 41	: localeInfo.WARP_MAP_NAME_DOYY,
		# 41	: localeInfo.WARP_MAP_NAME_YONGBI,
		
		# 41	: localeInfo.WARP_MAP_NAME_FARM1,
		# 41	: localeInfo.WARP_MAP_NAME_FARM2,
		# 41	: localeInfo.WARP_MAP_NAME_FARM3,
		# 41	: localeInfo.WARP_MAP_NAME_FARM4,
		# 41	: localeInfo.WARP_MAP_NAME_FARM5,
		# 41	: localeInfo.WARP_MAP_NAME_FARM6,
	
		# 41	: localeInfo.WARP_MAP_NAME_LEVELMAP,

	}
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/tempdropeventguideitem.py")
		except:
			import exception
			exception.Abort("TempDropEventGuideItem.LoadWindow.LoadObject")
		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()			
		self.itemSlot = self.GetChild("itemSlot")		
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip)) 	

		self.targetTextLine = self.GetChild("targetTextLine")
		self.runTimeTextLine = self.GetChild("runTimeTextLine")
		
		self.Show()
		
	def SetData(self,eventName,itemVnum,target,dropType,runTime):
	
		self.eventName = eventName
		self.itemVnum = int(itemVnum)
		self.target = int(target)
		self.runTime = int(runTime)
		self.dropType = int(dropType)
		
		self.targetTextLine.SetText(self.GetTarget(target,dropType))
		
		self.itemSlot.SetItemSlot(0, self.itemVnum, 0)
		self.itemSlot.RefreshSlot()		
	
	
	def GetTarget(self,target,dropType):
		if dropType == self.TEMP_DROP_TYPE_SINGLE:
			return nonplayer.GetMonsterName(target)
		
		elif dropType == self.TEMP_DROP_TYPE_MAP or dropType == self.TEMP_DROP_TYPE_DUNGEON:
			try:
				return self.mapNames[target]
			except:
				return "Unknown Map"
		
		elif dropType == self.TEMP_DROP_TYPE_ALL:
			return localeInfo.EVENT_TEMP_DROP_GLOBAL
		
		else:
			return "UNKNOWN DROPTYPE!"
	
	def ShowToolTip(self):
		if self.itemVnum > 0:
			self.itemtooltip.ClearToolTip()
			self.itemtooltip.AddItemData(self.itemVnum, [0, 0, 0, 0, 0, 0])		
			self.itemtooltip.ShowToolTip()	

	def HideToolTip(self):
		self.itemtooltip.HideToolTip()		
		
	def Destroy(self):
		self.__del__()

	def FormatTime(self, time):
		m, s = divmod(time, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%02d" % (h, m, s)
		
	def OnUpdate(self):
		if self.runTime > app.GetGlobalTimeStamp():
			timeLeft = self.runTime - app.GetGlobalTimeStamp()
			self.runTimeTextLine.SetText(self.FormatTime(timeLeft))
		else:
			self.runTimeTextLine.SetText("Abgelaufen!")


















		
