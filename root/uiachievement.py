import ui
import chat
import app
import fgGHGjjFHJghjfFG1545gGG as player
import snd
import item
import GFHhg54GHGhh45GHGH as net
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import uiCommon
import localeInfo
import systemSetting

TYPE_ACHIEVEMENT = 0
TYPE_DUNGEON = 1

STATUS_READY = 0
STATUS_BUSY = 1

MAX_ACHIEVEMENT_WINDOWS = 5

class AchievementController(ui.Window):

	def __init__(self):
		ui.Window.__init__(self)
		self.SetPosition((wndMgr.GetScreenWidth() / 2),wndMgr.GetScreenHeight() + 50)
		self.AchievementWindowList = {}
		self.AchievementWaitList = []
		
		for i in xrange(MAX_ACHIEVEMENT_WINDOWS):
			index = i + 1
			height = wndMgr.GetScreenHeight() - (50 + (index * 100))
			self.AchievementWindowList[i] = AchievementWindow(self,index)
			self.AchievementWindowList[i].SetPosition(25,wndMgr.GetScreenHeight()+200)
			self.AchievementWindowList[i].Init(height)
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"height: " + str(height))
			self.AchievementWindowList[i].Show()
	
	def __del__(self):
		ui.Window.__del__(self)
	
	def Destroy(self):
		self.AchievementWindowList = {}
		self.AchievementWaitList = []
	
	def AppendAchievement(self,index,points,count,ap):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Open Achievement!")
	
	# Checkt auf freie AchievementWindows.
	def IsAchievementBusy(self):
		return
	
	# Setzt die Achievements auf die Warteliste wenn alle Windows BUSY sind.
	def MoveAchievementToWaitList(self,info):
		return

	
	# Wird ausgelöst wenn AchievementWindow fertig ist.
	def AchievementDone(self,index):
		return
		
		

class AchievementWindow(ui.ScriptWindow):

	def __init__(self, achievementCTRL, index):
		ui.ScriptWindow.__init__(self)
		self.achievementCTRL = achievementCTRL
		self.achievementIndex = index
		self.targetHeight = 0
		self.initTime = 0
		self.achievementTimer = 8
		self.currentHeight = wndMgr.GetScreenHeight() + 200
		self.baseHeight = wndMgr.GetScreenHeight() + 200
		# self.SetPosition((wndMgr.GetScreenWidth() / 2) - 141,wndMgr.GetScreenHeight() - self.achievementWindowHeight)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/achievement.py")
		except:
			import exception
			exception.Abort("Achievement.LoadWindow.LoadObject")

		
	def Init(self,targetHeight):
		self.targetHeight = targetHeight
		self.initTime = app.GetTime() + self.achievementTimer
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"targetHeight: " + str(targetHeight))
		
	def OnUpdate(self):
		if self.initTime > app.GetTime():
			if self.targetHeight < self.currentHeight:
				self.currentHeight = self.currentHeight - 20
				self.SetPosition(25,self.currentHeight)
		
		else:
			if self.currentHeight < self.baseHeight:
				self.currentHeight = self.currentHeight + 20
				self.SetPosition(25,self.currentHeight)			
		
		
		
		