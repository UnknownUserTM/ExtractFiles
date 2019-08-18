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


class DungeonBoard(ui.ScriptWindow):
	NavButtons 					= {}
	NavButtonsTitles 			= {}
	ContentTextLines 			= {}
	SelectetDungeonDescLines 	= {}
	BossItemSlots				= {}
	
	cat 						= 0
	gui							= 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.gui = 0
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
	
	def Destroy(self):
		self.__del__()
	
	# 0 Nicht geladen
	# 1 Geschlossen
	# 2 Offen
	
	def CloseX(self):
		self.gui = 1
		self.Board.Hide()		
	
	def LoadUI(self):
		if self.gui == 1:
			self.gui = 2
			self.Board.Show()
			self.LoadCategory(0)
		elif self.gui == 2:
			self.gui = 1
			self.Board.Hide()
		else:
			self.gui = 1
			self.Board = ui.BoardWithTitleBar()
			self.Board.SetSize(700, 505)
			self.Board.SetCenterPosition()
			self.Board.AddFlag("movable")
			self.Board.AddFlag("float")
			self.Board.SetTitleName("Dungeonkompendium ~ Bruthöhle")
			self.Board.SetCloseEvent(self.CloseX)
			self.Board.Show()
			self.itemtooltip = uiToolTip.ItemToolTip()  
			self.itemtooltip.HideToolTip()	
			self.NavBoard = ui.ThinBoard()
			self.NavBoard.SetParent(self.Board)
			self.NavBoard.SetPosition(15,35)
			self.NavBoard.SetSize(200,455)
			self.NavBoard.Show()
			
			self.NavBG = ui.ImageBox()
			self.NavBG.SetParent(self.Board)
			self.NavBG.SetPosition(220,35)
			self.NavBG.LoadImage("images_dungeon/dungeonkompendium_header/dungeon_bluedead.tga")
			self.NavBG.Show()			
			
			self.HeaderBGThinBoard = ui.ThinBoard()
			self.HeaderBGThinBoard.SetParent(self.Board)
			self.HeaderBGThinBoard.SetPosition(220,35)
			self.HeaderBGThinBoard.SetSize(465,70)
			self.HeaderBGThinBoard.Show()	
			
			self.ReqThinBoard = ui.ThinBoard()
			self.ReqThinBoard.SetParent(self.Board)
			self.ReqThinBoard.SetPosition(220,110)
			self.ReqThinBoard.SetSize(465,50)
			self.ReqThinBoard.Show()
			
			self.MinLevelTextLineTitle = ui.TextLine()
			self.MinLevelTextLineTitle.SetParent(self.ReqThinBoard)
			self.MinLevelTextLineTitle.SetPosition(12,8)
			self.MinLevelTextLineTitle.SetText("Ab Level: ")
			self.MinLevelTextLineTitle.Show()
			
			self.MinLevelTextLine = ui.TextLine()
			self.MinLevelTextLine.SetParent(self.ReqThinBoard)
			self.MinLevelTextLine.SetPosition(80,8)
			self.MinLevelTextLine.SetText("125")
			self.MinLevelTextLine.Show()
			
			self.ItemTextLineTitle = ui.TextLine()
			self.ItemTextLineTitle.SetParent(self.ReqThinBoard)
			self.ItemTextLineTitle.SetPosition(12,25)
			self.ItemTextLineTitle.SetText("Gegenstand: ")
			self.ItemTextLineTitle.Show()		
			
			self.ItemTextLine = ui.TextLine()
			self.ItemTextLine.SetParent(self.ReqThinBoard)
			self.ItemTextLine.SetPosition(80,25)
			self.ItemTextLine.SetText("Arachnidenschlüssel")
			self.ItemTextLine.Show()	
			
			self.GroupTextLineTitle = ui.TextLine()
			self.GroupTextLineTitle.SetParent(self.ReqThinBoard)
			self.GroupTextLineTitle.SetPosition(200,8)
			self.GroupTextLineTitle.SetText("Gruppe benötigt: ")
			self.GroupTextLineTitle.Show()
			
			self.GroupTextLine = ui.TextLine()
			self.GroupTextLine.SetParent(self.ReqThinBoard)
			self.GroupTextLine.SetPosition(290,8)
			self.GroupTextLine.SetText("Nein")
			self.GroupTextLine.Show()
			
			self.TimeTextLineTitle = ui.TextLine()
			self.TimeTextLineTitle.SetParent(self.ReqThinBoard)
			self.TimeTextLineTitle.SetPosition(200,25)
			self.TimeTextLineTitle.SetText("Wartezeit: ")
			self.TimeTextLineTitle.Show()
			
			self.TimeTextLine = ui.TextLine()
			self.TimeTextLine.SetParent(self.ReqThinBoard)
			self.TimeTextLine.SetPosition(290,25)
			self.TimeTextLine.SetText("00:00:00 Sek.")
			self.TimeTextLine.Show()	
					
			self.ContentThinBoard = ui.ThinBoard()
			self.ContentThinBoard.SetParent(self.Board)
			self.ContentThinBoard.SetPosition(220,165)
			self.ContentThinBoard.SetSize(465,270)
			self.ContentThinBoard.Show()

			i = 0
			x = 8
			# max. 88 
			while i < 17:
				self.ContentTextLines[i] = ui.TextLine()
				self.ContentTextLines[i].SetParent(self.ContentThinBoard)
				self.ContentTextLines[i].SetPosition(233,x)
				self.ContentTextLines[i].SetHorizontalAlignCenter()
				self.ContentTextLines[i].SetText("")
				self.ContentTextLines[i].Show()
				x = x + 15
				i = i + 1
				
			self.InfoThinBoard = ui.ThinBoard()
			self.InfoThinBoard.SetParent(self.Board)
			self.InfoThinBoard.SetPosition(220,440)
			self.InfoThinBoard.SetSize(465,50)
			self.InfoThinBoard.Show()			

			i = 0
			y = 8
			while i < 14:
				self.BossItemSlots[i] = ui.GridSlotWindow()  
				self.BossItemSlots[i].SetParent(self.InfoThinBoard)  
				self.BossItemSlots[i].ArrangeSlot(i,1,1,32,32,0,0)  
				self.BossItemSlots[i].SetPosition(y, 8)  
				self.BossItemSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
				self.BossItemSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
				self.BossItemSlots[i].SetSelectItemSlotEvent(ui.__mem_func__(self.WarpToDungeon)) 
				self.BossItemSlots[i].Show()
				y = y + 32
				i = i + 1

			i = 0
			x = 8
			while i < len(settinginfo.DungeonMainSettings):
				self.NavButtons[i] = ui.Button()
				self.NavButtons[i].SetParent(self.NavBoard)
				self.NavButtons[i].SetPosition(10,x)
				self.NavButtons[i].SetText("")
				self.NavButtons[i].SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")  
				self.NavButtons[i].SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")  
				self.NavButtons[i].SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")	
				self.NavButtons[i].SetEvent(ui.__mem_func__(self.LoadCategory), i)
				self.NavButtons[i].Show()
				
				self.NavButtonsTitles[i] = ui.TextLine()
				self.NavButtonsTitles[i].SetParent(self.NavBoard)
				self.NavButtonsTitles[i].SetPosition(100,x+6)
				self.NavButtonsTitles[i].SetText(settinginfo.DungeonMainSettings[i][0][0])
				self.NavButtonsTitles[i].SetHorizontalAlignCenter()
				self.NavButtonsTitles[i].Show()
				i = i + 1
				x = x + 30		
			
			self.LoadCategory(0)
			self.Board.Hide()
			
	def WarpToDungeon(self,slot):
		DungeonSettings = settinginfo.DungeonMainSettings[self.cat]
		constInfo.INPUT_CMD = "WARP#2#" + str(DungeonSettings[4][1]) + "#"
		event.QuestButtonClick(constInfo.warpgui_qid)		
		
		
	def LoadCategory(self,catIndex):
		self.ResetUI()
		DungeonSettings = settinginfo.DungeonMainSettings[catIndex]
		
		self.Board.SetTitleName("Dungeonkompendium ~ " + str(DungeonSettings[0][0]))
		self.NavBG.LoadImage("images_dungeon/dungeonkompendium_header/" + str(DungeonSettings[1][3]))
		
		
		self.MinLevelTextLine.SetText(str(DungeonSettings[1][0]))
		self.ItemTextLine.SetText(str(DungeonSettings[1][1]))
		self.GroupTextLine.SetText(str(DungeonSettings[1][2]))
		
		if DungeonSettings[4][0]:
			if DungeonSettings[1][0] <= fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL):
				self.BossItemSlots[13].SetItemSlot(13, 91105, 0)
			else:
				self.BossItemSlots[13].SetItemSlot(13, 91105, DungeonSettings[1][0])
		
		# ---------------------------------------------------------------------------
		i = 0
		x = 8
		dungeonDescTextLines = settinginfo.DungeonMainSettings[catIndex][2]
		while i < len(dungeonDescTextLines):
			if dungeonDescTextLines[i][0] == "title":
				self.ContentTextLines[i].SetText("[ " + str(dungeonDescTextLines[i][1]) + " ]")
				self.ContentTextLines[i].SetFontColor(1.0, 0.7843, 0.0)		
				self.ContentTextLines[i].SetPosition(233,x)
				x = x + 20
			elif dungeonDescTextLines[i][0] == "normal":
				self.ContentTextLines[i].SetText(str(dungeonDescTextLines[i][1]))
				self.ContentTextLines[i].SetFontColor(0.7607, 0.7607, 0.7607)
				self.ContentTextLines[i].SetPosition(233,x)
				x = x + 15
			elif dungeonDescTextLines[i][0] == "warning":
				self.ContentTextLines[i].SetText("[Warnung] " + str(dungeonDescTextLines[i][1]))
				self.ContentTextLines[i].SetFontColor(0.9, 0.4745, 0.4627)
				x = x + 5
				self.ContentTextLines[i].SetPosition(233,x)
				x = x + 20
			elif dungeonDescTextLines[i][0] == "attention":
				self.ContentTextLines[i].SetText("[Hinweis] " + str(dungeonDescTextLines[i][1]))
				self.ContentTextLines[i].SetFontColor(0.9607, 0.2392, 0.0)
				self.ContentTextLines[i].SetPosition(233,x)				
				x = x + 5
				self.ContentTextLines[i].SetPosition(233,x)
				x = x + 20
			elif dungeonDescTextLines[i][0] == "break":
				x = x + dungeonDescTextLines[i][1]
			i = i + 1
		# ---------------------------------------------------------------------------
		i = 0 
		dungeonBossSlotInfos = settinginfo.DungeonMainSettings[catIndex][3]
		while i < len(dungeonBossSlotInfos):
			self.BossItemSlots[i].SetItemSlot(i, dungeonBossSlotInfos[i], 0)
			i = i + 1
		# ---------------------------------------------------------------------------
		self.cat = catIndex
		# ---------------------------------------------------------------------------
	def ShowToolTip(self,slot):
		if slot == 13:
			return
		self.itemtooltip.ClearToolTip()
		self.itemtooltip.AddItemData(settinginfo.DungeonMainSettings[self.cat][3][slot], [50000, 0, 0])
		self.itemtooltip.ShowToolTip()
		
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()
		
	def ResetUI(self):
		i = 0
		x = 8
		while i < 17:
			self.ContentTextLines[i].SetText("")
			self.ContentTextLines[i].SetFontColor(0.7607, 0.7607, 0.7607)
			self.ContentTextLines[i].SetPosition(233,x)	
			x = x + 15
			i = i + 1

		i = 0
		while i < 14:
			self.BossItemSlots[i].SetItemSlot(i, 0, 0)
			i = i + 1		
			
#WODDungeonBoard().Show()