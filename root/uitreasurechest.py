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
import uiPrivateShopBuilder



class TreasureChestBoard(ui.ScriptWindow):

	slotImages = {}
	otherBoxSlots = {}
	
	treasureBoxVnum = 0
	treasureBoxSlot = 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		#constInfo.warpgui_open = 0
		settinginfo.BoxOpenerOpen = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()

		
	def LoadUI(self):
		settinginfo.BoxOpenerOpen = 1
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(266, 405)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Truhen öffnen.")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()

		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()	
		
		self.OpenBoxThinBoardBG = ui.ImageBox()
		self.OpenBoxThinBoardBG.SetParent(self.Board)
		self.OpenBoxThinBoardBG.SetPosition(15,35)
		self.OpenBoxThinBoardBG.LoadImage("images_jewel/box_bg.tga")
		self.OpenBoxThinBoardBG.Show()
		
		self.OpenBoxThinBoard = ui.ThinBoard()
		self.OpenBoxThinBoard.SetParent(self.Board)
		self.OpenBoxThinBoard.SetSize(236,110)
		self.OpenBoxThinBoard.SetPosition(15,35)
		self.OpenBoxThinBoard.Show()
		
		self.OpenBoxInstruction = ui.TextLine()
		self.OpenBoxInstruction.SetParent(self.Board)
		self.OpenBoxInstruction.SetText("Bitte lege die zu öffnenden Truhen in den Slot.")
		self.OpenBoxInstruction.SetPosition(133,45)
		self.OpenBoxInstruction.SetHorizontalAlignCenter()
		self.OpenBoxInstruction.Show()		
		
		self.OpenBoxRedSlotImg = ui.ImageBox()
		self.OpenBoxRedSlotImg.SetParent(self.Board)
		self.OpenBoxRedSlotImg.SetPosition(113,70)
		self.OpenBoxRedSlotImg.LoadImage("images_jewel/red_slot.tga")
		self.OpenBoxRedSlotImg.Show()		
		
		self.OpenBoxSlot = ui.GridSlotWindow()  
		self.OpenBoxSlot.SetParent(self.OpenBoxRedSlotImg)  
		self.OpenBoxSlot.ArrangeSlot(50,1,1,32,32,0,0)  
		self.OpenBoxSlot.SetPosition(4, 4)  
		self.OpenBoxSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.OpenBoxSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
		self.OpenBoxSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
		self.OpenBoxSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
		self.OpenBoxSlot.Show()	

		self.OpenBoxButton = ui.Button()
		self.OpenBoxButton.SetParent(self.Board)
		self.OpenBoxButton.SetPosition(90,115)
		self.OpenBoxButton.SetText("")
		self.OpenBoxButton.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.OpenBoxButton.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.OpenBoxButton.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.OpenBoxButton.SetEvent(self.OpenBOXCMD)
		self.OpenBoxButton.Show()
		
		self.OpenBoxButtonText = ui.TextLine()
		self.OpenBoxButtonText.SetParent(self.Board)
		self.OpenBoxButtonText.SetText("Alle öffnen!")
		self.OpenBoxButtonText.SetPosition(133,118)
		self.OpenBoxButtonText.SetHorizontalAlignCenter()
		self.OpenBoxButtonText.Show()	


		self.OtherBoxTitleBar = ui.HorizontalBar()
		self.OtherBoxTitleBar.SetParent(self.Board)
		self.OtherBoxTitleBar.Create(235)
		self.OtherBoxTitleBar.SetPosition(16,150)
		self.OtherBoxTitleBar.Show()
		
		self.OtherBoxTitle = ui.TextLine()
		self.OtherBoxTitle.SetParent(self.Board)
		self.OtherBoxTitle.SetText("Truhen die hier geöffnet werden können.")
		self.OtherBoxTitle.SetPosition(133,150)
		self.OtherBoxTitle.SetHorizontalAlignCenter()
		self.OtherBoxTitle.Show()	
		
		
		i = 0
		count_line = 0
		next_line = 6
		slot_count = 42
		width = 30
		height = 170
		treasureBoxVnums = settinginfo.treasure_chest_vnum
		treasureBoxVnumsCount = len(treasureBoxVnums) - 1
		
		while i < slot_count:
			self.slotImages[i] = ui.ImageBox()
			self.slotImages[i].SetParent(self.Board)
			self.slotImages[i].SetPosition(width,height)
			self.slotImages[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			self.slotImages[i].Show()
			
			
			self.otherBoxSlots[i] = ui.GridSlotWindow()  
			self.otherBoxSlots[i].SetParent(self.slotImages[i])  
			self.otherBoxSlots[i].ArrangeSlot(i,1,1,32,32,0,0)  
			self.otherBoxSlots[i].SetPosition(0, 0)  
			self.otherBoxSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
			self.otherBoxSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
			self.otherBoxSlots[i].SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
			self.otherBoxSlots[i].SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
			self.otherBoxSlots[i].Show()				
			
			
			if treasureBoxVnumsCount >= i:
				self.otherBoxSlots[i].SetItemSlot(i, treasureBoxVnums[i], 0)
			

			
		
			width = width + 35
			count_line = count_line + 1
			
			if count_line == next_line:
				width = 30
				height = height + 32
				count_line = 0
			
			i = i + 1
		
		
		
		
	def OpenBOXCMD(self):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Scheiß Buguser...!!!")
			return
		if self.treasureBoxVnum == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Bitte lege eine Truhe in den Roten Slot.")	
			return
			
		if settinginfo.OpenBoxQID == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Kein QuestIndex gefunden!")	
			return			

		constInfo.INPUT_CMD = "OPEN#" + str(self.treasureBoxVnum) + "#" + str(self.treasureBoxSlot) + "#"
		event.QuestButtonClick(settinginfo.OpenBoxQID)			
		self.OpenBoxSlot.ClearSlot(50)
		self.OpenBoxSlot.SetItemSlot(50, 0, 0)
		self.OpenBoxSlot.RefreshSlot()	
		self.treasureBoxVnum = 0
		self.treasureBoxSlot = 0	
		self.OpenBoxRedSlotImg.LoadImage("images_jewel/red_slot.tga")	
		
		
	def ShowToolTip(self,slot):
		self.itemtooltip.ClearToolTip()
		if slot < 50:
			treasureBoxVnums = settinginfo.treasure_chest_vnum
			treasureBoxVnumsCount = len(treasureBoxVnums) - 1
			if treasureBoxVnumsCount >= slot:
				self.itemtooltip.AddItemData(treasureBoxVnums[slot], [0, 0, 0, 0, 0, 0])
				self.itemtooltip.ShowToolTip()
		else:
			if self.treasureBoxVnum != 0:
				self.itemtooltip.AddItemData(self.treasureBoxVnum, [0, 0, 0, 0, 0, 0])
				self.itemtooltip.ShowToolTip()
		
	
	
		
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()
		
		
	def add_slot(self,slot):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Scheiß Buguser...!!!")
			return
			
		isAttached = mouseModule.mouseController.isAttached()  
		if isAttached:  
			attachedSlotType = mouseModule.mouseController.GetAttachedType()  
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()  
			mouseModule.mouseController.DeattachObject()  
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY != attachedSlotType:  
				return  
			itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(attachedSlotPos)	

			if slot == 50:
				if itemvnum in settinginfo.treasure_chest_vnum:
					
					self.treasureBoxVnum = itemvnum
					self.treasureBoxSlot = attachedSlotPos		
					
					self.OpenBoxSlot.SetItemSlot(50, itemvnum, fgGHGjjFHJghjfFG1545gGG.GetItemCount(self.treasureBoxSlot))

					self.OpenBoxRedSlotImg.LoadImage("images_jewel/green_slot.tga")
					
		
	def del_slot(self,slot):
		if slot == 50:
			self.OpenBoxSlot.ClearSlot(50)
			self.OpenBoxSlot.SetItemSlot(50, 0, 0)
			self.OpenBoxSlot.RefreshSlot()	

			self.treasureBoxVnum = 0
			self.treasureBoxSlot = 0	
			
			self.OpenBoxRedSlotImg.LoadImage("images_jewel/red_slot.tga")
		
		
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE			
		
		
#TreasureChestBoard().Show()