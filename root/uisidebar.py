import ui
import wndMgr
import uiToolTip  
import constInfo
import background
import chat
import settinginfo


class SideBar(ui.ThinBoard):
	def __init__(self):
		ui.ThinBoard.__init__(self)
		
		self.ExpandBtn = ui.Button()
		self.ExpandBtn.SetParent(self)
		self.ExpandBtn.SetPosition(138, 0)
		self.ExpandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga")
		self.ExpandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga")
		self.ExpandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga")
		self.ExpandBtn.SetEvent(self.ToggleMinimize)
		self.ExpandBtn.Show()
		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()
		# self.itemtooltip.SetParent(self)
		# self.itemtooltip.SetFollow(False)
		# self.itemtooltip.SetPosition(50, (wndMgr.GetScreenHeight() - wndHeight) / 2)

		
		self.btns = []
		self.itemVnums = []
		self.minimized = 1
	
	def AddButton(self, text, event):
		height = len(self.btns) * 26
		wndHeight = max(108, 52 + height)
		
		self.SetSize(140, wndHeight)
		self.SetPosition(-126, (wndMgr.GetScreenHeight() - wndHeight) / 2)
		self.ExpandBtn.SetPosition(126, (wndHeight - 108) / 2)
		# self.itemtooltip.SetPosition(260, (wndMgr.GetScreenHeight() - wndHeight) / 2)
		
		btn = ui.Button()
		btn.SetParent(self)
		btn.SetPosition(35, 15 + height)
		btn.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		btn.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		btn.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		btn.SetText(text)
		btn.SetEvent(event)
		btn.Show()
		
		self.btns.append(btn)
		
		
	def AddSlot(self,itemVnum,event):
	
		height = len(self.btns) * 40
		wndHeight = max(108, 52 + height)
		
		self.SetSize(140, wndHeight)
		self.SetPosition(-126, (wndMgr.GetScreenHeight() - wndHeight) / 2)
		self.ExpandBtn.SetPosition(126, (wndHeight - 108) / 2)
	
		btn = ui.GridSlotWindow()  
		btn.SetParent(self)  
		btn.ArrangeSlot(len(self.btns),1,1,32,32,0,0)  
		btn.SetPosition(80, 15 + height) 
		btn.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		btn.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
		#btn.SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
		btn.SetSelectItemSlotEvent(event)  
		btn.Show()
		btn.SetItemSlot(len(self.btns),itemVnum,0)	
		
		self.itemVnums.append(itemVnum)
		self.btns.append(btn)

		
	def ShowToolTip(self,slot):
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"Slot: " + str(slot))
		self.itemtooltip.ClearToolTip()
		self.itemtooltip.AddItemData(self.itemVnums[slot], [0, 0, 0, 0, 0, 0])
		self.itemtooltip.ShowToolTip()
		
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()		
		
	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Destroy(self):
		self.Hide()
		for obj in self.btns:
			obj.Hide()
			obj = None
		del self.btns[:]
		self.btns = None
		
		for obj in self.itemVnums:
			#obj.Hide()
			obj = None
		del self.itemVnums[:]
		self.itemVnums = None		
		

	def OnUpdate(self):
		if self.minimized == 1:
			(x, y) = self.GetGlobalPosition()
			if x > -126:
				self.SetPosition(max(-126, x - 4), (wndMgr.GetScreenHeight() - (30 + len(self.btns) * 26)) / 2)
		else:
			(x, y) = self.GetGlobalPosition()
			if x < -65:
				self.SetPosition(min(-65, x + 4), (wndMgr.GetScreenHeight() - (30 + len(self.btns) * 26)) / 2)
				
		# if settinginfo.switchbot_minimize >= 1:
			# self.btns[0].ActivateSlot(0)	
		# else:
			# self.btns[0].DeactivateSlot(0)	
			
		# if constInfo.YangChatStatus == 1:
			# self.btns[5].ActivateSlot(5)	
		# else:
			# self.btns[5].DeactivateSlot(5)	
			
		# if constInfo.AntiExpStatus == 1:
			# self.btns[2].ActivateSlot(2)	
		# else:
			# self.btns[2].DeactivateSlot(2)				
			
		# if settinginfo.autoPotionStatus == 1:
			# self.btns[6].ActivateSlot(6)	
		# else:
			# self.btns[6].DeactivateSlot(6)				
		
	def ToggleMinimize(self):
		
		if background.GetCurrentMapName() == "map_login" or background.GetCurrentMapName() == "map_intro":
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Du kannst die Sidebar hier nicht öffnen!")
			return
		else:
			if self.minimized == 1:
				self.minimized = 0
				self.ExpandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_normal.tga")
				self.ExpandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_over.tga")
				self.ExpandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_expand_down.tga")
			else:
				self.minimized = 1
				self.ExpandBtn.SetUpVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_normal.tga")
				self.ExpandBtn.SetOverVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_over.tga")
				self.ExpandBtn.SetDownVisual("d:/ymir work/ui/game/belt_inventory/btn_minimize_down.tga")

