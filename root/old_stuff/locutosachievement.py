import wndMgr,ui,grp,event,chat,app,localeInfo,constInfo,nonplayer,settinginfo
# Developed by Locutos, 2017 @ Kimiko
class AchievementWindow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self,"TOP_MOST")
		self.SetSize(300, 40)
		self.SetPosition(wndMgr.GetScreenWidth()/2-150+60,wndMgr.GetScreenHeight()+150)
		self.Hide()
		self.Loaded = 0
		self.isLoaded = 0
		self.pos_height = 0
		self.delay = 0	
		self.index = 0
		self.initData()
		
	def initData(self):
		if self.Loaded > 0:
			self.Show()
			return
		
		self.Loaded = 1
		
		self.MainBGThinBoard = ui.Board()
		self.MainBGThinBoard.SetParent(self)
		self.MainBGThinBoard.SetPosition(0,0)
		self.MainBGThinBoard.SetSize(300, 40)
		self.MainBGThinBoard.Show()
		
		self.faceBoxIMG = ui.ImageBox()
		self.faceBoxIMG.SetParent(self.MainBGThinBoard)
		self.faceBoxIMG.SetPosition(5,7)
		self.faceBoxIMG.Show()	

		self.AchievementTitle = ui.TextLine()
		self.AchievementTitle.SetParent(self.MainBGThinBoard)
		self.AchievementTitle.SetPosition(170,8)
		self.AchievementTitle.SetHorizontalAlignCenter()
		self.AchievementTitle.SetFontColor(0.9607, 0.2392, 0.0)
		self.AchievementTitle.Show()
		
		self.AchievementText = ui.TextLine()
		self.AchievementText.SetParent(self.MainBGThinBoard)
		self.AchievementText.SetPosition(170,25)
		self.AchievementText.SetHorizontalAlignCenter()
		self.AchievementText.Show()		
		
		self.AchievementPointsText = ui.TextLine()
		self.AchievementPointsText.SetParent(self.MainBGThinBoard)
		self.AchievementPointsText.SetPosition(100,40)
		self.AchievementPointsText.SetText("Deine Punkte steigen auf")
		self.AchievementPointsText.Show()			
		
		self.AchievementPointsTextPoints = ui.TextLine()
		self.AchievementPointsTextPoints.SetParent(self.MainBGThinBoard)
		self.AchievementPointsTextPoints.SetPosition(216,40)
		self.AchievementPointsTextPoints.SetFontColor(1.0, 0.7843, 0.0)	
		self.AchievementPointsTextPoints.Show()	
		
		self.Hide()
		
	def Open(self):
		if self.IsShow():
			self.Hide()
			return
		self.initData()
		
	def SendAchievement(self,index,points,count,ap):
		if self.isLoaded == 0:
			self.AchievementTitle.SetText(str(self.GetAchievementName(int(index))) + " " + str(self.GetAchievementTypeByIndex(int(index))))
			self.AchievementText.SetText("Anzahl: " + constInfo.NumberToPointString(count) + "  |  Punkte erhalten: " + constInfo.NumberToPointString(points) + "")
			self.AchievementPointsTextPoints.SetText(constInfo.NumberToPointString(ap) + " AP!")

			try:
				self.faceBoxIMG.LoadImage("images_achievement/" + str(index) + ".tga")
			except:
				print "Achievement - %s No Face IMG in images_achievement/" % (index)
				self.faceBoxIMG.Hide()		

			self.Show()
			self.pos_height = wndMgr.GetScreenHeight() + 50
			self.SetPosition(wndMgr.GetScreenWidth() /2 - 150+60,wndMgr.GetScreenHeight()+50)
			self.isLoaded = 1
			self.index = int(index)
			
		if self.isLoaded == 2:
			self.AchievementPointsTextPoints.SetText(constInfo.NumberToPointString(ap) + " AP!")
			if self.index == int(index):
				self.AchievementText.SetText("Anzahl: " + constInfo.NumberToPointString(count) + "  |  Punkte erhalten: " + constInfo.NumberToPointString(points) + "")
				if self.delay > app.GetTime():
					HideTimeOut = self.delay - app.GetTime()
					if HideTimeOut < 5:
						self.delay = app.GetTime() + 5

		chat.AppendChat(chat.CHAT_TYPE_INFO,"[ "+ self.GetAchievementName(int(index)) + " " + self.GetAchievementTypeByIndex(int(index)) + ". Anzahl " + constInfo.NumberToPointString(count) + ", Punkte " + constInfo.NumberToPointString(points) + " (Achievement-Points steigen auf " + constInfo.NumberToPointString(ap) +" ]")
	
	def GetAchievementName(self,index):
		if index in settinginfo.Achievement_Names:
			return settinginfo.Achievement_Names[index]
		else:
			return str(index)

	def GetAchievementTypeByIndex(self,index):
		if index < 8000:
			return "besiegt"
		elif index >= 8000 and index < 9000:
			return "zerstört"
		elif index >= 10000 and index < 10100:
			return "abgeschlossen"
		else:
			return "besiegt"
	
	def OnUpdate(self):
		if self.isLoaded == 1:
			targetLocation = wndMgr.GetScreenHeight() - 150
			
			if self.pos_height > targetLocation:
				self.pos_height = self.pos_height - 5
				self.SetPosition(wndMgr.GetScreenWidth() /2 - 150+60,self.pos_height)
			else:
				if self.isLoaded == 1:
					self.isLoaded = 2
					self.delay = app.GetTime() + 5
					
		if self.isLoaded == 2 and self.delay < app.GetTime():
			targetLocation = wndMgr.GetScreenWidth() + 50
			if self.pos_height < targetLocation:
				self.pos_height = self.pos_height + 25
				self.SetPosition(wndMgr.GetScreenWidth() /2 - 150+60,self.pos_height)
			else:
				if self.isLoaded == 2:
					self.isLoaded = 0	
					self.index = 0
					self.Hide()
		
	def Destroy(self):
		self.Loaded = 0
		self.isLoaded = 0
		self.pos_height = 0
		self.delay = 0	
		self.index = 0
		self.Hide()
		self.__del__()
	
	def __del__(self):
		ui.Window.__del__(self)
