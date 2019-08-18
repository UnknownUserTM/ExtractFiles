import wndMgr,ui,grp,event,chat,app,localeInfo,constInfo,nonplayer,settinginfo

class AchievementWindow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self,"TOP_MOST")
		self.SetSize(336, 100)
		self.SetPosition(wndMgr.GetScreenWidth() +50,wndMgr.GetScreenHeight()-150)
		self.Hide()
		self.Loaded = 0
		self.isLoaded = 0
		self.pos_width = 0
		self.delay = 0	
		self.initData()
		
	def initData(self):
		if self.Loaded > 0:
			self.Show()
			return
		
		self.Loaded = 1
		
		self.MainBGThinBoard = ui.ThinBoard()
		self.MainBGThinBoard.SetParent(self)
		self.MainBGThinBoard.SetPosition(0,0)
		self.MainBGThinBoard.SetSize(336, 100)
		self.MainBGThinBoard.Show()
		
		self.AchievementIconIMG = ui.ImageBox()
		self.AchievementIconIMG.SetParent(self.MainBGThinBoard)
		self.AchievementIconIMG.SetPosition(20,20)
		self.AchievementIconIMG.LoadImage("d:/ymir work/ui/public/achievement_small.sub")
		self.AchievementIconIMG.Show()	
		
		self.AchievementTitle = ui.TextLine()
		self.AchievementTitle.SetParent(self.MainBGThinBoard)
		self.AchievementTitle.SetPosition((336/2)+30,8)
		self.AchievementTitle.SetHorizontalAlignCenter()
		self.AchievementTitle.SetText(localeInfo.ACHIEVEMENT_TITLE)
		#self.AchievementTitle.SetFontName(localeInfo.UI_DEF_FONT_LARGE)
		self.AchievementTitle.SetPackedFontColor(0xfff8d090)
		self.AchievementTitle.SetOutline()		
		self.AchievementTitle.Show()
		
		self.AchievementActivityInfo = ui.TextLine()
		self.AchievementActivityInfo.SetParent(self.MainBGThinBoard)
		self.AchievementActivityInfo.SetPosition((336/2)+30,25)
		self.AchievementActivityInfo.SetHorizontalAlignCenter()
		self.AchievementActivityInfo.SetText(localeInfo.ACHIEVEMENT_KILL % ("Razador"))
		self.AchievementActivityInfo.SetOutline()	
		self.AchievementActivityInfo.Show()
		self.AchievementPointMainInfo = ui.TextLine()
		self.AchievementPointMainInfo.SetParent(self.MainBGThinBoard)
		self.AchievementPointMainInfo.SetPosition((336/2)+30,40)
		self.AchievementPointMainInfo.SetHorizontalAlignCenter()
		self.AchievementPointMainInfo.SetText(localeInfo.ACHIEVEMENT_POINT_INFO % (100))
		self.AchievementPointMainInfo.SetOutline()	
		self.AchievementPointMainInfo.Show()	

		self.AchievementCountInfo = ui.TextLine()
		self.AchievementCountInfo.SetParent(self.MainBGThinBoard)
		self.AchievementCountInfo.SetPosition(160,70)
		self.AchievementCountInfo.SetHorizontalAlignCenter()
		self.AchievementCountInfo.SetText(localeInfo.ACHIEVEMENT_COUNT % (constInfo.NumberToPointString(90000)))
		self.AchievementCountInfo.SetOutline()	
		self.AchievementCountInfo.Show()	
		
		self.AchievementPointInfo = ui.TextLine()
		self.AchievementPointInfo.SetParent(self.MainBGThinBoard)
		self.AchievementPointInfo.SetPosition(240,70)
		self.AchievementPointInfo.SetHorizontalAlignCenter()
		self.AchievementPointInfo.SetText(localeInfo.ACHIEVEMENT_POINT % (constInfo.NumberToPointString(900000)))
		self.AchievementPointInfo.SetOutline()	
		self.AchievementPointInfo.Show()
		
		self.Hide()
		
	def Open(self):
		if self.IsShow():
			self.Hide()
			return
		self.initData()
		
		
		# achievement boss#Razador#100#5#10
	def SendAchievement(self,stringTypeInteger,achievementVnum,achievementPointThisInteger,achievementCountInteger,achievementPointNewInteger):
		if self.isLoaded == 0:
			achievementNameString = self.GetAchievementNameByVnum(achievementVnum)
			if stringTypeInteger == 1:		# Kill
				self.AchievementActivityInfo.SetText(localeInfo.ACHIEVEMENT_KILL % (achievementNameString))
			elif stringTypeInteger == 2:		# Dungeon
				self.AchievementActivityInfo.SetText(localeInfo.ACHIEVEMENT_DUNGEON % (achievementNameString))
			elif stringTypeInteger == 3:		# Destroy
				self.AchievementActivityInfo.SetText(localeInfo.ACHIEVEMENT_DESTROY % (achievementNameString))
			elif stringTypeInteger == 4:		# Reach
				self.AchievementActivityInfo.SetText(localeInfo.ACHIEVEMENT_REACH % (achievementNameString))
			
			self.AchievementPointMainInfo.SetText(localeInfo.ACHIEVEMENT_POINT_INFO % (achievementPointThisInteger))
			self.AchievementCountInfo.SetText(localeInfo.ACHIEVEMENT_COUNT % (constInfo.NumberToPointString(achievementCountInteger)))			
			self.AchievementPointInfo.SetText(localeInfo.ACHIEVEMENT_POINT % (constInfo.NumberToPointString(achievementPointNewInteger)))		
		
		
			self.Show()
			self.pos_width = wndMgr.GetScreenWidth() + 50
			self.SetPosition(wndMgr.GetScreenWidth() +50,wndMgr.GetScreenHeight()-150)
			self.isLoaded = 1
		else:
			achievementNameString = self.GetAchievementNameByVnum(achievementVnum)
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Du hast " + str(achievementNameString) + " besiegt! Du erhälst " + str(achievementPointThisInteger) + " Achievementpoints. (Gesamt: "+ str(achievementPointNewInteger) +", Count: "+str(achievementCountInteger)+")")
			
	def GetAchievementNameByVnum(self,vnum):
		if vnum < 10000:
			for i in xrange(len(settinginfo.MonsterAchievements)):
				if vnum == settinginfo.MonsterAchievements[i][0][0]:
					return settinginfo.MonsterAchievements[i][1][0]
			return "Noname"	
		elif vnum > 10000 and vnum < 10100:
			for i in xrange(len(settinginfo.DungeonAchievements)):
				if vnum == settinginfo.DungeonAchievements[i][0][0]:
					return settinginfo.DungeonAchievements[i][1][0]
			return "Noname"	
		else:
			return "Noname"
		
	def OnUpdate(self):
		if self.isLoaded == 1:
			targetLocation = wndMgr.GetScreenWidth() - 350
			#chat.AppendChat(chat.CHAT_TYPE_INFO,"targetLocation " + str(targetLocation))
			if self.pos_width > targetLocation:
				self.pos_width = self.pos_width - 15
				self.SetPosition(self.pos_width,wndMgr.GetScreenHeight()-150)
				#chat.AppendChat(chat.CHAT_TYPE_INFO,"pos_width " + str(self.pos_width))
			else:
				if self.isLoaded == 1:
					self.isLoaded = 2
					self.delay = app.GetTime() + 5
					
		if self.isLoaded == 2 and self.delay < app.GetTime():
			targetLocation = wndMgr.GetScreenWidth() + 350
			#chat.AppendChat(chat.CHAT_TYPE_INFO,"targetLocation " + str(targetLocation))
			if self.pos_width < targetLocation:
				self.pos_width = self.pos_width + 25
				self.SetPosition(self.pos_width,wndMgr.GetScreenHeight()-150)
				#chat.AppendChat(chat.CHAT_TYPE_INFO,"pos_width " + str(self.pos_width))			
			else:
				if self.isLoaded == 2:
					self.isLoaded = 0	
					self.Hide()
					#self.__del__()		
		
	def Destroy(self):
		self.Hide()
		self.__del__()
	
	def __del__(self):
		ui.Window.__del__(self)


		