import ui
import chat
import app
import fgGHGjjFHJghjfFG1545gGG as player
import snd
import item
import GFHhg54GHGhh45GHGH as net
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import uiCommon
import localeInfo
import systemSetting
import shopinfo

# Global Variables
ITEM_STACK_COUNT		= 500 		# Max. Item Stack
USE_SHOP_LIMIT_RANGE	= 1000		# Reichweite ab wann der Shop automatisch geschlossen wird.

class MultiShopWindow(ui.ScriptWindow):

	CURRENCY_TYPE_GOLD = 0
	CURRENCY_TYPE_ACHIEVEMENT = 1
	CURRENCY_TYPE_DUNGEON = 2
	CURRENCY_TYPE_ITEMSHOP = 3
	CURRENCY_TYPE_ITEM = 4
	
	# SHOP_STRING_DICT = shopinfo.shopStringTable
	
	CURRENCY_NAME_DICT = {
		CURRENCY_TYPE_GOLD			: localeInfo.MULTISHOP_CURRENCY_GOLD,
		CURRENCY_TYPE_ACHIEVEMENT	: localeInfo.MULTISHOP_CURRENCY_ACHIEVEMENT,
		CURRENCY_TYPE_DUNGEON		: localeInfo.MULTISHOP_CURRENCY_DUNGEON,
		CURRENCY_TYPE_ITEMSHOP		: localeInfo.MULTISHOP_CURRENCY_COINS,
	}

	SHOP_CATEGORY_MAX_COUNT = 14
	SHOP_SLOT_COUNT = 40

	def __init__(self, wndInventory):
		ui.ScriptWindow.__init__(self)
		self.shopContent = []
		self.slotLink = {}
		self.inventoryWindow = wndInventory
		self.buyItemDialog = None
		self.qid = 0
		self.shopIndex = 0
		self.xShopStart = 0
		self.yShopStart = 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/multishop.py")
		except:
			import exception
			exception.Abort("MultiShopWindow.LoadWindow.LoadObject")
			
		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()	
	
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		self.shopTitleTextLine = self.GetChild("shopTitleTextLine")
		self.shopCategoryTextLine = self.GetChild("shopCategoryTextLine")
		self.navigationListBox = self.GetChild("navigationListBox")
		self.navigationListBox.SetEvent(ui.__mem_func__(self.OnSelectCategory))
		self.navigationScrollBar = self.GetChild("QuestListScrollBar")
		self.navigationScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.itemSlot = self.GetChild("itemSlot")
		self.itemSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.BuyItem))  
		self.itemSlot.SAFE_SetButtonEvent("RIGHT", "ALWAYS", self.BuyItem)
		self.navigationScrollBar.Hide()		

	def BuyItem(self,slot):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"CLICK ITEM! slot: " + str(slot))
		
		index = self.slotLink[slot]
		itemInfo = self.shopContent[self.category]["category_content"][index]		
		item.SelectItem(itemInfo["item_vnum"])
		if app.IsPressed(app.DIK_LSHIFT):
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SHIFT PRESSED! BUY MORE!")
			
			self.buyItemDialog = BuyMultipleItemDialog()
			self.buyItemDialog.SetAcceptEvent(lambda arg=True: self.RequestBuyItem(arg))
			self.buyItemDialog.SetCancelEvent(lambda arg=False: self.RequestBuyItem(arg))			
			self.buyItemDialog.slot = slot
			self.buyItemDialog.count = 1
			self.buyItemDialog.price = itemInfo["currency_count"]
			self.buyItemDialog.SetInfo(item.GetItemName(), self.GetCurrencyName(itemInfo["currency_type"],itemInfo["currency_vnum"]), itemInfo["currency_count"])
			self.buyItemDialog.itemShopIndex = itemInfo["item_shop_index"]
			self.buyItemDialog.Open()			
		
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SHIFT NOT PRESSED! BUY ONE!")
			self.buyItemDialog = BuySingleItemDialog()
			self.buyItemDialog.SetAcceptEvent(lambda arg=True: self.RequestBuyItem(arg))
			self.buyItemDialog.SetCancelEvent(lambda arg=False: self.RequestBuyItem(arg))			
			self.buyItemDialog.slot = slot
			self.buyItemDialog.count = 1
			self.buyItemDialog.SetInfo(item.GetItemName(), self.GetCurrencyName(itemInfo["currency_type"],itemInfo["currency_vnum"]), itemInfo["currency_count"])
			self.buyItemDialog.itemShopIndex = itemInfo["item_shop_index"]
			self.buyItemDialog.Open()

	def GetCurrencyName(self,type,vnum):
		if type == self.CURRENCY_TYPE_ITEM:
			item.SelectItem(vnum)
			return item.GetItemName()
		else:
			try:
				return self.CURRENCY_NAME_DICT[type]
			except:
				return "NO_CURRENCY_NAME_FOUND"

	def RequestBuyItem(self,answer):
		if not self.buyItemDialog:
			return

		if answer:
			slotPos = self.buyItemDialog.slot
			itemCount = self.buyItemDialog.count
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"slot: " + str(slotPos))
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"count: " + str(itemCount))

			constInfo.INPUT_CMD = "BUY#" + str(self.shopIndex) + "#" + str(self.category) + "#" + str(self.buyItemDialog.itemShopIndex) + "#" + str(itemCount)
			event.QuestButtonClick(self.qid)				
			

		self.buyItemDialog.Close()
		self.buyItemDialog = None
		return
		
	def GetShopStringByNumber(self,number):
		try:
			return shopinfo.shopStringTable[number]
		
		except:
			return "NoName (" + str(number) + ")"
			
	def ShowToolTip(self,slot):
		index = self.slotLink[slot]
		itemInfo = self.shopContent[self.category]["category_content"][index]
		item.SelectItem(itemInfo["item_vnum"])
		self.itemtooltip.ClearToolTip()
		self.itemtooltip.AddItemData(itemInfo["item_vnum"], [0, 0, 0, 0, 0, 0])
		time = 0
		if item.GetItemType() == 16:
			if item.GetValue(0) > 0:
				time = item.GetValue(0)
				
		if item.GetItemType() == 28:
			(limittype,limitvalue) = item.GetLimit(0)
			time = int(limitvalue/60)

		if item.GetItemType() == 18:
			(limittype,limitvalue) = item.GetLimit(0)
			if limittype == 7 and limitvalue > 0:
				time = int(limitvalue/60)
			
		if time > 0:
			time = int(time/60)
			time_str = localeInfo.HOUR
			if time >= 48:
				time = int(time/24)
				time_str = localeInfo.DAY
			
			self.itemtooltip.AppendSpace(5)
			self.itemtooltip.AppendTextLine(localeInfo.MULTISHOP_RUNTIME, self.itemtooltip.SPECIAL_TITLE_COLOR)	
			self.itemtooltip.AppendTextLine(str(time) + " " + str(time_str), self.itemtooltip.NORMAL_COLOR)		
		
		self.itemtooltip.AppendSpace(5)
		self.itemtooltip.AppendTextLine(localeInfo.MULTISHOP_BUY, self.itemtooltip.SPECIAL_TITLE_COLOR)	
		
		if itemInfo["currency_type"] == self.CURRENCY_TYPE_GOLD:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_GOLD, self.itemtooltip.NORMAL_COLOR)
			self.itemtooltip.AppendSpace(5)
			self.itemtooltip.AppendHorizontalLine()
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_ACHIEVEMENT:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_ACHIEVEMENT, self.itemtooltip.NORMAL_COLOR)	
			self.itemtooltip.AppendSpace(5)
			self.itemtooltip.AppendHorizontalLine()	
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_DUNGEON:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_DUNGEON, self.itemtooltip.NORMAL_COLOR)	
			self.itemtooltip.AppendSpace(5)
			self.itemtooltip.AppendHorizontalLine()
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_ITEMSHOP:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_COINS, self.itemtooltip.NORMAL_COLOR)
			self.itemtooltip.AppendSpace(5)
			self.itemtooltip.AppendHorizontalLine()	
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_ITEM:
			item.SelectItem(itemInfo["currency_vnum"])
			self.itemtooltip.AppendSpace(10)
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + "x |Eemoji/" + str(itemInfo["currency_vnum"]) + "|e " + item.GetItemName())
			self.itemtooltip.AppendSpace(10)
			self.itemtooltip.AppendHorizontalLine()
		self.itemtooltip.AppendSpace(5)
		self.itemtooltip.AppendTextLine(localeInfo.TOOLTIP_MULTISHOP_SHORTCUT_BUY_MORE, self.itemtooltip.NORMAL_COLOR)
		self.itemtooltip.ShowToolTip()		
	
		
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()
	
	##########################################################
	## InterfaceModule.py INPUT
	
	def SetShopName(self,name):
		self.shopTitleTextLine.SetText(self.GetShopStringByNumber(name))
		
		
	def SetShopIndex(self,index):
		self.shopIndex = int(index)

	
	def AppendShopCategory(self,name):
		shopCategory = {
			"category_name" : name,
			"category_content" : [],
		}
		
		self.shopContent.append(shopCategory)


	def AppendShopItem(self,category,index,item_position,itemVnum,itemCount,currencyType,currencyVnum,currencyCount):
		itemInfo = {
			"item_shop_index" : int(index),
			"item_position" : int(item_position),
			"item_vnum" : int(itemVnum),
			"item_count" : int(itemCount),
			"currency_type" : int(currencyType),
			"currency_vnum" : int(currencyVnum),
			"currency_count" : int(currencyCount),
		}
		
		category = category - 1
		try:
			self.shopContent[category]["category_content"].append(itemInfo)
			
		except:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop][Error 1] Item " + str(itemVnum) + " could not be attached to index " + str(index))
	
	def SetQuestIndex(self,qid):
		self.qid = int(qid)

	def ClearMultiShop(self):
		self.navigationListBox.ClearItem()
		self.navigationScrollBar.Hide()
		for i in xrange(self.SHOP_SLOT_COUNT):
			self.itemSlot.SetItemSlot(i,0,0)
		
		self.shopContent = []
		self.category = 0
			
	def OpenMultiShop(self):
		self.BuildMultiShop()
		self.AdjustPosition()
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
		self.Show()
	
	##########################################################
		
	def BuildMultiShop(self):
		if len(self.shopContent) == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop][Error 2] No Data found in self.shopContent")
			return
			
		for i in xrange(len(self.shopContent)):
			self.navigationListBox.InsertItem(i,self.GetShopStringByNumber(self.shopContent[i]["category_name"]))
			
		if len(self.shopContent) > self.SHOP_CATEGORY_MAX_COUNT:
			self.navigationScrollBar.Show()
		
		
		self.navigationListBox.SelectItem(0)
		self.category = 0
		# self.BuildCategory()
		
		
	def BuildCategory(self):
		self.shopCategoryTextLine.SetText(self.GetShopStringByNumber(self.shopContent[self.category]["category_name"]))
		
		itemInfo = self.shopContent[self.category]["category_content"]
		if len(itemInfo) == 0:
			return
		
		self.slotLink = {}
		
		
		for i in xrange(len(itemInfo)):
			slot = itemInfo[i]["item_position"]
			self.itemSlot.SetItemSlot(slot,itemInfo[i]["item_vnum"],itemInfo[i]["item_count"])
			self.slotLink[slot] = i
			
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(self.slotLink))
			
	def OnSelectCategory(self):
		for i in xrange(self.SHOP_SLOT_COUNT):
			self.itemSlot.SetItemSlot(i,0,0)

		self.category = self.navigationListBox.GetSelectedItem()
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OnSelectCategory: " + str(self.navigationListBox.GetSelectedItem()))
		self.BuildCategory()
		
	def OnScroll(self):
		viewItemCount = self.navigationListBox.GetViewItemCount()
		itemCount = self.navigationListBox.GetItemCount()
		pos = self.navigationScrollBar.GetPos() * (itemCount - viewItemCount)
		self.navigationListBox.SetBasePos(int(pos))	

	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.navigationScrollBar.OnUp()
		else:
			self.navigationScrollBar.OnDown()		
		
	# def BindInventory(self,inventoryWindow):
		# self.inventoryWindow = inventoryWindow
		
	def GetBasePosition(self):
		x, y = self.inventoryWindow.GetGlobalPosition()
		return x - 360, y
		
	def AdjustPosition(self):
		bx, by = self.GetBasePosition()
		self.SetPosition(bx, by)
		
	def OnUpdate(self):
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xShopStart) > USE_SHOP_LIMIT_RANGE or abs(y - self.yShopStart) > USE_SHOP_LIMIT_RANGE:
			self.Close()
			
		if self.IsShow():
			if systemSetting.IsMultiShopLock() == 1:
				self.AdjustPosition()
			
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()

	def Close(self):
		# self.buySingleItemDialog.Close()
		self.Hide()
		

class MultiShopEditorWindow(ui.ScriptWindow):

	CURRENCY_TYPE_GOLD = 0
	CURRENCY_TYPE_ACHIEVEMENT = 1
	CURRENCY_TYPE_DUNGEON = 2
	CURRENCY_TYPE_ITEMSHOP = 3
	CURRENCY_TYPE_ITEM = 4
	
	# SHOP_STRING_DICT = shopinfo.shopStringTable
	
	CURRENCY_NAME_DICT = {
		CURRENCY_TYPE_GOLD			: localeInfo.MULTISHOP_CURRENCY_GOLD,
		CURRENCY_TYPE_ACHIEVEMENT	: localeInfo.MULTISHOP_CURRENCY_ACHIEVEMENT,
		CURRENCY_TYPE_DUNGEON		: localeInfo.MULTISHOP_CURRENCY_DUNGEON,
		CURRENCY_TYPE_ITEMSHOP		: localeInfo.MULTISHOP_CURRENCY_COINS,
	}

	SHOP_CATEGORY_MAX_COUNT = 14
	SHOP_SLOT_COUNT = 40

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.shopContent = []
		self.slotLink = {}
		self.buyItemDialog = None
		self.qid = 0
		self.shopIndex = 0
		self.xShopStart = 0
		self.yShopStart = 0
		self.category = 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/multishop_editor.py")
		except:
			import exception
			exception.Abort("MultiShopWindow.LoadWindow.LoadObject")
			
		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()	
	
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		self.shopTitleTextLine = self.GetChild("shopTitleTextLine")
		self.shopCategoryTextLine = self.GetChild("shopCategoryTextLine")
		self.navigationListBox = self.GetChild("navigationListBox")
		self.navigationListBox.SetEvent(ui.__mem_func__(self.OnSelectCategory))
		self.navigationScrollBar = self.GetChild("QuestListScrollBar")
		self.navigationScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.itemSlot = self.GetChild("itemSlot")
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip)) #

		self.itemSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		self.itemSlot.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))						
		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))

		self.navigationScrollBar.Hide()		
		
		self.OpenCategoryNameBoardButton = self.GetChild("makeNewCategory")
		self.CategoryNameBoard = self.GetChild("newCategoryNameBoard")
		self.addCategoryButton = self.GetChild("addCategoryButton")
		self.closeCategoryNameButton = self.GetChild("closeCategoryNameBoard")
		self.categoryNameEditLine = self.GetChild("newCategoryBackgroundInputEditLine")
		
		self.CategoryNameBoard.Hide()
		self.OpenCategoryNameBoardButton.SetEvent(self.OpenCategoryNameBoard)
		self.addCategoryButton.SetEvent(self.InsertNewCategory)
		self.closeCategoryNameButton.SetEvent(self.CloseCategoryNameBoard)
		
		
		self.currencyListBox = self.GetChild("currencyListBox")
		
		self.currencyListBox.InsertItem(self.CURRENCY_TYPE_GOLD,"CUR_GOLD")
		self.currencyListBox.InsertItem(self.CURRENCY_TYPE_ACHIEVEMENT,"CUR_ACHIEVEMENT")
		self.currencyListBox.InsertItem(self.CURRENCY_TYPE_DUNGEON,"CUR_DUNGEON")
		self.currencyListBox.InsertItem(self.CURRENCY_TYPE_ITEMSHOP,"CUR_ITEMSHOP")
		self.currencyListBox.InsertItem(self.CURRENCY_TYPE_ITEM,"CUR_ITEM")
		self.currencyListBox.SelectItem(0)
		self.makeVItemButton = self.GetChild("attachVirtualItemButton")
		self.makeVItemButton.SetEvent(self.MakeVirtualItem)
		
		self.makeItem_ItemVnumEditLine = self.GetChild("vnumInputEditLine")
		self.makeItem_ItemCountEditLine = self.GetChild("countInputEditLine")
		
		self.makeItem_ItemCurrencyListBox = self.GetChild("currencyListBox")
		self.makeItem_ItemCurrencyVnumEditLine = self.GetChild("currencyVnumInputEditLine")
		self.makeItem_ItemCurrencyCount = self.GetChild("currencyCountInputEditLine")
	
		self.deleteItemToggleButton = self.GetChild("deleteItem")
		self.deleteItemToggleButton.SetToggleDownEvent(self.OnBeginDeleteMode)
		self.deleteItemToggleButton.SetToggleUpEvent(self.OnEndDeleteMode)	
		
		
		self.openSaveShopDialogButton = self.GetChild("saveShopDialogButton")
		self.saveShopDialog = self.GetChild("saveShopBoard")
		self.saveShopIndexEditLine = self.GetChild("saveShopIndexBackgroundInputEditLine")
		self.saveShopNameEditLine = self.GetChild("saveShopBackgroundInputEditLine")
		self.saveShopButton = self.GetChild("saveShop")
		self.closeSaveShopDialogButton = self.GetChild("closeShopSaveDialog")
		
		
		self.saveShopDialog.Hide()
		self.openSaveShopDialogButton.SetEvent(self.OpenSaveShopDialog)
		self.saveShopButton.SetEvent(self.SaveShop)
		self.closeSaveShopDialogButton.SetEvent(self.CloseSaveShopDialog)
		
		
	def OpenSaveShopDialog(self):
		self.saveShopDialog.Show()
		
	def SaveShop(self):
		string = "multishop_List[" + self.saveShopIndexEditLine.GetText() + "] = {\n"
		string = string + self.saveShopNameEditLine.GetText() + ",\n{\n"
		
		for i in xrange(len(self.shopContent)):
			categoryName = self.shopContent[i]["category_name"]
			string = string + "{\n" + categoryName + ",\n{"
			
			for b in xrange(len(self.shopContent[i]["category_content"])):
				itemInfo = self.shopContent[i]["category_content"][b]
				
				string = string + "\n{"
				string = string + str(itemInfo["item_position"]) + "," + str(itemInfo["item_vnum"]) + "," + str(itemInfo["item_count"]) + "," + str(itemInfo["currency_type"]) + "," + str(itemInfo["currency_vnum"]) + "," + str(itemInfo["currency_count"])
				string = string + "},"

			string = string + "\n}\n},\n"
			
		string = string + "}\n}\n"
		fo = open("multishop.txt", "a")
		fo.write(string + "\n\n")
		fo.close()		
		
	def CloseSaveShopDialog(self):
		self.saveShopDialog.Hide()
	
	
	def OnBeginDeleteMode(self):
		app.SetCursor(app.CANT_GO)
		
	def OnEndDeleteMode(self):
		app.SetCursor(app.NORMAL)
	
	def UseItemSlot(self,slot):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"UseItemSlot (" + str(slot) + ")")
	
	def SelectEmptySlot(self,slot):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SelectEmptySlot (" + str(slot) + ")")
		
		if mouseModule.mouseController.isAttached():
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			
			currencyType = self.makeItem_ItemCurrencyListBox.GetSelectedItem()
			currencyVnum = int(self.makeItem_ItemCurrencyVnumEditLine.GetText())
			currencyCount = int(self.makeItem_ItemCurrencyCount.GetText())
			
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"currencyCount: " + str(currencyCount))
			
			
			self.AppendShopItem(self.category,slot,attachedItemIndex,attachedItemCount,currencyType,currencyVnum,currencyCount)
			for i in xrange(self.SHOP_SLOT_COUNT):
				self.itemSlot.ClearSlot(i)
				self.itemSlot.SetUsableSlot(i)
				self.itemSlot.EnableSlot(i)
				
			self.itemSlot.RefreshSlot()
			self.BuildCategory()
			
		mouseModule.mouseController.DeattachObject()
			
	
	def SelectItemSlot(self,slot):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SelectItemSlot (" + str(slot) + ")")
		
		item = self.GetItemBySlotPosition(slot)
		if item < 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"NO ITEM FOUND!")
			return
			
		del self.shopContent[self.category]["category_content"][item]
		self.OnSelectCategory()

	def GetItemBySlotPosition(self,slot):
		info = self.shopContent[self.category]["category_content"]
		for i in xrange(len(info)):
			if info[i]["item_position"] == slot:
				return i

		return -1
		
	def CheckVItemButton(self):
		canPass = True
		
		if len(self.makeItem_ItemVnumEditLine.GetText()) <= 1:
			canPass = False
		
		if len(self.makeItem_ItemCountEditLine.GetText()) <= 0:
			canPass = False
		
		count = int(self.makeItem_ItemCountEditLine.GetText())
		if count == 0 or count > ITEM_STACK_COUNT:
			canPass = False	
		
		currency = self.makeItem_ItemCurrencyListBox.GetSelectedItem()
		if currency >= self.CURRENCY_TYPE_GOLD and currency <= self.CURRENCY_TYPE_ITEMSHOP:
			self.makeItem_ItemCurrencyVnumEditLine.SetText("0")
		
		elif currency == self.CURRENCY_TYPE_ITEM:
			if len(self.makeItem_ItemCurrencyVnumEditLine.GetText()) <= 0:
				canPass = False	
		else:
			canPass = False
			
		if len(self.makeItem_ItemCurrencyCount.GetText()) <= 0:	
			canPass = False
			
		count = int(self.makeItem_ItemCurrencyCount.GetText())
		if count == 0:
			canPass = False

		if len(self.shopContent) == 0:
			canPass = False
			
			
		return canPass
			
	def MakeVirtualItem(self):
		if self.CheckVItemButton():
			itemVnum = int(self.makeItem_ItemVnumEditLine.GetText())
			itemCount = int(self.makeItem_ItemCountEditLine.GetText())
			mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, 0, itemVnum, itemCount)
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Das ist derzeit nicht möglich.")
		
	def OpenCategoryNameBoard(self):
		self.categoryNameEditLine.SetText("")
		self.CategoryNameBoard.Show()
		
	def CloseCategoryNameBoard(self):
		self.CategoryNameBoard.Hide()
	
	def InsertNewCategory(self):
		self.CategoryNameBoard.Hide()
		self.AppendShopCategory(self.categoryNameEditLine.GetText())
		
		self.navigationListBox.ClearItem()
		
		for i in xrange(len(self.shopContent)):
			self.navigationListBox.InsertItem(i,self.GetShopStringByNumber(self.shopContent[i]["category_name"]))
			
		if len(self.shopContent) > self.SHOP_CATEGORY_MAX_COUNT:
			self.navigationScrollBar.Show()

		self.navigationListBox.SelectItem(0)
		self.category = 0
	
	def GetCurrencyName(self,type,vnum):
		if type == self.CURRENCY_TYPE_ITEM:
			item.SelectItem(vnum)
			return item.GetItemName()
		else:
			try:
				return self.CURRENCY_NAME_DICT[type]
			except:
				return "NO_CURRENCY_NAME_FOUND"
		
		
	def GetShopStringByNumber(self,number):
		try:
			return shopinfo.shopStringTable[number]
		
		except:
			return "NoName (" + str(number) + ")"
			
	def ShowToolTip(self,slot):
		index = self.slotLink[slot]
		itemInfo = self.shopContent[self.category]["category_content"][index]
		item.SelectItem(itemInfo["item_vnum"])
		self.itemtooltip.ClearToolTip()
		self.itemtooltip.AddItemData(itemInfo["item_vnum"], [0, 0, 0, 0, 0, 0])
		time = 0
		if item.GetItemType() == 16:
			if item.GetValue(0) > 0:
				time = item.GetValue(0)
				
		if item.GetItemType() == 28:
			(limittype,limitvalue) = item.GetLimit(0)
			time = int(limitvalue/60)

		if item.GetItemType() == 18:
			(limittype,limitvalue) = item.GetLimit(0)
			if limittype == 7 and limitvalue > 0:
				time = int(limitvalue/60)
			
		if time > 0:
			time = int(time/60)
			time_str = localeInfo.HOUR
			if time >= 48:
				time = int(time/24)
				time_str = localeInfo.DAY
			
			self.itemtooltip.AppendSpace(5)
			self.itemtooltip.AppendTextLine(localeInfo.MULTISHOP_RUNTIME, self.itemtooltip.SPECIAL_TITLE_COLOR)	
			self.itemtooltip.AppendTextLine(str(time) + " " + str(time_str), self.itemtooltip.NORMAL_COLOR)		
		
		self.itemtooltip.AppendSpace(5)
		self.itemtooltip.AppendTextLine(localeInfo.MULTISHOP_BUY, self.itemtooltip.SPECIAL_TITLE_COLOR)	
		
		if itemInfo["currency_type"] == self.CURRENCY_TYPE_GOLD:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_GOLD, self.itemtooltip.NORMAL_COLOR)				
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_ACHIEVEMENT:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_ACHIEVEMENT, self.itemtooltip.NORMAL_COLOR)				
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_DUNGEON:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_DUNGEON, self.itemtooltip.NORMAL_COLOR)				
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_ITEMSHOP:
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + " " + localeInfo.MULTISHOP_CURRENCY_COINS, self.itemtooltip.NORMAL_COLOR)				
		elif itemInfo["currency_type"] == self.CURRENCY_TYPE_ITEM:
			item.SelectItem(itemInfo["currency_vnum"])
			self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(itemInfo["currency_count"]) + "x " + item.GetItemName())
		
		self.itemtooltip.AppendSpace(5)
		self.itemtooltip.AppendTextLine(localeInfo.TOOLTIP_MULTISHOP_SHORTCUT_BUY_MORE, self.itemtooltip.NORMAL_COLOR)
		self.itemtooltip.ShowToolTip()		
	
		
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()

	def SetShopName(self,name):
		self.shopTitleTextLine.SetText(self.GetShopStringByNumber(name))
		
		
	def SetShopIndex(self,index):
		self.shopIndex = int(index)

	
	def AppendShopCategory(self,name):
		shopCategory = {
			"category_name" : name,
			"category_content" : [],
		}
		
		self.shopContent.append(shopCategory)


	def AppendShopItem(self,index,item_position,itemVnum,itemCount,currencyType,currencyVnum,currencyCount):
		itemInfo = {
			"item_shop_index" : int(index),
			"item_position" : int(item_position),
			"item_vnum" : int(itemVnum),
			"item_count" : int(itemCount),
			"currency_type" : int(currencyType),
			"currency_vnum" : int(currencyVnum),
			"currency_count" : int(currencyCount),
		}
		# index = index - 1 # LUA +1 FIX
		try:
			self.shopContent[index]["category_content"].append(itemInfo)
			
		except:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop][Error 1] Item " + str(itemVnum) + " could not be attached to index " + str(index))
	
	def SetQuestIndex(self,qid):
		self.qid = int(qid)

	def ClearMultiShop(self):
		self.navigationListBox.ClearItem()
		self.navigationScrollBar.Hide()
		for i in xrange(self.SHOP_SLOT_COUNT):
			self.itemSlot.SetItemSlot(i,0,0)
		
		self.shopContent = []
		self.category = 0
			
	def OpenMultiShop(self):
		self.BuildMultiShop()
		self.AdjustPosition()
		(self.xShopStart, self.yShopStart, z) = player.GetMainCharacterPosition()
		self.Show()


	def BuildMultiShop(self):
		if len(self.shopContent) == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop][Error 2] No Data found in self.shopContent")
			return
			
		for i in xrange(len(self.shopContent)):
			self.navigationListBox.InsertItem(i,self.GetShopStringByNumber(self.shopContent[i]["category_name"]))
			
		if len(self.shopContent) > self.SHOP_CATEGORY_MAX_COUNT:
			self.navigationScrollBar.Show()
		
		
		self.navigationListBox.SelectItem(0)
		self.category = 0
		# self.BuildCategory()
		
		
	def BuildCategory(self):
		self.shopCategoryTextLine.SetText(self.GetShopStringByNumber(self.shopContent[self.category]["category_name"]))
		
		itemInfo = self.shopContent[self.category]["category_content"]
		if len(itemInfo) == 0:
			return
		
		self.slotLink = {}
		
		
		for i in xrange(len(itemInfo)):
			slot = itemInfo[i]["item_position"]
			self.itemSlot.SetItemSlot(slot,itemInfo[i]["item_vnum"],itemInfo[i]["item_count"])
			self.slotLink[slot] = i
			
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(self.slotLink))
			
	def OnSelectCategory(self):
		for i in xrange(self.SHOP_SLOT_COUNT):
			self.itemSlot.ClearSlot(i)
			self.itemSlot.SetUsableSlot(i)
			self.itemSlot.EnableSlot(i)
				
		self.itemSlot.RefreshSlot()
		self.category = self.navigationListBox.GetSelectedItem()
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OnSelectCategory: " + str(self.navigationListBox.GetSelectedItem()))
		self.BuildCategory()
		
	def OnScroll(self):
		viewItemCount = self.navigationListBox.GetViewItemCount()
		itemCount = self.navigationListBox.GetItemCount()
		pos = self.navigationScrollBar.GetPos() * (itemCount - viewItemCount)
		self.navigationListBox.SetBasePos(int(pos))	

	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.navigationScrollBar.OnUp()
		else:
			self.navigationScrollBar.OnDown()		

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()

	def Close(self):
		self.Hide()
	
class BuySingleItemDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.itemName = ""
		self.itemCurrency = ""
		self.currencyCount = 0
		self.itemShopIndex = 0
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "exscript/multishop_buydialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()
		
	def SetInfo(self, itemName, currencyName, currencyCount):
		self.itemName = itemName
		self.itemCurrency = currencyName
		self.currencyCount = currencyCount
		
		self.textLine.SetText(localeInfo.DO_YOU_BUY_ITEM_IN_MULTISHOP(self.itemName,self.count,self.currencyCount,self.itemCurrency))
		
	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

class BuyMultipleItemDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.itemName = ""
		self.itemCurrency = ""
		self.currencyCount = 0
		self.itemShopIndex = 0
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "exscript/multishop_buymultidialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.editLine = self.GetChild("inputEditLine")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")
	
	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetInfo(self, itemName, currencyName, currencyCount):
		self.itemName = itemName
		self.itemCurrency = currencyName
		self.currencyCount = currencyCount

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)
		
	def OnUpdate(self):
		if self.IsShow():
			
			tempCount = int(self.editLine.GetText())
			if tempCount > ITEM_STACK_COUNT:
				self.editLine.SetText(str(ITEM_STACK_COUNT))
			
			self.count = int(self.editLine.GetText())
			currencyRealCount = self.count * self.currencyCount
			self.textLine.SetText(localeInfo.DO_YOU_BUY_ITEM_IN_MULTISHOP(self.itemName,self.count,currencyRealCount,self.itemCurrency))
		
class MultiShopBoard(ui.ScriptWindow):
	slotImages = {}
	showDevSlotNumbers = 0
	DevSlotNumbers		= {}
	itemSlotsList 		= {}
	itemCurrencyType 	= {}
	itemCurrencyCount	= {}
	itemCountList		= {}
	
	currencyNames	= ["Yang","AP's","DP's","Coins","Vote-Coins","Drachencoins"]
	questIndex		= 0
	multishop_index	= 0
	
	multiShopInitX	= 0
	multiShopInitY	= 0
	
	currencyPlayerCount	= 0
	currencyType 	= 0

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()

	def Destroy(self):
		if self.itemBuyQuestionDialog:
			self.itemBuyQuestionDialog.Close()
			self.itemBuyQuestionDialog = None
		self.__del__()
		
	def closeX(self):
		self.ResetMultiShop()
		self.Board.Hide()
		
	def LoadUI(self):

		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(190, 330)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Multishop")
		self.Board.SetCloseEvent(self.closeX)
		self.Board.Show()

		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()
		i = 0
		line_width 	= 5
		line_height = 8
		
		line_width_count 	= 0
		line_height_count	= 0
		
		start_height = 35
		start_width = 15
		
		max_slots = 40
		
		while i < max_slots:
		
			self.slotImages[i] = ui.ImageBox()
			self.slotImages[i].SetParent(self.Board)
			self.slotImages[i].SetPosition(start_width,start_height)
			self.slotImages[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			self.slotImages[i].Show()	
			
			self.DevSlotNumbers[i] = ui.TextLine()
			self.DevSlotNumbers[i].SetParent(self.slotImages[i])
			self.DevSlotNumbers[i].SetPosition(16,16)
			self.DevSlotNumbers[i].SetText(str(i))
			self.DevSlotNumbers[i].SetHorizontalAlignRight()
			if self.showDevSlotNumbers == 1:
				self.DevSlotNumbers[i].Show()			
			
			
			
			
			start_width = start_width + 32
				
			line_width_count = line_width_count + 1
			if line_width_count == line_width:
				start_width = 15
				start_height = start_height + 32
				line_width_count = 0				

			i = i + 1
			
		self.CurrencyIcon = ui.ImageBox()
		self.CurrencyIcon.SetParent(self.Board)
		self.CurrencyIcon.SetPosition(20,296)
		self.CurrencyIcon.LoadImage("d:/ymir work/ui/daily.dds")
		self.CurrencyIcon.Show()

		self.CurrencyBG = ui.ImageBox()
		self.CurrencyBG.SetParent(self.Board)
		self.CurrencyBG.SetPosition(40,295)
		self.CurrencyBG.LoadImage("d:/ymir work/ui/public/parameter_slot_05.sub")
		self.CurrencyBG.Show()	

		self.CurrencyTextLine = ui.TextLine()
		self.CurrencyTextLine.SetParent(self.Board)
		self.CurrencyTextLine.SetPosition(164,297)
		self.CurrencyTextLine.SetText("")
		self.CurrencyTextLine.SetHorizontalAlignRight()
		self.CurrencyTextLine.Show()
		
		self.itemSlots = ui.GridSlotWindow()  
		self.itemSlots.SetParent(self.Board)  
		
		self.itemSlots.ArrangeSlot(0,5,8,32,32,0,0)  
		self.itemSlots.SetPosition(15,35)  
		self.itemSlots.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.itemSlots.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
		self.itemSlots.SetSelectItemSlotEvent(ui.__mem_func__(self.BuyItem))  
		self.itemSlots.SAFE_SetButtonEvent("RIGHT", "ALWAYS", self.BuyItem)
		self.itemSlots.Show()

		self.itemBuyQuestionDialog = None
		self.Board.Hide()

	def BuyItem(self,slot):
		if self.questIndex == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] FEHLER: Kein Questindex vorhanden!")
			return
		
		item.SelectItem(self.itemSlotsList[slot])
		itemName = item.GetItemName()
		currencyType	= self.itemCurrencyType[slot]		

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM_IN_MULTISHOP(itemName, self.itemCountList[slot], constInfo.NumberToPointString(self.itemCurrencyCount[slot]), self.currencyNames[currencyType]))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.slotPos = slot
		self.itemBuyQuestionDialog = itemBuyQuestionDialog
		return
		
	def RequestDropItem(self,answer):
	
		if not self.itemBuyQuestionDialog:
			return

		if answer:
			slotPos = self.itemBuyQuestionDialog.slotPos
			currencyCount	= self.itemCurrencyCount[slotPos]
			
			if currencyCount > self.currencyPlayerCount:			
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Du kannst dir diesen Gegenstand nicht leisten!")
				self.itemBuyQuestionDialog.Close()
				self.itemBuyQuestionDialog = None
				return
				
				
			constInfo.INPUT_CMD = "buy#" + str(self.multishop_index) + "#" + str(slotPos) + "#"
			event.QuestButtonClick(self.questIndex)
			

		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None
		return

	def ShowToolTip(self,slot):
		item.SelectItem(self.itemSlotsList[slot])
		self.itemtooltip.ClearToolTip()
		self.itemtooltip.AddItemData(self.itemSlotsList[slot], [0, 0, 0, 0, 0, 0])
		
		time = 0
		if item.GetItemType() == 16:
			if item.GetValue(0) > 0:
				time = item.GetValue(0)
				
		if item.GetItemType() == 28:
			(limittype,limitvalue) = item.GetLimit(0)
			time = int(limitvalue/60)

		if item.GetItemType() == 18:
			(limittype,limitvalue) = item.GetLimit(0)
			if limittype == 7 and limitvalue > 0:
				time = int(limitvalue/60)
			
		if time > 0:
			time = int(time/60)
			time_str = "Stunden"
			if time >= 48:
				time = int(time/24)
				time_str = "Tage"
			
			self.itemtooltip.AppendSpace(5)
			self.itemtooltip.AppendTextLine("[ Laufzeit ]", self.itemtooltip.SPECIAL_TITLE_COLOR)	
			self.itemtooltip.AppendTextLine(str(time) + " " + str(time_str), self.itemtooltip.NORMAL_COLOR)

		#currencyNames	= ["Yang","AP's","DP's"]
		currencyType	= self.itemCurrencyType[slot]
		currencyCount	= self.itemCurrencyCount[slot]
		
		if currencyCount > self.currencyPlayerCount:
			self.CurrencyTextLine.SetFontColor(0.9, 0.4745, 0.4627)
		else:
			self.CurrencyTextLine.SetFontColor(0.5411, 0.7254, 0.5568)
		self.itemtooltip.AppendSpace(5)
		self.itemtooltip.AppendTextLine("[ Kaufpreis ]", self.itemtooltip.SPECIAL_TITLE_COLOR)		
		
		self.itemtooltip.AppendTextLine(constInfo.NumberToPointString(currencyCount) + " " + self.currencyNames[currencyType], self.itemtooltip.NORMAL_COLOR)			
		self.itemtooltip.ShowToolTip()		
	
	def HideToolTip(self):
		self.CurrencyTextLine.SetFontColor(1.0, 1.0, 1.0)
		self.itemtooltip.HideToolTip()
		
	
	
	# Functions for game.py -----------------------------------------------------------------------
	def HideMultiShop(self):
		self.ResetMultiShop()
		self.Board.Hide()
		
	def ShowMultiShop(self):
		
		(self.multiShopInitX, self.multiShopInitY, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		self.Board.Show()
		
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] self.ShowMultiShop")
	
	def ResetMultiShop(self):
		for i in xrange(40):
			self.itemSlots.SetItemSlot(i, 0, 0)
			self.itemSlots.RefreshSlot()		
		if self.itemBuyQuestionDialog:
			self.itemBuyQuestionDialog.Close()
			self.itemBuyQuestionDialog = None	
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] self.ResetMultiShop")
		
	def SetMultiShopTitle(self,title):
		self.Board.SetTitleName(title)
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] self.SetMultiShopTitle")
		
	def SetMultiShopCurrency(self,currencyType,currencyAmount):
		currencyIcons 	= ["d:/ymir work/ui/game/windows/money_icon.sub","d:/ymir work/ui/achievement_small.dds","d:/ymir work/ui/daily.dds","d:/ymir work/ui/game/windows/money_icon.sub","d:/ymir work/ui/game/windows/money_icon.sub","d:/ymir work/ui/game/windows/money_icon.sub"]
		#currencyNames	= ["Yang","AP's","DP's"]
		self.CurrencyIcon.LoadImage(currencyIcons[currencyType])
		self.CurrencyTextLine.SetText(constInfo.NumberToPointString(currencyAmount) + " " + self.currencyNames[currencyType])
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] self.SetMultiShopCurrency")
		
		
		self.currencyPlayerCount = currencyAmount
		#self.currencyType = currencyType
		
	def SetMultiShopItemSlot(self,itemVnum,itemCount,slotPos,currencyType,itemPrice):
		
		self.itemSlotsList[slotPos] 		= int(itemVnum)
		self.itemCurrencyType[slotPos] 		= int(currencyType)
		self.itemCurrencyCount[slotPos]		= int(itemPrice)
		self.itemCountList[slotPos]			= int(itemCount)
		
		#itemCount = min(0,itemCount)
		self.itemSlots.SetItemSlot(slotPos, itemVnum, itemCount)
		self.itemSlots.RefreshSlot()
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] self.SetMultiShopItemSlot")
		
	def SetMultiShopIndex(self,multiShopIndex):
		self.multishop_index = multiShopIndex
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] self.SetMultiShopIndex")
		
	def SetMultiShopQuestIndex(self,curQuestIndex):
		self.questIndex = int(curQuestIndex)
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"[Multishop] self.SetMultiShopQuestIndex")
		
	def IsMultiShopOpen(self):
		if self.Board.IsShow():
			return True
		else:
			return False
		
#MultiShopBoard().Show()


# MultiShopWindow().Show()