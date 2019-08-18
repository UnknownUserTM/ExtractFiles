## Developed by Exterminatus!
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
import shop
import uiCommon

class BugReportBoard(ui.ScriptWindow):
	
	isOpen = False
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
			
	def Destroy(self):
		self.__del__()
	
	def Close(self):
		self.Board.Hide()
		
	def Manage(self):
		if self.isOpen:
			self.isOpen = False
			self.Board.Hide()

		else:
			self.isOpen = True
			self.Board.Show()
			
	def LoadUI(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(330, 185)
		# self.Board.SetPosition(wndMgr.GetScreenWidth()/2-165,wndMgr.GetScreenHeight()-wndMgr.GetScreenHeight()+100)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Fehlerbericht senden") 
		self.Board.SetCloseEvent(self.Manage)
		self.Board.Hide()
		
		self.ReportBG = ui.Bar()
		self.ReportBG.SetParent(self.Board)
		self.ReportBG.SetPosition(15,35)
		self.ReportBG.SetSize(300,100)
		self.ReportBG.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.ReportBG.Show()

		self.ReportEditLine = ui.EditLine()
		self.ReportEditLine.SetParent(self.Board)
		self.ReportEditLine.SetPosition(20,40)
		self.ReportEditLine.SetSize(300,95)
		self.ReportEditLine.bCodePage = True
		self.ReportEditLine.SetLimitWidth(295)
		self.ReportEditLine.SetMultiLine()
		self.ReportEditLine.SetMax(240)
		self.ReportEditLine.Show()
		
		self.ReportButtonBG = ui.Bar()
		self.ReportButtonBG.SetParent(self.Board)
		self.ReportButtonBG.SetPosition(15,138)
		self.ReportButtonBG.SetSize(300,30)
		self.ReportButtonBG.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.ReportButtonBG.Show()
		
		self.SendReportButton = ui.ToolTipButton()
		self.SendReportButton.SetParent(self.Board)
		self.SendReportButton.SetPosition(120,142)
		self.SendReportButton.SetText("")
		self.SendReportButton.SetButtonWidth(90)
		self.SendReportButton.AppendToolTipTextLine("Falschmeldungen oder ausnutzen dieser Funktion führt zur Accountsperre!")
		self.SendReportButton.ArrangeToolTip()
		self.SendReportButton.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.SendReportButton.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.SendReportButton.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.SendReportButton.SetEvent(self.__SendBugReport)
		self.SendReportButton.Show()	
		
		self.SendReportButtonTextLine = ui.TextLine()
		self.SendReportButtonTextLine.SetParent(self.Board)
		self.SendReportButtonTextLine.SetPosition(165,145)
		self.SendReportButtonTextLine.SetText("Senden...")
		self.SendReportButtonTextLine.SetHorizontalAlignCenter()
		self.SendReportButtonTextLine.Show()
		
		
	def __SendBugReport(self):
		reportString			= self.ReportEditLine.GetText()
		reportStringFormat 		= reportString.replace(" ", "_")
		reportStringFormatGM 	= reportStringFormat.replace("[", "")
		reportStringFormatGM2 	= reportStringFormatGM.replace("]", "")
		
		GFHhg54GHGhh45GHGH.SendChatPacket("/report " + reportStringFormatGM2)
		self.ReportEditLine.SetText("")
	
# BugReportBoard().Show()

