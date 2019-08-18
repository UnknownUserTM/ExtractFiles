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
import settinginfo
import localeInfo
import nonplayer


DAILY_STATUS	= 0
DAILY_TIME		= 0

class DailyBoard(ui.ScriptWindow):
	TargetTextLine = {}
	status = 0
	gui = 0
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.gui = 0
		self.LoadUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		
	def Destroy(self):
		self.__del__()
		
	def CloseX(self):
		self.gui = 1
		self.Board.Hide()
		
	def LoadUI(self):
		if self.gui == 1:
			self.gui = 2
			self.Board.Show()
			#self.SetLayoutType(settinginfo.DailyQuest_Status)
			
		elif self.gui == 2:
			self.gui = 1
			self.Board.Hide()
		else:
			self.gui = 1
			self.Board = ui.BoardWithTitleBar()
			self.Board.SetSize(250, 200)
			self.Board.SetCenterPosition()
			self.Board.AddFlag("movable")
			self.Board.AddFlag("float")
			self.Board.SetTitleName("Daily-Quest")
			self.Board.SetCloseEvent(self.CloseX)
			self.Board.Show()
			
			self.InfoThinBoard = ui.ThinBoard()
			self.InfoThinBoard.SetParent(self.Board)
			self.InfoThinBoard.SetPosition(15,35)
			self.InfoThinBoard.SetSize(220,45)
			self.InfoThinBoard.Show()

			
			self.MainTimeLine = ui.TextLine()
			self.MainTimeLine.SetParent(self.InfoThinBoard)
			self.MainTimeLine.SetPosition(110,15)
			self.MainTimeLine.SetHorizontalAlignCenter()
			self.MainTimeLine.SetText("[ Neue Quest in 13:59:57 Std. ]")
			self.MainTimeLine.SetFontColor(0.9, 0.4745, 0.4627)
			self.MainTimeLine.Show()
			
			self.TargetThinBoard = ui.ThinBoard()
			self.TargetThinBoard.SetParent(self.Board)
			self.TargetThinBoard.SetPosition(15,85)
			self.TargetThinBoard.SetSize(220,60)
			self.TargetThinBoard.Show()		
			
			self.TargetTextLine[0] = ui.TextLine()
			self.TargetTextLine[0].SetParent(self.TargetThinBoard)
			self.TargetTextLine[0].SetPosition(110,15)
			self.TargetTextLine[0].SetHorizontalAlignCenter()
			self.TargetTextLine[0].SetText("")
			self.TargetTextLine[0].SetFontColor(0.9, 0.4745, 0.4627)
			self.TargetTextLine[0].Show()		
			
			self.TargetTextLine[1] = ui.TextLine()
			self.TargetTextLine[1].SetParent(self.TargetThinBoard)
			self.TargetTextLine[1].SetPosition(110,30)
			self.TargetTextLine[1].SetHorizontalAlignCenter()
			self.TargetTextLine[1].SetText("")
			self.TargetTextLine[1].SetFontColor(0.9, 0.4745, 0.4627)
			self.TargetTextLine[1].Show()		
			
			self.QuestInitButton = ui.Button()
			self.QuestInitButton.SetParent(self.Board)
			self.QuestInitButton.SetPosition(35,95)
			self.QuestInitButton.SetText("")
			self.QuestInitButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")  
			self.QuestInitButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")  
			self.QuestInitButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")	
			self.QuestInitButton.SetEvent(self.QuestInit)
			self.QuestInitButton.Show()
					
			self.QuestInitButtonText = ui.TextLine()
			self.QuestInitButtonText.SetParent(self.Board)
			self.QuestInitButtonText.SetPosition(125,100)
			self.QuestInitButtonText.SetText("Quest starten")
			self.QuestInitButtonText.SetHorizontalAlignCenter()
			self.QuestInitButtonText.SetFontColor(1.0, 0.7843, 0.0)	
			self.QuestInitButtonText.Show()		
			self.Board.Hide()
			#self.SetLayoutType(1)
		
	def QuestInit(self):
		event.QuestButtonClick(settinginfo.DailyQuest_QID)
		
	def SetRewardAmount(self,dailyPoints):
		if dailyPoints == 0:
			self.Board.SetTitleName("Daily-Quest")
		else:
			self.Board.SetTitleName("Daily-Quest - [ Belohnung: " + str(dailyPoints) + " DPs ]")
		
	def UpdateKillCounter(self,mobIndex,mobVnum,mobCount,mobType):
		mobTypeNames = ["placeholder","besiegen","zerstören"]
		mobIndex = mobIndex - 1
		mobName = nonplayer.GetMonsterName(mobVnum)
		if mobCount == 0:
			self.TargetTextLine[mobIndex].SetFontColor(0.5411, 0.7254, 0.5568)
			self.TargetTextLine[mobIndex].SetText("[ " + mobName + " " + mobTypeNames[mobType] + " ] - [ Fertig ]")

		else:
			self.TargetTextLine[mobIndex].SetFontColor(0.9, 0.4745, 0.4627)	
			self.TargetTextLine[mobIndex].SetText("[ " + mobName + " " + mobTypeNames[mobType] + " ] - [ " + str(mobCount) + " Verbl. ]")
		
	def SetLayoutType(self,dailyStatus):
		if dailyStatus == 1: # Quest aktiv
			self.MainTimeLine.SetText("[ Verbl. Zeit: 13:59:57 Std. ]")
			self.MainTimeLine.SetFontColor(0.5411, 0.7254, 0.5568)	
			self.Board.SetSize(250, 165)
			self.TargetThinBoard.Show()
			self.QuestInitButton.Hide()
			self.QuestInitButtonText.Hide()			
			
		elif dailyStatus == 2: # Quest inaktiv.		<- Nicht bereit
			self.MainTimeLine.SetText("[ Neue Quest in 13:59:57 Std. ]")
			self.MainTimeLine.SetFontColor(0.9, 0.4745, 0.4627)	
			self.Board.SetSize(250, 105)
			self.TargetThinBoard.Hide()
			self.QuestInitButton.Hide()
			self.QuestInitButtonText.Hide()
			self.SetRewardAmount(0)
			
		elif dailyStatus == 3: # Quest inaktiv.		<- Bereit
			self.MainTimeLine.SetText("[ Bereit für neue Quest ]")
			self.MainTimeLine.SetFontColor(0.5411, 0.7254, 0.5568)
			
			self.Board.SetSize(250, 145)
			self.TargetThinBoard.Hide()

			self.QuestInitButton.Show()
			self.QuestInitButtonText.Show()	
			self.SetRewardAmount(0)
		
		self.status = dailyStatus
		
		
	def UpdateDailyTimer(self):
		if self.status == 2:
			if settinginfo.DailyQuest_Time > app.GetGlobalTimeStamp():				
				leftSec = max(0, settinginfo.DailyQuest_Time - app.GetGlobalTimeStamp())
				self.MainTimeLine.SetText("[ Neue Quest in " + localeInfo.SecondToDHM(leftSec) + " ]")
			else:
				event.QuestButtonClick(settinginfo.DailyQuest_QID)
				self.SetLayoutType(3)	
		
		elif self.status == 1:
			if settinginfo.DailyQuest_Time > app.GetGlobalTimeStamp():				
				leftSec = max(0, settinginfo.DailyQuest_Time - app.GetGlobalTimeStamp())
				self.MainTimeLine.SetText("[ Verbl. Zeit: " + localeInfo.SecondToDHM(leftSec) + " ]")
			else:
				event.QuestButtonClick(settinginfo.DailyQuest_QID)
				#chat.AppendChat(chat.CHAT_TYPE_INFO,"Die Zeit für die Daily-Quest ist abgelaufen!")
				self.SetLayoutType(3)			
		
	# def OnUpdate(self):
		# chat.AppendChat(chat.CHAT_TYPE_INFO,"OnUpdate")



	def FormatTime(self, time):
		m, s = divmod(time, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%02d" % (h, m, s)	
		
#DailyBoard().Show()