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

def IsBiologistItem(vnum):
	itemList = [
		30006, # Orkzahn
		30047, # Fluchsammlung
		30015, # Dämonenandenken
		30050, # Eiskugel
		30165, # Holzast
		30166, # Tafel
		30167, # Roter Ast
		30168, # Notizen
		30184, # Verzauberte Asche
		30188, # Vulkanglas
		30177, # Juwel des Feuers
		30178, # Juwel des Eises
	]
	if vnum in itemList:
		return True
		
	return False

def IsBiologistAccelerator(vnum):
	itemList = [
		160474, # 25%
		160475, # 50%,
		160476, # 75%,
		160477, # 100%

	]
	if vnum in itemList:
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"IsAccelede")
		return True
		
	return False

def IsBiologistChanceItem(vnum):
	itemList = [
		160470, # 25%
		160471, # 50%,
		160472, # 75%,
		160473, # 100%

	]
	if vnum in itemList:
		return True
		
	return False

class BiologistWindow(ui.ScriptWindow):

	STATE_RESEARCH_READY = 0
	STATE_RESEARCH_IN_PROGRESS = 1
	STATE_RESEARCH_COMPLETE = 2

	STATUS_INACTIVE = 0
	STATUS_ACTIVE = 1
	STATUS_COMPLETE = 2
	
	SLOT_RESEARCH_ITEM = 0
	SLOT_ACCELERATOR_ITEM = 1
	SLOT_CHANCE_ITEM = 2
	
	ITEM_COUNT = 5

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.biologistQuestDict = []
		self.questSelect = -1
		self.qid = 0
		self.LoadWindow()
		self.slotData = [
			{ # ItemResearch
				"itemVnum" : 0,
				"itemPos" : 0,
			},
			{ # Accelerator
				"itemVnum" : 0,
				"itemPos" : 0,			
			},
			{ # Chance Item
				"itemVnum" : 0,
				"itemPos" : 0,			
			}
		]

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
		
		
		self.ResearchWindow = self.GetChild("researchWindow")
		self.ResearchInfoTextLine = self.GetChild("researchInfoTextLine")
		self.BackToQuestListButton = self.GetChild("BackToQuestListButton")
		self.StartResearchButton = self.GetChild("StartResearchButton")
		
		self.ResearchItemSlot = self.GetChild("targetItemSlot")
		self.AcceleratorItemSlot = self.GetChild("timeItemSlot")
		self.ChanceItemSlot = self.GetChild("chanceItemSlot")
		
		self.ResearchItemSlotBlockImage = self.GetChild("targetItemSlotBlockImage")
		self.AcceleratorItemSlotBlockImage = self.GetChild("timeItemSlotBlockImage")
		self.ChanceItemSlotBlockImage = self.GetChild("chanceItemSlotBlockImage")
		
		self.ResearchItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.AddItem))  
		self.ResearchItemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.DeleteItem))  
		self.AcceleratorItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.AddItem))  
		self.AcceleratorItemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.DeleteItem))  
		self.ChanceItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.AddItem))  
		self.ChanceItemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.DeleteItem))  

		self.ResearchItemSlotBlockImage.Hide()
		self.AcceleratorItemSlotBlockImage.Hide()
		self.ChanceItemSlotBlockImage.Hide()
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
		self.StartResearchButton.SetEvent(self.StartResearch)

		
		# ###########################
		# ## TODO: Entfernen!!!!		
		# for i in xrange(17):
			# self.AddBiologistQuest(i,(i+1) * 10,1,3,app.GetRandom(0,2),30000 + i,(i+1) * 10,(i+1)*2,90 - i)
		
		
		
		# self.bioItemDict[1].SetTimer(69)
		# self.OnQuestListScroll()
		# self.Show()
		# ###########################
	
	
	def StartResearch(self):
		if self.qid == 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Error: No QID!")
			return
		if self.questSelect < 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Error: questSelect < 0")
			return
		
		if self.slotData[0]["itemVnum"] == 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Error: No item")
			return
			
		if self.biologistQuestDict[self.questSelect]["time"] >= app.GetGlobalTimeStamp():
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Error: Timer Active!")
			return
		
		accelerateItem = "no"
		chanceItem = "no"
		
		if self.slotData[1]["itemVnum"]:
			accelerateItem = self.slotData[1]["itemPos"]
		
		if self.slotData[2]["itemVnum"]:
			chanceItem = self.slotData[2]["itemPos"]		
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "qid: " + str(self.qid))
		constInfo.INPUT_CMD = "research#" + str(self.slotData[0]["itemPos"]) + "#" + str(accelerateItem) + "#" + str(chanceItem) + "#"
		event.QuestButtonClick(self.qid)
		self.ClearSlotData()
	
	def AddItemPerClick(self,slot):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(slot))
		
		if self.questSelect < 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Öffne das Biologen Fenster um Items zu erforschen!")
			return
		
		itemVnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(slot)
		if self.biologistQuestDict[self.questSelect]["itemVnum"] == itemVnum:
			if self.slotData[0]["itemVnum"] == 0:
				self.slotData[0]["itemVnum"] = itemVnum
				self.slotData[0]["itemPos"] = slot
				self.ResearchItemSlot.SetItemSlot(0, itemVnum, 0)
				self.ResearchItemSlot.RefreshSlot()
				self.StartResearchButton.Enable()			
			
		elif IsBiologistAccelerator(itemVnum):
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "isBiologistAccItem!")
			if self.slotData[1]["itemVnum"] == 0:
				self.slotData[1]["itemVnum"] = itemVnum
				self.slotData[1]["itemPos"] = slot
				self.AcceleratorItemSlot.SetItemSlot(1, itemVnum, 0)
				self.AcceleratorItemSlot.RefreshSlot()	
				self.UpdateChanceAndTimerWithSpecialItem()
			else:
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "!= vnum")
				if self.slotData[1]["itemVnum"] != itemVnum:
					self.slotData[1]["itemVnum"] = 0
					self.slotData[1]["itemPos"] = 0
					self.AcceleratorItemSlot.SetItemSlot(1, 0, 0)
					self.AcceleratorItemSlot.ClearSlot(1)
					self.AcceleratorItemSlot.RefreshSlot()
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "clear")					
					self.slotData[1]["itemVnum"] = itemVnum
					self.slotData[1]["itemPos"] = slot
					self.AcceleratorItemSlot.SetItemSlot(1, itemVnum, 0)
					self.AcceleratorItemSlot.RefreshSlot()
					self.UpdateChanceAndTimerWithSpecialItem()
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "set")

		elif IsBiologistChanceItem(itemVnum):
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "isBiologistAccItem!")
			if self.slotData[2]["itemVnum"] == 0:
				self.slotData[2]["itemVnum"] = itemVnum
				self.slotData[2]["itemPos"] = slot
				self.ChanceItemSlot.SetItemSlot(2, itemVnum, 0)
				self.ChanceItemSlot.RefreshSlot()
				self.UpdateChanceAndTimerWithSpecialItem()
			else:
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "!= vnum")
				if self.slotData[2]["itemVnum"] != itemVnum:
					self.slotData[2]["itemVnum"] = 0
					self.slotData[2]["itemPos"] = 0
					self.ChanceItemSlot.SetItemSlot(2, 0, 0)
					self.ChanceItemSlot.ClearSlot(2)
					self.ChanceItemSlot.RefreshSlot()	
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "clear")		
					self.slotData[2]["itemVnum"] = itemVnum
					self.slotData[2]["itemPos"] = slot
					self.ChanceItemSlot.SetItemSlot(2, itemVnum, 0)
					self.ChanceItemSlot.RefreshSlot()
					self.UpdateChanceAndTimerWithSpecialItem()
					# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "set")
					
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Unknown VNUM uibiologist 234.")
			
		
		
	def AddItem(self,slot):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(slot))
		if mouseModule.mouseController.isAttached():
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == mouseModule.mouseController.GetAttachedType():
				## RESEARCH ITEM
				if self.SLOT_RESEARCH_ITEM == slot:
					if self.biologistQuestDict[self.questSelect]["itemVnum"] == mouseModule.mouseController.GetAttachedItemIndex():
						if self.slotData[slot]["itemVnum"] == 0:
							self.slotData[slot]["itemVnum"] = mouseModule.mouseController.GetAttachedItemIndex()
							self.slotData[slot]["itemPos"] = attachedSlotPos
							self.ResearchItemSlot.SetItemSlot(slot, mouseModule.mouseController.GetAttachedItemIndex(), 0)
							self.ResearchItemSlot.RefreshSlot()
							self.StartResearchButton.Enable()
				# ## ACCELERATOR
				elif self.SLOT_ACCELERATOR_ITEM == slot:
					if IsBiologistAccelerator(mouseModule.mouseController.GetAttachedItemIndex()):
						# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Hallo?")
						self.slotData[slot]["itemVnum"] = mouseModule.mouseController.GetAttachedItemIndex()
						self.slotData[slot]["itemPos"] = attachedSlotPos
						self.AcceleratorItemSlot.SetItemSlot(slot, mouseModule.mouseController.GetAttachedItemIndex(), 0)
						self.AcceleratorItemSlot.RefreshSlot()	
						self.UpdateChanceAndTimerWithSpecialItem()
				
				# ## CHANCE
				elif self.SLOT_CHANCE_ITEM == slot:
					if IsBiologistChanceItem(mouseModule.mouseController.GetAttachedItemIndex()):
						self.slotData[slot]["itemVnum"] = mouseModule.mouseController.GetAttachedItemIndex()
						self.slotData[slot]["itemPos"] = attachedSlotPos
						self.ChanceItemSlot.SetItemSlot(slot, mouseModule.mouseController.GetAttachedItemIndex(), 0)
						self.ChanceItemSlot.RefreshSlot()
						self.UpdateChanceAndTimerWithSpecialItem()


						
				mouseModule.mouseController.DeattachObject()  
				

	
	def DeleteItem(self,slot):
		if self.SLOT_RESEARCH_ITEM == slot:
			if self.slotData[slot]["itemVnum"] != 0:
				self.slotData[slot]["itemVnum"] = 0
				self.slotData[slot]["itemPos"] = 0
				self.ResearchItemSlot.SetItemSlot(slot, 0, 0)
				self.ResearchItemSlot.ClearSlot(slot)
				self.ResearchItemSlot.RefreshSlot()				
				self.StartResearchButton.Disable()				
			
		elif self.SLOT_ACCELERATOR_ITEM == slot:
			if self.slotData[slot]["itemVnum"] != 0:
				self.slotData[slot]["itemVnum"] = 0
				self.slotData[slot]["itemPos"] = 0
				self.AcceleratorItemSlot.SetItemSlot(slot, 0, 0)
				self.AcceleratorItemSlot.ClearSlot(slot)
				self.AcceleratorItemSlot.RefreshSlot()	
				self.UpdateChanceAndTimerWithSpecialItem()
				
		elif self.SLOT_CHANCE_ITEM == slot:
			if self.slotData[slot]["itemVnum"] != 0:
				self.slotData[slot]["itemVnum"] = 0
				self.slotData[slot]["itemPos"] = 0
				self.ChanceItemSlot.SetItemSlot(slot, 0, 0)
				self.ChanceItemSlot.ClearSlot(slot)
				self.ChanceItemSlot.RefreshSlot()
				self.UpdateChanceAndTimerWithSpecialItem()
		else:
			return	
	
	def ClearSlotData(self):
		self.slotData[0]["itemVnum"] = 0
		self.slotData[0]["itemPos"] = 0
		
		self.ResearchItemSlot.SetItemSlot(0, 0, 0)
		self.ResearchItemSlot.ClearSlot(0)
		self.ResearchItemSlot.RefreshSlot()				
		self.StartResearchButton.Disable()				

		self.slotData[1]["itemVnum"] = 0
		self.slotData[1]["itemPos"] = 0
		self.AcceleratorItemSlot.SetItemSlot(1, 0, 0)
		self.AcceleratorItemSlot.ClearSlot(1)
		self.AcceleratorItemSlot.RefreshSlot()	
				
		self.slotData[2]["itemVnum"] = 0
		self.slotData[2]["itemPos"] = 0
		self.ChanceItemSlot.SetItemSlot(2, 0, 0)
		self.ChanceItemSlot.ClearSlot(2)
		self.ChanceItemSlot.RefreshSlot()
		
		self.UpdateChanceAndTimerWithSpecialItem()
	
	
	def UpdateChanceAndTimerWithSpecialItem(self):
		
		info = self.biologistQuestDict[self.questSelect]
		
		chance = info["base_chance"]
		if self.slotData[2]["itemVnum"] != 0:
			item.SelectItem(self.slotData[2]["itemVnum"])
			chance = chance + item.GetValue(0)
			if chance >= 100:
				chance = 100
		
			self.QuestChanceTextLine.SetText("Erfolgschance: " + str(chance) + "% (+" + str(item.GetValue(0)) + "%)") 
		else:
			self.QuestChanceTextLine.SetText("Erfolgschance: " + str(chance) + "%") 
		
		if self.slotData[1]["itemVnum"] != 0:
			item.SelectItem(self.slotData[1]["itemVnum"])
			# calcTimer = int((info["base_research_time"] * item.GetValue(0)) / 100)
			# if calcTimer <= 0:
				# calcTimer = 0
				
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, str(calcTimer))
			self.QuestResearchTimeTextLine.SetText("Forschungszeit: " + str(info["base_research_time"]) + " Min. (-" + str(item.GetValue(0)) + "%)")
		else:
			self.QuestResearchTimeTextLine.SetText("Forschungszeit: " + str(info["base_research_time"]) + " Min.")
		
			
	def OnUpdate(self):
	
		if self.questSelect >= 0:
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, str(self.biologistQuestDict[self.questSelect]["time"]) + " >= " + str(app.GetGlobalTimeStamp()))
			if self.biologistQuestDict[self.questSelect]["time"] >= app.GetGlobalTimeStamp():
				self.ResearchItemSlotBlockImage.Show()
				self.AcceleratorItemSlotBlockImage.Show()
				self.ChanceItemSlotBlockImage.Show()
				self.StartResearchButton.Disable()
				# self.ResearchInfoTextLine.SetText("Bereit!")
				
				sek = self.biologistQuestDict[self.questSelect]["time"] - app.GetGlobalTimeStamp()
				self.ResearchInfoTextLine.SetText("Wartezeit: " + exterminatus.SecondToDHMS(sek))				
				
			else:
				self.ResearchInfoTextLine.SetText("Bereit!")	
				if mouseModule.mouseController.isAttached():
					attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
					if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == mouseModule.mouseController.GetAttachedType():
						
						# is ResearchItem
						if self.biologistQuestDict[self.questSelect]["itemVnum"] == mouseModule.mouseController.GetAttachedItemIndex():
							self.ResearchItemSlotBlockImage.Hide()
							self.AcceleratorItemSlotBlockImage.Show()
							self.ChanceItemSlotBlockImage.Show()
							
						elif IsBiologistAccelerator(mouseModule.mouseController.GetAttachedItemIndex()):
							self.ResearchItemSlotBlockImage.Show()
							self.AcceleratorItemSlotBlockImage.Hide()
							self.ChanceItemSlotBlockImage.Show()
							
						elif IsBiologistChanceItem(mouseModule.mouseController.GetAttachedItemIndex()):
							self.ResearchItemSlotBlockImage.Show()
							self.AcceleratorItemSlotBlockImage.Show()
							self.ChanceItemSlotBlockImage.Hide()
							
						else:
							self.ResearchItemSlotBlockImage.Show()
							self.AcceleratorItemSlotBlockImage.Show()
							self.ChanceItemSlotBlockImage.Show()					
				else:
					self.ResearchItemSlotBlockImage.Hide()
					self.AcceleratorItemSlotBlockImage.Hide()
					self.ChanceItemSlotBlockImage.Hide()				
					
					
	###############################################################################	
	###############################################################################
	## interfaceModule INPUT
	def AddBiologistQuest(self,id,level,title,desc,status,itemVnum,itemCount_MAX,baseResearchTime,baseResearchChance):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"id: " + str(id) + ", level: " + str(level) + ", title: " + str(title) + ", desc: " + str(desc) + ", status: " + str(status) + ", itemVnum: " + str(itemVnum) + ", itemCount_MAX: " + str(itemCount_MAX) + ", baseResearchChance: " + str(baseResearchChance))
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
	
	def UpdateBiologistQuest(self,index,status):
		self.biologistQuestDict[index]["status"] = int(status)
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Quest " + str(index) + " Status set to " + str(self.biologistQuestDict[index]["status"]))
		
	def RefreshBiologistQuestList(self):
		self.OnQuestListScroll()
		self.CloseOverview()
	
	def UpdateBiologistQuest_ITEM_COUNT(self,index,count):
		self.biologistQuestDict[index]["itemCount"] = int(count)
		self.OnQuestListScroll()
		if index == self.questSelect:
			info = self.biologistQuestDict[index]
			self.QuestCountTextLine.SetText(str(count) + " / " + str(info["itemCount_MAX"]))

	def UpdateBiologistQuest_TIMER(self,index,timer):
		self.biologistQuestDict[index]["time"] = int(timer)
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "index: " + str(index))
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "timer: " + str(self.biologistQuestDict[index]["time"]))
		self.OnQuestListScroll()
	
	
	def SetQuestIndex(self,qid):
		self.qid = int(qid)
		
		
	###############################################################################
	###############################################################################
	
	
	
	def OnClickBiologistItem(self,index):
		pos = int(self.QuestListScrollBar.GetPos() * (len(self.biologistQuestDict) - self.ITEM_COUNT)) + index 
		
	
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(pos))
		self.questSelect = pos
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"self.questSelect: " + str(self.questSelect))
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
		
		if info["status"] == self.STATUS_ACTIVE:
			self.ResearchWindow.Show()
		else:
			self.ResearchWindow.Hide()
		
		self.QuestItemNameTextLine.SetText(item.GetItemName())
		self.QuestCountTextLine.SetText(str(info["itemCount"]) + " / " + str(info["itemCount_MAX"]))
		self.QuestResearchTimeTextLine.SetText("Forschungszeit: " + str(info["base_research_time"]) + " Min.")
		self.QuestChanceTextLine.SetText("Erfolgschance: " + str(info["base_chance"]) + "%") 
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"BuildOverview:INFO DONE")

		# self.ResearchInfoTextLine.SetText("Bereit!")
		self.StartResearchButton.Disable()		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"BuildOverview:DONE")
	def OpenOverview(self):
		self.QuestOverview.Show()
		
	def CloseOverview(self):
		self.questSelect = -1
		self.ClearSlotData()
		self.QuestOverview.Hide()
	
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.OnQuestListScroll()
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
			
			if info["status"] == self.bioItemDict[i].STATUS_ACTIVE:
				player_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
				if player_level < info["level"]:
					self.bioItemDict[i].SetStatusColor(self.bioItemDict[i].STATUS_LEVEL_LOW,info["level"])
				else:
					self.bioItemDict[i].SetStatusColor(info["status"],0)
			else:
				self.bioItemDict[i].SetStatusColor(info["status"],0)
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
	STATUS_LEVEL_LOW = 3

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
	
	def SetStatusColor(self,index,level):
		self.status = index
		if index == self.STATUS_INACTIVE:
			self.bar.SetColor(self.COLOR_INACTIVE)
			self.questCount.Hide()
			self.questPercent.Hide()	
			self.questTimer.SetText("Nicht verfügbar.")
		elif index == self.STATUS_ACTIVE:
			self.bar.SetColor(self.COLOR_ACTIVE)
			self.questCount.Show()
			self.questPercent.Show()		
		elif index == self.STATUS_COMPLETE:
			self.bar.SetColor(self.COLOR_COMPLETE)
			self.questCount.Hide()
			self.questPercent.Show()
			self.questTimer.SetText("Abgeschlossen")
		elif index == self.STATUS_LEVEL_LOW:
			self.bar.SetColor(self.COLOR_INACTIVE)
			self.questCount.Hide()
			self.questPercent.Hide()	
			self.questTimer.SetText("Ab Lv." + str(level))			
			
			
			
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"uibiologist.BiologistItem(): Unknown StatusIndex: " + str(index))
	
	
	def OnUpdate(self):
		if self.bar.IsIn():
			self.OnMouseOverIn()
		else:
			self.OnMouseOverOut()
		
		if self.status == self.STATUS_INACTIVE:
			self.questTimer.SetText("Noch nicht freigeschaltet!")	
			self.questPercent.SetText("0%")			
		
		elif self.status == self.STATUS_ACTIVE:
			if self.timer > app.GetGlobalTimeStamp():
				# self.questTimer.SetText(localeInfo.SecondToDHMS(self.timer - app.GetTime()))
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"TIMER ACTIVE!")
				sek = self.timer - app.GetGlobalTimeStamp()
				self.questTimer.SetText(exterminatus.SecondToDHMS(sek))
			else:
				self.questTimer.SetText("Bereit!")	
		elif self.status == self.STATUS_COMPLETE:
			self.questTimer.SetText("Abgeschlossen!")	
			self.questPercent.SetText("100%")
			
	def OnMouseOverIn(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OnMouseOverIn")
		index = self.status  
		if index == self.STATUS_INACTIVE:
			self.bar.SetColor(self.COLOR_INACTIVE_HOVER)
		
		elif index == self.STATUS_ACTIVE:
			self.bar.SetColor(self.COLOR_ACTIVE_HOVER)
		
		elif index == self.STATUS_COMPLETE:
			self.bar.SetColor(self.COLOR_COMPLETE_HOVER)	

		elif index == self.STATUS_LEVEL_LOW:
			self.bar.SetColor(self.COLOR_INACTIVE_HOVER)
		
	def OnMouseOverOut(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"OnMouseOverOut")
		index = self.status  
		if index == self.STATUS_INACTIVE:
			self.bar.SetColor(self.COLOR_INACTIVE)
		
		elif index == self.STATUS_ACTIVE:
			self.bar.SetColor(self.COLOR_ACTIVE)
		
		elif index == self.STATUS_COMPLETE:
			self.bar.SetColor(self.COLOR_COMPLETE)	

		elif index == self.STATUS_LEVEL_LOW:
			self.bar.SetColor(self.COLOR_INACTIVE)
	
	def SetItem(self,itemVnum):
		self.itemVnum = int(itemVnum)
		self.itemSlot.SetItemSlot(0,itemVnum,0)
	
	def SetQuestTitle(self,index):
		self.questName.SetText(index)
		
	def SetTimer(self,timer):
		if timer == 0:
			self.timer = 0
		else:
			self.timer = timer
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"timer: " + str(self.timer))
		# self.questTimer.SetText(str(timer))

	def SetCount(self,min,max):
		self.itemCount = int(min)
		self.itemCountNeed = int(max)

		self.questCount.SetText(str(min) + " / " + str(max))

		percent = (float(self.itemCount) / float(self.itemCountNeed)) * 100
		self.questPercent.SetText(str(int(percent)) + "%")
	
	def OnItemClick(self):
		if self.status == self.STATUS_COMPLETE or self.status == self.STATUS_INACTIVE or self.status == self.STATUS_LEVEL_LOW:
			return
			
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

