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
import settinginfo


warps = [
	[
		["Reiche Map 1"],
		[
			["Blaues Reich (Map 1)",1,3,"NOFLAG",0,0,0,0],
			["Rotes Reich (Map 1)",1,1,"NOFLAG",0,0,0,0],
			["Gelbes Reich (Map 1)",1,2,"NOFLAG",0,0,0,0]
		]

	],
	
	[
		["Reiche Map 2"],
		[
			["Blaues Reich (Map 2)",1,28,"NOFLAG",0,0,0,0],
			["Rotes Reich (Map 2)",1,29,"NOFLAG",0,0,0,0],
			["Gelbes Reich (Map 2)",1,30,"NOFLAG",0,0,0,0]
		]

	],

	[
		["Dungeons"],
		[
			["Bruthöhle",20,4,"NOFLAG",0,0,0,0],
			["Dämonenturm",40,6,"NOFLAG",0,0,0,0],
			["Drachenraum",75,7,"NOFLAG",0,0,0,0],
			["Katakomben",90,33,"NOFLAG",0,0,0,0],
			["Sturm auf die Runenfestung",100,10,"NOFLAG",0,0,0,0],
			["Rotdrachen-Festung",110,11,"NOFLAG",0,0,0,0],
			["Nemere's Warte",130,34,"NOFLAG",0,0,0,0]
			#["Schiffbruchtal",120,12,"NOFLAG",0]
		]

	],
	
	[
		["Sonstige"],
		[
			["Spinnendungeon 1",1,13,"NOFLAG",0,0,0,0],
			["Spinnendungeon 2",1,13,"NOFLAG",0,0,0,0],
			["Geisterwald",1,15,"NOFLAG",0,0,0,0],
			["Roter Wald",1,16,"NOFLAG",0,0,0,0],
			["Tempel",1,17,"NOFLAG",0,0,0,0],
			["Orktal",1,18,"NOFLAG",0,0,0,0],
			["Eisland",1,19,"NOFLAG",0,0,0,0],
			["Feuerland",1,20,"NOFLAG",0,0,0,0],
			["Wüste",1,21,"NOFLAG",0,0,0,0]
		]

	],

	[
		["Farmmaps"],
		[
			["Orktal",10,22,"NOFLAG",0,70,0,0],
			["Eisland",50,23,"NOFLAG",0,90,0,0],
			["Feuerland",50,35,"NOFLAG",0,90,60002,1],
			["Farmmap 3",75,24,"NOFLAG",0,135,0,0],
			["Farmmap 4",100,25,"NOFLAG",0,0,0,0],
			["Farmmap 5",135,26,"NOFLAG",0,0,0,0]
			

		]

	],
	[
		["Levelmaps"],
		[
			["Levelmap 1",90,27,"NOFLAG",0,0,0,0],

		]

	],
	
	[
		["Bossmap"],
		[
			["Anfang",1,28,"NOFLAG",0,0,0,0],
			["Zufall",1,29,"NOFLAG",0,0,0,0]

		]

	],
	[
		["Eventmaps"],
		[
			["Test",1,30,"eventmap_1",1,0,0,0],
			["Test 2",100,31,"eventmap_2",1,0,0,0]

		]

	],


]



board_count = 8
class WarpBoard(ui.ScriptWindow):
	NavButtons = {}	
	NavButtonTitles = {}
	
	
	WarpBGImages = {}
	WarpThinBoards = {}
	WarpTitleUnderLines = {}
	WarpMapNames = {}
	WarpButtons = {}
	WarpButtonTitles = {}
	WarpErrors = {}
	WarpClosed = {}
	WarpItemSlots = {}
	sel_cat = 0
		
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()

	def __del__(self):
		#constInfo.CALOPEN = 1
		constInfo.warpgui_open = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()

		
	def LoadUI(self):
		constInfo.warpgui_open = 1
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(700, 350)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Teleportation")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()
		
		self.NavThinBoard = ui.ThinBoard()
		self.NavThinBoard.SetParent(self.Board)
		self.NavThinBoard.SetPosition(15,35)
		self.NavThinBoard.SetSize(110,305)
		self.NavThinBoard.Show()
		self.itemtooltip = uiToolTip.ItemToolTip()  
		self.itemtooltip.HideToolTip()		
		i = 0
		nb_height = 10
		
		while i < len(warps):
		
			self.NavButtons[i] = ui.Button()
			self.NavButtons[i].SetParent(self.NavThinBoard)
			self.NavButtons[i].SetPosition(10,nb_height)
			self.NavButtons[i].SetText("")
			self.NavButtons[i].SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			self.NavButtons[i].SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			self.NavButtons[i].SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			self.NavButtons[i].SetEvent(ui.__mem_func__(self.LoadCategory), i)
			self.NavButtons[i].Show()

			self.NavButtonTitles[i] = ui.TextLine()
			self.NavButtonTitles[i].SetParent(self.NavButtons[i])
			self.NavButtonTitles[i].SetPosition(43,2)
			self.NavButtonTitles[i].SetText(str(warps[i][0][0]))
			self.NavButtonTitles[i].SetHorizontalAlignCenter()
			self.NavButtonTitles[i].Show()
			
			
			i = i + 1
			nb_height = nb_height + 22
		
		

		step = 5
		i = 1
		aIndex = 0
		wtb_width = 130
		wtb_height = 35
		player_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
		
		while i <= board_count:	
			self.WarpBGImages[i] = ui.ImageBox()
			self.WarpBGImages[i].SetParent(self.Board)
			self.WarpBGImages[i].SetPosition(wtb_width,wtb_height)
			self.WarpBGImages[i].LoadImage("images_warpgui/map/map_0_0.tga")
			self.WarpBGImages[i].Show()
			
			self.WarpThinBoards[i] = ui.ThinBoard()
			self.WarpThinBoards[i].SetParent(self.WarpBGImages[i])
			self.WarpThinBoards[i].SetSize(130,150)
			self.WarpThinBoards[i].SetPosition(0,0)
			self.WarpThinBoards[i].Show()
			
			
			self.WarpMapNames[i] = ui.TextLine()
			self.WarpMapNames[i].SetParent(self.WarpThinBoards[i])
			self.WarpMapNames[i].SetPosition(65,8)
			self.WarpMapNames[i].SetText("MapName")
			self.WarpMapNames[i].SetHorizontalAlignCenter()
			self.WarpMapNames[i].Show()			
			self.WarpTitleUnderLines[i] = ui.ImageBox()
			self.WarpTitleUnderLines[i].SetParent(self.WarpThinBoards[i])
			self.WarpTitleUnderLines[i].SetPosition(5,25)
			self.WarpTitleUnderLines[i].LoadImage("images_warpgui/title_underline.tga")
			self.WarpTitleUnderLines[i].Show()			
			
			self.WarpButtons[i] = ui.Button()
			self.WarpButtons[i].SetParent(self.WarpThinBoards[i])
			self.WarpButtons[i].SetPosition(22,125)
			self.WarpButtons[i].SetText("")
			self.WarpButtons[i].SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			self.WarpButtons[i].SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			self.WarpButtons[i].SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			self.WarpButtons[i].SetEvent(ui.__mem_func__(self.SendWarpPacket), i)
			self.WarpButtons[i].Show()			
				
			self.WarpButtonTitles[i] = ui.TextLine()
			self.WarpButtonTitles[i].SetParent(self.WarpButtons[i])
			self.WarpButtonTitles[i].SetPosition(43,2)
			self.WarpButtonTitles[i].SetText("Teleportieren")
			self.WarpButtonTitles[i].SetHorizontalAlignCenter()
			self.WarpButtonTitles[i].Show()			
			
			self.WarpErrors[i] = ui.TextLine()
			self.WarpErrors[i].SetParent(self.WarpThinBoards[i])
			self.WarpErrors[i].SetPosition(65,125)
			self.WarpErrors[i].SetText("[ Ab lv. ]")
			self.WarpErrors[i].SetHorizontalAlignCenter()
			self.WarpErrors[i].Show()	

			self.WarpItemSlots[i] = ui.GridSlotWindow()  
			self.WarpItemSlots[i].SetParent(self.WarpThinBoards[i])  
			self.WarpItemSlots[i].ArrangeSlot(i,1,1,32,32,0,0)  
			self.WarpItemSlots[i].SetPosition(49,75)  
			self.WarpItemSlots[i].SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
			self.WarpItemSlots[i].SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
			self.WarpItemSlots[i].Show()			
			# self.WarpItemSlots[i].SetItemSlot(0,27001,1)
			
			self.WarpClosed[i] = ui.TextLine()
			self.WarpClosed[i].SetParent(self.WarpThinBoards[i])
			self.WarpClosed[i].SetPosition(65,95)
			self.WarpClosed[i].SetText("[ Geschlossen! ]")
			self.WarpClosed[i].SetHorizontalAlignCenter()
			self.WarpClosed[i].Hide()
			
			aIndex = aIndex + 1
			i = i + 1
			wtb_width = wtb_width + 135
			if i == step:
				wtb_width = 130
				wtb_height = 190
		
		self.scrollbar = ui.ScrollBar()
		self.scrollbar.SetParent(self.Board)
		self.scrollbar.SetScrollBarSize(305)
		self.scrollbar.SetPosition(670, 35)	
		self.scrollbar.SetMiddleBarSize(float(board_count) / float(8))
		self.scrollbar.SetScrollEvent(self.__OnScroll)
		self.scrollbar.Show()		
		self.LoadCategory(0)

	def ResetUI(self):
		i = 1
		while i <= board_count:
			self.WarpBGImages[i].Hide()
			self.WarpClosed[i].Hide()
			i = i + 1
		
		
		
		
		
	def LoadCategory(self,idx):
		self.ResetUI()
		self.sel_cat = idx
		
		
		if len(warps[self.sel_cat][1]) > 8:
			self.scrollbar.Show()
			self.Board.SetSize(700, 355)

			self.scrollbar.SetMiddleBarSize(float(board_count) / float(len(warps[self.sel_cat][1])))
			self.scrollbar.SetPos(0)
			board_count_load = 8
		else:
			self.scrollbar.Hide()
			self.Board.SetSize(680, 355)
			board_count_load = len(warps[self.sel_cat][1])
			
		i = 1
		aIndex = 0
		while i <= board_count_load:
			self.WarpMapNames[i].SetText(str(warps[self.sel_cat][1][aIndex][0]))
			if warps[self.sel_cat][1][aIndex][2] != 0:
				self.WarpBGImages[i].LoadImage("images_warp/map_" + str(warps[self.sel_cat][1][aIndex][2]) + ".tga")
			else:
				self.WarpBGImages[i].LoadImage("images_warp/unknown.tga")
			player_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
			
			if warps[self.sel_cat][1][aIndex][5] > 0:
				if player_level >= warps[self.sel_cat][1][aIndex][1] and player_level <= warps[self.sel_cat][1][aIndex][5]:
					self.WarpButtons[i].Show()
					#self.WarpErrors[i].Hide()
					self.WarpErrors[i].SetPosition(65,110)
				else:
					self.WarpErrors[i].SetPosition(65,125)
					self.WarpButtons[i].Hide()
					self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][aIndex][1]) + " - lv." + str(warps[self.sel_cat][1][aIndex][5]) + " ]")
					self.WarpErrors[i].Show()			
			else:
				if player_level >= warps[self.sel_cat][1][aIndex][1]:
					self.WarpButtons[i].Show()
					#self.WarpErrors[i].Hide()
					self.WarpErrors[i].SetPosition(65,110)
				else:
					self.WarpErrors[i].SetPosition(65,125)
					self.WarpButtons[i].Hide()
					self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][aIndex][1]) + " ]")
					self.WarpErrors[i].Show()

			if warps[self.sel_cat][1][aIndex][3] != "NOFLAG":
				if settinginfo.searchForEventFlag(warps[self.sel_cat][1][aIndex][3],warps[self.sel_cat][1][aIndex][4]) == False:
					self.WarpButtons[i].Hide()
					self.WarpClosed[i].Show()
					self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][aIndex][1]) + " ]")
					self.WarpErrors[i].Show()

				else:
					self.WarpButtons[i].Show()
					self.WarpClosed[i].Hide()
					self.WarpErrors[i].Hide()
					if player_level < warps[self.sel_cat][1][aIndex][1]:
						self.WarpButtons[i].Hide()
						self.WarpErrors[i].Show()
						
			if warps[self.sel_cat][1][aIndex][6] != 0:
				self.WarpItemSlots[i].SetItemSlot(i,warps[self.sel_cat][1][aIndex][6],warps[self.sel_cat][1][aIndex][7])
			else:
				self.WarpItemSlots[i].SetItemSlot(i,0,0)
			self.WarpItemSlots[i].RefreshSlot()
			self.WarpBGImages[i].Show()
			aIndex = aIndex + 1
			i = i + 1			
		
		
	def SendWarpPacket(self,btn_idx):
		if len(warps[self.sel_cat][1]) <= 8:
			
			btn_idx = btn_idx - 1
			#chat.AppendChat(chat.CHAT_TYPE_INFO,"warp#" + str(self.sel_cat) + "#" + str(btn_idx))
			
			constInfo.INPUT_CMD = "WARP#" + str(self.sel_cat) + "#" + str(btn_idx) + "#"
			event.QuestButtonClick(constInfo.warpgui_qid)	
			
			
			#chat.AppendChat(chat.CHAT_TYPE_INFO,str(constInfo.INPUT_CMD))
	
		else:
			pos = int(self.scrollbar.GetPos() * (len(warps[self.sel_cat][1]) - board_count))
			realPos = (btn_idx + pos) - 1

			constInfo.INPUT_CMD = "WARP#" + str(self.sel_cat) + "#" + str(realPos) + "#"
			event.QuestButtonClick(constInfo.warpgui_qid)	

		self.__del__()

	def __OnScroll(self):
		self.ResetUI()
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"scrollbar.pos=" + str(self.scrollbar.GetPos()))
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"sel_cat=" + str(self.sel_cat))
		pos = int(self.scrollbar.GetPos() * (len(warps[self.sel_cat][1]) - board_count)) ##Aktuelle Position der Scrollbar
		#self.Board.SetTitleName("Teleportation + " + str(pos))
		i = 1
		while i <= board_count:
			realPos = (i + pos) - 1
			if realPos+1 <= len(warps[self.sel_cat][1]):
				self.WarpMapNames[i].SetText(str(warps[self.sel_cat][1][realPos][0]))
				player_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
				
				if warps[self.sel_cat][1][realPos][5] > 0:
					if player_level >= warps[self.sel_cat][1][realPos][1] and player_level <= warps[self.sel_cat][1][realPos][5]:
						self.WarpButtons[i].Show()
						#self.WarpErrors[i].Hide()
						self.WarpErrors[i].SetPosition(65,110)
					else:
						self.WarpErrors[i].SetPosition(65,125)
						self.WarpButtons[i].Hide()
						self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " - lv." + str(warps[self.sel_cat][1][realPos][5]) + " ]")
						self.WarpErrors[i].Show()					
				else:
					if player_level >= warps[self.sel_cat][1][realPos][1]:
						self.WarpButtons[i].Show()
						#self.WarpErrors[i].Hide()
						self.WarpErrors[i].SetPosition(65,110)
					else:
						self.WarpErrors[i].SetPosition(65,125)
						self.WarpButtons[i].Hide()
						self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " ]")
						self.WarpErrors[i].Show()		
					
				if warps[self.sel_cat][1][realPos][2] != 0:
					self.WarpBGImages[i].LoadImage("images_warp/map_" + str(warps[self.sel_cat][1][realPos][2]) + ".tga")
				else:
					self.WarpBGImages[i].LoadImage("images_warp/unknown.tga")	

				if warps[self.sel_cat][1][realPos][3] != "NOFLAG":
					if settinginfo.searchForEventFlag(warps[self.sel_cat][1][realPos][3],warps[self.sel_cat][1][realPos][4]) == False:
						self.WarpButtons[i].Hide()
						self.WarpClosed[i].Show()
						self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " ]")
						self.WarpErrors[i].Show()

					else:
						self.WarpButtons[i].Show()
						self.WarpClosed[i].Hide()
						self.WarpErrors[i].Hide()
						if player_level < warps[self.sel_cat][1][realPos][1]:
							self.WarpButtons[i].Hide()	
							self.WarpErrors[i].Show()

				if warps[self.sel_cat][1][realPos][6] != 0:
					self.WarpItemSlots[i].SetItemSlot(i,warps[self.sel_cat][1][realPos][6],warps[self.sel_cat][1][realPos][7])
				else:
					self.WarpItemSlots[i].SetItemSlot(i,0,0)
				self.WarpItemSlots[i].RefreshSlot()
				self.WarpBGImages[i].Show()
							
				self.WarpBGImages[i].Show()		
			i = i + 1
			
			
	def OnUpdate(self):
		if len(warps[self.sel_cat][1]) <= 8:
		
			i = 1
			
			while i <= board_count:
				if i <= len(warps[self.sel_cat][1]):
					player_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
					if warps[self.sel_cat][1][i-1][5] > 0:
						if player_level >= warps[self.sel_cat][1][i-1][1] and player_level <= warps[self.sel_cat][1][i-1][5]:
							self.WarpButtons[i].Show()
							#self.WarpErrors[i].Hide()
							self.WarpErrors[i].Show()
							self.WarpErrors[i].SetPosition(65,110)
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][i-1][1]) + " - lv." + str(warps[self.sel_cat][1][i-1][5]) + " ]")
						else:
							self.WarpErrors[i].SetPosition(65,125)
							self.WarpButtons[i].Hide()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][i-1][1]) + " - lv." + str(warps[self.sel_cat][1][i-1][5]) + " ]")
							self.WarpErrors[i].Show()					
					else:
					
						if player_level >= warps[self.sel_cat][1][i-1][1]:
							self.WarpButtons[i].Show()
							#self.WarpErrors[i].Hide()
							self.WarpErrors[i].Show()
							self.WarpErrors[i].SetPosition(65,110)
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][i-1][1]) + " ]")
							
						else:
							self.WarpErrors[i].SetPosition(65,125)
							self.WarpButtons[i].Hide()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][i-1][1]) + " ]")
							self.WarpErrors[i].Show()

					if warps[self.sel_cat][1][i-1][3] != "NOFLAG":
						if settinginfo.searchForEventFlag(warps[self.sel_cat][1][i-1][3],warps[self.sel_cat][1][i-1][4]) == False:
							self.WarpButtons[i].Hide()
							self.WarpClosed[i].Show()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][i-1][1]) + " ]")
							self.WarpErrors[i].Show()
						else:
							self.WarpButtons[i].Show()
							self.WarpClosed[i].Hide()
							self.WarpErrors[i].Hide()	
							if player_level < warps[self.sel_cat][1][i-1][1]:
								self.WarpButtons[i].Hide()
								self.WarpErrors[i].Show()								
						
				i = i + 1
		else:
			self.ResetUI()
			pos = int(self.scrollbar.GetPos() * (len(warps[self.sel_cat][1]) - board_count))			

			i = 1
			while i <= board_count:
				realPos = (i + pos) - 1
				if realPos+1 <= len(warps[self.sel_cat][1]):
					self.WarpMapNames[i].SetText(str(warps[self.sel_cat][1][realPos][0]))
					player_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)
					
					if warps[self.sel_cat][1][realPos][5] > 0:
						if player_level >= warps[self.sel_cat][1][realPos][1] and player_level <= warps[self.sel_cat][1][realPos][5]:
							self.WarpButtons[i].Show()
							#self.WarpErrors[i].Hide()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " - lv." + str(warps[self.sel_cat][1][realPos][5]) + " ]")
							self.WarpErrors[i].SetPosition(65,110)
							self.WarpErrors[i].Show()
						else:
							self.WarpErrors[i].SetPosition(65,125)
							self.WarpButtons[i].Hide()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " - lv." + str(warps[self.sel_cat][1][realPos][5]) + " ]")
							self.WarpErrors[i].Show()					
					else:
					
						if player_level >= warps[self.sel_cat][1][realPos][1]:
							self.WarpButtons[i].Show()
							self.WarpErrors[i].SetPosition(65,110)
							#self.WarpErrors[i].Hide()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " ]")
							self.WarpErrors[i].Show()
						else:
							self.WarpButtons[i].Hide()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " ]")
							self.WarpErrors[i].Show()
						
					if warps[self.sel_cat][1][realPos][3] != "NOFLAG":
						if settinginfo.searchForEventFlag(warps[self.sel_cat][1][realPos][3],warps[self.sel_cat][1][realPos][4]) == False:
							self.WarpButtons[i].Hide()
							self.WarpClosed[i].Show()
							self.WarpErrors[i].SetText("[ Ab lv." + str(warps[self.sel_cat][1][realPos][1]) + " ]")
							self.WarpErrors[i].Show()
						else:
							self.WarpButtons[i].Show()
							self.WarpClosed[i].Hide()
							self.WarpErrors[i].Hide()	
							if player_level < warps[self.sel_cat][1][realPos][1]:
								self.WarpButtons[i].Hide()	
								self.WarpErrors[i].Show()
					self.WarpBGImages[i].Show()		
					i = i + 1			
	
	def ShowToolTip(self,slotIndex):
		self.itemtooltip.ClearToolTip()
		if len(warps[self.sel_cat][1]) <= 8:
			slotIndex = slotIndex - 1
			self.itemtooltip.AddItemData(warps[self.sel_cat][1][slotIndex][6], [0, 0, 0, 0, 0, 0])	
		else:
			pos = int(self.scrollbar.GetPos() * (len(warps[self.sel_cat][1]) - board_count))
			realPos = (slotIndex + pos) - 1
			self.itemtooltip.AddItemData(warps[self.sel_cat][1][realPos][6], [0, 0, 0, 0, 0, 0])	
	
	def HideToolTip(self):
		self.itemtooltip.HideToolTip()
	
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE	

	
#WarpBoard().Show()