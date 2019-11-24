import ui
import app
import wndMgr 
import grp
import localeInfo
import mouseModule
import chat
import constInfo
import event

class TutorialJoinWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.qid = 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/tutorial_join.py")
		except:
			import exception
			exception.Abort("TutorialJoinWindow.LoadWindow.LoadObject")
		
		self.button = self.GetChild("enterButton")
		self.button.SetEvent(self.OnEnterTutorial)
		
		# self.Show()
	
	def Open(self,qid):
		self.qid = int(qid)
		self.Show()
	
	def OnEnterTutorial(self):
		self.Hide()
		chat.AppendChat(chat.CHAT_TYPE_INFO,"Du wirst zum Tutorial teleportiert.")
		constInfo.INPUT_CMD = "join/"
		event.QuestButtonClick(self.qid)

	def Close(self):
		self.Hide()


class TutorialWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/tutorialwindow.py")
		except:
			import exception
			exception.Abort("TutorialWindow.LoadWindow.LoadObject")
		
		self.rulesListBox = self.GetChild("rulesListBox")
		self.scrollBar = self.GetChild("scrollBar")
		self.scrollBar.SetScrollEvent(self.__OnScrollRules)
		self.acceptButton = self.GetChild("acceptButton")
		self.declineButton = self.GetChild("declineButton")
		self.acceptButton.Hide()
		self.declineButton.Hide()
		self.LoadGameRules()
		# self.Show()
		
	def LoadGameRules(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,app.GetLocalePath())
		try:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,app.GetLocalePath() + "/textfile/rules.txt")
			lines = pack_open(app.GetLocalePath() + "/textfile/rules.txt", "r").readlines()
		except IOError:
			import dbg
			dbg.LogBox("LoadRulesError")
			app.Abort()
		
		i = 0
		for line in lines:
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				if tokens[0] == "TITLE":
					self.rulesListBox.InsertItem(i,tokens[1],True)
				else:
					self.rulesListBox.InsertItem(i,tokens[1],False)
			else:
				self.rulesListBox.InsertItem(i,"",False)
			i = i + 1

	def __OnScrollRules(self):
		viewItemCount = self.rulesListBox.GetViewItemCount()
		itemCount = self.rulesListBox.GetItemCount()
		pos = self.scrollBar.GetPos() * (itemCount - viewItemCount)
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"pos: " + str(self.scrollBar.GetPos()))
		self.rulesListBox.SetBasePos(int(pos))
		
		if self.scrollBar.GetPos() == 1.0:
			self.acceptButton.Show()
			self.declineButton.Show()
			self.acceptButton.Flash()
		else:
			self.acceptButton.Hide()
			self.declineButton.Hide()
		
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.scrollBar.OnUp()
		else:
			self.scrollBar.OnDown()
			
	def Close(self):
		self.Hide()
