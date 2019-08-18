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

class AchievementStatisticBoard(ui.ScriptWindow):
	faceBoxIMG 		= {}
	faceBoxBGIMG 	= {} 
	DescThinBoard 	= {}
	
	AchievementTitle 		= {}
	AchievementText 		= {}
	AchievementCalcPoints	= {}
	
	cat = 0
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		settinginfo.Achievement_Statistic["status"] = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		
	def LoadUI(self):
		settinginfo.Achievement_Statistic["status"] = 1
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(266, 415) # 266
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Achievement-Statistik")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()

		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()	

		self.BossButtonUp = ui.Button()
		self.BossButtonUp.SetParent(self.Board)
		self.BossButtonUp.SetPosition(16,33)
		self.BossButtonUp.SetText("")
		self.BossButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.BossButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.BossButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.BossButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 1)
		self.BossButtonUp.Hide()
		
		self.BossButtonDown = ui.Button()
		self.BossButtonDown.SetParent(self.Board)
		self.BossButtonDown.SetPosition(16,33)
		self.BossButtonDown.SetText("")
		self.BossButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.BossButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.BossButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.BossButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 1)
		self.BossButtonDown.Show()
		
		self.MetinButtonUp = ui.Button()
		self.MetinButtonUp.SetParent(self.Board)
		self.MetinButtonUp.SetPosition(95,33)
		self.MetinButtonUp.SetText("")
		self.MetinButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.MetinButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.MetinButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.MetinButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 2)
		self.MetinButtonUp.Show()	
		
		self.MetinButtonDown = ui.Button()
		self.MetinButtonDown.SetParent(self.Board)
		self.MetinButtonDown.SetPosition(95,33)
		self.MetinButtonDown.SetText("")
		self.MetinButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.MetinButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.MetinButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.MetinButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 2)
		self.MetinButtonDown.Hide()
		
		self.DungeonsButtonUp = ui.Button()
		self.DungeonsButtonUp.SetParent(self.Board)
		self.DungeonsButtonUp.SetPosition(174,33)
		self.DungeonsButtonUp.SetText("")
		self.DungeonsButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.DungeonsButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.DungeonsButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.DungeonsButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 3)
		self.DungeonsButtonUp.Show()	
		
		self.DungeonsButtonDown = ui.Button()
		self.DungeonsButtonDown.SetParent(self.Board)
		self.DungeonsButtonDown.SetPosition(174,33)
		self.DungeonsButtonDown.SetText("")
		self.DungeonsButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.DungeonsButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.DungeonsButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.DungeonsButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 3)
		self.DungeonsButtonDown.Hide()

		self.scrollbar = ui.ScrollBar()
		self.scrollbar.SetParent(self.Board)
		self.scrollbar.SetScrollBarSize(340)
		self.scrollbar.SetPosition(255, 55)	
		self.scrollbar.SetMiddleBarSize(float(5) / float(7))
		self.scrollbar.SetScrollEvent(self.__OnScroll)
		self.scrollbar.Hide()
		
		self.ButtonTextLines = ui.TextLine()
		self.ButtonTextLines.SetParent(self.Board)
		self.ButtonTextLines.SetPosition(30,36)
		self.ButtonTextLines.SetText("    Bosse                  Metins              Dungeons")
		self.ButtonTextLines.Show()	

		self.SplitTitleBar = ui.HorizontalBar()
		self.SplitTitleBar.SetParent(self.Board)
		self.SplitTitleBar.Create(235)
		self.SplitTitleBar.SetPosition(16,55)
		self.SplitTitleBar.Show()
		
		self.AchievementError = ui.TextLine()
		self.AchievementError.SetParent(self.Board)
		self.AchievementError.SetPosition(133,80)
		self.AchievementError.SetFontColor(0.9607, 0.2392, 0.0)
		self.AchievementError.SetText("Es wurden keine Achievements gefunden!")
		self.AchievementError.SetHorizontalAlignCenter()
		self.AchievementError.Hide()

			
		i = 0
		height = 75
		max_box = 5
		
		while i < max_box:
		
			self.faceBoxIMG[i] = ui.ImageBox()
			self.faceBoxIMG[i].SetParent(self.Board)
			self.faceBoxIMG[i].SetPosition(17,height)
			self.faceBoxIMG[i].LoadImage("d:/ymir work/ui/game/windows/box_face.sub")
			self.faceBoxIMG[i].Show()

			
			self.DescThinBoard[i] = ui.ThinBoard()
			self.DescThinBoard[i].SetParent(self.Board)
			self.DescThinBoard[i].SetPosition(70,height)
			self.DescThinBoard[i].SetSize(180,60)
			self.DescThinBoard[i].Show()
			
			self.AchievementTitle[i] = ui.TextLine()
			self.AchievementTitle[i].SetParent(self.DescThinBoard[i])
			self.AchievementTitle[i].SetPosition(90,5)
			self.AchievementTitle[i].SetFontColor(0.9607, 0.2392, 0.0)
			self.AchievementTitle[i].SetText("Metin des Kummers")
			self.AchievementTitle[i].SetHorizontalAlignCenter()
			self.AchievementTitle[i].Show()
			
			self.AchievementText[i] = ui.TextLine()
			self.AchievementText[i].SetParent(self.DescThinBoard[i])
			self.AchievementText[i].SetPosition(90,20)
			self.AchievementText[i].SetText("Anzahl: 30.000 | Punkte: 10")
			self.AchievementText[i].SetHorizontalAlignCenter()
			self.AchievementText[i].Show()	
			
			self.AchievementCalcPoints[i] = ui.TextLine()
			self.AchievementCalcPoints[i].SetParent(self.DescThinBoard[i])
			self.AchievementCalcPoints[i].SetPosition(90,35)
			self.AchievementCalcPoints[i].SetText("Bisher erhaltene Punkte: 13.400.032")
			self.AchievementCalcPoints[i].SetHorizontalAlignCenter()
			self.AchievementCalcPoints[i].Show()			

			height = height + 65
			i = i + 1
		
		self.cat = 1
		self.ClearBoards()
		self.LoadCategory()
		
	def LoadCategory(self):
		self.ClearBoards()
		
		if len(settinginfo.Achievement_Statistic[self.cat]) == 0:
			
			#chat.AppendChat(chat.CHAT_TYPE_INFO,"NoAchievements: " + str(self.cat) + " Count: " + str(len(settinginfo.Achievement_Statistic[self.cat])))
		
			self.Board.SetSize(266, 415) 
			self.scrollbar.Hide()
			self.AchievementError.Show()
			return
			
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"StartListing")
		for i in xrange(min(len(settinginfo.Achievement_Statistic[self.cat]),5)):
			cmd = settinginfo.Achievement_Statistic[self.cat][i].split("#")

			self.AchievementTitle[i].SetText(self.GetAchievementName(int(cmd[0])))
			self.AchievementText[i].SetText("Anzahl: " + constInfo.NumberToPointString(int(cmd[1])) + " | Punkte: " + constInfo.NumberToPointString(int(cmd[2])))
			self.AchievementCalcPoints[i].SetText("Bisher erhaltene Punkte: " + constInfo.NumberToPointString(int(cmd[3])))

			self.faceBoxIMG[i].Show()
			self.DescThinBoard[i].Show()	

		if len(settinginfo.Achievement_Statistic[self.cat]) > 5:
			self.Board.SetSize(285, 415) 
			self.scrollbar.SetPos(0)
			self.scrollbar.SetMiddleBarSize(float(5) / float(len(settinginfo.Achievement_Statistic[self.cat])))
			self.scrollbar.Show()	
		else:
			self.Board.SetSize(266, 415) 
			self.scrollbar.Hide()			
		
		self.AchievementError.Hide()
		
	def GetAchievementName(self,index):
		if index in settinginfo.Achievement_Names:
			return settinginfo.Achievement_Names[index]
		else:
			return str(index)		
		
	def __OnScroll(self):
		pos = int(self.scrollbar.GetPos() * (len(settinginfo.Achievement_Statistic[self.cat]) - 5)) ##Aktuelle Position der Scrollbar
		#self.Board.SetTitleName("Achievement-Statistik (Pos: " + str(pos) + ")")
		for i in xrange(5):
			realPos = i + pos
			
			cmd = settinginfo.Achievement_Statistic[self.cat][realPos].split("#")

			self.AchievementTitle[i].SetText(self.GetAchievementName(int(cmd[0])))
			self.AchievementText[i].SetText("Anzahl: " + constInfo.NumberToPointString(int(cmd[1])) + " | Punkte: " + constInfo.NumberToPointString(int(cmd[2])))
			self.AchievementCalcPoints[i].SetText("Bisher erhaltene Punkte: " + constInfo.NumberToPointString(int(cmd[3])))
			try:
				self.faceBoxIMG[i].LoadImage("images_achievement/" + str(cmd[0]) + ".tga")
			except:
				self.faceBoxIMG[i].LoadImage("images_achievement/unknown.tga")

	def ClearBoards(self):
		i = 0
		max_box = 5
		while i < max_box:
			self.faceBoxIMG[i].Hide()
			self.DescThinBoard[i].Hide()
			i = i + 1
	
	def ChangeActionMode(self,idx):
		if self.cat == idx:
			return
			
		if idx == 1:
			self.BossButtonUp.Hide()
			self.BossButtonDown.Show()
			
			self.MetinButtonUp.Show()
			self.MetinButtonDown.Hide()

			self.DungeonsButtonUp.Show()
			self.DungeonsButtonDown.Hide()			
			

		elif idx == 2:
			self.BossButtonUp.Show()
			self.BossButtonDown.Hide()
			
			self.MetinButtonUp.Hide()
			self.MetinButtonDown.Show()

			self.DungeonsButtonUp.Show()
			self.DungeonsButtonDown.Hide()			
		
		elif idx == 3:
			self.BossButtonUp.Show()
			self.BossButtonDown.Hide()
			
			self.MetinButtonUp.Show()
			self.MetinButtonDown.Hide()

			self.DungeonsButtonUp.Hide()
			self.DungeonsButtonDown.Show()			
		
		self.cat = idx
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"ChangeActionMode: " + str(self.cat))
		self.LoadCategory()
	
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE			
#AchievementStatisticBoard().Show()