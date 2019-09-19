import ui
import fgGHGjjFHJghjfFG1545gGG as player
import mouseModule
import GFHhg54GHGhh45GHGH
import app
import snd
import item
import chat
import grp
import uiScriptLocale
import uiRefine
import uiAttachMetin
import uiPickMoney
import uiCommon
import uiPrivateShopBuilder # 개인상점 열동안 ItemMove 방지
import localeInfo
import constInfo
import ime
import wndMgr
import exchange
import settinginfo
import event
import background
from uiGuild import MouseReflector
import uiToolTip
import exterminatus

ITEM_MALL_BUTTON_ENABLE = True



ITEM_FLAG_APPLICABLE = 1 << 14

class DEVItemInformation(ui.Window):

	normalWidth = 190
	
	def __init__(self,wndInventory):
		ui.Window.__init__(self)
		self.wndInventory = wndInventory
		self.SetSize(self.normalWidth,100)
		self.slot = 0
		self.itemVnum = 0
		self.attributeList = []
		self.socketList = []	
		self.Hide()
		self.MakeToolTip()	
		self.MakeCloseButton()
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def AdjustPosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		self.SetPosition(x - self.normalWidth - 10 + 22 - 15,(y + 650)-self.toolTip.toolTipHeight)
		self.SetSize(self.normalWidth,self.toolTip.toolTipHeight)
		
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetParent(self)
		toolTip.SetPosition(1, 1)
		toolTip.SetFollow(False)
		toolTip.Show()
		self.toolTip = toolTip
		
	def MakeCloseButton(self):
		self.closeButton = ui.Button()
		self.closeButton.SetParent(self)
		self.closeButton.SetPosition(self.normalWidth - 20,8)
		self.closeButton.SetText("")
		self.closeButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		self.closeButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		self.closeButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		self.closeButton.SetEvent(self.Close)
		self.closeButton.Show()
	
	def Open(self,slot):
		self.slot = slot
		
		itemVnum = player.GetItemIndex(slot)
		item.SelectItem(itemVnum)
		
		self.itemVnum = itemVnum
		self.socketList = [player.GetItemMetinSocket(slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		self.attributeList = [player.GetItemAttribute(slot, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		self.Show()
		
	def OnUpdate(self):
		if self.itemVnum != 0:
			self.RenderToolTip()
		
	def RenderToolTip(self):
		slot = self.slot
		
		if player.GetItemIndex(slot) != self.itemVnum:
			self.Clear()
			self.Close()
			return
		
		self.socketList = [player.GetItemMetinSocket(slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		self.attributeList = [player.GetItemAttribute(slot, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		self.toolTip.ClearToolTip()
		item.SelectItem(self.itemVnum)		
		self.toolTip.AppendTextLine("Item-Information:",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendStatisticTextLine("itemVnum:",self.itemVnum)
		self.toolTip.AppendStatisticTextLine("itemType:",item.GetItemType())
		self.toolTip.AppendStatisticTextLine("itemSubType:",item.GetItemSubType())
		self.toolTip.AppendStatisticTextLine("slot:",slot)
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
		self.toolTip.AppendTextLine("Values:",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendStatisticTextLine("value 0:",item.GetValue(0))
		self.toolTip.AppendStatisticTextLine("value 1:",item.GetValue(1))
		self.toolTip.AppendStatisticTextLine("value 2:",item.GetValue(2))
		self.toolTip.AppendStatisticTextLine("value 3:",item.GetValue(3))
		self.toolTip.AppendStatisticTextLine("value 4:",item.GetValue(4))
		self.toolTip.AppendStatisticTextLine("value 5:",item.GetValue(5))
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
		self.toolTip.AppendTextLine("Sockets:",self.toolTip.TITLE_COLOR)
		for i in xrange(len(self.socketList)):
			self.toolTip.AppendStatisticTextLine("socket " + str(i) + ":",self.socketList[i])

		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
		self.toolTip.AppendTextLine("Attributes:",self.toolTip.TITLE_COLOR)
		for i in xrange(len(self.attributeList)):
			self.toolTip.AppendStatisticTextLine("attrSlot (" + str(i) + ") Type: " + str(self.attributeList[i][0]),self.attributeList[i][1])
		
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
			
		self.toolTip.ResizeToolTip()	
		self.AdjustPosition()

	def Clear(self):
		self.slot = 0
		self.attributeList = []
		self.socketList = []	
		self.toolTip.ClearToolTip()
		self.itemVnum = 0
		
	def Close(self):
		self.Hide()

class CostumeAttributeChanger(ui.ScriptWindow):

	class CostumeAttributeItem(ui.ScriptWindow):
	
		COLOR_NEGATIVE	= grp.GenerateColor(1.0, 0.0, 0.0, 0.3)
		COLOR_POSITIVE	= grp.GenerateColor(0.0, 1.0, 0.0, 0.2)
		
		def __init__(self, wndAttributeSwitcher, attrSlot):
			ui.ScriptWindow.__init__(self)
			self.wndAttributeSwitcher = wndAttributeSwitcher
			self.attributeIndex = 0
			self.attributeValue = 0
			self.attrSlot = attrSlot
			self.LoadWindow()

		def __del__(self):
			ui.ScriptWindow.__del__(self)

		def LoadWindow(self):
			try:
				pyScrLoader = ui.PythonScriptLoader()
				pyScrLoader.LoadScriptFile(self, "exscript/costumeattributeitem.py")
			except:
				import exception
				exception.Abort("CostumeAttributeItem.LoadWindow.LoadObject")
			
			
			self.pointArrow = exterminatus.PointArrow()
			self.pointArrow.SetParent(self)
			self.pointArrow.SetPosition((290-24)/2,-20)
			self.pointArrow.Hide()
			
			self.background = self.GetChild("board")
			self.background.SetOnClickEvent(self.UseSpecialSwitcher)
			self.addBonusBar = self.GetChild("addBonusBar")
			self.addBonusBar.SetColor(self.COLOR_POSITIVE)
			self.addBonusBar.SetOnClickEvent(self.AddBonus)
			self.addBonusBar.Hide()
			
			self.attributeIndexTextLine = self.GetChild("bonusTitleTextLine")
			self.attributeValueTextLine = self.GetChild("bonusValueTextLine")
			
			self.mouseReflector = MouseReflector(self.background)
			self.mouseReflector.SetSize(290-24, 22)
			self.mouseReflector.UpdateRect()	
		
		def AddBonus(self):
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"addBonus CLICK!")
			if mouseModule.mouseController.isAttached():
				constInfo.INPUT_CMD = "add#" + str(self.wndAttributeSwitcher.costumeSlotPosition) + "#" + str(self.attrSlot)
				event.QuestButtonClick(self.wndAttributeSwitcher.qid)
				mouseModule.mouseController.DeattachObject()
			
		def UseSpecialSwitcher(self):
			if self.wndAttributeSwitcher.isSpecialSwitchMode:
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"ChangeBonus CLICK!")
				constInfo.INPUT_CMD = "change_s#" + str(self.wndAttributeSwitcher.costumeSlotPosition) + "#" + str(self.attrSlot)
				event.QuestButtonClick(self.wndAttributeSwitcher.qid)
				
		def AddYToArrowPosition(self,y):
			self.pointArrow.SetPosition(((290-24)/2) + y,-20)
		
		def AddAttributeInformation(self,index,value):
			self.attributeIndex = index
			self.attributeValue = value	
			
			if index == 0:
				self.attributeIndexTextLine.SetText("Kein Bonus")
				
			else:
				try:
					self.attributeIndexTextLine.SetText(str(self.wndAttributeSwitcher.ATTRIBUTE_NAME_LIST[index]))
					
				except:
					self.attributeIndexTextLine.SetText("NO_ATTR_NAME_FOR:" + str(index))
				
				
			self.attributeValueTextLine.SetText(str(value))

		def OnUpdate(self):
			if mouseModule.mouseController.isAttached():

				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				if player.SLOT_TYPE_INVENTORY == mouseModule.mouseController.GetAttachedType():

					if self.wndAttributeSwitcher.BONUS_ADDER == mouseModule.mouseController.GetAttachedItemIndex():
						if self.attributeIndex == 0:
							self.addBonusBar.SetColor(self.COLOR_POSITIVE)
							self.addBonusBar.Show()
							self.pointArrow.Show()							
						
						else:
							self.addBonusBar.SetColor(self.COLOR_NEGATIVE)
							self.addBonusBar.Show()
							self.pointArrow.Hide()
				# mouseModule.mouseController.DeattachObject()		
			else:
				self.pointArrow.Hide()
				self.addBonusBar.Hide()
				if self.background.IsIn():
					if self.wndAttributeSwitcher.isSpecialSwitchMode:
						self.mouseReflector.Show()
					else:
						self.mouseReflector.Hide()
				else:
					self.mouseReflector.Hide()
				
	# ################################################# #			
			
			
	BONUS_ADDER			= 79998
	NORMAL_SWITCHER		= 79999
	SPECIAL_SWITCHER	= 80000
	
	COSTUME_SLOT = 199
	
	
	ATTRIBUTE_NAME_LIST = {
		
		12 : "Vergiftungschance",
		13 : "Ohnmachtschance",
		14 : "Verlangsamungschance",
		15 : "Chance auf krit. Treffer",
		16 : "Chance auf durchbohrenden Treffer",
		17 : "Stark gegen Halbmenschen",
	}
	
	def __init__(self, wndInventory):
		ui.ScriptWindow.__init__(self)
		self.wndInventory			= wndInventory
		self.costumeSlotPosition	= 0
		self.costumeItemVnum		= 0
		self.isSpecialSwitchMode	= False
		self.waitForServerAnswer	= False
		self.costumeAttributeList	= []
		self.costumeSocketList		= []
		self.qid					= 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/costumeattributechange.py")
		except:
			import exception
			exception.Abort("CostumeAttributeChanger.LoadWindow.LoadObject")
			
		self.costumeToolTip = uiToolTip.ItemToolTip()  
		self.costumeToolTip.HideToolTip()	

		self.costumeSwitcherToolTip = uiToolTip.ItemToolTip()  
		self.costumeSwitcherToolTip.HideToolTip()
		
		self.costumeSpecialSwitcherToolTip = uiToolTip.ItemToolTip()  
		self.costumeSpecialSwitcherToolTip.HideToolTip()
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.costumeSlot = self.GetChild("costumeSlot")
		self.costumeSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.costumeSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip)) 

		self.costumeSwitcherSlot = self.GetChild("costumeSwitcherSlot")
		self.costumeSwitcherSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowSwitcherToolTip))  
		self.costumeSwitcherSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideSwitcherToolTip)) 	
		self.costumeSwitcherSlot.SetSlotBaseImage("icon/item/" + str(self.NORMAL_SWITCHER) + ".tga", 1.0, 1.0, 1.0, 0.5)	
		self.costumeSwitcherSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.DoNormalSwitch)) 
		self.costumeSwitcherSlot.ShowSlotBaseImage(0)
		
		self.costumeSpecialSwitcherSlot = self.GetChild("specialCostumeSwitcherSlot")
		self.costumeSpecialSwitcherSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowSpecialSwitcherToolTip))  
		self.costumeSpecialSwitcherSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideSpecialSwitcherToolTip)) 		
		self.costumeSpecialSwitcherSlot.SetSlotBaseImage("icon/item/" + str(self.SPECIAL_SWITCHER) + ".tga", 1.0, 1.0, 1.0, 0.5)	
		self.costumeSpecialSwitcherSlot.SAFE_SetButtonEvent("RIGHT", "ALWAYS", self.ToggleSpecialSwitcher)
		self.costumeSpecialSwitcherSlot.ShowSlotBaseImage(0)
		
		self.bonusBackground = self.GetChild("bonusChangeBackground")
		
		self.bonusSlot = {}
		
		self.bonusSlot[0] = self.CostumeAttributeItem(self, 0)
		self.bonusSlot[0].SetParent(self.bonusBackground)
		self.bonusSlot[0].SetPosition(12,35)
		self.bonusSlot[0].AddYToArrowPosition(15)
		self.bonusSlot[0].Show()

		self.bonusSlot[1] = self.CostumeAttributeItem(self, 1)
		self.bonusSlot[1].SetParent(self.bonusBackground)
		self.bonusSlot[1].SetPosition(12,35 + 30)
		self.bonusSlot[1].AddYToArrowPosition(15 + 20)
		self.bonusSlot[1].Show()
		
		self.bonusSlot[2] = self.CostumeAttributeItem(self, 2)
		self.bonusSlot[2].SetParent(self.bonusBackground)
		self.bonusSlot[2].SetPosition(12,35 + 30 + 30)
		self.bonusSlot[2].AddYToArrowPosition(15 + 20 + 20)
		self.bonusSlot[2].Show()

		self.Open()
	
	def DoNormalSwitch(self,slot):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Hallo? Ist da jemand?")
		constInfo.INPUT_CMD = "change_n#" + str(self.costumeSlotPosition) + "#0"
		event.QuestButtonClick(self.qid)		
	
	def ToggleSpecialSwitcher(self,slot):
		if self.isSpecialSwitchMode:
			self.isSpecialSwitchMode = False
			self.costumeSpecialSwitcherSlot.DeactivateSlot(0)
			
		elif not self.isSpecialSwitchMode:
			count, s_count = self.CountCostumeSwitcher()
			if s_count == 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Du besitzt keine Special-Switcher!")
				return
				
			self.isSpecialSwitchMode = True
			self.costumeSpecialSwitcherSlot.ActivateSlot(0)
	
	def OnUpdate(self):
		if player.GetItemIndex(self.costumeSlotPosition) != self.costumeItemVnum:
			self.Clear()
			self.Close()
			return

		count, s_count = self.CountCostumeSwitcher()
		
		if count == 0 or self.isSpecialSwitchMode:
			self.costumeSwitcherSlot.SetItemSlot(0,0,0)
		else:
			self.costumeSwitcherSlot.SetItemSlot(0,self.NORMAL_SWITCHER,count)

		if s_count == 0:	
			self.costumeSpecialSwitcherSlot.SetItemSlot(0,0,0)
			
			if self.isSpecialSwitchMode:
				self.isSpecialSwitchMode = False
				self.costumeSpecialSwitcherSlot.DeactivateSlot(0)				
			
		else:
			self.costumeSpecialSwitcherSlot.SetItemSlot(0,self.SPECIAL_SWITCHER,s_count)
		
		
		
		tempAttrList = [player.GetItemAttribute(self.costumeSlotPosition, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		
		self.bonusSlot[0].AddAttributeInformation(tempAttrList[0][0],tempAttrList[0][1])
		self.bonusSlot[1].AddAttributeInformation(tempAttrList[1][0],tempAttrList[1][1])
		self.bonusSlot[2].AddAttributeInformation(tempAttrList[2][0],tempAttrList[2][1])

	def CountCostumeSwitcher(self):
		count = 0
		s_count = 0
		for i in range(0,(90*4)-1):
			if player.GetItemIndex(i) == self.NORMAL_SWITCHER:
				count = count + player.GetItemCount(i)
				
			elif player.GetItemIndex(i) == self.SPECIAL_SWITCHER:
				s_count = s_count + player.GetItemCount(i)	
				
		return count, s_count
		
	def ShowToolTip(self,slot):
		self.costumeSocketList = [player.GetItemMetinSocket(self.costumeSlotPosition, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		self.costumeAttributeList = [player.GetItemAttribute(self.costumeSlotPosition, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
	
		self.costumeToolTip.ClearToolTip()	
		self.costumeToolTip.AddItemData(self.costumeItemVnum, self.costumeSocketList, self.costumeAttributeList)	
		self.costumeToolTip.ShowToolTip()	
	
	def HideToolTip(self):
		self.costumeToolTip.HideToolTip()

	def ShowSwitcherToolTip(self,slot):
		self.costumeSwitcherToolTip.ClearToolTip()	
		self.costumeSwitcherToolTip.AddItemData(self.NORMAL_SWITCHER, [0,0,0,0,0,0])	
		
		self.costumeSwitcherToolTip.AppendTextLine("[Hinweis]",self.costumeSwitcherToolTip.TITLE_COLOR)
		self.costumeSwitcherToolTip.AppendTextLine("Alle 3 Boni werden neu gewurfelt!",self.costumeSwitcherToolTip.NORMAL_COLOR)
		self.costumeSwitcherToolTip.AppendHorizontalLine()
		self.costumeSwitcherToolTip.AppendTextLine("|Eemoji/key_lclick|e - Alle Switchen!",self.costumeSwitcherToolTip.NORMAL_COLOR)
		self.costumeSwitcherToolTip.AppendHorizontalLine()
		self.costumeSwitcherToolTip.ShowToolTip()	
		
	def HideSwitcherToolTip(self):
		self.costumeSwitcherToolTip.HideToolTip()

	def ShowSpecialSwitcherToolTip(self,slot):
		self.costumeSpecialSwitcherToolTip.ClearToolTip()	
		self.costumeSpecialSwitcherToolTip.AddItemData(self.SPECIAL_SWITCHER, [0,0,0,0,0,0])
		self.costumeSpecialSwitcherToolTip.AppendTextLine("[Hinweis]",self.costumeSwitcherToolTip.TITLE_COLOR)
		self.costumeSpecialSwitcherToolTip.AppendDescription("Nutze rechtsklick um den Spezial-Switcher zu aktivieren, und wahle dann rechts einen der 3 Boni aus. Es wird nur der ausgewahlte Boni geswitcht, alle anderen bleiben bestehen.", 25)
		self.costumeSpecialSwitcherToolTip.AppendHorizontalLine()
		self.costumeSpecialSwitcherToolTip.AppendTextLine("|Eemoji/key_rclick|e - Aktivieren",self.costumeSpecialSwitcherToolTip.NORMAL_COLOR)
		self.costumeSpecialSwitcherToolTip.AppendHorizontalLine()
		self.costumeSpecialSwitcherToolTip.ShowToolTip()
		
	def HideSpecialSwitcherToolTip(self):
		self.costumeSpecialSwitcherToolTip.HideToolTip()

	def OnPressEscapeKey(self):
		self.Close()
		return True
	
	def LoadItem(self,slot):
		if slot == self.COSTUME_SLOT:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Bitte lege das Kostum zum switchen ab!")
			return
		
		
		if self.qid == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Es ist ein Fehler aufgetreten. Bitte starte deinen Clienten neu. FEHLER: QID")
			return
	
		self.costumeSlotPosition = slot
		self.costumeItemVnum = player.GetItemIndex(slot)
		
		self.costumeSocketList = [player.GetItemMetinSocket(slot, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		self.costumeAttributeList = [player.GetItemAttribute(slot, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

		self.costumeSlot.SetItemSlot(0,self.costumeItemVnum,0)
		
		# self.wndInventory.wndItem.LockSlot(slot)
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"costumeSocketList : " + str(len(self.costumeSocketList)))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"costumeAttributeList : " + str(len(self.costumeAttributeList)))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"socket0: " + str(player.GetItemMetinSocket(slot,0)))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"slot: " + str(slot))
		
		self.Open()
		return
	
	def Clear(self):
		self.costumeSlotPosition = 0
		self.costumeItemVnum = 0
		self.costumeSlot.ClearSlot(0)
		self.isSpecialSwitchMode = False
		
	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
	
	def Refresh(self):
		return
	
	def SetQID(self,qid):
		self.qid = int(qid)

	def Close(self):
		self.Hide()
		
	def GetBasePosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		return x - 450, y
		
	def AdjustPosition(self):
		bx, by = self.GetBasePosition()
		self.SetPosition(bx, by)		
			
class SuperAwesomeIMBAKrassSideBarPrototypeJaKriegtNochAnderenCLASSNameHaHa(ui.ScriptWindow):

	COLOR_HOVER = grp.GenerateColor(1.0, 0.0, 0.0, 0.2)
	SIDEBAR_HEIGHT = 32 * 3
	BUTTON_DICT = [
		{
			"button_name" : "TestButton 1",
			"button_desc" : "Das ist eine Beschreibung der Funktion des TestButton 1. So noch etwas mehr Text da es sonst echt ... Naja aussieht.",
			"button_icon" : "icon/item/27001.tga",
			"button_func" : "",
		},
		{
			"button_name" : "TestButton 2",
			"button_desc" : "Das ist eine Beschreibung der Funktion des TestButton 2. So noch etwas mehr Text da es sonst echt ... Naja aussieht.",
			"button_icon" : "icon/item/27002.tga",
			"button_func" : "",
		},
	]

	def __init__(self, wndInventory):
		ui.ScriptWindow.__init__(self)
		self.wndInventory = wndInventory
		self.sideBarItem = {}
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		self.SetSize(33,self.SIDEBAR_HEIGHT)
		
		self.Background = ui.ThinBoardCircle()
		self.Background.SetParent(self)
		self.Background.SetPosition(0,0)
		self.Background.SetSize(33,self.SIDEBAR_HEIGHT)
		self.Background.Show()
		
		y = 1
		for i in xrange(len(self.BUTTON_DICT)):
			Info = self.BUTTON_DICT[i]
			self.sideBarItem[i] = EasySideBarItem(self)
			self.sideBarItem[i].SetParent(self)
			self.sideBarItem[i].SetPosition(1,y)
			self.sideBarItem[i].SetInfo(Info["button_name"],Info["button_desc"],Info["button_icon"],"no")
			self.sideBarItem[i].Show()
			y = y + 32

		self.Show()

class EasySideBarItem(ui.ScriptWindow):

	def __init__(self, wndSideBar):
		ui.ScriptWindow.__init__(self)
		self.wndSideBar = wndSideBar
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		self.SetSize(32,32)	
		
		self.Background = ui.ThinBoardCircle()
		self.Background.SetParent(self)
		self.Background.SetPosition(0,0)
		self.Background.SetSize(32,32)
		self.Background.Show()
		
		self.icon = ui.ImageBox()
		self.icon.SetParent(self.Background)
		self.icon.SetPosition(0,0)
		self.icon.LoadImage("icon/item/" + str(app.GetRandom(30001,30006)) + ".tga")
		self.icon.Show()
		
		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(31, 32)
		self.mouseReflector.UpdateRect()
		
		
		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.SetParent(self)
		self.toolTip.SetPosition(-195, 0)
		self.toolTip.SetFollow(False)
		
		
		self.toolTip.ClearToolTip()
		self.toolTip.AppendSpace(2)
		self.toolTip.SetTitle("Button Test 1")
		self.toolTip.AppendDescription("Macht noch nix... Ist nur ein Prototype. OK braucht noch mehr Text bla Bla bla.... Immernoch nicht genug? puhh keine Ahnung...",26)
		self.toolTip.AppendSpace(5)
		self.toolTip.ResizeToolTip()
		self.toolTip.Show()
		
		self.Show()
		
	def SetInfo(self,title,desc,image,func):
		try:
			self.icon.LoadImage(image)
		except:
			self.icon.LoadImage("icon/item/30001.tga")
			
		self.toolTip.ClearToolTip()
		self.toolTip.AppendSpace(2)
		self.toolTip.SetTitle(title)
		self.toolTip.AppendDescription(desc,26)
		self.toolTip.AppendSpace(5)
		self.toolTip.ResizeToolTip()
		self.toolTip.Show()
			
			
	def OnUpdate(self):
		if self.icon.IsIn():
			self.mouseReflector.Show()
			self.toolTip.Show()
		else:
			self.mouseReflector.Hide()
			self.toolTip.Hide()
			
class CurrencyDescriptionToolTip(ui.Window):
	CURRENCY_GOLD = 0
	CURRENCY_ACHIEVEMENT = 1
	CURRENCY_DUNGEON = 2

	normalWidth = 190
	currencyDesc = {
		CURRENCY_GOLD : localeInfo.CURRENCY_GOLD_DESCRIPTION,
		CURRENCY_ACHIEVEMENT : localeInfo.CURRENCY_ACHIEVEMENT_DESCRIPTION,
		CURRENCY_DUNGEON : localeInfo.CURRENCY_DUNGEON_DESCRIPTION,
	}
	
	def __init__(self,wndInventory):
		ui.Window.__init__(self)
		self.wndInventory = wndInventory
		self.SetSize(self.normalWidth,100)
		self.currency = 0
		self.Hide()
		self.MakeToolTip()	
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def AdjustPosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		self.SetPosition(x - self.normalWidth - 10 + 22,(y + 650)-self.toolTip.toolTipHeight)
		
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetParent(self)
		toolTip.SetPosition(1, 1)
		toolTip.SetFollow(False)
		toolTip.Show()
		self.toolTip = toolTip
	
	def Open(self,currency):
		self.currency = currency
		self.toolTip.ClearToolTip()
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendDescription(self.currencyDesc[currency],26)
		self.toolTip.AppendSpace(5)
		self.toolTip.ResizeToolTip()	
		self.AdjustPosition()
		self.Show()
		
	def Close(self,currency):
		if currency == self.currency:
			self.Hide()
		
class InventorySortDropDownMenu(ui.ScriptWindow):
	wndInventory = 0

	INVENTORY_SORT_TYPE_NOTHING = 0
	INVENTORY_SORT_TYPE_IGNORE = 1
	INVENTORY_SORT_TYPE_EQ = 2
	INVENTORY_SORT_TYPE_RM	= 3
	INVENTORY_SORT_TYPE_TREASURES = 4
	INVENTORY_SORT_TYPE_SPECIAL	= 5
	
	sortList = [
		localeInfo.INVENTORY_SORT_NOTHING,
		localeInfo.INVENTORY_SORT_IGNORE,
		localeInfo.INVENTORY_SORT_EQUIPMENT,
		localeInfo.INVENTORY_SORT_REFINE_MATERIAL,
		localeInfo.INVENTORY_SORT_TREASURES,
		localeInfo.INVENTORY_SORT_SPECIAL,
	]
	
	sortTypeItem = {}
	sortTypeButtons = {}
	
	def __init__(self, wndInventory):
		ui.ScriptWindow.__init__(self)
		self.wndInventory = wndInventory;
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):	
		self.background = ui.ThinBoardCircle()
		self.background.SetParent(self)
		self.background.SetPosition(0,0)
		self.background.Show()
		
		
		i = 0
		y = 0
		
		while i < len(self.sortList):
		
			self.sortTypeItem[i] = InventorySortDropDownMenuItem()
			self.sortTypeItem[i].SetParent(self)
			self.sortTypeItem[i].SetPosition(0,y)
			self.sortTypeItem[i].SetText(self.sortList[i])
			self.sortTypeItem[i].Show()
					
			self.sortTypeButtons[i] = ui.Button()
			self.sortTypeButtons[i].SetParent(self)
			self.sortTypeButtons[i].SetPosition(0,y)
			self.sortTypeButtons[i].SetSize(160,20)
			self.sortTypeButtons[i].SetEvent(self.OnToogleSortItem,i)
			self.sortTypeButtons[i].Show()
			
			
			i = i + 1
			y = y + 20
		
		# self.sortTypeItem[0].SetActive()
		self.OnToogleSortItem(0)
	def OnToogleSortItem(self,button):
		for i in xrange(len(self.sortTypeItem)):
			if i == button:
				self.sortTypeItem[i].SetActive()
				self.sortTypeButtons[i].Disable()
			else:
				self.sortTypeItem[i].SetInactive()
				self.sortTypeButtons[i].Enable()

		self.wndInventory.wndSortText.SetText(self.sortList[button])
		
	def SetMenuSize(self,heigth):
		self.SetSize(160,heigth)
		self.background.SetSize(160,heigth+1)
		
	def Open(self):
		if self.IsShow():
			self.Hide()
		else:
			self.Show()
			
class InventorySortDropDownMenuItem(ui.ScriptWindow):

	COLOR_INACTIVE = grp.GenerateColor(1.0, 0.0, 0.0, 0.2)
	COLOR_ACTIVE   = grp.GenerateColor(0.0, 1.0, 0.0, 0.2)
	
	STATUS_ACTIVE = 1
	STATUS_INACTIVE = 0
	
	wndDropDownMenu = 0
	status = 0
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		# self.wndDropDownMenu = wndDropDownMenu
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		self.SetSize(160,20)
	
		self.background = ui.Bar()
		self.background.SetParent(self)
		self.background.SetSize(158,19)
		self.background.SetPosition(1,1)
		self.background.SetColor(self.COLOR_INACTIVE)
		self.background.Show()
		
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self.background)
		self.textLine.SetPosition(80,8)
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.Show()
		

	def SetText(self,textLine):
		self.textLine.SetText(str(textLine))
		
	def SetActive(self):
		self.status = self.STATUS_ACTIVE
		self.background.SetColor(self.COLOR_ACTIVE)
		
	def SetInactive(self):
		self.status = self.STATUS_INACTIVE
		self.background.SetColor(self.COLOR_INACTIVE)
	
class GoldSafeWindow(ui.ScriptWindow):
	
	goldSafeVnum = [30251,30252,30253]
	goldSafePrice = [100000000,500000000,1000000000]
	
	def __init__(self, wndInventory):
		ui.ScriptWindow.__init__(self)
		self.wndInventory = wndInventory;
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/goldsafe.py")
		except:
			import exception
			exception.Abort("GoldSafe.LoadWindow.LoadObject")	

		self.moneySafeToolTip = uiToolTip.ItemToolTip()  
		self.moneySafeToolTip.HideToolTip()			
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.moneySafeSlot01 = self.GetChild("moneySlot_01_slot")
		self.moneySafeSlot02 = self.GetChild("moneySlot_02_slot")
		self.moneySafeSlot03 = self.GetChild("moneySlot_03_slot")
		
		self.moneySafeButton01 = self.GetChild("moneySlot_01_button")
		self.moneySafeButton02 = self.GetChild("moneySlot_02_button")
		self.moneySafeButton03 = self.GetChild("moneySlot_03_button")

		self.moneySafeButton01.SetEvent(self.OnCreateGoldSafe,1)
		self.moneySafeButton02.SetEvent(self.OnCreateGoldSafe,2)
		self.moneySafeButton03.SetEvent(self.OnCreateGoldSafe,3)
		
		self.moneySafeSlot01.SetItemSlot(0,self.goldSafeVnum[0],0)
		self.moneySafeSlot02.SetItemSlot(1,self.goldSafeVnum[1],0)
		self.moneySafeSlot03.SetItemSlot(2,self.goldSafeVnum[2],0)
		
		self.moneySafeSlot01.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.moneySafeSlot01.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip)) 		

		self.moneySafeSlot02.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.moneySafeSlot02.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip)) 		

		self.moneySafeSlot03.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.moneySafeSlot03.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip)) 		

	def ShowToolTip(self,slot):
		self.moneySafeToolTip.ClearToolTip()
		self.moneySafeToolTip.AddItemData(self.goldSafeVnum[slot], [0, 0, 0, 0, 0, 0])
		self.moneySafeToolTip.ShowToolTip()
		
	def HideToolTip(self):
		self.moneySafeToolTip.HideToolTip()
		
	def GetBasePosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		return x - 390, y + 490
		
	def AdjustPosition(self):
		bx, by = self.GetBasePosition()
		self.SetPosition(bx, by)
	
	# def OnUpdate(self):
		# self.UpdateCountAndPriceCheck()
	
	def UpdateCountAndPriceCheck(self):
		gold = player.GetElk()
	
		if gold >= self.goldSafePrice[0]:
			count100GoldSafe = int(gold/self.goldSafePrice[0])
			self.moneySafeSlot01.SetSlotCount(0,count100GoldSafe)
			self.moneySafeButton01.Enable()
			self.moneySafeButton01.SetText(localeInfo.GOLDSAFE_BUTTON_CREATE)
		else:
			self.moneySafeSlot01.SetSlotCount(0,0)
			self.moneySafeButton01.Disable()			
			self.moneySafeButton01.SetText(localeInfo.GOLDSAFE_BUTTON_NO_GOLD)	

	
		if gold >= self.goldSafePrice[1]:
			count500GoldSafe = int(gold/self.goldSafePrice[1])
			self.moneySafeSlot02.SetSlotCount(1,count500GoldSafe)
			self.moneySafeButton02.Enable()
			self.moneySafeButton02.SetText(localeInfo.GOLDSAFE_BUTTON_CREATE)
		else:
			self.moneySafeSlot02.SetSlotCount(1,0)
			self.moneySafeButton02.Disable()
			self.moneySafeButton02.SetText(localeInfo.GOLDSAFE_BUTTON_NO_GOLD)	

		if gold >= self.goldSafePrice[2]:
			count1000GoldSafe = int(gold/self.goldSafePrice[2])
			self.moneySafeSlot03.SetSlotCount(2,count1000GoldSafe)
			self.moneySafeButton03.Enable()
			self.moneySafeButton03.SetText(localeInfo.GOLDSAFE_BUTTON_CREATE)
		else:
			self.moneySafeSlot03.SetSlotCount(2,0)
			self.moneySafeButton03.Disable()
			self.moneySafeButton03.SetText(localeInfo.GOLDSAFE_BUTTON_NO_GOLD)	
	
	
	
	def OnCreateGoldSafe(self,idx):
		constInfo.INPUT_CMD = str(idx)
		event.QuestButtonClick(settinginfo.GoldStorageQID)				
	
	def Open(self):
		if self.IsShow():
			self.Hide()
		else:
			self.AdjustPosition()
			self.Show()

			
	def Close(self):
		self.Hide()
	
class CostumeWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception
		
		if not app.ENABLE_COSTUME_SYSTEM:			
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return						
			 	 
		ui.ScriptWindow.__init__(self)

		self.isLoaded = 0
		self.wndInventory = wndInventory;

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		self.RefreshCostumeSlot()

		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/CostumeWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			wndEquip = self.GetChild("CostumeSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		## Equipment
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))						
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndEquip = wndEquip
		self.AdjustPosition()

	def RefreshCostumeSlot(self):
		getItemVNum=player.GetItemIndex
		
		for i in xrange(item.COSTUME_SLOT_COUNT):
			slotNumber = item.COSTUME_SLOT_START + i
			self.wndEquip.SetItemSlot(slotNumber, getItemVNum(slotNumber), 0)
		self.wndEquip.SetItemSlot(item.EQUIPMENT_COSTUME_WEAPON, getItemVNum(item.EQUIPMENT_COSTUME_WEAPON), 0)

		self.wndEquip.RefreshSlot()

	def GetBasePosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		return x - 180, y
		
	def AdjustPosition(self):
		bx, by = self.GetBasePosition()
		self.SetPosition(bx, by)
		
class BeltInventoryWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception
		
		if not app.ENABLE_NEW_EQUIPMENT_SYSTEM:			
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return						
			 	 
		ui.ScriptWindow.__init__(self)

		self.isLoaded = 0
		self.wndInventory = wndInventory;
		
		self.wndBeltInventoryLayer = None
		self.wndBeltInventorySlot = None
		self.expandBtn = None
		self.minBtn = None

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self, openBeltSlot = FALSE):
		self.__LoadWindow()
		self.RefreshSlot()

		ui.ScriptWindow.Show(self)
		
		if openBeltSlot:
			self.OpenInventory()
		else:
			self.CloseInventory()

	def Close(self):
		self.Hide()

	def IsOpeningInventory(self):
		return self.wndBeltInventoryLayer.IsShow()
		
	def OpenInventory(self):
		self.wndBeltInventoryLayer.Hide()
		self.expandBtn.Hide()

		if localeInfo.IsARABIC() == 0:
			self.AdjustPositionAndSize()
				
	def CloseInventory(self):
		self.wndBeltInventoryLayer.Hide()
		self.expandBtn.Hide()
		
		if localeInfo.IsARABIC() == 0:
			self.AdjustPositionAndSize()

	## 현재 인벤토리 위치를 기준으로 BASE 위치를 계산, 리턴.. 숫자 하드코딩하기 정말 싫지만 방법이 없다..
	def GetBasePosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		return x - 148, y + 241
		
	def AdjustPositionAndSize(self):
		bx, by = self.GetBasePosition()
		
		if self.IsOpeningInventory():			
			self.SetPosition(bx, by)
			self.SetSize(self.ORIGINAL_WIDTH, self.GetHeight())
			
		else:
			self.SetPosition(bx + 138, by);
			self.SetSize(10, self.GetHeight())

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/BeltInventoryWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			self.ORIGINAL_WIDTH = self.GetWidth()
			wndBeltInventorySlot = self.GetChild("BeltInventorySlot")
			self.wndBeltInventoryLayer = self.GetChild("BeltInventoryLayer")
			self.expandBtn = self.GetChild("ExpandBtn")
			self.minBtn = self.GetChild("MinimizeBtn")
			
			self.expandBtn.SetEvent(ui.__mem_func__(self.OpenInventory))
			self.minBtn.SetEvent(ui.__mem_func__(self.CloseInventory))
			
			if localeInfo.IsARABIC() :
				self.expandBtn.SetPosition(self.expandBtn.GetWidth() - 2, 15)
				self.wndBeltInventoryLayer.SetPosition(self.wndBeltInventoryLayer.GetWidth() - 5, 0)
				self.minBtn.SetPosition(self.minBtn.GetWidth() + 3, 15)			
	
			for i in xrange(item.BELT_INVENTORY_SLOT_COUNT):
				slotNumber = item.BELT_INVENTORY_SLOT_START + i							
				wndBeltInventorySlot.SetCoverButton(slotNumber,	"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/belt_inventory/slot_disabled.tga", FALSE, FALSE)									
			
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		## Equipment
		wndBeltInventorySlot.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndBeltInventorySlot.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndBeltInventorySlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndBeltInventorySlot.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))						
		wndBeltInventorySlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndBeltInventorySlot.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndBeltInventorySlot = wndBeltInventorySlot

	def RefreshSlot(self):
		getItemVNum=player.GetItemIndex
		
		for i in xrange(item.BELT_INVENTORY_SLOT_COUNT):
			slotNumber = item.BELT_INVENTORY_SLOT_START + i
			self.wndBeltInventorySlot.SetItemSlot(slotNumber, getItemVNum(slotNumber), player.GetItemCount(slotNumber))
			self.wndBeltInventorySlot.SetAlwaysRenderCoverButton(slotNumber, TRUE)
			
			avail = "0"
			
			if player.IsAvailableBeltInventoryCell(slotNumber):
				self.wndBeltInventorySlot.EnableCoverButton(slotNumber)				
			else:
				self.wndBeltInventorySlot.DisableCoverButton(slotNumber)				

		self.wndBeltInventorySlot.RefreshSlot()
		
class InventoryWindow(ui.ScriptWindow):
	liHighlightedItems = []
	USE_TYPE_TUPLE = ("USE_CLEAN_SOCKET", "USE_CHANGE_ATTRIBUTE", "USE_ADD_ATTRIBUTE", "USE_ADD_ATTRIBUTE2", "USE_ADD_ACCESSORY_SOCKET", "USE_PUT_INTO_ACCESSORY_SOCKET", "USE_PUT_INTO_BELT_SOCKET", "USE_PUT_INTO_RING_SOCKET")

	questionDialog = None
	tooltipItem = None
	wndCostume = None
	lastGold = None
	wndBelt = None
	dlgPickMoney = None
	dlgCreateGoldSafe = None
	sideBar = None
	dlgSelectInventorySort = None
	sellingSlotNumber = -1
	isLoaded = 0
	isOpenedCostumeWindowWhenClosingInventory = 0		# 인벤토리 닫을 때 코스츔이 열려있었는지 여부-_-; 네이밍 ㅈㅅ
	isOpenedBeltWindowWhenClosingInventory = 0		# 인벤토리 닫을 때 벨트 인벤토리가 열려있었는지 여부-_-; 네이밍 ㅈㅅ

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.isOpenedBeltWindowWhenClosingInventory = 0		# 인벤토리 닫을 때 벨트 인벤토리가 열려있었는지 여부-_-; 네이밍 ㅈㅅ

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

		# 인벤토리를 닫을 때 코스츔이 열려있었다면 인벤토리를 열 때 코스츔도 같이 열도록 함.
		if self.isOpenedCostumeWindowWhenClosingInventory and self.wndCostume:
			self.wndCostume.Show() 

		# 인벤토리를 닫을 때 벨트 인벤토리가 열려있었다면 같이 열도록 함.
		if self.wndBelt:
			self.wndBelt.Show(self.isOpenedBeltWindowWhenClosingInventory)

	def BindInterfaceClass(self, interface):
		self.interface = interface
		
	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()

			if ITEM_MALL_BUTTON_ENABLE:
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "InventoryWindow.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/InventoryWindow.py")
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.LoadObject")

		try:
			wndItem = self.GetChild("ItemSlot")
			wndEquip = self.GetChild("EquipmentSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.wndMoney = self.GetChild("Money")
			self.wndMoneySlot = self.GetChild("Money_Slot")
			self.wndAchievementSlot = self.GetChild("achievementBackground")
			self.wndDungeonSlot = self.GetChild("dungeonBackground")
			
			
			
			# self.DSSButton = self.GetChild2("DSSButton")
			self.costumeButton = self.GetChild2("CostumeButton")
			self.wndAps = self.GetChild("AchievementPoints")
			# self.wndApsSlot = self.GetChild("Aps_Slot") ##Inventar AP Anzeige
			# self.wndDps = self.GetChild("DPs") ##Inventar DP Anzeige				
			# self.wndDpsSlot = self.GetChild("Dps_Slot") ##Inventar DP Anzeige
			# self.wndDCs = self.GetChild("DC") ##Inventar AP Anzeige
			# self.wndDCSlot = self.GetChild("DC_Slot") ##Inventar AP Anzeige
			
			self.wndSortBG = self.GetChild("inventory_sort_bg")
			self.wndSortText = self.GetChild("inventory_sort_textline")
			self.wndSortButton = self.GetChild("inventory_sort_button")
			# self.inventoryTab = []
			# self.inventoryTab.append(self.GetChild("Inventory_Tab_01"))
			# self.inventoryTab.append(self.GetChild("Inventory_Tab_02"))
			# self.inventoryTab.append(self.GetChild("Inventory_Tab_03"))
			# self.inventoryTab.append(self.GetChild("Inventory_Tab_04"))

			self.inventoryPageButton = []
			self.inventoryPageButton.append(self.GetChild("page_I_Button"))
			self.inventoryPageButton.append(self.GetChild("page_II_Button"))
			self.inventoryPageButton.append(self.GetChild("page_III_Button"))
			self.inventoryPageButton.append(self.GetChild("page_IV_Button"))
			self.inventoryPageButton.append(self.GetChild("page_V_Button"))

			self.inventoryPageButton.append(self.GetChild("page_VI_Button"))
			self.inventoryPageButton.append(self.GetChild("page_VII_Button"))
			self.inventoryPageButton.append(self.GetChild("page_VIII_Button"))
			self.inventoryPageButton.append(self.GetChild("page_IX_Button"))
			self.inventoryPageButton.append(self.GetChild("page_X_Button"))
			
			self.inventoryPageButtonBackground = []
			self.inventoryPageButtonBackground.append(self.GetChild("page_I_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_II_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_III_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_IV_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_V_ClickedBG"))
			
			self.inventoryPageButtonBackground.append(self.GetChild("page_VI_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_VII_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_VIII_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_IX_ClickedBG"))
			self.inventoryPageButtonBackground.append(self.GetChild("page_X_ClickedBG"))
			
			# self.equipmentTab = []
			# self.equipmentTab.append(self.GetChild("Equipment_Tab_01"))
			# self.equipmentTab.append(self.GetChild("Equipment_Tab_02"))
			
			# self.IStorageDropDownBoard = self.GetChild("DropDownBoard")
			# self.IStorageDropDownBoard.Hide()

			# self.GoldStorageDropDownBoard = self.GetChild("DropDownBoard2")
			# self.GoldStorageDropDownBoard.Hide()

			# self.DropDownButton1 = self.GetChild("DropDownButton1") # ItemLager
			# self.DropDownButton2 = self.GetChild("DropDownButton2") # Itemshop-Lager
			# self.DropDownButton3 = self.GetChild("DropDownButton3") # Gildelager
			# self.DropDownButton4 = self.GetChild("DropDownButton4") # FB-Lager
			# self.DropDownButton5 = self.GetChild("DropDownButton5") # UppItem-Lager
			
			# self.DropDownButton2_1 = self.GetChild("DropDownButton2_1") # 100kk 
			# self.DropDownButton2_2 = self.GetChild("DropDownButton2_2") # 500kk
			# self.DropDownButton2_3 = self.GetChild("DropDownButton2_3") # 1kkk
			
			# self.DropDownButton2_1.SetEvent(self.__OnClickDropDownButton2,1)
			# self.DropDownButton2_2.SetEvent(self.__OnClickDropDownButton2,2)
			# self.DropDownButton2_3.SetEvent(self.__OnClickDropDownButton2,3)				
			
			
			# self.DropDownButton1.SetEvent(self.__OnClickDropDownButton,1)
			# self.DropDownButton2.SetEvent(self.__OnClickDropDownButton,2)
			# self.DropDownButton3.SetEvent(self.__OnClickDropDownButton,3)	
			# self.DropDownButton4.SetEvent(self.__OnClickDropDownButton,4)	
			# self.DropDownButton5.SetEvent(self.__OnClickDropDownButton,5)	

			self.wndSortButton.SetEvent(self.OpenInventorySortDialog)

			
			if self.costumeButton and not app.ENABLE_COSTUME_SYSTEM:
				self.costumeButton.Hide()
				self.costumeButton.Destroy()
				self.costumeButton = 0

			# Belt Inventory Window
			self.wndBelt = None
			
			if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
				self.wndBelt = BeltInventoryWindow(self)
			
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.BindObject")

		## Item
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## Equipment
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## PickMoneyDialog
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.Hide()
		
		
		## SafeGoldDialog
		
		self.dlgCreateGoldSafe = GoldSafeWindow(self)
		self.dlgSelectInventorySort = InventorySortDropDownMenu(self)
		self.dlgSelectInventorySort.SetParent(self)
		self.dlgSelectInventorySort.SetPosition(20+22,294+20)
		self.dlgSelectInventorySort.SetMenuSize(6*20)
		
		
		self.currencyToolTip = CurrencyDescriptionToolTip(self)
		self.devItemToolTip = DEVItemInformation(self)
		
		self.sideBar = SuperAwesomeIMBAKrassSideBarPrototypeJaKriegtNochAnderenCLASSNameHaHa(self)
		self.sideBar.SetParent(self)
		self.sideBar.SetPosition(0, 90)
		# self.dlgCrateGoldSafe.Open()

		## RefineDialog
		self.refineDialog = uiRefine.RefineDialog()
		self.refineDialog.Hide()

		## AttachMetinDialog
		self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
		self.attachMetinDialog.Hide()
		
		
		self.costumeAttributeChange = CostumeAttributeChanger(self)
		self.costumeAttributeChange.Hide()
		self.costumeAttributeChange.AdjustPosition()
		## MoneySlot
		self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))
		
		self.mouseReflector = MouseReflector(self.wndMoneySlot)
		self.mouseReflector.SetSize(160, 20)
		# self.mouseReflector.SetPosition(5,5)
		self.mouseReflector.UpdateRect()

		self.mouseReflector1 = MouseReflector(self.wndSortBG)
		self.mouseReflector1.SetSize(160, 20)
		self.mouseReflector1.UpdateRect()
		
		self.inventoryPageButton[0].SetEvent(lambda arg=0: self.SetInventoryPage(arg))
		self.inventoryPageButton[1].SetEvent(lambda arg=1: self.SetInventoryPage(arg))
		self.inventoryPageButton[2].SetEvent(lambda arg=2: self.SetInventoryPage(arg))
		self.inventoryPageButton[3].SetEvent(lambda arg=3: self.SetInventoryPage(arg))
		
		
		self.inventoryPageButton[1].SetPosition(0,0)
		self.inventoryPageButton[2].SetPosition(0,0)
		self.inventoryPageButton[3].SetPosition(0,0)
		self.inventoryPageButton[4].SetPosition(0,0)
		self.inventoryPageButton[5].SetPosition(0,0)
		self.inventoryPageButton[6].SetPosition(0,0)
		self.inventoryPageButton[7].SetPosition(0,0)
		self.inventoryPageButton[8].SetPosition(0,0)
		self.inventoryPageButton[9].SetPosition(0,0)
		
		self.inventoryPageButtonBackground[1].Hide()
		self.inventoryPageButtonBackground[2].Hide()
		self.inventoryPageButtonBackground[3].Hide()
		self.inventoryPageButtonBackground[4].Hide()		
		self.inventoryPageButtonBackground[5].Hide()
		self.inventoryPageButtonBackground[6].Hide()
		self.inventoryPageButtonBackground[7].Hide()
		self.inventoryPageButtonBackground[8].Hide()
		self.inventoryPageButtonBackground[9].Hide()
		
		
		# self.inventoryTab[0].Down()
		
		self.inventoryPageIndex = 0

		# self.equipmentTab[0].SetEvent(lambda arg=0: self.SetEquipmentPage(arg))
		# self.equipmentTab[1].SetEvent(lambda arg=1: self.SetEquipmentPage(arg))
		# self.equipmentTab[0].Down()
		# self.equipmentTab[0].Hide()
		# self.equipmentTab[1].Hide()

		self.wndItem = wndItem
		self.wndEquip = wndEquip
		self.dlgPickMoney = dlgPickMoney

		
		
		
		# MallButton
		# if self.mallButton:
			# self.mallButton.SetEvent(ui.__mem_func__(self.ClickMallButton))

		# if self.DSSButton:
			# self.DSSButton.SetEvent(ui.__mem_func__(self.ClickDSSButton)) 
			
		# Geldspeicher
		# if self.YangSpeicher:
			# self.YangSpeicher.SetEvent(ui.__mem_func__(self.ClickYangSpeicherButton))
		
		# Costume Button
		if self.costumeButton:
			self.costumeButton.SetEvent(ui.__mem_func__(self.ClickCostumeButton))

		self.wndCostume = None
		self.listUnusableSlot = []
		
 		#####

		## Refresh
		self.SetInventoryPage(0)
		# self.SetEquipmentPage(0)
		self.RefreshItemSlot()
		self.RefreshStatus()
	
	
	def OpenInventorySortDialog(self):
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "BAAAAM!!!")
		self.dlgSelectInventorySort.Open()
		
	# def __OnClickDropDownButton2(self,idx):
		# constInfo.INPUT_CMD = str(idx)
		# event.QuestButtonClick(settinginfo.GoldStorageQID)	

		
	# def __OnClickDropDownButton(self,idx):
		# if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "Das geht nicht solange du einen laden offen hast.")
			# return
		# if settinginfo.BoxOpenerOpen == 1:
			# return
		# if idx == 1:
			# import event
			# event.QuestButtonClick(int(constInfo.mallqin))
		# elif idx == 2:
			# GFHhg54GHGhh45GHGH.SendChatPacket("/click_mall")
		# elif idx == 3:
			# import event
			# constInfo.GUILDSTORAGE["questCMD"] = 'OPEN'
			# event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
			
		# elif idx == 4:
			# if settinginfo.SkillBookStorageOpen == 0:
				# import uiskillbook
				# uiskillbook.SkillBookBoard().Show()		
				
		# elif idx == 5:
			# if settinginfo.UppItemStorageOpen == 0:
				# import uiuppstorage
				# uiuppstorage.UppStorageBoard().Show()		
				
		
	def Destroy(self):
		self.ClearDictionary()

		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = 0

		self.refineDialog.Destroy()
		self.refineDialog = 0

		self.attachMetinDialog.Destroy()
		self.attachMetinDialog = 0
		
		self.costumeAttributeChange = 0

		self.tooltipItem = None
		self.lastGold = None
		self.wndItem = 0
		self.wndEquip = 0
		self.dlgPickMoney = 0
		self.wndMoney = 0
		self.wndMoneySlot = 0
		self.questionDialog = None
		# self.mallButton = None
		# self.DSSButton = None
		self.interface = None
		
		self.wndAps = 0 ##Iventar AP Anzeige
		# self.wndApsSlot = 0 ##Inventar AP Anzeige

		if self.wndCostume:
			self.wndCostume.Destroy()
			self.wndCostume = 0
			
		if self.wndBelt:
			self.wndBelt.Destroy()
			self.wndBelt = None

		if self.dlgCreateGoldSafe:
			self.dlgCreateGoldSafe = None
			
		if self.sideBar:
			self.sideBar = None
			
		if self.dlgSelectInventorySort:
			self.dlgSelectInventorySort = None
			
		# self.inventoryTab = []
		# self.equipmentTab = []

	def Hide(self):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			self.OnCloseQuestionDialog()
			return
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

		if self.wndCostume:
			self.isOpenedCostumeWindowWhenClosingInventory = self.wndCostume.IsShow()			# 인벤토리 창이 닫힐 때 코스츔이 열려 있었는가?
			self.wndCostume.Close()
 
		if self.wndBelt:
			self.isOpenedBeltWindowWhenClosingInventory = self.wndBelt.IsOpeningInventory()		# 인벤토리 창이 닫힐 때 벨트 인벤토리도 열려 있었는가?
			print "Is Opening Belt Inven?? ", self.isOpenedBeltWindowWhenClosingInventory
			self.wndBelt.Close()
  
		if self.dlgPickMoney:
			self.dlgPickMoney.Close()
			
		if self.dlgCreateGoldSafe:
			self.dlgCreateGoldSafe.Close()
		
		
		# if self.sideBar:
			# self.sideBar.Hide()
		
		if self.dlgSelectInventorySort:
			self.dlgSelectInventorySort.Hide()
		
		wndMgr.Hide(self.hWnd)
		
	
	def Close(self):
		self.Hide()

	def SetInventoryPage(self, page):
		self.inventoryPageButtonBackground[self.inventoryPageIndex].Hide()
		self.inventoryPageButton[self.inventoryPageIndex].SetPosition(0,0)
		
		self.inventoryPageIndex = page
		self.inventoryPageButtonBackground[self.inventoryPageIndex].Show()
		self.inventoryPageButton[self.inventoryPageIndex].SetPosition(0,-1)

		self.RefreshBagSlotWindow()

	# def SetEquipmentPage(self, page):
		# self.equipmentPageIndex = page
		# self.equipmentTab[1-page].SetUp()
		# self.RefreshEquipSlotWindow()
		
	# def ClickMallButton(self):
		# if background.GetCurrentMapName() == "map_login" or background.GetCurrentMapName() == "map_intro":
			# chat.AppendChat(chat.CHAT_TYPE_INFO,"Du kannst von hier aus nicht auf das Lager zugreifen!")
			# return	
	
		# if self.IStorageDropDownBoard.IsShow():
			# self.IStorageDropDownBoard.Hide()
		# else:
			# self.IStorageDropDownBoard.SetTop()
			# self.IStorageDropDownBoard.Show()

	# DSSButton
	# def ClickDSSButton(self):
		# print "click_dss_button"
		# self.interface.ToggleDragonSoulWindow()

	def ClickCostumeButton(self):
		print "Click Costume Button"
		if self.wndCostume:
			if self.wndCostume.IsShow(): 
				self.wndCostume.Hide()
			else:

				self.wndCostume.AdjustPosition()
				self.wndCostume.Show()
		else:
			self.wndCostume = CostumeWindow(self)
			self.wndCostume.Show()
			
			
	# def ClickYangSpeicherButton(self):
		# if self.GoldStorageDropDownBoard.IsShow():
			# self.GoldStorageDropDownBoard.Hide()
		# else:
			# self.GoldStorageDropDownBoard.SetTop()
			# self.GoldStorageDropDownBoard.Show()

	def OpenPickMoneyDialog(self):
		self.dlgCreateGoldSafe.Open()
		# if mouseModule.mouseController.isAttached():

			# attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			# if player.SLOT_TYPE_SAFEBOX == mouseModule.mouseController.GetAttachedType():

				# if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					# GFHhg54GHGhh45GHGH.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					# snd.PlaySound("sound/ui/money.wav")

			# mouseModule.mouseController.DeattachObject()

		# else:
			# curMoney = player.GetElk()

			# if curMoney <= 0:
				# return

			# self.dlgPickMoney.SetTitleName(localeInfo.PICK_MONEY_TITLE)
			# self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
			# self.dlgPickMoney.Open(curMoney)
			# self.dlgPickMoney.SetMax(7) # 인벤토리 990000 제한 버그 수정

	def OnPickMoney(self, money):
		mouseModule.mouseController.AttachMoney(self, player.SLOT_TYPE_INVENTORY, money)

	def OnPickItem(self, count):
		itemSlotIndex = self.dlgPickMoney.itemGlobalSlotIndex
		selectedItemVNum = player.GetItemIndex(itemSlotIndex)
		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, count)

	def __InventoryLocalSlotPosToGlobalSlotPos(self, local):
		if player.IsEquipmentSlot(local) or player.IsCostumeSlot(local) or (app.ENABLE_NEW_EQUIPMENT_SYSTEM and player.IsBeltInventorySlot(local)):
			return local

		return self.inventoryPageIndex*player.INVENTORY_PAGE_SIZE + local

	def RefreshBagSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndItem.SetItemSlot
		
		for i in xrange(player.INVENTORY_PAGE_SIZE):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
			
			itemCount = getItemCount(slotNumber)
			if 0 == itemCount:
				self.wndItem.ClearSlot(i)
				continue
			elif 1 == itemCount:
				itemCount = 0
				
			itemVnum = getItemVNum(slotNumber)
			setItemVNum(i, itemVnum, itemCount)
			# if constInfo.IS_PET_SEAL(itemVnum):
				# metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				# if slotNumber >= player.INVENTORY_PAGE_SIZE and slotNumber < player.INVENTORY_PAGE_SIZE*2:
					# slotNumber -= player.INVENTORY_PAGE_SIZE
				# elif slotNumber >= player.INVENTORY_PAGE_SIZE*2 and slotNumber < player.INVENTORY_PAGE_SIZE*3:
					# slotNumber -= player.INVENTORY_PAGE_SIZE*2
				# elif slotNumber >= player.INVENTORY_PAGE_SIZE*3:
					# slotNumber -= player.INVENTORY_PAGE_SIZE*3
				# isActivated = 0 != metinSocket[0]
	
				# if isActivated:				
					# self.wndItem.ActivateSlot(slotNumber)
				# else:
					# self.wndItem.DeactivateSlot(slotNumber)
			
			if constInfo.avilable > 0 and constInfo.avilable < 4:
				self.RefreshBagSlotWindowOnAvilable()
			if constInfo.IS_AUTO_POTION(itemVnum):
				# metinSocket - [0] : 활성화 여부, [1] : 사용한 양, [2] : 최대 용량
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]	
				
				if slotNumber >= player.INVENTORY_PAGE_SIZE:
					slotNumber -= player.INVENTORY_PAGE_SIZE
					
				isActivated = 0 != metinSocket[0]
				
				if isActivated:
					self.wndItem.ActivateSlot(slotNumber)
					potionType = 0;
					if constInfo.IS_AUTO_POTION_HP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_HP
					elif constInfo.IS_AUTO_POTION_SP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_SP						
					
					usedAmount = int(metinSocket[1])
					totalAmount = int(metinSocket[2])					
					player.SetAutoPotionInfo(potionType, isActivated, (totalAmount - usedAmount), totalAmount, self.__InventoryLocalSlotPosToGlobalSlotPos(i))
					
				else:
					self.wndItem.DeactivateSlot(slotNumber)
		self.wndItem.RefreshSlot()
		
		if self.wndCostume:
			self.wndCostume.RefreshCostumeSlot()
		
		if self.dlgCreateGoldSafe:
			self.dlgCreateGoldSafe.UpdateCountAndPriceCheck()
		
	def RefreshEquipSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndEquip.SetItemSlot
		for i in xrange(player.EQUIPMENT_PAGE_COUNT):
			slotNumber = player.EQUIPMENT_SLOT_START + i
			itemCount = getItemCount(slotNumber)
			if itemCount <= 1:
				itemCount = 0
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)

		if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
			for i in xrange(player.NEW_EQUIPMENT_SLOT_COUNT):
				slotNumber = player.NEW_EQUIPMENT_SLOT_START + i
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
				print "ENABLE_NEW_EQUIPMENT_SYSTEM", slotNumber, itemCount, getItemVNum(slotNumber)
				
				
				
				
				

	def RefreshItemSlot(self):
		self.RefreshBagSlotWindow()
		self.RefreshEquipSlotWindow()
	
	# def SetDragonCoins(self,points):
		# self.wndDCs.SetText(constInfo.NumberToPointString(points) + " DC's")
	
	def RefreshStatus(self):
		import systemSetting
		
		
		# iLastGold    = self.lastGold
		# iGoldNow    = player.GetElk()
		# gIncrease    = 1 if (not (iGoldNow - iLastGold) / 10000 > 0) else 10000
		# for goldLoop in range(iLastGold, iGoldNow + 1, gIncrease):
			# goldLoop    = goldLoop
			# iGoldNow    = iGoldNow
			# self.wndMoney.SetText(localeInfo.NumberToMoneyString(goldLoop))
			# if (goldLoop == iGoldNow): break
		# self.wndMoney.SetText(localeInfo.NumberToMoneyString(iGoldNow))		
		
		
		# ## OLD MONEY DIALOG
		money = player.GetElk()
		self.wndMoney.SetText(localeInfo.NumberToMoneyString(money))
		
		
		
		
		self.wndAps.SetText(str(constInfo.aps) + " AP's")
		
		# if player.GetStatus(player.LEVEL) >= 35:
			# self.wndDps.SetText(str(constInfo.dps) + " DP's")
		# else:
			# self.wndDps.SetText("Ab lv.35 verfugbar!")
			# self.wndDps.SetFontColor(0.9, 0.4745, 0.4627)	
			
		if constInfo.avilable == 4:
			self.RefreshBagSlotWindow()
			constInfo.avilable = 0
			
	def RefreshBagSlotWindowOnAvilable(self):
		getItemVNum=player.GetItemIndex
		for i in xrange(player.INVENTORY_PAGE_SIZE):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

			itemVnum = getItemVNum(slotNumber)
			if constInfo.avilable == 1:
				if 0 != itemVnum:
					item.SelectItem(itemVnum)
					if item.IsAntiFlag(item.ANTIFLAG_GIVE):
						self.wndItem.DisableSlot(i)
			if constInfo.avilable == 2:
				if 0 != itemVnum:
					item.SelectItem(itemVnum)
					if item.IsAntiFlag(item.ANTIFLAG_SAFEBOX):
						self.wndItem.DisableSlot(i)
			if constInfo.avilable == 3:
				if 0 != itemVnum:
					item.SelectItem(itemVnum)
					if item.IsAntiFlag(item.ANTIFLAG_MYSHOP):
						self.wndItem.DisableSlot(i)
		self.wndItem.RefreshSlot()

		if self.wndBelt:
			self.wndBelt.RefreshSlot()
	def CheckAvilableExchange(self):
		constInfo.avilable = 1
		self.RefreshBagSlotWindowOnAvilable()
		self.RefreshBagSlotWindow()

	def CheckAvilableSafebox(self):
		constInfo.avilable = 2
		self.RefreshBagSlotWindowOnAvilable()

	def CheckAvilableShop(self):
		constInfo.avilable = 3
		self.RefreshBagSlotWindowOnAvilable()
		
	def DisturbCheckAvilable(self):
		constInfo.avilable = 0
		self.RefreshBagSlotWindow()
		
	def OnUpdate(self): ##Inventar AP Anzeige
		if self.wndAps == None:
			return
		self.wndAps.SetText(constInfo.NumberToPointString(constInfo.aps) + " AP's")
		
		# if self.wndDps == None:
			# return
			
		# if player.GetStatus(player.LEVEL) >= 35:
			# self.wndDps.SetText(constInfo.NumberToPointString(constInfo.dps) + " DP's")
			# self.wndDps.SetFontColor(0.7607, 0.7607, 0.7607)	
		# else:
			# self.wndDps.SetText(localeInfo.DAILY_LEVEL_LOW)
			# self.wndDps.SetFontColor(0.9, 0.4745, 0.4627)	
			
		if self.wndMoneySlot.IsIn():
			self.mouseReflector.Show()
			self.currencyToolTip.Open(0)
		else:
			self.mouseReflector.Hide()
			self.currencyToolTip.Close(0)
			
		if self.wndAchievementSlot.IsIn():
			self.currencyToolTip.Open(1)
		else:
			self.currencyToolTip.Close(1)

		if self.wndDungeonSlot.IsIn():
			self.currencyToolTip.Open(2)
		else:
			self.currencyToolTip.Close(2)			
			
		if self.wndSortButton.IsIn():
			self.mouseReflector1.Show()
		else:
			self.mouseReflector1.Hide()			
			
		#self.wndDps.SetText(str(constInfo.dps) + " DP's")

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SellItem(self):
		if self.sellingSlotitemIndex == player.GetItemIndex(self.sellingSlotNumber):
			if self.sellingSlotitemCount == player.GetItemCount(self.sellingSlotNumber):
				## 용혼석도 팔리게 하는 기능 추가하면서 인자 type 추가
				GFHhg54GHGhh45GHGH.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count, player.INVENTORY)
				snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnDetachMetinFromItem(self):
		if None == self.questionDialog:
			return
			
		#GFHhg54GHGhh45GHGH.SendItemUseToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)		
		self.__SendUseItemToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				itemCount = player.GetItemCount(attachedSlotPos)
				attachedCount = mouseModule.mouseController.GetAttachedItemCount()
				self.__SendMoveItemPacket(attachedSlotPos, selectedSlotPos, attachedCount)

				if item.IsRefineScroll(attachedItemIndex):
					self.wndItem.SetUseMode(False)

			elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
				mouseModule.mouseController.RunCallBack("INVENTORY")

			elif player.SLOT_TYPE_SHOP == attachedSlotType:
				GFHhg54GHGhh45GHGH.SendShopBuyPacket(attachedSlotPos)

			elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:

				if player.ITEM_MONEY == attachedItemIndex:
					GFHhg54GHGhh45GHGH.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					GFHhg54GHGhh45GHGH.SendSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)
					
#			elif player.SLOT_TYPE_GUILD_SAFEBOX == attachedSlotType:
#				if player.ITEM_MONEY == attachedItemIndex:
#					GFHhg54GHGhh45GHGH.SendGuildSafeboxTakeGoldPacket(mouseModule.mouseController.GetAttachedItemCount())
#					snd.PlaySound("sound/ui/money.wav")
#
#				else:
#					GFHhg54GHGhh45GHGH.SendGuildSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)

			elif player.SLOT_TYPE_MALL == attachedSlotType:
				GFHhg54GHGhh45GHGH.SendMallCheckoutPacket(attachedSlotPos, selectedSlotPos)

			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, itemSlotIndex):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return
		
		if itemSlotIndex in settinginfo.switchbot_Slots:
			chat.AppendChat(1, "[Switchbot] Dieser Gegenstand wird zurzeit vom Switchbot verwendet!")
			return	
		
		itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(itemSlotIndex)

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.__DropSrcItemToDestItemInInventory(attachedItemVID, attachedSlotPos, itemSlotIndex)

			mouseModule.mouseController.DeattachObject()

		else:

			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				self.__SellItem(itemSlotIndex)
				
			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)
				
			elif app.IsPressed(app.DIK_LALT):
				link = player.GetItemLink(itemSlotIndex)
				chat.AppendChat(chat.CHAT_TYPE_INFO, link)
				ime.PasteString(link)

			elif app.IsPressed(app.DIK_LSHIFT):
				itemCount = player.GetItemCount(itemSlotIndex)
				
				if itemCount > 1:
					self.dlgPickMoney.SetTitleName(localeInfo.PICK_ITEM_TITLE)
					self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickItem))
					self.dlgPickMoney.Open(itemCount)
					self.dlgPickMoney.itemGlobalSlotIndex = itemSlotIndex
				#else:
					#selectedItemVNum = player.GetItemIndex(itemSlotIndex)
					#mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum)

			elif app.IsPressed(app.DIK_LCONTROL):
				itemIndex = player.GetItemIndex(itemSlotIndex)
				item.SelectItem(itemIndex)
				if item.GetItemType() == 28:
					self.costumeAttributeChange.Clear()
					self.costumeAttributeChange.LoadItem(itemSlotIndex)
					# self.costumeAttributeChange.Open()
					return 
					
				if True == item.CanAddToQuickSlotItem(itemIndex):
					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_INVENTORY, itemSlotIndex)
				else:
					if itemIndex in settinginfo.PREVIEW_CHEST_LIST:						
						GFHhg54GHGhh45GHGH.SendChatPacket("/user_open_all_giftbox " + str(itemSlotIndex))
					else:
						chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.QUICKSLOT_REGISTER_DISABLE_ITEM)
						
			elif app.IsPressed(app.DIK_RCONTROL):
				self.devItemToolTip.Close()
				self.devItemToolTip.Clear()
			
				self.devItemToolTip.Open(itemSlotIndex)

			else:
				selectedItemVNum = player.GetItemIndex(itemSlotIndex)
				itemCount = player.GetItemCount(itemSlotIndex)
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
				
				if self.__IsUsableItemToItem(selectedItemVNum, itemSlotIndex):				
					self.wndItem.SetUseMode(True)
				else:					
					self.wndItem.SetUseMode(False)

				snd.PlaySound("sound/ui/pick.wav")
	
	
	def UseMountSkin(self):
		self.__SendUseItemToItemPacket(self.questionDialog.src, self.questionDialog.dst)
		self.OnCloseQuestionDialog()		
	
	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos):
		if srcItemSlotPos == dstItemSlotPos:
			return
			
		elif srcItemVID == player.GetItemIndex(dstItemSlotPos):
			self.__SendMoveItemPacket(srcItemSlotPos, dstItemSlotPos, 0)
			return
		if srcItemVID == 91001 and player.GetItemIndex(dstItemSlotPos) == 91002:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)	
			return
		if srcItemVID == 91201 and player.GetItemIndex(dstItemSlotPos) == 91200:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)	

		if srcItemVID == 55102 and player.GetItemIndex(dstItemSlotPos) == 55001:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)	
			
		if srcItemVID == 55102 and player.GetItemIndex(dstItemSlotPos) == 55002:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)	
			
		if srcItemVID == 91202 and player.GetItemIndex(dstItemSlotPos) == 91200:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)		
		if srcItemVID == 91203 and player.GetItemIndex(dstItemSlotPos) == 91200:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)		
		if srcItemVID == 91204 and player.GetItemIndex(dstItemSlotPos) == 91200:
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText("Mochtest du das Aussehen deines Reittieres wirklich andern?")
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.UseMountSkin))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.src = srcItemSlotPos
			self.questionDialog.dst = dstItemSlotPos
			return
			
		if srcItemVID == 39063:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)		
				
		elif item.IsRefineScroll(srcItemVID):
			self.RefineItem(srcItemSlotPos, dstItemSlotPos)
			self.wndItem.SetUseMode(False)

		elif item.IsMetin(srcItemVID):
			self.AttachMetinToItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsDetachScroll(srcItemVID):
			self.DetachMetinFromItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsKey(srcItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)			

		elif (player.GetItemFlags(srcItemSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif item.GetUseType(srcItemVID) in self.USE_TYPE_TUPLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)			

		else:
			#snd.PlaySound("sound/ui/drop.wav")

			## 이동시킨 곳이 장착 슬롯일 경우 아이템을 사용해서 장착 시킨다 - [levites]
			if player.IsEquipmentSlot(dstItemSlotPos):

				## 들고 있는 아이템이 장비일때만
				if item.IsEquipmentVID(srcItemVID):
					self.__UseItem(srcItemSlotPos)

			else:
				self.__SendMoveItemPacket(srcItemSlotPos, dstItemSlotPos, 0)
				#GFHhg54GHGhh45GHGH.SendItemMovePacket(srcItemSlotPos, dstItemSlotPos, 0)

	def __SellItem(self, itemSlotPos):
		if not player.IsEquipmentSlot(itemSlotPos):
			self.sellingSlotNumber = itemSlotPos
			itemIndex = player.GetItemIndex(itemSlotPos)
			itemCount = player.GetItemCount(itemSlotPos)
			
			
			self.sellingSlotitemIndex = itemIndex
			self.sellingSlotitemCount = itemCount

			item.SelectItem(itemIndex)
			## 안티 플레그 검사 빠져서 추가
			## 20140220
			if item.IsAntiFlag(item.ANTIFLAG_SELL):
				popup = uiCommon.PopupDialog()
				popup.SetText(localeInfo.SHOP_CANNOT_SELL_ITEM)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return

			itemPrice = item.GetISellItemPrice()

			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 5
			else:
				itemPrice = itemPrice * itemCount / 5

			item.GetItemName(itemIndex)
			itemName = item.GetItemName()

			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, itemCount, itemPrice))
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellItem))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.count = itemCount
		
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def __OnClosePopupDialog(self):
		self.pop = None

	def RefineItem(self, scrollSlotPos, targetSlotPos):

		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			return
		if app.ENABLE_REFINE_RENEWAL:
			constInfo.AUTO_REFINE_TYPE = 1
			constInfo.AUTO_REFINE_DATA["ITEM"][0] = scrollSlotPos
			constInfo.AUTO_REFINE_DATA["ITEM"][1] = targetSlotPos

		###########################################################
		self.__SendUseItemToItemPacket(scrollSlotPos, targetSlotPos)
		#GFHhg54GHGhh45GHGH.SendItemUseToItemPacket(scrollSlotPos, targetSlotPos)
		return
		###########################################################

		###########################################################
		#GFHhg54GHGhh45GHGH.SendRequestRefineInfoPacket(targetSlotPos)
		#return
		###########################################################

		result = player.CanRefine(scrollIndex, targetSlotPos)

		if player.REFINE_ALREADY_MAX_SOCKET_COUNT == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_MORE_SOCKET)

		elif player.REFINE_NEED_MORE_GOOD_SCROLL == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NEED_BETTER_SCROLL)

		elif player.REFINE_CANT_MAKE_SOCKET_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_SOCKET_DISABLE_ITEM)

		elif player.REFINE_NOT_NEXT_GRADE_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_UPGRADE_DISABLE_ITEM)

		elif player.REFINE_CANT_REFINE_METIN_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.REFINE_OK != result:
			return

		self.refineDialog.Open(scrollSlotPos, targetSlotPos)

	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if not player.CanDetach(scrollIndex, targetSlotPos):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
			return

		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REFINE_DO_YOU_SEPARATE_METIN)
		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()
		self.questionDialog.sourcePos = scrollSlotPos
		self.questionDialog.targetPos = targetSlotPos

	def AttachMetinToItem(self, metinSlotPos, targetSlotPos):
		metinIndex = player.GetItemIndex(metinSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)
		if targetIndex >= 45182 and targetIndex <= 45187:
			return

		item.SelectItem(metinIndex)
		itemName = item.GetItemName()

		result = player.CanAttachMetin(metinIndex, targetSlotPos)

		if player.ATTACH_METIN_NOT_MATCHABLE_ITEM == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_CAN_NOT_ATTACH(itemName))

		if player.ATTACH_METIN_NO_MATCHABLE_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_SOCKET(itemName))

		elif player.ATTACH_METIN_NOT_EXIST_GOLD_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_GOLD_SOCKET(itemName))

		elif player.ATTACH_METIN_CANT_ATTACH_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.ATTACH_METIN_OK != result:
			return

		self.attachMetinDialog.Open(metinSlotPos, targetSlotPos)


		
	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OverInItem(self, overSlotPos):
		overSlotPosGlobal = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
		self.wndItem.SetUsableItem(False)
		
		if overSlotPosGlobal in self.liHighlightedItems:
			self.liHighlightedItems.remove(overSlotPosGlobal)
			self.wndItem.DeactivateSlot(overSlotPos)
		
		if mouseModule.mouseController.isAttached():
			attachedItemType = mouseModule.mouseController.GetAttachedType()
			if player.SLOT_TYPE_INVENTORY == attachedItemType:
				
				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()
				
				if self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, overSlotPosGlobal):
					self.wndItem.SetUsableItem(True)
					self.ShowToolTip(overSlotPosGlobal)
					return
		
		self.ShowToolTip(overSlotPosGlobal)

	
	def __IsUsableItemToItem(self, srcItemVNum, srcSlotPos):
		"다른 아이템에 사용할 수 있는 아이템인가?"
		if srcItemVNum == 55102:
			return True				
		if srcItemVNum == 91201:
			return True	
		if srcItemVNum == 39063:
			return True	
		if srcItemVNum == 91202:
			return True	
		if srcItemVNum == 91203:
			return True	
		if srcItemVNum == 91204:
			return True	
		if srcItemVNum == 91001:
			return True				
		if item.IsRefineScroll(srcItemVNum):
			return True
		elif item.IsMetin(srcItemVNum):
			return True
		elif item.IsDetachScroll(srcItemVNum):
			return True
		elif item.IsKey(srcItemVNum):
			return True
		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True
		else:
			if item.GetUseType(srcItemVNum) in self.USE_TYPE_TUPLE:
				return True
			
		return False

	def __CanUseSrcItemToDstItem(self, srcItemVNum, srcSlotPos, dstSlotPos):
		"대상 아이템에 사용할 수 있는가?"

		if srcSlotPos == dstSlotPos:
			return False
		if srcItemVNum >= 55102 and player.GetItemIndex(dstSlotPos) == 55001:			
			return True	
		if srcItemVNum >= 55102 and player.GetItemIndex(dstSlotPos) == 55002:			
			return True	
		if srcItemVNum >= 91001 and player.GetItemIndex(dstSlotPos) == 91002:			
			return True			
		if srcItemVNum >= 91201 and player.GetItemIndex(dstSlotPos) == 91200:			
			return True		
		if srcItemVNum >= 91202 and player.GetItemIndex(dstSlotPos) == 91200:			
			return True		
		if srcItemVNum >= 91203 and player.GetItemIndex(dstSlotPos) == 91200:			
			return True		
		if srcItemVNum >= 91204 and player.GetItemIndex(dstSlotPos) == 91200:			
			return True
			
		if srcItemVNum == 39063:
			self.__SendUseItemToItemPacket(srcSlotPos, dstSlotPos)	
				
		if srcItemVNum == player.GetItemIndex(dstSlotPos):
			if player.GetItemCount(dstSlotPos) < 200:
				return True			
		elif item.IsRefineScroll(srcItemVNum):
			if player.REFINE_OK == player.CanRefine(srcItemVNum, dstSlotPos):
				return True
		elif item.IsMetin(srcItemVNum):
			if player.ATTACH_METIN_OK == player.CanAttachMetin(srcItemVNum, dstSlotPos):
				return True
		elif item.IsDetachScroll(srcItemVNum):
			if player.DETACH_METIN_OK == player.CanDetach(srcItemVNum, dstSlotPos):
				return True
		elif item.IsKey(srcItemVNum):
			if player.CanUnlock(srcItemVNum, dstSlotPos):
				return True

		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return True

		else:
			useType=item.GetUseType(srcItemVNum)

			if "USE_CLEAN_SOCKET" == useType:
				if self.__CanCleanBrokenMetinStone(dstSlotPos):
					return True
			elif "USE_CHANGE_ATTRIBUTE" == useType:
				if self.__CanChangeItemAttrList(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ATTRIBUTE2" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return True
			elif "USE_ADD_ACCESSORY_SOCKET" == useType:
				if self.__CanAddAccessorySocket(dstSlotPos):
					return True
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == useType:								
				if self.__CanPutAccessorySocket(dstSlotPos, srcItemVNum):
					return TRUE;
			elif "USE_PUT_INTO_BELT_SOCKET" == useType:								
				dstItemVNum = player.GetItemIndex(dstSlotPos)
				print "USE_PUT_INTO_BELT_SOCKET", srcItemVNum, dstItemVNum

				item.SelectItem(dstItemVNum)
		
				if item.ITEM_TYPE_BELT == item.GetItemType():
					return True

		return False

	def __CanCleanBrokenMetinStone(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)
		
		if item.ITEM_TYPE_WEAPON != item.GetItemType():
			return False

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemMetinSocket(dstSlotPos, i) == constInfo.ERROR_METIN_STONE:
				return True

		return False

	def __CanChangeItemAttrList(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):	 
			return False

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i) != 0:
				return True

		return False

	def __CanPutAccessorySocket(self, dstSlotPos, mtrlVnum):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return False

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return False

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)

		if mtrlVnum != constInfo.GET_ACCESSORY_MATERIAL_VNUM(dstItemVNum, item.GetItemSubType()):
			return False
		
		if curCount>=maxCount:
			return False

		return True

	def __CanAddAccessorySocket(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return False

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return False

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)
		
		ACCESSORY_SOCKET_MAX_SIZE = 3
		if maxCount >= ACCESSORY_SOCKET_MAX_SIZE:
			return False

		return True

	def __CanAddItemAttr(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return False

		item.SelectItem(dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):	 
			return False
			
		attrCount = 0
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i) != 0:
				attrCount += 1

		if attrCount<4:
			return True
								
		return False

	def ShowToolTip(self, slotIndex):
		if None != self.tooltipItem:
			self.tooltipItem.SetInventoryItem(slotIndex)

	def OnTop(self):
		if None != self.tooltipItem:
			self.tooltipItem.SetTop()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def UseItemSlot(self, slotIndex):
		curCursorNum = app.GetCursor()
		if app.SELL == curCursorNum:
			return

		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return
			
		if slotIndex in settinginfo.switchbot_Slots:
			chat.AppendChat(1, "[Switchbot] Dieser Gegenstand wird zurzeit vom Switchbot verwendet!")
			return	
			
		slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)

		
		
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			if self.wndDragonSoulRefine.IsShow():
				self.wndDragonSoulRefine.AutoSetItem((player.INVENTORY, slotIndex), 1)
				return

		self.__UseItem(slotIndex)
		mouseModule.mouseController.DeattachObject()
		self.OverOutItem()

	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(slotIndex)
		item.SelectItem(ItemVNum)
		if item.IsFlag(item.ITEM_FLAG_CONFIRM_WHEN_USE):
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.INVENTORY_REALLY_USE_ITEM)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
			self.questionDialog.Open()
			self.questionDialog.slotIndex = slotIndex
		
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

		else:
			self.__SendUseItemPacket(slotIndex)
			#GFHhg54GHGhh45GHGH.SendItemUsePacket(slotIndex)	

	def __UseItemQuestionDialog_OnCancel(self):
		self.OnCloseQuestionDialog()

	def __UseItemQuestionDialog_OnAccept(self):
		self.__SendUseItemPacket(self.questionDialog.slotIndex)
		self.OnCloseQuestionDialog()		

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos):
		# 개인상점 열고 있는 동안 아이템 사용 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return
		if constInfo.BlockItemsSystem["Block"] == 1:
			chat.AppendChat(1, "Sicherheitssystem ist Aktiviert.")
			return

		GFHhg54GHGhh45GHGH.SendItemUseToItemPacket(srcSlotPos, dstSlotPos)

	def __SendUseItemPacket(self, slotPos):
		# 개인상점 열고 있는 동안 아이템 사용 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return
		if constInfo.BlockItemsSystem["Block"] == 1:
			chat.AppendChat(1, "Sicherheitssystem ist Aktiviert.")
			return

		GFHhg54GHGhh45GHGH.SendItemUsePacket(slotPos)
	
	def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
		# 개인상점 열고 있는 동안 아이템 사용 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return
		if constInfo.BlockItemsSystem["Block"] == 1:
			chat.AppendChat(1, "Sicherheitssystem ist Aktiviert.")
			return
			
		# if srcSlotPos in settinginfo.switchbot_Slots:
			# chat.AppendChat(1, "[Switchbot] Dieser Gegenstand wird zurzeit vom Switchbot verwendet!")
			# return		
		
		# if dstSlotPos in settinginfo.switchbot_Slots:
			# chat.AppendChat(1, "[Switchbot] Die Zielposition wird zurzeit vom Switchbot verwendet!")
			# return	
		

		GFHhg54GHGhh45GHGH.SendItemMovePacket(srcSlotPos, dstSlotPos, srcItemCount)
	
	def SetDragonSoulRefineWindow(self, wndDragonSoulRefine):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoulRefine = wndDragonSoulRefine
			
	def OnMoveWindow(self, x, y):
#		print "Inventory Global Pos : ", self.GetGlobalPosition()
		if self.wndBelt:
#			print "Belt Global Pos : ", self.wndBelt.GetGlobalPosition()
			self.wndBelt.AdjustPositionAndSize()
			
		if self.dlgCreateGoldSafe:
			self.dlgCreateGoldSafe.AdjustPosition()
			
		# if self.sideBar:
			# self.sideBar.AdjustPosition()
			
		if self.wndCostume:
			self.wndCostume.AdjustPosition()
			
		if self.costumeAttributeChange:
			self.costumeAttributeChange.AdjustPosition()
			
	def HighlightSlot(self, slot):
		if not slot in self.liHighlightedItems:
			self.liHighlightedItems.append(slot)
	
	def __RefreshHighlights(self):
		for i in xrange(player.INVENTORY_PAGE_SIZE):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
			if slotNumber in self.liHighlightedItems:
				self.wndItem.ActivateSlot(i)
