## Developed by Exterminatus!
import ui
import chat
import app
import snd
import item
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import uiCommon
import exterminatus
import craftingproto
import fgGHGjjFHJghjfFG1545gGG as player
import event
import localeInfo


class CraftingWindow(ui.ScriptWindow):

	LIMIT_RANGE = 500

	qid = 0
	crafting_proto_name = "NONE"
	category_sel = -1
	selected_recipe = -1
	
	materialItemSlots = {}
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/craftingwindow.py")
		except:
			import exception
			exception.Abort("CraftingWindow.LoadWindow.LoadObject")
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		# self.BuildSearchBar()
		self.BuildNavigation()
		self.BuildInfoPage()
		# self.Show()
		# self.SetProto("ALCHEMIST")
		# self.LoadProto("ALCHEMY_TOWN")
		
		
	def BuildNavigation(self):
		self.navigationBoard = self.GetChild("navigationBoard")
		self.navigation = CraftingListBox(self)
		self.navigation.SetParent(self.navigationBoard)
		self.navigation.SetPosition(0,0)		

		self.navigation.ClearAll()


	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.navigation.scrollBar.OnUp()
		else:
			self.navigation.scrollBar.OnDown()
		
	def BuildInfoPage(self):
		self.infoPage = self.GetChild("infoBoard")
		self.itemSlot = self.GetChild("desiredItemSlot")
		self.noItemPage = self.GetChild("noItemSelectBoard")

		self.itemNameTextLine = self.GetChild("itemNameText")
		self.itemCountTextLine = self.GetChild("itemCountText")
		self.itemChanceTextLine = self.GetChild("itemChanceText")
				
		
		x = 22
		y = 8 + 96 + 10 + 29 + 5 + 15 + 10
		for i in xrange(10):
			self.materialItemSlots[i] = exterminatus.EasyItemSlot()
			self.materialItemSlots[i].SetParent(self.infoPage)
			self.materialItemSlots[i].SetPosition(x+2,y+2)
			self.materialItemSlots[i].SetItemData(70031)
			self.materialItemSlots[i].SetItemCount(10)
			self.materialItemSlots[i].Show()
			
			if i == 4:
				x = 22
				y = y + 42
			else:
				x = x + 42
		
		self.money = self.GetChild("money")
		self.craftButton = self.GetChild("craftButton")
		self.craftButton.SetEvent(self.DoCraft)
	
	def SetQID(self,qid):
		self.qid = int(qid)
		
	def SetProto(self,proto):
		self.LoadProto(proto)
		
	def DoCraft(self):
		if self.qid == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Crafting> No QID!")
			return
			
		data = craftingproto.GetCraftingProto(self.crafting_proto_name)
		if data == False:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Crafting> No Proto named " + proto)
			return

		# materialList = data["material_list"]
		# for i in xrange(len(materialList)):
		
			# count = 0
			# for c in range(0,(90*5)-1):
				# if player.GetItemIndex(c) == materialList[i][0]:
					# count = count + player.GetItemCount(c)		
		
			# if count < materialList[i][1]:
				# chat.AppendChat(chat.CHAT_TYPE_INFO,"Dir fehlen die nötigen Materialien!")
				# return

		constInfo.INPUT_CMD = "craft#" + self.crafting_proto_name + "#" + str(self.selected_recipe)
		event.QuestButtonClick(self.qid)		

	# def OnRunMouseWheel(self, nLen):
		# if nLen > 0:
			# self.navListBox.OnUp()
		# else:
			# self.navListBox.OnDown()	

	# def OnScroll(self):
		# viewItemCount = self.navListBox.GetViewItemCount()
		# itemCount = self.navListBox.GetItemCount()
		# pos = self.navScrollBar.GetPos() * (itemCount - viewItemCount)
		# self.navListBox.SetBasePos(int(pos))	


	def LoadProto(self,proto):
	
		data = craftingproto.GetCraftingProto(proto)
		if data == False:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Crafting> No Proto named " + proto)
			return

		self.crafting_proto_name	= proto		

		self.LoadNavigation(data)


	def LoadNavigation(self,data):
		# data = craftingproto.CRAFTING_PROTO[self.crafting_proto_name][0]["category_data"]
		self.navigation.ClearAll()
		
		data = data["CONTENT"]
		for i in xrange(len(data)):
			chat.AppendChat(chat.CHAT_TYPE_INFO, "i: " + str(i))
			if data[i]["type"] == "title":
				self.navigation.AppendTitleItem(data[i]["text"])
			
			# elif data[i]["type"] == "nav_item":
				# self.navigation.AppendNavItem(data[i]["category_name"],0,i,False)

			elif data[i]["type"] == "item":
				item.SelectItem(data[i]["itemVnum"])
				self.navigation.AppendNavItem(item.GetItemName(),data[i]["itemVnum"],i,True)
			
			elif data[i]["type"] == "empty":
				self.navigation.AppendEmptyItem()
				
			# elif data[i]["type"] == "back_item":
				# self.navigation.AppendBackItem()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Unknown category_type: " + str(data[i]["type"]))

		self.navigation.Build()			


	def LoadSubNavigation(self,index):
		chat.AppendChat(chat.CHAT_TYPE_INFO,"LoadSubNavigation CLICK!")
		self.selected_recipe = index
		self.LoadInfoPage()
		

	def LoadTopNavigation(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO,"LoadTopNavigation CLICK!")
		# self.category_sel = -1
		# data = craftingproto.CRAFTING_PROTO[self.crafting_proto_name][0]["category_data"]
		# self.LoadNavigation(data)

	def LoadInfoPage(self):
		data = craftingproto.GetCraftingProto(self.crafting_proto_name)
		if data == False:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "<Crafting> No Proto named " + self.crafting_proto_name)
			return
			
		data = data["CONTENT"][self.selected_recipe]
		item.SelectItem(data["itemVnum"])
		self.itemSlot.SetItemSlot(0,data["itemVnum"],0)
		
		self.itemNameTextLine.SetText(localeInfo.CRAFTING_WINDOW_NAME + item.GetItemName())
		self.itemCountTextLine.SetText(localeInfo.CRAFTING_WINDOW_COUNT + str(data["itemCount"]))
		self.itemChanceTextLine.SetText(localeInfo.CRAFTING_WINDOW_CHANCE + str(data["baseChance"]) + "%")		
		
		materialList = data["materialList"]
		for i in xrange(10):
			try:
				self.materialItemSlots[i].ClearItemData()
				self.materialItemSlots[i].SetItemData(materialList[i]["item"])
				self.materialItemSlots[i].SetItemCount(materialList[i]["itemCount"])

			except:
				self.materialItemSlots[i].ClearItemData()



		self.money.SetText(constInfo.NumberToPointString(data["gold"]) + localeInfo.CRAFTING_WINDOW_GOLD)
		
		self.noItemPage.Hide()	
			

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			(self.xStart, self.yStart, z) = player.GetMainCharacterPosition()
			self.Show()

	def Close(self):
		self.Hide()
		
	def OnUpdate(self):
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xStart) > self.LIMIT_RANGE or abs(y - self.yStart) > self.LIMIT_RANGE:
			self.Close()
			
class CraftingListBox(ui.Window):

	width = 250
	height = 420 - 65 + 15
	item_max = 19
	itemList = []
	
	class TitleItem(ui.Window):

		def __init__(self):
			ui.Window.__init__(self)
			self.SetSize(250,17)
			self.MakeTitleBar()
			self.Show()
			
		def MakeTitleBar(self):
			self.titleBar = ui.HorizontalBar()
			self.titleBar.SetParent(self)
			self.titleBar.SetPosition(1,0)
			self.titleBar.Create(250 - 3)
			self.titleBar.Show()
			
			self.textLine = ui.TextLine()
			self.textLine.SetParent(self.titleBar)
			self.textLine.SetPosition(9,2)
			self.textLine.SetPackedFontColor(0xFFFFE3AD)
			self.textLine.Show()
			
		def SetText(self,text):
			self.textLine.SetText(text)
			
		def SetScrollBarMode(self,mode):
			if mode:
				self.titleBar.SetWidth(250 - 2 - 16)
				self.SetSize(250 - 3 - 16,17)
			else:
				self.titleBar.SetWidth(250 - 3)
				self.SetSize(250 - 2,17)

	class NavItem(ui.Window):
		text = ""
		item_vnum = 0
		index = 0
		isRecipe = False
		
		def __init__(self,wndListBox):
			ui.Window.__init__(self)
			self.wndListBox = wndListBox
			self.SetSize(250,17)
			self.MakeTitleBar()
			self.toolTip = uiToolTip.ItemToolTip()
			self.toolTip.HideToolTip()
			self.Show()
			
		def MakeTitleBar(self):
			self.thinBoard = ui.ThinBoardCircle()
			self.thinBoard.SetParent(self)
			self.thinBoard.SetPosition(1,0)
			self.thinBoard.SetSize(250 - 2,17)
			self.thinBoard.Show()
			
			self.textLine = ui.TextLine()
			self.textLine.SetParent(self.thinBoard)
			self.textLine.SetPosition(9,2)
			self.textLine.SetText("")
			self.textLine.Show()
	
		def SetText(self,text):
			self.text = text
			self.textLine.SetText(text)
			
		def SetItem(self,item_vnum):
			self.item_vnum = item_vnum
			
		def SetEventIndex(self,index):
			self.index = index
			self.thinBoard.SetOnClickEvent(self.wndListBox.OnClickItem,index)
		
		# def SetRecipe(self,isRecipe):
			# self.isRecipe = isRecipe
		
		def OnUpdate(self):
			if self.thinBoard.IsIn():
				self.textLine.SetPosition(9 + 5,2)
				self.textLine.SetFontColor(0.5411, 0.7254, 0.5568)		
				if self.item_vnum > 0:
					self.toolTip.ClearToolTip()
					self.toolTip.AddItemData(self.item_vnum, [0, 0, 0, 0, 0, 0])
					self.toolTip.ShowToolTip()					
			else:
				self.textLine.SetPosition(9,2)
				self.textLine.SetFontColor(1.0, 1.0, 1.0)	
				if self.item_vnum > 0:
					self.toolTip.HideToolTip()

		def SetScrollBarMode(self,mode):
			if mode:
				self.thinBoard.SetSize(250 - 2 - 16,17)
				self.SetSize(250 - 2 - 16,17)
			else:
				self.thinBoard.SetSize(250 - 2,17)	
				self.SetSize(250 - 2,17)	

	class BackItem(ui.Window):

		def __init__(self,wndListBox):
			ui.Window.__init__(self)
			self.wndListBox = wndListBox
			self.SetSize(250,17)
			self.MakeTitleBar()
			self.Show()
			
		def MakeTitleBar(self):
			self.thinBoard = ui.ThinBoardCircle()
			self.thinBoard.SetParent(self)
			self.thinBoard.SetPosition(1,0)
			self.thinBoard.SetSize(250 - 2,17)
			self.thinBoard.Show()
			
			self.textLine = ui.TextLine()
			self.textLine.SetParent(self.thinBoard)
			self.textLine.SetPosition(9,2)
			self.textLine.SetText("Zurück")
			self.textLine.Show()

			self.thinBoard.SetOnClickEvent(self.wndListBox.OnClickBackItem)
			
		def OnUpdate(self):
			if self.thinBoard.IsIn():
				self.textLine.SetPosition(9 + 5,2)
				self.textLine.SetFontColor(0.9, 0.4745, 0.4627)						
			else:
				self.textLine.SetPosition(9,2)
				self.textLine.SetFontColor(1.0, 1.0, 1.0)	


		def SetScrollBarMode(self,mode):
			if mode:
				self.thinBoard.SetSize(250 - 2 - 16,17)
				self.SetSize(250 - 2 - 16,17)
			else:
				self.thinBoard.SetSize(250 - 2,17)	
				self.SetSize(250 - 2,17)

	class EmptyItem(ui.Window):

		def __init__(self):
			ui.Window.__init__(self)
			self.SetSize(250 -2 - 16,17)
			self.Show()
	
		def SetScrollBarMode(self,mode):
			return
	
	def __init__(self,wndCrafting):
		ui.Window.__init__(self)
		self.wndCrafting = wndCrafting
		self.SetSize(self.width,self.height)
		self.MakeScrollBar()
		self.Show()
		
	def MakeScrollBar(self):
		self.scrollBar = ui.SmallThinScrollBar()
		self.scrollBar.SetParent(self)
		self.scrollBar.SetPosition(248 - 20 + 7,1)
		self.scrollBar.CreateScrollBar()
		self.scrollBar.SetScrollBarSize(420 - 65 - 15 - 2 + 3)
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.scrollBar.Hide()		
		
	def OnClickItem(self,index):
		chat.AppendChat(chat.CHAT_TYPE_INFO,"Aua, du hast auf item " + str(index) + " geklickt!")
		self.wndCrafting.LoadSubNavigation(index)

	def OnClickBackItem(self):
		# chat.AppendChat(chat.CHAT_TYPE_INFO,"Und zurück...")
		self.wndCrafting.LoadTopNavigation()
		
	def AppendTitleItem(self,text):
		titleItem = self.TitleItem()
		titleItem.SetParent(self)
		titleItem.SetText(text)
		titleItem.Hide()
		self.itemList.append(titleItem)

	def AppendNavItem(self,text,item_vnum,index,isRecipe):
		navItem = self.NavItem(self)
		navItem.SetParent(self)
		navItem.SetText(text)
		navItem.SetItem(item_vnum)
		# navItem.SetRecipe(isRecipe)
		navItem.SetEventIndex(index)
		navItem.Hide()
		self.itemList.append(navItem)
		
	def AppendBackItem(self):
		backItem = self.BackItem(self)
		backItem.SetParent(self)
		backItem.Hide()
		self.itemList.append(backItem)		
		
	def AppendEmptyItem(self):
		emptyItem = self.EmptyItem()
		emptyItem.SetParent(self)
		emptyItem.Hide()
		self.itemList.append(emptyItem)		
	
	def RenderListBox(self):
		scrollBarLenght = self.isScrollLength()
		if scrollBarLenght:
			self.scrollBar.Show()
			pos = int(self.scrollBar.GetPos() * (len(self.itemList) - self.item_max)) 
			y = 1
			for i in xrange(self.item_max):
				realPos = pos + i
				self.itemList[realPos].SetPosition(1,y)
				self.itemList[realPos].SetScrollBarMode(True)
				self.itemList[realPos].Show()
				y = y + 18
		else:
			y = 1
			self.scrollBar.Hide()
			for i in xrange(len(self.itemList)):
				self.itemList[i].SetPosition(1,y)
				self.itemList[i].SetScrollBarMode(False)
				self.itemList[i].Show()
				y = y + 18
			
	def HideAllItems(self):
		for i in xrange(len(self.itemList)):
			self.itemList[i].Hide()		


	# def OnRunMouseWheel(self, nLen):
		# if nLen > 0:
			# self.scrollBar.OnUp()
		# else:
			# self.scrollBar.OnDown()
			
	def OnScroll(self):
		self.HideAllItems()
		self.RenderListBox()
			
	def Build(self):
		self.HideAllItems()
		self.RenderListBox()
		
	def ClearAll(self):
		self.HideAllItems()
		self.itemList = []
		self.scrollBar.SetPos(0.0)
		self.scrollBar.Hide()

	def isScrollLength(self):
		if len(self.itemList) > self.item_max:
			return True
		else:
			return False
	
			
	def __del__(self):
		ui.Window.__del__(self)


