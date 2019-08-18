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

TextIndex = 0

class GuideBoard(ui.ScriptWindow):
	TextLines = {}
	
	PageIndex		= 0
	TextBoxIndex	= 0
	curQuestIndex	= 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		
	def noclose(self):
		return
		
	def Destroy(self):
		self.__del__()
		
	def LoadUI(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(400, 510)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("")
		self.Board.SetCloseEvent(self.CloseIntroDungeonGUIAndContinue)
		self.Board.Show()
		
		self.HeadImages = ui.ImageBox()
		self.HeadImages.SetParent(self.Board)
		self.HeadImages.SetPosition(15,35)
		#self.HeadImages.LoadImage("d:/ymir work/ui/game/windows/box_face.sub")
		self.HeadImages.Show()
			
		self.HeadThinBoard = ui.ThinBoard()
		self.HeadThinBoard.SetParent(self.Board)
		self.HeadThinBoard.SetSize(371,55)
		self.HeadThinBoard.SetPosition(15,35)
		self.HeadThinBoard.Show()
		
		self.SlotBar = ui.SlotBar()
		self.SlotBar.SetParent(self.Board)
		self.SlotBar.SetPosition(15,95)
		self.SlotBar.SetSize(370,370)
		self.SlotBar.Show()
		
		i 			= 0
		max_line	= 23
		pos_h		= 8
		
		while i < max_line:
			
			self.TextLines[i] = ui.TextLine()
			self.TextLines[i].SetParent(self.SlotBar)
			self.TextLines[i].SetPosition(8,pos_h)
			self.TextLines[i].SetText("Zeile: " + str(i))
			self.TextLines[i].Show()
			
			i = i + 1
			pos_h = pos_h + 15
		
		

		
		self.NextButton = ui.Button()
		self.NextButton.SetParent(self.Board)
		self.NextButton.SetPosition(15,470)
		self.NextButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.NextButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.NextButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.NextButton.SetText("Letzte Seite")
		self.NextButton.SetEvent(self.ButtonBack)
		self.NextButton.Show()
		
		self.BackButton = ui.Button()
		self.BackButton.SetParent(self.Board)
		self.BackButton.SetPosition(300,470)
		self.BackButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.BackButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.BackButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.BackButton.SetText("Nächste Seite")
		self.BackButton.SetEvent(self.ButtonNext)
		self.BackButton.Show()

		
		# self.DeleteButton = ui.Button()
		# self.DeleteButton.SetParent(self.Board)
		# self.DeleteButton.SetPosition(155,470)
		# self.DeleteButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		# self.DeleteButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		# self.DeleteButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		# self.DeleteButton.SetText("Schließen")
		# self.DeleteButton.SetEvent(self.CloseIntroDungeonGUIAndContinue)
		# self.DeleteButton.Hide()	
		
		self.SetPage()
		self.Board.Hide()
		
	def ClearTextLines(self):
		i 			= 0
		max_line	= 23
		while i < max_line:
			self.TextLines[i].SetText("")
			i = i + 1
		
	def SetPage(self):
		self.ClearTextLines()
		TextLines = settinginfo.GuideBoardTextLines
		if TextLines[self.TextBoxIndex][self.PageIndex][0][1] == "head_img":
			self.HeadImages.LoadImage("guide_board/"+str(TextLines[self.TextBoxIndex][self.PageIndex][0][0])+".tga")
			
		i = 0
		TextLine = 1
		while i < len(TextLines[self.TextBoxIndex][self.PageIndex]):
			if len(TextLines[self.TextBoxIndex][self.PageIndex]) > TextLine:
				if TextLines[self.TextBoxIndex][self.PageIndex][TextLine][1] == "title":
					self.TextLines[i].SetFontColor(1.0, 0.7843, 0.0)	
				elif TextLines[self.TextBoxIndex][self.PageIndex][TextLine][1] == "warning":
					self.TextLines[i].SetFontColor(0.9, 0.4745, 0.4627)
				elif TextLines[self.TextBoxIndex][self.PageIndex][TextLine][1] == "attention":
					self.TextLines[i].SetFontColor(0.9607, 0.2392, 0.0)
				elif TextLines[self.TextBoxIndex][self.PageIndex][TextLine][1] == "normal_color":
					self.TextLines[i].SetFontColor(1.0, 1.0, 1.0)
				self.TextLines[i].SetText(TextLines[self.TextBoxIndex][self.PageIndex][TextLine][0])
				TextLine = TextLine + 1
			i = i + 1	

		self.Board.SetTitleName("Seite " + str(self.PageIndex+1) + " / " + str(len(TextLines[self.TextBoxIndex])) + "")
		
		
	# Weiter
	def ButtonNext(self):
		nextPage = self.PageIndex + 1
		TextLines = settinginfo.GuideBoardTextLines
		MaxPage = len(TextLines[self.TextBoxIndex])-1
		
		if nextPage > MaxPage:
			return
		self.PageIndex = nextPage
		self.SetPage()
		#self.Board.SetTitleName("Seite " + str(self.PageIndex) + " / " + str(MaxPage) + "")
		
		if self.PageIndex == 0:
			self.NextButton.Hide()
		else:
			self.NextButton.Show()		
		
		if self.PageIndex == MaxPage:
			self.BackButton.Hide()
			#self.DeleteButton.Show()
		else:
			self.BackButton.Show()
			#self.DeleteButton.Hide()			
	
	# Zurück
	def ButtonBack(self):
		nextPage = self.PageIndex - 1
		TextLines = settinginfo.GuideBoardTextLines
		MaxPage = len(TextLines[self.TextBoxIndex])-1
		
		if nextPage < 0:
			return
		self.PageIndex = nextPage
		self.SetPage()
		#self.Board.SetTitleName("Seite " + str(self.PageIndex) + " / " + str(MaxPage) + "")
		
		if self.PageIndex == 0:
			self.NextButton.Hide()
		else:
			self.NextButton.Show()		
		
		if self.PageIndex == MaxPage:
			self.BackButton.Hide()
			#self.DeleteButton.Show()
		else:
			self.BackButton.Show()
			#self.DeleteButton.Hide()
	
	def CloseIntroDungeonGUIAndContinue(self):
		#event.QuestButtonClick(self.curQuestIndex)
		self.Board.Hide()
	
	def GAME_InitGuideBoard(self,textBlockIndex):
		self.TextBoxIndex = textBlockIndex
		self.PageIndex = 0
		self.SetPage()
		self.Board.Show()		

	def OnPressEscapeKey(self):
		self.CloseIntroDungeonGUIAndContinue()
		return TRUE

	def OnPressExitKey(self):		
		self.CloseIntroDungeonGUIAndContinue()
		return TRUE			

#IntroDungeonBoard().Show()