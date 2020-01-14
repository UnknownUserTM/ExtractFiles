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
from uitooltip import ItemToolTip
import localeInfo
import exterminatus

WEAR_NAMES = ItemToolTip.WEAR_NAMES
AFFECT_DICT = ItemToolTip.AFFECT_DICT

class SwitchBoard(ui.ScriptWindow):
	
	pageIndex		= 0
	counter			= 0
	itemSlots 		= [0,0,0,0,0]
	itemSlotStatus 	= [0,0,0,0,0]
	itemAttrValues 	= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	itemBoniValues 	= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	# itemDevType 	= 1
	alternatePage	= 0  # 0:Normal, 1:Alternate
	itemAttrValuesA	= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	itemBoniValuesA	= [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]		
	
	itemTempBoniList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	itemTempBonusValueSlot = 0
	itemTempBonusValueMax = 0
	
	speedIndex 		= 1
	speedValue		= 80
	bonusSlotBar 	= {}
	bonusTextLine 	= {}
	bonusButton  	= {}
	bonusButtonDelete = {}
	
	itemSlotIMG		= {}
	
	pageButtons		= {}
	
	def __init__(self, wndMinimap):
		ui.ScriptWindow.__init__(self)
		self.wndMinimap = wndMinimap
		self.SwitchLog = SwitchLog()
		self.SwitchLog.HideSwitchLogs()
		self.LoadUI()

	def __del__(self):
		self.SwitchLog.Destroy()
		self.wndMinimap.SwitchBotButtonInactive.Show()
		self.wndMinimap.SwitchBotButton.Hide()
		settinginfo.switchbot = 0
		settinginfo.switchbot_Slots = [-1,-1,-1,-1,-1]
		settinginfo.switchbot_switch_count = [0,0,0,0,0]
		self.ClearLists()
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		
	def ClearLists(self):
		for i in xrange(5):
			self.itemSlots[i] = 0
			self.itemSlotStatus[i] = 0
			for a in xrange(5):
				self.itemAttrValues[i][a] = 0
				self.itemBoniValues[i][a] = 0
				self.itemAttrValuesA[i][a] = 0
				self.itemBoniValuesA[i][a] = 0		
				
	def LoadUI(self):
		settinginfo.switchbot = 1
		settinginfo.switchbot_minimize = 0

		self.Board = ui.BoardWithRoofBar()
		self.Board.SetSize(800-9, 330-30-9-5)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		# self.Board.SetTitleName("Switchbot - [Seite 1]")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()
		
		self.qmark = exterminatus.HelpButtonWindow()
		self.qmark.SetParent(self.Board)
		self.qmark.SetPosition(20,25)
		self.qmark.Show()
		
		self.MinimizeBotButton = ui.Button()
		self.MinimizeBotButton.SetParent(self.Board)
		self.MinimizeBotButton.SetPosition(60,10+10)
		self.MinimizeBotButton.SetText("")
		self.MinimizeBotButton.SetUpVisual("yamato_mm/zout_n.tga")
		self.MinimizeBotButton.SetOverVisual("yamato_mm/zout_h.tga")
		self.MinimizeBotButton.SetDownVisual("yamato_mm/zout_p.tga")
		self.MinimizeBotButton.SetEvent(self.DoMinimize)
		self.MinimizeBotButton.SetWindowHorizontalAlignRight()
		self.MinimizeBotButton.Show()
		
		self.BonusSelectorBG = ui.Bar()
		self.BonusSelectorBG.SetParent(self.Board)
		self.BonusSelectorBG.SetPosition(16+9,60+30)
		self.BonusSelectorBG.SetSize(315,255)
		self.BonusSelectorBG.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.BonusSelectorBG.Show()
		
		self.SelectBonusTitleBar = ui.HorizontalBar()
		self.SelectBonusTitleBar.SetParent(self.Board)
		self.SelectBonusTitleBar.Create(315)
		self.SelectBonusTitleBar.SetPosition(16+9,60+30)
		self.SelectBonusTitleBar.Show()
		
		self.BoniList = ui.ListBox()
		self.BoniList.SetParent(self.Board)
		self.BoniList.SetSize(297, 200)
		self.BoniList.SetPosition(15+9, 83+30)
		self.BoniList.SetEvent(ui.__mem_func__(self.__OnSelectBonus))
		self.BoniList.Show()

		self.BoniListScrollBar = ui.ScrollBar()
		self.BoniListScrollBar.SetParent(self.Board)
		self.BoniListScrollBar.SetPosition(315+9, 83+30)
		self.BoniListScrollBar.SetScrollBarSize(200)
		self.BoniListScrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScrollBoniList))
		self.BoniListScrollBar.Show()
		
		self.BoniValueSlotBar = ui.SlotBar()
		self.BoniValueSlotBar.SetParent(self.Board)
		self.BoniValueSlotBar.SetPosition(20+9,285+30)
		self.BoniValueSlotBar.SetSize(305,19)
		self.BoniValueSlotBar.Hide()
		
		self.BonusValueTextLine = ui.TextLine()
		self.BonusValueTextLine.SetParent(self.BoniValueSlotBar)
		self.BonusValueTextLine.SetPosition(152,3)
		self.BonusValueTextLine.SetText("1000")
		self.BonusValueTextLine.SetHorizontalAlignCenter()
		self.BonusValueTextLine.Show()
		
		self.BonusValueDownButton = ui.Button()
		self.BonusValueDownButton.SetParent(self.BoniValueSlotBar)
		self.BonusValueDownButton.SetPosition(3,3)
		self.BonusValueDownButton.SetText("")
		self.BonusValueDownButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_minus_up.sub")
		self.BonusValueDownButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_minus_over.sub")
		self.BonusValueDownButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_minus_down.sub")
		self.BonusValueDownButton.SetEvent(self.BonusValueDown)
		self.BonusValueDownButton.SetWindowHorizontalAlignLeft()
		self.BonusValueDownButton.Show()	
		
		self.BonusValueUpButton = ui.Button()
		self.BonusValueUpButton.SetParent(self.BoniValueSlotBar)
		self.BonusValueUpButton.SetPosition(15,3)
		self.BonusValueUpButton.SetText("")
		self.BonusValueUpButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_plus_up.sub")
		self.BonusValueUpButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_plus_over.sub")
		self.BonusValueUpButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_plus_down.sub")
		self.BonusValueUpButton.SetEvent(self.BonusValueUp)
		self.BonusValueUpButton.SetWindowHorizontalAlignRight()
		self.BonusValueUpButton.Show()	

		self.BonusOverviewBG = ui.Bar()
		self.BonusOverviewBG.SetParent(self.Board)
		self.BonusOverviewBG.SetPosition(336+9,60+30)
		self.BonusOverviewBG.SetSize(315,255)
		self.BonusOverviewBG.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.BonusOverviewBG.Show()
		
		self.BonusOverviewTitleBar = ui.HorizontalBar()
		self.BonusOverviewTitleBar.SetParent(self.Board)
		self.BonusOverviewTitleBar.Create(315)
		self.BonusOverviewTitleBar.SetPosition(336+9,60+30)
		self.BonusOverviewTitleBar.Show()

		i = 0
		max_boni = 5
		height = 30
		width = 10
		while i < max_boni:
			self.bonusSlotBar[i] = ui.SlotBar()
			self.bonusSlotBar[i].SetParent(self.BonusOverviewBG)
			self.bonusSlotBar[i].SetPosition(width,height)
			self.bonusSlotBar[i].SetSize(295,19)
			self.bonusSlotBar[i].Show()		

			self.bonusTextLine[i] = ui.TextLine()
			self.bonusTextLine[i].SetParent(self.bonusSlotBar[i])
			self.bonusTextLine[i].SetPosition(5,3)
			self.bonusTextLine[i].SetText("(leer)")
			self.bonusTextLine[i].SetHorizontalAlignLeft()
			self.bonusTextLine[i].Show()	
			
			self.bonusButton[i] = ui.Button()
			self.bonusButton[i].SetParent(self.bonusSlotBar[i])
			self.bonusButton[i].SetPosition(30,3)
			self.bonusButton[i].SetText("")
			self.bonusButton[i].SetUpVisual("d:/ymir work/ui/game/windows/btn_plus_up.sub")
			self.bonusButton[i].SetOverVisual("d:/ymir work/ui/game/windows/btn_plus_over.sub")
			self.bonusButton[i].SetDownVisual("d:/ymir work/ui/game/windows/btn_plus_down.sub")
			self.bonusButton[i].SetWindowHorizontalAlignRight()
			self.bonusButton[i].SetEvent(ui.__mem_func__(self.LoadBonus), i)
			self.bonusButton[i].Show()

			self.bonusButtonDelete[i] = ui.Button()
			self.bonusButtonDelete[i].SetParent(self.bonusSlotBar[i])
			self.bonusButtonDelete[i].SetPosition(15,3)
			self.bonusButtonDelete[i].SetText("")
			self.bonusButtonDelete[i].SetUpVisual("d:/ymir work/ui/game/windows/btn_minus_up.sub")
			self.bonusButtonDelete[i].SetOverVisual("d:/ymir work/ui/game/windows/btn_minus_over.sub")
			self.bonusButtonDelete[i].SetDownVisual("d:/ymir work/ui/game/windows/btn_minus_down.sub")
			self.bonusButtonDelete[i].SetWindowHorizontalAlignRight()
			self.bonusButtonDelete[i].SetEvent(ui.__mem_func__(self.DeleteBonus), i)
			self.bonusButtonDelete[i].Show()			
			height = height + 22
			i = i + 1


		self.alternateBonusButton = ui.ToggleButton()
		self.alternateBonusButton.SetParent(self.BonusOverviewBG)
		self.alternateBonusButton.SetPosition(96+5,140)
		self.alternateBonusButton.SetText("")
		self.alternateBonusButton.SetUpVisual("yamato_helpboard/normal_button_n.tga")
		self.alternateBonusButton.SetOverVisual("yamato_helpboard/normal_button_h.tga")
		self.alternateBonusButton.SetDownVisual("yamato_helpboard/normal_button_p.tga")
		self.alternateBonusButton.SetToggleDownEvent(self.SwitchBonusListDown)
		self.alternateBonusButton.SetToggleUpEvent(self.SwitchBonusListUp)
		self.alternateBonusButton.SetWindowHorizontalAlignRight()
		self.alternateBonusButton.Show()	

		self.alternateBonusButtonTextLine = ui.TextLine()
		self.alternateBonusButtonTextLine.SetParent(self.BonusOverviewBG)
		self.alternateBonusButtonTextLine.SetPosition(226,145)
		self.alternateBonusButtonTextLine.SetText(localeInfo.SWITCHBOT_UI_ALTERNATIVE_LIST_BUTTON)
		# self.alternateBonusButtonTextLine.SetHorizontalAlignRight()
		self.alternateBonusButtonTextLine.Show()

		self.saveBonusSetButton = ui.Button()
		self.saveBonusSetButton.SetParent(self.BonusOverviewBG)
		self.saveBonusSetButton.SetPosition(5,140)
		self.saveBonusSetButton.SetText("")
		self.saveBonusSetButton.SetUpVisual("yamato_helpboard/normal_button_n.tga")
		self.saveBonusSetButton.SetOverVisual("yamato_helpboard/normal_button_h.tga")
		self.saveBonusSetButton.SetDownVisual("yamato_helpboard/normal_button_p.tga")
		self.saveBonusSetButton.SetDisableVisual("yamato_helpboard/normal_button_d.tga")
		self.saveBonusSetButton.SetEvent(self.OpenBonusSaveDialog)
		self.saveBonusSetButton.Disable()	
		self.saveBonusSetButton.Show()	

		self.saveBonusSetButtonTextLine = ui.TextLine()
		self.saveBonusSetButtonTextLine.SetParent(self.BonusOverviewBG)
		self.saveBonusSetButtonTextLine.SetPosition(55,145)
		self.saveBonusSetButtonTextLine.SetText("Save")
		self.saveBonusSetButtonTextLine.SetHorizontalAlignCenter()
		self.saveBonusSetButtonTextLine.Show()
		
		self.loadBonusSetButton = ui.Button()
		self.loadBonusSetButton.SetParent(self.BonusOverviewBG)
		self.loadBonusSetButton.SetPosition(5 + 95,140)
		self.loadBonusSetButton.SetText("")
		self.loadBonusSetButton.SetUpVisual("yamato_helpboard/normal_button_n.tga")
		self.loadBonusSetButton.SetOverVisual("yamato_helpboard/normal_button_h.tga")
		self.loadBonusSetButton.SetDownVisual("yamato_helpboard/normal_button_p.tga")
		self.loadBonusSetButton.SetDisableVisual("yamato_helpboard/normal_button_d.tga")
		self.loadBonusSetButton.SetEvent(self.OpenBonusLoadDialog)
		self.loadBonusSetButton.Disable()	
		self.loadBonusSetButton.Show()	

		self.loadBonusSetButtonTextLine = ui.TextLine()
		self.loadBonusSetButtonTextLine.SetParent(self.BonusOverviewBG)
		self.loadBonusSetButtonTextLine.SetPosition(55 + 95,145)
		self.loadBonusSetButtonTextLine.SetText("Load")
		self.loadBonusSetButtonTextLine.SetHorizontalAlignCenter()
		self.loadBonusSetButtonTextLine.Show()
		
		# self.bonusInfoTextLine = ui.TextLine()
		# self.bonusInfoTextLine.SetParent(self.BonusOverviewBG)
		# self.bonusInfoTextLine.SetPosition(40-5,145)
		# self.bonusInfoTextLine.SetText(localeInfo.SWITCHBOT_UI_DESC)
		# # self.bonusInfoTextLine.SetHorizontalAlignCenter()
		# self.bonusInfoTextLine.Show()
			
		# self.bonusInfoTextLine = ui.TextLine()
		# self.bonusInfoTextLine.SetParent(self.BonusOverviewBG)
		# self.bonusInfoTextLine.SetPosition(165,145)
		# self.bonusInfoTextLine.SetText("Klicke auf den + Button um Boni hinzuzufügen.")
		# self.bonusInfoTextLine.SetHorizontalAlignCenter()
		# self.bonusInfoTextLine.Show()
		
		self.SplitLineDeco = ui.Line()
		self.SplitLineDeco.SetParent(self.BonusOverviewBG)
		self.SplitLineDeco.SetPosition(5, 170)
		self.SplitLineDeco.SetSize(305, 0)
		self.SplitLineDeco.SetColor(CTOA("ff777777"))
		self.SplitLineDeco.Show()
		
		self.BonusSwitcherBG = ui.Bar()
		self.BonusSwitcherBG.SetParent(self.BonusOverviewBG)
		self.BonusSwitcherBG.SetPosition(5,200)
		self.BonusSwitcherBG.SetSize(305,50)
		self.BonusSwitcherBG.SetColor(grp.GenerateColor(1.0, 0.0, 0.0, 0.2))
		self.BonusSwitcherBG.Show()
		
		self.BonusSwitcherStartButton = ui.Button()
		self.BonusSwitcherStartButton.SetParent(self.BonusSwitcherBG)
		self.BonusSwitcherStartButton.SetPosition(60+20-10,11)
		self.BonusSwitcherStartButton.SetText("")
		self.BonusSwitcherStartButton.SetUpVisual("yamato_helpboard/wide_button_n.tga")
		self.BonusSwitcherStartButton.SetOverVisual("yamato_helpboard/wide_button_h.tga")	
		self.BonusSwitcherStartButton.SetDownVisual("yamato_helpboard/wide_button_p.tga")	
		self.BonusSwitcherStartButton.SetEvent(self.Start)
		self.BonusSwitcherStartButton.Show()
		
		self.BonusSwitcherStartButtonText = ui.TextLine()
		self.BonusSwitcherStartButtonText.SetParent(self.BonusSwitcherBG)
		self.BonusSwitcherStartButtonText.SetPosition(153,18)
		self.BonusSwitcherStartButtonText.SetText(localeInfo.SWITCHBOT_UI_START_BUTTON)
		self.BonusSwitcherStartButtonText.SetHorizontalAlignCenter()
		self.BonusSwitcherStartButtonText.Show()
		
		# i = 0
		# max_boni = 5
		# height = 30
		# width = 10
		self.speedSlotBar = ui.SlotBar()
		self.speedSlotBar.SetParent(self.BonusOverviewBG)
		self.speedSlotBar.SetPosition(10,175)
		self.speedSlotBar.SetSize(295,19)
		self.speedSlotBar.Show()		

		self.speedTextLine = ui.TextLine()
		self.speedTextLine.SetParent(self.speedSlotBar)
		self.speedTextLine.SetPosition(147,3)
		self.speedTextLine.SetText("Normal")
		self.speedTextLine.SetHorizontalAlignCenter()
		self.speedTextLine.Show()	
			
		self.speedUpButton = ui.Button()
		self.speedUpButton.SetParent(self.speedSlotBar)
		self.speedUpButton.SetPosition(3,3)
		self.speedUpButton.SetText("")
		self.speedUpButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_plus_up.sub")
		self.speedUpButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_plus_over.sub")
		self.speedUpButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_plus_down.sub")
		self.speedUpButton.SetEvent(self.higherSwitchSpeed)
		self.speedUpButton.Show()

		self.speedLowButton = ui.Button()
		self.speedLowButton.SetParent(self.speedSlotBar)
		self.speedLowButton.SetPosition(15,3)
		self.speedLowButton.SetText("")
		self.speedLowButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_minus_up.sub")
		self.speedLowButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_minus_over.sub")
		self.speedLowButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_minus_down.sub")
		self.speedLowButton.SetWindowHorizontalAlignRight()
		self.speedLowButton.SetEvent(self.lowerSwitchSpeed)
		self.speedLowButton.Show()			
			# height = height + 22
			# i = i + 1
		
		
		
		self.itemInsertBG = ui.Bar()
		self.itemInsertBG.SetParent(self.Board)
		self.itemInsertBG.SetPosition(656+9,60+30)
		self.itemInsertBG.SetSize(130,255)
		self.itemInsertBG.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.itemInsertBG.Show()	

		self.itemInsertTitleBar = ui.HorizontalBar()
		self.itemInsertTitleBar.SetParent(self.Board)
		self.itemInsertTitleBar.Create(130)
		self.itemInsertTitleBar.SetPosition(656+9,60+30)
		self.itemInsertTitleBar.Show()
		
		i = 0
		x = 50
		while i < 3:
			self.itemSlotIMG[i] = ui.ImageBox()
			self.itemSlotIMG[i].SetParent(self.itemInsertBG)
			self.itemSlotIMG[i].SetPosition(49,x)
			self.itemSlotIMG[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			self.itemSlotIMG[i].Show()
			
			x = x + 32
			i = i +1
			
		self.itemSlot = ui.GridSlotWindow()  
		self.itemSlot.SetParent(self.itemInsertBG)  
		
		self.itemSlot.ArrangeSlot(0,1,3,32,32,0,0)  
		self.itemSlot.SetPosition(49,50)  
		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.AddItem))  
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.DelItemClick))  
		self.itemSlot.Show()			
			
		x = x + 20
		self.PlaceItemDialog = ui.TextLine()
		self.PlaceItemDialog.SetParent(self.itemInsertBG)
		self.PlaceItemDialog.SetPosition(65,x)
		self.PlaceItemDialog.SetText(localeInfo.SWITCHBOT_UI_INSERT_ITEM_LINE1)
		self.PlaceItemDialog.SetHorizontalAlignCenter()
		self.PlaceItemDialog.Show()
		x = x + 15
		self.PlaceItemDialog1 = ui.TextLine()
		self.PlaceItemDialog1.SetParent(self.itemInsertBG)
		self.PlaceItemDialog1.SetPosition(65,x)
		self.PlaceItemDialog1.SetText(localeInfo.SWITCHBOT_UI_INSERT_ITEM_LINE2)
		self.PlaceItemDialog1.SetHorizontalAlignCenter()
		self.PlaceItemDialog1.Show()
		x = x + 15
		self.PlaceItemDialog2 = ui.TextLine()
		self.PlaceItemDialog2.SetParent(self.itemInsertBG)
		self.PlaceItemDialog2.SetPosition(65,x)
		self.PlaceItemDialog2.SetText(localeInfo.SWITCHBOT_UI_INSERT_ITEM_LINE3)
		self.PlaceItemDialog2.SetHorizontalAlignCenter()
		self.PlaceItemDialog2.Show()
		x = x + 25
		self.ItemTypeDialog = ui.TextLine()
		self.ItemTypeDialog.SetParent(self.itemInsertBG)
		self.ItemTypeDialog.SetPosition(65,x)
		self.ItemTypeDialog.SetText(localeInfo.SWITCHBOT_UI_EMPTY2)
		self.ItemTypeDialog.SetHorizontalAlignCenter()
		self.ItemTypeDialog.Show()

		i = 0
		button_count = 5
		width = 25
		
		while i < button_count:
			self.pageButtons[i] = ui.Button()
			self.pageButtons[i].SetParent(self.Board)
			self.pageButtons[i].SetPosition(width,35+30-3)
			self.pageButtons[i].SetText("")
			self.pageButtons[i].SetUpVisual("yamato_helpboard/normal_button_n.tga")
			self.pageButtons[i].SetOverVisual("yamato_helpboard/normal_button_h.tga")
			self.pageButtons[i].SetDownVisual("yamato_helpboard/normal_button_p.tga")
			self.pageButtons[i].SetDisableVisual("yamato_helpboard/normal_button_d.tga")
			self.pageButtons[i].SetEvent(ui.__mem_func__(self.LoadPage), i)
			self.pageButtons[i].Show()
			width = width + 90 + 8
			i = i + 1
		self.pageButtons[0].Disable()	
		self.SlotIndexTextLine = ui.TextLine()
		self.SlotIndexTextLine.SetParent(self.Board)
		self.SlotIndexTextLine.SetPosition(16+9,38+30)
		self.SlotIndexTextLine.SetText("               I                               II                              III                             IV                              V")
		self.SlotIndexTextLine.Show()		
		self.ClearBonusList()
		self.updateSwitchSpeed()
		
		width = width + 230
		self.logButton = ui.Button()
		self.logButton.SetParent(self.Board)
		self.logButton.SetPosition(width-43,35+30-3)
		self.logButton.SetText("")
		self.logButton.SetUpVisual("yamato_helpboard/normal_button_n.tga")
		self.logButton.SetOverVisual("yamato_helpboard/normal_button_h.tga")
		self.logButton.SetDownVisual("yamato_helpboard/normal_button_p.tga")
		self.logButton.SetEvent(self.OpenLog)
		self.logButton.Show()
		
		self.logButtonText = ui.TextLine()
		self.logButtonText.SetParent(self.Board)
		self.logButtonText.SetPosition(width-8,38+30)
		self.logButtonText.SetText("Logs")
		self.logButtonText.Show()
		
		
		self.blockBarBackground = ui.Bar()
		self.blockBarBackground.SetParent(self.Board)
		self.blockBarBackground.SetPosition(20,60)
		self.blockBarBackground.SetSize(780,255 + 30)
		self.blockBarBackground.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.blockBarBackground.Hide()	
		
		self.bonusSaveDialog = SaveBonusSetDialog(self)
		self.bonusSaveDialog.SetParent(self.blockBarBackground)
		self.bonusSaveDialog.SetPosition(250,60)
		self.bonusSaveDialog.Close()
		
		self.bonusLoadDialog = LoadBonusSetDialog(self)
		self.bonusLoadDialog.SetParent(self.blockBarBackground)
		self.bonusLoadDialog.SetPosition(250,0)
		self.bonusLoadDialog.Close()	
		
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.BoniListScrollBar.OnUp()
		else:
			self.BoniListScrollBar.OnDown()		
		
	def OpenBonusSaveDialog(self):
		self.bonusSaveDialog.Open()
		# self.blockBarBackground.Show()	
		
	def OpenBonusLoadDialog(self):
		self.bonusLoadDialog.Open()
	
	def OpenLog(self):
		if self.SwitchLog.Open == 0:
			self.SwitchLog.ShowSwitchLogs()
		else:
			self.SwitchLog.HideSwitchLogs()

	def DoMinimize(self):
		if settinginfo.switchbot_minimize == 0:
			settinginfo.switchbot_minimize = 1
			self.SwitchLog.HideSwitchLogs()
			self.Board.Hide()
		else:
			settinginfo.switchbot_minimize = 0
			self.Board.Show()			
	
	def updateSwitchSpeed(self):
		speedNameList = [localeInfo.SWITCHBOT_UI_SPEED_SLOW,localeInfo.SWITCHBOT_UI_SPEED_NORMAL,localeInfo.SWITCHBOT_UI_SPEED_FAST]
		speedValueList = [120,80,40]
		self.speedTextLine.SetText(speedNameList[self.speedIndex])
		self.speedValue = speedValueList[self.speedIndex]

	def lowerSwitchSpeed(self):
		minSpeedIndex = 0
		if self.speedIndex == minSpeedIndex:
			return
		self.speedIndex = self.speedIndex - 1
		self.updateSwitchSpeed()
		
	
	def higherSwitchSpeed(self):
		maxSpeedIndex = 2
		if self.speedIndex == maxSpeedIndex:
			return
		self.speedIndex = self.speedIndex + 1
		self.updateSwitchSpeed()		
		
	################################################################
	## BonusSelector
	def GenerateBonusList(self,itemType):
		self.BoniList.ClearItem()
		bonusList = settinginfo.Switchbot_BonusList
		c = 0
		for i in xrange(len(bonusList)):
			itemTypeList = bonusList[i][1]
			for a in xrange(len(itemTypeList)):
				if itemType == itemTypeList[a]:
					self.BoniList.InsertItem(c,str(bonusList[i][0][1]))		
					self.itemTempBoniList[c] = i
					c = c + 1
					
		self.BoniList.SelectItem(0)
		if self.BoniList.GetItemCount() > 11:
			self.BoniListScrollBar.Show()
		else:
			self.BoniListScrollBar.Hide()
		
	def __OnSelectBonus(self):
		bonusListIndex = self.BoniList.GetSelectedItem()
		bonusSettingList = settinginfo.Switchbot_BonusList
		bonusIndex = self.itemTempBoniList[bonusListIndex]
		
		self.itemTempBonusValueSlot = 0
		self.itemTempBonusValueMax 	= len(bonusSettingList[bonusIndex][2])-1
		self.itemTempBonusValue 	= bonusSettingList[bonusIndex][2][0]
		
		self.BonusValueTextLine.SetText(str(self.itemTempBonusValue))
		
	def UpdateValueTextLine(self):
		bonusListIndex = self.BoniList.GetSelectedItem()
		bonusSettingList = settinginfo.Switchbot_BonusList
		bonusIndex = self.itemTempBoniList[bonusListIndex]
		self.itemTempBonusValue 	= bonusSettingList[bonusIndex][2][self.itemTempBonusValueSlot]
		self.BonusValueTextLine.SetText(str(self.itemTempBonusValue))
		
	def BonusValueUp(self):
		if self.itemTempBonusValueSlot == self.itemTempBonusValueMax:
			return
		self.itemTempBonusValueSlot = self.itemTempBonusValueSlot + 1
		self.UpdateValueTextLine()
		
		
	def BonusValueDown(self):
		if self.itemTempBonusValueSlot == 0:
			return
		self.itemTempBonusValueSlot = self.itemTempBonusValueSlot - 1
		self.UpdateValueTextLine()
		
	def __OnScrollBoniList(self):
		viewItemCount = self.BoniList.GetViewItemCount()
		itemCount = self.BoniList.GetItemCount()
		pos = self.BoniListScrollBar.GetPos() * (itemCount - viewItemCount)
		self.BoniList.SetBasePos(int(pos))
		
	
	def LoadBonus(self,index):
		bonusListIndex = self.BoniList.GetSelectedItem()
		bonusSettingList = settinginfo.Switchbot_BonusList
		bonusIndex = self.itemTempBoniList[bonusListIndex]
		bonusID = bonusSettingList[bonusIndex][0][0]
		
		if self.alternatePage == 0:
		
			if bonusID in self.itemAttrValues[self.pageIndex]:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_JUST_ONE_TIME)
				return
			self.bonusTextLine[index].SetText(str(AFFECT_DICT[bonusID](self.itemTempBonusValue)))
			self.itemAttrValues[self.pageIndex][index] = bonusID
			self.itemBoniValues[self.pageIndex][index] = self.itemTempBonusValue
		else:
			
			if self.itemAttrValues[self.pageIndex][index] == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_PRIMARY_BONUS_FIRST)
				return
			if bonusID in self.itemAttrValuesA[self.pageIndex]:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_JUST_ONE_TIME)
				return
			self.bonusTextLine[index].SetText(str(AFFECT_DICT[bonusID](self.itemTempBonusValue)))
			self.itemAttrValuesA[self.pageIndex][index] = bonusID
			self.itemBoniValuesA[self.pageIndex][index] = self.itemTempBonusValue			
		

		
	def DeleteBonus(self,index):
		if self.alternatePage == 0:
			self.bonusTextLine[index].SetText(localeInfo.SWITCHBOT_UI_EMPTY)
			self.itemAttrValues[self.pageIndex][index] = 0
			self.itemBoniValues[self.pageIndex][index] = 0

		else:
			self.bonusTextLine[index].SetText(localeInfo.SWITCHBOT_UI_EMPTY)
			self.itemAttrValuesA[self.pageIndex][index] = 0
			self.itemBoniValuesA[self.pageIndex][index] = 0
			
	def AddItem(self,slot):
		isAttached = mouseModule.mouseController.isAttached()  
		if isAttached:  
			attachedSlotType = mouseModule.mouseController.GetAttachedType()  
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()  
			mouseModule.mouseController.DeattachObject() 
			
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "[Debug] attachedSlotType: " + str(attachedSlotType))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "[Debug] attachedSlotPos: " + str(attachedSlotPos))
			
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY != attachedSlotType:  
				return  
				
			if fgGHGjjFHJghjfFG1545gGG.IsEquipmentSlot(attachedSlotPos):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_UNEQUIP_ITEM)
				return
				
			if self.itemSlots[self.pageIndex] != 0 and self.itemSlotStatus[self.pageIndex] > 0:
				return
				
			if self.SlotIsAlreadyInUse(attachedSlotPos) == 0 or self.Slot0Fix(attachedSlotPos) == 0:
				
				itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(attachedSlotPos)	
				item.SelectItem(itemvnum)
				
				itemSubType = item.GetItemSubType()
				itemType  	= item.GetItemType()
		
				if itemType >= 1 and itemType <= 2:
					self.ClearItemSlot(self.pageIndex)
					itemAttrType = self.GetItemAttrType(itemType,itemSubType)
					self.SetItemAttrName(itemAttrType)
					self.itemSlots[self.pageIndex] = attachedSlotPos
					settinginfo.switchbot_Slots[self.pageIndex] = attachedSlotPos
					
					self.itemSlotStatus[self.pageIndex] = 1
					self.itemSlot.SetItemSlot(0, itemvnum, 0)
					self.GenerateBonusList(itemAttrType)
					self.BoniValueSlotBar.Show()
					self.ManageStartButtonUI(2)
					
					self.loadBonusSetButton.Enable()	
					self.saveBonusSetButton.Enable()	

				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_ITEM_CAN_NOT_SWITCH)
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_SLOT_IS_IN_USE)
	
	def Slot0Fix(self,slot):
		if slot == 0 and self.itemSlotStatus[0] == 0:
			return 0
		return 1

	def DelItemClick(self,slot):
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "[DelItem] " + str(slot))
		
		pageIndex = self.pageIndex
		self.itemSlots[pageIndex] = 0
		settinginfo.switchbot_Slots[self.pageIndex] = 0
		self.itemSlotStatus[pageIndex] =  0
		self.itemSlot.ClearSlot(0)
		self.itemSlot.ClearSlot(1)
		self.itemSlot.ClearSlot(2)
		self.itemSlot.RefreshSlot()
		self.ClearItemAttrName()
		self.ClearItemSlot(pageIndex)
		self.ClearBonusList()
		self.BoniValueSlotBar.Hide()
		self.ManageStartButtonUI(2)
		settinginfo.switchbot_switch_count[pageIndex] = 0
		self.loadBonusSetButton.Disable()	
		self.saveBonusSetButton.Disable()
					
	def DelItem(self,slot):
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "[DelItem] " + str(slot))
		self.itemSlots[slot] = 0
		settinginfo.switchbot_Slots[slot] = 0
		self.itemSlotStatus[slot] =  0
		self.itemSlot.ClearSlot(0)
		self.itemSlot.ClearSlot(1)
		self.itemSlot.ClearSlot(2)
		self.itemSlot.RefreshSlot()
		self.ClearItemAttrName()
		self.ClearItemSlot(slot)
		self.ClearBonusList()
		self.BoniValueSlotBar.Hide()
		self.ManageStartButtonUI(2)
		settinginfo.switchbot_switch_count[slot] = 0
		self.loadBonusSetButton.Disable()	
		self.saveBonusSetButton.Disable()
			
	def SetItemAttrName(self,attrType):
		self.ItemTypeDialog.SetText("[ " + str(settinginfo.itemAttrTypeName[attrType]) + " ]")
		
	def ClearItemAttrName(self):
		self.ItemTypeDialog.SetText(localeInfo.SWITCHBOT_UI_EMPTY2)
			
	def GetItemAttrType(self,itemType,itemSubType):
		for i in xrange(len(settinginfo.itemAttrType)):
			if itemType == settinginfo.itemAttrType[i][0] and itemSubType == settinginfo.itemAttrType[i][1]:
				return settinginfo.itemAttrType[i][2]
		
	def ClearItemSlot(self,index):
		for i in xrange(5):
			self.bonusTextLine[i].SetText(localeInfo.SWITCHBOT_UI_EMPTY)
			self.itemAttrValues[index][i] = 0
			self.itemBoniValues[index][i] = 0
			self.itemAttrValuesA[index][i] = 0
			self.itemBoniValuesA[index][i] = 0
			
	def ClearBonusList(self):
		self.BoniList.ClearItem()
		self.BoniListScrollBar.Hide()	
		self.BoniListScrollBar.SetPos(0)
			
	def LoadBonusTempList(self):
		if self.alternatePage == 0:
			for i in xrange(5):
				#chat.AppendChat(chat.CHAT_TYPE_INFO, "itemAttrValues: "+str(self.itemAttrValues[self.pageIndex][i]))
				if self.itemAttrValues[self.pageIndex][i] == 0:
					self.bonusTextLine[i].SetText(localeInfo.SWITCHBOT_UI_EMPTY)
				else:
					attrIndex	= self.itemAttrValues[self.pageIndex][i]
					attrValue	= self.itemBoniValues[self.pageIndex][i]				
					self.bonusTextLine[i].SetText(str(AFFECT_DICT[attrIndex](attrValue)))
		else:
			for i in xrange(5):
				#chat.AppendChat(chat.CHAT_TYPE_INFO, "itemAttrValues: "+str(self.itemAttrValues[self.pageIndex][i]))
				if self.itemAttrValuesA[self.pageIndex][i] == 0:
					self.bonusTextLine[i].SetText(localeInfo.SWITCHBOT_UI_EMPTY)
				else:
					attrIndex	= self.itemAttrValuesA[self.pageIndex][i]
					attrValue	= self.itemBoniValuesA[self.pageIndex][i]				
					self.bonusTextLine[i].SetText(str(AFFECT_DICT[attrIndex](attrValue)))		
		
	def ClearPage(self):
		self.ClearItemAttrName()
		for i in xrange(5):
			self.bonusTextLine[i].SetText(localeInfo.SWITCHBOT_UI_EMPTY)

		self.ClearBonusList()
		self.itemSlot.ClearSlot(0)
		self.itemSlot.ClearSlot(1)
		self.itemSlot.ClearSlot(2)
		self.itemSlot.RefreshSlot()		
		self.ManageStartButtonUI(2)
		self.loadBonusSetButton.Disable()	
		self.saveBonusSetButton.Disable()
		
	def LoadPage(self,index):
		if index == self.pageIndex:
			return
			
		for i in xrange(5):
			if index == i:
				self.pageButtons[i].Disable()
			else:
				self.pageButtons[i].Enable()
			
		self.ClearPage()
		self.BoniListScrollBar.SetPos(0)
		self.pageIndex = index
		# self.Board.SetTitleName("Switchbot - [Seite "+str(self.pageIndex+1)+"]")
		self.BoniValueSlotBar.Hide()
		if self.itemSlotStatus[index] > 0:
			itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(self.itemSlots[index])	
			item.SelectItem(itemvnum)
				
			itemSubType = item.GetItemSubType()
			itemType  	= item.GetItemType()
		
			itemAttrType = self.GetItemAttrType(itemType,itemSubType)
			self.SetItemAttrName(itemAttrType)
			self.ManageStartButtonUI(self.TranslateButtonStatus(self.itemSlotStatus[self.pageIndex]))
			self.itemSlot.SetItemSlot(0, itemvnum, 0)
			self.GenerateBonusList(itemAttrType)
			self.LoadBonusTempList()
			self.BoniValueSlotBar.Show()

			self.loadBonusSetButton.Enable()	
			self.saveBonusSetButton.Enable()
			
	def TranslateButtonStatus(self,status):
		statusList = [0,2,1]
		return statusList[status]
		
	def BotIsReadyToStart(self):
		botIsReady = False
		for i in xrange(5):
			if self.itemAttrValues[self.pageIndex][i] > 0:
				botIsReady = True
			
			
		return botIsReady
				
	def ManageStartButtonUI(self,botStatus):
		if botStatus == 0:
			return 0
		elif botStatus == 1:
			if self.BotIsReadyToStart():
				self.BonusSwitcherBG.SetColor(grp.GenerateColor(0.0, 1.0, 0.0, 0.2))
				self.BonusSwitcherStartButtonText.SetText(localeInfo.SWITCHBOT_UI_STOP_BUTTON)	
				self.wndMinimap.SwitchBotButtonInactive.Hide()
				self.wndMinimap.SwitchBotButton.Show()
				return 2
			else:
				chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.SWITCHBOT_UI_ERROR_NO_ATTR_CONFIG)
				return botStatus
		elif botStatus == 2:
			self.BonusSwitcherBG.SetColor(grp.GenerateColor(1.0, 0.0, 0.0, 0.2))
			self.BonusSwitcherStartButtonText.SetText(localeInfo.SWITCHBOT_UI_START_BUTTON)		
			self.wndMinimap.SwitchBotButtonInactive.Show()
			self.wndMinimap.SwitchBotButton.Hide()
			return 1
	
	def SlotIsAlreadyInUse(self,slot):
		if slot in self.itemSlots:
			return 1
		return 0
		
		
	def Start(self):
		status = self.ManageStartButtonUI(self.itemSlotStatus[self.pageIndex])
		self.itemSlotStatus[self.pageIndex] = status
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "itemSlotStatus: "+str(self.itemSlotStatus[self.pageIndex]))
	
	def AutoStopBot(self,pageIndex):
		status = self.ManageStartButtonUI(self.itemSlotStatus[pageIndex])
		self.itemSlotStatus[pageIndex] = status		
	
	def CountBoniSet(self,pageIndex):
		count = 0
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "CountBoniSet: "+str(pageIndex))
		for i in xrange(5):
			#chat.AppendChat(chat.CHAT_TYPE_INFO, "CountBoniSet: "+str(self.itemAttrValues[pageIndex][i]) + " != 0")
			if self.itemAttrValues[pageIndex][i] != 0:
				count = count + 1
				
				
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "CountBoniSet: Count "+str(count))
		return count
		
	def SwitchBonusListDown(self):
		self.alternatePage = 1
		self.LoadBonusTempList()
			
	def SwitchBonusListUp(self):		
		self.alternatePage = 0
		self.LoadBonusTempList()
	
	
	def DoFinishSwitchLog(self,itemVnum,slot):
		item.SelectItem(itemVnum)
		text = "Slot " + str(slot) + ": " + str(item.GetItemName()) + " " + localeInfo.SWITCHBOT_UI_IS_DONE + " (" + str(settinginfo.switchbot_switch_count[slot-1]) + "x " + localeInfo.SWITCHBOT_UI_SWITCHED + ")"
		self.SwitchLog.AddLog(text)
	
	def DoSwitch(self,itemSlot):
		inventorySlot = self.itemSlots[itemSlot]
		if self.itemSlotStatus[itemSlot] < 2:
			return
		itemVnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(inventorySlot)
		if itemVnum == 0:		
			self.DelItem(itemSlot)
			return
		
		values 				= [fgGHGjjFHJghjfFG1545gGG.GetItemAttribute(inventorySlot, i) for i in range(0,5)]
		bonusNeedToComplete = self.CountBoniSet(itemSlot)
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "bonusNeedToComplete: "+str(bonusNeedToComplete))
		
		
		bonusComplete 		= 0
		switchItem 			= 0
		overSwitchProtection = [0,0,0,0,0]
		i = 0
		for i in xrange(5):
			for a in xrange(5):
				if values[i][0] == self.itemAttrValues[itemSlot][a]:
					if values[i][1] >= self.itemBoniValues[itemSlot][a]:
						if values[i][0] not in overSwitchProtection:
							overSwitchProtection[i] = values[i][0]
							bonusComplete = bonusComplete + 1	
				else: # AlternativeList
					if self.itemAttrValues[itemSlot][a] != 0:
						if self.itemAttrValuesA[itemSlot][a] != 0:
							if values[i][0] == self.itemAttrValuesA[itemSlot][a]:
								if values[i][1] >= self.itemBoniValuesA[itemSlot][a]:
									if values[i][0] not in overSwitchProtection:
										overSwitchProtection[i] = values[i][0]
										bonusComplete = bonusComplete + 1						
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "bonusComplete: "+str(bonusComplete))
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "bonusNeedToComplete: "+str(bonusNeedToComplete))
		if bonusComplete == bonusNeedToComplete:
			# chat.AppendChat(chat.CHAT_TYPE_COMMAND, "Slot " + str(itemSlot+1) + " wurde fertig geswitcht!")
			
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_announce_switch_complete " + str(itemSlot+1))
			
			self.DoFinishSwitchLog(itemVnum,itemSlot+1)
			self.DelItem(itemSlot)
			return
			
		countSwitcher = 0
		isEndlessSwitcher = 0
		switcherSlot = 0
		for i in range(0,(90*4)-1):
			if fgGHGjjFHJghjfFG1545gGG.GetItemIndex(i) == settinginfo.itemSwitchVnum or fgGHGjjFHJghjfFG1545gGG.GetItemIndex(i) == settinginfo.itemSwitchVnum2:
				if fgGHGjjFHJghjfFG1545gGG.GetItemIndex(i) == settinginfo.itemSwitchVnum:
					isEndlessSwitcher = 1
					switcherSlot = i
					break
				else:
					countSwitcher+=fgGHGjjFHJghjfFG1545gGG.GetItemCount(i)
				

		
			

		# else:
		# if shop.IsOpen():
			# if countSwitcher < 15:
				# self.buyNewSwitcher()
				# return
			
		if countSwitcher == 0 and isEndlessSwitcher == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_NO_SWITCHER_ITEMS)
			self.AutoStopBot(itemSlot)
			return
			
		# if isEndlessSwitcher == 1:	
		if fgGHGjjFHJghjfFG1545gGG.GetMoney() < 10000:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SWITCHBOT_UI_ERROR_NO_GOLD)
			self.AutoStopBot(itemSlot)
			return				
		
		for i in range(0,90*4):
			if fgGHGjjFHJghjfFG1545gGG.GetItemIndex(i) == settinginfo.itemSwitchVnum or fgGHGjjFHJghjfFG1545gGG.GetItemIndex(i) == settinginfo.itemSwitchVnum2:
				GFHhg54GHGhh45GHGH.SendItemUseToItemPacket(i,inventorySlot)
				
				settinginfo.switchbot_switch_count[itemSlot] = settinginfo.switchbot_switch_count[itemSlot] + 1
				# chat.AppendChat(chat.CHAT_TYPE_INFO, "settinginfo: " + str(settinginfo.switchbot_switch_count[itemSlot]))
				return		
	
	# def buyNewSwitcher(self):
		# for i in range(0,shop.SHOP_SLOT_COUNT):
			# me = shop.GetItemID(i)
			# if me == settinginfo.itemSwitchVnum:
				# if shop.GetItemPrice(i) <= fgGHGjjFHJghjfFG1545gGG.GetMoney():
					# GFHhg54GHGhh45GHGH.SendShopBuyPacket(i)
					# chat.AppendChat(chat.CHAT_TYPE_INFO, "[Switchbot] Es wurden neue Switcher gekauft!")
					# return
					
	def OnUpdate(self):
		if settinginfo.switchbot_minimize == 2:
			self.DoMinimize()
			
		self.counter+=1
		if self.counter >= self.speedValue: # 40
			self.counter = 0
			for n in xrange(5):
				self.DoSwitch(n)

	
class SwitchLog(ui.ScriptWindow):
	
	Logs 		= {}
	LogCount 	= 0
	Open		= 0

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
			
	def Destroy(self):
		self.__del__()
	
	def HideSwitchLogs(self):
		self.Open = 0
		self.Board.Hide()
				
	def ShowSwitchLogs(self):
		self.Open = 1
		self.Board.Show()
			
	def LoadUI(self):
		self.Board = ui.BoardWithRoofBar()
		self.Board.SetSize(330-9, 330-30-9)
		self.Board.SetPosition(5,5)
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		# self.Board.SetTitleName("Switchbot - Logs")
		self.Board.SetCloseEvent(self.HideSwitchLogs)
		self.Board.Show()
		
		self.LogBG = ui.Bar()
		self.LogBG.SetParent(self.Board)
		self.LogBG.SetPosition(15+9,35+30)
		self.LogBG.SetSize(300,280)
		self.LogBG.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.5))
		self.LogBG.Show()
		
		self.LogList = ui.ListBox()
		self.LogList.SetParent(self.Board)
		self.LogList.SetSize(290, 280)
		self.LogList.SetPosition(15+9, 35+30)
		self.LogList.SetEvent(ui.__mem_func__(self.__OnSelectLog))
		self.LogList.Show()

		self.LogListScrollBar = ui.ScrollBar()
		self.LogListScrollBar.SetParent(self.Board)
		self.LogListScrollBar.SetPosition(300+9, 35+30)
		self.LogListScrollBar.SetScrollBarSize(280)
		self.LogListScrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScrollLogList))
		self.LogListScrollBar.Hide()

	def AddLog(self,text):
		localtime = localtime = time.strftime("[%H:%M:%S]")
		text = text + " " + localtime
		self.Logs[self.LogCount] = str(text)
		self.LogCount = self.LogCount + 1
		self.ReloadLogList()
		
	def ReloadLogList(self):
		self.LogList.ClearItem()
		for i in xrange(len(self.Logs)):
			self.LogList.InsertItem(i,str(self.Logs[i]))		
		
		if self.LogCount > 16:
			self.LogListScrollBar.Show()
		else:
			self.LogListScrollBar.Hide()
		
	def __OnSelectLog(self):
		return
	
	def __OnScrollLogList(self):
		viewItemCount = self.LogList.GetViewItemCount()
		itemCount = self.LogList.GetItemCount()
		pos = self.LogListScrollBar.GetPos() * (itemCount - viewItemCount)
		self.LogList.SetBasePos(int(pos))
		
class SaveBonusSetDialog(ui.ScriptWindow):
	
	buttonStatus = 0
	
	def __init__(self,botWindow):
		ui.ScriptWindow.__init__(self)
		self.botWindow = botWindow
		self.LoadWindow()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/bonussavedialog.py")
		except:
			import exception
			exception.Abort("BonusSaveDialog.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Open)
		
		self.bonusSaveTitle = self.GetChild("nameyourset_TextLine")
		self.bonusSaveEditLine = self.GetChild("nameyourset_EditLine")
		self.bonusSaveSaveButton = self.GetChild("saveButton")
		self.bonusSaveCloseButton = self.GetChild("closeButton")

		self.bonusSaveSaveButton.SetEvent(self.Save)
		self.bonusSaveCloseButton.SetEvent(self.Open)

	def Save(self):
		saveString = self.bonusSaveEditLine.GetText() + "/"

		itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(self.botWindow.itemSlots[self.botWindow.pageIndex])	
		item.SelectItem(itemvnum)
				
		itemSubType = item.GetItemSubType()
		itemType  	= item.GetItemType()
		itemAttrType = self.botWindow.GetItemAttrType(itemType,itemSubType)
	
		saveString = saveString + str(itemAttrType) + "/"
		
		
		bonusAttrListNormal = self.botWindow.itemAttrValues[self.botWindow.pageIndex]
		bonusBoniListNormal = self.botWindow.itemBoniValues[self.botWindow.pageIndex]
		bonusNormalString = ""
		for i in xrange(5):
			bonusNormalString = bonusNormalString + str(bonusAttrListNormal[i]) + ":" + str(bonusBoniListNormal[i]) + "#"
	
		saveString = saveString + bonusNormalString + "/"

		bonusAttrListAlternate = self.botWindow.itemAttrValuesA[self.botWindow.pageIndex]
		bonusBoniListAlternate = self.botWindow.itemBoniValuesA[self.botWindow.pageIndex]
		bonusAlternateString = ""
		for i in xrange(5):
			bonusAlternateString = bonusAlternateString + str(bonusAttrListAlternate[i]) + ":" + str(bonusBoniListAlternate[i]) + "#"
	
		saveString = saveString + bonusAlternateString + "/"
		
		fo = open("switchbot.txt", "a")
		fo.write(saveString + "\n")
		fo.close()
		
		self.botWindow.bonusLoadDialog.LoadSwitchbotTXT()
		
		self.Open()
		
	def OnUpdate(self):
		if self.IsShow():
			letterCount = len(self.bonusSaveEditLine.GetText())
			# if letterCount > 0:
				# if self.buttonStatus == 0:
					# self.buttonStatus == 1
					# self.bonusSaveSaveButton.Enable()
			# else:
				# self.buttonStatus = 0
				# self.bonusSaveSaveButton.Disable()
				
			self.bonusSaveTitle.SetText("Name your bonus set: (" + str(letterCount) + "/20)")

	def Open(self):
		if self.IsShow():
			self.botWindow.blockBarBackground.Hide()
			self.Close()
		else:
			self.botWindow.blockBarBackground.Show()
			self.Show()

	def Close(self):
		self.Hide()



class LoadBonusSetDialog(ui.ScriptWindow):
	
	BONUS_NAME = 0
	BONUS_ITEM_TYPE = 1
	BONUS_LIST_NORMAL = 2
	BONUS_LIST_ALTERNATE = 3
	
	maxViewItem = 8
	
	def __init__(self,botWindow):
		ui.ScriptWindow.__init__(self)
		self.botWindow = botWindow
		self.LoadWindow()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/bonusloaddialog.py")
		except:
			import exception
			exception.Abort("BonusLoadDialog.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Open)
		
		self.listBox = self.GetChild("list_box")
		self.scrollBar = self.GetChild("scrollbar")
		self.loadButton = self.GetChild("loadButton")
		self.closeButton = self.GetChild("closeButton")
		
		
		
		self.closeButton.SetEvent(self.Open)
		self.loadButton.SetEvent(self.Load)
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScroll))
		
		self.LoadSwitchbotTXT()
		# self.scrollBar.Hide()
		
		# for i in xrange(20):
			# self.listBox.InsertItem(i,"testName"+str(i))			
	
	def Load(self):
		index = self.listBox.GetSelectedItem()
		bonusSave = self.switchbotSaves[index]
	
	
		itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(self.botWindow.itemSlots[self.botWindow.pageIndex])	
		item.SelectItem(itemvnum)
				
		itemSubType = item.GetItemSubType()
		itemType  	= item.GetItemType()
		itemAttrType = self.botWindow.GetItemAttrType(itemType,itemSubType)
		
		if itemAttrType != bonusSave["item_type"]:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"You can not load this bonus set with the current Item! WRONG ITEM_TYPE!")
			return
			
		bonusListNormal_Index = bonusSave["n_list_index"]
		bonusListNormal_Value = bonusSave["n_list_value"]
		for i in xrange(5):
			bonusID = bonusListNormal_Index[i]
			bonusValue = bonusListNormal_Value[i]
			if self.botWindow.alternatePage == 0:
				if bonusID == 0:
					self.botWindow.bonusTextLine[i].SetText(localeInfo.SWITCHBOT_UI_EMPTY)
				else:
					self.botWindow.bonusTextLine[i].SetText(str(AFFECT_DICT[bonusID](bonusValue)))
				
			self.botWindow.itemAttrValues[self.botWindow.pageIndex][i] = bonusID
			self.botWindow.itemBoniValues[self.botWindow.pageIndex][i] = bonusValue		
		
		bonusListAlternate_Index = bonusSave["a_list_index"]
		bonusListAlternate_Value = bonusSave["a_list_value"]
		for i in xrange(5):
			bonusID = bonusListAlternate_Index[i]
			bonusValue = bonusListAlternate_Value[i]
			if self.botWindow.alternatePage == 1:
				if bonusID == 0:
					self.botWindow.bonusTextLine[i].SetText(localeInfo.SWITCHBOT_UI_EMPTY)
				else:
					self.botWindow.bonusTextLine[i].SetText(str(AFFECT_DICT[bonusID](bonusValue)))
				
			self.botWindow.itemAttrValuesA[self.botWindow.pageIndex][i] = bonusID
			self.botWindow.itemBoniValuesA[self.botWindow.pageIndex][i] = bonusValue				
		
		chat.AppendChat(chat.CHAT_TYPE_INFO,"Bonus set is loaded!")
		
		self.Open()
	
	def LoadSwitchbotTXT(self):
		self.switchbotSaves = []
		# chat.AppendChat(chat.CHAT_TYPE_INFO,"switchbotSaves: " + str(len(self.switchbotSaves)))
		fo = open("switchbot.txt", "r")
		i = 0
		for line in fo:
			line_split = line.split("/")
			
			save_name = line_split[self.BONUS_NAME]
			save_type = line_split[self.BONUS_ITEM_TYPE]
			save_bonus_n = line_split[self.BONUS_LIST_NORMAL]
			save_bonus_a = line_split[self.BONUS_LIST_ALTERNATE]
			
			
			save_bonus_list_n_index = []
			save_bonus_list_n_value = []
			save_bonus_n = save_bonus_n.split("#")
			for i in xrange(5):
				final_bonus_split = save_bonus_n[i].split(":")
				save_bonus_list_n_index.append(int(final_bonus_split[0]))
				save_bonus_list_n_value.append(int(final_bonus_split[1]))
				
			save_bonus_list_a_index = []
			save_bonus_list_a_value = []
			save_bonus_a = save_bonus_a.split("#")
			for i in xrange(5):
				final_bonus_split = save_bonus_a[i].split(":")
				save_bonus_list_a_index.append(int(final_bonus_split[0]))
				save_bonus_list_a_value.append(int(final_bonus_split[1]))		

			
			proto = {
				"name" : save_name,
				"item_type" : int(save_type),
			
				"n_list_index" : save_bonus_list_n_index,
				"n_list_value" : save_bonus_list_n_value,

				"a_list_index" : save_bonus_list_a_index,
				"a_list_value" : save_bonus_list_a_value,
				
			}
			
			self.switchbotSaves.append(proto)
			# chat.AppendChat(chat.CHAT_TYPE_INFO,"switchbotSaves: " + str(len(self.switchbotSaves)))
			
			# chat.AppendChat(chat.CHAT_TYPE_INFO,save_name)
			# chat.AppendChat(chat.CHAT_TYPE_INFO,save_type)
			# chat.AppendChat(chat.CHAT_TYPE_INFO,str(len(save_bonus_list_n_index)))
			# chat.AppendChat(chat.CHAT_TYPE_INFO,str(len(save_bonus_list_n_value)))
			
			# chat.AppendChat(chat.CHAT_TYPE_INFO,str(len(save_bonus_list_a_index)))
			# chat.AppendChat(chat.CHAT_TYPE_INFO,str(len(save_bonus_list_a_value)))			

			i = i + 1
		self.BuildListBox()
		
	def BuildListBox(self):
		self.listBox.ClearItem()
		if len(self.switchbotSaves) == 0:
			return
			
		
		for i in xrange(len(self.switchbotSaves)):
			self.listBox.InsertItem(i,self.switchbotSaves[i]["name"] + " - [" + settinginfo.itemAttrTypeName[self.switchbotSaves[i]["item_type"]] + "]")
		
		if len(self.switchbotSaves) > self.maxViewItem:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"scrollbar SHOW!")
			self.scrollBar.Show()
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"scrollbar HIDE!")
			self.scrollBar.Hide()
	
	def __OnScroll(self):
		viewItemCount = self.listBox.GetViewItemCount()
		itemCount = self.listBox.GetItemCount()
		pos = self.scrollBar.GetPos() * (itemCount - viewItemCount)
		self.listBox.SetBasePos(int(pos))
			
	def Open(self):
		if self.IsShow():
			self.botWindow.blockBarBackground.Hide()
			self.Close()
		else:
			self.botWindow.blockBarBackground.Show()
			self.Show()

	def Close(self):
		self.Hide()



























			
#SwitchBoard().Show()