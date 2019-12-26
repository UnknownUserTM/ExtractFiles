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

class DungeonGuideMiniMapButton(ui.Window):

	def __init__(self):
		ui.Window.__init__(self)
		self.SetSize(27,27)
		self.SetPosition(wndMgr.GetScreenWidth() - 149,58)
		self.dungeonGuideWindow = DungeonGuideWindow()
		self.dungeonGuideWindow.Close()
		
		self.dungeonCoolDownWindow = DungeonCooldownToolTip(self, self.dungeonGuideWindow)
		
		self.MakeButton()
		self.Show()
		
	def __del__(self):
		ui.Window.__del__(self)	

	def MakeButton(self):
		self.button = ui.Button()
		self.button.SetParent(self)
		self.button.SetPosition(0,0)
		self.button.SetUpVisual("yamato_dungeoncompendium/dc_button_n.tga")
		self.button.SetOverVisual("yamato_dungeoncompendium/dc_button_h.tga")
		self.button.SetDownVisual("yamato_dungeoncompendium/dc_button_n.tga")
		# self.button.ShowToolTip = lambda arg=1: self.ShowToolTip(arg)
		# self.button.HideToolTip = lambda arg=1: self.HideToolTip()
		self.button.SetEvent(self.OpenDungeonGuide)
		self.button.Show()
	
	def OpenDungeonGuide(self):
		self.dungeonGuideWindow.Open()
	
	
	# def ShowToolTip(self,arg):
	def OnUpdate(self):
		if self.button.IsIn():
			self.dungeonCoolDownWindow.Open()
		else:
		
	# def HideToolTip(self):
			self.dungeonCoolDownWindow.Close()
	# def HideToolTip(self):
		

class DungeonCooldownToolTip(ui.Window):
	normalWidth = 200
	
	
	dungeonCooldown = [
		app.GetGlobalTimeStamp() + (1*60),
		app.GetGlobalTimeStamp() + (15*60),
		app.GetGlobalTimeStamp() + (3*60),
		app.GetGlobalTimeStamp() + (5*60)
	]
	
	
	
	def __init__(self,dgButton,dgWindow):
		ui.Window.__init__(self)
		self.dgButton = dgButton
		self.SetSize(self.normalWidth,100)
		self.dgWindow = dgWindow
		self.Hide()
		self.MakeToolTip()	
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def AdjustPosition(self):
		x, y = self.dgButton.GetGlobalPosition()
		# self.SetPosition(x - self.normalWidth - 10 + 22,(y + 630)-self.toolTip.toolTipHeight)
		self.SetPosition(wndMgr.GetScreenWidth() - 256 - 75 - 20,75)
		
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetParent(self)
		toolTip.SetPosition(1, 1)
		toolTip.SetFollow(False)
		toolTip.Show()
		self.toolTip = toolTip
	
	def Open(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Open!")
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine("Dungeonkompendium",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendDescription("Hier findest du alle Infos zu den Dungeons, so das du ja nichts selber rausfinden musst!",26)
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
		self.toolTip.AppendTextLine("Abklingzeiten:",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendCooldownTextLine("DungeonName 01 :",0)
		self.toolTip.AppendCooldownTextLine("Dämonenturm :",0)
		self.toolTip.AppendCooldownTextLine("Devils Catacomb :",0)
		self.toolTip.AppendCooldownTextLine("Drachenraum :",self.dungeonCooldown[0])
		self.toolTip.AppendCooldownTextLine("Tal der Keine Ahnung :",self.dungeonCooldown[1])
		self.toolTip.AppendCooldownTextLine("Höhlen der Planlosigkeit :",self.dungeonCooldown[2])
		self.toolTip.AppendCooldownTextLine("WasGibtsNoch-Run :",self.dungeonCooldown[3])
		self.toolTip.AppendCooldownTextLine("Verlies des Roten Drachen :",0)
		self.toolTip.AppendSpace(5)
		self.toolTip.ResizeToolTip()	
		self.AdjustPosition()
		self.Show()
		
	def Close(self):
		self.Hide()
	
class DungeonGuideWindow(ui.ScriptWindow):
	
	TEXT_MIN_LEVEL 			= 0
	TEXT_MAX_LEVEL 			= 1
	TEXT_PARTY				= 2
	TEXT_COOLDOWN			= 3
	TEXT_EFF_BONUS			= 4
	TEXT_DEF_BONUS			= 5
	TEXT_DUNGEONPOINTS		= 6
	TEXT_ITEM				= 7
	TEXT_PERS_COOLDOWN		= 8
	TEXT_PERS_COUNT			= 9
	TEXT_PERS_BESTTIME		= 10
	TEXT_PERS_M_KILLS		= 11
	TEXT_PERS_B_KILLS		= 12
	TEXT_PERS_S_KILLS		= 13
	TEXT_SERVER_COUNT		= 14
	TEXT_SERVER_BESTTIME	= 15

	PARTY_TYPE_SOLO_ONLY = "Nein"
	PARTY_TYPE_PARTY_AND_SOLO = "Nein aber möglich"
	PARTY_TYPE_PARTY_ONLY = "Ja"
	PARTY_TYPE_GUILD_ONLY = "Nur mit Gilde!"
	
	COOLDOWN_READY = "Bereit!"
	
	DUNGEON_01_TUTORIAL = 0
	DUNGEON_30_TEMPLE = 1
	DUNGEON_40_DEVILTOWER = 2
	DUNGEON_70_DEVILCAVE = 3
	DUNGEON_80_DRAGONROOM = 4
	DUNGEON_90_SPIDERCAVE = 5
	DUNGEON_100_RAZADOR = 6
	DUNGEON_100_NEMERE = 7
	DUNGEON_110_SHIPBREAK = 8
	DUNGEON_120_REDDRAGON = 9
	
	DATA = [
		{
			"dungeon_name"	: "Verlies des Roten Drachen",
			"dungeon_desc"	: "dungeon_01.txt",
			
			# REQs
			"min_level"					: 100,
			"max_level"					: 135,
			"party"						: PARTY_TYPE_SOLO_ONLY,
			"cooldown"					: 30,
			"eff_bonus" 				: "Stark gegen Schwachköpfe",
			"def_bonus" 				: "Abwehr gegen Schwachköpfe",
			"dungeonpoints"				: 50,
			"dungeonpoints_local_event"	: 0,
			"item" : [],

			# PERS_STAT
			"pers_cooldown" 	: 0,
			"pers_count" 		: 0,
			"pers_besttime" 	: 0,
			"pers_m_kills" 		: 0,
			"pers_b_kills" 		: 0,
			"pers_s_kills" 		: 0,

			# SERVER_STAT
			"server_count" 		: 0,
			"server_besttime" 	: [0,"NoName"],
		},
	
	
	
	]
	
	EVENT_GLOBAL_DUNGEONPOINTS = 0

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/dungeoncompendium.py")
		except:
			import exception
			exception.Abort("DungeonIntroWindow.LoadWindow.LoadObject")
		
		
		
		self.selectBoard = self.GetChild("selectBackground")
		self.infoBoard = self.GetChild("infoBackground")
		
		
		# self.dungeonButton = []
		self.dungeonButton = self.GetChild("dungeon_0")
		self.dungeonButton.SetEvent(self.ShowInfoBoard)
		self.descListBox = self.GetChild("dungeonDescBox")
		self.descScrollBar = self.GetChild("descScrollBar")
		self.descScrollBar.SetScrollEvent(self.__OnScrollDesc)
		self.infoBoard.Hide()
		
		
		self.backButton = self.GetChild("backButton")
		self.forwardButton = self.GetChild("forwardButton")
		self.forwardButton.Disable()
		self.backButton.SetEvent(self.ShowSelectBoard)
		
		self.LoadDungeonDesc()
		# self.Show()

	def ShowSelectBoard(self):
		self.infoBoard.Hide()
		self.selectBoard.Show()
		
	def ShowInfoBoard(self):
		self.selectBoard.Hide()
		self.infoBoard.Show()
	
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.descScrollBar.OnUp()
		else:
			self.descScrollBar.OnDown()
		
	def __OnScrollDesc(self):
		viewItemCount = self.descListBox.GetViewItemCount()
		itemCount = self.descListBox.GetItemCount()
		pos = self.descScrollBar.GetPos() * (itemCount - viewItemCount)
		self.descListBox.SetBasePos(int(pos))
		
	def LoadDungeonDesc(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,app.GetLocalePath())
		try:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,app.GetLocalePath() + "/textfile/dungeon_01.txt")
			lines = pack_open(app.GetLocalePath() + "/textfile/dungeon_01.txt", "r").readlines()
		except IOError:
			import dbg
			dbg.LogBox("LoadDungeonDESCError")
			app.Abort()
		
		i = 0
		for line in lines:
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				if tokens[0] == "TITLE":
					self.descListBox.InsertItem(i,tokens[1],True)
				else:
					self.descListBox.InsertItem(i,tokens[1],False)
			else:
				self.descListBox.InsertItem(i,"",False)
			i = i + 1

		
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
		# self.Show()
	
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


# DungeonGuideMiniMapButton()
