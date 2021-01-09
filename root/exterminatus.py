import ui
import localeInfo
import chat
import uiToolTip
import item
import fgGHGjjFHJghjfFG1545gGG as player

#Halloooo
def StringBoolToRealBool(boolString):
	if boolString == "true":
		return True
		
	return False
	
def SecondToDHMS(time):
	if time < 60:
		return str(int(time)) + " " + localeInfo.SECOND
		
	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:
		text += str(day) + " " + localeInfo.DAY
		text += " "

	if hour > 0:
		text += str(hour) + " " + localeInfo.HOUR
		text += " "

	if minute > 0:
		text += str(minute) + " " + localeInfo.MINUTE

	return text

class PointArrow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self)
		self.SetSize(20,35)
		
		self.MakeArrow()
		self.Show()
		
	def __del__(self):
		ui.Window.__del__(self)
		
		
	def MakeArrow(self):
		self.arrow = ui.AniImageBox()
		self.arrow.SetParent(self)
		self.arrow.SetPosition(0,0)
		self.arrow.SetDelay(10.0)
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/1.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/2.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/3.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/4.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/5.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/4.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/3.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/2.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/1.sub")
		self.arrow.Show()

class HelpButtonWindow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self)
		self.button = None
		self.SetSize(17,17)
		# self.MakeToolTip()
		self.MakeButton()

		
	def __del__(self):
		ui.Window.__del__(self)

	def MakeButton(self):
	
		self.toolTip = uiToolTip.ToolTip()  
		self.toolTip.HideToolTip()	
		
		self.button = ui.Button()
		self.button.SetParent(self)
		self.button.SetPosition(0,0)
		self.button.SetUpVisual("yamato_button/q_mark_01.tga")
		self.button.SetOverVisual("yamato_button/q_mark_02.tga")
		self.button.SetDownVisual("yamato_button/q_mark_02.tga")
		self.button.ShowToolTip = lambda arg=1: self.ShowToolTip(arg)
		self.button.HideToolTip = lambda arg=1: self.HideToolTip()
		self.button.Show()		
	
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "QMARK DONE!")
		# self.DefineToolTipContent("test")
	
	# def ToggleToolTipBox(self):
		# if self.toolTip.IsShow():
			# self.HideToolTip()
		# else:
			# self.ShowToolTip()
	
	
	def ShowToolTip(self,arg):
		self.toolTip.ShowToolTip()
	
	def HideToolTip(self):
		self.toolTip.HideToolTip()
		
	def DefineToolTipContent(self,localeString):
		self.toolTip.ClearToolTip()
		# self.toolTip.SetTitle("Hallo Welt!")
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendDescription(localeString,26)
		self.toolTip.AppendSpace(10)
		self.toolTip.ResizeToolTip()		
	
	
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.Show()
		self.toolTip = toolTip
		
		
	def Destroy(self):
		self.button = None
		self.Hide()
		self.__del__()

class EasyItemSlot(ui.Window):
	
	BACKGROUND_SLOT = "d:/ymir work/ui/public/Slot_Base.sub"
	
	ALPHA_NORMAL = 1.0
	ALPHA_NEGATIVE = 0.5
	
	size = 1
	item = 0
	item_count_need = 0
	enable_item_check = False
	backgroundSlotImage = {}
	def __init__(self):
		ui.Window.__init__(self)
		self.SetSize(32,32)
		self.MakeSlot()

	def __del__(self):
		ui.Window.__del__(self)

	def MakeSlot(self):
		self.toolTip = uiToolTip.ItemToolTip()  
		self.toolTip.HideToolTip()	
		
		y = 0
		for i in xrange(3):
			self.backgroundSlotImage[i] = ui.ImageBox()
			self.backgroundSlotImage[i].SetParent(self)
			self.backgroundSlotImage[i].SetPosition(0,y)
			self.backgroundSlotImage[i].LoadImage(self.BACKGROUND_SLOT)
			self.backgroundSlotImage[i].Hide()
			y = y + 32
		
		
		self.itemImage = ui.ImageBox()
		self.itemImage.SetParent(self)
		self.itemImage.SetPosition(0,0)
		self.itemImage.SAFE_SetStringEvent("MOUSE_OVER_IN",self.ShowToolTip)
		self.itemImage.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.HideToolTip)
		self.itemImage.Show()
		
		self.itemCountTextLine = ui.TextLine()
		self.itemCountTextLine.SetParent(self)
		self.itemCountTextLine.SetPosition(16,32-15)
		self.itemCountTextLine.SetText("100/100")
		self.itemCountTextLine.SetOutline()
		self.itemCountTextLine.SetFontColor(0.9, 0.4745, 0.4627)		
		self.itemCountTextLine.SetHorizontalAlignCenter()
		self.itemCountTextLine.Show()
	
	def ShowToolTip(self):
		if self.item > 0:
			self.toolTip.ClearToolTip()
			self.toolTip.AddItemData(self.item, [0, 0, 0, 0, 0, 0])
			self.toolTip.ShowToolTip()				
	
	def HideToolTip(self):
		self.toolTip.HideToolTip()
	
	
	def SetItemData(self,vnum):
		self.item = vnum
		item.SelectItem(vnum)
		self.itemImage.LoadImage(item.GetIconImageFileName())
		self.itemImage.Show()
	
	def ClearItemData(self):
		self.enable_item_check = False
		self.item = 0
		self.itemImage.Hide()
		self.SetItemCount(0)
		
	def Alpha(self,alpha):	
		self.itemImage.SetAlpha(alpha)
		
	# 1 - 3
	def SetSlotSize(self,size):	
		self.SetSize(32,32*size)
		self.itemCountTextLine.SetPosition(16,(32*size)-15)
		self.size = size
		
	def ShowBackgroundSlots(self):
		for i in xrange(self.size):
			self.backgroundSlotImage[i].Show()	

	def HideBackgroundSlots(self):
		for i in xrange(self.size):
			self.backgroundSlotImage[i].Hide()			
		
	def LoadCustomBackgroundSlots(self,image):
		for i in xrange(3):
			self.backgroundSlotImage[i].LoadImage(image)
	

	def SetItemCount(self,item_need_count):
		self.item_count_need = item_need_count
		if item_need_count == 0:
			self.itemCountTextLine.Hide()
			self.enable_item_check = False
		else:
			self.itemCountTextLine.Show()
			self.enable_item_check = True

	def DisableItemCheck(self):
		self.enable_item_check = False
	
	def UpdateRealItemCount(self):
		if self.enable_item_check:
			count = 0
			for i in range(0,(90*5)-1):
				if player.GetItemIndex(i) == self.item:
					count = count + player.GetItemCount(i)
					
			self.itemCountTextLine.SetText(str(count) + "/" + str(self.item_count_need))
			if count >= self.item_count_need:
				self.itemCountTextLine.SetFontColor(0.5411, 0.7254, 0.5568)
				self.Alpha(self.ALPHA_NORMAL)				
			else:
				self.itemCountTextLine.SetFontColor(0.9, 0.4745, 0.4627)
				self.Alpha(self.ALPHA_NEGATIVE)
			
	
	def OnUpdate(self):
		self.UpdateRealItemCount()
	
	
	def Clear(self):
		self.enable_item_check = False
		self.Hide()
		self.size = 1
		