import ui
import chat
import app
import GFHhg54GHGhh45GHGH as net
import snd
import item
import fgGHGjjFHJghjfFG1545gGG as player
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo
from uiGuild import MouseReflector
import systemSetting
blockMode = 0

class DungeonIntroWindow(ui.ScriptWindow):

	MAX_DIFF = 5

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.selectDifficulty = 1
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/dungeonintro.py")
		except:
			import exception
			exception.Abort("DungeonIntroWindow.LoadWindow.LoadObject")
		
		self.difficultyToolTip = uiToolTip.ToolTip()
		self.difficultyToolTip.HideToolTip()
		
		self.descListBox = self.GetChild("desc_box")
		self.descScrollBar = self.GetChild("scrollBar")
		self.descScrollBar.Hide()
		
		self.descListBox.InsertDescItem("Brauchte mal ne Pause vom blöden C++,")
		self.descListBox.InsertDescItem("denn der scheiß stinkt!!! Also ne Dungeon")
		self.descListBox.InsertDescItem("EintrittsGUI ka. Mit schwierigkeits")
		self.descListBox.InsertDescItem("auswahl. Es ist 00:43Uhr meine gedanken")
		self.descListBox.InsertDescItem("ergeben irgendwie keinen sinn mehr")
		self.descListBox.InsertDescItem("ich geh besser Pennen. ^^")
		self.descListBox.InsertEmptyItem()
		self.descListBox.InsertDescItem("P.s: Die Schwierigkeitsanzeige hat nen")
		self.descListBox.InsertDescItem("     geilen ToolTip! HaHa. Gute Nacht.")
		self.difficultyNumber = self.GetChild("difficulty_number")
		self.difficultyPlus = self.GetChild("plus_button")
		self.difficultyMinus = self.GetChild("minus_button")
		self.difficultyFrame = self.GetChild("difficulty_frame")
		
		self.difficultyPlus.SetEvent(self.PlusDifficulty)
		self.difficultyMinus.SetEvent(self.MinusDifficulty)
		self.UpdateChangeButtonStatus()
		self.Show()
	
	def OnUpdate(self):
		if self.difficultyFrame.IsIn():
			self.difficultyToolTip.ClearToolTip()
			self.difficultyToolTip.AppendTextLine("Erhöhe die schwierigkeit des Dungeons",self.difficultyToolTip.TITLE_COLOR)
			self.difficultyToolTip.AppendTextLine("für mehr Ruhm und Dungeonpoints!",self.difficultyToolTip.TITLE_COLOR)
			self.difficultyToolTip.AppendSpace(5)
			self.difficultyToolTip.AppendHorizontalLine()
			self.difficultyToolTip.AppendStatisticTextLine("Monster-TP","+" + str(self.selectDifficulty * 10) + "%")
			self.difficultyToolTip.AppendStatisticTextLine("Monsterstärke","+" + str(self.selectDifficulty * 20) + "%")
			self.difficultyToolTip.AppendStatisticTextLine("Max. Tode",str(6 - self.selectDifficulty))
			self.difficultyToolTip.AppendStatisticTextLine("Zeit (Min)",str((6 - self.selectDifficulty) * 10))
			self.difficultyToolTip.AppendStatisticTextLine("Dungeonpoints","+" + str((self.selectDifficulty-1) * 10) + "%")
			# self.difficultyToolTip.AppendSpace(5)
			self.difficultyToolTip.ShowToolTip()
		else:
			self.difficultyToolTip.HideToolTip()
	
	def PlusDifficulty(self):
		self.selectDifficulty = self.selectDifficulty + 1
		self.UpdateChangeButtonStatus()
		
	def MinusDifficulty(self):
		self.selectDifficulty = self.selectDifficulty - 1
		self.UpdateChangeButtonStatus()
		
	def UpdateChangeButtonStatus(self):
		if self.selectDifficulty == self.MAX_DIFF:
			self.difficultyPlus.Disable()
		else:
			self.difficultyPlus.Enable()

		if self.selectDifficulty == 1:
			self.difficultyMinus.Disable()
		else:
			self.difficultyMinus.Enable()
	
		self.difficultyNumber.LoadImage("yamato_dungeon/numbers/" + str(self.selectDifficulty) + ".tga")	
		
	def Destroy(self):
		self.Hide()
			
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
