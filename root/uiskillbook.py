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
import localeInfo


class SkillBookBoard(ui.ScriptWindow):
	slotImages = {}
	radiaButtons = {}
	skillBookSlots = {}
	
	YamatoWidth = 15
	YamatoHeight = 30
	
	selActionMode = 1 # Lesen
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		settinginfo.SkillBookStorageOpen = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()

		
	def LoadUI(self):
		settinginfo.SkillBookStorageOpen = 1
		self.Board = ui.BoardWithRoofBar()
		self.Board.SetSize(266, 400)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.AddFlag("attach")
		# self.Board.SetTitleName("Fertigkeitsbücher-Lager")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()

		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()	
		
		

		
		self.ReadButtonUp = ui.Button()
		self.ReadButtonUp.SetParent(self.Board)
		self.ReadButtonUp.SetPosition(16 + self.YamatoWidth,33 + self.YamatoHeight)
		self.ReadButtonUp.SetText("")
		self.ReadButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.ReadButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.ReadButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.ReadButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 1)
		self.ReadButtonUp.Hide()
		
		self.ReadButtonDown = ui.Button()
		self.ReadButtonDown.SetParent(self.Board)
		self.ReadButtonDown.SetPosition(16 + self.YamatoWidth,33 + self.YamatoHeight)
		self.ReadButtonDown.SetText("")
		self.ReadButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.ReadButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.ReadButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.ReadButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 1)
		self.ReadButtonDown.Show()
		
		self.TakeButtonUp = ui.Button()
		self.TakeButtonUp.SetParent(self.Board)
		self.TakeButtonUp.SetPosition(95 + self.YamatoWidth,33 + self.YamatoHeight)
		self.TakeButtonUp.SetText("")
		self.TakeButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.TakeButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.TakeButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.TakeButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 2)
		self.TakeButtonUp.Show()	
		
		self.TakeButtonDown = ui.Button()
		self.TakeButtonDown.SetParent(self.Board)
		self.TakeButtonDown.SetPosition(95 + self.YamatoWidth,33 + self.YamatoHeight)
		self.TakeButtonDown.SetText("")
		self.TakeButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.TakeButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.TakeButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.TakeButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 2)
		self.TakeButtonDown.Hide()
		
		self.SellButtonUp = ui.Button()
		self.SellButtonUp.SetParent(self.Board)
		self.SellButtonUp.SetPosition(174 + self.YamatoWidth,33 + self.YamatoHeight)
		self.SellButtonUp.SetText("")
		self.SellButtonUp.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.SellButtonUp.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.SellButtonUp.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.SellButtonUp.SetEvent(ui.__mem_func__(self.ChangeActionMode), 3)
		self.SellButtonUp.Show()	
		
		self.SellButtonDown = ui.Button()
		self.SellButtonDown.SetParent(self.Board)
		self.SellButtonDown.SetPosition(174 + self.YamatoWidth,33 + self.YamatoHeight)
		self.SellButtonDown.SetText("")
		self.SellButtonDown.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.SellButtonDown.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.SellButtonDown.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.SellButtonDown.SetEvent(ui.__mem_func__(self.ChangeActionMode), 3)
		self.SellButtonDown.Hide()
		
		self.ButtonTextLines = ui.TextLine()
		self.ButtonTextLines.SetParent(self.Board)
		self.ButtonTextLines.SetPosition(30 + self.YamatoWidth + 15,36 + self.YamatoHeight)
		self.ButtonTextLines.SetText(localeInfo.SKILLBOOK_STORAGE_TITLE)
		self.ButtonTextLines.Show()	


		
		self.WarriorTitleBar = ui.HorizontalBar()
		self.WarriorTitleBar.SetParent(self.Board)
		self.WarriorTitleBar.Create(235)
		self.WarriorTitleBar.SetPosition(16 + self.YamatoWidth,55 + self.YamatoHeight)
		self.WarriorTitleBar.Show()
		
		self.WarriorTitle = ui.TextLine()
		self.WarriorTitle.SetParent(self.Board)
		self.WarriorTitle.SetPosition(30 + self.YamatoWidth,56 + self.YamatoHeight)
		self.WarriorTitle.SetText(localeInfo.SKILLBOOK_STORAGE_WARRIOR)
		self.WarriorTitle.Show()

			
		self.NinjaTitleBar = ui.HorizontalBar()
		self.NinjaTitleBar.SetParent(self.Board)
		self.NinjaTitleBar.Create(235)
		self.NinjaTitleBar.SetPosition(16 + self.YamatoWidth,144 + self.YamatoHeight)
		self.NinjaTitleBar.Show()
		
		self.NinjaTitle = ui.TextLine()
		self.NinjaTitle.SetParent(self.Board)
		self.NinjaTitle.SetPosition(30 + self.YamatoWidth,145 + self.YamatoHeight)
		self.NinjaTitle.SetText(localeInfo.SKILLBOOK_STORAGE_NINJA)
		self.NinjaTitle.Show()
		
		self.SuraTitleBar = ui.HorizontalBar()
		self.SuraTitleBar.SetParent(self.Board)
		self.SuraTitleBar.Create(235)
		self.SuraTitleBar.SetPosition(16 + self.YamatoWidth,233 + self.YamatoHeight)
		self.SuraTitleBar.Show()
		
		self.SuraTitle = ui.TextLine()
		self.SuraTitle.SetParent(self.Board)
		self.SuraTitle.SetPosition(30 + self.YamatoWidth,234 + self.YamatoHeight)
		self.SuraTitle.SetText(localeInfo.SKILLBOOK_STORAGE_SURA)
		self.SuraTitle.Show()
		
		self.ShamanTitleBar = ui.HorizontalBar()
		self.ShamanTitleBar.SetParent(self.Board)
		self.ShamanTitleBar.Create(235)
		self.ShamanTitleBar.SetPosition(16 + self.YamatoWidth,322 + self.YamatoHeight)
		self.ShamanTitleBar.Show()
		
		self.ShamanTitle = ui.TextLine()
		self.ShamanTitle.SetParent(self.Board)
		self.ShamanTitle.SetPosition(30 + self.YamatoWidth,323 + self.YamatoHeight)
		self.ShamanTitle.SetText(localeInfo.SKILLBOOK_STORAGE_SHAMAN)
		self.ShamanTitle.Show()		
		
		i = 0
		slot_count = 48
		
		
		inner_line = 0
		height_jump = 6
		
		height_big_jump = 0
		outer_line = 0
		height_pos = [75+ self.YamatoHeight,164+ self.YamatoHeight,253+ self.YamatoHeight,342+ self.YamatoHeight,0]
		
		height = height_pos[0]
		
		standart_width = 38 + self.YamatoWidth
		width = standart_width

		while i < slot_count:
			self.slotImages[i] = ui.ImageBox()
			self.slotImages[i].SetParent(self.Board)
			self.slotImages[i].SetPosition(width,height)
			self.slotImages[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			self.slotImages[i].Show()	
			
			self.skillBookSlots[i] = ui.GridSlotWindow()  
			self.skillBookSlots[i].SetParent(self.slotImages[i])  
			self.skillBookSlots[i].ArrangeSlot(i,1,1,32,32,0,0)  
			self.skillBookSlots[i].SetPosition(0, 0)  
			self.skillBookSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
			self.skillBookSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
			self.skillBookSlots[i].SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
			self.skillBookSlots[i].SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
			self.skillBookSlots[i].SAFE_SetButtonEvent("RIGHT", "ALWAYS", self.del_slot)
			self.skillBookSlots[i].Show()			
			
			slot = i + 1
			if settinginfo.SkillBookItemVnumList[slot] != 0:
				self.skillBookSlots[i].SetItemSlot(i, settinginfo.SkillBookItemVnumList[slot], 0)
			
			
			width = width + 32
			inner_line = inner_line + 1
			height_big_jump = height_big_jump + 1
			
			
			
			if inner_line == height_jump:
				height = height + 32
				width = standart_width
				
			if height_big_jump == 12:
				width = standart_width
				outer_line = outer_line + 1
				if outer_line < 5:
					height = height_pos[outer_line]
				height_big_jump = 0
				inner_line = 0
			i = i + 1
		
			
	def ShowToolTip(self,slot):
		self.itemtooltip.ClearToolTip()
		slot = slot + 1
		if settinginfo.SkillBookItemVnumList[slot] != 0:
			self.itemtooltip.AddItemData(settinginfo.SkillBookItemVnumList[slot], [0, self.selActionMode, settinginfo.SkillBookGoldPrice])
			self.itemtooltip.ShowToolTip()		
	
		
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()
		
	def add_slot(self,slot):
		return
		
	def del_slot(self,slot):
		slot = slot + 1
		if settinginfo.SkillBookItemVnumList[slot] != 0:
			if settinginfo.OpenBoxQID == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO,localeInfo.SKILLBOOK_STORAGE_NO_QUEST_INDEX)	
				return					

			if settinginfo.SkillBookCount[slot] == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO,localeInfo.SKILLBOOK_STORAGE_NO_BOOK)	
				return						
			
			if self.selActionMode == 1:
				item.SelectItem(settinginfo.SkillBookItemVnumList[slot])
				constInfo.INPUT_CMD = "read#" + str(slot) + "#" + str(item.GetValue(0)) + "#"
				event.QuestButtonClick(settinginfo.SkillBookQID)				
				
			elif self.selActionMode == 2:
				constInfo.INPUT_CMD = "take#" + str(slot) + "#"
				event.QuestButtonClick(settinginfo.SkillBookQID)
					
			elif self.selActionMode == 3:
				constInfo.INPUT_CMD = "sell#" + str(slot) + "#"
				event.QuestButtonClick(settinginfo.SkillBookQID)						
				

	def ChangeActionMode(self,buttonIndex):
		if self.selActionMode == buttonIndex:
			return
			
		if buttonIndex == 1:
			self.ReadButtonDown.Show()
			self.ReadButtonUp.Hide()
			
			self.TakeButtonDown.Hide()
			self.TakeButtonUp.Show()
				
			self.SellButtonDown.Hide()
			self.SellButtonUp.Show()		
		
		elif buttonIndex == 2:
			self.ReadButtonDown.Hide()
			self.ReadButtonUp.Show()
			
			self.TakeButtonDown.Show()
			self.TakeButtonUp.Hide()
				
			self.SellButtonDown.Hide()
			self.SellButtonUp.Show()		
		
		elif buttonIndex == 3:
			self.ReadButtonDown.Hide()
			self.ReadButtonUp.Show()
			
			self.TakeButtonDown.Hide()
			self.TakeButtonUp.Show()
				
			self.SellButtonDown.Show()
			self.SellButtonUp.Hide()		
		
		self.selActionMode = buttonIndex

		
	def OnUpdate(self):
		i = 0
		slot_count = 48
		while i < slot_count:	
			slot = i + 1
			self.skillBookSlots[i].SetItemSlot(i, settinginfo.SkillBookItemVnumList[slot], settinginfo.SkillBookCount[slot])
			self.skillBookSlots[i].SetCoverButton(i)
			# self.skillBookSlots[i].EnableCoverButton(i)			
			if settinginfo.SkillBookCount[slot] <= 0:
				self.skillBookSlots[i].DisableCoverButton(i)
			else:
				self.skillBookSlots[i].EnableCoverButton(i)
			self.skillBookSlots[i].RefreshSlot()
			i = i + 1
		
		
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE	
	
		
#SkillBookBoard().Show()