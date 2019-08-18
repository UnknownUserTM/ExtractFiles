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

FORGE_GUIDE_PVM = 0
FORGE_GUIDE_PVP = 1

board_count = 3
Cat = 0
StufenSlots = [
	## SlotStart, SlotEnd, Stufe
	## Board 1
	[0,2,0],
	[3,5,1],
	[6,8,2],
	[9,11,3],
	[12,14,4],
	[15,17,5],
	[18,20,6],
	[21,23,7],
	[24,26,8],
	## Board 2
	[27,29,0],
	[30,32,1],
	[33,35,2],
	[36,38,3],
	[39,41,4],
	[42,44,5],
	[45,47,6],
	[48,50,7],
	[51,53,8],
	## Board 3
	[54,56,0],
	[57,59,1],
	[60,62,2],
	[63,65,3],
	[66,68,4],
	[69,71,5],
	[72,74,6],
	[75,77,7],
	[78,80,8]
]
class UppWikiBoard(ui.ScriptWindow):
	ButtonTitles = {}
	itemTypeButtons = {}
	itemBoards = {}
	itemMainSlots = {}
	Trennstriche = {}
	UppStufenHeadline = {}
	UppItemsSlots = {}
	Selitems = {}
	Category = 0
	ForgeGuide = 0
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		# self.Hide()
		self.LoadUI()

	def __del__(self):
		settinginfo.SchmiedehandbuchOpen = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()

	def LoadUI(self):
		settinginfo.SchmiedehandbuchOpen = 1
		self.Board = ui.BoardWithRoofBar()
		self.Board.SetSize(700, 450)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		# self.Board.SetTitleName("Schmiedehandbuch")
		self.Board.SetCloseEvent(self.Open)
		self.Board.Hide()
		############################################################
		## Navigation
		self.NavBoard = ui.Board()
		self.NavBoard.SetParent(self.Board)
		self.NavBoard.SetPosition(15,65)
		self.NavBoard.SetSize(210,485)
		self.NavBoard.HideBottom()
		self.NavBoard.Show()
		
		self.ForgeGuideBoard = ui.Board()
		self.ForgeGuideBoard.SetParent(self.Board)
		self.ForgeGuideBoard.SetPosition(15,65)
		self.ForgeGuideBoard.SetSize(210,485)
		self.ForgeGuideBoard.HideBottom()
		self.ForgeGuideBoard.Show()
		
		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()			
		i = 0
		x = 12
		button_x = 19
		while i < len(settinginfo.SchmiedeHandBuchInfos[0]):
			self.itemTypeButtons[i] = ui.Button()
			self.itemTypeButtons[i].SetParent(self.NavBoard)
			self.itemTypeButtons[i].SetPosition(25,x)
			self.itemTypeButtons[i].SetText("")
			self.itemTypeButtons[i].SetUpVisual("yamato_helpboard/wide_button_n.tga")  
			self.itemTypeButtons[i].SetOverVisual("yamato_helpboard/wide_button_h.tga")  
			self.itemTypeButtons[i].SetDownVisual("yamato_helpboard/wide_button_p.tga")	
			self.itemTypeButtons[i].SetDisableVisual("yamato_helpboard/wide_button_d.tga")	
			self.itemTypeButtons[i].SetEvent(ui.__mem_func__(self.LoadCategory), i)
			self.itemTypeButtons[i].Show()
			self.ButtonTitles[i] = ui.TextLine()
			self.ButtonTitles[i].SetParent(self.NavBoard)
			self.ButtonTitles[i].SetPosition(105,button_x)
			self.ButtonTitles[i].SetHorizontalAlignCenter()
			self.ButtonTitles[i].SetText(settinginfo.SchmiedeHandBuchInfos[0][i][0][0])
			self.ButtonTitles[i].Show()
			
			button_x = button_x + 30
			i = i + 1
			x = x + 30
			
		self.ForgeGuideBoard = ui.Board()
		self.ForgeGuideBoard.SetParent(self.Board)
		self.ForgeGuideBoard.SetPosition(15,x + 65)
		self.ForgeGuideBoard.SetSize(210,80)
		self.ForgeGuideBoard.HideBottom()
		self.ForgeGuideBoard.Show()
		
		
		self.ForgeGuidePVM = ui.Button()
		self.ForgeGuidePVM.SetParent(self.ForgeGuideBoard)
		self.ForgeGuidePVM.SetPosition(25,15)
		self.ForgeGuidePVM.SetUpVisual("yamato_helpboard/wide_button_n.tga")  
		self.ForgeGuidePVM.SetOverVisual("yamato_helpboard/wide_button_h.tga")  
		self.ForgeGuidePVM.SetDownVisual("yamato_helpboard/wide_button_p.tga")	
		self.ForgeGuidePVM.SetDisableVisual("yamato_helpboard/wide_button_d.tga")	
		self.ForgeGuidePVM.SetEvent(ui.__mem_func__(self.LoadForgeGuide), 0)
		self.ForgeGuidePVM.Show()

		self.ForgeGuidePVP = ui.Button()
		self.ForgeGuidePVP.SetParent(self.ForgeGuideBoard)
		self.ForgeGuidePVP.SetPosition(25,45)
		self.ForgeGuidePVP.SetUpVisual("yamato_helpboard/wide_button_n.tga")  
		self.ForgeGuidePVP.SetOverVisual("yamato_helpboard/wide_button_h.tga")  
		self.ForgeGuidePVP.SetDownVisual("yamato_helpboard/wide_button_p.tga")	
		self.ForgeGuidePVP.SetDisableVisual("yamato_helpboard/wide_button_d.tga")	
		self.ForgeGuidePVP.SetEvent(ui.__mem_func__(self.LoadForgeGuide), 1)
		self.ForgeGuidePVP.Show()


		self.ForgeGuidePVMTextLine = ui.TextLine()
		self.ForgeGuidePVMTextLine.SetParent(self.ForgeGuideBoard)
		self.ForgeGuidePVMTextLine.SetPosition(105,15 + 6)
		self.ForgeGuidePVMTextLine.SetHorizontalAlignCenter()
		self.ForgeGuidePVMTextLine.SetText("PVM")
		self.ForgeGuidePVMTextLine.Show()
		
		self.ForgeGuidePVPTextLine = ui.TextLine()
		self.ForgeGuidePVPTextLine.SetParent(self.ForgeGuideBoard)
		self.ForgeGuidePVPTextLine.SetPosition(105,45 + 6)
		self.ForgeGuidePVPTextLine.SetHorizontalAlignCenter()
		self.ForgeGuidePVPTextLine.SetText("PVP")
		self.ForgeGuidePVPTextLine.Show()
		
		############################################################
		## Content	
		self.ForgeGuideTitleBoard = ui.Board()
		self.ForgeGuideTitleBoard.SetParent(self.Board)
		self.ForgeGuideTitleBoard.SetPosition(205,65)
		self.ForgeGuideTitleBoard.SetSize(515,80)
		self.ForgeGuideTitleBoard.HideBottom()
		self.ForgeGuideTitleBoard.Show()
		
		self.ForgeGuideBGBoard = ui.Board()
		self.ForgeGuideBGBoard.SetParent(self.Board)
		self.ForgeGuideBGBoard.SetPosition(205,110)
		self.ForgeGuideBGBoard.SetSize(515,440)
		self.ForgeGuideBGBoard.HideBottom()
		self.ForgeGuideBGBoard.Show()
		
		self.ForgeGuideTitleTextLine = ui.TextLine()
		self.ForgeGuideTitleTextLine.SetParent(self.ForgeGuideTitleBoard)
		self.ForgeGuideTitleTextLine.SetPosition(257,20)
		self.ForgeGuideTitleTextLine.SetHorizontalAlignCenter()
		self.ForgeGuideTitleTextLine.SetText("Schmiedehandbuch - PVM")
		self.ForgeGuideTitleTextLine.SetPackedFontColor(0xffd8a055)
		self.ForgeGuideTitleTextLine.Show()
		
		i = 0
		x = 120
		trennstrichCounter = 0
		uppitemslots = 0
		while i < 3:
			self.itemBoards[i] = ui.ImageBox()
			self.itemBoards[i].SetParent(self.Board)
			self.itemBoards[i].SetPosition(240-15,x)
			self.itemBoards[i].LoadImage("yamato_forgeguide/forge_guide_bg.tga")
			self.itemBoards[i].Show()
			
			self.itemMainSlots[i] = ui.GridSlotWindow()  
			self.itemMainSlots[i].SetParent(self.itemBoards[i])  
			self.itemMainSlots[i].ArrangeSlot(i,1,1,32,96,0,0)  
			self.itemMainSlots[i].SetPosition(8, 20)  
			self.itemMainSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTipEmpty))  
			self.itemMainSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTipEmpty))  
			self.itemMainSlots[i].SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slotEmpty))  
			self.itemMainSlots[i].SetSelectItemSlotEvent(ui.__mem_func__(self.del_slotEmpty))  
			self.itemMainSlots[i].Show()		
			
			trenn_y = 40
			for t in xrange(10):
				self.Trennstriche[trennstrichCounter] = ui.ImageBox()
				self.Trennstriche[trennstrichCounter].SetParent(self.itemBoards[i])
				self.Trennstriche[trennstrichCounter].SetPosition(trenn_y,20)
				self.Trennstriche[trennstrichCounter].LoadImage("yamato_forgeguide/split.tga")
				self.Trennstriche[trennstrichCounter].Show()
				trenn_y = trenn_y + 45
				trennstrichCounter = trennstrichCounter + 1
			
			self.UppStufenHeadline[i] = ui.TextLine()
			self.UppStufenHeadline[i].SetParent(self.itemBoards[i])
			self.UppStufenHeadline[i].SetPosition(45,5)
			self.UppStufenHeadline[i].SetText("   +1            +2           +3           +4           +5           +6           +7           +8           +9")
			self.UppStufenHeadline[i].Show()
			y_slot = 47
			for t in xrange(9):
				x_slot = 20
				for z in xrange(3):
					self.UppItemsSlots[uppitemslots] = ui.GridSlotWindow()  
					self.UppItemsSlots[uppitemslots].SetParent(self.itemBoards[i])  
					self.UppItemsSlots[uppitemslots].ArrangeSlot(uppitemslots,1,1,32,32,0,0)  
					self.UppItemsSlots[uppitemslots].SetPosition(y_slot, x_slot)  
					self.UppItemsSlots[uppitemslots].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
					self.UppItemsSlots[uppitemslots].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
					self.UppItemsSlots[uppitemslots].SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
					self.UppItemsSlots[uppitemslots].SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
					self.UppItemsSlots[uppitemslots].Show()		
					uppitemslots = uppitemslots + 1
					x_slot = x_slot + 32
					if z == 2:
						y_slot = y_slot +45
						
			i = i + 1
			x = x + 132

		self.scrollbar = ui.ScrollBar()
		self.scrollbar.SetParent(self.Board)
		self.scrollbar.SetScrollBarSize(395)
		self.scrollbar.SetPosition(675 + 10, 120)
		self.scrollbar.SetMiddleBarSize(float(board_count) / float(len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1])))
		self.scrollbar.SetScrollEvent(self.__OnScroll)
		self.scrollbar.Show()
		self.LoadForgeGuide(0)
		self.LoadCategory(0)
	
	def LoadForgeGuide(self,idx):
		if idx == FORGE_GUIDE_PVM:
			self.ForgeGuide = FORGE_GUIDE_PVM
			self.ForgeGuideTitleTextLine.SetText(localeInfo.FORGE_GUIDE_PVM)
			self.ForgeGuidePVM.Disable()		
			self.ForgeGuidePVP.Enable()		
		else:
			self.ForgeGuide = FORGE_GUIDE_PVP	
			self.ForgeGuideTitleTextLine.SetText(localeInfo.FORGE_GUIDE_PVP)
			self.ForgeGuidePVM.Enable()		
			self.ForgeGuidePVP.Disable()			

		self.LoadCategory(0)
		
	def ClearSlots(self):
		i = 0
		while i < 81:
			self.UppItemsSlots[i].SetItemSlot(i,0,0)
			i = i + 1
		
	def __OnScroll(self):
		pos = int(self.scrollbar.GetPos() * (len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1]) - board_count)) ##Aktuelle Position der Scrollbar
		self.ClearSlots()
		start_slot = 0
		for i in xrange(board_count):
			realPos = i + pos
			self.itemMainSlots[i].SetItemSlot(i, settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][0][0], 0)
			for stufen in xrange(9):
				for uppitems in xrange(3):
					if uppitems+1 <= len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][stufen+1]):
						self.UppItemsSlots[start_slot].SetItemSlot(start_slot, settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][stufen+1][uppitems][0], settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][stufen+1][uppitems][1])
						self.Selitems[start_slot] = realPos
					start_slot = start_slot +1
		
	def ShowToolTip(self,slot):
		pos = int(self.scrollbar.GetPos() * (len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1]) - board_count))
		realPos = slot + pos
		self.itemtooltip.ClearToolTip()
		self.itemtooltip.AddItemData(int(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][self.Selitems[slot]][self.getStufebySlot(slot)+1][self.getUppitemSlotbySlot(slot)][0]), [40000, 0, 0, 0, 0, 0])
		self.itemtooltip.ShowToolTip()
		
	def getStufebySlot(self,slot):
		i = 0
		while i < len(StufenSlots):
			if slot >= StufenSlots[i][0] and slot <= StufenSlots[i][1]:
				return StufenSlots[i][2]
			i = i + 1
			
	def getUppitemSlotbySlot(self,slot):
		i = 0
		while i < len(StufenSlots):
			for t in xrange(3):
				if slot == (StufenSlots[i][0]+t):
					return t
			i = i + 1
		
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()
		
	def add_slot(self,slot):
		return

	def del_slot(self,slot):
		return
		
	def test_set_pos(self):
		self.scrollbar.SetPos(0)
		
	def LoadCategory(self,id):
		self.Category = id
		# self.Board.SetTitleName("Schmiedehandbuch ~ " + str(settinginfo.SchmiedeHandBuchInfos[id][0][0]))
		self.ClearSlots()
		self.scrollbar.SetPos(0)
		self.scrollbar.SetMiddleBarSize(float(board_count) / float(len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1])))
		pos = int(self.scrollbar.GetPos() * (len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1]) - board_count))
		start_slot = 0
		for i in xrange(board_count):
			realPos = i + pos
			self.itemMainSlots[i].SetItemSlot(i, settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][0][0], 0)
			for stufen in xrange(9):
				for uppitems in xrange(3):
					if uppitems+1 <= len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][stufen+1]):
						self.UppItemsSlots[start_slot].SetItemSlot(start_slot, settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][stufen+1][uppitems][0], settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][stufen+1][uppitems][1])
						self.Selitems[start_slot] = realPos
					start_slot = start_slot +1		
		
		for i in xrange(len(self.itemTypeButtons)):
			if id == i:
				self.itemTypeButtons[i].Disable()
			else:
				self.itemTypeButtons[i].Enable()
		
		
	def add_slotEmpty(self,slot):
		return
	def del_slotEmpty(self,slot):
		return
		
	def ShowToolTipEmpty(self,slot):
		pos = int(self.scrollbar.GetPos() * (len(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1]) - board_count))
		realPos = slot + pos
		self.itemtooltip.ClearToolTip()
		self.itemtooltip.AddItemData(int(settinginfo.SchmiedeHandBuchInfos[self.ForgeGuide][self.Category][1][realPos][0][0]), [0, 0, 0, 0, 0, 0])
		self.itemtooltip.ShowToolTip()	
		
	def HideToolTipEmpty(self):
		self.itemtooltip.HideToolTip()
		
	def Open(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
	
	
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE		
