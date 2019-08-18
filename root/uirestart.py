import dbg
import app
import GFHhg54GHGhh45GHGH

import ui

###################################################################################################
## Restart
class RestartDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/restartdialog.py")
		except Exception, msg:
			import sys
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("RestartDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		try:
			self.restartHereButton=self.GetChild("restart_here_button")
			self.restartTownButton=self.GetChild("restart_town_button")
		except:
			import sys
			(type, msg, tb)=sys.exc_info()
			dbg.TraceError("RestartDialog.LoadDialog - %s:%s" % (type, msg))
			app.Abort()
			return 0

		self.restartHereButton.SetEvent(ui.__mem_func__(self.RestartHere))
		self.restartTownButton.SetEvent(ui.__mem_func__(self.RestartTown))

		return 1

	def Destroy(self):
		self.restartNowTime = 0
		self.townRestartTime = 0
		self.restartHereButton=0
		self.restartTownButton=0
		self.ClearDictionary()

	def OpenDialog(self, time):
		self.restartNowTime = app.GetTime() + time[0]
		self.townRestartTime = app.GetTime() + time[0]
		self.restartHereButton.Disable()
		self.restartTownButton.Disable()
		self.Show()

	def Close(self):
		self.Hide()
		return True
		
	def OnUpdate(self):
		if self.restartNowTime > 0: 
			if self.restartNowTime < app.GetTime():
				self.restartNowTime = 0
				self.restartHereButton.SetText("Hier neu starten")
				self.restartHereButton.Enable()
			else:
				sec = self.restartNowTime - app.GetTime()
				self.restartHereButton.SetText("Hier neu starten in " + str(int(sec)) + " Sek.")
				
		if self.townRestartTime > 0: 
			if self.townRestartTime < app.GetTime():
				self.townRestartTime = 0
				self.restartTownButton.SetText("In der Stadt neu starten")
				self.restartTownButton.Enable()
			else:
				sec = self.townRestartTime - app.GetTime()
				self.restartTownButton.SetText("In der Stadt neu starten in " + str(int(sec)) + " Sek.")				
				
				
	def RestartHere(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/restart_here")

	def RestartTown(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/restart_town")

	def OnPressExitKey(self):
		return True

	def OnPressEscapeKey(self):
		return True
