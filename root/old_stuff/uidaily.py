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



class DailyBoard(ui.ScriptWindow):
	slotImages = {}
	targetSlots = {}
	rewardSlotImages = {}
	rewardSlots = {}
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		settinginfo.DailyQuest_GUI = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()

		
	def LoadUI(self):
		settinginfo.DailyQuest_GUI = 1 
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(266, 340)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Daily-Quest")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()

		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()	
		
		self.TimeThinBoard = ui.ThinBoard()
		self.TimeThinBoard.SetParent(self.Board)
		self.TimeThinBoard.SetPosition(16,35)
		self.TimeThinBoard.SetSize(235,60)
		self.TimeThinBoard.Show()
		
		
		self.TitleBar = ui.HorizontalBar()
		self.TitleBar.SetParent(self.Board)
		self.TitleBar.Create(235)
		self.TitleBar.SetPosition(16,35)
		self.TitleBar.Show()
		
		self.TitleBarTitle = ui.TextLine()
		self.TitleBarTitle.SetParent(self.Board)
		self.TitleBarTitle.SetPosition(133,36)
		self.TitleBarTitle.SetHorizontalAlignCenter()
		self.TitleBarTitle.SetText("Zeit")
		self.TitleBarTitle.Show()
		
		
		self.MainTimeLine = ui.TextLine()
		self.MainTimeLine.SetParent(self.Board)
		self.MainTimeLine.SetPosition(133,65)
		self.MainTimeLine.SetHorizontalAlignCenter()
		self.MainTimeLine.SetText("[ Verbl. Zeit: 13:59:57 Std. ]")
		self.MainTimeLine.SetFontColor(0.5411, 0.7254, 0.5568)		
		self.MainTimeLine.Show()	

		self.TargetThinBoard = ui.ThinBoard()
		self.TargetThinBoard.SetParent(self.Board)
		self.TargetThinBoard.SetPosition(16,100)
		self.TargetThinBoard.SetSize(235,65)
		self.TargetThinBoard.Show()
		
		
		self.TargetTitleBar = ui.HorizontalBar()
		self.TargetTitleBar.SetParent(self.Board)
		self.TargetTitleBar.Create(235)
		self.TargetTitleBar.SetPosition(16,100)
		self.TargetTitleBar.Show()

		self.TargetTitle = ui.TextLine()
		self.TargetTitle.SetParent(self.Board)
		self.TargetTitle.SetPosition(133,101)
		self.TargetTitle.SetHorizontalAlignCenter()
		self.TargetTitle.SetText("Ziel(e)")
		self.TargetTitle.Show()

		
		i = 0
		slot_count = 6
		width = 37
		while i < slot_count:
			self.slotImages[i] = ui.ImageBox()
			self.slotImages[i].SetParent(self.Board)
			self.slotImages[i].SetPosition(width,120)
			self.slotImages[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			self.slotImages[i].Show()
			
			
			self.targetSlots[i] = ui.GridSlotWindow()  
			self.targetSlots[i].SetParent(self.slotImages[i])  
			self.targetSlots[i].ArrangeSlot(i,1,1,32,32,0,0)  
			self.targetSlots[i].SetPosition(0, 0)  
			self.targetSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
			self.targetSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
			self.targetSlots[i].SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
			self.targetSlots[i].SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
			self.targetSlots[i].Show()				
			

			width = width + 32
			i = i + 1		

		
		self.rewardThinBoard = ui.ThinBoard()
		self.rewardThinBoard.SetParent(self.Board)
		self.rewardThinBoard.SetPosition(16,170)
		self.rewardThinBoard.SetSize(235,65)
		self.rewardThinBoard.Show()
		
		
		self.rewardTitleBar = ui.HorizontalBar()
		self.rewardTitleBar.SetParent(self.Board)
		self.rewardTitleBar.Create(235)
		self.rewardTitleBar.SetPosition(16,170)
		self.rewardTitleBar.Show()

		self.rewardTitle = ui.TextLine()
		self.rewardTitle.SetParent(self.Board)
		self.rewardTitle.SetPosition(133,171)
		self.rewardTitle.SetHorizontalAlignCenter()
		self.rewardTitle.SetText("Belohnung")
		self.rewardTitle.Show()	
		
		i = 0
		slot_count = 6
		width = 37
		slot_idx = 7
		while i < slot_count:
			self.rewardSlotImages[i] = ui.ImageBox()
			self.rewardSlotImages[i].SetParent(self.Board)
			self.rewardSlotImages[i].SetPosition(width,190)
			self.rewardSlotImages[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			self.rewardSlotImages[i].Show()
			

			
			self.rewardSlots[i] = ui.GridSlotWindow()  
			self.rewardSlots[i].SetParent(self.rewardSlotImages[i])  
			self.rewardSlots[i].ArrangeSlot(slot_idx,1,1,32,32,0,0)  
			self.rewardSlots[i].SetPosition(0, 0)  
			self.rewardSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
			self.rewardSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
			self.rewardSlots[i].SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
			self.rewardSlots[i].SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
			self.rewardSlots[i].Show()				
			slot_idx = slot_idx + 1
			width = width + 32
			i = i + 1			
		
		
		self.startThinBoard = ui.ThinBoard()
		self.startThinBoard.SetParent(self.Board)
		self.startThinBoard.SetPosition(16,240)
		self.startThinBoard.SetSize(235,85)
		self.startThinBoard.Show()
		
		
		self.startTitleBar = ui.HorizontalBar()
		self.startTitleBar.SetParent(self.Board)
		self.startTitleBar.Create(235)
		self.startTitleBar.SetPosition(16,240)
		self.startTitleBar.Show()

		self.startTitle = ui.TextLine()
		self.startTitle.SetParent(self.Board)
		self.startTitle.SetPosition(133,241)
		self.startTitle.SetHorizontalAlignCenter()
		self.startTitle.SetText("Quest starten")
		self.startTitle.Show()	
		
		self.startButton = ui.Button()
		self.startButton.SetParent(self.Board)
		self.startButton.SetPosition(40,270)
		self.startButton.SetText("")
		self.startButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")  
		self.startButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")  
		self.startButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")	
		self.startButton.SetEvent(self.StartQuest)
		self.startButton.Show()	
		
		self.disStartButton = ui.Button()
		self.disStartButton.SetParent(self.Board)
		self.disStartButton.SetPosition(40,270)
		self.disStartButton.SetText("")
		self.disStartButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_03.sub")  
		self.disStartButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_03.sub")  
		self.disStartButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")	
		self.disStartButton.SetEvent(self.disButtonFunc)
		self.disStartButton.Hide()	
		
		self.startButtonTitle = ui.TextLine()
		self.startButtonTitle.SetParent(self.Board)
		self.startButtonTitle.SetPosition(133,276)
		self.startButtonTitle.SetHorizontalAlignCenter()
		self.startButtonTitle.SetText("Starten!")
		self.startButtonTitle.Show()		
		
	def StartQuest(self):
		event.QuestButtonClick(settinginfo.DailyQuest_QID)
		
	def disButtonFunc(self):
		return
		
	def ShowToolTip(self,slot):

		self.itemtooltip.ClearToolTip()
		
		if slot < 7:
			if slot+1 <= len(settinginfo.DailyQuest_Monster):
				self.itemtooltip.AddItemData(settinginfo.DailyQuest_Monster[slot], [0, 0, 0])
				self.itemtooltip.ShowToolTip()		
		else:
			rewardArrSlot = slot - 7
			if rewardArrSlot+1 <= len(settinginfo.DailyQuest_Reward):
				
				self.itemtooltip.AddItemData(settinginfo.DailyQuest_Reward[rewardArrSlot], [0, 0, 0])
				self.itemtooltip.ShowToolTip()	

				
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()
		
	def add_slot(self,slot):
		return
		
	def del_slot(self,slot):
		return

	def OnUpdate(self):
		if settinginfo.DailyQuest_Status == 0:
			if app.GetGlobalTimeStamp() < settinginfo.DailyQuest_Time:
				self.MainTimeLine.SetText("[ Zeit bis zur nächsten Quest: " + str(self.FormatTime()) + " Std. ]")				
				self.MainTimeLine.SetFontColor(0.9, 0.4745, 0.4627)
				
				self.disStartButton.Show()
				self.startButton.Hide()					
			else:
				self.MainTimeLine.SetText("[ Du kannst eine neue Quest beginnen! ]")				
				self.MainTimeLine.SetFontColor(0.5411, 0.7254, 0.5568)			
				self.disStartButton.Hide()
				self.startButton.Show()	
				
			i = 0
			slot_count = 6
			while i < slot_count:
						
				self.targetSlots[i].ClearSlot(i)
				#self.targetSlots[i].SetItemSlot(i, settinginfo.DailyQuest_Monster[i], settinginfo.DailyQuest_Count[i])
				self.targetSlots[i].RefreshSlot()
						
				rewardSlotCount = i + 7
				self.rewardSlots[i].ClearSlot(rewardSlotCount)
				#self.rewardSlots[i].SetItemSlot(rewardSlotCount, settinginfo.DailyQuest_Reward[i], settinginfo.DailyQuest_RewardCount[i])
				self.rewardSlots[i].RefreshSlot()						

				i = i + 1
				
		elif settinginfo.DailyQuest_Status == 1:
			if app.GetGlobalTimeStamp() < settinginfo.DailyQuest_Time:
				self.MainTimeLine.SetText("[ Verbl. Zeit: " + str(self.FormatTime()) + " Std. ]")				
				self.MainTimeLine.SetFontColor(0.5411, 0.7254, 0.5568)
				self.disStartButton.Show()
				self.startButton.Hide()				
				if len(settinginfo.DailyQuest_Monster) > 0:
					i = 0
					slot_count = 6
					while i < slot_count:
						
						if i+1 <= len(settinginfo.DailyQuest_Monster):
							self.targetSlots[i].ClearSlot(i)
							self.targetSlots[i].SetItemSlot(i, settinginfo.DailyQuest_Monster[i], settinginfo.DailyQuest_Count[i])
							self.targetSlots[i].RefreshSlot()
							
							if settinginfo.DailyQuest_Count[i] == 0:
								self.targetSlots[i].ActivateSlot(i)
						
						
						if i+1 <= len(settinginfo.DailyQuest_Reward):
							rewardSlotCount = i + 7
							self.rewardSlots[i].ClearSlot(rewardSlotCount)
							self.rewardSlots[i].SetItemSlot(rewardSlotCount, settinginfo.DailyQuest_Reward[i], settinginfo.DailyQuest_RewardCount[i])
							self.rewardSlots[i].RefreshSlot()					

						i = i + 1					

					
			else:
				self.MainTimeLine.SetText("[ Die Zeit ist abgelaufen! ]")				
				self.MainTimeLine.SetFontColor(0.9, 0.4745, 0.4627)		
				self.disStartButton.Show()
				self.startButton.Hide()				
				
	def FormatTime(self):
		sec = settinginfo.DailyQuest_Time - app.GetGlobalTimeStamp() 
		m, s = divmod(sec, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%02d" % (h, m, s)	
		
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE	
		
#DailyBoard().Show()