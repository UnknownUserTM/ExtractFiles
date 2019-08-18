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



class CalenderWindow(ui.ScriptWindow):

	boxSlots = 42
	
	eventInfo = []
	
	# eventNameList = {
		
		# "ox" : [localeInfo.EVENT_NAME_OX,localeInfo.EVENT_DESC_OX],
	
	
	# }
	
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
			
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		self.GetChild("bottom_tutorial_line").SetFontColor(0.9490, 0.9058, 0.7568)
		
		self.toolTip = uiToolTip.ToolTip()
		
		i = 1
		self.eventDayTextLine = []
		while i <= self.boxSlots:
			self.eventDayTextLine.append(self.GetChild("day_slot_0" + str(i) + "_text"))
			i = i + 1
		
		i = 1
		self.eventDayImage = []
		while i <= self.boxSlots:
			self.eventDayImage.append(self.GetChild("day_slot_0" + str(i) + "_img"))
			i = i + 1

		i = 1
		while i <= self.boxSlots:
			self.GetChild("day_slot_0" + str(i) + "_button").SetEvent(lambda arg=i: self.OnClickEventSlot(arg))
			i = i + 1

			
		i = 1
		while i <= self.boxSlots:
			self.GetChild("day_slot_0" + str(i) + "_button").ShowToolTip = lambda arg=i: self.__OverInEventButton(arg)
			self.GetChild("day_slot_0" + str(i) + "_button").HideToolTip = lambda arg=i: self.__OverOutEventButton()
			i = i + 1			
			

			
			
		
		self.SetCalenderStartEndPosition(1,30)	
		
		
		self.AppendEventInfo(18,"test","17:00")
		self.AppendEventInfo(22,"ox","17:00")
		
		# self.Show()
		# self.eventDayImage[12].Show()
	
	
	def __OverInEventButton(self,slot):
		return
		# self.toolTip.ClearToolTip()
		
		# for i in xrange(len(self.eventInfo)):
			# infoSlot = self.eventInfo[i]["slot"]
			
			# if infoSlot == slot:
				# event = self.eventInfo[i]["event"]
				
				
				# eventString = self.eventNameList[event]
				
				# self.toolTip.AppendTextLine(str(eventString[0]))
				# self.toolTip.AppendHorizontalLine()
				# self.toolTip.AppendDescription(str(eventString[1]),26)
		
				# self.toolTip.AppendHorizontalLine()
				# self.toolTip.AppendTextLine(str(self.eventInfo[i]["event_time"]))
				# self.toolTip.AppendHorizontalLine()
				# self.toolTip.ShowToolTip()
				# break
	
	def __OverOutEventButton(self):
		return
		# self.toolTip.HideToolTip()
	
	def OnClickEventSlot(self,idx):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "OnClickEventSlot: " + str(idx))	
		return
	def ResetCalender(self):
		for i in xrange(self.boxSlots):
			self.eventDayTextLine[i].SetText("")
			self.eventDayImage[i].Hide()

	def ResetEventSlotInCalender(self):
		for i in xrange(self.boxSlots):
			self.eventDayImage[i].Hide()
			
	def SetCalenderStartEndPosition(self,start,end):
		self.ResetCalender()
		i = start
		day = 1
		while i <= end:
			self.eventDayTextLine[i-1].SetText(str(day))
			day = day + 1
			
			i = i + 1
	
	def AppendEventInfo(self,slot,event,eventTime):
		event = {
			
			"slot" : int(slot),
			"event" : event,
			"event_time" : eventTime
		
		}
		
		self.eventInfo.append(event)
		self.ResetEventSlotInCalender()
		self.RefreshCalenderEventSlots()
	
	def RefreshCalenderEventSlots(self):
		for i in xrange(len(self.eventInfo)):
			slot = self.eventInfo[i]["slot"]
			event = self.eventInfo[i]["event"]
			
			self.eventDayImage[slot-1].LoadImage("event/" + str(event) + ".tga")
			self.eventDayImage[slot-1].Show()
	
	# # def OnUpdate(self):
		# # showTip = False
		# # for i in xrange(len(self.eventInfo)):
			# # slot = self.eventInfo[i]["slot"]
			# # event = self.eventInfo[i]["event_time"]
			
			# # if self.eventDayImage[slot-1].IsIn():
				# # showTip = 
				# # self.ShowToolTip(event)
				
	
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

