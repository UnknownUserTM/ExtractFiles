import ui
import uiScriptLocale
import wndMgr
import fgGHGjjFHJghjfFG1545gGG
import miniMap
import localeInfo
import GFHhg54GHGhh45GHGH
import app
import colorInfo
import constInfo
import background
import time
import settinginfo
import chat
import item
import uiToolTip

BOSS_DATA = {
	"metin2_map_c3" : [
		[141,30,"Brutaler Hauptmann",20],
		[25,146,"Brutaler Hauptmann",20],
		[150,147,"Brutaler Hauptmann",20]
	],
	"metin2_map_a3" : [
		[118,15,"Brutaler Hauptmann",20],
		[15,87,"Brutaler Hauptmann",20],
		[142,147,"Brutaler Hauptmann",20]
	],
	"metin2_map_b3" : [
		[122,28,"Brutaler Hauptmann",20],
		[36,82,"Brutaler Hauptmann",20],
		[114,128,"Brutaler Hauptmann",20]
	],
	"map_a2" : [
		[105,115,"Oberork",20],
		[140,112,"Oberork",20],
		[130,142,"Oberork",20]
	],
	"metin2_map_n_flame_01" : [
		[27,138,"Flammenkönig",20],
		[157,18,"Flammenkönig",20],
		[235,70,"Flammenkönig",20],
		[103,65,"Flammenkönig",20],
		[204,232,"Flammenkönig",20]
	],
	"map_n_snowm_01" : [
		[160,77,"Neunschwanz",20],
		[64,144,"Neunschwanz",20],
		[201,126,"Neunschwanz",20],
		[224,219,"Neunschwanz",20],
		[128,201,"Neunschwanz",20]
	],
	"metin2_map_eastplain_01" : [
		[87,132,"Jabba the Hutt",20],
		[92,200,"Jabba the Hutt",20],
		[163,163,"Jabba the Hutt",20],
		[107,231,"Jabba the Hutt",20]
	],
	"metin2_map_eastplain_02" : [
		[101,14,"Der Große Oger",20],
		[37,108,"Der Große Oger",20],
		[23,219,"Der Große Oger",20],
		[90,224,"Der Große Oger",20],
		[92,288,"Der Große Oger",20]
	],
	"metin2_map_eastplain_03" : [
		[186,110,"Martyaxwar",20],
		[56,109,"Martyaxwar",20],
		[47,22,"Martyaxwar",20],
		[140,23,"Martyaxwar",20]
	],
}

SHOW_BOSS_ICON_POSITION_HELPER = True # Auf True ändern um koordinaten angezeigt zu bekommen.


class SwitchBotToolTipNEW(ui.Window):
	normalWidth = 200

	def __init__(self,wndMinimap):
		ui.Window.__init__(self)
		self.wndMinimap = wndMinimap
		self.SetSize(self.normalWidth,100)
		# self.dgWindow = dgWindow
		self.Hide()
		self.MakeToolTip()	
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def AdjustPosition(self):
		x, y = self.wndMinimap.GetGlobalPosition()
		# self.SetPosition(x - self.normalWidth - 10 + 22,(y + 630)-self.toolTip.toolTipHeight)
		self.SetPosition(wndMgr.GetScreenWidth() - 256 - 75 - 15 + 15,120)
		
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetParent(self)
		toolTip.SetPosition(1, 1)
		toolTip.SetFollow(False)
		toolTip.Show()
		self.toolTip = toolTip
		
	def GetItemNameBySlot(self,slot):
		itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(slot)
		item.SelectItem(itemvnum)
		
		return item.GetItemName()	
		
	def Open(self):
		self.Show()
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Open!")
		
		
	def OnUpdate(self):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine("Switchbot",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendDescription("Switchbot halt, was soll man dazu sonst noch schreiben. Grün = Aktiv, Rot = Inaktiv.",26)
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
		self.toolTip.AppendTextLine("Status:",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendSpace(5)
			
		for i in xrange(5):
			realSlot = i + 1
			if settinginfo.switchbot_switch_count[i] > 0:
				self.toolTip.AppendStatusTextLine("Slot " + str(realSlot) + " (" + self.GetItemNameBySlot(settinginfo.switchbot_Slots[i]) + ")",1)
			else:
				self.toolTip.AppendStatusTextLine("Slot " + str(realSlot),0)

		self.toolTip.AppendSpace(5)
		self.toolTip.ResizeToolTip()	
		self.AdjustPosition()
		# self.Show()
		
	def Close(self):
		self.Hide()
	

class TeamlerOnlineToolTipNEW(ui.Window):
	normalWidth = 200
	
	
	# dungeonCooldown = [
		# app.GetGlobalTimeStamp() + (1*60),
		# app.GetGlobalTimeStamp() + (15*60),
		# app.GetGlobalTimeStamp() + (3*60),
		# app.GetGlobalTimeStamp() + (5*60)
	# ]
	
	
	
	def __init__(self,wndMinimap):
		ui.Window.__init__(self)
		self.wndMinimap = wndMinimap
		self.SetSize(self.normalWidth,100)
		# self.dgWindow = dgWindow
		self.Hide()
		self.MakeToolTip()	
		
	def __del__(self):
		ui.Window.__del__(self)
		
	def AdjustPosition(self):
		x, y = self.wndMinimap.GetGlobalPosition()
		# self.SetPosition(x - self.normalWidth - 10 + 22,(y + 630)-self.toolTip.toolTipHeight)
		self.SetPosition(wndMgr.GetScreenWidth() - 256 - 75 - 15,100)
		
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetParent(self)
		toolTip.SetPosition(1, 1)
		toolTip.SetFollow(False)
		toolTip.Show()
		self.toolTip = toolTip
	
	def Open(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Open!")
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine("Support-Team",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendDescription("Hier siehst du wer vom Team gerade Online ist. Außerdem kannst du bei Klick auf den Button Support anfordern.",26)
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendHorizontalLine()
		self.toolTip.AppendTextLine("Team:",self.toolTip.TITLE_COLOR)
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendOnlineTextLine("[GM]Werner:",1)
		self.toolTip.AppendOnlineTextLine("[GM]Heinrich:",1)
		self.toolTip.AppendOnlineTextLine("[GM]Walter:",0)
		self.toolTip.AppendOnlineTextLine("[GM]Günther:",0)
		self.toolTip.AppendOnlineTextLine("[GM]ObiWan:",1)
		self.toolTip.AppendOnlineTextLine("[GM]HatHaltEchtKeinPlan:",0)
		self.toolTip.AppendSpace(5)
		self.toolTip.ResizeToolTip()	
		self.AdjustPosition()
		self.Show()
		
	def Close(self):
		self.Hide()

class TeamlerOnlineToolTip(ui.Window):

	textLine = {}

	def __init__(self):
		ui.Window.__init__(self)
		self.SetPosition(wndMgr.GetScreenWidth() - 256 - 75,105)
		self.SetSize(220,20)
		# self.LoadWindow()
		
		
	def LoadWindow(self):
		self.thinBoard = ui.ThinBoard()
		self.thinBoard.SetParent(self)
		self.thinBoard.SetSize(220 - 40,20)
		self.thinBoard.SetPosition(0,0)
		self.thinBoard.Show()	
		
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetPosition(110 - 20,8)
		self.textLine.SetText("Es sind keine Teamler Online")
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.Show()		
			
	def Destroy(self):
		self.thinBoard = None
		self.textLine = None
		
	def Open(self):
		self.Show()
	
	
	def Close(self):
		self.Hide()
	

class SwitchBotToolTip(ui.Window):

	textLine = {}

	def __init__(self):
		ui.Window.__init__(self)
		self.SetPosition(wndMgr.GetScreenWidth() - 256 - 80 - 10,135)
		self.SetSize(220,110)
		# self.LoadWindow()
		
		
	def LoadWindow(self):
		self.thinBoard = ui.ThinBoard()
		self.thinBoard.SetParent(self)
		self.thinBoard.SetSize(220,110)
		self.thinBoard.SetPosition(0,0)
		self.thinBoard.Show()		
		
		y = 12
		for i in xrange(5):
			self.textLine[i] = ui.TextLine()
			self.textLine[i].SetParent(self)
			self.textLine[i].SetPosition(110,y)
			# self.textLine[i].SetText("Slot 1: Vollmondschwert+9 (87x Geswitcht)")
			self.textLine[i].SetHorizontalAlignCenter()
			self.textLine[i].Show()
			
			y = y + 18
			
	def Destroy(self):
		self.thinBoard = None
		self.textLine = None
		
	def Open(self):
		self.Show()
	
	
	def Close(self):
		self.Hide()
	
	def GetItemNameBySlot(self,slot):
		itemvnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(slot)
		item.SelectItem(itemvnum)
		
		return item.GetItemName()
	
	def OnUpdate(self):
		for i in xrange(5):
			if settinginfo.switchbot_switch_count[i] > 0:
				self.textLine[i].SetText("Slot " + str(i+1) + ": " + self.GetItemNameBySlot(settinginfo.switchbot_Slots[i]) + " (" + str(settinginfo.switchbot_switch_count[i]) + "x Geswitcht)")
				self.textLine[i].SetFontColor(0.5411, 0.7254, 0.5568)
			else:
				self.textLine[i].SetText("Slot " + str(i+1) + ": Inaktiv")
				self.textLine[i].SetFontColor(0.9, 0.4745, 0.4627)
				
				
class MapTextToolTip(ui.Window):
	def __init__(self):			
		ui.Window.__init__(self)

		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetHorizontalAlignCenter()
		textLine.SetOutline()
		textLine.SetHorizontalAlignRight()
		textLine.Show()
		self.textLine = textLine

	def __del__(self):			
		ui.Window.__del__(self)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetTooltipPosition(self, PosX, PosY):
		if localeInfo.IsARABIC():
			w, h = self.textLine.GetTextSize()
			self.textLine.SetPosition(PosX - w - 5, PosY)
		else:
			self.textLine.SetPosition(PosX - 5, PosY)

	def SetTextColor(self, TextColor):
		self.textLine.SetPackedFontColor(TextColor)

	def GetTextSize(self):
		return self.textLine.GetTextSize()

class AtlasBossIcon(ui.Window):

	def __init__(self):
		ui.Window.__init__(self)
		self.SetSize(16,16)
		# self.SetPosition(wndMgr.GetScreenWidth() - 149,58)
		self.MakeSkull()
		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.HideToolTip()
		self.name = "NoName"
		self.respawnTime = 0
		self.Show()
		
	def __del__(self):
		ui.Window.__del__(self)	

	def MakeSkull(self):
		self.skullImage = ui.ImageBox()
		self.skullImage.SetParent(self)
		self.skullImage.SetPosition(0,0)
		self.skullImage.LoadImage("yamato_boss/skull3.tga")
		self.skullImage.Show()
	
	def SetBossInfo(self,name,respawnTime,x,y):
		self.name = str(name)
		self.respawnTime = str(respawnTime)
		self.x = int(x) + 8
		self.y = int(y) + 8
		
	def Update(self):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Update")
		if self.skullImage.IsIn():
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"IsIn!")
			
	def CheckMousePositionForToolTip(self,x,y):
		canShowX = False
		canShowY = False
		if x >= self.x - 5 and x <= self.x + 5:
			canShowX = True
	
		if y >= self.y - 5 and y <= self.y + 5:
			canShowY = True
			
		if canShowX and canShowY:	
			self.ShowToolTip()
		else:
			self.HideToolTip()
		
	def ShowToolTip(self):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(self.name,self.toolTip.TITLE_COLOR)			
		self.toolTip.AppendTextLine("Respawnzeit: " + self.respawnTime + " Min.",self.toolTip.NORMAL_COLOR)			
		self.toolTip.ShowToolTip()

	def HideToolTip(self):
		self.toolTip.HideToolTip()
		

class AtlasWindow(ui.ScriptWindow):

	class AtlasRenderer(ui.Window):
		def __init__(self):
			ui.Window.__init__(self)
			self.AddFlag("not_pick")
			

		def OnUpdate(self):
			miniMap.UpdateAtlas()

		def OnRender(self):
			(x, y) = self.GetGlobalPosition()
			fx = float(x)
			fy = float(y)
			miniMap.RenderAtlas(fx, fy)
			# miniMap.AddWayPoint(0,float(587000),float(63400),"Gespeicherte Position")

		def HideAtlas(self):
			miniMap.HideAtlas()

		def ShowAtlas(self):
			miniMap.ShowAtlas()
		
		# def OnMouseLeftButtonDown(self):
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Hallo?")

	def __init__(self):
		self.tooltipInfo = MapTextToolTip()
		self.tooltipInfo.Hide()
		self.infoGuildMark = ui.MarkBox()
		self.infoGuildMark.Hide()
		self.AtlasMainWindow = None
		self.bossIconList = {}
		self.mapName = ""
		self.board = 0
		self.gmJumpEnabled = 0
		self.showLocalMousePosition = True

		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
	
	
	def MakeBossIcons(self):
		mapName = background.GetCurrentMapName()
		
		if mapName in BOSS_DATA:
			data = BOSS_DATA[mapName]
			for i in xrange(len(data)):
				self.bossIconList[i] = AtlasBossIcon()
				self.bossIconList[i].SetParent(self.AtlasMainWindow)
				self.bossIconList[i].SetPosition(data[i][0],data[i][1])
				self.bossIconList[i].SetBossInfo(data[i][2],data[i][3],data[i][0],data[i][1])
				self.bossIconList[i].Show()
				
	def ClearBossIcons(self):
		self.bossIconList = {}

	
	def SetMapName(self, mapName):
		if 949==app.GetDefaultCodePage():
			try:
				self.board.SetTitleName(localeInfo.MINIMAP_ZONE_NAME_DICT[mapName])
			except:
				pass

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/AtlasWindow.py")
		except:
			import exception
			exception.Abort("AtlasWindow.LoadWindow.LoadScript")

		try:
			self.board = self.GetChild("board")
			self.titleBar = self.GetChild("TitleBar")
			# self.toolTipPos = self.GetChild("positionToolTip")
			self.enableGMJumpButton = self.GetChild("enableWarpWindowButton")
			self.enableGMJumpButton.SetEvent(self.ToggleGMJump)
		except:
			import exception
			exception.Abort("AtlasWindow.LoadWindow.BindObject")

		self.AtlasMainWindow = self.AtlasRenderer()

		self.toolTipPos = ui.TextLine()
		self.toolTipPos.SetParent(self.AtlasMainWindow)
		self.toolTipPos.SetOutline()
		self.toolTipPos.Hide()
		self.toolTipPos.SetTop()
		self.titleBar.SetCloseEvent(self.Hide)
		self.AtlasMainWindow.SetParent(self.board)
		self.AtlasMainWindow.SetPosition(12+13, 34-10-8)
		self.tooltipInfo.SetParent(self.board)
		self.infoGuildMark.SetParent(self.board)
		self.SetPosition(wndMgr.GetScreenWidth() - 136 - 256 - 10, 0)
		self.Hide()
		self.ClearBossIcons()
		self.MakeBossIcons()
		miniMap.RegisterAtlasWindow(self)
		
		self.warpWindow = ui.Window()
		self.warpWindow.SetParent(self.board)
		self.warpWindow.SetPosition(12+13, 34-10-8)
		self.warpWindow.Hide()
		self.warpWindow.SetMouseLeftButtonDownEvent(self.OnGMJump)

	def Destroy(self):
		miniMap.UnregisterAtlasWindow()
		self.ClearDictionary()
		self.AtlasMainWindow = None
		self.tooltipAtlasClose = 0
		self.tooltipInfo = None
		self.infoGuildMark = None
		self.board = None
		self.titleBar = None
		self.warpWindow = None
		self.ClearBossIcons()
	
	def ToggleGMJump(self):
		if self.gmJumpEnabled == 0:
			self.warpWindow.Show()
			self.warpWindow.SetTop()
			self.gmJumpEnabled = 1
		else:
			self.warpWindow.Hide()
			self.gmJumpEnabled = 0
	
	def OnGMJump(self):
		(x, y) = self.GetGlobalPosition()
		(mouseX, mouseY) = wndMgr.GetMousePosition()
		(iPosX, iPosY) = miniMap.GetAtlasPositionInfo(mouseX, mouseY)
		textWidth, textHeight = self.toolTipPos.GetTextSize()
			
		self.toolTipPos.SetText("Jump tp (" + str(iPosX) + ", " + str(iPosY)+")")
			
		GFHhg54GHGhh45GHGH.SendChatPacket("/go " + str(iPosX) + " " + str(iPosY))
			
	def OnUpdate(self):

		if not self.tooltipInfo:
			return

		if not self.infoGuildMark:
			return
			
		if self.gmJumpEnabled == 1:
			if False == self.warpWindow.IsIn():
				return			
			(x, y) = self.GetGlobalPosition()
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			(iPosX, iPosY) = miniMap.GetAtlasPositionInfo(mouseX, mouseY)
			textWidth, textHeight = self.toolTipPos.GetTextSize()
			
			self.toolTipPos.SetText("Jump tp (" + str(iPosX) + ", " + str(iPosY)+")")
			self.toolTipPos.SetPosition(mouseX - x - textWidth - 18 - 5, mouseY - y - 50)
			self.toolTipPos.Show()			
			return
			
		self.infoGuildMark.Hide()
		self.tooltipInfo.Hide()
		self.toolTipPos.Hide()
		if False == self.board.IsIn():
			return
		(x, y) = self.GetGlobalPosition()
		(mouseX, mouseY) = wndMgr.GetMousePosition()
		(iPosX, iPosY) = miniMap.GetAtlasPositionInfo(mouseX, mouseY)
		textWidth, textHeight = self.toolTipPos.GetTextSize()
		
		if SHOW_BOSS_ICON_POSITION_HELPER:
			# self.toolTipPos.SetText("x: " + str(mouseX - x - 25) + ", y: " + str(mouseY - y - 66))
			self.toolTipPos.SetText("x: " + str(iPosX) + ", y: " + str(iPosY))
			self.toolTipPos.SetPosition(mouseX - x - textWidth - 18 - 5, mouseY - y - 50)
			self.toolTipPos.Show()
		
		for i in xrange(len(self.bossIconList)):
			self.bossIconList[i].CheckMousePositionForToolTip(mouseX - x - 25,mouseY - y - 66)

		
		
		(bFind, sName, iPosX, iPosY, dwTextColor, dwGuildID) = miniMap.GetAtlasInfo(mouseX, mouseY)	
		if False == bFind:
			return

		if "empty_guild_area" == sName:
			sName = localeInfo.GUILD_EMPTY_AREA

		if localeInfo.IsARABIC() and sName[-1].isalnum():
			self.tooltipInfo.SetText("(%s)%d, %d" % (sName, iPosX, iPosY))						
		else:
			self.tooltipInfo.SetText("%s(%d, %d)" % (sName, iPosX, iPosY))
			
		
		
		self.tooltipInfo.SetTooltipPosition(mouseX - x, mouseY - y - 50)
		self.tooltipInfo.SetTextColor(dwTextColor)
		self.tooltipInfo.Show()
		self.tooltipInfo.SetTop()

		if 0 != dwGuildID:
			textWidth, textHeight = self.tooltipInfo.GetTextSize()
			self.infoGuildMark.SetIndex(dwGuildID)
			self.infoGuildMark.SetPosition(mouseX - x - textWidth - 18 - 5, mouseY - y - 50)
			self.infoGuildMark.Show()
			

			
			
	def Hide(self):
		if self.AtlasMainWindow:
			self.AtlasMainWindow.HideAtlas()
			self.AtlasMainWindow.Hide()
		ui.ScriptWindow.Hide(self)

	def Show(self):
		if self.AtlasMainWindow:
			(bGet, iSizeX, iSizeY) = miniMap.GetAtlasSize()
			if bGet:
				self.SetSize(iSizeX + 15, iSizeY + 38)

				if localeInfo.IsARABIC():
					self.board.SetPosition(iSizeX+15, 0)

				self.board.SetSize(iSizeX + 50, iSizeY + 38)
				self.warpWindow.SetSize(iSizeX + 50, iSizeY + 38)
				self.SetSize(iSizeX + 50, iSizeY + 38+50)
				self.titleBar.SetWidth(iSizeX +50+15)
				#self.AtlasMainWindow.SetSize(iSizeX, iSizeY)
				self.AtlasMainWindow.ShowAtlas()
				self.AtlasMainWindow.Show()
		ui.ScriptWindow.Show(self)

	def SetCenterPositionAdjust(self, x, y):
		self.SetPosition((wndMgr.GetScreenWidth() - self.GetWidth()) / 2 + x, (wndMgr.GetScreenHeight() - self.GetHeight()) / 2 + y)

	def OnPressEscapeKey(self):
		self.Hide()
		return True

def __RegisterMiniMapColor(type, rgb):
	miniMap.RegisterColor(type, rgb[0], rgb[1], rgb[2])

class MiniMap(ui.ScriptWindow):

	CANNOT_SEE_INFO_MAP_DICT = {
		"metin2_map_monkeydungeon" : False,
		"metin2_map_monkeydungeon_02" : False,
		"metin2_map_monkeydungeon_03" : False,
		"metin2_map_devilsCatacomb" : False,
	}

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.__Initialize()

		miniMap.Create()
		miniMap.SetScale(2.0)

		self.AtlasWindow = AtlasWindow()
		self.AtlasWindow.LoadWindow()
		self.AtlasWindow.Hide()
		
		# self.SwitchBotToolTip = SwitchBotToolTip()
		# self.SwitchBotToolTip.LoadWindow()
		# self.SwitchBotToolTip.Close()
		
		# self.TeamlerOnlineToolTip = TeamlerOnlineToolTipNEW()
		# self.TeamlerOnlineToolTip.LoadWindow()
		# self.TeamlerOnlineToolTip.Close()
		
		self.teamOnlineToolTip = TeamlerOnlineToolTipNEW(self)
		self.switchBotToolTip = SwitchBotToolTipNEW(self)
		self.switchBotToolTip2 = SwitchBotToolTipNEW(self)
		
		self.tooltipMiniMapOpen = MapTextToolTip()
		self.tooltipMiniMapOpen.SetText(localeInfo.MINIMAP)
		self.tooltipMiniMapOpen.Show()
		self.tooltipMiniMapClose = MapTextToolTip()
		self.tooltipMiniMapClose.SetText(localeInfo.UI_CLOSE)
		self.tooltipMiniMapClose.Show()
		self.tooltipScaleUp = MapTextToolTip()
		self.tooltipScaleUp.SetText(localeInfo.MINIMAP_INC_SCALE)
		self.tooltipScaleUp.Show()
		self.tooltipScaleDown = MapTextToolTip()
		self.tooltipScaleDown.SetText(localeInfo.MINIMAP_DEC_SCALE)
		self.tooltipScaleDown.Show()
		self.tooltipAtlasOpen = MapTextToolTip()
		self.tooltipAtlasOpen.SetText(localeInfo.MINIMAP_SHOW_AREAMAP)
		self.tooltipAtlasOpen.Show()
		
		# self.tooltipLeaveBattlezone = MapTextToolTip()
		# self.tooltipLeaveBattlezone.SetText("Kampfzone verlassen.")
		# self.tooltipLeaveBattlezone.Show()
		
		self.tooltipInfo = MapTextToolTip()
		self.tooltipInfo.Show()

		if miniMap.IsAtlas():
			self.tooltipAtlasOpen.SetText(localeInfo.MINIMAP_SHOW_AREAMAP)
		else:
			self.tooltipAtlasOpen.SetText(localeInfo.MINIMAP_CAN_NOT_SHOW_AREAMAP)

		self.tooltipInfo = MapTextToolTip()
		self.tooltipInfo.Show()

		self.mapName = ""

		self.isLoaded = 0
		self.canSeeInfo = True
		
		# AUTOBAN
		self.imprisonmentDuration = 0
		self.imprisonmentEndTime = 0
		self.imprisonmentEndTimeText = ""
		# END_OF_AUTOBAN

	def __del__(self):
		miniMap.Destroy()
		ui.ScriptWindow.__del__(self)

	def __Initialize(self):
		self.positionInfo = 0
		self.observerCount = 0

		self.OpenWindow = 0
		self.CloseWindow = 0
		self.ScaleUpButton = 0
		self.ScaleDownButton = 0
		self.MiniMapHideButton = 0
		self.MiniMapShowButton = 0
		self.AtlasShowButton = 0

		self.tooltipMiniMapOpen = 0
		self.tooltipMiniMapClose = 0
		self.tooltipScaleUp = 0
		self.tooltipScaleDown = 0
		# self.tooltipLeaveBattlezone = 0
		self.tooltipAtlasOpen = 0
		self.tooltipInfo = None
		self.serverInfo = None

	def SetMapName(self, mapName):
		self.mapName=mapName
		self.AtlasWindow.SetMapName(mapName)

		if self.CANNOT_SEE_INFO_MAP_DICT.has_key(mapName):
			self.canSeeInfo = False
			self.HideMiniMap()
			self.tooltipMiniMapOpen.SetText(localeInfo.MINIMAP_CANNOT_SEE)
		else:
			self.canSeeInfo = True
			self.ShowMiniMap()
			self.tooltipMiniMapOpen.SetText(localeInfo.MINIMAP)
			
	# AUTOBAN
	def SetImprisonmentDuration(self, duration):
		self.imprisonmentDuration = duration
		self.imprisonmentEndTime = app.GetGlobalTimeStamp() + duration				
		
		self.__UpdateImprisonmentDurationText()
		
	def __UpdateImprisonmentDurationText(self):
		restTime = max(self.imprisonmentEndTime - app.GetGlobalTimeStamp(), 0)
		
		imprisonmentEndTimeText = localeInfo.SecondToDHM(restTime)
		if imprisonmentEndTimeText != self.imprisonmentEndTimeText:
			self.imprisonmentEndTimeText = imprisonmentEndTimeText
			self.serverInfo.SetText("%s: %s" % (uiScriptLocale.AUTOBAN_QUIZ_REST_TIME, self.imprisonmentEndTimeText))
	# END_OF_AUTOBAN	

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			if localeInfo.IsARABIC():
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "Minimap.py")
			else:
				pyScrLoader.LoadScriptFile(self, "UIScript/MiniMap.py")
		except:
			import exception
			exception.Abort("MiniMap.LoadWindow.LoadScript")

		try:
			self.OpenWindow = self.GetChild("OpenWindow")
			self.MiniMapWindow = self.GetChild("MiniMapWindow")
			self.ScaleUpButton = self.GetChild("ScaleUpButton")
			self.ScaleDownButton = self.GetChild("ScaleDownButton")
			self.MiniMapHideButton = self.GetChild("MiniMapHideButton")
			self.AtlasShowButton = self.GetChild("AtlasShowButton")
			self.SwitchBotButton = self.GetChild("SwitchBotButton_Active")
			self.SwitchBotButtonInactive = self.GetChild("SwitchBotButton_InActive")
			self.GMPanelButton = self.GetChild("GMPanelButton")
			
			# self.BattlezoneLeaveButton = self.GetChild("BattlezoneLeaveButton")
			self.CloseWindow = self.GetChild("CloseWindow")
			self.MiniMapShowButton = self.GetChild("MiniMapShowButton")
			self.positionInfo = self.GetChild("PositionInfo")
			self.bioInfo = self.GetChild("BioTimerInfo")
			self.observerCount = self.GetChild("ObserverCount")
			self.serverInfo = self.GetChild("ServerInfo")
			self.timeInfo = self.GetChild("TimeInfo")
			self.mapNameInfo = self.GetChild("MapNameInfo")
			# self.battleZonePoints = self.GetChild("battlezonePoints")
			# self.battleZoneTitle = self.GetChild("battlezoneTitle")
			
			
			self.bossMapTitle	= self.GetChild("bossMapTitle")
			self.bossMapUses	= self.GetChild("bossMapUses")
			self.bossMapTimer	= self.GetChild("bossMapTimer")
			
			# self.battlezoneLeaveTimeTitle = self.GetChild("battlezoneLeaveTimeTitle")
			
			# self.battlezoneLeaveTime = self.GetChild("battlezoneLeaveTime")
			self.bioInfo.SetText("")
			
		except:
			import exception
			exception.Abort("MiniMap.LoadWindow.Bind")

		if constInfo.MINIMAP_POSITIONINFO_ENABLE==0:
			self.positionInfo.Hide()

		self.serverInfo.SetText(GFHhg54GHGhh45GHGH.GetServerInfo())
		self.ScaleUpButton.SetEvent(ui.__mem_func__(self.ScaleUp))
		self.ScaleDownButton.SetEvent(ui.__mem_func__(self.ScaleDown))
		self.MiniMapHideButton.SetEvent(ui.__mem_func__(self.HideMiniMap))
		self.MiniMapShowButton.SetEvent(ui.__mem_func__(self.ShowMiniMap))
		
		
		self.SwitchBotButton.Hide()
		self.SwitchBotButton.SetEvent(self.Switchbot)
		self.SwitchBotButtonInactive.SetEvent(self.Switchbot)
		# self.GMPanelButton.Hide()
		# self.battlezoneLeaveTime.Hide()
		# self.battlezoneLeaveTimeTitle.Hide()		
		# self.BattlezoneLeaveButton.SetEvent(ui.__mem_func__(self.BattlezoneLeave))

		self.bossMapTitle.Hide()
		self.bossMapUses.Hide()
		self.bossMapTimer.Hide()
		self.bioInfo.Hide()
		
		if miniMap.IsAtlas():
			self.AtlasShowButton.SetEvent(ui.__mem_func__(self.ShowAtlas))

		(ButtonPosX, ButtonPosY) = self.MiniMapShowButton.GetGlobalPosition()
		self.tooltipMiniMapOpen.SetTooltipPosition(ButtonPosX, ButtonPosY)

		(ButtonPosX, ButtonPosY) = self.MiniMapHideButton.GetGlobalPosition()
		self.tooltipMiniMapClose.SetTooltipPosition(ButtonPosX, ButtonPosY)

		(ButtonPosX, ButtonPosY) = self.ScaleUpButton.GetGlobalPosition()
		self.tooltipScaleUp.SetTooltipPosition(ButtonPosX, ButtonPosY)

		(ButtonPosX, ButtonPosY) = self.ScaleDownButton.GetGlobalPosition()
		self.tooltipScaleDown.SetTooltipPosition(ButtonPosX, ButtonPosY)
		
		(ButtonPosX, ButtonPosY) = self.ScaleDownButton.GetGlobalPosition()
		# self.tooltipLeaveBattlezone.SetTooltipPosition(ButtonPosX, ButtonPosY)
		
		(ButtonPosX, ButtonPosY) = self.AtlasShowButton.GetGlobalPosition()
		self.tooltipAtlasOpen.SetTooltipPosition(ButtonPosX, ButtonPosY)

		self.ShowMiniMap()

	def Destroy(self):
		self.HideMiniMap()

		self.AtlasWindow.Destroy()
		self.AtlasWindow = None

		self.ClearDictionary()

		self.__Initialize()
	
	def Switchbot(self):
		if settinginfo.switchbot == 0:
			import uiswitchbot
			uiswitchbot.SwitchBoard(self).Show()	
		else:
			if settinginfo.switchbot_minimize == 1:
				settinginfo.switchbot_minimize = 2		
	
	def UpdateObserverCount(self, observerCount):
		if observerCount>0:
			self.observerCount.Show()
		elif observerCount<=0:
			self.observerCount.Hide()

		self.observerCount.SetText(localeInfo.MINIMAP_OBSERVER_COUNT % observerCount)
		
	def ShowBossMapInfo(self):
		self.bossMapTitle.Show()
		self.bossMapTitle.SetFontColor(1.0, 0.7843, 0.0)		
		self.bossMapUses.Show()
		self.bossMapTimer.Show()

		self.bioInfo.SetPosition(70,280)		

	def UpdateBossMapUsesInfo(self,count):
		if count == 0:
			self.bossMapUses.SetFontColor(0.9, 0.4745, 0.4627)
		else:
			self.bossMapUses.SetFontColor(0.5411, 0.7254, 0.5568)
			
		self.bossMapUses.SetText(str(count) + " Rufrollen verbl.")
		
	def UpdateBossMapTimer(self):
		if settinginfo.bossMapTimer > app.GetGlobalTimeStamp():
			timeLeft = settinginfo.bossMapTimer - app.GetGlobalTimeStamp()
			self.bossMapTimer.SetFontColor(0.9, 0.4745, 0.4627)
			self.bossMapTimer.SetText(self.AyFormatRebootTime(timeLeft) + " Min. bis Reset!")
		else:
			self.bossMapTimer.SetText("Reset bereit!")
			self.bossMapTimer.SetFontColor(0.5411, 0.7254, 0.5568)
	
	def UpdateServerInfo(self):
		self.serverInfo.SetText("Kimiko, Channel " + str(settinginfo.realChannel) + "")
		#chat.AppendChat(chat.CHAT_TYPE_NOTICE,GFHhg54GHGhh45GHGH.GetServerInfo())
		
	def OnUpdate(self):
		(x, y, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		miniMap.Update(x, y)

		self.positionInfo.SetText("(%.0f, %.0f)" % (x/100, y/100))
		
		localtime = localtime = time.strftime("[%H:%M:%S]")
		self.timeInfo.SetText(localtime + "[" + str(app.GetRenderFPS()) + " FPS]")
		
		self.mapNameInfo.SetText(settinginfo.GetMapNameByMapFolderName(1))
		if settinginfo.MapIsSpecialMap(1):
			self.mapNameInfo.SetFontColor(1.0, 0.63, 0)
		
		if settinginfo.realChannel > 0:
			self.UpdateServerInfo()
		
		# if settinginfo.bio_timer_status == 1:
			# if app.GetGlobalTimeStamp() > settinginfo.bio_timer:
				# self.bioInfo.SetText("[BIO] Bereit!")
				# self.bioInfo.SetFontColor(0.5411, 0.7254, 0.5568)
				# self.bioInfo.Show()
			# else:
				# timeLeft = settinginfo.bio_timer - app.GetGlobalTimeStamp()
				# self.bioInfo.SetText("[BIO] Zeit: " + self.AyFormatRebootTime(timeLeft))
				# self.bioInfo.SetFontColor(0.9, 0.4745, 0.4627)
				# self.bioInfo.Show()
				
		self.UpdateBossMapTimer()
		self.UpdateForestZoneTimer()
		
		
		if self.SwitchBotButton.IsIn():
			self.switchBotToolTip.Open()
		else:
			self.switchBotToolTip.Close()
			
		if self.SwitchBotButtonInactive.IsIn():
			self.switchBotToolTip2.Open()
		else:
			self.switchBotToolTip2.Close()			
			
		if self.GMPanelButton.IsIn():
			# self.TeamlerOnlineToolTip.Open()
			
			self.teamOnlineToolTip.Open()
		else:
			# self.TeamlerOnlineToolTip.Close()
			
			self.teamOnlineToolTip.Close()
		# -------------------------------------------------------------------
		# Battlezone-Infos
		# if background.GetCurrentMapName() == "metin2_map_battlefield":
			# self.battleZoneTitle.Show()
			# self.battleZonePoints.SetText(str(settinginfo.battlezonePoints) + " Punkt(e)")
			
			# if settinginfo.battlezoneLeaveTime > app.GetGlobalTimeStamp():
				# self.BattlezoneLeaveButton.Hide()
				# self.battlezoneLeaveTimeTitle.Show()
				# battlezoneTimeLeft = settinginfo.battlezoneLeaveTime - app.GetGlobalTimeStamp()
				# self.battlezoneLeaveTime.SetText(str(self.AyFormatRebootTime(int(battlezoneTimeLeft))))
				# self.battlezoneLeaveTime.Show()
			# else:
				# self.BattlezoneLeaveButton.Show()
				# self.battlezoneLeaveTimeTitle.Hide()
				# self.battlezoneLeaveTime.Hide()
		# else:
			# self.battleZoneTitle.Hide()
			# self.battleZonePoints.Hide()
			# self.BattlezoneLeaveButton.Hide()
			# self.battlezoneLeaveTime.Hide()
			# self.battlezoneLeaveTimeTitle.Hide()
			
		# -------------------------------------------------------------------
		if self.tooltipInfo:
			if True == self.MiniMapWindow.IsIn():
				(mouseX, mouseY) = wndMgr.GetMousePosition()
				(bFind, sName, iPosX, iPosY, dwTextColor) = miniMap.GetInfo(mouseX, mouseY)
				if bFind == 0:
					self.tooltipInfo.Hide()
				elif not self.canSeeInfo:
					self.tooltipInfo.SetText("%s(%s)" % (sName, localeInfo.UI_POS_UNKNOWN))
					self.tooltipInfo.SetTooltipPosition(mouseX - 5, mouseY)
					self.tooltipInfo.SetTextColor(dwTextColor)
					self.tooltipInfo.Show()
				else:
					if localeInfo.IsARABIC() and sName[-1].isalnum():
						self.tooltipInfo.SetText("(%s)%d, %d" % (sName, iPosX, iPosY))
					else:
						self.tooltipInfo.SetText("%s(%d, %d)" % (sName, iPosX, iPosY))
					self.tooltipInfo.SetTooltipPosition(mouseX - 5, mouseY)
					self.tooltipInfo.SetTextColor(dwTextColor)
					self.tooltipInfo.Show()
			else:
				self.tooltipInfo.Hide()
			
			# AUTOBAN
			if self.imprisonmentDuration:
				self.__UpdateImprisonmentDurationText()				
			# END_OF_AUTOBAN

		if True == self.MiniMapShowButton.IsIn():
			self.tooltipMiniMapOpen.Show()
		else:
			self.tooltipMiniMapOpen.Hide()

		if True == self.MiniMapHideButton.IsIn():
			self.tooltipMiniMapClose.Show()
		else:
			self.tooltipMiniMapClose.Hide()

		if True == self.ScaleUpButton.IsIn():
			self.tooltipScaleUp.Show()
		else:
			self.tooltipScaleUp.Hide()

		if True == self.ScaleDownButton.IsIn():
			self.tooltipScaleDown.Show()
		else:
			self.tooltipScaleDown.Hide()
			
		# if True == self.BattlezoneLeaveButton.IsIn():
			# self.tooltipLeaveBattlezone.Show()
		# else:
			# self.tooltipLeaveBattlezone.Hide()
			
		if True == self.AtlasShowButton.IsIn():
			self.tooltipAtlasOpen.Show()
		else:
			self.tooltipAtlasOpen.Hide()

	def OnRender(self):
		(x, y) = self.GetGlobalPosition()
		fx = float(x)
		fy = float(y)
		miniMap.Render(fx + 4.0, fy + 5.0)

	def Close(self):
		self.HideMiniMap()

	def HideMiniMap(self):
		miniMap.Hide()
		self.OpenWindow.Hide()
		self.CloseWindow.Show()

	def ShowMiniMap(self):
		if not self.canSeeInfo:
			return

		miniMap.Show()
		self.OpenWindow.Show()
		self.CloseWindow.Hide()
	
	# def BattlezoneLeave(self):
		# if settinginfo.battlezoneLeaveTime < app.GetGlobalTimeStamp():
			# GFHhg54GHGhh45GHGH.SendChatPacket("/user_request_leave_battlezone")
		
	def isShowMiniMap(self):
		return miniMap.isShow()

	def ScaleUp(self):
		miniMap.ScaleUp()

	def ScaleDown(self):
		miniMap.ScaleDown()

	def ShowAtlas(self):
		if not miniMap.IsAtlas():
			return
		if not self.AtlasWindow.IsShow():
			self.AtlasWindow.Show()

	def ToggleAtlasWindow(self):
		if not miniMap.IsAtlas():
			return
		if self.AtlasWindow.IsShow():
			self.AtlasWindow.Hide()
		else:
			self.AtlasWindow.Show()
	
	# REBOOTSYSTEM
	def AyFormatRebootTime(self, time):
		m, s = divmod(time, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%02d" % (h, m, s)
		
	def UpdateForestZoneTimer(self):
		if settinginfo.forest_zone_time > 0:
			self.bossMapTitle.Show()
			timeLeft = settinginfo.forest_zone_time - app.GetGlobalTimeStamp()
			self.bossMapTitle.SetText("Verbl. Zeit im Wald: " + self.AyFormatRebootTime(timeLeft))
