import ui
import chat
import app
import fgGHGjjFHJghjfFG1545gGG
import snd
import item
import GFHhg54GHGhh45GHGH
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo
import questinfo
import exterminatus


class BiologistWindow(ui.ScriptWindow):

	STATE_RESEARCH_READY = 0
	STATE_RESEARCH_IN_PROGRESS = 1
	STATE_RESEARCH_COMPLETE = 2
	
	ITEM_COUNT = 5

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.biologistQuestDict = []
		self.questSelect = 0
		self.qid = 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/biologistwindow2.py")
		except:
			import exception
			exception.Abort("BiologistWindow.LoadWindow.LoadObject")

		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		# OVERVIEW
		self.QuestListWindow = self.GetChild("QuestListWindow")
		self.QuestListScrollBar = self.GetChild("QuestListScrollBar")
		self.QuestOverview = self.GetChild("QuestDescWindow")
		self.QuestDescriptionTitle = self.GetChild("QuestTitle")
		self.QuestDescriptionListBox = self.GetChild("QuestContentListBox")
		self.QuestDescriptionScrollBar = self.GetChild("scrollBar")
		self.QuestItemSlot = self.GetChild("itemSlot")
		
		self.QuestItemNameTextLine = self.GetChild("itemName")
		self.QuestCountTextLine = self.GetChild("itemCount")
		self.QuestResearchTimeTextLine = self.GetChild("researchTime")
		self.QuestChanceTextLine = self.GetChild("researchChance")

		self.ResearchInfoTextLine = self.GetChild("researchInfoTextLine")
		self.BackToQuestListButton = self.GetChild("BackToQuestListButton")
		self.StartResearchButton = self.GetChild("StartResearchButton")
		
		self.ResearchItemSlot = self.GetChild("targetItemSlot")
		self.AcceleratorItemSlot = self.GetChild("timeItemSlot")
		self.Addition = self.GetChild("chanceItemSlot")

		# QUEST_ITEM
		y = 1
		self.bioItemDict = {}
		for i in xrange(5):
			self.bioItemDict[i] = BiologistItem(self,i)
			self.bioItemDict[i].SetParent(self.QuestListWindow)
			self.bioItemDict[i].SetPosition(1,y)
			self.bioItemDict[i].Show()			
			
			y = y + 81
		
		# BIND_FUNCTION
		self.QuestListScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestListScroll))
		self.QuestDescriptionScrollBar.SetScrollEvent(ui.__mem_func__(self.OnDescScroll))
		self.BackToQuestListButton.SetEvent(self.CloseOverview)	
		
		self.QuestOverview.Hide()
		self.StartResearchButton.Disable()


		
		# ###########################
		# ## TODO: Entfernen!!!!		
		# for i in xrange(17):
			# self.AddBiologistQuest(i,(i+1) * 10,1,3,app.GetRandom(0,2),30000 + i,(i+1) * 10,(i+1)*2,90 - i)
		
		
		
		# self.bioItemDict[1].SetTimer(69)
		# self.OnQuestListScroll()
		# self.Show()
		# ###########################
		
	###############################################################################	
	###############################################################################
	## interfaceModule INPUT
	def AddBiologistQuest(self,id,level,title,desc,status,itemVnum,itemCount_MAX,baseResearchTime,baseResearchChance):
	
		quest = {
			
			"id" : int(id),
			"level" : int(level),
			"title" : int(title),
			"desc" : int(desc),
			
			"status" : int(status),
			
			"itemVnum" : int(itemVnum),
			"itemCount" : 0,
			"itemCount_MAX" : int(itemCount_MAX),
			
			"base_research_time" : int(baseResearchTime),
			"base_chance" : int(baseResearchChance),

			"time" : 0,
		}
		
		self.biologistQuestDict.append(quest)
		
	def UpdateBiologistQuest_ITEM_COUNT(self,index,count):
		self.biologistQuestDict[index]["itemCount"] = int(count)
		self.OnQuestListScroll()
		if index == self.questSelect:
			info = self.biologistQuestDict[index]
			self.QuestCountTextLine.SetText(str(count) + " / " + str(info["itemCount_MAX"]))

	def UpdateBiologistQuest_TIMER(self,index,timer):
		self.biologistQuestDict[index]["time"] = int(timer)
		self.OnQuestListScroll()
	
	
	def SetQuestIndex(self,qid):
		self.qid = int(qid)
		
		
	###############################################################################
	###############################################################################
	
	
	
	def OnClickBiologistItem(self,index):
		pos = int(self.QuestListScrollBar.GetPos() * (len(self.biologistQuestDict) - self.ITEM_COUNT)) + index 
		
	
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(pos))
		self.questSelect = pos
		self.ClearOverview()
		self.BuildOverview(pos)
		self.OpenOverview()
		
	def ClearOverview(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"ClearOverview:START")
		self.QuestDescriptionTitle.SetText("")
		self.QuestDescriptionListBox.ClearItem()
		self.QuestDescriptionScrollBar.Hide()

		self.QuestItemSlot.ClearSlot(0)
		self.QuestItemSlot.RefreshSlot()


		self.QuestItemNameTextLine.SetText("")
		self.QuestCountTextLine.SetText("")
		self.QuestResearchTimeTextLine.SetText("")
		self.QuestChanceTextLine.SetText("")


		self.ResearchInfoTextLine.SetText("")
		self.StartResearchButton.Disable()
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"ClearOverview:DONE")

	def BuildOverview(self,index):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"BuildOverview:START")
		info = self.biologistQuestDict[index]
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"info: " + str(len(info)))
		
		self.QuestDescriptionTitle.SetText(questinfo.GetQuestString(info["title"]))
		
		desc_idx = questinfo.GetQuestString(info["desc"])
		desc = desc_idx.split("[ENTER]")
		for i in xrange(len(desc)):
			self.QuestDescriptionListBox.InsertItem(i,desc[i])
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"BuildOverview:DESC DONE")
		
		
		self.QuestDescriptionScrollBar.Show()

		self.QuestItemSlot.SetItemSlot(0,info["itemVnum"],0)
		self.QuestItemSlot.RefreshSlot()
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"BuildOverview:SLOT DONE")
		
		item.SelectItem(info["itemVnum"])
		
		
		self.QuestItemNameTextLine.SetText(item.GetItemName())
		self.QuestCountTextLine.SetText(str(info["itemCount"]) + " / " + str(info["itemCount_MAX"]))
		self.QuestResearchTimeTextLine.SetText("Forschungszeit: " + exterminatus.SecondToDHMS(info["base_research_time"]))
		self.QuestChanceTextLine.SetText("Erfolgschance: " + str(info["base_chance"]) + "%") 
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"BuildOverview:INFO DONE")

		self.ResearchInfoTextLine.SetText("Bereit!")
		self.StartResearchButton.Disable()		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"BuildOverview:DONE")
	def OpenOverview(self):
		self.QuestOverview.Show()
		
	def CloseOverview(self):
		self.QuestOverview.Hide()
	
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
		
	def OnQuestListScroll(self):
		pos = int(self.QuestListScrollBar.GetPos() * (len(self.biologistQuestDict) - self.ITEM_COUNT)) 
		for i in xrange(self.ITEM_COUNT):
			realPos = i + pos
			info = self.biologistQuestDict[realPos]
			self.bioItemDict[i].SetItem(info["itemVnum"])
			self.bioItemDict[i].SetQuestTitle(questinfo.GetQuestString(info["title"]))
			self.bioItemDict[i].SetCount(info["itemCount"],info["itemCount_MAX"])
			self.bioItemDict[i].SetStatusColor(info["status"])
			self.bioItemDict[i].SetTimer(info["time"])

		
		
	def OnDescScroll(self):
		viewItemCount = self.QuestDescriptionListBox.GetViewItemCount()
		itemCount = self.QuestDescriptionListBox.GetItemCount()
		pos = self.QuestDescriptionScrollBar.GetPos() * (itemCount - viewItemCount)
		self.QuestDescriptionListBox.SetBasePos(int(pos))
		
	def OnRunMouseWheel(self, nLen):
		if self.QuestOverview.IsShow():
			if nLen > 0:
				self.QuestDescriptionScrollBar.OnUp()
			else:
				self.QuestDescriptionScrollBar.OnDown()
		
		else:
			if nLen > 0:
				self.QuestListScrollBar.OnUp()
			else:
				self.QuestListScrollBar.OnDown()			

		
class BiologistItem(ui.ScriptWindow):

	STATUS_INACTIVE = 0
	STATUS_ACTIVE = 1
	STATUS_COMPLETE = 2

	COLOR_INACTIVE = grp.GenerateColor(1.0, 0.0, 0.0, 0.2)
	COLOR_ACTIVE   = grp.GenerateColor(0.0, 1.0, 0.0, 0.2)
	COLOR_COMPLETE = grp.GenerateColor(0.5, 0.5, 0.5, 0.2)

	COLOR_INACTIVE_HOVER = grp.GenerateColor(1.0, 0.0, 0.0, 0.3)
	COLOR_ACTIVE_HOVER   = grp.GenerateColor(0.0, 1.0, 0.0, 0.3)
	COLOR_COMPLETE_HOVER = grp.GenerateColor(0.5, 0.5, 0.5, 0.3)
	
	def __init__(self, biologistWindow, index):
		ui.ScriptWindow.__init__(self)
		self.biologistWindow = biologistWindow
		self.index = index
		self.status = self.STATUS_INACTIVE
		self.itemVnum = 0
		self.itemCount = 0
		self.itemCountNeed = 0
		self.timer = 0
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/biologistitem.py")
		except:
			import exception
			exception.Abort("BiologistItem.LoadWindow.LoadObject")
			
		self.toolTip = uiToolTip.ItemToolTip()  
		self.toolTip.HideToolTip()	
		
		self.bar = self.GetChild("board")
		self.bar.SetOnClickEvent(self.OnItemClick)
		
		self.itemSlot = self.GetChild("itemSlot")
		self.itemSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))		
		
		self.questName = self.GetChild("questName")
		self.questTimer = self.GetChild("timer")
		self.questCount = self.GetChild("progress")
		self.questPercent = self.GetChild("progressPercent")
		
	
	def ShowToolTip(self,slot):
		if self.itemVnum == 0:
			return
			
		self.toolTip.ClearToolTip()
		self.toolTip.AddItemData(self.itemVnum, [0, 0, 0, 0, 0, 0])
		self.toolTip.ShowToolTip()		

	def HideToolTip(self):
		if self.itemVnum == 0:
			return
		self.toolTip.Hide()
	
	def SetStatusColor(self,index):
		self.status = index
		if index == self.STATUS_INACTIVE:
			self.bar.SetColor(self.COLOR_INACTIVE)
		
		elif index == self.STATUS_ACTIVE:
			self.bar.SetColor(self.COLOR_ACTIVE)
		
		elif index == self.STATUS_COMPLETE:
			self.bar.SetColor(self.COLOR_COMPLETE)
		
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"uibiologist.BiologistItem(): Unknown StatusIndex: " + str(index))
	
	
	def OnUpdate(self):
		if self.bar.IsIn():
			self.OnMouseOverIn()
		else:
			self.OnMouseOverOut()
			
		if self.timer > app.GetTime():
			# self.questTimer.SetText(localeInfo.SecondToDHMS(self.timer - app.GetTime()))
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"TIMER ACTIVE!")
			sek = self.timer - app.GetTime()
			self.questTimer.SetText(exterminatus.SecondToDHMS(sek))
		else:
			self.questTimer.SetText("Bereit!")	
			
			
	def OnMouseOverIn(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OnMouseOverIn")
		index = self.status  
		if index == self.STATUS_INACTIVE:
			self.bar.SetColor(self.COLOR_INACTIVE_HOVER)
		
		elif index == self.STATUS_ACTIVE:
			self.bar.SetColor(self.COLOR_ACTIVE_HOVER)
		
		elif index == self.STATUS_COMPLETE:
			self.bar.SetColor(self.COLOR_COMPLETE_HOVER)		
		
	def OnMouseOverOut(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OnMouseOverOut")
		index = self.status  
		if index == self.STATUS_INACTIVE:
			self.bar.SetColor(self.COLOR_INACTIVE)
		
		elif index == self.STATUS_ACTIVE:
			self.bar.SetColor(self.COLOR_ACTIVE)
		
		elif index == self.STATUS_COMPLETE:
			self.bar.SetColor(self.COLOR_COMPLETE)	
	
	def SetItem(self,itemVnum):
		self.itemVnum = int(itemVnum)
		self.itemSlot.SetItemSlot(0,itemVnum,0)
	
	def SetQuestTitle(self,index):
		self.questName.SetText(index)
		
	def SetTimer(self,timer):
		if timer == 0:
			self.timer = 0
		else:
			self.timer = int(app.GetTime() + timer)
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"timer: " + str(self.timer))
		# self.questTimer.SetText(str(timer))

	def SetCount(self,min,max):
		self.itemCount = int(min)
		self.itemCountNeed = int(max)

		self.questCount.SetText(str(min) + " / " + str(max))

		percent = (float(self.itemCount) / float(self.itemCountNeed)) * 100
		self.questPercent.SetText(str(int(percent)) + "%")
	
	def OnItemClick(self):
		snd.PlaySound("sound/ui/click.wav")
		self.biologistWindow.OnClickBiologistItem(self.index)

	def SetOnClickEvent(self,event):
		self.event = event

class BiologistWindow_OLD(ui.ScriptWindow):

	biologistLevel = 2
	biologistItemVnum = 30006
	biologistResearchTime = 30
	
	slotCount = 25
	
	itemCount = 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		#constInfo.CALOPEN = 1
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/biologistwindow.py")
		except:
			import exception
			exception.Abort("BiologistWindow.LoadWindow.LoadObject")

		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		self.SetCenterPosition()
		
		
		self.itemSlot = self.GetChild("ItemSlot")
		# self.itemSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)

		for i in xrange(self.slotCount):
			self.itemSlot.SetCoverButton(i,"d:/ymir work/ui/game/quest/slot_button_01.sub",\
											"d:/ymir work/ui/game/quest/slot_button_01.sub",\
											"d:/ymir work/ui/game/quest/slot_button_01.sub",\
											"d:/ymir work/ui/game/belt_inventory/slot_disabled.tga", FALSE, FALSE)	
			self.itemSlot.SetAlwaysRenderCoverButton(i, TRUE)
			self.itemSlot.DisableCoverButton(i)
		
		self.itemSlot.RefreshSlot()
		
		self.SetBaseLayout()
	
	def SetBaseLayout(self):
		self.itemCount = 0
		for i in xrange(self.slotCount):
			if i < self.biologistLevel:
				self.itemSlot.EnableCoverButton(i)
				
				item.SelectItem(self.biologistItemVnum)
				itemIcon = item.GetIconImage()
				(width, height) = item.GetItemSize()
				self.itemSlot.SetSlot(i, 0, width, height, itemIcon, (1.0, 1.0, 1.0, 0.5))
				self.itemSlot.SetSlotCount(i, 0)				

			else:
				self.itemSlot.DisableCoverButton(i)

		self.itemSlot.RefreshSlot()
	
	def AddItem(self,itemVnum):
		itemCount = itemCount + 1
		
	def DefineItemInfo(self,itemVnum):
		self.biologistItemVnum = int(itemVnum)
		
	def DefineBiologistLevel(self,level):
		self.biologistLevel = int(level)
	
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			if self.biologistLevel == 0:
				return
			
			
			self.SetBaseLayout()
			self.Show()
		
		
	def Close(self):
		self.Hide()

