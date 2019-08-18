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



class UppStorageBoard(ui.ScriptWindow):
	slotImages = {}
	radiaButtons = {}
	itemSlots = {}
	storeAllTimeBlock = 0
	YamatoWidth = 15
	YamatoHeight = 30
	selCat = 1 # Lesen
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		settinginfo.UppItemStorageOpen = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		

		
	def LoadUI(self):
		settinginfo.UppItemStorageOpen = 1
		self.Board = ui.BoardWithRoofBar()
		self.Board.SetSize(266, 425+20 - self.YamatoHeight - 20)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.AddFlag("attach")
		# self.Board.SetTitleName("UppItem-Lager")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()

		self.itemtooltipup = uiToolTip.ItemToolTip()  
		self.itemtooltipup.HideToolTip()	

		self.NormalButtonUp = ui.Button()
		self.NormalButtonUp.SetParent(self.Board)
		self.NormalButtonUp.SetPosition(16 + self.YamatoWidth,33 + self.YamatoHeight)
		self.NormalButtonUp.SetText("")
		self.NormalButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.NormalButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.NormalButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.NormalButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 1)
		self.NormalButtonUp.Hide()
		
		self.NormalButtonDown = ui.Button()
		self.NormalButtonDown.SetParent(self.Board)
		self.NormalButtonDown.SetPosition(16 + self.YamatoWidth,33 + self.YamatoHeight)
		self.NormalButtonDown.SetText("")
		self.NormalButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.NormalButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.NormalButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.NormalButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 1)
		self.NormalButtonDown.Show()
		
		self.UsuallyButtonUp = ui.Button()
		self.UsuallyButtonUp.SetParent(self.Board)
		self.UsuallyButtonUp.SetPosition(95 + self.YamatoWidth,33 + self.YamatoHeight)
		self.UsuallyButtonUp.SetText("")
		self.UsuallyButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.UsuallyButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.UsuallyButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.UsuallyButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 2)
		self.UsuallyButtonUp.Show()	
		
		self.UsuallyButtonDown = ui.Button()
		self.UsuallyButtonDown.SetParent(self.Board)
		self.UsuallyButtonDown.SetPosition(95 + self.YamatoWidth,33 + self.YamatoHeight)
		self.UsuallyButtonDown.SetText("")
		self.UsuallyButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.UsuallyButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.UsuallyButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.UsuallyButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 2)
		self.UsuallyButtonDown.Hide()
		
		self.RareButtonUp = ui.Button()
		self.RareButtonUp.SetParent(self.Board)
		self.RareButtonUp.SetPosition(174 + self.YamatoWidth,33 + self.YamatoHeight)
		self.RareButtonUp.SetText("")
		self.RareButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.RareButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.RareButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.RareButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 3)
		self.RareButtonUp.Show()	
		
		self.RareButtonDown = ui.Button()
		self.RareButtonDown.SetParent(self.Board)
		self.RareButtonDown.SetPosition(174 + self.YamatoWidth,33 + self.YamatoHeight)
		self.RareButtonDown.SetText("")
		self.RareButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.RareButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.RareButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.RareButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 3)
		self.RareButtonDown.Hide()
		
		self.ButtonTextLines = ui.TextLine()
		self.ButtonTextLines.SetParent(self.Board)
		self.ButtonTextLines.SetPosition(30 + self.YamatoWidth,36 + self.YamatoHeight)
		self.ButtonTextLines.SetText("   Normal            Gewöhnlich             Selten")
		self.ButtonTextLines.Show()	

		self.SplitTitleBar = ui.HorizontalBar()
		self.SplitTitleBar.SetParent(self.Board)
		self.SplitTitleBar.Create(235)
		self.SplitTitleBar.SetPosition(16 + self.YamatoWidth,55 + self.YamatoHeight)
		self.SplitTitleBar.Show()

		slot_count = 60
		i = 0
		line_count = 0
		height_jump = 6
		width = 38 + self.YamatoWidth
		height = 75 + self.YamatoHeight
		
		while i < slot_count:
			self.slotImages[i] = ui.ImageBox()
			self.slotImages[i].SetParent(self.Board)
			self.slotImages[i].SetPosition(width,height)
			self.slotImages[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			self.slotImages[i].Show()	
			
			self.itemSlots[i] = ui.GridSlotWindow()  
			self.itemSlots[i].SetParent(self.slotImages[i])  
			self.itemSlots[i].ArrangeSlot(i,1,1,32,32,0,0)  
			self.itemSlots[i].SetPosition(0, 0)  
			self.itemSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
			self.itemSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
			self.itemSlots[i].SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
			self.itemSlots[i].SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
			self.itemSlots[i].SetCoverButton(i)
			self.itemSlots[i].Show()	
			
			width = width + 32
			line_count = line_count + 1
			if line_count == height_jump:
				width = 38 + self.YamatoWidth
				height = height + 32
				line_count = 0
			i = i + 1
			
		height = height + 10
			
		self.StoreAllButton = ui.Button()
		self.StoreAllButton.SetParent(self.Board)
		self.StoreAllButton.SetPosition(43 + self.YamatoWidth,height)
		self.StoreAllButton.SetText("")
		self.StoreAllButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")  
		self.StoreAllButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")  
		self.StoreAllButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")	
		self.StoreAllButton.SetEvent(self.StoreAll)
		self.StoreAllButton.Show()
		
		self.ButtonTextLine = ui.TextLine()
		self.ButtonTextLine.SetParent(self.Board)
		self.ButtonTextLine.SetPosition(133 + self.YamatoWidth,height+5)
		self.ButtonTextLine.SetText("Alles einlagern!")
		self.ButtonTextLine.SetHorizontalAlignCenter()
		self.ButtonTextLine.Show()	


		
	def StoreAll(self):
		if self.storeAllTimeBlock < app.GetTime():
			self.storeAllTimeBlock = app.GetTime() + 5
			constInfo.INPUT_CMD = "store_all#"
			event.QuestButtonClick(settinginfo.UppItemStorageQID)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[UppItem-Lager] Bitte warte einen moment...")	
			
	def OnUpdate(self):
		slot_count = 60
		i = 0
		while i < slot_count:
			if i <= len(settinginfo.UppItemStorageItemList[self.selCat])-1:
				itemCount = 0
				itemCountStart = i + 1
				if self.selCat == 1:
					itemCount = settinginfo.UppItemStorageNormal[itemCountStart]
				elif self.selCat == 2:
					itemCount = settinginfo.UppItemStorageUsually[itemCountStart]
				elif self.selCat == 3:
					itemCount = settinginfo.UppItemStorageRare[itemCountStart]
				
				self.itemSlots[i].SetItemSlot(i, settinginfo.UppItemStorageItemList[self.selCat][i], itemCount)
				if itemCount > 0:
					self.itemSlots[i].EnableCoverButton(i)
				else:
					self.itemSlots[i].DisableCoverButton(i)
				
			i = i + 1

	def ShowToolTip(self,slot):
		self.itemtooltipup.ClearToolTip()
		if slot <= len(settinginfo.UppItemStorageItemList[self.selCat])-1:
			self.itemtooltipup.AddItemData(settinginfo.UppItemStorageItemList[self.selCat][slot], [40000, 1, 0])
			self.itemtooltipup.ShowToolTip()

	def HideToolTip(self):
		self.itemtooltipup.HideToolTip()
		
	def add_slot(self,slot):
		return
		
	def del_slot(self,slot):
		slotquest = slot + 1
		if slotquest <= len(settinginfo.UppItemStorageItemList[self.selCat]):
			if settinginfo.UppItemStorageQID == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Kein QuestIndex gefunden!")	
				return					

			if settinginfo.UppItemStorageItemList[self.selCat][slot] <= 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Du besitzt diesen Gegenstand nicht.")	
				return						
			if app.IsPressed(app.DIK_LCONTROL):
				#chat.AppendChat(chat.CHAT_TYPE_INFO,"DIK_LCONTROL pressed!")	
				constInfo.INPUT_CMD = "take#" + str(slotquest) + "#" + str(self.selCat) + "#true#"
			else:	
				constInfo.INPUT_CMD = "take#" + str(slotquest) + "#" + str(self.selCat) + "#false#"
			event.QuestButtonClick(settinginfo.UppItemStorageQID)				
		
	def ChangeActionMode(self,buttonIndex):
		if self.selCat == buttonIndex:
			return
			
		if buttonIndex == 1:
			self.NormalButtonDown.Show()
			self.NormalButtonUp.Hide()
			
			self.UsuallyButtonDown.Hide()
			self.UsuallyButtonUp.Show()
				
			self.RareButtonDown.Hide()
			self.RareButtonUp.Show()		
		
		elif buttonIndex == 2:
			self.NormalButtonDown.Hide()
			self.NormalButtonUp.Show()
			
			self.UsuallyButtonDown.Show()
			self.UsuallyButtonUp.Hide()
				
			self.RareButtonDown.Hide()
			self.RareButtonUp.Show()		
		
		elif buttonIndex == 3:
			self.NormalButtonDown.Hide()
			self.NormalButtonUp.Show()
			
			self.UsuallyButtonDown.Hide()
			self.UsuallyButtonUp.Show()
				
			self.RareButtonDown.Show()
			self.RareButtonUp.Hide()		
		
		self.selCat = buttonIndex
		slot_count = 60
		i = 0
		while i < slot_count:		
			self.itemSlots[i].ClearSlot(i)
			self.itemSlots[i].SetItemSlot(i, 0, 0)
			self.itemSlots[i].RefreshSlot()
			i = i + 1
	
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE			
