import app
import ui
import fgGHGjjFHJghjfFG1545gGG
import GFHhg54GHGhh45GHGH

class GameButtonWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow("UIScript/gamewindow.py")

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self, filename):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, filename)
		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return False

		try:
			self.gameButtonDict={
				"STATUS" : self.GetChild("StatusPlusButton"),
				"SKILL" : self.GetChild("SkillPlusButton"),
				"QUEST" : self.GetChild("QuestButton"),
#				"HELP" : self.GetChild("HelpButton"),
				"BUILD" : self.GetChild("BuildGuildBuilding"),
				"EXIT_OBSERVER" : self.GetChild("ExitObserver"),
			}

			self.gameButtonDict["EXIT_OBSERVER"].SetEvent(ui.__mem_func__(self.__OnClickExitObserver))

		except Exception, msg:
			import dbg
			dbg.TraceError("GameButtonWindow.LoadScript - %s" % (msg))
			app.Abort()
			return False

		self.__HideAllGameButton()
		self.SetObserverMode(fgGHGjjFHJghjfFG1545gGG.IsObserverMode())
		return True

	def Destroy(self):
		for key in self.gameButtonDict:
			self.gameButtonDict[key].SetEvent(0)

		self.gameButtonDict={}

	def SetButtonEvent(self, name, event):
		try:
			self.gameButtonDict[name].SetEvent(event)
		except Exception, msg:
			print "GameButtonWindow.LoadScript - %s" % (msg)
			app.Abort()
			return

	def ShowBuildButton(self):
		self.gameButtonDict["BUILD"].Show()

	def HideBuildButton(self):
		self.gameButtonDict["BUILD"].Hide()
	
	def CheckGameButton(self):

		if not self.IsShow():
			return

		statusPlusButton=self.gameButtonDict["STATUS"]
		skillPlusButton=self.gameButtonDict["SKILL"]
#		helpButton=self.gameButtonDict["HELP"]

		if fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.STAT) > 0:
			statusPlusButton.Show()
		else:
			statusPlusButton.Hide()

		if self.__IsSkillStat():
			skillPlusButton.Show()
		else:
			skillPlusButton.Hide()

#		if 0 == fgGHGjjFHJghjfFG1545gGG.GetPlayTime():
#			helpButton.Show()
#		else:
#			helpButton.Hide()


	def HideGameButton(self):

		if not self.IsShow():
			return

		statusPlusButton=self.gameButtonDict["STATUS"]
		skillPlusButton=self.gameButtonDict["SKILL"]
#		helpButton=self.gameButtonDict["HELP"]

		statusPlusButton.Hide()
		skillPlusButton.Hide()
		


			

	def __IsSkillStat(self):
		if fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.SKILL_ACTIVE) > 0:
			return True

		return False

	def __OnClickExitObserver(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/observer_exit")

	def __HideAllGameButton(self):
		for btn in self.gameButtonDict.values():
			btn.Hide()

	def SetObserverMode(self, isEnable):
		if isEnable:
			self.gameButtonDict["EXIT_OBSERVER"].Show()
		else:
			self.gameButtonDict["EXIT_OBSERVER"].Hide()
