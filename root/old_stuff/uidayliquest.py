#Code by Yoshix3 for Akaya2
#Version 0.0 (08.11.2014)
import ui
import fgGHGjjFHJghjfFG1545gGG
import app
import math

class MainWindow(ui.BoardWithTitleBar):
	
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.SetSize(350,350)
		self.SetCenterPosition()
		self.SetTitleName("Daily-Quest")
		self.AddFlag("movable")
		self.AddFlag("float")
		self.Hide()
		
		self.Index = 0
		self.AddQuestHeight = 1
		
		self.OverLines = []
		for i in [["Auftrag:",45],["Zeit bis zur nächsten Daily:",80],["Belohnung:",130],["Auftrag starten:",255]]:
			b = ui.HorizontalBar()
			b.SetParent(self)
			b.SetPosition(12,i[1]+(i[1] > 45 and self.AddQuestHeight*15))
			b.pos = i[1]
			b.Create(326)
			b.Show()
			b.line = ui.TextLine()
			b.line.SetParent(b)
			b.line.SetPosition(326/2,1)
			b.line.SetHorizontalAlignCenter()
			b.line.SetText(i[0])
			b.line.Show()
			self.OverLines.append(b)
		
		self.MobInfoLines = []
		for i in xrange(10):
			l = ui.TextLine()
			l.SetParent(self)
			if i in [1,3,5,7,9]:
				l.SetPosition(336,70+(i-1)/2*15)
			else:
				l.SetPosition(14,70+i/2*15)
			if i in [1,3,5,7,9]:
				l.SetHorizontalAlignRight()
			# l.SetText("Töte 10 Wildhunde")
			l.Hide()
			self.MobInfoLines.append(l)
		
		self.TimeLeft = ui.TextLine()
		self.TimeLeft.SetParent(self)
		self.TimeLeft.SetPosition(14,self.AddQuestHeight*15+105)
		self.TimeLeft.SetText("Du kannst wieder einen Auftrag starten.")
		self.TimeLeft.Time = 0
		self.TimeLeft.Show()
		
		self.qLimit = ui.Button()
		self.qLimit.SetParent(self)
		self.qLimit.SetPosition(50,280+self.AddQuestHeight*15)
		self.qLimit.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.qLimit.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.qLimit.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.qLimit.limit = 2
		self.qLimit.limitTable = [["Lv. 1 bis Lv. 84","Lv. 85 bis Lv. 134","Lv. 135"],["Leicht","Mittel","Schwer"]]
		# self.qLimit.SetEvent(ui.__mem_func__(self.ChangeLimit))
		self.qLimit.Show()
	
		self.qStart = ui.RadioButton()
		self.qStart.SetParent(self)
		self.qStart.SetPosition(220,280+self.AddQuestHeight*15)
		self.qStart.SetUpVisual("d:/ymir work/ui/game/windows/tab_button_large_01.sub")
		self.qStart.SetOverVisual("d:/ymir work/ui/game/windows/tab_button_large_02.sub")
		self.qStart.SetDownVisual("d:/ymir work/ui/game/windows/tab_button_large_03.sub")
		self.qStart.SetText("Auftrag starten")
		self.qStart.SetEvent(ui.__mem_func__(self.StartQuest))
		self.qStart.Show()
		self.qStart.Down()
		
		self.ThinWinText = ui.ThinBoard()
		self.ThinWinText.SetParent(self)
		self.ThinWinText.SetPosition(12,155+self.AddQuestHeight*15)
		self.ThinWinText.SetSize(165,90)
		self.ThinWinText.Show()
		
		self.InfoLines = []
		for i in xrange(7):
			l = ui.TextLine()
			if i < 5:
				l.SetParent(self.ThinWinText)
				l.SetPosition(165/2,7+i*15)
			else:
				l.SetParent(self)
				l.SetPosition(262,165+self.AddQuestHeight*15+45*(i-5))
			l.SetHorizontalAlignCenter()
			l.SetText(["Nach abschließen","dieser Quest","erhälst du","folgend gelistete","Items:","Daily-Kiste","1 Dailypoint(s)"][i])
			l.Show()
			self.InfoLines.append(l)
		
		#self.ItemImage = ui.ImageBox()
		#self.ItemImage.SetParent(self)
		#self.ItemImage.SetPosition(262-16,185+self.AddQuestHeight*15)
		#self.ItemImage.LoadImage("icon/item/daily.tga")
		#self.ItemImage.Show()
	
		self.ItemImage2 = ui.ImageBox()
		self.ItemImage2.SetParent(self)
		self.ItemImage2.SetPosition(262-16,185+self.AddQuestHeight*15+45)
		self.ItemImage2.LoadImage("icon/sidebar/daily.tga")
		self.ItemImage2.Show()
		
		self.ChangeLimit()
	
		self.SetSize(350,320+self.AddQuestHeight*15)
	
	def OnUpdate(self):
		if self.TimeLeft.Time == 0:
			return
		if self.TimeLeft.Time > app.GetTime():
			leftsec = self.TimeLeft.Time-app.GetTime()
			stunden = int(math.floor(leftsec/60/60))
			min = int(math.floor((leftsec-stunden*60*60)/60))
			sec = int(leftsec-stunden*60*60-min*60)
			self.TimeLeft.SetText("Du musst noch "+str(stunden)+" Stunden, "+str(min)+" Minuten und "+str(sec)+" Sekunden warten.")
		else:
			self.TimeLeft.SetText("Du kannst wieder einen neuen Auftrag annehmen.")
			self.TimeLeft.Time = 0
			self.qStart.SetUp()
		
	def WorkWithString(self, str):
		if str.find("#") != -1:
			str = str.split("#")
			self.Index = int(str[0])
			if len(str) < 4:
				self.AddQuestHeight = 1
				self.HideMobLines()
				self.MobInfoLines[0].SetText("Derzeit kein Auftrag Aktiv")
				self.MobInfoLines[0].Show()
			else:
				self.qStart.Down()
				# self.AddQuestHeight = 1
				self.HideMobLines()
				self.ArrangeMobLines(str[3])
			self.ArrangePosition()
			if int(str[1]) < 1:
				self.TimeLeft.Time = -1
			else:
				self.TimeLeft.Time = app.GetTime()+int(str[1])
				self.qStart.Down()
			if int(str[2]) > 0:
				self.qStart.SetText("Belohnung abholen")
				self.qStart.SetUp()
			else:
				self.qStart.SetText("Auftrag starten")
		
	def ArrangeMobLines(self, lines):
		if lines.find("|") != -1:
			lines = lines.split("|")
			for i in xrange(len(lines)-1):
				row = lines[i].split(",")
				self.MobInfoLines[i*2].SetText("Töte "+row[2]+" "+row[0].replace("_"," ")+":")
				self.MobInfoLines[i*2+1].SetText(row[1]+" von "+row[2]+" erlegt")
				self.MobInfoLines[i*2].Show()
				self.MobInfoLines[i*2+1].Show()
		self.AddQuestHeight = len(lines)-1
		
	def HideMobLines(self):
		for i in self.MobInfoLines:
			i.Hide()
	
	def ChangeLimit(self):
		# self.qLimit.limit+=1
		# if self.qLimit.limit > 2:
			# self.qLimit.limit = 0
		# self.qLimit.SetToolTipText(self.qLimit.limitTable[0][self.qLimit.limit])
		# self.qLimit.SetText(self.qLimit.limitTable[1][self.qLimit.limit])
		level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
		if level <= 84:
			self.qLimit.limit = 0
		elif level >= 85 and level <= 134:
			self.qLimit.limit = 1
		else:
			self.qLimit.limit = 2
		self.InfoLines[6].SetText(str(self.qLimit.limit+1)+" Dailypoints")
		self.qLimit.SetToolTipText(self.qLimit.limitTable[0][self.qLimit.limit])
		self.qLimit.SetText(self.qLimit.limitTable[1][self.qLimit.limit])
		# self.ItemImage2.LoadImage("icon/item/daily.tga")
		
	def StartQuest(self):
		if self.Index < 1:
			return
		if fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL) < 5:
			import chat
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Dein Level ist noch zu niedrig.")
			self.qStart.SetUp()
			return
		import event
		event.QuestButtonClick(self.Index)
	
	def ArrangePosition(self):
		for i in xrange(len(self.OverLines)):
			if i > 0:
				self.OverLines[i].SetPosition(12,self.OverLines[i].pos+self.AddQuestHeight*15)
		self.TimeLeft.SetPosition(14,self.AddQuestHeight*15+105)
		self.qLimit.SetPosition(50,280+self.AddQuestHeight*15)
		self.ThinWinText.SetPosition(12,155+self.AddQuestHeight*15)
		self.qStart.SetPosition(220,280+self.AddQuestHeight*15)
		#self.ItemImage.SetPosition(262-16,170+self.AddQuestHeight*15)
		
		self.ItemImage2.SetPosition(262-16,170+self.AddQuestHeight*15+45)
		
		self.InfoLines[5].Hide()#SetPosition(262,155+self.AddQuestHeight*15)
		self.InfoLines[6].SetPosition(262,155+self.AddQuestHeight*15+45)
		self.SetSize(350,320+self.AddQuestHeight*15)
			
		
	def Open(self):
		if self.IsShow():
			self.Hide()
		else:
			if self.Index < 1:
				import chat
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Das System wird noch geladen.")
				return
			self.Show()
	
	def Destroy(self):
		self.Hide()
		
	def __del__(self):
		self.Hide()
		ui.BoardWithTitleBar.__del__(self)

