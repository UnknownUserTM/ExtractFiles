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
from uitooltip import ItemToolTip
AFFECT_DICT = ItemToolTip.AFFECT_DICT

class PetBoard(ui.ScriptWindow):
	PetName = "TestName"
	PetItemVnum = 55003
	PetLifetime = app.GetGlobalTimeStamp() + (60*60*24*3)
	PetLevel = 135
	PetAffects = [1,3000,2,500,3,12]
	PetSkillLevel = 20
	PetSkillStatus = 0
	PetMobEXP = 30000
	PetItemEXP = 90
	isLoaded = 0
	
	PetContentBoardTitleBars = {}
	PetEXPBubble = {}
	PetBoni = {}
	expGauge = {}
	ItemExpGauge = {}
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"closegui")
		constInfo.PET_INFOS["gui"] = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()

	def LoadUI(self):
		if constInfo.PET_INFOS["gui"] == 1:
			constInfo.PET_INFOS["gui"] = 0
			self.__del__()
			return
		
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(400, 415)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Pet")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()
		
		self.tooltip = uiToolTip.ToolTip()  
		self.tooltip.HideToolTip()
		
		self.HeadBoard = ui.ThinBoard()
		self.HeadBoard.SetParent(self.Board)
		self.HeadBoard.SetPosition(15,35)
		self.HeadBoard.SetSize(370,80)
		self.HeadBoard.Show()
		
		self.PetItemSlotIMG = ui.ImageBox()
		self.PetItemSlotIMG.SetParent(self.HeadBoard)
		self.PetItemSlotIMG.SetPosition(15,17)
		self.PetItemSlotIMG.LoadImage("exterminatus/new_pet_images/pet_incu_slot_001.tga")
		self.PetItemSlotIMG.Show()
		
		self.PetItemVnumIMG = ui.ImageBox()
		self.PetItemVnumIMG.SetParent(self.PetItemSlotIMG)
		self.PetItemVnumIMG.SetPosition(4,4)
		self.PetItemVnumIMG.LoadImage("icon/item/55001.tga")
		self.PetItemVnumIMG.Show()
		
		self.PetNameSlotBar = ui.SlotBar()
		self.PetNameSlotBar.SetParent(self.HeadBoard)
		self.PetNameSlotBar.SetPosition(70,25)
		self.PetNameSlotBar.SetSize(225,19)
		self.PetNameSlotBar.Show()
			
		self.PetNameTextLine = ui.TextLine()
		self.PetNameTextLine.SetParent(self.PetNameSlotBar)
		self.PetNameTextLine.SetPosition(8,2)
		self.PetNameTextLine.SetText(str(constInfo.PET_INFOS["name"]))
		self.PetNameTextLine.Show()
		
		self.StatBoard = ui.ThinBoard()
		self.StatBoard.SetParent(self.Board)
		self.StatBoard.SetPosition(15,120)
		self.StatBoard.SetSize(370,120)
		self.StatBoard.Show()
		
		i = 0
		y = 15
		y_add = 120
		headlines = [["Level",36],["Erfahrung",28],["Laufzeit",32]]
		while i < 3:
			self.PetContentBoardTitleBars[i] = ui.HorizontalBar()
			self.PetContentBoardTitleBars[i].SetParent(self.StatBoard)
			self.PetContentBoardTitleBars[i].SetPosition(y,10)
			self.PetContentBoardTitleBars[i].Create(100)
			self.PetContentBoardTitleBars[i].Show()
			self.PetContentBoardTitleBars[i+10] = ui.TextLine()
			self.PetContentBoardTitleBars[i+10].SetParent(self.PetContentBoardTitleBars[i])
			self.PetContentBoardTitleBars[i+10].SetPosition(headlines[i][1],2)
			self.PetContentBoardTitleBars[i+10].SetText(str(headlines[i][0]))
			self.PetContentBoardTitleBars[i+10].Show()
			if i > 0:
				self.PetContentBoardTitleBars[i+100] = ui.ImageBox()
				self.PetContentBoardTitleBars[i+100].SetParent(self.StatBoard)
				self.PetContentBoardTitleBars[i+100].SetPosition(y-11,5)
				self.PetContentBoardTitleBars[i+100].LoadImage("exterminatus/new_pet_images/pet_trenn_line.tga")			
				self.PetContentBoardTitleBars[i+100].Show()
			
			i = i + 1
			y = y + y_add
			
		

		self.PetLevelSlotBar = ui.SlotBar()
		self.PetLevelSlotBar.SetParent(self.StatBoard)
		self.PetLevelSlotBar.SetPosition(15,35)
		self.PetLevelSlotBar.SetSize(98,19)
		self.PetLevelSlotBar.Show()
		self.PetLevelTextLine = ui.TextLine()
		self.PetLevelTextLine.SetParent(self.PetLevelSlotBar)
		self.PetLevelTextLine.SetPosition(39,2)
		self.PetLevelTextLine.SetText("  7")
		self.PetLevelTextLine.Show()		
		i = 0
		y = 142
		y_add = 17

		
		while i < 5:
			self.PetEXPBubble[i] = ui.ImageBox()
			self.PetEXPBubble[i].SetParent(self.StatBoard)
			self.PetEXPBubble[i].SetPosition(y,35)
			self.PetEXPBubble[i].LoadImage("exterminatus/new_pet_images/exp_bubble_empty.tga")
			self.PetEXPBubble[i].Show()	
			if i < 4: 
				self.expGauge[i] = ui.ExpandedImageBox()
				self.expGauge[i].SetParent(self.StatBoard)
				self.expGauge[i].SetPosition(y,35)
				self.expGauge[i].LoadImage("exterminatus/new_pet_images/exp_bubble_full.tga")
				self.expGauge[i].Show()
			else:
				self.ItemExpGauge[0] = ui.ExpandedImageBox()
				self.ItemExpGauge[0].SetParent(self.StatBoard)
				self.ItemExpGauge[0].SetPosition(y,35)
				self.ItemExpGauge[0].LoadImage("exterminatus/new_pet_images/exp_bubble_item.tga")
				self.ItemExpGauge[0].Show()
				
			i = i + 1
			y = y + y_add
		self.PetEXPBlock = ui.ImageBox()
		self.PetEXPBlock.SetParent(self.StatBoard)
		self.PetEXPBlock.SetPosition(142,35)
		self.PetEXPBlock.LoadImage("exterminatus/new_pet_images/pet_exp_block.tga")
		self.PetEXPBlock.Show()			
		self.SetExperience(0,2000)	
		self.SetItemExperience(0,2)
		# self.PetItemEXPSlotIMG = ui.ImageBox()
		# self.PetItemEXPSlotIMG.SetParent(self.StatBoard)
		# self.PetItemEXPSlotIMG.SetPosition(167,65)
		# self.PetItemEXPSlotIMG.LoadImage("d:/ymir work/ui/public/slot_base.sub")
		# self.PetItemEXPSlotIMG.Show()
		# self.PetItemEXPSlotItemIMG = ui.ImageBox()
		# self.PetItemEXPSlotItemIMG.SetParent(self.PetItemEXPSlotIMG)
		# self.PetItemEXPSlotItemIMG.SetPosition(0,0)
		# self.PetItemEXPSlotItemIMG.LoadImage("icon/item/55100.tga")
		# self.PetItemEXPSlotItemIMG.Show()
		# self.PetItemEXPSlotItemIMGCover = ui.ImageBox()
		# self.PetItemEXPSlotItemIMGCover.SetParent(self.PetItemEXPSlotIMG)
		# self.PetItemEXPSlotItemIMGCover.SetPosition(2,2)
		# self.PetItemEXPSlotItemIMGCover.LoadImage("exterminatus/new_pet_images/slot_block.tga")
		# self.PetItemEXPSlotItemIMGCover.Show()
		# self.PetItemEXPSlotItemIMGCover1 = ui.ImageBox()
		# self.PetItemEXPSlotItemIMGCover1.SetParent(self.PetItemEXPSlotIMG)
		# self.PetItemEXPSlotItemIMGCover1.SetPosition(2,2)
		# self.PetItemEXPSlotItemIMGCover1.LoadImage("exterminatus/new_pet_images/slot_block.tga")
		# self.PetItemEXPSlotItemIMGCover1.Show()
		
		# self.PetItemEXPSlotItemSlot = ui.GridSlotWindow()  
		# self.PetItemEXPSlotItemSlot.SetParent(self.PetItemEXPSlotIMG)  
		# self.PetItemEXPSlotItemSlot.ArrangeSlot(1,1,1,32,32,0,0)  
		# self.PetItemEXPSlotItemSlot.SetPosition(0, 0)  
		# #self.PetItemEXPSlotItemSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		# #self.PetItemEXPSlotItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
		# self.PetItemEXPSlotItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
		# #self.PetItemEXPSlotItemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
		# self.PetItemEXPSlotItemSlot.Show()		
		
		
		
		self.PetLifeTimeSlotBar = ui.SlotBar()
		self.PetLifeTimeSlotBar.SetParent(self.StatBoard)
		self.PetLifeTimeSlotBar.SetPosition(255,35)
		self.PetLifeTimeSlotBar.SetSize(98,19)
		self.PetLifeTimeSlotBar.Show()
		self.PetLifeTimeTextLine = ui.TextLine()
		self.PetLifeTimeTextLine.SetParent(self.PetLifeTimeSlotBar)
		self.PetLifeTimeTextLine.SetPosition(18,2)
		self.PetLifeTimeTextLine.SetText("0")
		self.PetLifeTimeTextLine.Show()
		# self.PetLifeTimeSlotIMG = ui.ImageBox()
		# self.PetLifeTimeSlotIMG.SetParent(self.StatBoard)
		# self.PetLifeTimeSlotIMG.SetPosition(287,65)
		# self.PetLifeTimeSlotIMG.LoadImage("d:/ymir work/ui/public/slot_base.sub")
		# self.PetLifeTimeSlotIMG.Show()
		# self.PetLifeTimeSlotItemIMG = ui.ImageBox()
		# self.PetLifeTimeSlotItemIMG.SetParent(self.PetLifeTimeSlotIMG)
		# self.PetLifeTimeSlotItemIMG.SetPosition(0,0)
		# self.PetLifeTimeSlotItemIMG.LoadImage("icon/item/55102.tga")
		# self.PetLifeTimeSlotItemIMG.Show()
		# self.PetLifeTimeSlotItemIMGCover = ui.ImageBox()
		# self.PetLifeTimeSlotItemIMGCover.SetParent(self.PetLifeTimeSlotIMG)
		# self.PetLifeTimeSlotItemIMGCover.SetPosition(2,2)
		# self.PetLifeTimeSlotItemIMGCover.LoadImage("exterminatus/new_pet_images/slot_block.tga")
		# self.PetLifeTimeSlotItemIMGCover.Show()
		# self.PetLifeTimeSlotItemIMGCover1 = ui.ImageBox()
		# self.PetLifeTimeSlotItemIMGCover1.SetParent(self.PetLifeTimeSlotIMG)
		# self.PetLifeTimeSlotItemIMGCover1.SetPosition(2,2)
		# self.PetLifeTimeSlotItemIMGCover1.LoadImage("exterminatus/new_pet_images/slot_block.tga")
		# self.PetLifeTimeSlotItemIMGCover1.Show()

		# self.LifeTimeSlotItemSlot = ui.GridSlotWindow()  
		# self.LifeTimeSlotItemSlot.SetParent(self.PetLifeTimeSlotIMG)  
		# self.LifeTimeSlotItemSlot.ArrangeSlot(2,1,1,32,32,0,0)  
		# self.LifeTimeSlotItemSlot.SetPosition(0, 0)  
		# self.LifeTimeSlotItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
		# self.LifeTimeSlotItemSlot.Show()

		
		self.BoniBoard = ui.ThinBoard()
		self.BoniBoard.SetParent(self.Board)
		self.BoniBoard.SetPosition(15,245)
		self.BoniBoard.SetSize(370,100)
		self.BoniBoard.Show()		

		self.SkillBoard = ui.ThinBoard()
		self.SkillBoard.SetParent(self.Board)
		self.SkillBoard.SetPosition(15,350)
		self.SkillBoard.SetSize(370,50)
		self.SkillBoard.Show()
		
		i = 0
		x = 15
		list = 0
		boni = ["Verteidigung +75","Stark gegen Monster +20%","Chance auf krit. Treffer +10%"]
		while i < 3:
			self.PetBoni[i] = ui.TextLine()
			self.PetBoni[i].SetParent(self.BoniBoard)
			self.PetBoni[i].SetPosition(15,x)
			self.PetBoni[i].SetText("Bonus " + str(i+1) + ":")
			self.PetBoni[i].Show()
			self.PetBoni[i+3] = ui.TextLine()
			self.PetBoni[i+3].SetParent(self.BoniBoard)
			self.PetBoni[i+3].SetPosition(65,x)
			self.PetBoni[i+3].SetText(str(self.__CreateAffectString(self.PetAffects[list],self.PetAffects[list+1]*2)))
			self.PetBoni[i+3].SetFontColor(0.5411, 0.7254, 0.5568)
			self.PetBoni[i+3].Show()			
			list = list + 2
			i = i + 1
			x = x + 26
			
		self.PetSkillSlotBGImg = ui.ImageBox()
		self.PetSkillSlotBGImg.SetParent(self.SkillBoard)
		self.PetSkillSlotBGImg.SetPosition(8,8)
		self.PetSkillSlotBGImg.LoadImage("d:/ymir work/ui/public/slot_base.sub")
		self.PetSkillSlotBGImg.Show()			
		
		self.PetSkillSlotBGImg1 = ui.GridSlotWindow()  
		self.PetSkillSlotBGImg1.SetParent(self.PetSkillSlotBGImg)  
		self.PetSkillSlotBGImg1.ArrangeSlot(3,1,1,32,32,0,0)  
		self.PetSkillSlotBGImg1.SetPosition(0, 0)  
		#self.PetSkillSlotBGImg1.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		#self.PetSkillSlotBGImg1.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
		#self.PetSkillSlotBGImg1.SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
		self.PetSkillSlotBGImg1.SetSelectItemSlotEvent(ui.__mem_func__(self.ActivateSkill))  
		self.PetSkillSlotBGImg1.Show()
		self.PetSkillSlotBGImg1.SetItemSlot(3, 70002, constInfo.PET_INFOS["skill_level"])
		self.PetSkillNameTitle = ui.TextLine()
		self.PetSkillNameTitle.SetParent(self.SkillBoard)
		self.PetSkillNameTitle.SetPosition(45,8)
		self.PetSkillNameTitle.SetText("Automatisches aufheben")
		self.PetSkillNameTitle.Show()		
		self.PetSkillNameError = ui.TextLine()
		self.PetSkillNameError.SetParent(self.SkillBoard)
		self.PetSkillNameError.SetPosition(45,23)
		self.PetSkillNameError.SetText("Die Fertigkeit kann erst erlernt werden wenn dein Pet lv.10 ist.")
		self.PetSkillNameError.SetFontColor(0.9, 0.4745, 0.4627)
		self.PetSkillNameError.Show()		
		constInfo.PET_INFOS["gui"] = 1
		
	def ActivateSkill(self,slot):
		if constInfo.PET_INFOS["skill_level"] < 20:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Die Fertigkeit muss auf Stufe 20 sein!")
			return
			
		if constInfo.PET_INFOS["skill_status"] == 0:
			constInfo.PET_INFOS["skill_status"] = 1
		else:
			constInfo.PET_INFOS["skill_status"] = 0
		
	def add_slot(self,slot):
		isAttached = mouseModule.mouseController.isAttached()  
		if isAttached:  
			attachedSlotType = mouseModule.mouseController.GetAttachedType()  
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()  
			mouseModule.mouseController.DeattachObject()  
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY != attachedSlotType:  
				return  
			itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(attachedSlotPos)		
			if slot == 1:
				if itemvnum == 91163:
					constInfo.INPUT_CMD = "ITEMEXP#"
					event.QuestButtonClick(constInfo.PET_INFOS["qid"])
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO,"Verdammt! Willst du dein Pet etwa umbringen?")
					return
			else:
				if itemvnum == 55102:
					if constInfo.PET_INFOS["life"] > app.GetGlobalTimeStamp():
						chat.AppendChat(chat.CHAT_TYPE_INFO,"Dein Pet hat noch genügend Laufzeit!")
					else:
						constInfo.INPUT_CMD = "REVIVE#"
						event.QuestButtonClick(constInfo.PET_INFOS["qid"])
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO,"Verdammt! Willst du dein Pet etwa umbringen?")
					return				

			
	def SetExperience(self, curPoint, maxPoint):

		curPoint = min(curPoint, maxPoint)
		curPoint = max(curPoint, 0)
		maxPoint = max(maxPoint, 0)

		quarterPoint = maxPoint / 4
		FullCount = 0

		if 0 != quarterPoint:
			FullCount = min(4, curPoint / quarterPoint)

		for i in xrange(4):
			self.expGauge[i].Hide()

		for i in xrange(FullCount):
			self.expGauge[i].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.expGauge[i].Show()

		if 0 != quarterPoint:
			if FullCount < 4:
				Percentage = float(curPoint % quarterPoint) / quarterPoint - 1.0
				self.expGauge[FullCount].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.expGauge[FullCount].Show()
		
	def SetItemExperience(self, curPoint, maxPoint):

		curPoint = min(curPoint, maxPoint)
		curPoint = max(curPoint, 0)
		maxPoint = max(maxPoint, 0)

		quarterPoint = maxPoint / 1
		FullCount = 0

		if 0 != quarterPoint:
			FullCount = min(1, curPoint / quarterPoint)

		for i in xrange(1):
			self.ItemExpGauge[i].Hide()

		for i in xrange(FullCount):
			self.ItemExpGauge[i].SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			self.ItemExpGauge[i].Show()

		if 0 != quarterPoint:
			if FullCount < 1:
				Percentage = float(curPoint % quarterPoint) / quarterPoint - 1.0
				self.ItemExpGauge[FullCount].SetRenderingRect(0.0, Percentage, 0.0, 0.0)
				self.ItemExpGauge[FullCount].Show()		
		

	def ShowLevelInfoToolTip(self):
		self.tooltip.ClearToolTip()
		MaxMobEXP = (constInfo.PET_INFOS["level"] + 1) * 1000
		MaxItemEXP = constInfo.PET_INFOS["level"] + 1
		self.tooltip.AppendTextLine("Monster-EXP: " + constInfo.NumberToPointString(constInfo.PET_INFOS["mob_exp"]) + "/" + constInfo.NumberToPointString(MaxMobEXP))
		self.tooltip.AppendTextLine("Item-EXP: " + constInfo.NumberToPointString(constInfo.PET_INFOS["item_exp"]) + "/" + constInfo.NumberToPointString(MaxItemEXP))
		if constInfo.PET_INFOS["double_exp"] > app.GetGlobalTimeStamp():
			self.tooltip.AppendHorizontalLine()
			self.tooltip.AppendTextLine("[ Pet-EXP Ring aktiv ]")
			self.tooltip.AppendMallItemLastTime(constInfo.PET_INFOS["double_exp"])

		
		self.tooltip.ShowToolTip()
		
	def HideLevelInfoToolTip(self):
		self.tooltip.HideToolTip()

		
		
	def OnUpdate(self):
		if self.IsShow():
		
			if self.PetEXPBlock.IsIn():
				# self.Board.SetTitleName("Pet - IN")
				self.ShowLevelInfoToolTip()
			else:
				# self.Board.SetTitleName("Pet - OUT")
				self.HideLevelInfoToolTip()
		
			if constInfo.PET_INFOS["level"] == 0 or constInfo.PET_INFOS["guiclose"] == 1:
				constInfo.PET_INFOS["skill_status"] = 0
				constInfo.PET_INFOS["gui"] = 0
				constInfo.PET_INFOS["guiclose"] = 0
				self.HideLevelInfoToolTip()
				self.__del__()
				return
				
			itemVnum = 55001
			for i in xrange(fgGHGjjFHJghjfFG1545gGG.INVENTORY_PAGE_SIZE*4):
				if constInfo.IS_PET_SEAL(fgGHGjjFHJghjfFG1545gGG.GetItemIndex(i)):
					metinSocket = [fgGHGjjFHJghjfFG1545gGG.GetItemMetinSocket(i, j) for j in xrange(fgGHGjjFHJghjfFG1545gGG.METIN_SOCKET_MAX_NUM)]
					if metinSocket[0] == 1:
						itemVnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(i)
			self.PetItemVnumIMG.LoadImage("icon/item/" + str(itemVnum) + ".tga")
			if constInfo.PET_INFOS["life"] > app.GetGlobalTimeStamp(): 
				leftSec = max(0, constInfo.PET_INFOS["life"] - app.GetGlobalTimeStamp())
				self.PetLifeTimeTextLine.SetText(localeInfo.SecondToDHM(leftSec))
				self.PetLifeTimeTextLine.SetPosition(18,2)
				self.PetLifeTimeTextLine.SetFontColor(0.5411, 0.7254, 0.5568)	
			else:
				self.PetLifeTimeTextLine.SetText("Schläft")
				self.PetLifeTimeTextLine.SetFontColor(0.9, 0.4745, 0.4627)
				self.PetLifeTimeTextLine.SetPosition(42,2)
			
			if constInfo.PET_INFOS["level"] < 10:
				self.PetLevelTextLine.SetText("  " + str(constInfo.PET_INFOS["level"]))
			elif constInfo.PET_INFOS["level"] >= 10 and constInfo.PET_INFOS["level"] < 100:
				self.PetLevelTextLine.SetText(" " + str(constInfo.PET_INFOS["level"]))
			elif constInfo.PET_INFOS["level"] >= 100:
				self.PetLevelTextLine.SetText(str(constInfo.PET_INFOS["level"]))
			
			MaxMobEXP = (constInfo.PET_INFOS["level"] + 1) * 1000
			MaxItemEXP = constInfo.PET_INFOS["level"] + 1
			self.SetExperience(constInfo.PET_INFOS["mob_exp"],MaxMobEXP)	
			self.SetItemExperience(constInfo.PET_INFOS["item_exp"],MaxItemEXP)
				
			i = 0
			list = 0
			while i < 3:
				self.PetBoni[i+3].SetText(str(self.__CreateAffectString(constInfo.PET_INFOS["attr"][list],constInfo.PET_INFOS["attr"][list+1])))			
				list = list + 2
				i = i + 1
				
			if constInfo.PET_INFOS["skill_status"] == 1:
				self.PetSkillSlotBGImg1.ActivateSlot(3)	
				self.PetSkillNameError.SetText("(Aktiviert)")
			else:
				self.PetSkillSlotBGImg1.DeactivateSlot(3)
				self.PetSkillNameError.SetText("(Deaktiviert)")				
				
			if constInfo.PET_INFOS["level"] < 10:
				self.PetSkillNameError.SetText("Die Fertigkeit kann erst erlernt werden wenn dein Pet lv.10 ist.")
				self.PetSkillNameError.SetFontColor(0.9, 0.4745, 0.4627)
			elif constInfo.PET_INFOS["level"] >= 10 and constInfo.PET_INFOS["skill_level"] < 20:
				self.PetSkillNameError.SetText("Du kannst die Fertigkeit nun mit den Meisterbüchern trainieren.")
				self.PetSkillNameError.SetFontColor(0.5411, 0.7254, 0.5568)			
			elif constInfo.PET_INFOS["level"] >= 10 and constInfo.PET_INFOS["skill_level"] >= 20:
				#self.PetSkillNameError.SetText("")
				self.PetSkillNameError.SetFontColor(0.5411, 0.7254, 0.5568)	
			if constInfo.PET_INFOS["skill_level"] >= 20:
				self.PetSkillSlotBGImg1.SetItemSlot(3, 70002, 20)
			else:
				self.PetSkillSlotBGImg1.SetItemSlot(3, 70002, constInfo.PET_INFOS["skill_level"])
	def __CreateAffectString(self, affectType, affectValue):
		if 0 == affectType:
			return None

		if 0 == affectValue:
			return None

		try:
			return AFFECT_DICT[affectType](affectValue)
		except TypeError:
			return "UNKNOWN_VALUE[%s] %s" % (affectType, affectValue)
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s" % (affectType, affectValue)	

class PetBoxBoard(ui.ScriptWindow):
	itemVnum = constInfo.PET_INFOS["itemVnum"]
	goldPrice = constInfo.PET_INFOS["price"]
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		
	def close(self):
		constInfo.PET_INFOS["gui_box"] = 0
		self.__del__()

	def LoadUI(self):
		constInfo.PET_INFOS["gui_box"] = 1
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(200, 210)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		if constInfo.PET_INFOS["box_mode"] == 0:
			self.Board.SetTitleName("Brutkasten")
		else:
			self.Board.SetTitleName("Name ändern")
		self.Board.SetCloseEvent(self.close)
		self.Board.Show()
		self.PetItemSlotIMG = ui.ImageBox()
		self.PetItemSlotIMG.SetParent(self.Board)
		self.PetItemSlotIMG.SetPosition(80,35)
		self.PetItemSlotIMG.LoadImage("exterminatus/new_pet_images/pet_incu_slot_001.tga")
		self.PetItemSlotIMG.Show()
		self.PetItemVnumIMG = ui.ImageBox()
		self.PetItemVnumIMG.SetParent(self.PetItemSlotIMG)
		self.PetItemVnumIMG.SetPosition(4,4)
		self.PetItemVnumIMG.LoadImage("icon/item/55001.tga")
		self.PetItemVnumIMG.Show()		
		
		self.PetNameBox = ui.ThinBoard()
		self.PetNameBox.SetParent(self.Board)
		self.PetNameBox.SetPosition(15,80)
		self.PetNameBox.SetSize(170,70)
		self.PetNameBox.Show()
		
		self.PetNameTitle = ui.TextLine()
		self.PetNameTitle.SetParent(self.PetNameBox)
		self.PetNameTitle.SetPosition(52,3)
		self.PetNameTitle.SetText("Name des Pets")
		self.PetNameTitle.Show()
		self.PetNameSlotBar = ui.SlotBar()
		self.PetNameSlotBar.SetParent(self.PetNameBox)
		self.PetNameSlotBar.SetPosition(8,22)
		self.PetNameSlotBar.SetSize(152,19)
		self.PetNameSlotBar.Show()		
		self.NameInput = ui.EditLine()
		self.NameInput.SetParent(self.PetNameSlotBar)
		self.NameInput.SetPosition(5,3)
		self.NameInput.SetSize(142,19)
		self.NameInput.SetMax(12)
		self.NameInput.OnSetFocus()
		self.NameInput.Show()		
		
		if constInfo.PET_INFOS["box_mode"] == 0:
			self.PetPriceTitle = ui.TextLine()
			self.PetPriceTitle.SetParent(self.Board)
			self.PetPriceTitle.SetPosition(55,155)
			self.PetPriceTitle.SetText("Preis: " + self.NumberToCoinsString(self.goldPrice))
			self.PetPriceTitle.Show()		
		
		self.FinishButton = ui.Button()
		self.FinishButton.SetParent(self.Board)
		self.FinishButton.SetPosition(60,175)
		#self.FinishButton.SetText("Ausbrüten")
		self.FinishButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")  
		self.FinishButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")  
		self.FinishButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")		
		self.FinishButton.SetEvent(self.FinishConfig)
		self.FinishButton.Show()			
		self.FinishButtonTextLine = ui.TextLine()
		self.FinishButtonTextLine.SetParent(self.FinishButton)
		self.FinishButtonTextLine.SetPosition(20,3)
		if constInfo.PET_INFOS["box_mode"] == 0:
			self.FinishButtonTextLine.SetText("Ausbrüten")
		else:
			self.FinishButtonTextLine.SetText("Ändern")
		self.FinishButtonTextLine.Show()	


	def FinishConfig(self):
		PetName = self.NameInput.GetText()
		if GFHhg54GHGhh45GHGH.IsInsultIn(PetName):
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Dieser Name ist unangebracht...")
			return
		if len(PetName) == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Du hast keinen Namen angegeben!")
			return
		if PetName.find(localeInfo.CREATE_GM_NAME)!=-1:
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Dieser Name enthält Zeichen von localeInfo.CREATE_GM_NAME. Und ist unzulässig!")
			return
		StupidLetters = ['!','@','#','$','%','^','&','*','(',')','_','+','|','{','}',':','"','<','>','?','~']
		for i in xrange(len(StupidLetters)):
			if PetName.find(StupidLetters[i])!=-1:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Der eingegebene Name enthält unzulässige zeichen!")
				return 
		if constInfo.PET_INFOS["box_mode"] == 0:
			constInfo.INPUT_CMD = "CONFIG#" + str(constInfo.PET_INFOS["itemIndex"]) + "#" + str(PetName)
		else:
			constInfo.INPUT_CMD = "CHANGENAME#" + str(constInfo.PET_INFOS["itemIndex"]) + "#" + str(PetName)
		event.QuestButtonClick(constInfo.PET_INFOS["qid"])			
		self.close()
		
	def NumberToCoinsString(self,n):
		if n <= 0 :
			return "0 %s" % ("Yang")
		return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), "Yang") 
		
