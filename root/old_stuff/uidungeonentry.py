import wndMgr,ui,grp,event

class EntranceWindow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self,"TOP_MOST")
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetPosition(0,0)
		self.Hide()
		self.Loaded = 0
		
	def initData(self):
		if self.Loaded > 0:
			self.Show()
			return
		
		self.Loaded = 1
		
		self.Background = ui.Bar()
		self.Background.SetParent(self)
		self.Background.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.Background.SetPosition(0,0)
		self.Background.SetColor(grp.GenerateColor(0.0,0.0,0.0,150.0/255.0))
		self.Background.Show()
		
		self.HeadIMGThinBoard = ui.ThinBoard()
		self.HeadIMGThinBoard.SetParent(self)
		self.HeadIMGThinBoard.SetPosition((wndMgr.GetScreenWidth()/2) - 150,(wndMgr.GetScreenHeight()/2) - 180)
		self.HeadIMGThinBoard.SetSize(300,80)
		self.HeadIMGThinBoard.Show()
		
		
		self.CloseButton = ui.Button()
		self.CloseButton.SetParent(self)
		self.CloseButton.SetPosition((wndMgr.GetScreenWidth()/2) + 104,(wndMgr.GetScreenHeight()/2) - 200)
		self.CloseButton.SetText("")
		self.CloseButton.SetUpVisual("images_dungeon\src_illumina\close_button_01.tga")  
		self.CloseButton.SetOverVisual("images_dungeon\src_illumina\close_button_02.tga")  
		self.CloseButton.SetDownVisual("images_dungeon\src_illumina\close_button_03.tga")	
		self.CloseButton.SetEvent(self.Open)
		self.CloseButton.Show()		
		
		
		
		self.StoryTextThinBoard = ui.ThinBoard()
		self.StoryTextThinBoard.SetParent(self)
		self.StoryTextThinBoard.SetPosition((wndMgr.GetScreenWidth()/2) - 150,(wndMgr.GetScreenHeight()/2) - 95)
		self.StoryTextThinBoard.SetSize(300,400)
		self.StoryTextThinBoard.Show()
		
		self.HeadLineCenterImage = ui.ImageBox()
		self.HeadLineCenterImage.SetParent(self.StoryTextThinBoard)
		self.HeadLineCenterImage.SetPosition(150-104,18)
		self.HeadLineCenterImage.LoadImage("images_dungeon\src_illumina\center.tga")
		self.HeadLineCenterImage.Show()
		
		self.DungeonNameTextLine = ui.TextLine()
		self.DungeonNameTextLine.SetParent(self.StoryTextThinBoard)
		self.DungeonNameTextLine.SetPosition(150,15)
		self.DungeonNameTextLine.SetHorizontalAlignCenter()
		self.DungeonNameTextLine.SetText("Dungeon-Name")
		self.DungeonNameTextLine.Show()


				
		i = 0
		x = 8
		
		
		self.Show()
		
	def Open(self):
		if self.IsShow():
			self.Hide()
			return
		self.initData()
		
	def Destroy(self):
		self.Hide()
		self.__del__()
	
	def __del__(self):
		ui.Window.__del__(self)

	def OnPressEscapeKey(self):
		self.Open()
		return TRUE

	def OnPressExitKey(self):		
		self.Open()
		return TRUE	
		