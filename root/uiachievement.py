import wndMgr
import ui
import grp
import event
import chat
import app
import localeInfo
import constInfo
import nonplayer
import settinginfo
import achievementproto
# Developed by Exterminatus, 2020 @ Kimiko
class AchievementWindow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self,"TOP_MOST")
		self.SetSize(300, 72)
		self.SetPosition(wndMgr.GetScreenWidth()/2-150+60+50,wndMgr.GetScreenHeight()+150)
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
		
		self.MainBGThinBoard = ui.ImageBox()
		self.MainBGThinBoard.SetParent(self)
		self.MainBGThinBoard.SetPosition(0,0)
		self.MainBGThinBoard.LoadImage("yamato_achievement/achievement_" + app.GetLanguage() + "_background.tga")
		self.MainBGThinBoard.Show()
		
		self.faceBoxIMG = ui.ImageBox()
		self.faceBoxIMG.SetParent(self.MainBGThinBoard)
		self.faceBoxIMG.SetPosition(5 + 12,7 + 20)
		self.faceBoxIMG.Show()	

		self.AchievementTitle = ui.TextLine()
		self.AchievementTitle.SetParent(self.MainBGThinBoard)
		self.AchievementTitle.SetPosition(170,8 + 20)
		self.AchievementTitle.SetHorizontalAlignCenter()
		self.AchievementTitle.SetFontColor(0.9607, 0.2392, 0.0)
		self.AchievementTitle.Show()
		
		self.AchievementText = ui.TextLine()
		self.AchievementText.SetParent(self.MainBGThinBoard)
		self.AchievementText.SetPosition(170,25 + 20)
		self.AchievementText.SetHorizontalAlignCenter()
		self.AchievementText.Show()		
		
		self.AchievementPointsText = ui.TextLine()
		self.AchievementPointsText.SetParent(self.MainBGThinBoard)
		self.AchievementPointsText.SetPosition(100,40 + 20)
		self.AchievementPointsText.SetText(localeInfo.ACHIEVEMENT_UI_POINTS_TEXT)
		self.AchievementPointsText.Show()			
		
		self.AchievementPointsTextPoints = ui.TextLine()
		self.AchievementPointsTextPoints.SetParent(self.MainBGThinBoard)
		self.AchievementPointsTextPoints.SetPosition(216,40 + 20)
		self.AchievementPointsTextPoints.SetFontColor(1.0, 0.7843, 0.0)	
		self.AchievementPointsTextPoints.Show()	
		
		self.Hide()
		
	def Open(self):
		if self.IsShow():
			self.Hide()
			return
		self.initData()
		
	def SendAchievement(self,index,points,count,ap):
		data = achievementproto.GetAchievementInfo(int(index))
		if data == False:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Achievement Error: No Achievement found with index = " + str(index))
			return
			
		name = self.GetAchievementName(data[achievementproto.VNUM],data[achievementproto.DESC],data[achievementproto.TYPE])
		type = data[achievementproto.TYPE]	
		if self.isLoaded == 0:
			self.AchievementTitle.SetText(str(name) + " " + str(self.GetAchievementTypeByIndex(int(type))))
			self.AchievementText.SetText(localeInfo.ACHIEVEMENT_UI_COUNT + constInfo.NumberToPointString(count) + localeInfo.ACHIEVEMENT_UI_POINTS_GET + constInfo.NumberToPointString(data[achievementproto.POINTS]) + "")
			self.AchievementPointsTextPoints.SetText(constInfo.NumberToPointString(ap) + " AP!")

			try:
				self.faceBoxIMG.LoadImage("images_achievement/" + str(index) + ".tga")
			except:
				print "Achievement - %s No Face IMG in images_achievement/" % (index)
				self.faceBoxIMG.Hide()		

			self.Show()
			self.pos_height = wndMgr.GetScreenHeight() + 50
			self.SetPosition(wndMgr.GetScreenWidth() /2 - 150,wndMgr.GetScreenHeight()+50)
			self.isLoaded = 1
			self.index = int(index)
			
		if self.isLoaded == 2:
			# data = achievementproto.GetAchievementInfo(int(index))
			# if data == False:
				# return
			
			# name = self.GetAchievementName(data[achievementproto.VNUM],data[achievementproto.DESC],data[achievementproto.TYPE])
			# type = data[achievementproto.TYPE]
			
			self.AchievementPointsTextPoints.SetText(constInfo.NumberToPointString(ap) + " AP!")
			if self.index == int(index):
				self.AchievementText.SetText(localeInfo.ACHIEVEMENT_UI_COUNT + constInfo.NumberToPointString(count) + "  |  Punkte erhalten: " + constInfo.NumberToPointString(data[achievementproto.POINTS]) + "")
				if self.delay > app.GetTime():
					HideTimeOut = self.delay - app.GetTime()
					if HideTimeOut < 5:
						self.delay = app.GetTime() + 5

		chat.AppendChat(chat.CHAT_TYPE_INFO,"[ "+ name + " " + self.GetAchievementTypeByIndex(type) + localeInfo.ACHIEVEMENT_CHAT_COUNT + constInfo.NumberToPointString(count) + localeInfo.ACHIEVEMENT_CHAT_POINTS + constInfo.NumberToPointString(points) + localeInfo.ACHIEVEMENT_CHAT_POINTS_RISE + constInfo.NumberToPointString(ap) +" ]")
	
	def GetAchievementName(self,index,desc,type):
		if type == achievementproto.TYPE_BOSS or achievementproto.TYPE_STONE:
			return nonplayer.GetMonsterName(index)
		else:
			return desc

	def GetAchievementTypeByIndex(self,type):
		if type == achievementproto.TYPE_BOSS:
			return localeInfo.ACHIEVEMENT_TYPE_BOSS_TEXT
		elif type == achievementproto.TYPE_STONE:
			return localeInfo.ACHIEVEMENT_TYPE_STONE_TEXT
		elif type == achievementproto.TYPE_DUNGEON:
			return localeInfo.ACHIEVEMENT_TYPE_DUNGEON_TEXT
		elif type == achievementproto.TYPE_LEVEL:
			return ""			
		elif type == achievementproto.TYPE_REFINE:
			return ""			
		else:
			return ""
	
	def OnUpdate(self):
		if self.isLoaded == 1:
			targetLocation = wndMgr.GetScreenHeight() - 170
			
			if self.pos_height > targetLocation:
				self.pos_height = self.pos_height - 5
				self.SetPosition(wndMgr.GetScreenWidth() /2 - 150 + 5,self.pos_height)
			else:
				if self.isLoaded == 1:
					self.isLoaded = 2
					self.delay = app.GetTime() + 5
					
		if self.isLoaded == 2 and self.delay < app.GetTime():
			if self.MainBGThinBoard.IsIn():
				return
				
			targetLocation = wndMgr.GetScreenWidth() + 50
			if self.pos_height < targetLocation:
				self.pos_height = self.pos_height + 25
				self.SetPosition(wndMgr.GetScreenWidth() /2 - 150 + 5,self.pos_height)
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
