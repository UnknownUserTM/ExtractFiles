import ui
import GFHhg54GHGhh45GHGH
import app
import chat
import item
import event
import fgGHGjjFHJghjfFG1545gGG
import wndMgr
import constInfo
import uiToolTip
import mouseModule

class KeyTreasureGui(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Hide()
		self.old_time = app.GetTime()
		self.xyScale = 0.1
		self.yPic = 32
		self.isScaling = 0
		self.__EasyBuild = EasyBuildKilroy()

	def Configuration(self, cmd):
		CMD = cmd.split("/")
		if CMD[0]=="qid":
			constInfo.KEY_TREASURE_CONFIG["QID"] = int(CMD[1])
		elif CMD[0]=="input":
			GFHhg54GHGhh45GHGH.SendQuestInputStringPacket(str(constInfo.KEY_TREASURE_CONFIG["CMD"]))
			constInfo.KEY_TREASURE_CONFIG["CMD"] = ""
		elif CMD[0]=="item":
			item.SelectItem(int(CMD[1]))
			itemIcon = item.GetIconImageFileName()
			self.ItemPicture.LoadImage(itemIcon)
			self.yPic = {32:20, 64:35, 96:45}.get(self.ItemPicture.GetHeight(), 33.33)
			self.ItemPicture.SetScale(0.1, 0.1)
			self.ItemPicture.SetPosition(380, 150)
			self.xyScale = 0.1
			self.TreasurePic.Start()
			self.isScaling = 1

	def BuildWindow(self):
		self.KeyTreasureBoard = self.__EasyBuild.CreateBoardWithTitle(-1, -1, 635, 450)
		self.KeyTreasureBoard.SetTitleName("Spezial Truhen")
		self.KeyTreasureBoard.SetCloseEvent(self.Open)
		self.KeyTreasureBoard.SetCenterPosition()

		self.OpenTreasureButton = self.__EasyBuild.CreateButton(
												self.KeyTreasureBoard, 80, 300, "Truhe öffnen",
												self.__OpenTreasure,
												"d:/ymir work/ui/public/large_button_01.sub",
												"d:/ymir work/ui/public/large_button_02.sub",
												"d:/ymir work/ui/public/large_button_03.sub",
												-1,
												""
											)

		self.TreasurePic = AniImageBox()
		self.TreasurePic.SetParent(self.KeyTreasureBoard)
		self.TreasurePic.SetPosition(220,35)
		for i in range(1,15):
			self.TreasurePic.AddImage("locale/de/ui/interfaces/special_cases/frame-%02d.tga" % i)
		self.TreasurePic.Show()
		self.TreasurePic.OnFrameEnd(1)
		self.TreasurePic.SetDelay(0.1)

		self.ItemPicture = self.__EasyBuild.CreateImage(self.KeyTreasureBoard, 380, 150, None)

		self.SlotGridTableHead = self.__EasyBuild.CreateTextLine(self.KeyTreasureBoard, 30,175, "Wähle einen Schlüssel", "normal")
		self.SlotGridTable = self.__EasyBuild.CreateGridSlotWindow(self.KeyTreasureBoard, 30, 190, [0, 5, 1, 32, 32, 0, 0], "d:/ymir work/ui/public/Slot_Base.sub")
		self.SlotGridTable.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.SlotGridTable.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.SlotGridTable.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.SlotGridTable.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.SlotGridTable.SAFE_SetButtonEvent("RIGHT", "EXIST", self.OnRightClickSlot)
		self.SlotGridTable.SetUsableItem(True)

		self.SlotGridTable2Head = self.__EasyBuild.CreateTextLine(self.KeyTreasureBoard, 30,235, "Wähle eine Truhe", "normal")
		self.SlotGridTable2 = self.__EasyBuild.CreateGridSlotWindow(self.KeyTreasureBoard, 30, 250, [5, 5, 1, 32, 32, 0, 0], "d:/ymir work/ui/public/Slot_Base.sub")
		self.SlotGridTable2.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.SlotGridTable2.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.SlotGridTable2.SAFE_SetButtonEvent("RIGHT", "EXIST", self.OnRightClickSlot)
		self.SlotGridTable2.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.SlotGridTable2.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.SlotGridTable2.SetUsableItem(True)

		self.toolTip = uiToolTip.ItemToolTip()

		self.ItemSlot = []
		for i in range(0,10):
			self.ItemSlot += [ [-1,-1,-1,0] ]

		self.Show()

	def SelectEmptySlot(self, itemSlotIndex):
		slot = self.GetSlot(itemSlotIndex)
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == attachedSlotType:
				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				itemIndex = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(attachedSlotPos)
				itemCount = fgGHGjjFHJghjfFG1545gGG.GetItemCount(attachedSlotPos)
				item.SelectItem(itemIndex)
				x,y = item.GetItemSize()
				mouseModule.mouseController.DeattachObject()
				if int(x)==1 and int(y)!=1:
					return
				for i in xrange(len(self.ItemSlot)):
					if self.ItemSlot[i][0]==attachedSlotPos:
						s = self.GetSlot(i)
						self.ItemSlot[i] = [-1,-1,-1,0]
						s.ClearSlot(i)
						s.DeactivateSlot(i)
				self.ItemSlot[itemSlotIndex] = [int(attachedSlotPos), itemIndex, itemCount, 0]
				slot.SetItemSlot(itemSlotIndex, itemIndex, itemCount)
				slot.RefreshSlot()

	def OnRightClickSlot(self, slotNumber):
		slot = self.GetSlot(slotNumber)
		if self.ItemSlot[slotNumber][3]==1:
			slot.DeactivateSlot(slotNumber)
			self.ItemSlot[slotNumber][3] = 0
		else:
			a,b = self.GetActivSlots()
			if (len(a)<4 and slotNumber<5) or (len(b)<4 and slotNumber>4):
				slot.ActivateSlot(slotNumber)
				self.ItemSlot[slotNumber][3] = 1

	def SelectItemSlot(self, itemSlotIndex):
		slot = self.GetSlot(itemSlotIndex)
		isAttached = mouseModule.mouseController.isAttached()
		if not isAttached:
			slot.ClearSlot(itemSlotIndex)
			slot.DeactivateSlot(itemSlotIndex)
			slot.RefreshSlot()
			self.ItemSlot[itemSlotIndex] = [-1,-1,-1,0]

	def OverInItem(self, slotNumber):
		if self.toolTip:
			if self.ItemSlot[slotNumber][0]!=-1:
				self.toolTip.SetInventoryItem(self.ItemSlot[slotNumber][0])

	def OnOverOutItem(self):
		self.toolTip.Hide()

	def __OpenTreasure(self):
		a,b = self.GetActivSlots()
		if len(a)==4 and len(b)==4:
			self.TreasurePic.Reset()
			slots = [a] + [b]
			SendString = ','.join(map(str, [i[0] for i in slots]))
			constInfo.KEY_TREASURE_CONFIG["CMD"] = ("input/%s" % SendString)
			event.QuestButtonClick(constInfo.KEY_TREASURE_CONFIG["QID"])
		else:
			chat.AppendChat(1, "Wähle zuerst einen Schlüssel und eine Truhe aus!")

	def OnUpdate(self):
		if self.isScaling and (self.old_time + 0.05) < app.GetTime():
			self.xyScale += 0.1
			self.old_time = app.GetTime() 

			self.ItemPicture.SetScale(self.xyScale, self.xyScale)
			self.ItemPicture.SetPosition(380-(self.xyScale*17), 150-(self.xyScale*self.yPic))
			if self.xyScale > 2:
				self.isScaling = 0

		for i in xrange(len(self.ItemSlot)):
			if self.ItemSlot[i][0] != -1:
				if fgGHGjjFHJghjfFG1545gGG.GetItemIndex(self.ItemSlot[i][0]) != self.ItemSlot[i][1] or fgGHGjjFHJghjfFG1545gGG.GetItemCount(self.ItemSlot[i][0]) != self.ItemSlot[i][2]:
					slot = self.GetSlot(i)
					slot.ClearSlot(i)
					slot.DeactivateSlot(i)
					slot.RefreshSlot()
					self.ItemSlot[i] = [-1,-1,-1,0]

	def GetActivSlots(self):
		a, b = [], []
		for i in xrange(len(self.ItemSlot)):
			if self.ItemSlot[i][3]==1 and i<5:
				a = self.ItemSlot[i]
			elif self.ItemSlot[i][3]==1 and i>4:
				b = self.ItemSlot[i]
		return a,b

	def GetSlot(self, n):
		if n<5:
			return self.SlotGridTable
		else:
			return self.SlotGridTable2

	def Open(self):
		if self.IsShow():
			self.KeyTreasureBoard.Hide()
			self.Hide()
			return
		self.BuildWindow()


class EasyBuildKilroy():

	def CreateBoardWithTitle(self, x, y, width, height):
		board = ui.BoardWithTitleBar()
		board.SetSize(width, height)
		board.SetPosition(x, y)
		board.AddFlag("movable")
		board.Show()
		return board

	def CreateGridSlotWindow(self, parent, x, y, arrayslot, image):
		gridslotwindow = ui.GridSlotWindow()
		gridslotwindow.SetParent(parent)
		gridslotwindow.SetPosition(x, y)
		gridslotwindow.ArrangeSlot(arrayslot[0], arrayslot[1], arrayslot[2], arrayslot[3], arrayslot[4], arrayslot[5], arrayslot[6])
		wndMgr.SetSlotBaseImage(gridslotwindow.hWnd, image, 1.0, 1.0, 1.0, 1.0)
		gridslotwindow.Show()
		return gridslotwindow

	def CreateButton(self, parent, x, y, text, func, up, over, down, f_event=None, tooltip=""):
		button = ui.Button()
		button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(up)
		button.SetOverVisual(over)
		button.SetDownVisual(down)
		button.SetText(text)
		button.SetEvent(func)
		if f_event!=None:
			button.SetEvent(ui.__mem_func__(func), f_event)

		if tooltip!="":
			button.SetToolTipText(tooltip)

		button.Show()
		return button

	def CreateImage(self, parent, x, y, path=None, not_pick=TRUE):
		image = ui.ExpandedImageBox()
		image.SetParent(parent)
		if not_pick:
			image.AddFlag("not_pick")
		image.SetPosition(x,y)
		if path!=None:
			image.LoadImage(path)
		image.Show()
		return image

	def CreateTextLine(self, parent, x, y, text, align="center"):
		textline = ui.TextLine()
		textline.SetParent(parent)
		textline.SetPosition(x,y)
		textline.SetText(text)
		if align=="center":
			textline.SetHorizontalAlignCenter()
		textline.Show()
		return textline


class AniImageBox(ui.Window):
	def __init__(self, layer = "UI"):
		ui.Window.__init__(self, layer)

		self.width = 0
		self.height = 0
		self.imageList = []
		self.Selected = -1
		self.old_time = app.GetTime()
		self.delay = 10.0
		self.isOn = 0
		self.isStop = 0

		image = ui.ImageBox()
		image.SetParent(self)
		image.SetPosition(0,0)
		image.Hide()
		self.Image = image

	def __del__(self):
		ui.Window.__del__(self)

	def RemoveImage(self, i):
		del self.imageList[i]
		self.ArrangeButtons()

	def AddImage(self, path):
		self.imageList.append(path)
		self.ArrangeButtons()

	def ArrangeButtons(self):
		self.buttonList = []
		self.Image.Hide()
		self.Image.LoadImage(self.imageList[0])
		self.Image.Show()

	def Start(self):
		self.isOn = 1

	def Reset(self):
		self.Image.LoadImage(self.imageList[0])
		self.Selected = 0

	def Stop(self):
		self.isOn = 0

	def OnFrameEnd(self, n=1):
		self.isStop = n

	def SetDelay(self, d):
		self.delay = float(d)

	def SetSize(self, width, height):
		ui.Window.SetSize(self, width, height)
		self.width = width
		self.height = height

	def OnUpdate(self):
		if (self.old_time+self.delay) < app.GetTime() and self.isOn:

			self.old_time = app.GetTime()
			self.Selected +=1

			if self.Selected>len(self.imageList)-1:
				if self.isStop:
					self.isOn = 0
					return
				self.Selected = 0

			self.Image.LoadImage(self.imageList[self.Selected])
