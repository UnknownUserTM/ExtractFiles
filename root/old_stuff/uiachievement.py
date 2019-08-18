import ui
import snd
import systemSetting
import GFHhg54GHGhh45GHGH
import chat
import app
import locale
import chrmgr
import uiWhisper
import interfacemodule
import time
import wndMgr

AchievementPoints = 0

class AchievementDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Load()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Hide()
		return TRUE
		
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("AchievementDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			self.AchievementText = self.GetChild("Achievement_Text")
			self.AchievementTextFiller = self.GetChild("Achievement_Filler")
			self.AchievementCountText = self.GetChild("Count_Achievement_Text")
			self.AchievementCountTextFiller = self.GetChild("Count_Filler")
			self.AchievementPointsText = self.GetChild("Achievement_Points_Text")
			self.AchievementInfoTextPage1 = self.GetChild("Achievement_Info_1")
			self.AchievementInfoTextPage2 = self.GetChild("Achievement_Info_2")
			self.AchievementInfoTextPage3 = self.GetChild("Achievement_Info_3")
		except:
			import exception
			exception.Abort("AchievementDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/achievementboard.py")
		self.__Load_BindObject()
		width = wndMgr.GetScreenWidth()
		height = wndMgr.GetScreenHeight()
	
	def Show(self, wahl, archivement):
		global AchievementPoints
		ui.ScriptWindow.Show(self)
		if wahl == 1:
			self.AchievementSetText(str(archivement))
			self.WarteSchleife = WaitingDialog()
			self.WarteSchleife.Open(3.0)
			self.WarteSchleife.SAFE_SetTimeOverEvent(self.ShowAchievementPoints)
		elif wahl == 2:
			self.AchievementWindow(AchievementPoints)
		
	
	def AchievementSetText(self, archivement):
		global AchievementPoints
		if archivement.find("_") != -1:
			archivement = archivement.replace('_', ' ')
		if archivement.find("%") != -1:
			AchievementSplit = archivement.split("%")
			archivement = AchievementSplit[0]
			AchievementPoints = AchievementSplit[1]
		if archivement.find("#") != -1:
			Splittext = archivement.split("#")
			Achievement = Splittext[0]
			Count = Splittext[1]
			self.AchievementText.SetText(str(Achievement))
			self.AchievementCountText.SetText(str(Count))
		else:
			self.AchievementText.SetText(str(archivement))
			self.AchievementCountTextFiller.SetText("Herzlichen Glückwunsch.")
			self.AchievementCountText.SetText("")
		self.AchievementPointsText.SetText("")
		self.AchievementInfoTextPage1.SetText("")
		self.AchievementInfoTextPage2.SetText("")
		self.AchievementInfoTextPage3.SetText("")
	
	def ShowAchievementPoints(self):
		global AchievementPoints
		self.AchievementTextFiller.SetText("Deine Achievement-Points")
		self.AchievementText.SetText("")
		self.AchievementPointsText.SetText("steigen auf:")
		self.AchievementCountTextFiller.SetText("")
		self.AchievementCountText.SetText(str(AchievementPoints))
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(3.0)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.Information)
		
	def Information(self):
		self.AchievementTextFiller.SetText("")
		self.AchievementText.SetText("")
		self.AchievementPointsText.SetText("")
		self.AchievementCountTextFiller.SetText("")
		self.AchievementCountText.SetText("")
		self.AchievementInfoTextPage1.SetText("Du kannst deine Points")
		self.AchievementInfoTextPage2.SetText("im Achievement-Shop")
		self.AchievementInfoTextPage3.SetText("eintauschen")
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(2.5)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.Close)
		
	def AchievementWindow(self, points):
		self.AchievementTextFiller.SetText("Deine Achievement-Points")
		self.AchievementText.SetText("")
		self.AchievementPointsText.SetText("   betragen:")
		self.AchievementCountTextFiller.SetText("")
		self.AchievementCountText.SetText(str(points))
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(3.0)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.Information)
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Hide()
		return TRUE

class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/WarteSchleife.py")

		except:
			import exception
			exception.Abort("WaitingDialog.LoadDialog.BindObject")

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()		

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
