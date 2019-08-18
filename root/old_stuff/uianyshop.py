# Python File written by Kilroy.
# Function: AnyShop Lua/Python/Sql
# Pythonpart: 1/1

import ui
import GFHhg54GHGhh45GHGH
import app
import grp
import chat
import item
import event
import wndMgr
import uiCommon
import constInfo
import uiToolTip

IMAGE_SLIDE_SHOW = ["locale/de/ui/interfaces/ingame_shops/imageshow/show1.tga", "locale/de/ui/interfaces/ingame_shops/imageshow/show2.tga"]


class AnyShop(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__EasyBuild = EasyBuildKilroy()

	def BuildWindow(self):

		w, h = 750, 530
		self.ShopBoard = self.__EasyBuild.CreateBoardWithTitle(-1, -1, w, h)
		self.ShopBoard.SetTitleName("Multishop")
		self.ShopBoard.SetCloseEvent(self.Open)
		self.ShopBoard.SetCenterPosition()

		control = PageControl()
		control.SetParent(self.ShopBoard)
		control.SetPosition(60,70)
		control.SetSize(w-55, h-85)

		self.GuiTabs = []
		tab = Page(Startseite(), "Startseite")
		tab.SetParent(self.ShopBoard)
		control.AddPage(tab)
		tab.Show()
		self.GuiTabs += [tab]

		for key in constInfo.INGAME_SHOPS_CONFIG["SHOPNAMEN"]:
			tab = Page(Shop(key), constInfo.INGAME_SHOPS_CONFIG["SHOPNAMEN"][key])
			tab.SetParent(self.ShopBoard)
			control.AddPage(tab)
			tab.Hide()
			self.GuiTabs += [tab]


		self.moneyBars = {}
		x = 85
		for key in constInfo.INGAME_SHOPS_CONFIG["MONEY"]:
			bar = self.__EasyBuild.CreateResizableButton(
								self.ShopBoard, x, 40, 160, 25, "%d %s" % (tuple(constInfo.INGAME_SHOPS_CONFIG["MONEY"][key])),
								self.__None, None,
								(0.0,0.0,0.0,1.0),
								(0.0,0.0,0.0,1.0),
								(0.0,0.0,0.0,1.0)
							)
			bar.SetUpEdgeColor(0.2, 0.2, 0.2, 1.0)
			x += 200
			self.moneyBars[key] = bar 


		control.Show()
		self.control = control
		self.control.ArrangeTitleBar()
		self.Show()


	def __None(self):
		pass

	def ReloadMoney(self):
		for key in constInfo.INGAME_SHOPS_CONFIG["MONEY"]:
			self.moneyBars[key].SetText("%d %s" % tuple(constInfo.INGAME_SHOPS_CONFIG["MONEY"][key]))

	def Open(self):
		if self.IsShow():
			self.ShopBoard.Hide()
			self.Hide()
			return
		constInfo.INGAME_SHOPS_CONFIG["CMD"] = "open/"
		event.QuestButtonClick(int(constInfo.INGAME_SHOPS_CONFIG["INDEX"]))

	def Configuration(self, cmd):
		CMD = cmd.split("/")
		if CMD[0]=="index":
			constInfo.INGAME_SHOPS_CONFIG["INDEX"] = int(CMD[1])
		elif CMD[0]=="input":
			GFHhg54GHGhh45GHGH.SendQuestInputStringPacket(str(constInfo.INGAME_SHOPS_CONFIG["CMD"]))
			constInfo.INGAME_SHOPS_CONFIG["CMD"] = ""
		elif CMD[0]=="config":
			for INFO in CMD[1].split("|"):
				INFO = INFO.split(",")
				constInfo.INGAME_SHOPS_CONFIG["MONEY"][int(INFO[3])] = [int(INFO[0]), INFO[1]]
				constInfo.INGAME_SHOPS_CONFIG["SHOPNAMEN"][int(INFO[3])] = INFO[2]
		elif CMD[0]=="ClearBoard":
			constInfo.INGAME_SHOPS_CONFIG["SHOPS"] = {}
			constInfo.INGAME_SHOPS_CONFIG["SHOPNAMEN"] = {}
			constInfo.INGAME_SHOPS_CONFIG["MONEY"] = {}
			constInfo.INGAME_SHOPS_CONFIG["ANGEBOTE"] = []
			constInfo.INGAME_SHOPS_CONFIG["MEISTGEKAUFT"] = []
			constInfo.INGAME_SHOPS_CONFIG["CATEGORIES"] = {}
		elif CMD[0]=="setmoney":
			constInfo.INGAME_SHOPS_CONFIG["MONEY"][int(CMD[1])][0] = int(CMD[2])
			self.ReloadMoney()
		elif CMD[0]=="FinishSending":
			self.BuildWindow()
		elif CMD[0]=="AddToList": 
			for ITEM in CMD[1].split("|"):
				ITEM = ITEM.split(",")

				ITEM[1] = int(ITEM[1])
				if not ITEM[1] in constInfo.INGAME_SHOPS_CONFIG["SHOPS"]:
					constInfo.INGAME_SHOPS_CONFIG["SHOPS"][ITEM[1]] = {}
				if not ITEM[2] in constInfo.INGAME_SHOPS_CONFIG["SHOPS"][ITEM[1]]:
					constInfo.INGAME_SHOPS_CONFIG["SHOPS"][ITEM[1]][ITEM[2]] = []

				if not ITEM[1] in constInfo.INGAME_SHOPS_CONFIG["CATEGORIES"]:
					constInfo.INGAME_SHOPS_CONFIG["CATEGORIES"][ITEM[1]] = {}
				constInfo.INGAME_SHOPS_CONFIG["CATEGORIES"][ITEM[1]][int(ITEM[7])] = ITEM[2]

				itemlist = [ int(ITEM[0]), int(ITEM[5]), int(ITEM[3]), ITEM[6], int(ITEM[4]), ITEM[1]]
				constInfo.INGAME_SHOPS_CONFIG["SHOPS"][ITEM[1]][ITEM[2]].append(itemlist)

				if (int(ITEM[5])>0 and int(ITEM[4])>0) and len(constInfo.INGAME_SHOPS_CONFIG["ANGEBOTE"])<10:
					constInfo.INGAME_SHOPS_CONFIG["ANGEBOTE"].append(itemlist)
				if len(constInfo.INGAME_SHOPS_CONFIG["MEISTGEKAUFT"])<10:
					constInfo.INGAME_SHOPS_CONFIG["MEISTGEKAUFT"].append(itemlist)

class Startseite(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.__EasyBuild = EasyBuildKilroy()

		self.barMitte = self.__EasyBuild.CreateImage(self, 0, 20, "locale/de/ui/interfaces/ingame_shops/barmitte.tga")

		global IMAGE_SLIDE_SHOW
		if len(IMAGE_SLIDE_SHOW)!=0:
			self.SlideShow = ImageSlideShow()
			self.SlideShow.SetParent(self.barMitte)
			self.SlideShow.SetPosition(4,4)
			for image in IMAGE_SLIDE_SHOW:
				self.SlideShow.AddImage(image)
			self.SlideShow.Show()

		self.barUnten = self.__EasyBuild.CreateImage(self, 0, 250, "locale/de/ui/interfaces/ingame_shops/barunten.tga")
		self.barRechts = self.__EasyBuild.CreateImage(self, 465, 20, "locale/de/ui/interfaces/ingame_shops/barrechts.tga")
		self.barUntenHead = self.__EasyBuild.CreateImage(self.barUnten, 0, 0, "locale/de/ui/interfaces/ingame_shops/baruntenhead.tga")
		self.barRechtsHead = self.__EasyBuild.CreateImage(self.barRechts, 0, 0, "locale/de/ui/interfaces/ingame_shops/baruntenhead.tga")

		self.barRechtsHeadText = self.__EasyBuild.CreateTextLine(self.barRechtsHead, 5,2, "Aktuelle Angebote:", "normal")
		self.barUntenHeadText = self.__EasyBuild.CreateTextLine(self.barUntenHead, 5,2, "Die Meistverkauften:", "normal")

		self.ScrollItemsVertical = []
		self.ScrollItemsHorizontal = []
		self.LoadScrollHorizontal()
		self.LoadScrollVertical()

	def LoadScrollHorizontal(self):
		ItemList = constInfo.INGAME_SHOPS_CONFIG["MEISTGEKAUFT"]
		for i in xrange(len(self.ScrollItemsHorizontal)):
			self.ScrollItemsHorizontal[i].Close()

		self.ScrollItemsHorizontal = []

		self.ScrollBarHorizontal = self.__EasyBuild.CreateHorizontalScrollbar(self.barUnten, 420, 20, 131)
		self.ScrollBarHorizontal.barSlot.Hide()
		board_amount = 3
		for i in xrange(min(board_amount, len(ItemList))):
			self.ScrollItemsHorizontal += [ scrollBoard(self.barUnten, 37.5 + 130 * i, 40) ]
			self.ScrollItemsHorizontal[-1].SetButtonInfo(ItemList[i])
		if len(ItemList) <= board_amount:
			self.ScrollBarHorizontal.Hide()
		else:
			self.ScrollBarHorizontal.SetMiddleBarSize(float(board_amount) / float(len(ItemList)))
			self.ScrollBarHorizontal.Show()
		self.ScrollBarHorizontal.SetScrollEvent(self.__OnScrollHorizontal)

	def __OnScrollHorizontal(self):
		ItemList = constInfo.INGAME_SHOPS_CONFIG["MEISTGEKAUFT"]
		board_amount = len(self.ScrollItemsHorizontal)
		pos = int(self.ScrollBarHorizontal.GetPos() * (len(ItemList) - board_amount))

		for i in xrange(board_amount):
			realPos = i + pos
			self.ScrollItemsHorizontal[i].SetButtonInfo(ItemList[realPos])


	def LoadScrollVertical(self):
		ItemList = constInfo.INGAME_SHOPS_CONFIG["ANGEBOTE"]
		if len(self.ScrollItemsVertical)!=0:
			for i in xrange(len(self.ScrollItemsVertical)):
				self.ScrollItemsVertical[i].Close()

		self.ScrollItemsVertical = []

		self.ScrollBarVertical = self.__EasyBuild.CreateScrollbar(self.barRechts, 270, 140, 20)
		self.ScrollBarVertical.barSlot.Hide()
		board_amount = 2
		for i in xrange(min(board_amount, len(ItemList))):
			self.ScrollItemsVertical += [ scrollBoard(self.barRechts, 10, 50 + 130 * i) ]
			self.ScrollItemsVertical[-1].SetButtonInfo(ItemList[i])

		if len(ItemList) <= board_amount:
			self.ScrollBarVertical.Hide()
		else:
			self.ScrollBarVertical.SetMiddleBarSize(float(board_amount) / float(len(ItemList)))
			self.ScrollBarVertical.Show()

		self.ScrollBarVertical.SetScrollEvent(self.__OnScrollVertical)

	def __OnScrollVertical(self):
		ItemList = constInfo.INGAME_SHOPS_CONFIG["ANGEBOTE"]
		board_amount = len(self.ScrollItemsVertical)
		pos = int(self.ScrollBarVertical.GetPos() * (len(ItemList) - board_amount))

		for i in xrange(board_amount):
			realPos = i + pos
			self.ScrollItemsVertical[i].SetButtonInfo(ItemList[realPos])


class Shop(ui.Window):
	def __init__(self, id):
		ui.Window.__init__(self)
		self.__EasyBuild = EasyBuildKilroy()
		self.ShopId = id
		self.ButtonList = []
		self.ItemList = []

		self.barButton = self.__EasyBuild.CreateImage(self, 0, 20, "locale/de/ui/interfaces/ingame_shops/barbutton.tga")
		self.barItem = self.__EasyBuild.CreateImage(self, 150, 20, "locale/de/ui/interfaces/ingame_shops/baritem.tga")
		self.siteText = self.__EasyBuild.CreateTextLine(self.barItem, 460,5, "0/0", "normal")

		if id in constInfo.INGAME_SHOPS_CONFIG["SHOPS"]:
			self.ButtonList = list(constInfo.INGAME_SHOPS_CONFIG["CATEGORIES"][id].values())
			self.ScrollButtons = []
			self.ScrollItem = None
			self.LoadScrollButton()
			self.LoadScrollItems()


	def LoadScrollButton(self):

		for i in xrange(len(self.ScrollButtons)):
			self.ScrollButtons[i].Close()

		self.ScrollButtons = []
		button_amount = 9

		self.ScrollBar = self.__EasyBuild.CreateScrollbar(self.barButton, 345, 5, 10)
		self.ScrollBar.barSlot.Hide()

		for i in xrange(min(button_amount, len(self.ButtonList))):
			x = 25
			if len(self.ButtonList) <= button_amount:
				x -= 8
			self.ScrollButtons += [ scrollButton(self.barButton, x, 23 + 35 * i) ]
			self.ScrollButtons[-1].SetButtonInfo(self.ButtonList[i], (ui.__mem_func__(self.LoadScrollItems), self.ButtonList[i]))

		if len(self.ButtonList) <= button_amount:
			self.ScrollBar.Hide()
		else:
			self.ScrollBar.SetMiddleBarSize(float(button_amount) / float(len(self.ButtonList)))
			self.ScrollBar.Show()

		self.ScrollBar.SetScrollEvent(self.__OnScrollButton)

	def __OnScrollButton(self):
		button_amount = len(self.ScrollButtons)
		pos = int(self.ScrollBar.GetPos() * (len(self.ButtonList) - button_amount))

		for i in xrange(button_amount):
			realPos = i + pos
			self.ScrollButtons[i].SetButtonInfo(self.ButtonList[realPos], (ui.__mem_func__(self.LoadScrollItems), self.ButtonList[realPos]))


	def LoadScrollItems(self, button=""):
		ItemList = constInfo.INGAME_SHOPS_CONFIG["SHOPS"][self.ShopId]
		if button=="":
			ItemList = ItemList[self.ButtonList[0]]
		else:
			ItemList = ItemList[button]

		if self.ScrollItem:
			self.ScrollItem.Close()

		self.ScrollItem = None

		site_amount = (len(ItemList)//9)
		if len(ItemList)%9!=0:
			site_amount += 1

		self.site_amount = site_amount
		self.ItemList = ItemList


		self.ScrollBarHorizontal = self.__EasyBuild.CreateHorizontalScrollbar(self.barItem, 475, 5, 340)
		self.ScrollBarHorizontal.barSlot.Hide()

		self.siteText.SetText("1/%d" % self.site_amount)

		self.ScrollItem = scrollBoardItemHorizontal(self.barItem, 35, 30)
		self.ScrollItem.SetButtonInfo(self.ItemList[0:9:1])

		if len(self.ItemList) <= 9:
			self.ScrollBarHorizontal.Hide()
		else:
			self.ScrollBarHorizontal.SetMiddleBarSize(1.0/float(self.site_amount))
			self.ScrollBarHorizontal.Show()

		self.ScrollBarHorizontal.SetScrollEvent(self.__OnScrollItem)

	def __OnScrollItem(self):
		pos = int(self.ScrollBarHorizontal.GetPos() * self.site_amount+1)

		if pos>self.site_amount:
			pos = self.site_amount

		self.siteText.SetText("%d/%d" % (pos, self.site_amount))

		i = (pos-1)*9
		self.ScrollItem.SetButtonInfo(self.ItemList[i:i+9:1])


class boardItem(ui.ScriptWindow):
	def __init__(self, parent, x, y):
		ui.ScriptWindow.__init__(self)

		self.__EasyBuild = EasyBuildKilroy()
		self.wndQuestionDialog = None
		self.price = 0
		self.suffix = ""
		self.itemVnum = 0
		self.ShopId = 0


		self.board = self.__EasyBuild.CreateImage(parent, x, y, "locale/de/ui/interfaces/ingame_shops/boarditem.tga")
		self.itemName = self.__EasyBuild.CreateTextLine(self.board, 8, 3, "", "normal")
		self.boardHead = self.__EasyBuild.CreateImage(self.board, 0, -17, "locale/de/ui/interfaces/ingame_shops/boarditemhead.tga")
		self.boardHeadText = self.__EasyBuild.CreateTextLine(self.boardHead, 45, 3, "", "center")

		self.buyButton = self.__EasyBuild.CreateResizableButton(
								self.board, 69, 50, 50, 17, "Kaufen",
								self.__Accept, None,
								(0.0,0.0,0.0,1.0),
								(0.1,0.1,0.1,0.5),
								(0.0,0.0,0.0,1.0)
							)
		self.buyButton.SetUpEdgeColor(0.2, 0.2, 0.2, 1.0)

		self.buyBar = self.__EasyBuild.CreateResizableButton( #used as render
								self.board, 69, 25, 50, 17, "",
								self.__None, None,
								(0.0,0.0,0.0,1.0),
								(0.0,0.0,0.0,1.0),
								(0.0,0.0,0.0,1.0)
							)
		self.buyBar.SetUpEdgeColor(0.2, 0.2, 0.2, 1.0)
		self.Box, self.priceBar = self.__EasyBuild.CreateEditLine(self.buyBar, "1", 0, 0, 50, 17, 3)
		self.priceBar.SetParent(self.buyBar)
		self.priceBar.SetNumberMode()
		self.STK = self.__EasyBuild.CreateTextLine(self.buyBar, 50-22, 1.5, "STK.", "normal")

		self.itemBackground = self.__EasyBuild.CreateResizableButton( # used as render
								self.board, 5, 20, 60, 57, "",
								self.__None, None,
								(1.0,0.0,0.0,0.2),
								(1.0,0.0,0.0,0.2),
								(1.0,0.0,0.0,0.2)
							)
		self.itemBackground.SetUpEdgeColor(0.2,0.2,0.2,1.0)

		self.itemPrice = self.__EasyBuild.CreateTextLine(self.itemBackground, 3, 32+8, "", "normal")
		self.itemIcon = self.__EasyBuild.CreateImage(self.itemBackground, 10, 5, None, FALSE)

		del self.Box
		self.toolTip = uiToolTip.ItemToolTip()


	def OnUpdate(self):
		if self.itemIcon.IsIn():
			self.toolTip.SetItemToolTip(self.itemVnum)
		else:
			self.toolTip.HideToolTip()

	def __None(self):
		pass

	def __Accept(self):
		amount = self.priceBar.GetText()
		self.wndQuestionDialog = self.__EasyBuild.CreateQuestionDialog(
			"Willst du %sx %s für %d %s kaufen?" % (amount, self.itemName.GetText(), self.price*int(amount), self.suffix),
			lambda arg=1: self.AnswerDialog(arg, "QUESTION"),
			lambda arg=0: self.AnswerDialog(arg, "QUESTION")
		)

	def AnswerDialog(self, answer, typ):
		if not self.wndQuestionDialog:
			return

		if typ=="QUESTION" and answer==1:
			amount = self.priceBar.GetText()
			if constInfo.INGAME_SHOPS_CONFIG["MONEY"][self.ShopId][0]<self.price*int(amount):
				chat.AppendChat(1, "Du hast nicht genug %s für dieses Item!" % self.suffix)
			else:
				constInfo.INGAME_SHOPS_CONFIG["CMD"] = "buy/%d/%s/%d" % (self.itemVnum, amount, self.ShopId)
				event.QuestButtonClick(int(constInfo.INGAME_SHOPS_CONFIG["INDEX"]))

		self.wndQuestionDialog.Close()
		self.wndQuestionDialog = None

	def SetItem(self, vnum, angebot, price, suffix, rabatt, shop):
		item.SelectItem(vnum)
		itemIcon = item.GetIconImageFileName()
		itemName = item.GetItemName()

		if (angebot>=0 and rabatt>0):
			price -= int((price*(float(rabatt)/100.0))//1)
			if angebot==0:
				angebot = 'Permanent'
			else:
				angebot = self.__EasyBuild.toTimeString(angebot)
			self.SetAngebot(angebot + (" - %d%%" % rabatt))
		else:
			self.UnsetAngebot()

		self.itemIcon.LoadImage(itemIcon)
		self.itemIcon.SetScale(1, float(32.0/float(self.itemIcon.GetHeight())))
		self.itemPrice.SetText("%d %s" % (price, suffix))
		self.itemName.SetText(itemName)

		self.itemVnum = vnum
		self.price = price
		self.suffix = suffix
		self.ShopId = shop
		self.Show()

	def SetAngebot(self, angebot):
		self.boardHead.Show()
		self.boardHeadText.Show()
		self.boardHeadText.SetText(angebot)

	def UnsetAngebot(self):
		self.boardHead.Hide()
		self.boardHeadText.Hide()

	def Close(self):
		self.board.Hide()
		self.Hide()

	def Open(self):
		self.board.Show()
		self.Show()

class scrollBoard(ui.ScriptWindow):
	def __init__(self, parent, x, y):
		ui.ScriptWindow.__init__(self)
		self.board = boardItem(parent, x, y)

	def SetButtonInfo(self, ItemList):
		self.board.SetItem(*ItemList)

	def Close(self):
		self.board.Hide()

class scrollBoardItemHorizontal(ui.ScriptWindow):
	def __init__(self, parent, x, y):
		ui.ScriptWindow.__init__(self)
		self.boards = []
		for i in xrange(3):
			for s in xrange(3):
				self.boards += [ boardItem(parent, x+140*i, y+110*s) ]

	def SetButtonInfo(self, ItemList):
		for i in xrange(len(self.boards)):
			self.boards[i].Close()
		for i in xrange(len(ItemList)):
			self.boards[i].Open()
			self.boards[i].SetItem(*ItemList[i])

	def Close(self):
		for board in self.boards:
			board.Close()

class scrollButton(ui.ScriptWindow):

	def __init__(self, parent, x, y):
		ui.ScriptWindow.__init__(self)
		self.__EasyBuild = EasyBuildKilroy()
		self.Button = self.__EasyBuild.CreateResizableButton(
												parent, x, y, 110, 30, "",
												self.__OnClickButton, None,
												(0.2, 0.17, 0.15, 1.0),
												(0.2, 0.17, 0.15, 0.7),
												(0.17, 0.12, 0.10, 1.0)
											)

	def SetButtonInfo(self, text, func):
		self.Button.SetText(text)
		self.Button.SetEvent(*func)

	def __OnClickButton(self, text):
		pass

	def Close(self):
		self.Button.Hide()

class PageControl(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.pages = []

	def AddPage(self,page):
		self.pages.append(page)
		page.SetParent(self)
		self.ArrangeTitleBar()

	def RemovePage(self,page):
		self.pages.remove(page)
		self.ArrangeTitleBar()

	def SelectTab(self, selected):
		for page in self.pages:
			if page == selected:
				page.Show()
			else:
				page.Hide()

	def ArrangeTitleBar(self):
		(x, y, width, height) = self.GetRect()
		curx = 0
		for page in self.pages:
			head = page.GetHead()
			head.SetPosition(curx,0)
			curx+= head.GetWidth()

			content = page.GetContent()
			content.SetPosition(0,head.HEAD_HEIGHT)
			content.SetSize(width,height-head.HEAD_HEIGHT)
			if page.IsSelected():
				content.Show()

class PageHead(ui.Window):
	HEAD_HEIGHT = 0
	PADDING = 5
	HEAD_WIDTH = 0

	def __init__(self):
		ui.Window.__init__(self)
		self.state = 0
		self.__EasyBuild = EasyBuildKilroy()

		self.head = self.__EasyBuild.CreateResizableButton(
												self, 0, 0, 150, 40, "",
												self.OnClickTab, None,
												(0.2, 0.17, 0.15, 1.0),
												(0.2, 0.17, 0.15, 0.7),
												(0.17, 0.12, 0.10, 1.0)
											)
		self.SetSizeWindow(self.head.GetWidth(),self.head.GetHeight())

	def SetText(self,text):
		self.head.SetText(text)

	def SetPadding(self, pad):
		self.PADDING = pad
		self.SetSizeWindow(self.HEAD_WIDTH, self.HEAD_HEIGHT)

	def SetSizeWindow(self, width, height):
		self.HEAD_WIDTH = width
		self.HEAD_HEIGHT = height
		self.SetSize(width+self.PADDING, height)

	def SetUp(self):
		self.state = 0
		self.head.SetUpVisualColor(0.2, 0.17, 0.15, 1.0)
		self.head.SetOverVisualColor(0.2, 0.17, 0.15, 0.7)
		self.head.SetDownVisualColor(0.17, 0.12, 0.10, 1.0)

	def SetDown(self):
		self.state = 1

	def SetPage(self, page):
		self.page = page

	def OnClickTab(self):
		self.page.ToggleDown()

	def OnUpdate(self):
		if self.state==1:
			self.head.SetUpVisualColor(0.17, 0.12, 0.10, 1.0)
			self.head.SetOverVisualColor(0.17, 0.12, 0.10, 1.0)
			self.head.SetDownVisualColor(0.17, 0.12, 0.10, 1.0)


class Page:
	def __init__(self, obj, title="NONAME"):
		self.SetContent(obj)
		self.SetHead(PageHead())
		self.SetTitle(title)
		self.head.Show()

		self.isSelected = 0

	def Show(self):
		self.content.Show()
		self.head.SetDown()
		self.isSelected = 1

	def Hide(self):
		self.content.Hide()
		self.head.SetUp()
		self.isSelected = 0

	def IsSelected(self):
		return self.isSelected

	def ToggleDown(self):
		self.parent.SelectTab(self)

	def SetParent(self,par):
		self.content.SetParentProxy(par)
		self.head.SetParentProxy(par)
		self.parent = par

	def SetPadding(self, pad):
		self.head.SetPadding(pad)

	def SetContent(self,cont):
		self.content = cont

	def GetContent(self):
		return self.content

	def SetHead(self,head):
		self.head = head
		head.SetPage(self)

	def GetHead(self):
		return self.head

	def SetTitle(self,title):
		self.title = title
		self.head.SetText(title)


class ResizableButton(ui.Window):

	VISUAL_COLOR = grp.GenerateColor(0.2, 0.2, 0.2, 1.0) #default
	EDGE_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 1.0) #default

	OVER_VISUAL_COLOR = grp.GenerateColor(1.0, 1.0, 1.0, 0.1) # default
	DOWN_VISUAL_COLOR = grp.GenerateColor(0.1, 0.1, 0.1, 1.0) # default

	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.eventFunc = None
		self.eventArgs = None

		self.ButtonText = None
		self.ToolTipText = None

		self.isOver = FALSE
		self.isSelected = FALSE
		self.isClicked = FALSE

		self.width = 0
		self.height = 0

	def __del__(self):
		ui.Window.__del__(self)

		self.eventFunc = None
		self.eventArgs = None

	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def SetUpVisualColor(self, r, g, b, l):
		self.VISUAL_COLOR = grp.GenerateColor(r, g, b, l)

	def SetUpEdgeColor(self, r, g, b, l):
		self.EDGE_COLOR = grp.GenerateColor(r, g, b, l)

	def SetOverVisualColor(self, r, g, b, l):
		self.OVER_VISUAL_COLOR = grp.GenerateColor(r, g, b, l)

	def SetDownVisualColor(self, r, g, b, l):
		self.DOWN_VISUAL_COLOR = grp.GenerateColor(r, g, b, l)

	def SetEvent(self, func, *args):
		self.eventFunc = func
		self.eventArgs = args

	def SetTextColor(self, color):
		if not self.ButtonText:
			return
		self.ButtonText.SetPackedFontColor(color)

	def SetText(self, text):
		if not self.ButtonText:
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetPosition(self.GetWidth()/2, self.GetHeight()/2)
			textLine.SetVerticalAlignCenter()
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.ButtonText = textLine

		self.ButtonText.SetText(text)

	def SetToolTipText(self, text, x=0, y = -19):
		if not self.ToolTipText:
			toolTip=ui.createToolTipWindowDict["TEXT"]()
			toolTip.SetParent(self)
			toolTip.SetSize(0, 0)
			toolTip.SetHorizontalAlignCenter()
			toolTip.SetOutline()
			toolTip.Hide()
			toolTip.SetPosition(x + self.GetWidth()/2, y)
			self.ToolTipText=toolTip

		self.ToolTipText.SetText(text)

	def ShowToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Show()

	def HideToolTip(self):
		if self.ToolTipText:
			self.ToolTipText.Hide()

	def OnMouseLeftButtonDown(self):
		self.isSelected = TRUE
		self.isClicked = TRUE

	def OnMouseLeftButtonUp(self):
		self.isSelected = FALSE
		if self.eventFunc and self.IsIn() and self.isClicked:
			apply(self.eventFunc, self.eventArgs)

	def OnUpdate(self):
		if self.IsIn():
			self.isOver = TRUE
			self.ShowToolTip()
		else:
			self.isClicked = FALSE
			self.isOver = FALSE
			self.HideToolTip()

	def OnRender(self):
		xRender, yRender = self.GetGlobalPosition()

		widthRender = self.width
		heightRender = self.height
		if self.isOver:
			if self.isSelected:
				grp.SetColor(self.DOWN_VISUAL_COLOR)
				grp.RenderBar(xRender, yRender, self.width, heightRender)
			else:
				grp.SetColor(self.OVER_VISUAL_COLOR)
				grp.RenderBar(xRender, yRender, self.width, heightRender)
		else:
			grp.SetColor(self.VISUAL_COLOR)
			grp.RenderBar(xRender, yRender, widthRender, heightRender)
		grp.SetColor(self.EDGE_COLOR)
		grp.RenderLine(xRender, yRender, widthRender, 0)
		grp.RenderLine(xRender, yRender, 0, heightRender)
		grp.RenderLine(xRender, yRender+heightRender, widthRender, 0)
		grp.RenderLine(xRender+widthRender, yRender, 0, heightRender)

class VerticalScrollBar(ui.Window):

	SCROLLBAR_WIDTH = 17
	SCROLLBAR_MIDDLE_HEIGHT = 9
	SCROLLBAR_BUTTON_WIDTH = 17
	SCROLLBAR_BUTTON_HEIGHT = 17
	MIDDLE_BAR_POS = 5
	MIDDLE_BAR_UPPER_PLACE = 3
	MIDDLE_BAR_DOWNER_PLACE = 4
	TEMP_SPACE = MIDDLE_BAR_UPPER_PLACE + MIDDLE_BAR_DOWNER_PLACE

	class MiddleBar(ui.DragButton):
		def __init__(self):
			ui.DragButton.__init__(self)
			self.AddFlag("movable")
			#self.AddFlag("restrict_x")

		def MakeImage(self):
			top = ui.ImageBox()
			top.SetParent(self)
			top.LoadImage("locale/de/ui/interfaces/ingame_shops/vscrollbar_top.tga")
			top.SetPosition(0, 0)
			top.AddFlag("not_pick")
			top.Show()
			bottom = ui.ImageBox()
			bottom.SetParent(self)
			bottom.LoadImage("locale/de/ui/interfaces/ingame_shops/vscrollbar_bottom.tga")
			bottom.AddFlag("not_pick")
			bottom.Show()

			middle = ui.ExpandedImageBox()
			middle.SetParent(self)
			middle.LoadImage("locale/de/ui/interfaces/ingame_shops/vscrollbar_middle.tga")
			middle.SetPosition(0, 4)
			middle.AddFlag("not_pick")
			middle.Show()

			self.top = top
			self.bottom = bottom
			self.middle = middle

		def SetSize(self, height):
			height = max(12, height)
			ui.DragButton.SetSize(self, 10, height)
			self.bottom.SetPosition(0, height-4)

			height -= 4*3
			self.middle.SetRenderingRect(0, 0, 0, float(height)/4.0)

	def __init__(self):
		ui.Window.__init__(self)

		self.pageSize = 1
		self.curPos = 0.0
		self.eventScroll = lambda *arg: None
		self.lockFlag = FALSE
		self.scrollStep = 0.20


		self.CreateScrollBar()

	def __del__(self):
		ui.Window.__del__(self)

	def CreateScrollBar(self):
		barSlot = ui.Bar3D()
		barSlot.SetParent(self)
		barSlot.AddFlag("not_pick")
		barSlot.Show()

		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(ui.__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.MakeImage()
		middleBar.SetSize(12)

		upButton = ui.Button()
		upButton.SetParent(self)
		upButton.SetEvent(ui.__mem_func__(self.OnUp))
		upButton.SetUpVisual("locale/de/ui/interfaces/ingame_shops/vscrollbar_up_button_01.tga")
		upButton.SetOverVisual("locale/de/ui/interfaces/ingame_shops/vscrollbar_up_button_02.tga")
		upButton.SetDownVisual("locale/de/ui/interfaces/ingame_shops/vscrollbar_up_button_03.tga")
		upButton.Show()

		downButton = ui.Button()
		downButton.SetParent(self)
		downButton.SetEvent(ui.__mem_func__(self.OnDown))
		downButton.SetUpVisual("locale/de/ui/interfaces/ingame_shops/vscrollbar_down_button_01.tga")
		downButton.SetOverVisual("locale/de/ui/interfaces/ingame_shops/vscrollbar_down_button_02.tga")
		downButton.SetDownVisual("locale/de/ui/interfaces/ingame_shops/vscrollbar_down_button_03.tga")
		downButton.Show()

		self.upButton = upButton
		self.downButton = downButton
		self.middleBar = middleBar
		self.barSlot = barSlot

		self.SCROLLBAR_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_MIDDLE_HEIGHT = self.middleBar.GetHeight()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight()

	def Destroy(self):
		self.middleBar = None
		self.upButton = None
		self.downButton = None
		self.eventScroll = lambda *arg: None

	def SetScrollEvent(self, event):
		self.eventScroll = event

	def SetMiddleBarSize(self, pageScale):
		realHeight = self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2
		self.SCROLLBAR_MIDDLE_HEIGHT = int(pageScale * float(realHeight))
		self.middleBar.SetSize(self.SCROLLBAR_MIDDLE_HEIGHT)
		self.pageSize = (self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)

	def SetScrollBarSize(self, height):
		self.pageSize = (height - self.SCROLLBAR_BUTTON_HEIGHT*2) - self.SCROLLBAR_MIDDLE_HEIGHT - (self.TEMP_SPACE)
		self.SetSize(self.SCROLLBAR_WIDTH, height)
		self.upButton.SetPosition(0, 0)
		self.downButton.SetPosition(0, height - self.SCROLLBAR_BUTTON_HEIGHT)
		self.middleBar.SetRestrictMovementArea(self.MIDDLE_BAR_POS, self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE, self.MIDDLE_BAR_POS+2, height - self.SCROLLBAR_BUTTON_HEIGHT*2 - self.TEMP_SPACE)
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, 0)

		self.UpdateBarSlot()

	def UpdateBarSlot(self):
		self.barSlot.SetPosition(0, self.SCROLLBAR_BUTTON_HEIGHT)
		self.barSlot.SetSize(self.GetWidth() - 2, self.GetHeight() - self.SCROLLBAR_BUTTON_HEIGHT*2 - 2)

	def GetPos(self):
		return self.curPos

	def SetPos(self, pos):
		pos = max(0.0, pos)
		pos = min(1.0, pos)

		newPos = float(self.pageSize) * pos
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, int(newPos) + self.SCROLLBAR_BUTTON_HEIGHT + self.MIDDLE_BAR_UPPER_PLACE)
		self.OnMove()

	def SetScrollStep(self, step):
		self.scrollStep = step
	
	def GetScrollStep(self):
		return self.scrollStep
		
	def OnUp(self):
		self.SetPos(self.curPos-self.scrollStep)

	def OnDown(self):
		self.SetPos(self.curPos+self.scrollStep)

	def OnMove(self):

		if self.lockFlag:
			return

		if 0 == self.pageSize:
			return

		(xLocal, yLocal) = self.middleBar.GetLocalPosition()
		self.curPos = float(yLocal - self.SCROLLBAR_BUTTON_HEIGHT - self.MIDDLE_BAR_UPPER_PLACE) / float(self.pageSize)
		self.eventScroll()

	def OnMouseLeftButtonDown(self):
		(xMouseLocalPosition, yMouseLocalPosition) = self.GetMouseLocalPosition()
		pickedPos = yMouseLocalPosition - self.SCROLLBAR_BUTTON_HEIGHT - self.SCROLLBAR_MIDDLE_HEIGHT/2
		newPos = float(pickedPos) / float(self.pageSize)
		self.SetPos(newPos)

	def LockScroll(self):
		self.lockFlag = TRUE

	def UnlockScroll(self):
		self.lockFlag = FALSE


class HorizontalScrollBar(VerticalScrollBar):

	SCROLLBAR_WIDTH = 17
	SCROLLBAR_MIDDLE_WIDTH = 9
	SCROLLBAR_BUTTON_WIDTH = 17
	SCROLLBAR_BUTTON_HEIGHT = 17
	MIDDLE_BAR_POS = 5
	MIDDLE_BAR_UPPER_PLACE = 3
	MIDDLE_BAR_DOWNER_PLACE = 4
	TEMP_SPACE = MIDDLE_BAR_UPPER_PLACE + MIDDLE_BAR_DOWNER_PLACE

	class MiddleBar(ui.DragButton):
		def __init__(self):
			ui.DragButton.__init__(self)
			self.AddFlag("movable")
			#self.AddFlag("restrict_x")

		def MakeImage(self):
			top = ui.ImageBox()
			top.SetParent(self)
			top.LoadImage("locale/de/ui/interfaces/ingame_shops/hscrollbar_top.tga")
			top.SetPosition(0, 0)
			top.AddFlag("not_pick")
			top.Show()
			bottom = ui.ImageBox()
			bottom.SetParent(self)
			bottom.LoadImage("locale/de/ui/interfaces/ingame_shops/hscrollbar_bottom.tga")
			bottom.AddFlag("not_pick")
			bottom.Show()

			middle = ui.ExpandedImageBox()
			middle.SetParent(self)
			middle.LoadImage("locale/de/ui/interfaces/ingame_shops/hscrollbar_middle.tga")
			middle.SetPosition(4, 0)
			middle.AddFlag("not_pick")
			middle.Show()

			self.top = top
			self.bottom = bottom
			self.middle = middle

		def SetSize(self, width):
			width = max(12, width)
			ui.DragButton.SetSize(self, width, 10)
			self.bottom.SetPosition(width-4,0)

			width -= 4*3
			self.middle.SetRenderingRect(0, 0, float(width)/4.0, 0)

	def CreateScrollBar(self):
		barSlot = ui.Bar3D()
		barSlot.SetParent(self)
		barSlot.AddFlag("not_pick")
		barSlot.Show()

		middleBar = self.MiddleBar()
		middleBar.SetParent(self)
		middleBar.SetMoveEvent(ui.__mem_func__(self.OnMove))
		middleBar.Show()
		middleBar.MakeImage()
		middleBar.SetSize(12)

		upButton = ui.Button()
		upButton.SetParent(self)
		upButton.SetEvent(ui.__mem_func__(self.OnUp))
		upButton.SetUpVisual("locale/de/ui/interfaces/ingame_shops/hscrollbar_left_button_01.tga")
		upButton.SetOverVisual("locale/de/ui/interfaces/ingame_shops/hscrollbar_left_button_02.tga")
		upButton.SetDownVisual("locale/de/ui/interfaces/ingame_shops/hscrollbar_left_button_03.tga")
		upButton.Show()

		downButton = ui.Button()
		downButton.SetParent(self)
		downButton.SetEvent(ui.__mem_func__(self.OnDown))
		downButton.SetUpVisual("locale/de/ui/interfaces/ingame_shops/hscrollbar_right_button_01.tga")
		downButton.SetOverVisual("locale/de/ui/interfaces/ingame_shops/hscrollbar_right_button_02.tga")
		downButton.SetDownVisual("locale/de/ui/interfaces/ingame_shops/hscrollbar_right_button_03.tga")
		downButton.Show()

		self.upButton = upButton
		self.downButton = downButton
		self.middleBar = middleBar
		self.barSlot = barSlot

		self.SCROLLBAR_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_MIDDLE_WIDTH = self.middleBar.GetWidth()
		self.SCROLLBAR_BUTTON_WIDTH = self.upButton.GetWidth()
		self.SCROLLBAR_BUTTON_HEIGHT = self.upButton.GetHeight()

	def SetMiddleBarSize(self, pageScale):
		realHeight = self.GetWidth() - self.SCROLLBAR_BUTTON_WIDTH*2
		self.SCROLLBAR_MIDDLE_WIDTH = int(pageScale * float(realHeight))
		self.middleBar.SetSize(self.SCROLLBAR_MIDDLE_WIDTH)
		self.pageSize = (self.GetWidth() - self.SCROLLBAR_BUTTON_WIDTH*2) - self.SCROLLBAR_MIDDLE_WIDTH - (self.TEMP_SPACE)

	def SetScrollBarSize(self, width):
		self.pageSize = (width - self.SCROLLBAR_BUTTON_WIDTH*2) - self.SCROLLBAR_MIDDLE_WIDTH - (self.TEMP_SPACE)
		self.SetSize(width, self.SCROLLBAR_WIDTH)
		self.upButton.SetPosition(-1, 0)
		self.downButton.SetPosition(width - self.SCROLLBAR_BUTTON_WIDTH, 0)
		self.middleBar.SetRestrictMovementArea(self.SCROLLBAR_BUTTON_WIDTH + self.MIDDLE_BAR_UPPER_PLACE, self.MIDDLE_BAR_POS, width - self.SCROLLBAR_BUTTON_WIDTH*2 - self.TEMP_SPACE, self.MIDDLE_BAR_POS+2)
		self.middleBar.SetPosition(self.MIDDLE_BAR_POS, 0)

		self.UpdateBarSlot()

	def UpdateBarSlot(self):
		self.barSlot.SetPosition(self.SCROLLBAR_BUTTON_WIDTH,0)
		self.barSlot.SetSize(self.GetWidth() - 2 - self.SCROLLBAR_BUTTON_WIDTH*2, self.GetHeight() - 2)

	def SetPos(self, pos):
		pos = max(0.0, pos)
		pos = min(1.0, pos)

		newPos = float(self.pageSize) * pos
		self.middleBar.SetPosition(int(newPos) + self.SCROLLBAR_BUTTON_WIDTH + self.MIDDLE_BAR_UPPER_PLACE, self.MIDDLE_BAR_POS)
		self.OnMove()

	def OnMove(self):

		if self.lockFlag:
			return

		if 0 == self.pageSize:
			return

		(xLocal, yLocal) = self.middleBar.GetLocalPosition()
		self.curPos = float(xLocal - self.SCROLLBAR_BUTTON_WIDTH - self.MIDDLE_BAR_UPPER_PLACE) / float(self.pageSize)
		self.eventScroll()

	def OnMouseLeftButtonDown(self):
		(xMouseLocalPosition, yMouseLocalPosition) = self.GetMouseLocalPosition()
		pickedPos = xMouseLocalPosition - self.SCROLLBAR_BUTTON_WIDTH - self.SCROLLBAR_MIDDLE_WIDTH/2
		newPos = float(pickedPos) / float(self.pageSize)
		self.SetPos(newPos)

class ImageSlideShow(ui.Window):
	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.width = 0
		self.height = 0
		self.imageList = []
		self.buttonList = []
		self.Selected = -1
		self.old_time = app.GetTime()
		self.delay = 10.0

		image = ui.ImageBox()
		image.SetParent(self)
		image.SetPosition(0,0)
		image.Hide()
		self.Image = image

	def __del__(self):
		ui.Window.__del__(self)

	def RemoveImage(self, i):
		del self.imageList[i]
		self.ArrangeButtons()

	def AddImage(self, path):
		self.imageList.append(path)
		self.ArrangeButtons()

	def ArrangeButtons(self):
		self.buttonList = []
		self.Image.Hide()
		for i in xrange(len(self.imageList)):
			self.Image.LoadImage(self.imageList[i])
			self.HandlePictureWidthHeight(self.Image)

		for i in xrange(len(self.imageList)):
			button = ui.Button()
			button.SetParent(self)
			button.SetPosition(self.width-(20+i*20), self.height-20)
			button.SetUpVisual("locale/de/ui/interfaces/ingame_shops/imageshow_button_01.tga")
			button.SetOverVisual("locale/de/ui/interfaces/ingame_shops/imageshow_button_02.tga")
			button.SetDownVisual("locale/de/ui/interfaces/ingame_shops/imageshow_button_03.tga")
			button.SetEvent(ui.__mem_func__(self.__OnClick), i)
			button.Show()
			self.buttonList.append(button)

		self.Image.LoadImage(self.imageList[0])
		self.Selected = 0
		self.Image.Show()

	def __OnClick(self, arg):
		self.buttonList[self.Selected].SetUp()
		self.Selected = arg
		self.Image.LoadImage(self.imageList[arg])

	def SetDelay(self, d):
		self.delay = float(d)

	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def HandlePictureWidthHeight(self, obj):
			(width, height) = obj.GetWidth(), obj.GetHeight()

			if self.width<width and self.height>height:
				self.SetSize(width, self.height)
			elif self.width>width and self.height<height:
				self.SetSize(self.width, height)
			elif self.width<width and self.height<height:
				self.SetSize(width, height)

	def OnUpdate(self):
		if self.Selected!=-1:
			self.buttonList[self.Selected].Down()

		if (self.old_time+self.delay) < app.GetTime():
			self.buttonList[self.Selected].SetUp()

			self.old_time = app.GetTime()
			self.Selected +=1

			if self.Selected>len(self.imageList)-1:
				self.Selected = 0

			self.Image.LoadImage(self.imageList[self.Selected])

class EasyBuildKilroy():

	def NumberToMoneyString(self, money):
		sourceText = str(money)
		if len(sourceText) <= 3:
			return sourceText
		return self.NumberToMoneyString(sourceText[:-3]) + "." + sourceText[-3:]

	def toTimeString(self, seconds):
		if type(seconds) is not int or seconds<1:
			return '0s'

		timeTuple = (
			("h", 3600, ""),
			("m", 60, "")
			)

		result, timeString = [], ""

		for timeName, timeSeconds, plural in timeTuple:
			timeValue = (seconds // timeSeconds) # // is floor division
			if timeValue: # if not 0 (false)
				seconds -= (timeValue * timeSeconds)
				if timeValue != 1:
					timeName += plural
				result += [ "%d %s" % (timeValue, timeName) ]

		valueCount = len(result)
		for i in xrange(valueCount):
			leftValues = valueCount - i - 1
			timeString += result[i] + {0: "", 1: " "}.get(leftValues, " ")

		return timeString

	def CreateBoardWithTitle(self, x, y, width, height):
		board = ui.BoardWithTitleBar()
		board.SetSize(width, height)
		board.SetPosition(x, y)
		board.AddFlag("movable")
		board.Show()
		return board

	def CreateSlotBar(self, parent, x, y, width, heigh):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		return SlotBar

	def CreateResizableButton(self, parent, x, y, width, height, text, func, f_event=None, up=(0.2, 0.2, 0.2, 1.0), over=(1.0, 1.0, 1.0, 0.1), down=(0.1, 0.1, 0.1, 1.0)):
		button = ResizableButton()
		button.SetParent(parent)
		button.SetEvent(func)
		if f_event!=None:
			button.SetEvent(ui.__mem_func__(func), f_event)

		button.SetPosition(x, y)
		button.SetUpVisualColor(*up)
		button.SetOverVisualColor(*over)
		button.SetDownVisualColor(*down)
		button.SetSize(width, height) ##Resizes button
		button.SetText(text)
		button.Show()
		return button

	def CreateImage(self, parent, x, y, path=None, not_pick=TRUE):
		image = ui.ExpandedImageBox()
		image.SetParent(parent)
		if not_pick:
			image.AddFlag("not_pick")
		image.SetPosition(x,y)
		if path!=None:
			image.LoadImage(path)
		image.Show()
		return image

	def CreateTextLine(self, parent, x, y, text, align="center"):
		textline = ui.TextLine()
		textline.SetParent(parent)
		textline.SetPosition(x,y)
		textline.SetText(text)
		if align=="center":
			textline.SetHorizontalAlignCenter()
		textline.Show()
		return textline

	def CreateScrollbar(self, parent, height, x, y):
		scrollbar = VerticalScrollBar()
		scrollbar.SetParent(parent)
		scrollbar.SetScrollBarSize(height)
		scrollbar.SetPosition(x, y)
		scrollbar.Show()
		return scrollbar

	def CreateHorizontalScrollbar(self, parent, width, x, y):
		scrollbar = HorizontalScrollBar()
		scrollbar.SetParent(parent)
		scrollbar.SetScrollBarSize(width)
		scrollbar.SetPosition(x, y)
		scrollbar.Show()
		return scrollbar

	def CreateEditLine(self, parent, text, x, y, width, heigh, max):
		SlotBar = self.CreateSlotBar(parent,x,y,width,heigh)
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(3, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(text)
		Value.Show()
		return SlotBar, Value

	def CreateQuestionDialog(self, text, yes_func, no_func):
		wndQuestionDialog = uiCommon.QuestionDialog()
		wndQuestionDialog.SetText(text)
		wndQuestionDialog.SetAcceptEvent(yes_func)
		wndQuestionDialog.SetCancelEvent(no_func)
		wndQuestionDialog.Open()
		return wndQuestionDialog

