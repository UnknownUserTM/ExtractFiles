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

	def __init__(self):
		self.tooltipInfo = MapTextToolTip()
		self.tooltipInfo.Hide()
		self.infoGuildMark = ui.MarkBox()
		self.infoGuildMark.Hide()
		self.AtlasMainWindow = None
		self.mapName = ""
		self.board = 0
		self.showLocalMousePosition = True

		ui.ScriptWindow.__init__(self)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

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
			self.toolTipPos = self.GetChild("positionToolTip")

		except:
			import exception
			exception.Abort("AtlasWindow.LoadWindow.BindObject")
		self.toolTipPos.Hide()
		self.AtlasMainWindow = self.AtlasRenderer()
		self.titleBar.SetCloseEvent(self.Hide)
		self.AtlasMainWindow.SetParent(self.board)
		self.AtlasMainWindow.SetPosition(12+13, 34-10-8)
		self.tooltipInfo.SetParent(self.board)
		self.infoGuildMark.SetParent(self.board)
		self.SetPosition(wndMgr.GetScreenWidth() - 136 - 256 - 10, 0)
		self.Hide()

		miniMap.RegisterAtlasWindow(self)

	def Destroy(self):
		miniMap.UnregisterAtlasWindow()
		self.ClearDictionary()
		self.AtlasMainWindow = None
		self.tooltipAtlasClose = 0
		self.tooltipInfo = None
		self.infoGuildMark = None
		self.board = None
		self.titleBar = None

	def OnUpdate(self):

		if not self.tooltipInfo:
			return

		if not self.infoGuildMark:
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
		self.toolTipPos.SetText("x: " + str(iPosX) + ", y: " + str(iPosY))
		self.toolTipPos.SetPosition(mouseX - x - textWidth - 18 - 5, mouseY - y - 50)
		self.toolTipPos.Show()

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
		
		self.SwitchBotToolTip = SwitchBotToolTip()
		self.SwitchBotToolTip.LoadWindow()
		self.SwitchBotToolTip.Close()
		
		self.TeamlerOnlineToolTip = TeamlerOnlineToolTip()
		self.TeamlerOnlineToolTip.LoadWindow()
		self.TeamlerOnlineToolTip.Close()
		
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
			self.SwitchBotButton = self.GetChild("SwitchBotButton")
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
		
		self.SwitchBotButton.SetEvent(self.Switchbot)
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
			uiswitchbot.SwitchBoard().Show()	
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
		self.serverInfo.SetText("Yunari2, Channel " + str(settinginfo.realChannel) + "")
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
			self.SwitchBotToolTip.Open()
		else:
			self.SwitchBotToolTip.Close()
			
		if self.GMPanelButton.IsIn():
			self.TeamlerOnlineToolTip.Open()
		else:
			self.TeamlerOnlineToolTip.Close()
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
