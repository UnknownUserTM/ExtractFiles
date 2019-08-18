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


class GMPostBoard(ui.ScriptWindow):
	
	EditLines 	= {}
	TimeBlock	= 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		
	def LoadUI(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(397, 310)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("GM-Nachricht schreiben")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()

		self.SlotBar = ui.SlotBar()
		self.SlotBar.SetParent(self.Board)
		self.SlotBar.SetPosition(15,35)
		self.SlotBar.SetSize(367,230)
		self.SlotBar.Show()

		i = 0
		max_lines = 14
		height = 8
		while i < max_lines:
			self.EditLines[i] = ui.EditLine()
			self.EditLines[i].SetParent(self.SlotBar)
			self.EditLines[i].SetPosition(8,height)
			self.EditLines[i].SetSize(367,15)
			self.EditLines[i].SetMax(70)
			self.EditLines[i].Show()	
		
			i = i + 1
			height = height + 15

		self.EditLines[0].SetFocus()
		self.SendButton = ui.Button()
		self.SendButton.SetParent(self.Board)
		self.SendButton.SetPosition(15,275)
		self.SendButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.SendButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.SendButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.SendButton.SetText("Absenden")
		self.SendButton.SetEvent(self.PostGMMessage)
		self.SendButton.Show()
		
		self.DeleteButton = ui.Button()
		self.DeleteButton.SetParent(self.Board)
		self.DeleteButton.SetPosition(110,275)
		self.DeleteButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.DeleteButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.DeleteButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.DeleteButton.SetText("Löschen")
		self.DeleteButton.SetEvent(self.ClearGMMessage)
		self.DeleteButton.Show()	
		
	def PostGMMessage(self):
		if self.TimeBlock < app.GetTime():
			for i in xrange(14):
				if len(self.EditLines[i].GetText()) > 0:
					if self.EditLines[i].GetText() == "[ENTER]":
						GFHhg54GHGhh45GHGH.SendChatPacket("/n ", chat.CHAT_TYPE_COMMAND)
					else:
						GFHhg54GHGhh45GHGH.SendChatPacket("/n " + self.EditLines[i].GetText(), chat.CHAT_TYPE_COMMAND)
			self.TimeBlock = app.GetTime() + 10
		else:
			timeLeft = self.TimeBlock - app.GetTime()
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Bitte warte noch " + str(timeLeft) +" Sek. nach dem absenden einer Nachricht!")
			
	def ClearGMMessage(self):
		for i in xrange(14):
			self.EditLines[i].SetText("")
		self.EditLines[0].SetFocus()
		
#GMPostBoard().Show()