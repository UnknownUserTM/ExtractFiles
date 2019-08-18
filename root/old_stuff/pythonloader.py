import app,os,ui,dbg
isShow = 0 
class Loader(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(465, 298)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('PythonLoader by Noa')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		self.comp = Component()
		self.run = self.comp.Button(self.Board, 'Run', '', 17, 260, self.run_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.close = self.comp.Button(self.Board, 'CloseMetin', '', 362, 260, self.close_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.fresh = self.comp.Button(self.Board, 'Refresh', '', 262, 260, self.refresh_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.bar_liste, self.list_liste = self.comp.ListBoxEx(self.Board, 6, 30, 451, 223)
		self.log = self.comp.TextLine(self.Board, 'Log', 115, 264, self.comp.RGB(255, 255, 255))
	def run_func(self):
		self.ItemIndex = self.list_liste.GetSelectedItem()
		if self.ItemIndex:
			self.log.SetText("run "+str(self.ItemIndex.GetText()))
			execfile(self.ItemIndex.GetText(),{})
		else:
			self.log.SetText('No Item Selected')
	def refresh_func(self):
		if not os.path.exists("uiskripts"):
			os.makedirs("uiskripts")
			
		self.list_liste.RemoveAllItems()
		for files in os.listdir("uiskripts"):
			self.list_liste.AppendItem(Item("uiskripts/"+files))	
			
	def close_func(self):
		app.Exit()
	def Close(self):
		global isShow 
		isShow = 0
		self.Board.Hide()

class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)
	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin


	def ListBoxEx(self, parent, x, y, width, heigh):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

class Item(ui.ListBoxEx.Item):
	def __init__(self, text):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=text
		self.textLine=self.__CreateTextLine(text[:50])
	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)
	def GetText(self):
		return self.text
	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 7*len(self.textLine.GetText()) + 4, height)
	def __CreateTextLine(self, text):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(text)
		textLine.Show()
		return textLine
class Starter(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.Board = ui.ThinBoard()
		self.Board.SetSize(100, 26)
		self.Board.SetPosition(925, 418)
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.Show()
		self.x = 0
		self.y = 0
		self.comp = Component()
		self.start = self.comp.Button(self.Board, 'PyLoader', '', 6, 5, self.start_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
#	def OnUpdate(self):
#		(self.x,self.y)= self.start.GetLocalPosition()
#		self.start.SetText(str(self.x)+"-"+str(self.y))
	def start_func(self):
		global isShow 
		if isShow==0:
			isShow = 1
			Loader().Show()
Starter().Show()