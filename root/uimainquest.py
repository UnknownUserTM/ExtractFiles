import ui
import chat
import fgGHGjjFHJghjfFG1545gGG as player
import item
import GFHhg54GHGhh45GHGH as net 
import constInfo
import event
import localeInfo
import questinfo
import nonplayer
import exterminatus
import app
import wndMgr
# from uitooltip import ItemToolTip
# AFFECT_DICT = ItemToolTip.AFFECT_DICT

class QuestDialog(ui.ScriptWindow):
	BOTTOM_MODE_INTRO = 0
	BOTTOM_MODE_DIALOG = 1
	BOTTOM_MODE_REWARD = 2
	BOTTOM_MODE_MAX = 3
	
	BUTTON_TYPE_ACCEPT = 0
	BUTTON_TYPE_DECLINE = 1
	BUTTON_TYPE_CONTINUE = 2
	BUTTON_TYPE_COMPLETE = 3
	BUTTON_TYPE_FOLLOW = 4
	
	TARGET_TYPE_KILL = 0
	TARGET_TYPE_TALK = 1
	TARGET_TYPE_COLLECT = 2

	LINES_UNTIL_SHOW_SCROLLBAR = 17
	
	x_start = 0
	y_start = 0
	
	quest_index = 0
	def __init__(self,interface):
		ui.ScriptWindow.__init__(self)
		self.interface = interface
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/questdialog.py")
		except:
			import exception
			exception.Abort("QuestIntroBoard.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		self.board = self.GetChild("board")
		
		self.questDialogBottom = []
		self.questDialogBottom.append(self.GetChild("QuestBottomBar_0"))
		self.questDialogBottom.append(self.GetChild("QuestBottomBar_1"))
		self.questDialogBottom.append(self.GetChild("QuestBottomBar_2"))
		
		self.AcceptButton = self.GetChild("AcceptButton")
		self.DeclineButton = self.GetChild("DeclineButton")
		self.ContinueButton = self.GetChild("ContinueButton")
		self.CompleteButton = self.GetChild("CompleteButton")
		
		self.AcceptButton.SetEvent(self.OnClickQuestDialogButton,self.BUTTON_TYPE_ACCEPT)
		self.DeclineButton.SetEvent(self.OnClickQuestDialogButton,self.BUTTON_TYPE_DECLINE)
		self.ContinueButton.SetEvent(self.OnClickQuestDialogButton,self.BUTTON_TYPE_CONTINUE)
		self.CompleteButton.SetEvent(self.OnClickQuestDialogButton,self.BUTTON_TYPE_COMPLETE)
	
		self.QuestPaper = QuestPaper(self.interface)
		self.QuestPaper.SetParent(self.board)
		self.QuestPaper.SetPosition(0,0)
		self.QuestPaper.Show()
		
		self.SetBottomMode(self.BOTTOM_MODE_INTRO)
		
		self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)
		
	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.QuestPaper.questListScrollBar.OnUp()
		else:
			self.QuestPaper.questListScrollBar.OnDown()
		
	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			(self.x_start, self.y_start, z) = player.GetMainCharacterPosition()
			self.Show()
			
	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.__del__()	
		
	# QUEST_INPUT BEGIN!
	def SetTitle(self,index):
		self.QuestPaper.SetTitle(questinfo.GetQuestString(index))
		
	def SetDescription(self,index):
		self.QuestPaper.SetDescription(questinfo.GetQuestString(index))
		self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)
		
	def SetTargetTitle(self):
		self.QuestPaper.SetObjectiveTitle()
		self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)
		
	def SetTarget(self,type,vnum,min_count,max_count,status):
		if type == self.TARGET_TYPE_KILL:
			string = str(min_count) + " / " + str(max_count) + " " + str(nonplayer.GetMonsterName(vnum)) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_KILL
		elif type == self.TARGET_TYPE_TALK:
			string = localeInfo.QUEST_INTRO_OBJECTIVE_TALK + " " + nonplayer.GetMonsterName(vnum) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_TALK2
		elif type == self.TARGET_TYPE_COLLECT:
			item.SelectItem(vnum)
			string = str(min_count) + " / " + str(max_count) + " " + str(item.GetItemName()) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_COLLECT
		else:
			string = questinfo.GetQuestString(vnum)
			
		self.QuestPaper.SetObjective(string,exterminatus.StringBoolToRealBool(status))
		self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)
		
	def SetRewardTitle(self):
		self.QuestPaper.SetRewardTitle()
	
	def SetReward(self,type,vnum,count):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SetReward QD: " + str(type) + ", " + str(vnum) + ", " + str(count))
		self.QuestPaper.SetReward(type,vnum,count)
		self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)
	
	def SetBottomMode(self,mode):
		mode = int(mode)
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SetBottomMode: " + str(mode))
		for i in xrange(self.BOTTOM_MODE_MAX):
			if i == mode:
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SetBottomMode: " + str(i) + " set Show!") #+ str(mode))
				self.questDialogBottom[i].Show()
			else:
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SetBottomMode: " + str(i) + " set Hide!") #+ str(mode))
				self.questDialogBottom[i].Hide()
		
		self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)

	def SetQuestIndex(self,index):
		self.quest_index = int(index)
	
	def DisableDeclineButton(self):
		self.DeclineButton.Disable()
	
	def ClearQuestDialog(self):
		self.SetBottomMode(self.BOTTOM_MODE_INTRO)
		self.QuestPaper.Clear()
		self.quest_index = 0
		self.DeclineButton.Enable()
		# self.scrollBar.SetPos(0)
		
	# QUEST_INPUT END!
	def OnClickQuestDialogButton(self,buttonType):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(buttonType))
		constInfo.INPUT_CMD = str(buttonType) + "/"
		event.QuestButtonClick(self.quest_index)

	def OnUpdate(self):
		USE_LIMIT_RANGE = 1000
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.x_start) > USE_LIMIT_RANGE or abs(y - self.y_start) > USE_LIMIT_RANGE:
			self.Close()
			

class QuestPaper(ui.ScriptWindow):
	
	QUEST_REWARD_TYPE_GOLD				= 0
	QUEST_REWARD_TYPE_ACHIEVEMENTPOINTS	= 1
	QUEST_REWARD_TYPE_DUNGEONPOINTS		= 2
	QUEST_REWARD_TYPE_EVENTPOINTS		= 3
	QUEST_REWARD_TYPE_ITEM				= 4
	QUEST_REWARD_TYPE_ATTRIBUTE			= 5
	QUEST_REWARD_TYPE_EXP				= 6
	
	QUEST_REWARD_ICON = {
		QUEST_REWARD_TYPE_GOLD				: "gold_coin",
		QUEST_REWARD_TYPE_ACHIEVEMENTPOINTS : "achievement_small",
		QUEST_REWARD_TYPE_DUNGEONPOINTS		: "gold_coin",
		QUEST_REWARD_TYPE_EVENTPOINTS		: "gold_coin",
		QUEST_REWARD_TYPE_ITEM				: "item",
		QUEST_REWARD_TYPE_ATTRIBUTE			: "bonus",
		QUEST_REWARD_TYPE_EXP				: "exp",
	}
	
	def __init__(self,interface):
		ui.ScriptWindow.__init__(self)
		self.interface = interface
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/questpaper.py")
		except:
			import exception
			exception.Abort("QuestPaper.LoadWindow.LoadObject")
		
		self.questTitle = self.GetChild("QuestTitleTextLine")
		self.questListBox = self.GetChild("QuestContentListBox")
		self.questListScrollBar = self.GetChild("scrollBar")
		self.questListScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestScroll))
	
	def SetTitle(self,title):
		self.questTitle.SetText(str(title))
		
	def SetDescription(self,desc):
		self.questListBox.InsertTitleItem(localeInfo.QUEST_INTRO_DESCRIPTION_TITLE)
		desc = desc.split("[ENTER]")
		for i in xrange(len(desc)):
			self.questListBox.InsertDescItem(desc[i])
		self.questListBox.InsertEmptyItem()
		
	def SetObjectiveTitle(self):
		self.questListBox.InsertTitleItem(localeInfo.QUEST_INTRO_OBJECTIVE_TITLE)
		
	def SetObjective(self,text,status):
		self.questListBox.InsertObjectiveItem(text,status)
	
	def UpdateObjective(self,index,text,status):
		self.questListBox.ChangeObjectiveItem(index,text,status)
	
	def SetRewardTitle(self):
		self.questListBox.InsertEmptyItem()
		self.questListBox.InsertTitleItem(localeInfo.QUEST_INTRO_REWARD_TITLE)
	
	def SetReward(self,type,vnum,count):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"SetReward: " + str(type) + ", " + str(vnum) + ", " + str(count))
		if type >= self.QUEST_REWARD_TYPE_GOLD and type <= self.QUEST_REWARD_TYPE_ACHIEVEMENTPOINTS:
			self.questListBox.InsertCurrencyItem(constInfo.NumberToPointString(count),self.QUEST_REWARD_ICON[type])
			
		elif type == self.QUEST_REWARD_TYPE_ITEM:
			self.questListBox.InsertItemRewardItem(vnum,count)

		elif type == self.QUEST_REWARD_TYPE_ATTRIBUTE:
			# self.questListBox.InsertAttributeItem(str(AFFECT_DICT[vnum](count)))
			return
		elif type == self.QUEST_REWARD_TYPE_EXP:
			self.questListBox.InsertCurrencyItem(constInfo.NumberToPointString(count),self.QUEST_REWARD_ICON[type])
		
		else:
			return
	
	def CheckForScrollBar(self,minCountForScrollBar):
		itemCount = self.questListBox.GetItemCount()
		if itemCount > minCountForScrollBar:
			self.questListScrollBar.Show()
		else:
			self.questListScrollBar.Hide()
	
	def Clear(self):
		self.questTitle.SetText("")
		self.questListBox.ClearItem()
		self.questListScrollBar.SetPos(0)
			
	def OnQuestScroll(self):
		viewItemCount = self.questListBox.GetViewItemCount()
		itemCount = self.questListBox.GetItemCount()
		pos = self.questListScrollBar.GetPos() * (itemCount - viewItemCount)
		self.questListBox.SetBasePos(int(pos))		
		
	def Destroy(self):
		self.__del__()	


class QuestWindow(ui.ScriptWindow):

	QUEST_DATA_QUESTINDEX = 0
	QUEST_DATA_TITLE = 1
	QUEST_DATA_DESC = 2
	QUEST_DATA_TARGET = 3
	QUEST_DATA_REWARD = 4
	QUEST_DATA_DECLINE = 5
	QUEST_DATA_FOLLOW = 6
	
	QUEST_DATA_TARGET_TYPE = 0
	QUEST_DATA_TARGET_VNUM = 1
	QUEST_DATA_TARGET_MIN_COUNT = 2
	QUEST_DATA_TARGET_MAX_COUNT = 3
	QUEST_DATA_TARGET_STATUS = 4
	
	QUEST_DATA_REWARD_TYPE = 0
	QUEST_DATA_REWARD_VNUM = 1
	QUEST_DATA_REWARD_COUNT = 2
	
	TARGET_TYPE_KILL = 0
	TARGET_TYPE_TALK = 1
	TARGET_TYPE_COLLECT = 2
	
	TAB_BUTTON_MAIN_QUEST		= 0
	TAB_BUTTON_SIDE_QUEST		= 1
	TAB_BUTTON_DUNGEON_QUEST	= 2
	TAB_BUTTON_EVENT_QUEST		= 3
	TAB_BUTTON_CHALLENGE_QUEST	= 4
	
	QUEST_CATEGORY_NAME = {
		TAB_BUTTON_MAIN_QUEST		: localeInfo.QUEST_WINDOW_CATEGORY_MAINQUEST,
		TAB_BUTTON_SIDE_QUEST		: localeInfo.QUEST_WINDOW_CATEGORY_SIDEQUEST,
		TAB_BUTTON_DUNGEON_QUEST	: localeInfo.QUEST_WINDOW_CATEGORY_DUNGEON,
		TAB_BUTTON_EVENT_QUEST		: localeInfo.QUEST_WINDOW_CATEGORY_EVENT,
		TAB_BUTTON_CHALLENGE_QUEST	: localeInfo.QUEST_WINDOW_CATEGORY_CHALLENGE,
	}
	
	QUEST_TAB_COUNT = 5
	LINES_UNTIL_SHOW_SCROLLBAR = 17

	questTabButtonBasePosition = [15,5]

	def __init__(self,interface):
		ui.ScriptWindow.__init__(self)
		self.interface = interface
		self.questDialog = None
		self.questCurrent = 0
		self.questContent = [
			[], # <- placeholder
			[], # <- TAB_BUTTON_MAIN_QUEST
			[], # <- TAB_BUTTON_SIDE_QUEST
			[], # <- TAB_BUTTON_HUNT_QUEST
			[], # <- TAB_BUTTON_EVENT_QUEST
			[], # <- TAB_BUTTON_CHALLENGE_QUEST
		]
		self.questCategory = self.TAB_BUTTON_MAIN_QUEST
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/mainquestboard.py")
		except:
			import exception
			exception.Abort("QuestWindow.LoadWindow.LoadObject")	
		
		try:
			# Close Event
			self.GetChild("Close_Button").SetEvent(self.Close)
			
			# QuestDialog
			self.questDialog = QuestDialog(self.interface)
			
			self.questView = QuestView()
			self.questView.Open()
			
			self.questListContentCarv = self.GetChild("QuestList_ContentCarve")
			self.questListBox = self.GetChild("Quest_ListBox")
			self.questListBox.SetEvent(ui.__mem_func__(self.OnSelectQuest))
			self.questListScrollBar = self.GetChild("Quest_ScrollBar")
			
			# QuestTab Buttons
			self.questTab = []
			self.questTab.append(self.GetChild("MainQuestTab_Button"))
			self.questTab.append(self.GetChild("BiologistQuestTab_Button"))
			self.questTab.append(self.GetChild("HuntQuestTab_Button"))
			self.questTab.append(self.GetChild("SideQuestTab_Button"))
			self.questTab.append(self.GetChild("QuestBookQuestTab_Button"))	
			
			self.questTabTextLine = []
			self.questTabTextLine.append(self.GetChild("MainQuestTab_Title"))
			self.questTabTextLine.append(self.GetChild("BiologistQuestTab_Title"))
			self.questTabTextLine.append(self.GetChild("HuntQuestTab_Title"))
			self.questTabTextLine.append(self.GetChild("SideQuestTab_Title"))
			self.questTabTextLine.append(self.GetChild("QuestBookQuestTab_Title"))
			
			self.questPaperBackground = self.GetChild("QuestDescContentCarve")
			
			self.QuestPaper = QuestPaper(self.interface)
			self.QuestPaper.SetParent(self.questPaperBackground)
			self.QuestPaper.SetPosition(-24,-14)
			self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)
			self.QuestPaper.Show()			
			# BottomButtons
			self.followButton = self.GetChild("FollowButton")
			self.followButton.SetEvent(self.FollowQuest)
			self.declineButton = self.GetChild("AbortButton")
			self.declineButton.SetEvent(self.AbortQuest)

		except:
			import exception
			exception.Abort("QuestWindow.LoadWindow.BindObject")		
		
		self.questListScrollBar.Hide()
		self.questListContentCarv.Hide()
		self.questTab[0].SetEvent(lambda arg=self.TAB_BUTTON_MAIN_QUEST: self.SetQuestCategory(arg))
		self.questTab[1].SetEvent(lambda arg=self.TAB_BUTTON_SIDE_QUEST: self.SetQuestCategory(arg))
		self.questTab[2].SetEvent(lambda arg=self.TAB_BUTTON_DUNGEON_QUEST: self.SetQuestCategory(arg))
		self.questTab[3].SetEvent(lambda arg=self.TAB_BUTTON_EVENT_QUEST: self.SetQuestCategory(arg))
		self.questTab[4].SetEvent(lambda arg=self.TAB_BUTTON_CHALLENGE_QUEST: self.SetQuestCategory(arg))		

		self.ReArrangeButtons()
		self.Refresh()

		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def Open(self):
		self.Show()
		
	def Destroy(self):
		self.Hide()
		self.questDialog.Destroy()
		self.questDialog = None
		self.questContent = [[],[],[],[],[],[],]
		self.questView.Destroy()
		
	def Refresh(self):
		for i in xrange(5):
			self.questTabTextLine[i].SetText(self.QUEST_CATEGORY_NAME[i] + " (" + str(len(self.questContent[i])) + ")")
		
		self.QuestPaper.Clear()
		self.followButton.Disable()
		self.declineButton.Disable()	
		self.BuildQuestList()

		
	def BuildQuestList(self):
		self.questListBox.ClearItem()
		if len(self.questContent[self.questCategory]) == 0:
			return
			
		for i in xrange(len(self.questContent[self.questCategory])):
			self.questListBox.InsertItem(i,questinfo.GetQuestString(self.questContent[self.questCategory][i][self.QUEST_DATA_TITLE]))
		
		# self.questListBox.SelectItem(0)
		
		if len(self.questContent[self.questCategory]) >= 8:
			self.questListScrollBar.Show()
		else:
			self.questListScrollBar.Hide()
		
	def BuildQuestPaper(self):
		self.QuestPaper.Clear()
		myQuest = self.questContent[self.questCategory][self.questCurrent]
		self.QuestPaper.SetTitle(questinfo.GetQuestString(myQuest[self.QUEST_DATA_TITLE]))
		self.QuestPaper.SetDescription(questinfo.GetQuestString(myQuest[self.QUEST_DATA_DESC]))
		
		if len(myQuest[self.QUEST_DATA_TARGET]) > 0:
			self.QuestPaper.SetObjectiveTitle()
			for i in xrange(len(myQuest[self.QUEST_DATA_TARGET])):
			
				type		= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_TYPE]
				vnum		= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_VNUM]
				min_count	= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_MIN_COUNT]
				max_count	= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_MAX_COUNT]
				status		= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_STATUS]
				
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"type : " + str(type))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"vnum : " + str(vnum))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"min_count : " + str(min_count))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"max_count : " + str(max_count))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"status : " + str(status))

				if type == self.TARGET_TYPE_KILL:
					string = str(min_count) + " / " + str(max_count) + " " + str(nonplayer.GetMonsterName(vnum)) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_KILL
				elif type == self.TARGET_TYPE_TALK:
					string = localeInfo.QUEST_INTRO_OBJECTIVE_TALK + " " + nonplayer.GetMonsterName(vnum) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_TALK2
				elif type == self.TARGET_TYPE_COLLECT:
					item.SelectItem(vnum)
					string = str(min_count) + " / " + str(max_count) + " " + str(item.GetItemName()) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_COLLECT
				else:
					string = questinfo.GetQuestString(vnum)
			
				self.QuestPaper.SetObjective(string,exterminatus.StringBoolToRealBool(status))		
			
		
		if len(myQuest[self.QUEST_DATA_REWARD]) > 0:
			self.QuestPaper.SetRewardTitle()
			for i in xrange(len(myQuest[self.QUEST_DATA_REWARD])):
				
				type	= myQuest[self.QUEST_DATA_REWARD][i][self.QUEST_DATA_REWARD_TYPE]
				vnum	= myQuest[self.QUEST_DATA_REWARD][i][self.QUEST_DATA_REWARD_VNUM]
				count	= myQuest[self.QUEST_DATA_REWARD][i][self.QUEST_DATA_REWARD_COUNT]
				
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"type : " + str(type))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"vnum : " + str(vnum))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"count : " + str(count))
				
				self.QuestPaper.SetReward(type,vnum,count)
			self.QuestPaper.questListBox.InsertEmptyItem()
		self.QuestPaper.CheckForScrollBar(self.LINES_UNTIL_SHOW_SCROLLBAR)
		if myQuest[self.QUEST_DATA_DECLINE] == "false":
			self.declineButton.Disable()
		else:
			self.declineButton.Enable()
			
		if myQuest[self.QUEST_DATA_FOLLOW] == "false":
			self.followButton.Disable()
		else:
			self.followButton.Enable()
			
		# if len(myQuest[self.QUEST_DATA_TARGET]) > 0:
			# # chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FollowButton Enable!")
			# self.followButton.Enable()
		# else:
			# # chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FollowButton Disable!")
			# self.followButton.Disable()
			
	def UpdateQuestPaperTarget(self,qid,questType): #,type,vnum,min_count,max_count,status):
		quest = self.FindQuestByQID(qid,questType)
		if quest < 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FEHLER: Quest mit der ID " + str(qid) + " wurde nicht gefunden!")
			return

		
		if self.questCategory != questType:
			return
			
		if self.questContent[self.questCategory][quest][self.QUEST_DATA_QUESTINDEX] != qid:
			return
		
		myQuest = self.questContent[self.questCategory][self.questCurrent]
		for i in xrange(len(myQuest[self.QUEST_DATA_TARGET])):
			type		= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_TYPE]
			vnum		= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_VNUM]
			min_count	= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_MIN_COUNT]
			max_count	= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_MAX_COUNT]
			status		= myQuest[self.QUEST_DATA_TARGET][i][self.QUEST_DATA_TARGET_STATUS]
					
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"type : " + str(type))
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"vnum : " + str(vnum))
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"min_count : " + str(min_count))
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"max_count : " + str(max_count))
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"status : " + str(status))

			if type == self.TARGET_TYPE_KILL:
				string = str(min_count) + " / " + str(max_count) + " " + str(nonplayer.GetMonsterName(vnum)) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_KILL
			elif type == self.TARGET_TYPE_TALK:
				string = localeInfo.QUEST_INTRO_OBJECTIVE_TALK + " " + nonplayer.GetMonsterName(vnum) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_TALK2
			elif type == self.TARGET_TYPE_COLLECT:
				item.SelectItem(vnum)
				string = str(min_count) + " / " + str(max_count) + " " + str(item.GetItemName()) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_COLLECT
			else:
				string = questinfo.GetQuestString(vnum)

			self.QuestPaper.UpdateObjective(i,string,exterminatus.StringBoolToRealBool(status))
		
		
		
	def OnSelectQuest(self):
		self.questCurrent = self.questListBox.GetSelectedItem()
		self.BuildQuestPaper()
		
		
	####################################
	## QUEST_INPUT

	def InitQuest(self,qid,questType,title,desc,declineButton,followStatus):
		quest = self.FindQuestByQID(qid,questType)
		if quest >= 0:
			return
			
		quest = {
			self.QUEST_DATA_QUESTINDEX	: int(qid),
			self.QUEST_DATA_TITLE		: int(title),
			self.QUEST_DATA_DESC		: int(desc),
			self.QUEST_DATA_TARGET		: [],
			self.QUEST_DATA_REWARD		: [],
			self.QUEST_DATA_DECLINE		: declineButton,
			self.QUEST_DATA_FOLLOW		: followStatus,
		}

		self.questContent[questType].append(quest)
		self.Refresh()
		
		
	def RemoveQuest(self,qid,questType):
		quest = self.FindQuestByQID(qid,questType)
		if quest < 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FEHLER: Quest mit der ID " + str(qid) + " wurde nicht gefunden!")
			return

		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(len(self.questContent[questType])))
		del self.questContent[questType][quest]
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(len(self.questContent[questType])))
		self.Refresh()
		
	def AppendTarget(self,qid,questType,type,vnum,min_count,max_count,status):
		quest = self.FindQuestByQID(qid,questType)
		if quest < 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FEHLER: Quest mit der ID " + str(qid) + " wurde nicht gefunden!")
			return
		
		target = {
			self.QUEST_DATA_TARGET_TYPE			: int(type),
			self.QUEST_DATA_TARGET_VNUM			: int(vnum),
			self.QUEST_DATA_TARGET_MIN_COUNT	: int(min_count),
			self.QUEST_DATA_TARGET_MAX_COUNT	: int(max_count),
			self.QUEST_DATA_TARGET_STATUS		: status,
		}
		
		self.questContent[questType][quest][self.QUEST_DATA_TARGET].append(target)
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(self.questContent[questType][quest][self.QUEST_DATA_TARGET][0][self.QUEST_DATA_TARGET_VNUM]))
		
	def UpdateQuestTarget(self,qid,questType,index,min_count,max_count,status):
		quest = self.FindQuestByQID(qid,questType)
		if quest < 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FEHLER: Quest mit der ID " + str(qid) + " wurde nicht gefunden!")
			return	
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(self.questContent[questType][quest][self.QUEST_DATA_TARGET][0][self.QUEST_DATA_TARGET_MIN_COUNT]))
		self.questContent[questType][quest][self.QUEST_DATA_TARGET][index][self.QUEST_DATA_TARGET_MIN_COUNT] = int(min_count)
		self.questContent[questType][quest][self.QUEST_DATA_TARGET][index][self.QUEST_DATA_TARGET_MAX_COUNT] = int(max_count)
		self.questContent[questType][quest][self.QUEST_DATA_TARGET][index][self.QUEST_DATA_TARGET_STATUS] = status
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(self.questContent[questType][quest][self.QUEST_DATA_TARGET][0][self.QUEST_DATA_TARGET_MIN_COUNT]))
		
		self.UpdateQuestPaperTarget(qid,questType)
		
		
	def AppendReward(self,qid,questType,type,vnum,count):
		quest = self.FindQuestByQID(qid,questType)
		if quest < 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FEHLER: Quest mit der ID " + str(qid) + " wurde nicht gefunden!")
			return
		
		reward = {
			self.QUEST_DATA_REWARD_TYPE			: int(type),
			self.QUEST_DATA_REWARD_VNUM			: int(vnum),
			self.QUEST_DATA_REWARD_COUNT		: int(count),
		}
		
		self.questContent[questType][quest][self.QUEST_DATA_REWARD].append(reward)
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(self.questContent[questType][quest][self.QUEST_DATA_REWARD][0][self.QUEST_DATA_REWARD_VNUM]))		
	

	
	def InitFollow(self,qid,title):
		self.questView.AppendQuestView(qid,title)
	
	def AppendQuestFollowObjective(self,qid,type,vnum,min_count,max_count):
		self.questView.AppendQuestViewObjective(qid,type,vnum,min_count,max_count)
	
	def UpdateFollow(self,qid,index,min_count,max_count):
		self.questView.UpdateQuestViewObjective(qid,index,min_count,max_count)
		
	def RemoveFollow(self,qid):
		self.questView.RemoveQuestViewItem(qid)
		
	def RefreshQuestView(self):
		self.questView.Refresh()
		
	####################################
		
	def FindQuestByQID(self,qid,questType):
		for i in xrange(len(self.questContent[questType])):
			if self.questContent[questType][i][self.QUEST_DATA_QUESTINDEX] == qid:
				return i
		
		return -1
		
	def SetQuestCategory(self,questCategory):
		if questCategory == self.questCategory:
			return

		self.questCategory = int(questCategory)
		self.questCurrent = 0
		self.ReArrangeButtons()
		self.Refresh()
		
	def ReArrangeButtons(self):
		y = 5
		for i in xrange(self.QUEST_TAB_COUNT):	
			questTabIndex = i 
			
			self.questTab[i].SetPosition(15,y)
			
			if questTabIndex == self.questCategory:
				self.questListScrollBar.SetPosition(15+3+280-12,y+37-2)
				self.questListContentCarv.SetPosition(15+3,y+37-2)
				self.questListContentCarv.Show()
				y = y + 159 + 5 + 2 + 37
			else:
				y = y + 39
		
	def FollowQuest(self):
		constInfo.INPUT_CMD = str(self.questDialog.BUTTON_TYPE_FOLLOW) + "/"
		event.QuestButtonClick(self.questContent[self.questCategory][self.questCurrent][self.QUEST_DATA_QUESTINDEX])
		
	def AbortQuest(self):
		constInfo.INPUT_CMD = str(self.questDialog.BUTTON_TYPE_DECLINE) + "/"
		event.QuestButtonClick(self.questContent[self.questCategory][self.questCurrent][self.QUEST_DATA_QUESTINDEX])
		
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.QuestPaper.questListScrollBar.OnUp()
		else:
			self.QuestPaper.questListScrollBar.OnDown()	
			
class QuestView(ui.ScriptWindow):

	QUEST_VIEW_INDEX = 0
	QUEST_VIEW_TITLE = 1
	QUEST_VIEW_OBJECTIVE = 2
	
	QUEST_OBJECTIVE_TYPE = 0
	QUEST_OBJECTIVE_VNUM = 1
	QUEST_OBJECTIVE_MIN_COUNT = 2
	QUEST_OBJECTIVE_MAX_COUNT = 3
	QUEST_OBJECTIVE_STATUS = 4
	QUEST_OBJECTIVE_ITEM = 5
	
	QUEST_STATUS_NOT_STARTED = 0
	QUEST_STATUS_IN_PROGRESS = 1
	QUEST_STATUS_FINISHED = 2
	
	TARGET_TYPE_KILL = 0
	TARGET_TYPE_TALK = 1
	TARGET_TYPE_COLLECT = 2
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.questViewList = []
		self.minimize = True
		self.userMinimize = False
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/questviewboard.py")
		except:
			import exception
			exception.Abort("QuestIntroBoard.LoadWindow.LoadObject")
		self.SetPosition(wndMgr.GetScreenWidth()-23,230)
		self.questViewListBox = self.GetChild("QuestViewListBox")
		self.questViewButton = self.GetChild("QuestIcon")
		self.questViewNoQuest = self.GetChild("NoQuestsTextLine")
		self.questViewNoQuest.Hide()
		self.questViewButton.SetEvent(self.ToggleQuestView)
	
	def MinimizeQuestView(self):
		self.SetPosition(wndMgr.GetScreenWidth()-23,230)
		self.minimize = True
		self.userMinimize = True
		self.Clear()
	
	def MaximizeQuestView(self):
		self.SetPosition(wndMgr.GetScreenWidth()-210,230)
		self.minimize = False
		self.userMinimize = False
		self.BuildQuestView()
		
	def ForceMinimize(self):
		self.SetPosition(wndMgr.GetScreenWidth()-23,230)
		self.Clear()
		
	def ToggleQuestView(self):
		if self.minimize:
			if len(self.questViewList) <= 0:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Du folgst keinen Quests.")
				return
			self.MaximizeQuestView()
		else:
			self.MinimizeQuestView()
	
	def BuildQuestView(self):
		# if self.minimize:
			# return
		if len(self.questViewList) <= 0:
			self.SetPosition(wndMgr.GetScreenWidth()-23,230)
			self.minimize = True
			return
		else:
			if self.minimize and not self.userMinimize:
				self.minimize = False
				self.SetPosition(wndMgr.GetScreenWidth()-210,230)
			# self.questViewButton.Enable()
			self.SetPosition(wndMgr.GetScreenWidth()-210,230)
			for i in xrange(len(self.questViewList)):
				
				questTitle		= self.questViewList[i][self.QUEST_VIEW_TITLE]
				questObjective	= self.questViewList[i][self.QUEST_VIEW_OBJECTIVE]
				
				self.questViewListBox.InsertQuestViewTitle(questinfo.GetQuestString(questTitle))
				
				for b in xrange(len(questObjective)):
					type		= questObjective[b][self.QUEST_OBJECTIVE_TYPE]
					vnum		= questObjective[b][self.QUEST_OBJECTIVE_VNUM]
					min_count	= questObjective[b][self.QUEST_OBJECTIVE_MIN_COUNT]
					max_count	= questObjective[b][self.QUEST_OBJECTIVE_MAX_COUNT]
					# status		= questObjective[b][self.QUEST_OBJECTIVE_STATUS]

					# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"QUESTVIEW: type : " + str(type))
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"QUESTVIEW: vnum : " + str(vnum))
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"QUESTVIEW: min_count : " + str(min_count))
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"QUESTVIEW: max_count : " + str(max_count))					
				
					if type == self.TARGET_TYPE_KILL:
						string = str(min_count) + " / " + str(max_count) + " " + str(nonplayer.GetMonsterName(vnum)) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_KILL
					elif type == self.TARGET_TYPE_TALK:
						string = localeInfo.QUEST_INTRO_OBJECTIVE_TALK + " " + nonplayer.GetMonsterName(vnum) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_TALK2
					elif type == self.TARGET_TYPE_COLLECT:
						item.SelectItem(vnum)
						string = str(min_count) + " / " + str(max_count) + " " + str(item.GetItemName()) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_COLLECT
					else:
						if max_count > 0:
							string = str(min_count) + " / " + str(max_count) + " " + questinfo.GetQuestString(vnum)
						else:
							string = questinfo.GetQuestString(vnum)
				
					index = self.questViewListBox.InsertObjectiveItem(string,self.StatusToQuestViewStatus(type,min_count,max_count))
					self.questViewList[i][self.QUEST_VIEW_OBJECTIVE][b][self.QUEST_OBJECTIVE_ITEM] = index
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"QUESTVIEW: index : " + str(index))
				self.questViewListBox.InsertEmptyItem()
				
	def Clear(self):
		self.questViewListBox.ClearItem()
		
	def Refresh(self):
		self.Clear()
		self.BuildQuestView()
		
	def AppendQuestView(self,qid,title):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestView Count BEFORE: " + str(len(self.questViewList)))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestView QID: " + str(qid))
	
	
		questView = {
			self.QUEST_VIEW_INDEX 		: int(qid),
			self.QUEST_VIEW_TITLE 		: title,
			self.QUEST_VIEW_OBJECTIVE	: [],
		}
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestView QID: " + str(qid))
	
		self.questViewList.append(questView)
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestView Count AFTER: " + str(len(self.questViewList)))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestView Count TEST: " + str(self.questViewList))
		# self.Clear()
		# self.BuildQuestView()		
		
		
	def AppendQuestViewObjective(self,qid,type,vnum,min_count,max_count):#,status):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestViewObjective: START!")
		quest = self.FindQuestViewItemByQID(qid)
		if quest < 0:
			# chat.AppendChat(chat.CHAT_TYPE_NOTICE,"AppendQuestViewObjective: Keine Quest mit ID " + str(qid) + " in QuestView gefunden!")
			return
			
		objective = {
			self.QUEST_OBJECTIVE_TYPE		: int(type),
			self.QUEST_OBJECTIVE_VNUM		: int(vnum),
			self.QUEST_OBJECTIVE_MIN_COUNT	: int(min_count),
			self.QUEST_OBJECTIVE_MAX_COUNT	: int(max_count),
			self.QUEST_OBJECTIVE_ITEM		: -1,
			# self.QUEST_OBJECTIVE_STATUS		: status,
		}
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestViewObjective Count BEFORE: " + str(len(self.questViewList[quest][self.QUEST_VIEW_OBJECTIVE])))
		self.questViewList[quest][self.QUEST_VIEW_OBJECTIVE].append(objective)
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestViewObjective Count AFTER: " + str(len(self.questViewList[quest][self.QUEST_VIEW_OBJECTIVE])))
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"AppendQuestViewObjective: END!")
		
		
	def UpdateQuestViewObjective(self,qid,index,min_count,max_count):#,status):
		quest = self.FindQuestViewItemByQID(qid)
		if quest < 0:
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"UpdateQuestViewObjective: Keine Quest mit ID " + str(qid) + " in QuestView gefunden!")
			return		

		self.questViewList[quest][self.QUEST_VIEW_OBJECTIVE][index][self.QUEST_OBJECTIVE_MIN_COUNT] = min_count
		self.questViewList[quest][self.QUEST_VIEW_OBJECTIVE][index][self.QUEST_OBJECTIVE_MAX_COUNT] = max_count
		# self.questViewList[quest][self.QUEST_VIEW_OBJECTIVE][index][self.QUEST_OBJECTIVE_STATUS] = status

		questObjective = self.questViewList[quest][self.QUEST_VIEW_OBJECTIVE]
				
		type		= questObjective[index][self.QUEST_OBJECTIVE_TYPE]
		vnum		= questObjective[index][self.QUEST_OBJECTIVE_VNUM]
		min_count	= questObjective[index][self.QUEST_OBJECTIVE_MIN_COUNT]
		max_count	= questObjective[index][self.QUEST_OBJECTIVE_MAX_COUNT]
		# status		= questObjective[index][self.QUEST_OBJECTIVE_STATUS]
		list_index	= questObjective[index][self.QUEST_OBJECTIVE_ITEM]
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"questObjective: type : " + str(type))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"questObjective: vnum : " + str(vnum))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"questObjective: min_count : " + str(min_count))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"questObjective: max_count : " + str(max_count))
					
		if type == self.TARGET_TYPE_KILL:
			string = str(min_count) + " / " + str(max_count) + " " + str(nonplayer.GetMonsterName(vnum)) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_KILL
		elif type == self.TARGET_TYPE_TALK:
			string = localeInfo.QUEST_INTRO_OBJECTIVE_TALK + " " + nonplayer.GetMonsterName(vnum) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_TALK2
		elif type == self.TARGET_TYPE_COLLECT:
			item.SelectItem(vnum)
			string = str(min_count) + " / " + str(max_count) + " " + str(item.GetItemName()) + " " + localeInfo.QUEST_INTRO_OBJECTIVE_COLLECT
		else:
			if max_count > 0:
				string = str(min_count) + " / " + str(max_count) + " " + questinfo.GetQuestString(vnum)
			else:
				string = questinfo.GetQuestString(vnum)
		
		if list_index >= 0:
			self.questViewListBox.ChangeObjectiveItem(list_index,string,self.StatusToQuestViewStatus(type,min_count,max_count))
	
	def RemoveQuestViewItem(self,qid):
		quest = self.FindQuestViewItemByQID(qid)
		if quest < 0:
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"RemoveQuestViewItem: Keine Quest mit ID " + str(qid) + " in QuestView gefunden!")
			return	
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Quest " + str(quest) + " wurde aus QuestView gelöscht!")
		
		del self.questViewList[quest]
		# self.Clear()
		# self.BuildQuestView()
		
	def StatusToQuestViewStatus(self,type,count_min,count_max):
		if type == self.TARGET_TYPE_KILL:
			if count_min > 0:
				if count_min < count_max:
					return self.QUEST_STATUS_IN_PROGRESS
				
				return self.QUEST_STATUS_FINISHED
		
			return self.QUEST_STATUS_NOT_STARTED
		else:
			return self.QUEST_STATUS_IN_PROGRESS
				
		
	def FindQuestViewItemByQID(self,qid):
		for i in xrange(len(self.questViewList)):
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"FindQuestViewItemByQID CHECK: " + str(self.questViewList[i][self.QUEST_VIEW_INDEX]) + " == " + str(qid))
			if self.questViewList[i][self.QUEST_VIEW_INDEX] == qid:
				return i
		
		return -1
	
	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
			
	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.__del__()	

class QuestMaker(ui.ScriptWindow):

	SYSTEM_INDEX = 0

	STATE_WINDOW_INIT = 0
	STATE_WINDOW_INTRO = 1
	# STATE_WINDOW_KILL = 2
	# STATE_WINDOW_DIALOG = 3
	# STATE_WINDOW_DROP = 4
	# STATE_WINDOW_COLLECT = 5
	# STATE_WINDOW_REWARD = 6
	
	QUEST_TAB_MAIN = 0
	QUEST_TAB_SIDE = 1
	QUEST_TAB_DUNGEON = 2
	QUEST_TAB_EVENT = 3
	QUEST_TAB_CHALLENGE = 4
	
	STATUS_MESSAGE_TIME_MESSAGE_SHOW = 3
	STATUS_MESSAGE_TIMER = 0
	STATUS_MESSAGE_DEFAULT_TEXT = "Bereit!"
	STATUS_MESSAGE_COLOR_NORMAL = 1
	STATUS_MESSAGE_COLOR_POSITIVE = 2
	STATUS_MESSAGE_COLOR_NEGATIVE = 3
	
	max_line = 28

	def __init__(self,systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.myQuest = []
		self.stateSelect = 0
		self.stateType = 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/questmaker.py")
		except:
			import exception
			exception.Abort("QuestMakerWindow.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)

		self.newQuestButton = self.GetChild("NewButton")
		self.newQuestButton.SetEvent(self.ShowMakeNewQuestDialog)
		self.makeQuestButton = self.GetChild("MakeButton")
		self.statusMessage = self.GetChild("statusMessage")
		self.stateListBox = self.GetChild("stateListBox")
		self.stateListBox.SetEvent(ui.__mem_func__(self.OnSelectState))
		self.stateScrollBar = self.GetChild("scrollBar")
		self.stateAddButton = self.GetChild("AddStateButton")
		self.stateAddButton.SetEvent(self.OpenStateMakeDialog)

		self.stateDelButton = self.GetChild("DeleteStateButton")
		self.stateDelButton.SetEvent(self.DeletateState)
		
		## STATE_WINDOW_DICT
		self.stateWindowDict = {}
		self.stateWindowDict[self.STATE_WINDOW_INIT] = self.GetChild("stateTypeINITWindow")
		self.stateWindowDict[self.STATE_WINDOW_INTRO] = self.GetChild("stateTypeINTROWindow")
		
		
		
		# stateTypeINTROWindow
		# STATE_WINDOW_INIT = 0
		# STATE_WINDOW_INTRO = 1
		# STATE_WINDOW_KILL = 2
		# STATE_WINDOW_DIALOG = 3

		
		## INIT WINDOWS
		self.InitStatePickDialog()
		self.InitNewQuestDialog()
		self.InitStateInitWindow()
		
		## Final Initialisation
		self.InitGUI()
		
		
	def InitNewQuestDialog(self):
		self.newQuestBackground = self.GetChild("makeNewQuestBackground")
		self.newQuestNewButton = self.GetChild("makeNewQuestYESButton")
		self.newQuestCloseButton = self.GetChild("makeNewQuestNOButton")
		self.newQuestBackground.Hide()
		
		self.newQuestNewButton.SetEvent(self.MakeNewQuest)
		self.newQuestCloseButton.SetEvent(self.CloseMakeNewQuestDialog)		
	
	def InitStatePickDialog(self):
		self.statePickDialog = self.GetChild("stateSelectBackground")
		self.stateNameEditLine = self.GetChild("statePickNameEditLine")
		self.statePickListBox = self.GetChild("statePickListBox")
		self.statePickAddButton = self.GetChild("statepick_add")
		self.statePickCloseButton = self.GetChild("statepick_close")
		self.statePickDialog.Hide()
		
		self.statePickAddButton.SetEvent(self.MakeState)
		self.statePickCloseButton.SetEvent(self.CloseStateMakeDialog)
		
		self.questTypes = [
			["INTRO",self.STATE_WINDOW_INTRO],
		]
		for i in xrange(len(self.questTypes)):
			self.statePickListBox.InsertItem(self.questTypes[i][1],self.questTypes[i][0])	
	
	
	
	###############################
	## STATE_WINDOW_INIT!
	
	def InitStateInitWindow(self):
		## BIND
		self.stateWindow_INIT_minLevel_EditLine = self.GetChild("stateTypeINITMinLevelEditLine")
		self.stateWindow_INIT_maxLevel_EditLine = self.GetChild("stateTypeINITMaxLevelEditLine")
		
		self.stateWindow_INIT_Job_ButtonDict = {}
		self.stateWindow_INIT_Job_ButtonDict[0] = self.GetChild("stateTypeINITJobSelectAllButton")
		self.stateWindow_INIT_Job_ButtonDict[1] = self.GetChild("stateTypeINITJobSelectWarriorButton")
		self.stateWindow_INIT_Job_ButtonDict[2] = self.GetChild("stateTypeINITJobSelectNinjaButton")
		self.stateWindow_INIT_Job_ButtonDict[3] = self.GetChild("stateTypeINITJobSelectSuraButton")
		self.stateWindow_INIT_Job_ButtonDict[4] = self.GetChild("stateTypeINITJobSelectShamanButton")
		
		self.stateWindow_INIT_Sex_ButtonDict = {}
		self.stateWindow_INIT_Sex_ButtonDict[0] = self.GetChild("stateTypeINITSexSelectAllButton")
		self.stateWindow_INIT_Sex_ButtonDict[1] = self.GetChild("stateTypeINITSexSelectMaleButton")
		self.stateWindow_INIT_Sex_ButtonDict[2] = self.GetChild("stateTypeINITSexSelectFemaleButton")	
		
		self.stateWindow_INIT_eventFlagName_EditLine = self.GetChild("stateTypeINITEventFlagEditLine")
		self.stateWindow_INIT_eventFlagValue_EditLine = self.GetChild("stateTypeINITEventFlagEditLineValue")

		self.stateWindow_INIT_questFlagQuestName_EditLine = self.GetChild("stateTypeINITQuestFlagQuestEditLine")
		self.stateWindow_INIT_questFlagName_EditLine = self.GetChild("stateTypeINITQuestFlagFlagEditLine")
		self.stateWindow_INIT_questFlagValue_EditLine = self.GetChild("stateTypeINITQuestFlagEditLineValue")		

		self.stateWindow_INIT_otherQuestProgressName_EditLine = self.GetChild("stateTypeINITOtherQuestProgressEditLine")
		self.stateWindow_INIT_otherQuestProgressValue_EditLine = self.GetChild("stateTypeINITOtherQuestProgressEditLineValue")
		
		self.stateWindow_INIT_otherQuestDone_EditLine = self.GetChild("stateTypeINITCheckOtherQuestDoneEditLine")
		
		self.stateWindow_INIT_SaveButton = self.GetChild("stateTypeINITSaveButton")
		
		## VARs
		self.stateWindow_INIT_Job_ALL = 0
		self.stateWindow_INIT_Job_WARRIOR = 1
		self.stateWindow_INIT_Job_NINJA = 2
		self.stateWindow_INIT_Job_SURA = 3
		self.stateWindow_INIT_Job_SHAMAN = 4
		
		self.stateWindow_INIT_Sex_ALL = 0
		self.stateWindow_INIT_Sex_MALE = 1
		self.stateWindow_INIT_Sex_FEMALE = 2
		
		self.stateWindow_INIT_Job_Select = [self.stateWindow_INIT_Job_ALL]	# <- ALL
		self.stateWindow_INIT_Sex_Select = [self.stateWindow_INIT_Sex_ALL]	# <- ALL	

		## FUNCTION
		
		self.stateWindow_INIT_Job_ButtonDict[0].SetEvent(self.SW_INIT_Job_ButtonClick,self.stateWindow_INIT_Job_ALL)
		self.stateWindow_INIT_Job_ButtonDict[1].SetEvent(self.SW_INIT_Job_ButtonClick,self.stateWindow_INIT_Job_WARRIOR)
		self.stateWindow_INIT_Job_ButtonDict[2].SetEvent(self.SW_INIT_Job_ButtonClick,self.stateWindow_INIT_Job_NINJA)
		self.stateWindow_INIT_Job_ButtonDict[3].SetEvent(self.SW_INIT_Job_ButtonClick,self.stateWindow_INIT_Job_SURA)
		self.stateWindow_INIT_Job_ButtonDict[4].SetEvent(self.SW_INIT_Job_ButtonClick,self.stateWindow_INIT_Job_SHAMAN)
		self.SW_INIT_Job_ButtonClick(self.stateWindow_INIT_Job_ALL)

		self.stateWindow_INIT_Sex_ButtonDict[0].SetEvent(self.SW_INIT_Sex_ButtonClick,self.stateWindow_INIT_Sex_ALL)
		self.stateWindow_INIT_Sex_ButtonDict[1].SetEvent(self.SW_INIT_Sex_ButtonClick,self.stateWindow_INIT_Sex_MALE)
		self.stateWindow_INIT_Sex_ButtonDict[2].SetEvent(self.SW_INIT_Sex_ButtonClick,self.stateWindow_INIT_Sex_FEMALE)
		self.SW_INIT_Sex_ButtonClick(self.stateWindow_INIT_Sex_ALL)
		
		self.stateWindow_INIT_SaveButton.SetEvent(self.SW_INIT_SaveData)


			# "state_name"			: "INITIALIZER",
			# "min_level"				: 0,
			# "max_level"				: 135,
			# "job"					: [self.stateWindow_INIT_Job_ALL],
			# "sex"					: [self.stateWindow_INIT_Sex_ALL],
			# "eventflag"				: ["no_flag",0],
			# "questflag"				: ["no_quest","no_flag",0],
			# "other_quest_progress"  : ["no_quest",0],
			# "other_quest_done" 		: ["no_quest"],
			
			# "deletable"				: False,
			# "window_id"				: self.STATE_WINDOW_INIT,	
	def SW_INIT_LoadData(self,data):
		self.AppendStatusMessage("State " + data["state_name"] + " wird geladen...",self.STATUS_MESSAGE_COLOR_NORMAL,15)
		self.stateWindow_INIT_minLevel_EditLine.SetText(str(data["min_level"]))
		self.stateWindow_INIT_maxLevel_EditLine.SetText(str(data["max_level"]))	

		self.stateWindow_INIT_Job_Select = data["job"]
		for i in xrange(len(self.stateWindow_INIT_Job_ButtonDict)):
			self.stateWindow_INIT_Job_ButtonDict[i].Enable()
		
		for i in xrange(len(self.stateWindow_INIT_Job_Select)):
			index = self.stateWindow_INIT_Job_Select[i]
			self.stateWindow_INIT_Job_ButtonDict[index].Disable()
		
		self.stateWindow_INIT_Sex_Select = data["sex"]
		for i in xrange(len(self.stateWindow_INIT_Sex_ButtonDict)):
			self.stateWindow_INIT_Sex_ButtonDict[i].Enable()
		
		for i in xrange(len(self.stateWindow_INIT_Sex_Select)):
			index = self.stateWindow_INIT_Sex_Select[i]
			self.stateWindow_INIT_Sex_ButtonDict[index].Disable()

		self.stateWindow_INIT_eventFlagName_EditLine.SetText(data["eventflag"][0])
		self.stateWindow_INIT_eventFlagValue_EditLine.SetText(data["eventflag"][1])

		self.stateWindow_INIT_questFlagQuestName_EditLine.SetText(data["questflag"][0])
		self.stateWindow_INIT_questFlagName_EditLine.SetText(data["questflag"][1])
		self.stateWindow_INIT_questFlagValue_EditLine.SetText(data["questflag"][2])

		self.stateWindow_INIT_otherQuestProgressName_EditLine.SetText(data["other_quest_progress"][0])
		self.stateWindow_INIT_otherQuestProgressValue_EditLine.SetText(data["other_quest_progress"][1])
		
		self.stateWindow_INIT_otherQuestDone_EditLine.SetText(data["other_quest_done"][0])		

		self.AppendStatusMessage("State " + data["state_name"] + " wurde erfolgreich geladen!",self.STATUS_MESSAGE_COLOR_POSITIVE)	
	
	def SW_INIT_SaveData(self):
		stateIndex = self.stateSelect

		self.myQuest[stateIndex]["min_level"] = self.stateWindow_INIT_minLevel_EditLine.GetText()
		self.myQuest[stateIndex]["max_level"] = self.stateWindow_INIT_maxLevel_EditLine.GetText()
		
		self.myQuest[stateIndex]["job"] = self.stateWindow_INIT_Job_Select
		self.myQuest[stateIndex]["sex"] = self.stateWindow_INIT_Sex_Select
		
		self.myQuest[stateIndex]["eventflag"] = [
			self.stateWindow_INIT_eventFlagName_EditLine.GetText(),
			self.stateWindow_INIT_eventFlagValue_EditLine.GetText()		
		]
		
		self.myQuest[stateIndex]["questflag"] = [
			self.stateWindow_INIT_questFlagQuestName_EditLine.GetText(),
			self.stateWindow_INIT_questFlagName_EditLine.GetText(),
			self.stateWindow_INIT_questFlagValue_EditLine.GetText()		
		]
		
		self.myQuest[stateIndex]["other_quest_progress"] = [
			self.stateWindow_INIT_otherQuestProgressName_EditLine.GetText(),
			self.stateWindow_INIT_otherQuestProgressValue_EditLine.GetText()		
		]
		
		self.myQuest[stateIndex]["other_quest_done"] = [
			self.stateWindow_INIT_otherQuestDone_EditLine.GetText()
		]
		
		self.AppendStatusMessage("Daten gespeichert!",self.STATUS_MESSAGE_COLOR_POSITIVE)
	
	
	def SW_INIT_Job_ButtonClick(self,job):
		if job == self.stateWindow_INIT_Job_ALL:
			self.stateWindow_INIT_Job_Select = [self.stateWindow_INIT_Job_ALL]
		else:
			if self.stateWindow_INIT_Job_Select[0] == self.stateWindow_INIT_Job_ALL:
				self.stateWindow_INIT_Job_Select = []
				
			self.stateWindow_INIT_Job_Select.append(job)
		
		for i in xrange(len(self.stateWindow_INIT_Job_ButtonDict)):
			self.stateWindow_INIT_Job_ButtonDict[i].Enable()
		
		for i in xrange(len(self.stateWindow_INIT_Job_Select)):
			index = self.stateWindow_INIT_Job_Select[i]
			self.stateWindow_INIT_Job_ButtonDict[index].Disable()

	def SW_INIT_Sex_ButtonClick(self,job):
		if job == self.stateWindow_INIT_Sex_ALL:
			self.stateWindow_INIT_Sex_Select = [self.stateWindow_INIT_Sex_ALL]
		else:
			if self.stateWindow_INIT_Sex_Select[0] == self.stateWindow_INIT_Sex_ALL:
				self.stateWindow_INIT_Sex_Select = []
				
			self.stateWindow_INIT_Sex_Select.append(job)
		
		for i in xrange(len(self.stateWindow_INIT_Sex_ButtonDict)):
			self.stateWindow_INIT_Sex_ButtonDict[i].Enable()
		
		for i in xrange(len(self.stateWindow_INIT_Sex_Select)):
			index = self.stateWindow_INIT_Sex_Select[i]
			self.stateWindow_INIT_Sex_ButtonDict[index].Disable()			
				
			
		
	###############################
	def InitGUI(self):
		self.makeQuestButton.Disable()
		self.stateAddButton.Disable()
		self.stateDelButton.Disable()
		for i in xrange(len(self.stateWindowDict)):
			self.stateWindowDict[i].Hide()
			
		self.newQuestButton.Flash()
	
	def InitQuest(self):
		self.AppendInitState()
		self.BuildStateList()

		self.stateAddButton.Enable()
		self.stateDelButton.Enable()	
	
	## MAKE_NEW_QUEST_FUNCTION
	def ShowMakeNewQuestDialog(self):
		if len(self.myQuest) > 0:
			self.newQuestBackground.Show()
		else:
			self.InitQuest()
			
	def MakeNewQuest(self):
		self.InitQuest()	
		
	def CloseMakeNewQuestDialog(self):
		self.newQuestBackground.Hide()
		
		
	#####################################	
		
		
	def OnSelectState(self):
		item = self.stateListBox.GetSelectedItem()
		self.LoadStateWindow(item)
		
	def LoadStateWindow(self,item):
		self.stateWindowDict[self.stateType].Hide()
		self.stateSelect = item
		self.stateType = self.myQuest[item]["window_id"]
		self.stateWindowDict[self.stateType].Show()
		
		if self.stateType == self.STATE_WINDOW_INIT:
			self.SW_INIT_LoadData(self.myQuest[item])
		
		if self.myQuest[item]["deletable"]:
			self.stateDelButton.Enable()
		else:
			self.stateDelButton.Disable()
	
	def OpenStateMakeDialog(self):
		self.stateNameEditLine.SetText("")
		self.statePickDialog.Show()
	
	def CloseStateMakeDialog(self):
		self.statePickDialog.Hide()
		
	def MakeState(self):
		self.CloseStateMakeDialog()
		state = self.statePickListBox.GetSelectedItem()
		
		if state == self.STATE_WINDOW_INTRO:
			self.AppendIntroState(self.stateNameEditLine.GetText())
		
		# elif state == self.QUEST_TYPE_DIALOG:
			# self.AppendDialogState(self.stateNameEditLine.GetText())
		
		else:
			self.AppendStatusMessage(str(state) + " ist kein gültiger QuestType!",self.STATUS_MESSAGE_COLOR_NEGATIVE)
			return
			
		self.BuildStateList()
		
	def DeletateState(self):
		state = self.stateListBox.GetSelectedItem()
		
		del self.myQuest[state]
		self.BuildStateList()
		self.stateDelButton.Disable()
		for i in xrange(len(self.stateWindowDict)):
			self.stateWindowDict[i].Hide()
			
	def BuildStateList(self):
		self.stateScrollBar.Hide()
		self.ClearStateList()
		for i in xrange(len(self.myQuest)):
			stateName = self.myQuest[i]["state_name"]
			self.stateListBox.InsertItem(i,stateName)
			
		if len(self.myQuest) > self.max_line:
			self.stateScrollBar.Show()
		
	def ClearStateList(self):
		self.stateListBox.ClearItem()
	
	
	###########################################
	###########################################
	###########################################
	###########################################
	###########################################
	## STATE STRUCTURES!
	
	def AppendInitState(self):
		newState = {
			"state_name"			: "INITIALIZER",
			"min_level"				: 1,
			"max_level"				: 135,
			"job"					: [self.stateWindow_INIT_Job_ALL],
			"sex"					: [self.stateWindow_INIT_Sex_ALL],
			"eventflag"				: ["no_flag",0],
			"questflag"				: ["no_quest","no_flag",0],
			"other_quest_progress"  : ["no_quest",0],
			"other_quest_done" 		: ["no_quest"],
			
			"deletable"				: False,
			"window_id"				: self.STATE_WINDOW_INIT,
		}
		self.myQuest.append(newState)	
		self.AppendStatusMessage("INITIALIZER wurde erfolgreich erstellt!",self.STATUS_MESSAGE_COLOR_POSITIVE)
	
	def AppendIntroState(self,name="intro"):
		newState = {
			"state_name"			: name + " (INTRO)",
			"tab"					: self.QUEST_TAB_MAIN,
			"target"				: 0,
			"letter"				: [0,0],
			
			"dialog"				: [0,0],
			"dialog_target"			: [],
			
			"show_reward"			: False,
			"can_decline"			: True,
			"can_follow"  			: True,
			"init_follow" 			: False,
			
			"deletable"				: True,
			"window_id"				: self.STATE_WINDOW_INTRO,
		}
		self.myQuest.append(newState)	
		self.AppendStatusMessage(name + " wurde erfolgreich erstellt!",self.STATUS_MESSAGE_COLOR_POSITIVE)
	
	###########################################
	###########################################
	###########################################
	###########################################
	###########################################
	###########################################
	
	
	# STATUS_MESSAGE_TIME_MESSAGE_SHOW = 3
	# STATUS_MESSAGE_TIMER = 0
	# STATUS_MESSAGE_DEFAULT_TEXT = "Bereit!"
	# STATUS_MESSAGE_COLOR_NORMAL = 1
	# STATUS_MESSAGE_COLOR_POSITIVE = 2
	# STATUS_MESSAGE_COLOR_NEGATIVE = 3
	
	def AppendStatusMessage(self,text,color,time=STATUS_MESSAGE_TIME_MESSAGE_SHOW):
		self.STATUS_MESSAGE_TIMER = app.GetTime() + time
		self.statusMessage.SetText(str(text))
		if color == self.STATUS_MESSAGE_COLOR_NORMAL:
			self.statusMessage.SetFontColor(1.0, 1.0, 1.0)
		elif color == self.STATUS_MESSAGE_COLOR_POSITIVE:
			self.statusMessage.SetFontColor(0.5411, 0.7254, 0.5568)
		elif color == self.STATUS_MESSAGE_COLOR_NEGATIVE:
			self.statusMessage.SetFontColor(0.9, 0.4745, 0.4627)

	def UpdateStatusMessage(self):
		if self.STATUS_MESSAGE_TIMER > 0:
			if self.STATUS_MESSAGE_TIMER < app.GetTime():
				self.STATUS_MESSAGE_TIMER = 0
				self.statusMessage.SetText(self.STATUS_MESSAGE_DEFAULT_TEXT)
				self.statusMessage.SetFontColor(1.0, 1.0, 1.0)
	
	def OnUpdate(self):
		self.UpdateStatusMessage()
	
	def OnRunMouseWheel(self, nLen):
		if nLen > 0:
			self.stateScrollBar.OnUp()
		else:
			self.stateScrollBar.OnDown()		
		
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
			
	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.__del__()
		
class QuestTextTool(ui.ScriptWindow):

	SYSTEM_INDEX = 0
	
	questText = []

	def __init__(self,systemIndex):
		ui.ScriptWindow.__init__(self)
		self.SYSTEM_INDEX = systemIndex
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/questtexttool.py")
		except:
			import exception
			exception.Abort("QuestTextTool.LoadWindow.LoadObject")
		
		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		self.board = self.GetChild("board")
		self.addButton = self.GetChild("addTextButton")
		self.saveButton = self.GetChild("SaveButton")
		self.clearAllButton = self.GetChild("ClearButton")
		self.clearLastButton = self.GetChild("BackButton")
		
		self.addButton.SetEvent(self.AddText)
		self.saveButton.SetEvent(self.SaveText)
		self.clearAllButton.SetEvent(self.ClearAll)
		self.clearLastButton.SetEvent(self.ClearLast)
		self.clearLastButton.Disable()
		self.editLine = self.GetChild("questText_EditLine")
		self.editLine.SetReturnEvent(self.AddText)
		self.QuestPaper = QuestPaper(self)
		self.QuestPaper.SetParent(self.board)
		self.QuestPaper.SetPosition(0,30)
		self.QuestPaper.Show()

		self.QuestPaper.SetTitle("This is just decorative Title. Part VII")
		self.QuestPaper.questListBox.InsertTitleItem(localeInfo.QUEST_INTRO_DESCRIPTION_TITLE)
		
	def AddText(self):
		text = self.editLine.GetText()
		if text == "":
			text = "[ENTER]"
		self.questText.append(text)
		self.editLine.SetText("")
		self.clearLastButton.Enable()
		self.Rebuild()

	def SaveText(self):
		saveString = ""
		for i in xrange(len(self.questText)):
			if self.questText[i] == "[ENTER]":
				saveString = saveString + "[ENTER]"
			else:
				saveString = saveString + self.questText[i] + "[ENTER]"

		fo = open("questtext.txt", "a")
		fo.write(saveString + "\n")
		fo.close()
		self.ClearAll()
		chat.AppendChat(chat.CHAT_TYPE_INFO,"Questext wurde in questtext.txt gespeichert. Du findest die Datei im Hauptverzeichnis.")
		
	def ClearAll(self):
		self.questText = []
		self.QuestPaper.Clear()
		self.QuestPaper.SetTitle("This is just decorative Title. Part VII")
		self.QuestPaper.questListBox.InsertTitleItem(localeInfo.QUEST_INTRO_DESCRIPTION_TITLE)
		self.clearLastButton.Disable()
		
	def ClearLast(self):
		index = len(self.questText) - 1
		del self.questText[index]
		self.Rebuild()
		
	def Rebuild(self):
		self.QuestPaper.Clear()
		self.QuestPaper.SetTitle("This is just decorative Title. Part VII")
		self.QuestPaper.questListBox.InsertTitleItem(localeInfo.QUEST_INTRO_DESCRIPTION_TITLE)
		for i in xrange(len(self.questText)):
			self.QuestPaper.questListBox.InsertDescItem(self.questText[i])
		
		if len(self.questText) == 0:
			self.clearLastButton.Disable()
		else:
			self.clearLastButton.Enable()
			
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
			
	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.__del__()			
		
		