import os
import app
import dbg
import grp
import item
import background
import chr
import chrmgr
import fgGHGjjFHJghjfFG1545gGG
import snd
import chat
import textTail
import snd
import GFHhg54GHGhh45GHGH
import effect
import wndMgr
import fly
import systemSetting
import quest
import guild
import skill
import messenger
import localeInfo
import constInfo
import exchange
import ime
# import nonplayertest
# import uidungeonentry
# import uidungeonkompendium
import uiachievement
# import uidaily_new
# import uimultishop
# import uiintrodungeon
# import uiguidedialog
#import uibattlezone
import event
import ui
import uiCommon
import uiPhaseCurtain
import uiMapNameShower
import uiAffectShower
import uiPlayerGauge
import uiCharacter
import uiTarget
# import uisidebar
import settinginfo
import uihalloffame
# import uicalender
import uiox
# import uibugreport
import uidialog

# PRIVATE_SHOP_PRICE_LIST
import uiPrivateShopBuilder
# END_OF_PRIVATE_SHOP_PRICE_LIST

import mouseModule
import consoleModule
import localeInfo

import playerSettingModule
import interfaceModule

import musicInfo
import debugInfo
import stringCommander
import uiaddpyshining
# import uidungeonmaker
svsidedia = None
svsidedi_cp =  ""
from svsideoi import SvsideDialog
import binascii

# import uikeytreasure

from _weakref import proxy
# from switchbot import Bot

# TEXTTAIL_LIVINGTIME_CONTROL
#if localeInfo.IsJAPAN():
#	app.SetTextTailLivingTime(8.0)
# END_OF_TEXTTAIL_LIVINGTIME_CONTROL

# SCREENSHOT_CWDSAVE
SCREENSHOT_CWDSAVE = False
SCREENSHOT_DIR = None

if localeInfo.IsEUROPE():
	SCREENSHOT_CWDSAVE = True

if localeInfo.IsCIBN10():
	SCREENSHOT_CWDSAVE = False
	SCREENSHOT_DIR = "YT2W"

cameraDistance = 1550.0
cameraPitch = 27.0
cameraRotation = 0.0
cameraHeight = 100.0

testAlignment = 0
BPisLoaded = 0

CANNOT_DESTROY_ITEM_LIST = [160480,160481,160482,160483,160484,160485,160486,160487,80000]

class GameWindow(ui.ScriptWindow):
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self, "GAME")
		self.SetWindowName("game")
		GFHhg54GHGhh45GHGH.SetPhaseWindow(GFHhg54GHGhh45GHGH.PHASE_WINDOW_GAME, self)
		fgGHGjjFHJghjfFG1545gGG.SetGameWindow(self)
		uiaddpyshining.LoadEffectTable()
		
		global svsidedia
		if svsidedia == None:
			svsidedia = SvsideDialog()
		svsidedia.Board.Hide()

		self.quickSlotPageIndex = 0
		self.lastPKModeSendedTime = 0
		self.pressNumber = None
		
		self.guildWarQuestionDialog = None
		self.interface = None
		self.targetBoard = None
		self.console = None
		self.mapNameShower = None
		self.affectShower = None
		self.playerGauge = None
		# self.switchbot = Bot()
		# self.switchbot.Hide()
		# self.TickTime = 0
		self.isDebugMode = 0
		self.stream=stream
		self.interface = interfaceModule.Interface()
		self.interface.MakeInterface()
		self.interface.ShowDefaultWindows()

		self.curtain = uiPhaseCurtain.PhaseCurtain()
		self.curtain.speed = 0.03
		self.curtain.Hide()

		self.targetBoard = uiTarget.TargetBoard()
		self.targetBoard.SetWhisperEvent(ui.__mem_func__(self.interface.OpenWhisperDialog))
		self.targetBoard.Hide()

		self.console = consoleModule.ConsoleWindow()
		self.console.BindGameClass(self)
		self.console.SetConsoleSize(wndMgr.GetScreenWidth(), 200)
		self.console.Hide()

		self.mapNameShower = uiMapNameShower.MapNameShower()
		self.affectShower = uiAffectShower.AffectShower()
		
		import uilanguagesystem
		self.wndAnnouncementWindow = uilanguagesystem.AnnouncementWindow()
		self.wndAnnouncementWindow.Hide()

		self.playerGauge = uiPlayerGauge.PlayerGauge(self)
		self.playerGauge.Hide()
		
		#wj 2014.1.2. ESC키를 누를 시 우선적으로 DropQuestionDialog를 끄도록 만들었다. 하지만 처음에 itemDropQuestionDialog가 선언되어 있지 않아 ERROR가 발생하여 init에서 선언과 동시에 초기화 시킴.
		self.itemDropQuestionDialog = None
		self.itemDestroyQuestionDialog = None

		self.__SetQuickSlotMode()

		self.__ServerCommand_Build()
		self.__ProcessPreservedServerCommand()
		
		# self.dungeonMakerToolBar = uidungeonmaker.DungeonMakerToolBar()
		# self.dungeonMakerToolBar.Open()
		
		# self.DungeonEntrance = uidungeonentry.EntranceWindow()
		# self.DungeonKompendium = uidungeonkompendium.DungeonBoard()
		
		# self.DailyGUI = uidaily_new.DailyBoard()

		# self.MultiShop = uimultishop.MultiShopBoard()
		
		self.OXManager = uiox.OXBoard()
		
		# self.BugReporter = uibugreport.BugReportBoard()
		
		# self.IntroDungeonTextBoard = uiintrodungeon.IntroDungeonBoard()
		# self.GuideDialogBoard = uiguidedialog.GuideBoard()
		
		self.AchievementWindow = uiachievement.AchievementWindow()
		
		import uichanneltabbar
		self.wndChannelTabBar = uichanneltabbar.ChannelTabBar()
		
		# self.Calender = uicalender.CalenderBoard()
		
		#self.BattleZoneWindow = uibattlezone.BattleZoneWindow()
		
		# self.sideBar = uisidebar.SideBar()
		#self.sideBar.AddSlot(91104, self.__toggleSwitchbot)
		# self.sideBar.AddSlot(91104, self.OpenSwitchBot)
		# self.sideBar.AddSlot(91103, self.OpenBoxOpener)
		# self.sideBar.AddSlot(91101, self.AntiEXPButton)
		# self.sideBar.AddSlot(91102, self.BonusBoardButton)
		# self.sideBar.AddSlot(91105, self.OpenWarpGUI)
		# self.sideBar.AddSlot(91106, self.YangChatButton)
		# self.sideBar.AddSlot(91106, self.AutoPotButton)
		# self.sideBar.AddSlot(91100, self.openHallOfFame)
		# self.sideBar.AddSlot(91100, self.Schmiedehandbuch)
		# self.sideBar.AddSlot(91100, self.SchmiedehandbuchPVP)
		# self.sideBar.AddSlot(31014, self.DailyGUIOpen)
		# self.sideBar.AddSlot(31015, self.DungeonkompendiumOpen)
		# self.sideBar.AddSlot(91104, self.OpenSwitchBot)
		# self.sideBar.AddSlot(91103, self.OpenBoxOpener)
		# self.sideBar.AddSlot(91101, self.AntiEXPButton)
		# self.sideBar.AddSlot(91102, self.BonusBoardButton)
		# self.sideBar.AddSlot(91105, self.OpenWarpGUI)
		# self.sideBar.AddSlot(91106, self.TestGMPanel)
		# self.sideBar.AddSlot(70251, self.AutoPotButton)
		# self.sideBar.AddSlot(70252, self.openHallOfFame)
		# self.sideBar.AddSlot(91100, self.Schmiedehandbuch)
		# self.sideBar.AddSlot(70253, self.SchmiedehandbuchPVP)
		# self.sideBar.AddSlot(31014, self.DailyGUIOpen)
		# self.sideBar.AddSlot(31015, self.DungeonkompendiumOpen)	
		# self.sideBar.AddSlot(55105, self.CalenderButton)

		#self.sideBar.AddButton("Spezial Truhe", self.__SpecialCasesOpenFunction)
		# self.sideBar.Show()
		# SPECIAL CASES
		# constInfo.KEY_TREASURE_CONFIG["GUI"] = uikeytreasure.KeyTreasureGui()
		
	def __del__(self):
		fgGHGjjFHJghjfFG1545gGG.SetGameWindow(0)
		GFHhg54GHGhh45GHGH.ClearPhaseWindow(GFHhg54GHGhh45GHGH.PHASE_WINDOW_GAME, self)
		ui.ScriptWindow.__del__(self)

	def Open(self):
		app.SetFrameSkip(1)

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())

		self.quickSlotPageIndex = 0
		self.PickingCharacterIndex = -1
		self.PickingItemIndex = -1
		self.consoleEnable = False
		self.isShowDebugInfo = False
		self.ShowNameFlag = False

		self.enableXMasBoom = False
		self.startTimeXMasBoom = 0.0
		self.indexXMasBoom = 0

		global cameraDistance, cameraPitch, cameraRotation, cameraHeight

		app.SetCamera(cameraDistance, cameraPitch, cameraRotation, cameraHeight)

		constInfo.SET_DEFAULT_CAMERA_MAX_DISTANCE()
		constInfo.SET_DEFAULT_CHRNAME_COLOR()
		constInfo.SET_DEFAULT_FOG_LEVEL()
		constInfo.SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE()
		constInfo.SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS()
		constInfo.SET_DEFAULT_USE_SKILL_EFFECT_ENABLE()
		# self.ResetActivateButtons()
		# TWO_HANDED_WEAPON_ATTACK_SPEED_UP
		constInfo.SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE()
		# END_OF_TWO_HANDED_WEAPON_ATTACK_SPEED_UP

		import event
		event.SetLeftTimeString(localeInfo.UI_LEFT_TIME)

		textTail.EnablePKTitle(constInfo.PVPMODE_ENABLE)

		if constInfo.PVPMODE_TEST_ENABLE:
			self.testPKMode = ui.TextLine()
			self.testPKMode.SetFontName(localeInfo.UI_DEF_FONT)
			self.testPKMode.SetPosition(0, 15)
			self.testPKMode.SetWindowHorizontalAlignCenter()
			self.testPKMode.SetHorizontalAlignCenter()
			self.testPKMode.SetFeather()
			self.testPKMode.SetOutline()
			self.testPKMode.Show()

			self.testAlignment = ui.TextLine()
			self.testAlignment.SetFontName(localeInfo.UI_DEF_FONT)
			self.testAlignment.SetPosition(0, 35)
			self.testAlignment.SetWindowHorizontalAlignCenter()
			self.testAlignment.SetHorizontalAlignCenter()
			self.testAlignment.SetFeather()
			self.testAlignment.SetOutline()
			self.testAlignment.Show()

		self.__BuildKeyDict()
		self.__BuildDebugInfo()

		# PRIVATE_SHOP_PRICE_LIST
		uiPrivateShopBuilder.Clear()
		# END_OF_PRIVATE_SHOP_PRICE_LIST

		# UNKNOWN_UPDATE
		exchange.InitTrading()
		# END_OF_UNKNOWN_UPDATE

		if debugInfo.IsDebugMode():
			self.ToggleDebugInfo()

		## Sound
		snd.SetMusicVolume(systemSetting.GetMusicVolume()*GFHhg54GHGhh45GHGH.GetFieldMusicVolume())
		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		netFieldMusicFileName = GFHhg54GHGhh45GHGH.GetFieldMusicFileName()
		if netFieldMusicFileName:
			snd.FadeInMusic("BGM/" + netFieldMusicFileName)
		elif musicInfo.fieldMusic != "":						
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

		self.__SetQuickSlotMode()
		self.__SelectQuickPage(self.quickSlotPageIndex)
		
		if constInfo.Night == 1:
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			background.SetEnvironmentData(1)
		else:
			background.SetEnvironmentData(0)

		self.SetFocus()
		self.Show()
		app.ShowCursor()

		GFHhg54GHGhh45GHGH.SendEnterGamePacket()

		# START_GAME_ERROR_EXIT
		try:
			self.StartGame()
		except:
			import exception
			exception.Abort("GameWindow.Open")
		# END_OF_START_GAME_ERROR_EXIT
		
		# NPC가 큐브시스템으로 만들 수 있는 아이템들의 목록을 캐싱
		# ex) cubeInformation[20383] = [ {"rewordVNUM": 72723, "rewordCount": 1, "materialInfo": "101,1&102,2", "price": 999 }, ... ]
		self.cubeInformation = {}
		self.currentCubeNPC = 0
		
	def Close(self):
		self.Hide()

		global cameraDistance, cameraPitch, cameraRotation, cameraHeight
		(cameraDistance, cameraPitch, cameraRotation, cameraHeight) = app.GetCamera()

		if musicInfo.fieldMusic != "":
			snd.FadeOutMusic("BGM/"+ musicInfo.fieldMusic)

		self.onPressKeyDict = None
		self.onClickKeyDict = None

		chat.Close()
		snd.StopAllSound()
		grp.InitScreenEffect()
		chr.Destroy()
		textTail.Clear()
		quest.Clear()
		background.Destroy()
		guild.Destroy()
		messenger.Destroy()
		skill.ClearSkillData()
		wndMgr.Unlock()
		mouseModule.mouseController.DeattachObject()

		if self.guildWarQuestionDialog:
			self.guildWarQuestionDialog.Close()

		self.guildNameBoard = None
		self.partyRequestQuestionDialog = None
		self.partyInviteQuestionDialog = None
		self.guildInviteQuestionDialog = None
		self.guildWarQuestionDialog = None
		self.messengerAddFriendQuestion = None

		# UNKNOWN_UPDATE
		self.itemDropQuestionDialog = None
		self.itemDestroyQuestionDialog = None
		
		# END_OF_UNKNOWN_UPDATE

		# QUEST_CONFIRM
		self.confirmDialog = None
		# END_OF_QUEST_CONFIRM

		self.PrintCoord = None
		self.FrameRate = None
		self.Pitch = None
		self.Splat = None
		self.TextureNum = None
		self.ObjectNum = None
		self.ViewDistance = None
		self.PrintMousePos = None

		self.ClearDictionary()

		self.playerGauge = None
		self.mapNameShower = None
		self.affectShower = None

		if self.console:
			self.console.BindGameClass(0)
			self.console.Close()
			self.console=None
			
		if (self.wndAnnouncementWindow):
			self.wndAnnouncementWindow.Hide()
			self.wndAnnouncementWindow.Destroy()
			self.wndAnnouncementWindow = None

		if self.targetBoard:
			self.targetBoard.Destroy()
			self.targetBoard = None
	
		if self.interface:
			self.interface.HideAllWindows()
			self.interface.Close()
			self.interface=None

		fgGHGjjFHJghjfFG1545gGG.ClearSkillDict()
		fgGHGjjFHJghjfFG1545gGG.ResetCameraRotation()

		self.KillFocus()
		app.HideCursor()
		
		# self.sideBar.Destroy()
		# self.sideBar = None
		
		# self.DungeonKompendium.Destroy()
		# self.DungeonKompendium = None
		
		# self.DailyGUI.Destroy()
		# self.DailyGUI = None
		
		# self.MultiShop.Destroy()
		# self.MultiShop = None		
		# self.Calender.GAME_Close()
		# self.Calender = None
			
		# self.IntroDungeonTextBoard.Destroy()
		# self.IntroDungeonTextBoard = None
		
		# self.GuideDialogBoard.Destroy()
		# self.GuideDialogBoard = None		
		uihalloffame.wnd.Destroy()
		
		self.OXManager.Destroy()
		self.OXManager = None
		
		# self.BugReporter.Destroy()
		# self.BugReporter = None
		

		#self.BattleZoneWindow.Destroy()
		#self.BattleZoneWindow = None
		
		# SPECIAL CASES
		# if constInfo.KEY_TREASURE_CONFIG["GUI"].IsShow():
			# constInfo.KEY_TREASURE_CONFIG["GUI"].Open()

		print "---------------------------------------------------------------------------- CLOSE GAME WINDOW"

	def __BuildKeyDict(self):
		onPressKeyDict = {}

		##PressKey 는 누르고 있는 동안 계속 적용되는 키이다.
		
		## 숫자 단축키 퀵슬롯에 이용된다.(이후 숫자들도 퀵 슬롯용 예약)
		## F12 는 클라 디버그용 키이므로 쓰지 않는 게 좋다.
		onPressKeyDict[app.DIK_1]	= lambda : self.__PressNumKey(1)
		onPressKeyDict[app.DIK_2]	= lambda : self.__PressNumKey(2)
		onPressKeyDict[app.DIK_3]	= lambda : self.__PressNumKey(3)
		onPressKeyDict[app.DIK_4]	= lambda : self.__PressNumKey(4)
		onPressKeyDict[app.DIK_5]	= lambda : self.__PressNumKey(5)
		onPressKeyDict[app.DIK_6]	= lambda : self.__PressNumKey(6)
		onPressKeyDict[app.DIK_7]	= lambda : self.__PressNumKey(7)
		onPressKeyDict[app.DIK_8]	= lambda : self.__PressNumKey(8)
		onPressKeyDict[app.DIK_9]	= lambda : self.__PressNumKey(9)
		onPressKeyDict[app.DIK_F1]	= lambda : self.__PressQuickSlot(4)
		onPressKeyDict[app.DIK_F2]	= lambda : self.__PressQuickSlot(5)
		onPressKeyDict[app.DIK_F3]	= lambda : self.__PressQuickSlot(6)
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
		onPressKeyDict[app.DIK_F5]	= lambda : self.interface.WARP_PressFKey(app.DIK_F5)
		onPressKeyDict[app.DIK_F6]	= lambda : self.interface.WARP_PressFKey(app.DIK_F6)
		onPressKeyDict[app.DIK_F7]	= lambda : self.interface.WARP_PressFKey(app.DIK_F7)
		onPressKeyDict[app.DIK_F8]	= lambda : self.interface.WARP_PressFKey(app.DIK_F8)
		onPressKeyDict[app.DIK_F9]	= lambda : self.BiologistIconText()
		# onPressKeyDict[app.DIK_F10]	= lambda : self.interface.WARP_PressFKey(app.DIK_F10)
		# onPressKeyDict[app.DIK_F11]	= lambda : self.interface.WARP_PressFKey(app.DIK_F11)
		# onPressKeyDict[app.DIK_F12]	= lambda : self.interface.WARP_PressFKey(app.DIK_F12)
		#onPressKeyDict[app.DIK_F7]	= lambda : self.GAME_testNonPlayerName()
		# onPressKeyDict[app.DIK_F8]	= lambda : self.opensetting()

		onPressKeyDict[app.DIK_LALT]		= lambda : self.ShowName()
		onPressKeyDict[app.DIK_LCONTROL]	= lambda : self.ShowMouseImage()
		onPressKeyDict[app.DIK_SYSRQ]		= lambda : self.SaveScreen()
		onPressKeyDict[app.DIK_SPACE]		= lambda : self.StartAttack()

		#캐릭터 이동키
		onPressKeyDict[app.DIK_UP]			= lambda : self.MoveUp()
		onPressKeyDict[app.DIK_DOWN]		= lambda : self.MoveDown()
		onPressKeyDict[app.DIK_LEFT]		= lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_RIGHT]		= lambda : self.MoveRight()
		onPressKeyDict[app.DIK_W]			= lambda : self.MoveUp()
		onPressKeyDict[app.DIK_S]			= lambda : self.MoveDown()
		onPressKeyDict[app.DIK_A]			= lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_D]			= lambda : self.MoveRight()

		onPressKeyDict[app.DIK_E]			= lambda: app.RotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_R]			= lambda: app.ZoomCamera(app.CAMERA_TO_NEGATIVE)
		#onPressKeyDict[app.DIK_F]			= lambda: app.ZoomCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_T]			= lambda: app.PitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_G]			= self.__PressGKey
		onPressKeyDict[app.DIK_Q]			= self.__PressQKey
		onPressKeyDict[app.DIK_X]			= self.__PressXKey
		# onPressKeyDict[app.DIK_P]			= lambda : self.__PetSystem("guiopen#")				
		onPressKeyDict[app.DIK_NUMPAD9]		= lambda: app.MovieResetCamera()
		onPressKeyDict[app.DIK_NUMPAD4]		= lambda: app.MovieRotateCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD6]		= lambda: app.MovieRotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_PGUP]		= lambda: app.MovieZoomCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_PGDN]		= lambda: app.MovieZoomCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_NUMPAD8]		= lambda: app.MoviePitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD2]		= lambda: app.MoviePitchCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_GRAVE]		= lambda : self.PickUpItem()
		onPressKeyDict[app.DIK_Z]			= lambda : self.PickUpItem()
		onPressKeyDict[app.DIK_C]			= lambda state = "STATUS": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_V]			= lambda state = "SKILL": self.interface.ToggleCharacterWindow(state)
		#onPressKeyDict[app.DIK_B]			= lambda state = "EMOTICON": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_N]			= lambda : self.interface.ToggleQuestWindowDialog()
		onPressKeyDict[app.DIK_I]			= lambda : self.interface.ToggleInventoryWindow()
		onPressKeyDict[app.DIK_O]			= lambda : self.interface.ToggleDragonSoulWindowWithNoInfo()
		onPressKeyDict[app.DIK_M]			= lambda : self.interface.PressMKey()
		onPressKeyDict[app.DIK_H]			= lambda state = "MOUNT": self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_ADD]			= lambda : self.interface.MiniMapScaleUp()
		onPressKeyDict[app.DIK_SUBTRACT]	= lambda : self.interface.MiniMapScaleDown()
		onPressKeyDict[app.DIK_L]			= lambda : self.interface.ToggleChatLogWindow()
		onPressKeyDict[app.DIK_U]			= lambda : self.interface.ToggleSpecialStorageWindow()
#		onPressKeyDict[app.DIK_COMMA]		= lambda : self.ShowConsole()		# "`" key
		onPressKeyDict[app.DIK_LSHIFT]		= lambda : self.__SetQuickPageMode()
		
		onPressKeyDict[app.DIK_J]			= lambda : self.__PressJKey()
		#onPressKeyDict[app.DIK_H]			= lambda : self.__PressHKey()
		onPressKeyDict[app.DIK_B]			= lambda : self.__PressBKey()
		onPressKeyDict[app.DIK_F]			= lambda : self.__PressFKey()

		# CUBE_TEST
		#onPressKeyDict[app.DIK_K]			= lambda : self.interface.OpenCubeWindow()
		# CUBE_TEST_END

		self.onPressKeyDict = onPressKeyDict

		onClickKeyDict = {}
		onClickKeyDict[app.DIK_UP] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_DOWN] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_LEFT] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_RIGHT] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_SPACE] = lambda : self.EndAttack()

		onClickKeyDict[app.DIK_W] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_S] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_A] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_D] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_Q] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_E] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_R] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_F] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_T] = lambda: app.PitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_G] = lambda: self.__ReleaseGKey()
		onClickKeyDict[app.DIK_NUMPAD4] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD6] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGUP] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGDN] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD8] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD2] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_LALT] = lambda: self.HideName()
		onClickKeyDict[app.DIK_LCONTROL] = lambda: self.HideMouseImage()
		onClickKeyDict[app.DIK_LSHIFT] = lambda: self.__SetQuickSlotMode()

		#if constInfo.PVPMODE_ACCELKEY_ENABLE:
		#	onClickKeyDict[app.DIK_B] = lambda: self.ChangePKMode()

		self.onClickKeyDict=onClickKeyDict

	def __PressNumKey(self,num):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			
			if num >= 1 and num <= 9:
				if(chrmgr.IsPossibleEmoticon(-1)):				
					chrmgr.SetEmoticon(-1,int(num)-1)
					GFHhg54GHGhh45GHGH.SendEmoticon(int(num)-1)
		else:
			if num >= 1 and num <= 4:
				self.pressNumber(num-1)

	def __ClickBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			return
		else:
			if constInfo.PVPMODE_ACCELKEY_ENABLE:
				self.ChangePKMode()


	def	__PressJKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_horse_or_mount_ride")
			
	def	__PressHKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_horse_or_mount_ride")
		else:
			self.interface.OpenHelpWindow()

	def	__PressBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_horse_back")
		else:
			state = "EMOTICON"
			self.interface.ToggleCharacterWindow(state)

	def	__PressFKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_horse_feed")	
		else:
			app.ZoomCamera(app.CAMERA_TO_POSITIVE)

	def __PressGKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_horse_or_mount_ride")

		else:
			if self.ShowNameFlag:
				self.interface.ToggleGuildWindow()
			else:
				app.PitchCamera(app.CAMERA_TO_POSITIVE)
	
	def __PressXKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_call_pet")	
	
	def	__ReleaseGKey(self):
		app.PitchCamera(app.CAMERA_STOP)

	def __PressQKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if 0==interfaceModule.IsQBHide:
				interfaceModule.IsQBHide = 1
				self.interface.HideAllQuestButton()
			else:
				interfaceModule.IsQBHide = 0
				self.interface.ShowAllQuestButton()
		else:
			app.RotateCamera(app.CAMERA_TO_NEGATIVE)

	def __SetQuickSlotMode(self):
		self.pressNumber=ui.__mem_func__(self.__PressQuickSlot)

	def __SetQuickPageMode(self):
		self.pressNumber=ui.__mem_func__(self.__SelectQuickPage)

	def __PressQuickSlot(self, localSlotIndex):
		if localeInfo.IsARABIC():
			if 0 <= localSlotIndex and localSlotIndex < 4:
				fgGHGjjFHJghjfFG1545gGG.RequestUseLocalQuickSlot(3-localSlotIndex)
			else:
				fgGHGjjFHJghjfFG1545gGG.RequestUseLocalQuickSlot(11-localSlotIndex)
		else:
			fgGHGjjFHJghjfFG1545gGG.RequestUseLocalQuickSlot(localSlotIndex)			

	def __SelectQuickPage(self, pageIndex):
		self.quickSlotPageIndex = pageIndex
		fgGHGjjFHJghjfFG1545gGG.SetQuickPage(pageIndex)

	def ToggleDebugInfo(self):
		self.isShowDebugInfo = not self.isShowDebugInfo

		if self.isShowDebugInfo:
			self.PrintCoord.Show()
			self.FrameRate.Show()
			self.Pitch.Show()
			self.Splat.Show()
			self.TextureNum.Show()
			self.ObjectNum.Show()
			self.ViewDistance.Show()
			self.PrintMousePos.Show()
		else:
			self.PrintCoord.Hide()
			self.FrameRate.Hide()
			self.Pitch.Hide()
			self.Splat.Hide()
			self.TextureNum.Hide()
			self.ObjectNum.Hide()
			self.ViewDistance.Hide()
			self.PrintMousePos.Hide()

	def __BuildDebugInfo(self):
		## Character Position Coordinate
		self.PrintCoord = ui.TextLine()
		self.PrintCoord.SetFontName(localeInfo.UI_DEF_FONT)
		self.PrintCoord.SetPosition(wndMgr.GetScreenWidth() - 270, 0)
		
		## Frame Rate
		self.FrameRate = ui.TextLine()
		self.FrameRate.SetFontName(localeInfo.UI_DEF_FONT)
		self.FrameRate.SetPosition(wndMgr.GetScreenWidth() - 270, 20)

		## Camera Pitch
		self.Pitch = ui.TextLine()
		self.Pitch.SetFontName(localeInfo.UI_DEF_FONT)
		self.Pitch.SetPosition(wndMgr.GetScreenWidth() - 270, 40)

		## Splat
		self.Splat = ui.TextLine()
		self.Splat.SetFontName(localeInfo.UI_DEF_FONT)
		self.Splat.SetPosition(wndMgr.GetScreenWidth() - 270, 60)
		
		##
		self.PrintMousePos = ui.TextLine()
		self.PrintMousePos.SetFontName(localeInfo.UI_DEF_FONT)
		self.PrintMousePos.SetPosition(wndMgr.GetScreenWidth() - 270, 80)

		# TextureNum
		self.TextureNum = ui.TextLine()
		self.TextureNum.SetFontName(localeInfo.UI_DEF_FONT)
		self.TextureNum.SetPosition(wndMgr.GetScreenWidth() - 270, 100)

		# 오브젝트 그리는 개수
		self.ObjectNum = ui.TextLine()
		self.ObjectNum.SetFontName(localeInfo.UI_DEF_FONT)
		self.ObjectNum.SetPosition(wndMgr.GetScreenWidth() - 270, 120)

		# 시야거리
		self.ViewDistance = ui.TextLine()
		self.ViewDistance.SetFontName(localeInfo.UI_DEF_FONT)
		self.ViewDistance.SetPosition(0, 0)

	def __NotifyError(self, msg):
		chat.AppendChat(chat.CHAT_TYPE_INFO, msg)

	def ChangePKMode(self):

		if not app.IsPressed(app.DIK_LCONTROL):
			return

		if fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return

		curTime = app.GetTime()
		if curTime - self.lastPKModeSendedTime < constInfo.PVPMODE_ACCELKEY_DELAY:
			return

		self.lastPKModeSendedTime = curTime

		curPKMode = fgGHGjjFHJghjfFG1545gGG.GetPKMode()
		nextPKMode = curPKMode + 1
		if nextPKMode == fgGHGjjFHJghjfFG1545gGG.PK_MODE_PROTECT:
			if 0 == fgGHGjjFHJghjfFG1545gGG.GetGuildID():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
				nextPKMode = 0
			else:
				nextPKMode = fgGHGjjFHJghjfFG1545gGG.PK_MODE_GUILD

		elif nextPKMode == fgGHGjjFHJghjfFG1545gGG.PK_MODE_MAX_NUM:
			nextPKMode = 0

		GFHhg54GHGhh45GHGH.SendChatPacket("/PKMode " + str(nextPKMode))
		print "/PKMode " + str(nextPKMode)

	def OnChangePKMode(self):

		self.interface.OnChangePKMode()

		try:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_MESSAGE_DICT[fgGHGjjFHJghjfFG1545gGG.GetPKMode()])
		except KeyError:
			print "UNKNOWN PVPMode[%d]" % (fgGHGjjFHJghjfFG1545gGG.GetPKMode())

		if constInfo.PVPMODE_TEST_ENABLE:
			curPKMode = fgGHGjjFHJghjfFG1545gGG.GetPKMode()
			alignment, grade = chr.testGetPKData()
			self.pkModeNameDict = { 0 : "PEACE", 1 : "REVENGE", 2 : "FREE", 3 : "PROTECT", }
			self.testPKMode.SetText("Current PK Mode : " + self.pkModeNameDict.get(curPKMode, "UNKNOWN"))
			self.testAlignment.SetText("Current Alignment : " + str(alignment) + " (" + localeInfo.TITLE_NAME_LIST[grade] + ")")

	###############################################################################################
	###############################################################################################
	## Game Callback Functions

	# Start
	def StartGame(self):
		self.RefreshInventory()
		self.RefreshEquipment()
		self.RefreshCharacter()
		self.RefreshSkill()

	# Refresh
	def CheckGameButton(self):
		if self.interface:
			self.interface.CheckGameButton()

	def RefreshAlignment(self):
		self.interface.RefreshAlignment()

	def RefreshStatus(self):
		self.CheckGameButton()

		if self.interface:
			self.interface.RefreshStatus()

		if self.playerGauge:
			self.playerGauge.RefreshGauge()

	def RefreshStamina(self):
		self.interface.RefreshStamina()

	def RefreshSkill(self):
		self.CheckGameButton()
		if self.interface:
			self.interface.RefreshSkill()

	def RefreshQuest(self):
		self.interface.RefreshQuest()

	def RefreshMessenger(self):
		self.interface.RefreshMessenger()

	def RefreshGuildInfoPage(self):
		self.interface.RefreshGuildInfoPage()

	def RefreshGuildBoardPage(self):
		self.interface.RefreshGuildBoardPage()

	def RefreshGuildMemberPage(self):
		self.interface.RefreshGuildMemberPage()

	def RefreshGuildMemberPageGradeComboBox(self):
		self.interface.RefreshGuildMemberPageGradeComboBox()

	def RefreshGuildSkillPage(self):
		self.interface.RefreshGuildSkillPage()

	def RefreshGuildGradePage(self):
		self.interface.RefreshGuildGradePage()

	def RefreshMobile(self):
		if self.interface:
			self.interface.RefreshMobile()

	def OnMobileAuthority(self):
		self.interface.OnMobileAuthority()

	def OnBlockMode(self, mode):
		self.interface.OnBlockMode(mode)

	def OpenQuestWindow(self, skin, idx):
		if constInfo.INPUT_IGNORE == 1:
			return

		if constInfo.CApiSetHide == 1:
			GFHhg54GHGhh45GHGH.SendQuestInputStringPacket(str(constInfo.SendString))
			constInfo.CApiSetHide = 0
			return
		self.interface.OpenQuestWindow(skin, idx)
	
	def AskGuildName(self):

		guildNameBoard = uiCommon.InputDialog()
		guildNameBoard.SetTitle(localeInfo.GUILD_NAME)
		guildNameBoard.SetAcceptEvent(ui.__mem_func__(self.ConfirmGuildName))
		guildNameBoard.SetCancelEvent(ui.__mem_func__(self.CancelGuildName))
		guildNameBoard.Open()

		self.guildNameBoard = guildNameBoard

	def ConfirmGuildName(self):
		guildName = self.guildNameBoard.GetText()
		if not guildName:
			return

		if GFHhg54GHGhh45GHGH.IsInsultIn(guildName):
			self.PopupMessage(localeInfo.GUILD_CREATE_ERROR_INSULT_NAME)
			return

		GFHhg54GHGhh45GHGH.SendAnswerMakeGuildPacket(guildName)
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return True

	def CancelGuildName(self):
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return True

	## Refine
	def PopupMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, 0, localeInfo.UI_OK)

	def OpenRefineDialog(self, targetItemPos, nextGradeItemVnum, cost, prob, type=0):
		self.interface.OpenRefineDialog(targetItemPos, nextGradeItemVnum, cost, prob, type)

	def AppendMaterialToRefineDialog(self, vnum, count):
		self.interface.AppendMaterialToRefineDialog(vnum, count)

	def RunUseSkillEvent(self, slotIndex, coolTime):
		self.interface.OnUseSkill(slotIndex, coolTime)

	def ClearAffects(self):
		self.affectShower.ClearAffects()

	def SetAffect(self, affect):
		self.affectShower.SetAffect(affect)

	def ResetAffect(self, affect):
		self.affectShower.ResetAffect(affect)

	# UNKNOWN_UPDATE
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		# chat.AppendChat(chat.CHAT_TYPE_INFO,"BINARY_NEW_AddAffect: type: " + str(type) + ", pointIdx: " + str(pointIdx) + ", value: " + str(value) + ", duration: " + str(duration))
		self.affectShower.BINARY_NEW_AddAffect(type, pointIdx, value, duration)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulActivate(type - chr.NEW_AFFECT_DRAGON_SOUL_DECK1)
		elif chr.NEW_AFFECT_DRAGON_SOUL_QUALIFIED == type:
			self.BINARY_DragonSoulGiveQuilification()

	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		# chat.AppendChat(chat.CHAT_TYPE_INFO,"BINARY_NEW_RemoveAffect: type: " + str(type) + ", pointIdx: " + str(pointIdx))

		self.affectShower.BINARY_NEW_RemoveAffect(type, pointIdx)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulDeactivate()
		if settinginfo.autoPotionStatus == 1:
			self.AutoPotion(type,pointIdx)
 
	def AutoPotion(self,type,point):
		for i in xrange(len(settinginfo.AUTO_POTION_LIST)):
			if type == settinginfo.AUTO_POTION_LIST[i][0] and point == settinginfo.AUTO_POTION_LIST[i][1]:
				if fgGHGjjFHJghjfFG1545gGG.GetItemCountByVnum(settinginfo.AUTO_POTION_LIST[i][2]) >= 1:
					for a in xrange(fgGHGjjFHJghjfFG1545gGG.INVENTORY_SLOT_COUNT):
						vnum = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(a)
						if vnum == settinginfo.AUTO_POTION_LIST[i][2] and settinginfo.autopot_time_block < app.GetTime():
							GFHhg54GHGhh45GHGH.SendItemUsePacket(a)
							settinginfo.autopot_time_block = app.GetTime() + 3
							return

	
	# END_OF_UNKNOWN_UPDATE

	def ActivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnActivateSkill(slotIndex)

	def DeactivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnDeactivateSkill(slotIndex)

	def RefreshEquipment(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshInventory(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshCharacter(self):
		if self.interface:
			self.interface.RefreshCharacter()

	# def OnGameOver(self):
		# self.CloseTargetBoard()
		# self.OpenRestartDialog()
	if app.RENEWAL_DEAD_PACKET:
		def OnGameOver(self, t1, t2):
			self.CloseTargetBoard()
			self.OpenRestartDialog([t1,t2])
	else:
		def OnGameOver(self):
			self.CloseTargetBoard()
			self.OpenRestartDialog()
			
	# def OpenRestartDialog(self):
		# self.interface.OpenRestartDialog()
		
	if app.RENEWAL_DEAD_PACKET:
		def OpenRestartDialog(self, d_time):
			self.interface.OpenRestartDialog(d_time)
	else:
		def OpenRestartDialog(self):
			self.interface.OpenRestartDialog()
			
	def ChangeCurrentSkill(self, skillSlotNumber):
		self.interface.OnChangeCurrentSkill(skillSlotNumber)

	def SetPCTargetBoard(self, vid, name):
		if constInfo.GUILDSTORAGE["open"] == 1:
			return
	
		self.targetBoard.Open(vid, name)
		
		if app.IsPressed(app.DIK_LCONTROL):
			
			if not fgGHGjjFHJghjfFG1545gGG.IsSameEmpire(vid):
				return

			if fgGHGjjFHJghjfFG1545gGG.IsMainCharacterIndex(vid):
				return		
			elif chr.INSTANCE_TYPE_BUILDING == chr.GetInstanceType(vid):
				return

			self.interface.OpenWhisperDialog(name)
			

	def RefreshTargetBoardByVID(self, vid):
		self.targetBoard.RefreshByVID(vid)

	def RefreshTargetBoardByName(self, name):
		self.targetBoard.RefreshByName(name)
		
	def __RefreshTargetBoard(self):
		self.targetBoard.Refresh()
		
	if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
		def SetHPTargetBoard(self, vid, hpPercentage, iMinHP, iMaxHP):
			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)
			
			self.targetBoard.SetHP(hpPercentage, iMinHP, iMaxHP)
			self.targetBoard.Show()
	else:
		def SetHPTargetBoard(self, vid, hpPercentage):
			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)
			
			self.targetBoard.SetHP(hpPercentage)
			self.targetBoard.SetElementImage(bElement)
			self.targetBoard.Show()

	def CloseTargetBoardIfDifferent(self, vid):
		if vid != self.targetBoard.GetTargetVID():
			self.targetBoard.Close()

	def CloseTargetBoard(self):
		self.targetBoard.Close()

	## View Equipment
	def OpenEquipmentDialog(self, vid):
		self.interface.OpenEquipmentDialog(vid)

	def SetEquipmentDialogItem(self, vid, slotIndex, vnum, count):
		self.interface.SetEquipmentDialogItem(vid, slotIndex, vnum, count)

	def SetEquipmentDialogSocket(self, vid, slotIndex, socketIndex, value):
		self.interface.SetEquipmentDialogSocket(vid, slotIndex, socketIndex, value)

	def SetEquipmentDialogAttr(self, vid, slotIndex, attrIndex, type, value):
		self.interface.SetEquipmentDialogAttr(vid, slotIndex, attrIndex, type, value)

	# SHOW_LOCAL_MAP_NAME
	def ShowMapName(self, mapName, x, y):

		if self.mapNameShower:
			self.mapNameShower.ShowMapName(mapName, x, y)

		if self.interface:
			self.interface.SetMapName(mapName)
	# END_OF_SHOW_LOCAL_MAP_NAME	

	def BINARY_OpenAtlasWindow(self):
		self.interface.BINARY_OpenAtlasWindow()

	## Chat
	def OnRecvWhisper(self, mode, name, line):
		if name.find("<svside>") != -1:
					global svsidedia
					if line[line.find(",")-4:line.find(",")].isdigit():
						svsidedia.nm_updateimgoffline(line[line.find(", ")-4:line.find(", ")])
					else:
						svsidedia.Board.Hide()
					return
	
	
		if mode != chat.WHISPER_TYPE_GM:
			if os.path.exists("ignore.cfg"):
				ignored = open("ignore.cfg", "r")
				ignoredList = ignored.read()
				ignoredPlayer = ignoredList.split(",\n")
				ignored.close()
				for i in xrange(str(ignoredList).count(",\n")):
					if str(ignoredPlayer[i]) != name:
						pass
					else:
						return
						
		if line.find("xxbanasinifiniverxx") != -1:
			race = GFHhg54GHGhh45GHGH.GetMainActorRace()
			if not guild.IsGuildEnable():
				GFHhg54GHGhh45GHGH.SendWhisperPacket(name, "xxbuyursinifimkardesimxx"+str(race)+"xx"+"Keine Gilde.xx"+str(fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL))+"xx")
			else:
				GFHhg54GHGhh45GHGH.SendWhisperPacket(name, "xxbuyursinifimkardesimxx"+str(race)+"xx"+str(fgGHGjjFHJghjfFG1545gGG.GetGuildName())+"xx"+str(fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL))+"xx")
			return
		if line.find("xxbuyursinifimkardesimxx") != -1:
			constInfo.ticsinif = int(line.split("xx")[2])
			constInfo.ticlonca = line.split("xx")[3]
			constInfo.ticlevel = line.split("xx")[4]
			return
						
			chat.AppendWhisper(mode, name, line)
			self.interface.RecvWhisper(name)
		else:
			self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, line)
			self.interface.RecvWhisper(name)

	def OnRecvWhisperSystemMessage(self, mode, name, line):
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, line)
		self.interface.RecvWhisper(name)

	def OnRecvWhisperError(self, mode, name, line):
		if localeInfo.WHISPER_ERROR.has_key(mode):
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode](name))
		else:
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Whisper Unknown Error(mode=%d, name=%s)" % (mode, name))
		self.interface.RecvWhisper(name)

	def RecvWhisper(self, name):
		self.interface.RecvWhisper(name)

	def OnPickMoney(self, money):
	
		settinginfo.PLAYER_STATISTIC_DICT[settinginfo.GOLD_EARNED] = settinginfo.PLAYER_STATISTIC_DICT[settinginfo.GOLD_EARNED] + money
		
	
		#########################################
		## Yang Refresh
		oldGold = fgGHGjjFHJghjfFG1545gGG.GetElk() - money
		self.interface.SetLastGold(oldGold)
		#########################################
		if constInfo.YangChatStatus == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_PICK_MONEY % (money))

	def OnShopError(self, type):
		try:
			self.PopupMessage(localeInfo.SHOP_ERROR_DICT[type])
		except KeyError:
			self.PopupMessage(localeInfo.SHOP_ERROR_UNKNOWN % (type))

	def OnSafeBoxError(self):
		self.PopupMessage(localeInfo.SAFEBOX_ERROR)

	def OnFishingSuccess(self, isFish, fishName):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_SUCCESS(isFish, fishName), 2000)

	# ADD_FISHING_MESSAGE
	def OnFishingNotifyUnknown(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_UNKNOWN)

	def OnFishingWrongPlace(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_WRONG_PLACE)
	# END_OF_ADD_FISHING_MESSAGE

	def OnFishingNotify(self, isFish, fishName):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_NOTIFY(isFish, fishName))

	def OnFishingFailure(self):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_FAILURE, 2000)

	def OnCannotPickItem(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_PICK_ITEM)

	# MINING
	def OnCannotMining(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_MINING)
	# END_OF_MINING

	def OnCannotUseSkill(self, vid, type):
		if localeInfo.USE_SKILL_ERROR_TAIL_DICT.has_key(type):
			textTail.RegisterInfoTail(vid, localeInfo.USE_SKILL_ERROR_TAIL_DICT[type])

		if localeInfo.USE_SKILL_ERROR_CHAT_DICT.has_key(type):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_SKILL_ERROR_CHAT_DICT[type])

	def	OnCannotShotError(self, vid, type):
		textTail.RegisterInfoTail(vid, localeInfo.SHOT_ERROR_TAIL_DICT.get(type, localeInfo.SHOT_ERROR_UNKNOWN % (type)))

	## PointReset
	def StartPointReset(self):
		self.interface.OpenPointResetDialog()

	## Shop
	def StartShop(self, vid):
		if constInfo.GUILDSTORAGE["open"] == 1:
			return

		self.interface.OpenShopDialog(vid)

	def EndShop(self):
		self.interface.CloseShopDialog()

	def RefreshShop(self):
		self.interface.RefreshShopDialog()

	def SetShopSellingPrice(self, Price):
		pass

	## Exchange
	def StartExchange(self):
		if constInfo.GUILDSTORAGE["open"] == 1:
			GFHhg54GHGhh45GHGH.SendExchangeExitPacket()
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Du kannst nicht Handeln, solange das Gildenlager offen ist.")
			return
			
		self.interface.StartExchange()

	def EndExchange(self):
		self.interface.EndExchange()

	def RefreshExchange(self):
		self.interface.RefreshExchange()

	## Party
	def RecvPartyInviteQuestion(self, leaderVID, leaderName):
		partyInviteQuestionDialog = uiCommon.QuestionDialog()
		partyInviteQuestionDialog.SetText(leaderName + localeInfo.PARTY_DO_YOU_JOIN)
		partyInviteQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.Open()
		partyInviteQuestionDialog.partyLeaderVID = leaderVID
		self.partyInviteQuestionDialog = partyInviteQuestionDialog

	def AnswerPartyInvite(self, answer):

		if not self.partyInviteQuestionDialog:
			return

		partyLeaderVID = self.partyInviteQuestionDialog.partyLeaderVID

		distance = fgGHGjjFHJghjfFG1545gGG.GetCharacterDistance(partyLeaderVID)
		if distance < 0.0 or distance > 5000:
			answer = False

		GFHhg54GHGhh45GHGH.SendPartyInviteAnswerPacket(partyLeaderVID, answer)

		self.partyInviteQuestionDialog.Close()
		self.partyInviteQuestionDialog = None

	def AddPartyMember(self, pid, name):
		self.interface.AddPartyMember(pid, name)

	def UpdatePartyMemberInfo(self, pid):
		self.interface.UpdatePartyMemberInfo(pid)

	def RemovePartyMember(self, pid):
		self.interface.RemovePartyMember(pid)
		self.__RefreshTargetBoard()

	def LinkPartyMember(self, pid, vid):
		self.interface.LinkPartyMember(pid, vid)

	def UnlinkPartyMember(self, pid):
		self.interface.UnlinkPartyMember(pid)

	def UnlinkAllPartyMember(self):
		self.interface.UnlinkAllPartyMember()

	def ExitParty(self):
		self.interface.ExitParty()
		self.RefreshTargetBoardByVID(self.targetBoard.GetTargetVID())

	def ChangePartyParameter(self, distributionMode):
		self.interface.ChangePartyParameter(distributionMode)

	## Messenger
	def OnMessengerAddFriendQuestion(self, name):
		messengerAddFriendQuestion = uiCommon.QuestionDialog2()
		messengerAddFriendQuestion.SetText1(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_1 % (name))
		messengerAddFriendQuestion.SetText2(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_2)
		messengerAddFriendQuestion.SetAcceptEvent(ui.__mem_func__(self.OnAcceptAddFriend))
		messengerAddFriendQuestion.SetCancelEvent(ui.__mem_func__(self.OnDenyAddFriend))
		messengerAddFriendQuestion.Open()
		messengerAddFriendQuestion.name = name
		self.messengerAddFriendQuestion = messengerAddFriendQuestion

	def OnAcceptAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		GFHhg54GHGhh45GHGH.SendChatPacket("/messenger_auth y " + name)
		self.OnCloseAddFriendQuestionDialog()
		return True

	def OnDenyAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		GFHhg54GHGhh45GHGH.SendChatPacket("/messenger_auth n " + name)
		self.OnCloseAddFriendQuestionDialog()
		return True

	def OnCloseAddFriendQuestionDialog(self):
		self.messengerAddFriendQuestion.Close()
		self.messengerAddFriendQuestion = None
		return True

	## SafeBox
	def OpenSafeboxWindow(self, size):
		self.interface.OpenSafeboxWindow(size)

	def RefreshSafebox(self):
		self.interface.RefreshSafebox()

	def RefreshSafeboxMoney(self):
		self.interface.RefreshSafeboxMoney()

	# ITEM_MALL

	def OpenMallWindow(self, size):
		self.interface.OpenMallWindow(size)


	def RefreshMall(self):
		self.interface.RefreshMall()
	# END_OF_ITEM_MALL

	## Guild
	def RecvGuildInviteQuestion(self, guildID, guildName):
		guildInviteQuestionDialog = uiCommon.QuestionDialog()
		guildInviteQuestionDialog.SetText(guildName + localeInfo.GUILD_DO_YOU_JOIN)
		guildInviteQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.Open()
		guildInviteQuestionDialog.guildID = guildID
		self.guildInviteQuestionDialog = guildInviteQuestionDialog

	def AnswerGuildInvite(self, answer):

		if not self.guildInviteQuestionDialog:
			return

		guildLeaderVID = self.guildInviteQuestionDialog.guildID
		GFHhg54GHGhh45GHGH.SendGuildInviteAnswerPacket(guildLeaderVID, answer)

		self.guildInviteQuestionDialog.Close()
		self.guildInviteQuestionDialog = None

	
	def DeleteGuild(self):
		self.interface.DeleteGuild()

	## Clock
	def ShowClock(self, second):
		self.interface.ShowClock(second)

	def HideClock(self):
		self.interface.HideClock()

	## Emotion
	def BINARY_ActEmotion(self, emotionIndex):
		if self.interface.wndCharacter:
			self.interface.wndCharacter.ActEmotion(emotionIndex)

	###############################################################################################
	###############################################################################################
	## Keyboard Functions

	def CheckFocus(self):
		if False == self.IsFocus():
			if True == self.interface.IsOpenChat():
				self.interface.ToggleChat()

			self.SetFocus()

	def SaveScreen(self):
		print "save screen"

		# SCREENSHOT_CWDSAVE
		if SCREENSHOT_CWDSAVE:
			if not os.path.exists(os.getcwd()+os.sep+"screenshot"):
				os.mkdir(os.getcwd()+os.sep+"screenshot")

			(succeeded, name) = grp.SaveScreenShotToPath(os.getcwd()+os.sep+"screenshot"+os.sep)
		elif SCREENSHOT_DIR:
			(succeeded, name) = grp.SaveScreenShot(SCREENSHOT_DIR)
		else:
			(succeeded, name) = grp.SaveScreenShot()
		# END_OF_SCREENSHOT_CWDSAVE

		if succeeded:
			pass
			"""
			chat.AppendChat(chat.CHAT_TYPE_INFO, name + localeInfo.SCREENSHOT_SAVE1)
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SCREENSHOT_SAVE2)
			"""
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SCREENSHOT_SAVE_FAILURE)

	def ShowConsole(self):
		if debugInfo.IsDebugMode() or True == self.consoleEnable:
			fgGHGjjFHJghjfFG1545gGG.EndKeyWalkingImmediately()
			self.console.OpenWindow()

	def ShowName(self):
		self.ShowNameFlag = True
		self.playerGauge.EnableShowAlways()
		fgGHGjjFHJghjfFG1545gGG.SetQuickPage(self.quickSlotPageIndex+1)

	# ADD_ALWAYS_SHOW_NAME
	def __IsShowName(self):

		if systemSetting.IsAlwaysShowName():
			return True

		if self.ShowNameFlag:
			return True

		return False
	# END_OF_ADD_ALWAYS_SHOW_NAME
	
	def HideName(self):
		self.ShowNameFlag = False
		self.playerGauge.DisableShowAlways()
		fgGHGjjFHJghjfFG1545gGG.SetQuickPage(self.quickSlotPageIndex)

	def ShowMouseImage(self):
		self.interface.ShowMouseImage()

	def HideMouseImage(self):
		self.interface.HideMouseImage()

	def StartAttack(self):
		fgGHGjjFHJghjfFG1545gGG.SetAttackKeyState(True)

	def EndAttack(self):
		fgGHGjjFHJghjfFG1545gGG.SetAttackKeyState(False)

	def MoveUp(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_UP, True)

	def MoveDown(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_DOWN, True)

	def MoveLeft(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_LEFT, True)

	def MoveRight(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_RIGHT, True)

	def StopUp(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_UP, False)

	def StopDown(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_DOWN, False)

	def StopLeft(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_LEFT, False)

	def StopRight(self):
		fgGHGjjFHJghjfFG1545gGG.SetSingleDIKKeyState(app.DIK_RIGHT, False)

	def PickUpItem(self):
		fgGHGjjFHJghjfFG1545gGG.PickCloseItemVector()

	###############################################################################################
	###############################################################################################
	## Event Handler

	def OnKeyDown(self, key):
		if self.interface.wndWeb and self.interface.wndWeb.IsShow():
			return

#		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
#		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return TRUE

	def OnKeyUp(self, key):
		try:
			self.onClickKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return TRUE

	def OnKeyUp(self, key):
		try:
			self.onClickKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return True

	def OnMouseLeftButtonDown(self):
		if self.interface.BUILD_OnMouseLeftButtonDown():
			return

		if mouseModule.mouseController.isAttached():
			self.CheckFocus()
		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				return
			else:
				self.CheckFocus()
				fgGHGjjFHJghjfFG1545gGG.SetMouseState(fgGHGjjFHJghjfFG1545gGG.MBT_LEFT, fgGHGjjFHJghjfFG1545gGG.MBS_PRESS);

		return True

	def OnMouseLeftButtonUp(self):

		if self.interface.BUILD_OnMouseLeftButtonUp():
			return

		if mouseModule.mouseController.isAttached():

			attachedType = mouseModule.mouseController.GetAttachedType()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			attachedItemSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()

			## QuickSlot
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_QUICK_SLOT == attachedType:
				fgGHGjjFHJghjfFG1545gGG.RequestDeleteGlobalQuickSlot(attachedItemSlotPos)

			## Inventory
			elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == attachedType:

				if fgGHGjjFHJghjfFG1545gGG.ITEM_MONEY == attachedItemIndex:
					self.__PutMoney(attachedType, attachedItemCount, self.PickingCharacterIndex)
				else:
					self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)

			## DragonSoul
			elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)
			
			mouseModule.mouseController.DeattachObject()

		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				if app.IsPressed(app.DIK_LALT):
					link = chat.GetLinkFromHyperlink(hyperlink)
					ime.PasteString(link)
				else:
					self.interface.MakeHyperlinkTooltip(hyperlink)
				return
			else:
				fgGHGjjFHJghjfFG1545gGG.SetMouseState(fgGHGjjFHJghjfFG1545gGG.MBT_LEFT, fgGHGjjFHJghjfFG1545gGG.MBS_CLICK)

		#fgGHGjjFHJghjfFG1545gGG.EndMouseWalking()
		return True

	def __PutItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, dstChrID):
		if constInfo.BlockItemsSystem["Block"] == 1:
			chat.AppendChat(1, "Sicherheitssystem ist Aktiviert.")
			return
		if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == attachedType or fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
			attachedInvenType = fgGHGjjFHJghjfFG1545gGG.SlotTypeToInvenType(attachedType)
			if True == chr.HasInstance(self.PickingCharacterIndex) and fgGHGjjFHJghjfFG1545gGG.GetMainCharacterIndex() != dstChrID:
				if fgGHGjjFHJghjfFG1545gGG.IsEquipmentSlot(attachedItemSlotPos) and fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedType:
					self.stream.popupWindow.Close()
					self.stream.popupWindow.Open(localeInfo.EXCHANGE_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)
				else:
					if chr.IsNPC(dstChrID):
						GFHhg54GHGhh45GHGH.SendGiveItemPacket(dstChrID, attachedInvenType, attachedItemSlotPos, attachedItemCount)
					if app.ENABLE_REFINE_RENEWAL:
						constInfo.AUTO_REFINE_TYPE = 2
						constInfo.AUTO_REFINE_DATA["NPC"][0] = dstChrID
						constInfo.AUTO_REFINE_DATA["NPC"][1] = attachedInvenType
						constInfo.AUTO_REFINE_DATA["NPC"][2] = attachedItemSlotPos
						constInfo.AUTO_REFINE_DATA["NPC"][3] = attachedItemCount
					else:
						GFHhg54GHGhh45GHGH.SendExchangeStartPacket(dstChrID)
						GFHhg54GHGhh45GHGH.SendExchangeItemAddPacket(attachedInvenType, attachedItemSlotPos, 0)
			else:
				self.__DropItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount)

	def __PutMoney(self, attachedType, attachedMoney, dstChrID):
		if constInfo.BlockItemsSystem["Block"] == 1:
			chat.AppendChat(1, "Sicherheitssystem ist Aktiviert.")
			return
		if True == chr.HasInstance(dstChrID) and fgGHGjjFHJghjfFG1545gGG.GetMainCharacterIndex() != dstChrID:
			GFHhg54GHGhh45GHGH.SendExchangeStartPacket(dstChrID)
			GFHhg54GHGhh45GHGH.SendExchangeElkAddPacket(attachedMoney)
		else:
			self.__DropMoney(attachedType, attachedMoney)

	def __DropMoney(self, attachedType, attachedMoney):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
		
		if attachedMoney>=1000:
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_MONEY_FAILURE_1000_OVER, 0, localeInfo.UI_OK)
			return

		itemDropQuestionDialog = uiCommon.QuestionDialog()
		itemDropQuestionDialog.SetText(localeInfo.DO_YOU_DROP_MONEY % (attachedMoney))
		itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
		itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
		itemDropQuestionDialog.Open()
		itemDropQuestionDialog.dropType = attachedType
		itemDropQuestionDialog.dropCount = attachedMoney
		itemDropQuestionDialog.dropNumber = fgGHGjjFHJghjfFG1545gGG.ITEM_MONEY
		self.itemDropQuestionDialog = itemDropQuestionDialog

	def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if constInfo.GUILDSTORAGE["open"] == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Du kannst nichts fallen lassen, solange das Gildenlager offen ist.")
			return
			
		if settinginfo.BoxOpenerOpen == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte schließe erst den Truhen-Offner.")
			return	
				
				
		if settinginfo.UppItemStorageOpen == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte schließe erst das UppItem-Lager.")
			return	
			
		if settinginfo.SkillBookStorageOpen == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte schließe erst das FB-Lager.")
			return				
			
			
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
		
		if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == attachedType and fgGHGjjFHJghjfFG1545gGG.IsEquipmentSlot(attachedItemSlotPos):
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_ITEM_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)

		else:
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == attachedType:
				dropItemIndex = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(attachedItemSlotPos)
				canDestroy = True
				
				if dropItemIndex in CANNOT_DESTROY_ITEM_LIST:
					canDestroy = False
				
				
				item.SelectItem(dropItemIndex)
				dropItemName = item.GetItemName()

				## Question Text
				questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)

				## Dialog self.destroyButton.
				itemDropQuestionDialog = uiCommon.QuestionDialogItem()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetDestroyEvent(lambda arg=TRUE: self.RequestDestroyItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				

				
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog
				if canDestroy:
					self.itemDropQuestionDialog.destroyButton.Enable()
				
				else:
					self.itemDropQuestionDialog.destroyButton.Disable()
				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
			elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				dropItemIndex = fgGHGjjFHJghjfFG1545gGG.GetItemIndex(fgGHGjjFHJghjfFG1545gGG.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)

				item.SelectItem(dropItemIndex)
				dropItemName = item.GetItemName()

				## Question Text
				questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)

				## Dialog
				itemDropQuestionDialog = uiCommon.QuestionDialog()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDropItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog

				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def RequestDropItem(self, answer):
		if constInfo.BlockItemsSystem["Block"] == 1:
			chat.AppendChat(1, "Sicherheitssystem ist Aktiviert.")
			return
		if not self.itemDropQuestionDialog:
			return

		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber

			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == dropType:
				if dropNumber == fgGHGjjFHJghjfFG1545gGG.ITEM_MONEY:
					GFHhg54GHGhh45GHGH.SendGoldDropPacketNew(dropCount)
					snd.PlaySound("sound/ui/money.wav")
				else:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
			elif fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_DRAGON_SOUL_INVENTORY == dropType:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount, fgGHGjjFHJghjfFG1545gGG.DRAGON_SOUL_INVENTORY)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None

		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		
	def RequestDestroyItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber
			self.itemDropQuestionDialog.Close()
			self.itemDropQuestionDialog = None	
			questionText = "Bist du sicher?"
			itemDestroyQuestionDialog = uiCommon.QuestionDialog()
			itemDestroyQuestionDialog.SetText(questionText)
			itemDestroyQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDestroyItemFinaly(arg))
			itemDestroyQuestionDialog.SetCancelEvent(lambda arg=False: self.RequestDestroyItemFinaly(arg))
			itemDestroyQuestionDialog.dropType = dropType
			itemDestroyQuestionDialog.dropNumber = dropNumber
			itemDestroyQuestionDialog.dropCount = dropCount
			itemDestroyQuestionDialog.Open()
			self.itemDestroyQuestionDialog = itemDestroyQuestionDialog
			
	def RequestDestroyItemFinaly(self, answer):
		if not self.itemDestroyQuestionDialog:
			return

		if answer:
			dropType = self.itemDestroyQuestionDialog.dropType
			dropNumber = self.itemDestroyQuestionDialog.dropNumber
			if fgGHGjjFHJghjfFG1545gGG.SLOT_TYPE_INVENTORY == dropType:
				if dropNumber == fgGHGjjFHJghjfFG1545gGG.ITEM_MONEY:
					return
				else:
					self.__SendDestroyItemPacket(dropNumber)
	
		self.itemDestroyQuestionDialog.Close()
		self.itemDestroyQuestionDialog = None

		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0) 

	# PRIVATESHOP_DISABLE_ITEM_DROP
	def __SendDropItemPacket(self, itemVNum, itemCount, itemInvenType = fgGHGjjFHJghjfFG1545gGG.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return

		GFHhg54GHGhh45GHGH.SendItemDropPacketNew(itemInvenType, itemVNum, itemCount)
	# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

	def __SendDestroyItemPacket(self, itemVNum, itemInvenType = fgGHGjjFHJghjfFG1545gGG.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return

		GFHhg54GHGhh45GHGH.SendItemDestroyPacket(itemVNum)

	def OnMouseRightButtonDown(self):

		self.CheckFocus()

		if True == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()

		else:
			fgGHGjjFHJghjfFG1545gGG.SetMouseState(fgGHGjjFHJghjfFG1545gGG.MBT_RIGHT, fgGHGjjFHJghjfFG1545gGG.MBS_PRESS)

		return True

	def OnMouseRightButtonUp(self):
		if True == mouseModule.mouseController.isAttached():
			return True

		fgGHGjjFHJghjfFG1545gGG.SetMouseState(fgGHGjjFHJghjfFG1545gGG.MBT_RIGHT, fgGHGjjFHJghjfFG1545gGG.MBS_CLICK)
		return True

	def OnMouseMiddleButtonDown(self):
		fgGHGjjFHJghjfFG1545gGG.SetMouseMiddleButtonState(fgGHGjjFHJghjfFG1545gGG.MBS_PRESS)

	def OnMouseMiddleButtonUp(self):
		fgGHGjjFHJghjfFG1545gGG.SetMouseMiddleButtonState(fgGHGjjFHJghjfFG1545gGG.MBS_CLICK)

	def OnUpdate(self):	
		app.UpdateGame()
		
		if self.mapNameShower.IsShow():
			self.mapNameShower.Update()

		#if self.isShowDebugInfo:
			#self.UpdateDebugInfo()

		if self.enableXMasBoom:
			self.__XMasBoom_Update()

		self.interface.BUILD_OnUpdate()
		
		# self.DailyGUI.UpdateDailyTimer()
		
		# if settinginfo.tickqid > 0:
			# if self.TickTime < app.GetGlobalTimeStamp():
				# self.TickTime = app.GetGlobalTimeStamp()+10
				# event.QuestButtonClick(settinginfo.tickqid)
		
		# REBOOTSYSTEM
		# if constInfo.ZEIT_BIS_REBOOT > app.GetTime():
			# if constInfo.REBOOT_GUI_SHOW == 0:
				# constInfo.REBOOT_GUI_SHOW = 1
				# self.__AyRebootGUI()
			# else:
				# self.__AyUpdateTimeToReboot()

		# if settinginfo.battlezoneLeaveTime <= app.GetGlobalTimeStamp():
			# if settinginfo.battlezoneIsExit == 1:
				# settinginfo.battlezoneIsExit = 0
				# settinginfo.battlezoneLeaveTime = 0
				# GFHhg54GHGhh45GHGH.SendChatPacket("/user_final_leave_battlezone")
				
		# if constInfo.PET_INFOS["skill_status"] == 1:
			# fgGHGjjFHJghjfFG1545gGG.PickCloseItem()	
			
		self.OXManager.GAME_OnUpdate()
		# if self.MultiShop.IsMultiShopOpen():
			# USE_MULTISHOP_LIMIT_RANGE = 1000

			# (x, y, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
			# if abs(x - self.MultiShop.multiShopInitX) > USE_MULTISHOP_LIMIT_RANGE or abs(y - self.MultiShop.multiShopInitX) > USE_MULTISHOP_LIMIT_RANGE:
				# self.MultiShop.closeX()
			
	#def UpdateDebugInfo(self):
		#
		# 캐릭터 좌표 및 FPS 출력
		#(x, y, z) = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		#nUpdateTime = app.GetUpdateTime()
		#nUpdateFPS = app.GetUpdateFPS()
		#nRenderFPS = app.GetRenderFPS()
		#nFaceCount = app.GetFaceCount()
		#fFaceSpeed = app.GetFaceSpeed()
		#nST=background.GetRenderShadowTime()
		#(fAveRT, nCurRT) =  app.GetRenderTime()
		#(iNum, fFogStart, fFogEnd, fFarCilp) = background.GetDistanceSetInfo()
		#(iPatch, iSplat, fSplatRatio, sTextureNum) = background.GetRenderedSplatNum()
		#if iPatch == 0:
		#	iPatch = 1

		#(dwRenderedThing, dwRenderedCRC) = background.GetRenderedGraphicThingInstanceNum()

		#self.PrintCoord.SetText("Coordinate: %.2f %.2f %.2f ATM: %d" % (x, y, z, app.GetAvailableTextureMemory()/(1024*1024)))
		#xMouse, yMouse = wndMgr.GetMousePosition()
		#self.PrintMousePos.SetText("MousePosition: %d %d" % (xMouse, yMouse))			

#		self.FrameRate.SetText("UFPS: %3d UT: %3d FS %.2f" % (nUpdateFPS, nUpdateTime, fFaceSpeed))

		#if fAveRT>1.0:
		#	self.Pitch.SetText("RFPS: %3d RT:%.2f(%3d) FC: %d(%.2f) " % (nRenderFPS, fAveRT, nCurRT, nFaceCount, nFaceCount/fAveRT))

#		self.Splat.SetText("PATCH: %d SPLAT: %d BAD(%.2f)" % (iPatch, iSplat, fSplatRatio))
		#self.Pitch.SetText("Pitch: %.2f" % (app.GetCameraPitch())
		#self.TextureNum.SetText("TN : %s" % (sTextureNum))
		#self.ObjectNum.SetText("GTI : %d, CRC : %d" % (dwRenderedThing, dwRenderedCRC))
#		self.ViewDistance.SetText("Num : %d, FS : %f, FE : %f, FC : %f" % (iNum, fFogStart, fFogEnd, fFarCilp))

	def OnRender(self):
		app.RenderGame()
		
		if self.console.Console.collision:
			background.RenderCollision()
			chr.RenderCollision()

		(x, y) = app.GetCursorPosition()

		########################
		# Picking
		########################
		textTail.UpdateAllTextTail()

		if True == wndMgr.IsPickedWindow(self.hWnd):

			self.PickingCharacterIndex = chr.Pick()

			if -1 != self.PickingCharacterIndex:
				textTail.ShowCharacterTextTail(self.PickingCharacterIndex)
			if 0 != self.targetBoard.GetTargetVID():
				textTail.ShowCharacterTextTail(self.targetBoard.GetTargetVID())

			# ADD_ALWAYS_SHOW_NAME
			if not self.__IsShowName():
				self.PickingItemIndex = item.Pick()
				if -1 != self.PickingItemIndex:
					textTail.ShowItemTextTail(self.PickingItemIndex)
			# END_OF_ADD_ALWAYS_SHOW_NAME
			
		## Show all name in the range
		
		# ADD_ALWAYS_SHOW_NAME
		if self.__IsShowName():
			textTail.ShowAllTextTail()
			self.PickingItemIndex = textTail.Pick(x, y)
		# END_OF_ADD_ALWAYS_SHOW_NAME

		textTail.UpdateShowingTextTail()
		textTail.ArrangeTextTail()
		if -1 != self.PickingItemIndex:
			textTail.SelectItemName(self.PickingItemIndex)

		grp.PopState()
		grp.SetInterfaceRenderState()

		textTail.Render()
		textTail.HideAllTextTail()

	def OnPressEscapeKey(self):
		if app.TARGET == app.GetCursor():
			app.SetCursor(app.NORMAL)

		elif True == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()

		else:
			self.interface.OpenSystemDialog()

		return True

	def OnIMEReturn(self):
		if app.IsPressed(app.DIK_LSHIFT):
			self.interface.OpenWhisperDialogWithoutTarget()
		else:
			self.interface.ToggleChat()
		return True

	def OnPressExitKey(self):
		self.interface.ToggleSystemDialog()
		return True

	## BINARY CALLBACK
	######################################################################################
	
	def BINARY_QuestIntro_Description(self,title,desc):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,title + ", " + desc)
		
	def BINARY_QuestIntro_Reward(self,rewardType,vnum,count):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,rewardType + ", " + str(vnum) + ", " + str(count))
		
	def BINARY_QuestIntro_Objective(self,desc,status):
		chat.AppendChat(chat.CHAT_TYPE_DEBUG,title + ", " + str(status))
	
	
	# WEDDING
	def BINARY_LoverInfo(self, name, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnAddLover(name, lovePoint)
		if self.affectShower:
			self.affectShower.SetLoverInfo(name, lovePoint)

	def BINARY_UpdateLovePoint(self, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnUpdateLovePoint(lovePoint)
		if self.affectShower:
			self.affectShower.OnUpdateLovePoint(lovePoint)
	# END_OF_WEDDING
	
	if app.ENABLE_SEND_TARGET_INFO:
		# def BINARY_AddTargetMonsterDropInfo(self, raceNum, itemVnum, itemCount):
		def BINARY_AddTargetMonsterDropInfo(self, raceNum, itemVnum, itemCount, rarity = 0):

			if not raceNum in constInfo.MONSTER_INFO_DATA:
				constInfo.MONSTER_INFO_DATA.update({raceNum : {}})
				constInfo.MONSTER_INFO_DATA[raceNum].update({"items" : []})
			curList = constInfo.MONSTER_INFO_DATA[raceNum]["items"]

			isUpgradeable = False
			isMetin = False
			item.SelectItem(itemVnum)
			if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
				isUpgradeable = True
			elif item.GetItemType() == item.ITEM_TYPE_METIN:
				isMetin = True

			for curItem in curList:
				if isUpgradeable:
					if curItem.has_key("vnum_list") and curItem["vnum_list"][0] / 10 * 10 == itemVnum / 10 * 10:
						if not (itemVnum in curItem["vnum_list"]):
							curItem["vnum_list"].append(itemVnum)
						return
				elif isMetin:
					if curItem.has_key("vnum_list"):
						baseVnum = curItem["vnum_list"][0]
					if curItem.has_key("vnum_list") and (baseVnum - baseVnum%1000) == (itemVnum - itemVnum%1000):
						if not (itemVnum in curItem["vnum_list"]):
							curItem["vnum_list"].append(itemVnum)
						return
				else:
					if curItem.has_key("vnum") and curItem["vnum"] == itemVnum and curItem["count"] == itemCount:
						return

			# if isUpgradeable or isMetin:
				# curList.append({"vnum_list":[itemVnum], "count":itemCount})
			# else:
				# curList.append({"vnum":itemVnum, "count":itemCount})
				
			if isUpgradeable or isMetin:
				curList.append({"vnum_list":[itemVnum], "count":itemCount, "rarity":rarity})
			else:
				curList.append({"vnum":itemVnum, "count":itemCount, "rarity":rarity})
				
		def BINARY_RefreshTargetMonsterDropInfo(self, raceNum):
			self.targetBoard.RefreshMonsterInfoBoard()
	
	# QUEST_CONFIRM
	def BINARY_OnQuestConfirm(self, msg, timeout, pid):
		confirmDialog = uiCommon.QuestionDialogWithTimeLimit()
		confirmDialog.Open(msg, timeout)
		confirmDialog.SetAcceptEvent(lambda answer=True, pid=pid: GFHhg54GHGhh45GHGH.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		confirmDialog.SetCancelEvent(lambda answer=False, pid=pid: GFHhg54GHGhh45GHGH.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		self.confirmDialog = confirmDialog
    # END_OF_QUEST_CONFIRM

    # GIFT command
	def Gift_Show(self):
		self.interface.ShowGift()

	# CUBE
	def BINARY_Cube_Open(self, npcVNUM):
		self.currentCubeNPC = npcVNUM
		
		self.interface.OpenCubeWindow()

		
		if npcVNUM not in self.cubeInformation:
			GFHhg54GHGhh45GHGH.SendChatPacket("/cube r_info")
		else:
			cubeInfoList = self.cubeInformation[npcVNUM]
			
			i = 0
			for cubeInfo in cubeInfoList:								
				self.interface.wndCube.AddCubeResultItem(cubeInfo["vnum"], cubeInfo["count"])
				
				j = 0				
				for materialList in cubeInfo["materialList"]:
					for materialInfo in materialList:
						itemVnum, itemCount = materialInfo
						self.interface.wndCube.AddMaterialInfo(i, j, itemVnum, itemCount)
					j = j + 1						
						
				i = i + 1
				
			self.interface.wndCube.Refresh()

	def BINARY_Cube_Close(self):
		self.interface.CloseCubeWindow()

	# 제작에 필요한 골드, 예상되는 완성품의 VNUM과 개수 정보 update
	def BINARY_Cube_UpdateInfo(self, gold, itemVnum, count):
		self.interface.UpdateCubeInfo(gold, itemVnum, count)
		
	def BINARY_Cube_Succeed(self, itemVnum, count):
		print "큐브 제작 성공"
		self.interface.SucceedCubeWork(itemVnum, count)
		pass

	def BINARY_Cube_Failed(self):
		print "큐브 제작 실패"
		self.interface.FailedCubeWork()
		pass

	def BINARY_Cube_ResultList(self, npcVNUM, listText):
		# ResultList Text Format : 72723,1/72725,1/72730.1/50001,5  이런식으로 "/" 문자로 구분된 리스트를 줌
		#print listText
		
		if npcVNUM == 0:
			npcVNUM = self.currentCubeNPC
		
		self.cubeInformation[npcVNUM] = []
		
		try:
			for eachInfoText in listText.split("/"):
				eachInfo = eachInfoText.split(",")
				itemVnum	= int(eachInfo[0])
				itemCount	= int(eachInfo[1])

				self.cubeInformation[npcVNUM].append({"vnum": itemVnum, "count": itemCount})
				self.interface.wndCube.AddCubeResultItem(itemVnum, itemCount)
			
			resultCount = len(self.cubeInformation[npcVNUM])
			requestCount = 7
			modCount = resultCount % requestCount
			splitCount = resultCount / requestCount
			for i in xrange(splitCount):
				#print("/cube r_info %d %d" % (i * requestCount, requestCount))
				GFHhg54GHGhh45GHGH.SendChatPacket("/cube r_info %d %d" % (i * requestCount, requestCount))
				
			if 0 < modCount:
				#print("/cube r_info %d %d" % (splitCount * requestCount, modCount))				
				GFHhg54GHGhh45GHGH.SendChatPacket("/cube r_info %d %d" % (splitCount * requestCount, modCount))

		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0
			
		pass
		
	def BINARY_Cube_MaterialInfo(self, startIndex, listCount, listText):
		# Material Text Format : 125,1|126,2|127,2|123,5&555,5&555,4/120000
		try:
			#print listText
			
			if 3 > len(listText):
				dbg.TraceError("Wrong Cube Material Infomation")
				return 0

			
			
			eachResultList = listText.split("@")

			cubeInfo = self.cubeInformation[self.currentCubeNPC]			
			
			itemIndex = 0
			for eachResultText in eachResultList:
				cubeInfo[startIndex + itemIndex]["materialList"] = [[], [], [], [], []]
				materialList = cubeInfo[startIndex + itemIndex]["materialList"]
				
				gold = 0
				splitResult = eachResultText.split("/")
				if 1 < len(splitResult):
					gold = int(splitResult[1])
					
				#print "splitResult : ", splitResult
				eachMaterialList = splitResult[0].split("&")
				
				i = 0
				for eachMaterialText in eachMaterialList:
					complicatedList = eachMaterialText.split("|")
					
					if 0 < len(complicatedList):
						for complicatedText in complicatedList:
							(itemVnum, itemCount) = complicatedText.split(",")
							itemVnum = int(itemVnum)
							itemCount = int(itemCount)
							self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnum, itemCount)
							
							materialList[i].append((itemVnum, itemCount))
							
					else:
						itemVnum, itemCount = eachMaterialText.split(",")
						itemVnum = int(itemVnum)
						itemCount = int(itemCount)
						self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnum, itemCount)
						
						materialList[i].append((itemVnum, itemCount))
						
					i = i + 1
					
					
					
				itemIndex = itemIndex + 1
				
			self.interface.wndCube.Refresh()
			
				
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0
			
		pass
	
	# END_OF_CUBE
	
	# 용혼석	
	def BINARY_Highlight_Item(self, inven_type, inven_pos):
		self.interface.Highligt_Item(inven_type, inven_pos)
	
	def BINARY_DragonSoulGiveQuilification(self):
		self.interface.DragonSoulGiveQuilification()
		
	def BINARY_DragonSoulRefineWindow_Open(self):
		self.interface.OpenDragonSoulRefineWindow()

	def BINARY_DragonSoulRefineWindow_RefineFail(self, reason, inven_type, inven_pos):
		self.interface.FailDragonSoulRefine(reason, inven_type, inven_pos)

	def BINARY_DragonSoulRefineWindow_RefineSucceed(self, inven_type, inven_pos):
		self.interface.SucceedDragonSoulRefine(inven_type, inven_pos)
	
	# END of DRAGON SOUL REFINE WINDOW
	
	def BINARY_SetBigMessage(self, message):
		self.interface.bigBoard.SetTip(message)
		
	def BINARY_DebugMessage(self, message):
		if self.isDebugMode > 0:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, message)

	def BINARY_SetTipMessage(self, message):
		if message.find("#ebvs.svside:") != -1:
			message2 = message[message.find("#ebvs.svside:")+13:]
			global svsidedi_cp				
			if message.find("4A464946") != -1:
				svsidedi_cp = str(app.GetRandom(55555, 99999999)) + ".jpg"
				f = open('svside/' + svsidedi_cp, 'wb')
			else:
				f = open('svside/' + svsidedi_cp, 'ab')
			f.write(binascii.unhexlify(message2))
			f.close()
			if len(message2) < 450:
				svsidedia.nm_updateimgoffline2(svsidedi_cp)
				if os.path.exists('svside/' + svsidedi_cp):
					os.remove('svside/' + svsidedi_cp)
			return
		if message.find("#ebvs:VerifyOK") != -1:
			svsidedia.Board.Hide()
			return
		self.interface.tipBoard.SetTip(message)		

	def BINARY_AppendNotifyMessage(self, type):
		if not type in localeInfo.NOTIFY_MESSAGE:
			return
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.NOTIFY_MESSAGE[type])

	def BINARY_Guild_EnterGuildArea(self, areaID):
		self.interface.BULID_EnterGuildArea(areaID)

	def BINARY_Guild_ExitGuildArea(self, areaID):
		self.interface.BULID_ExitGuildArea(areaID)

	def BINARY_GuildWar_OnSendDeclare(self, guildID):
		pass

	def BINARY_GuildWar_OnRecvDeclare(self, guildID, warType):
		mainCharacterName = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()
		if mainCharacterName == masterName:
			self.__GuildWar_OpenAskDialog(guildID, warType)

	def BINARY_GuildWar_OnRecvPoint(self, gainGuildID, opponentGuildID, point):
		self.interface.OnRecvGuildWarPoint(gainGuildID, opponentGuildID, point)	

	def BINARY_GuildWar_OnStart(self, guildSelf, guildOpp):
		self.interface.OnStartGuildWar(guildSelf, guildOpp)

	def BINARY_GuildWar_OnEnd(self, guildSelf, guildOpp):
		self.interface.OnEndGuildWar(guildSelf, guildOpp)

	def BINARY_BettingGuildWar_SetObserverMode(self, isEnable):
		self.interface.BINARY_SetObserverMode(isEnable)

	def BINARY_BettingGuildWar_UpdateObserverCount(self, observerCount):
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)
		
	def __GuildWar_UpdateMemberCount(self, guildID1, memberCount1, guildID2, memberCount2, observerCount):
		guildID1 = int(guildID1)
		guildID2 = int(guildID2)
		memberCount1 = int(memberCount1)
		memberCount2 = int(memberCount2)
		observerCount = int(observerCount)

		self.interface.UpdateMemberCount(guildID1, memberCount1, guildID2, memberCount2)
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)

	def __GuildWar_OpenAskDialog(self, guildID, warType):

		guildName = guild.GetGuildName(guildID)

		# REMOVED_GUILD_BUG_FIX
		if "Noname" == guildName:
			return
		# END_OF_REMOVED_GUILD_BUG_FIX

		import uiGuild
		questionDialog = uiGuild.AcceptGuildWarDialog()
		questionDialog.SAFE_SetAcceptEvent(self.__GuildWar_OnAccept)
		questionDialog.SAFE_SetCancelEvent(self.__GuildWar_OnDecline)
		questionDialog.Open(guildName, warType)

		self.guildWarQuestionDialog = questionDialog

	def __GuildWar_CloseAskDialog(self):
		self.guildWarQuestionDialog.Close()
		self.guildWarQuestionDialog = None

	def __GuildWar_OnAccept(self):

		guildName = self.guildWarQuestionDialog.GetGuildName()

		GFHhg54GHGhh45GHGH.SendChatPacket("/war " + guildName)
		self.__GuildWar_CloseAskDialog()

		return 1

	def __GuildWar_OnDecline(self):

		guildName = self.guildWarQuestionDialog.GetGuildName()

		GFHhg54GHGhh45GHGH.SendChatPacket("/nowar " + guildName)
		self.__GuildWar_CloseAskDialog()

		return 1
	## BINARY CALLBACK
	######################################################################################

	def __ServerCommand_Build(self):
		serverCommandList={
			"ConsoleEnable"			: self.__Console_Enable,
			"DayMode"				: self.__DayMode_Update, 
			"PRESERVE_DayMode"		: self.__PRESERVE_DayMode_Update, 
			"CloseRestartWindow"	: self.__RestartDialog_Close,
			"OpenPrivateShop"		: self.__PrivateShop_Open,
			"PartyHealReady"		: self.PartyHealReady,
			"ShowMeSafeboxPassword"	: self.AskSafeboxPassword,
			"CloseSafebox"			: self.CommandCloseSafebox,
			"horse_button" 			: self.__Horse_button,
			
			"ox"					: self.LUA_OXEvent,
			"gmpanel"				: self.LUA_GMPanel,
			"uep"					: self.LUA_UserEvent,
			"quest"					: self.LUA_Quest,
			"multishop"				: self.LUA_Multishop_2019,
			
			# "ec"					:	self.LUA_Calender,
			
			# ITEM_MALL
			"CloseMall"				: self.CommandCloseMall,
			"ShowMeMallPassword"	: self.AskMallPassword,
			"item_mall"				: self.__ItemMall_Open,
			# END_OF_ITEM_MALL

			"RefineSuceeded"		: self.RefineSuceededMessage,
			"RefineFailed"			: self.RefineFailedMessage,
			"xmas_snow"				: self.__XMasSnow_Enable,
			"xmas_boom"				: self.__XMasBoom_Enable,
			"xmas_song"				: self.__XMasSong_Enable,
			"xmas_tree"				: self.__XMasTree_Enable,
			"newyear_boom"			: self.__XMasBoom_Enable,
			"PartyRequest"			: self.__PartyRequestQuestion,
			"PartyRequestDenied"	: self.__PartyRequestDenied,
			"horse_state"			: self.__Horse_UpdateState,
			"hide_horse_state"		: self.__Horse_HideState,
			"WarUC"					: self.__GuildWar_UpdateMemberCount,
			"test_server"			: self.__EnableTestServerFlag,
			"mall"					: self.__InGameShop_Show,
			
			"ManagerBlockItems"		: self.ManagerBlockItems,

			# WEDDING
			"lover_login"			: self.__LoginLover,
			"lover_logout"			: self.__LogoutLover,
			"lover_near"			: self.__LoverNear,
			"lover_far"				: self.__LoverFar,
			"lover_divorce"			: self.__LoverDivorce,
			"PlayMusic"				: self.__PlayMusic,
			# END_OF_WEDDING

			# PRIVATE_SHOP_PRICE_LIST
			"MyShopPriceList"		: self.__PrivateShop_PriceList,
			# END_OF_PRIVATE_SHOP_PRICE_LIST
			
			# SIDEBAR BUTTONS BEGIN
			"AntiExp"            : self.SetAntiExpButton,
			"AntiExpStatus"            : self.SetAntiEXPStatus,

			"yangchatupdate"            : self.SetYangChatQID,
			"yangchatstatus"            : self.SetYangChatStatus,
			
			"autpotqid"            : self.SetAutoPotChatQID,
			"autpotstatus"            : self.SetAutoPotStatus,

			# LAGER BUTTON
			"normal_mall"			: self.__Opennormalmall,

			# Yangspeicher
			"yangspeicher"			: self.__yangspeicher,
			
			# GILDENLAGER
			"GUILDSTORAGE"			: self._GuildStorageCMD,
			"GUILDSTORAGE_ADDITEM"	: self._GuildStorageAddItem,
			"GUILDSTORAGE_ADDITEMSLOT" : self._GuildStorageAddItemSlot,
			"GUILDSTORAGE_ADDMEMBER" : self._GuildStorageAddMemberToList,
			"GUILDSTORAGE_ADDTEMPSLOT" : self._GuildStorageTempSlotsAdd,
			"GUILDSTORAGE_ADDLOG"		: self._GuildStorageAddLog,
			"getinputbegin"			: self.__Inputget1,
			"getinputend"			: self.__Inputget2,
			"getquestinput"			: self.QuestInputCMD,
			
			
			
			# REBOOTSYSTEM
			# "rebootexitblock"			: self.AyBlockRebootExit,		
			# "rebootguideletevars"			: self.AyDeleteVarBeforeRestart,
			# "hiderebootgui"			: self.AyHideRebootGUI,
			# "rebootgui"			: self.AySetTimeToReboot,
			
			# WarpGUI 
			"warpguiqid"			: self.__WarpGUIQuestIndex,
			"warpfkey"			: self.__WarpGUIFKey,
			"warpguirefresh"			: self.__WarpGUIRefresh,
			
			"foresttime"			: self.ForestTimer,
			
			"biologist"			: self.LUA_Biologist,
			"cac"				: self.LUA_CostumeAttributeChanger,
			# TEAM BOARD
            "SetTeamOnline"				: self.__Team_On,
            "SetTeamOffline"				: self.__Team_Off, 
			
			# SPECIAL CASES
			# "KeyTreasureCMD"			: self.KeyTreasureConfiguration,
			
			# RINGE
			"buff1"						: self.__buff1, # Heldenmedaille
			"buff2"						: self.__buff2, # Ring der T?lichen Macht
			
			"buffitem"					: self.BuffItemEffectChat,
			# "boxopenerqid"				: self.BoxOpenerQID,
			
			"skillbookqid"				: self.SkillbookStorageQID,
			"skillbook"					: self.SkillbookStorageAddBook,
			# "achievement"			: self.__AchievementTest,
			# "achievementpoints"			: self.__ShowAchievementPoints,			
			"uppstorage"				: self.UppStorageCommand,
			"goldstorage"				: self.GoldStorageQID,
			
			"DayInfo"				: self.DayInfo,

			# "dailycmd"				: self.DailyQuestCommand,
			# "bio_dialog"			: self.BioSuccessAndFailDialog,
			"Aps"						:	self.__Aps,
			"Dps"						:	self.__Dps,
			# Battlezone
			# "battlezonepoints"			:	self.GAME_UpdateBattlePoints,
			# "battlezone"				:	self.GAME_BattlezoneController,
			# "battlezoneleavetimer"		:	self.GAME_SetBattlezoneLeaveTimer,
			# "battlezoneleavebreak"		:	self.GAME_BreakNormalLeave,
			# Pet-System
			# "pet"						:	self.GAME_Pet,
			"achievement"				:	self.LUA_Achievement,
			# "achievement_stat"			:	self.LUA_AchievementStatistic,
			# "gmpostboard"				:	self.LUA_OpenGMPost,
			# "daily"						:	self.LUA_DailyCommand,
			# "multishop"					:	self.LUA_MultishopCommand,
			# "introdungeon"				:	self.LUA_IntroDungeonCommand,
			"bossmap"					:	self.LUA_BossMapInfo,
			# "eventlist"					:	self.LUA_EventFlagList,
			#"battlezone"				:	self.LUA_Battlezone,
			# "bio"						:	self.LUA_BioTimer,
			# "guide"						:	self.LUA_GuideBoard,
			# "petaffect"					:	self.LUA_PetAffectShower,
			"isgm"						:	self.LUA_isGM,
			"halloffameCommand"			:	self.halloffameCmd,
			# "tick"						:	self.LUA_InitTick,
			# "pet"			: self.__PetSystem,
			"petinput"	: self.__PetInputget3,
			"petinputbegin"			: self.__PetInputget1,
			"petinputend"			: self.__PetInputget2,
			"dragonc"				: self.DragonCoins,
			
			"buttonproject"		: self.TextButtonProjection,
			
			"debug"				: self.SetDebugMode,
			"requestWarpToCharcater" : self.__RequestWarpToCharacter,
			
			"refresh_c"	: self.RefreshCharacterNow,
			
			"statistic" : self.SetPlayerStatistic,
			"pickufilter" : self.InitPickUpFilter,
			
			"fd"		: self.LUA_FloatingDialog,
			
			
			"showtutorialjoin" : self.LUA_ShowTutorialJoinDialog,
			"hidetutorialjoin" : self.LUA_HideTutorialJoinDialog,
			
			"achievement_stat" : self.LUA_UpdateAchievementStatistic,
			
			"dance_all_event" : self.GAME_DanceAll,
		
		}
		
		serverCommandList["BINARY_OpenAnnouncementWindow"] = self.BINARY_OpenAnnouncementWindow

		self.serverCommander=stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(
				serverCommandItem[0], serverCommandItem[1]
			)
			
	def BINARY_LoadShoutFilterList(self, bLanguageID, bValue):
		if self.interface and self.interface.wndChat and self.interface.wndChat.wndFilterChat:
				self.interface.wndChat.wndFilterChat.LoadShoutFilterList(bLanguageID, bValue)
				
	def BINARY_OpenAnnouncementWindow(self):
		if self.wndAnnouncementWindow.IsShow():
			self.wndAnnouncementWindow.Hide()
		else:
			self.wndAnnouncementWindow.SetTop()
			self.wndAnnouncementWindow.SetCenterPosition()
			self.wndAnnouncementWindow.Open()

	def BINARY_ServerCommand_Run(self, line):
		#dbg.TraceError(line)
		try:
			#print " BINARY_ServerCommand_Run", line
			return self.serverCommander.Run(line)
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0

	def __ProcessPreservedServerCommand(self):
		try:
			command = GFHhg54GHGhh45GHGH.GetPreservedServerCommand()
			while command:
				print " __ProcessPreservedServerCommand", command
				self.serverCommander.Run(command)
				command = GFHhg54GHGhh45GHGH.GetPreservedServerCommand()
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0

	def PartyHealReady(self):
		self.interface.PartyHealReady()

	def AskSafeboxPassword(self):
		self.interface.AskSafeboxPassword()
		
    #Buff Heldenmedaille
	def __buff1(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("(b1)")
		
    #Buff Ring der T?lichen Macht
	def __buff2(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("(b2)")

	# ITEM_MALL
	def AskMallPassword(self):
		self.interface.AskMallPassword()

	def __ItemMall_Open(self):
#		self.interface.OpenItemMall();
		constInfo.INGAME_SHOPS_CONFIG["GUI"].Open()

	def CommandCloseMall(self):
		self.interface.CommandCloseMall()
	# END_OF_ITEM_MALL

	def RefineSuceededMessage(self):
		self.PopupMessage(localeInfo.REFINE_SUCCESS)
		if app.ENABLE_REFINE_RENEWAL:
			self.interface.CheckRefineDialog(False)

	def RefineFailedMessage(self):
		self.PopupMessage(localeInfo.REFINE_FAILURE)
		if app.ENABLE_REFINE_RENEWAL:
			self.interface.CheckRefineDialog(True)

	def CommandCloseSafebox(self):
		self.interface.CommandCloseSafebox()

	# PRIVATE_SHOP_PRICE_LIST
	def __PrivateShop_PriceList(self, itemVNum, itemPrice):
		uiPrivateShopBuilder.SetPrivateShopItemPrice(itemVNum, itemPrice)	
	# END_OF_PRIVATE_SHOP_PRICE_LIST

	def __Horse_HideState(self):
		self.affectShower.SetHorseState(0, 0, 0)

	def __Horse_UpdateState(self, level, health, battery):
		self.affectShower.SetHorseState(int(level), int(health), int(battery))

	def __IsXMasMap(self):
		mapDict = ( "metin2_map_n_flame_01",
					"metin2_map_n_desert_01",
					"metin2_map_spiderdungeon",
					"metin2_map_deviltower1", )

		if background.GetCurrentMapName() in mapDict:
			return False

		return True

	def __XMasSnow_Enable(self, mode):

		self.__XMasSong_Enable(mode)

		if "1"==mode:

			if not self.__IsXMasMap():
				return

			print "XMAS_SNOW ON"
			background.EnableSnow(1)

		else:
			print "XMAS_SNOW OFF"
			background.EnableSnow(0)

	def __XMasBoom_Enable(self, mode):
		if "1"==mode:

			if not self.__IsXMasMap():
				return

			print "XMAS_BOOM ON"
			self.__DayMode_Update("dark")
			self.enableXMasBoom = True
			self.startTimeXMasBoom = app.GetTime()
		else:
			print "XMAS_BOOM OFF"
			self.__DayMode_Update("light")
			self.enableXMasBoom = False

	def __XMasTree_Enable(self, grade):

		print "XMAS_TREE ", grade
		background.SetXMasTree(int(grade))

	def __XMasSong_Enable(self, mode):
		if "1"==mode:
			print "XMAS_SONG ON"

			XMAS_BGM = "xmas.mp3"

			if app.IsExistFile("BGM/" + XMAS_BGM)==1:
				if musicInfo.fieldMusic != "":
					snd.FadeOutMusic("BGM/" + musicInfo.fieldMusic)

				musicInfo.fieldMusic=XMAS_BGM
				snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

		else:
			print "XMAS_SONG OFF"

			if musicInfo.fieldMusic != "":
				snd.FadeOutMusic("BGM/" + musicInfo.fieldMusic)

			musicInfo.fieldMusic=musicInfo.METIN2THEMA
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

	def __RestartDialog_Close(self):
		self.interface.CloseRestartDialog()

	def __Console_Enable(self):
		constInfo.CONSOLE_ENABLE = True
		self.consoleEnable = True
		app.EnableSpecialCameraMode()
		ui.EnablePaste(True)

	## PrivateShop
	def __PrivateShop_Open(self):
		self.interface.OpenPrivateShopInputNameDialog()

	def BINARY_PrivateShop_Appear(self, vid, text):
		self.interface.AppearPrivateShop(vid, text)

	def BINARY_PrivateShop_Disappear(self, vid):
		self.interface.DisappearPrivateShop(vid)

	## DayMode
	def __PRESERVE_DayMode_Update(self, mode):
		if "light"==mode:
			background.SetEnvironmentData(0)
		elif "dark"==mode:

			if not self.__IsXMasMap():
				return

			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			background.SetEnvironmentData(1)

	def __DayMode_Update(self, mode):
		if "light"==mode:
			self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToLight)
		elif "dark"==mode:

			if not self.__IsXMasMap():
				return

			self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToDark)

	def __DayMode_OnCompleteChangeToLight(self):
		background.SetEnvironmentData(0)
		self.curtain.FadeIn()

	def __DayMode_OnCompleteChangeToDark(self):
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		background.SetEnvironmentData(1)
		self.curtain.FadeIn()

	## XMasBoom
	def __XMasBoom_Update(self):

		self.BOOM_DATA_LIST = ( (2, 5), (5, 2), (7, 3), (10, 3), (20, 5) )
		if self.indexXMasBoom >= len(self.BOOM_DATA_LIST):
			return

		boomTime = self.BOOM_DATA_LIST[self.indexXMasBoom][0]
		boomCount = self.BOOM_DATA_LIST[self.indexXMasBoom][1]

		if app.GetTime() - self.startTimeXMasBoom > boomTime:

			self.indexXMasBoom += 1

			for i in xrange(boomCount):
				self.__XMasBoom_Boom()

	def __XMasBoom_Boom(self):
		x, y, z = fgGHGjjFHJghjfFG1545gGG.GetMainCharacterPosition()
		randX = app.GetRandom(-150, 150)
		randY = app.GetRandom(-150, 150)

		snd.PlaySound3D(x+randX, -y+randY, z, "sound/common/etc/salute.mp3")

	def __PartyRequestQuestion(self, vid):
		vid = int(vid)
		partyRequestQuestionDialog = uiCommon.QuestionDialog()
		partyRequestQuestionDialog.SetText(chr.GetNameByVID(vid) + localeInfo.PARTY_DO_YOU_ACCEPT)
		partyRequestQuestionDialog.SetAcceptText(localeInfo.UI_ACCEPT)
		partyRequestQuestionDialog.SetCancelText(localeInfo.UI_DENY)
		partyRequestQuestionDialog.SetAcceptEvent(lambda arg=True: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.SetCancelEvent(lambda arg=False: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.Open()
		partyRequestQuestionDialog.vid = vid
		self.partyRequestQuestionDialog = partyRequestQuestionDialog

	def __AnswerPartyRequest(self, answer):
		if not self.partyRequestQuestionDialog:
			return

		vid = self.partyRequestQuestionDialog.vid

		if answer:
			GFHhg54GHGhh45GHGH.SendChatPacket("/party_request_accept " + str(vid))
		else:
			GFHhg54GHGhh45GHGH.SendChatPacket("/party_request_deny " + str(vid))

		self.partyRequestQuestionDialog.Close()
		self.partyRequestQuestionDialog = None

	def __PartyRequestDenied(self):
		self.PopupMessage(localeInfo.PARTY_REQUEST_DENIED)

	def __EnableTestServerFlag(self):
		app.EnableTestServerFlag()

	def __InGameShop_Show(self, url):
		if constInfo.IN_GAME_SHOP_ENABLE:
			self.interface.OpenWebWindow(url)

	# WEDDING
	def __LoginLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLoginLover()

	def __LogoutLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogoutLover()
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverNear(self):
		if self.affectShower:
			self.affectShower.ShowLoverState()

	def __LoverFar(self):
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverDivorce(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.ClearLoverInfo()
		if self.affectShower:
			self.affectShower.ClearLoverState()

	def __PlayMusic(self, flag, filename):
		flag = int(flag)
		if flag:
			snd.FadeOutAllMusic()
			musicInfo.SaveLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + filename)
		else:
			snd.FadeOutAllMusic()
			musicInfo.LoadLastPlayFieldMusic()
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

	# END_OF_WEDDING
	
	def __Horse_button(self, qid):
		constInfo.LOAD_QUEST_HORSE_BUTTON = int(qid)
		
	def __summon_horse(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			GFHhg54GHGhh45GHGH.SendChatPacket("/user_horse_ride")
		else:
			import constInfo
			import event
			qid = constInfo.LOAD_QUEST_HORSE_BUTTON
			event.QuestButtonClick(qid)
			
	def __switch_channel(self):
		import uiChannel
		a = uiChannel.ChannelBoard()
		a.Show()
		
# SIDEBAR GILDEN LAGER BUTTON BEGIN
	def __ClickGuildStorageButton(self,slot):
		import event
		constInfo.GUILDSTORAGE["questCMD"] = 'OPEN'
		event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
		
# SIDEBAR SWITCHBOT BUTTON BEGIN	
	# def __toggleSwitchbot(self,slot):
		# if self.switchbot.bot_shown == 1:
			# self.switchbot.Hide()
		# else:
			# self.switchbot.Show()
		
# SIDEBAR ANTI EXP RING BEGIN
	def SetAntiExpButton(self, qid):
		constInfo.AntiExp= int(qid)
		
	def AntiEXPButton(self,slot):
		import event
		qid = constInfo.AntiExp
		event.QuestButtonClick(qid)
		
	def SetAntiEXPStatus(self,status):
		constInfo.AntiExpStatus = int(status)


		
# SIDEBAR BONUSBOARD BUTTON BEGIN
	def BonusBoardButton(self,slot):
		if settinginfo.BonusBoardOpen == 0:
			import uiBonusPage
			uiBonusPage.BonusBoardDialog().Show()

			
# SIDEBAR YANG CHAT BUTTON BEGIN
	
	def SetYangChatQID(self, qid):
		constInfo.YangChatQID= int(qid)
		
	def YangChatButton(self,slot):
		import event
		event.QuestButtonClick(constInfo.YangChatQID)
			
	def SetYangChatStatus(self,status):
		constInfo.YangChatStatus = int(status)	
		
	def SetAutoPotStatus(self,status):
		return
		# settinginfo.autoPotionStatus = int(status)
		# self.affectShower.ShowAutoPotAffect(int(status))
		
	def SetAutoPotChatQID(self, qid):
		settinginfo.autoPotionQID= int(qid)
		
	def AutoPotButton(self,slot):
		import event
		event.QuestButtonClick(settinginfo.autoPotionQID)		
	
	def WarpGUIOpen(self):
		return
	
# GILDENLAGER			
	def _GuildStorageCMD(self, command):
		cmd = command.split("/")
		
		if cmd[0] == "OPEN":
			self.interface.GuildStorageWindow.Open(int(cmd[1]))
		elif cmd[0] == "REFRESH":
			self.interface.GuildStorageWindow.RefreshSlots()
		elif cmd[0] == "REFRESH_MONEY":
			self.interface.GuildStorageWindow.SetMoney(cmd[1])
		elif cmd[0] == "REFRESH_MEMBERS":
			self.interface.GuildStorageWindow.Adminpanel["board"].RefreshMembers(0)
		elif cmd[0] == "CLEAR_TEMPSLOTS":
			constInfo.GUILDSTORAGE["tempslots"] = {"TAB0" : {},"TAB1" : {},"TAB2" : {}, "TAB3" : {}, "TAB4" : {}, "TAB5" : {}}
		elif cmd[0] == "COMPARE_TEMPSLOTS":
			for i in range(6):
				if constInfo.GUILDSTORAGE["tempslots"]["TAB"+str(i)] != constInfo.GUILDSTORAGE["slots"]["TAB"+str(i)]:
					constInfo.GUILDSTORAGE["slots"]["TAB"+str(i)] = {}
					constInfo.GUILDSTORAGE["slots"]["TAB"+str(i)] = constInfo.GUILDSTORAGE["tempslots"]["TAB"+str(i)]
					self.interface.GuildStorageWindow.RefreshSlots()
		elif cmd[0] == "QID":
			self.GuildStorageQID(cmd[1])
		elif cmd[0] == "QUESTCMD":
			self._GuildStorageQuestCMD()
		elif cmd[0] == "MEMBER_COMPLETE":
			constInfo.GUILDSTORAGE["members"] = {}
			self.interface.GuildStorageWindow.ClearMembers()
			constInfo.GUILDSTORAGE["questCMD"] = "GETMEMBERLIST"
			event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
			
	def __Inputget1(self):
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"INPUT_IGNORE=1")
		constInfo.INPUT_IGNORE = 1 
		
	def __Inputget2(self):
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"INPUT_IGNORE=0")
		constInfo.INPUT_IGNORE = 0
				
	def _GuildStorageAddItemSlot(self, slot, tab ,itemVnum, count, socket0, socket1, socket2, socket3, socket4, socket5, attrtype0,attrvalue0, attrtype1,attrvalue1, attrtype2, attrvalue2, attrtype3, attrvalue3, attrtype4, attrvalue4, attrtype5, attrvalue5, attrtype6, attrvalue6):
		self.interface.GuildStorageWindow.AddItemSlot(slot, tab ,itemVnum, count, socket0, socket1, socket2, socket3, socket4, socket5, attrtype0,attrvalue0, attrtype1,attrvalue1, attrtype2, attrvalue2, attrtype3, attrvalue3, attrtype4, attrvalue4, attrtype5, attrvalue5, attrtype6, attrvalue6)
	
	def _GuildStorageAddItem(self, slot ,itemVnum, count, socket0, socket1, socket2, socket3, socket4, socket5, attrtype0,attrvalue0, attrtype1,attrvalue1, attrtype2, attrvalue2, attrtype3, attrvalue3, attrtype4, attrvalue4, attrtype5, attrvalue5, attrtype6, attrvalue6):
		slotsWidth = 15
		slotsHeight = 8
		slot = int(slot)
		if slot <= 120:
			constInfo.GUILDSTORAGE["slots"]["TAB0"][slot] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 120 and slot <= 240:
			constInfo.GUILDSTORAGE["slots"]["TAB1"][slot-120] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 240 and slot <= 360:
			constInfo.GUILDSTORAGE["slots"]["TAB2"][slot-240] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 360 and slot <= 480:
			constInfo.GUILDSTORAGE["slots"]["TAB3"][slot-360] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 480 and slot <= 600: 
			constInfo.GUILDSTORAGE["slots"]["TAB4"][slot-480] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 600 and slot <= 720: 
			constInfo.GUILDSTORAGE["slots"]["TAB5"][slot-600] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
			
	def _GuildStorageTempSlotsAdd(self,slot ,itemVnum, count, socket0, socket1, socket2, socket3, socket4, socket5, attrtype0,attrvalue0, attrtype1,attrvalue1, attrtype2, attrvalue2, attrtype3, attrvalue3, attrtype4, attrvalue4, attrtype5, attrvalue5, attrtype6, attrvalue6):
		slot = int(slot)
		if slot <= 120:
			constInfo.GUILDSTORAGE["tempslots"]["TAB0"][slot] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 120 and slot <= 240:
			constInfo.GUILDSTORAGE["tempslots"]["TAB1"][slot-120] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 240 and slot <= 360:
			constInfo.GUILDSTORAGE["tempslots"]["TAB2"][slot-240] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 360 and slot <= 480:
			constInfo.GUILDSTORAGE["tempslots"]["TAB3"][slot-360] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 480 and slot <= 600:
			constInfo.GUILDSTORAGE["tempslots"]["TAB4"][slot-480] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
		elif slot > 600 and slot <= 720:
			constInfo.GUILDSTORAGE["tempslots"]["TAB5"][slot-600] = [int(itemVnum),int(count), int(socket0), int(socket1), int(socket2), int(socket3), int(socket4), int(socket5), int(attrtype0),int(attrvalue0), int(attrtype1),int(attrvalue1), int(attrtype2), int(attrvalue2), int(attrtype3), int(attrvalue3), int(attrtype4), int(attrvalue4), int(attrtype5), int(attrvalue5), int(attrtype6), int(attrvalue6)]
			
	def _GuildStorageAddLog(self,id,name,date,type,do,desc):
		date = date.replace("+-+"," ")
		desc = desc.replace("+-+"," ")
		self.interface.GuildStorageWindow.LogsInsert(id,name,date,type,do,desc)
		constInfo.GUILDSTORAGE["logs"][int(id)] = [name,date,type,do,desc]
		
	def _GuildStorageQuestCMD(self):
		GFHhg54GHGhh45GHGH.SendQuestInputStringPacket(str(constInfo.GUILDSTORAGE["questCMD"]))
		constInfo.GUILDSTORAGE["questCMD"] = "NULL#"
	
	def GuildStorageQID(self, qid):
		constInfo.GUILDSTORAGE["qid"] = int(qid)
		
	def _GuildStorageAddMemberToList(self,memberId,member,authority0,authority1,authority2,authority3):
		constInfo.GUILDSTORAGE["members"]["member"+memberId] = [member,int(authority0),int(authority1),int(authority2),int(authority3)]
		
	# def AyBlockRebootExit(self):
		# constInfo.REBOOT_BLOCK_EXIT = 1
	
	# def AyDeleteVarBeforeRestart(self):
		# constInfo.ZEIT_BIS_REBOOT = 0
		# constInfo.REBOOT_GUI_SHOW = 0
		# constInfo.REBOOT_POPUP_DIALOG = 0		
	
	# # REBOOTSYSTEM
	# def AyHideRebootGUI(self):
		# if constInfo.REBOOT_GUI_SHOW == 1:
			# constInfo.ZEIT_BIS_REBOOT = 0
			# constInfo.REBOOT_GUI_SHOW = 0
			# constInfo.REBOOT_POPUP_DIALOG = 0
			# self.RebootBoard.Hide()
	
	# def AyFormatRebootTime(self, time):
		# m, s = divmod(time, 60)
		# h, m = divmod(m, 60)
		# return "%d:%02d:%02d" % (h, m, s)	
	
	# def AySetTimeToReboot(self,zeit):
		# if constInfo.REBOOT_GUI_SHOW == 0:
			# rechnen = app.GetTime() + int(zeit)
			# constInfo.ZEIT_BIS_REBOOT = rechnen

	# def __AyUpdateTimeToReboot(self):
		# rechnen = constInfo.ZEIT_BIS_REBOOT - app.GetTime()
		# # Update Reboot-Gui
		# if rechnen > 300:
			# self.RebootZeit.SetText("Verbl. Zeit bis Reboot: " + self.AyFormatRebootTime(rechnen) + " Minuten!")
		# else:

			# rechnen2 = app.GetTime() + 60
			# constInfo.ZEIT_BIS_LOGOUT = rechnen2
			
			# self.RebootZeit.SetText("Verbl. Zeit bis Logout: " + self.AyFormatRebootTime(rechnen) + " Minuten!")
		# # Pop-Up Dialogs
		# if rechnen < 1800 and constInfo.REBOOT_POPUP_DIALOG == 0:
			# self.PopupMessage("In 15 Minuten wirst du vom Server getrennt!")
			# constInfo.REBOOT_POPUP_DIALOG = 1
		# elif rechnen < 960 and constInfo.REBOOT_POPUP_DIALOG == 1:			
		# #elif rechnen < 300 and constInfo.REBOOT_POPUP_DIALOG == 2:
			# self.PopupMessage("In 60 Sekunden wirst du vom Server getrennt!")
			# constInfo.REBOOT_POPUP_DIALOG = 3
		# elif rechnen < 900 and constInfo.REBOOT_POPUP_DIALOG == 3:
			# gms = ["[SA]OnlyTM","[SGM]EnergiZer","[TA]Lisa","[DEV]Exterminatus","[SE]Saxe","[SE]Bonsailix","[SE]Falballa"]
			# # Die Namen die dort man hier eintr?t werden nicht
			# # vom Rebootsystem gekickt
			# if not chr.GetName() in gms:
				# app.Exit()
				
	# def __AyRebootGUI(self):
		# self.RebootBoard = ui.Board()
		# self.RebootBoard.SetSize(300, 40)
		# self.RebootBoard.SetCenterPosition()
		# self.RebootBoard.SetPosition(wndMgr.GetScreenWidth()-440,3)
		# self.RebootBoard.AddFlag('movable')
		# self.RebootBoard.Show()
		
		# # self.RebootIcon = ui.AniImageBox()
		# # #self.RebootIcon.AddFlag("not_pick")
		# # self.RebootIcon.SetPosition(15,15)
		# # self.RebootIcon.SetParent(self.RebootBoard)
		# # self.RebootIcon.AppendImage("d:/ymir work/ui/reboot.tga")
		# # self.RebootIcon.Show()		

		# self.RebootZeit = ui.TextLine()
		# self.RebootZeit.SetParent(self.RebootBoard)
		# self.RebootZeit.SetDefaultFontName()
		# self.RebootZeit.SetPosition(150, 25)
		# self.RebootZeit.SetText("Verbl. Zeit bis Reboot: ??:?? Minuten!")
		# self.RebootZeit.SetHorizontalAlignCenter()
		# self.RebootZeit.SetFontColor(1.0, 0.7843, 0.0)		
		# self.RebootZeit.Show()

	# TEAM BOARD
	def __Team_On(self, name):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogin(2, name)

	# TEAM BOARD		
	def __Team_Off(self, name):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogout(2, name)
			
			
	# WarpGUI
	def OpenWarpGUI(self,slot):
		if background.GetCurrentMapName() == "metin2_map_battlefield":
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Du kannst dich von hier aus nicht Teleportieren!")
			chat.AppendChat(chat.CHAT_TYPE_INFO,"Zum Verlassen der Kampfzone nutze den Button links unten an der Minimap.")
		else:
			if constInfo.warpgui_open == 0:
				import uiwarpboard
				uiwarpboard.WarpBoard().Show()
			
			
	# def Schmiedehandbuch(self,slot):
		# if settinginfo.SchmiedehandbuchOpen == 0:
			# import uischmiedehandbuch
			# uischmiedehandbuch.UppWikiBoard().Show()

	# def SchmiedehandbuchPVP(self,slot):
		# if settinginfo.SchmiedehandbuchPVPOpen == 0:
			# import uischmiedehandbuch_pvp
			# uischmiedehandbuch_pvp.UppWikiBoard().Show()
			
	# def OpenBoxOpener(self,slot):
		# if settinginfo.BoxOpenerOpen == 0:
			# if uiPrivateShopBuilder.IsBuildingPrivateShop():			
				# chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
				# return
			# self.interface.CloseGuildStorage()
			# self.interface.CommandCloseSafebox()
			# import uitreasurechest
			# uitreasurechest.TreasureChestBoard().Show()			
	
	# def OpenSwitchBot(self,slot):
		# if settinginfo.switchbot == 0:
			# import uiswitchbot
			# uiswitchbot.SwitchBoard().Show()	
		# else:
			# if settinginfo.switchbot_minimize == 1:
				# settinginfo.switchbot_minimize = 2
	
	# def BoxOpenerQID(self,qid):
		# settinginfo.OpenBoxQID = int(qid)
		
	# def SkillbookStorageOpen(self,slot):
		# if settinginfo.SkillBookStorageOpen == 0:
			# import uiskillbook
			# uiskillbook.SkillBookBoard().Show()			
		
	def SkillbookStorageQID(self,qid):
		settinginfo.SkillBookQID = int(qid)	
		
	def SkillbookStorageAddBook(self,cmdString):
	
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"SkillbookStorageAddBook")
		cmd = cmdString.split("#")
		bookIndex = int(cmd[0])
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"bookIndex " + str(bookIndex))
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"bookIndex2 " + str(cmd[1]))
		
		
		settinginfo.SkillBookCount[bookIndex] = int(cmd[1])	
		
		#chat.AppendChat(chat.CHAT_TYPE_INFO,str(settinginfo.SkillBookCount[bookIndex]))
	
	# def DungeonkompendiumOpen(self,slot):
		# self.DungeonKompendium.LoadUI()
		
	# def DailyGUIOpen(self,slot):
		# self.interface.OnOpenDaily()
	
	# def DailyGUI(self,slot):
		# if settinginfo.DailyQuest_GUI == 0:
			# if fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL) >= 5:
				# import uidaily
				# uidaily.DailyBoard().Show()	
			# else:
				# chat.AppendChat(chat.CHAT_TYPE_INFO,"Du musst min. Level 5 erreich haben!")
			
	# def DailyQuestCommand(self,cmdString):
		# cmd = cmdString.split("#")
		# if cmd[0] == "qid":
			# settinginfo.DailyQuest_QID = int(cmd[1])
		
		# elif cmd[0] == "mob":
		
			# mobSlot = int(cmd[1])
			# settinginfo.DailyQuest_Monster[mobSlot] = int(cmd[2])
			# settinginfo.DailyQuest_Count[mobSlot] = int(cmd[3])
			
		# elif cmd[0] == "reward":	
			# rewardSlot = int(cmd[1])
			# settinginfo.DailyQuest_Reward[rewardSlot] = int(cmd[2])
			# settinginfo.DailyQuest_RewardCount[rewardSlot] = int(cmd[3])

		
		# elif cmd[0] == "time":
			# settinginfo.DailyQuest_Time = int(cmd[1])

		# elif cmd[0] == "status":
			# settinginfo.DailyQuest_Status = int(cmd[1])
			


	# def DailyTimeText(self):
		# settinginfo.DailyQuest_Time = int(app.GetGlobalTimeStamp()+300)		
		
	def GoldStorageQID(self,inputString):
		settinginfo.GoldStorageQID = int(inputString)
		
	def UppStorageCommand(self,cmdString):
		cmd = cmdString.split("#")
		if cmd[0] == "qid":
			settinginfo.UppItemStorageQID = int(cmd[1])
		elif cmd[0] == "item":
			
			uppStorageCat = int(cmd[1])
			uppStorageSlot = int(cmd[3])
			if uppStorageCat == 1:
				settinginfo.UppItemStorageNormal[uppStorageSlot] = int(cmd[2])
			
			elif uppStorageCat == 2:
				settinginfo.UppItemStorageUsually[uppStorageSlot] = int(cmd[2])
			
			elif uppStorageCat == 3:
				settinginfo.UppItemStorageRare[uppStorageSlot] = int(cmd[2])
			
			 
		elif cmd[0] == "check":
			chat.AppendChat(chat.CHAT_TYPE_INFO,str(len(settinginfo.UppItemStorageNormal)))
			chat.AppendChat(chat.CHAT_TYPE_INFO,str(len(settinginfo.UppItemStorageUsually)))
			chat.AppendChat(chat.CHAT_TYPE_INFO,str(len(settinginfo.UppItemStorageRare)))
		
		elif cmd[0] == "store_all":
			constInfo.INPUT_CMD = "store_all#"
			event.QuestButtonClick(settinginfo.UppItemStorageQID)		
		elif cmd[0] == "update":
			constInfo.INPUT_CMD = "update#"
			event.QuestButtonClick(settinginfo.UppItemStorageQID)			
		
	# SPECIAL CASES
	# def KeyTreasureConfiguration(self, cmd):
		# constInfo.KEY_TREASURE_CONFIG["GUI"].Configuration(cmd)
	
	# SPECIAL CASES
	# def __SpecialCasesOpenFunction(self):	
		# constInfo.KEY_TREASURE_CONFIG["GUI"].Open()
	
	# LAGER BUTTON
	def __Opennormalmall(self, qid):
		constInfo.mallqin= int(qid)
		
	# Yangspeicher
	def __yangspeicher(self, qid):
		constInfo.yangspeicher= int(qid)
		
		
	def __WarpGUIQuestIndex(self,qid):
		self.interface.WARP_SendQuestIndex(qid)
		
	def __WarpGUIFKey(self,cmdString):
		cmd = cmdString.split("#")	
		self.interface.WARP_SetFKey(int(cmd[1]),int(cmd[2]),int(cmd[0]))
	
	def __WarpGUIRefresh(self):
		self.interface.WARP_Refresh()
	
		
	def QuestInputCMD(self):
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"QuestInputCMD")
		GFHhg54GHGhh45GHGH.SendQuestInputStringPacket(str(constInfo.INPUT_CMD))
		constInfo.INPUT_CMD = ""		
		
	def BuffItemEffectChat(self,buffCMD):
		GFHhg54GHGhh45GHGH.SendChatPacket("(" + str(buffCMD) + ")")
		
	# def __ShowAchievementPoints(self, points):
		# import uiAchievement
		# import uiTaskbar
		# self.uiAchievement = uiAchievement.AchievementDialog()
		# uiAchievement.AchievementPoints = int(points)
	
	# def __AchievementTest(self, archivement):
		# import uiAchievement
		# self.uiAchievement = uiAchievement.AchievementDialog()
		# self.uiAchievement.Show(1, str(archivement))
		# self.uiAchievement.SetTop()
		
	def __Aps(self, aps):
		# self.interface.UpdateChannel()
		import constInfo
		constInfo.aps = int(aps)
		
	def __Dps(self, dps):
		import constInfo
		constInfo.dps = int(dps)
		self.interface.RefreshStatus()
		
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"__Dps " + str(constInfo.dps))
	
	# --------------------------------------------------------------------------------
	# Battlezone - Functions
	# def GAME_UpdateBattlePoints(self,points):
		# settinginfo.battlezonePoints = points
		
	# def GAME_SetBattlezoneLeaveTimer(self,timeStamp):
		# settinginfo.battlezoneLeaveTime = int(timeStamp)	
		# settinginfo.battlezoneIsExit = 1
	
	# def GAME_BreakNormalLeave(self):
		# settinginfo.battlezoneLeaveTime = 0
		# settinginfo.battlezoneIsExit = 0
	
	# def GAME_BattlezoneController(self,status):
		# if status == "win":
			# self.mapNameShower.ShowMapName("battle_win", 3, 3)
			# # GFHhg54GHGhh45GHGH.SendChatPacket("/cheerup")		

			# # GFHhg54GHGhh45GHGH.SendChatPacket("/cheer1")		
		# elif status == "loose":
			# self.mapNameShower.ShowMapName("battle_loose", 3, 3)
			# # GFHhg54GHGhh45GHGH.SendChatPacket("/sad")
		
		# elif status == "draw":
			# self.mapNameShower.ShowMapName("battle_draw", 3, 3)
			# # GFHhg54GHGhh45GHGH.SendChatPacket("/cheer1")
		
		
		# if status == "enter_request":
			# itemDropQuestionDialog = uiCommon.QuestionDialog()
			# itemDropQuestionDialog.SetText("Mochtest du die Kampfzone betreten?")
			# itemDropQuestionDialog.SetAcceptEvent(lambda arg=1: self.battlezoneRequestEnter(arg))
			# itemDropQuestionDialog.SetCancelEvent(lambda arg=2: self.battlezoneRequestEnter(arg))
			# itemDropQuestionDialog.Open()
			# self.itemDropQuestionDialog = itemDropQuestionDialog
			# constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		# elif status == "request":
			# itemDropQuestionDialog = uiCommon.QuestionBattlezoneDialogLeave()
			# itemDropQuestionDialog.SetText(str(settinginfo.battlezonePoints) + "Punkt(e)")
			# itemDropQuestionDialog.SetAcceptEvent(lambda arg=1: self.battlezoneRequestleave(arg))
			# itemDropQuestionDialog.SetDestroyEvent(lambda arg=2: self.battlezoneRequestleave(arg))
			# itemDropQuestionDialog.SetCancelEvent(lambda arg=3: self.battlezoneRequestleave(arg))
			# itemDropQuestionDialog.Open()
			# self.itemDropQuestionDialog = itemDropQuestionDialog

			# constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		# elif status == "instant_exit":
			# itemDropQuestionDialog = uiCommon.QuestionDialog()
			# itemDropQuestionDialog.SetText("Mochtest du die Kampfzone jetzt verlassen?")
			# itemDropQuestionDialog.SetAcceptEvent(lambda arg=1: self.battlezoneRequestLeaveInstant(arg))
			# itemDropQuestionDialog.SetCancelEvent(lambda arg=2: self.battlezoneRequestLeaveInstant(arg))
			# itemDropQuestionDialog.Open()
			# self.itemDropQuestionDialog = itemDropQuestionDialog
			# constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		# elif status == "succeed":
			# if app.GetRandom(1,2) == 1:
				# GFHhg54GHGhh45GHGH.SendChatPacket("/cheer2")		
			# else:
				# GFHhg54GHGhh45GHGH.SendChatPacket("/cheer1")
				
	# def battlezoneRequestLeaveInstant(self,arg):
		# if not self.itemDropQuestionDialog:
			# return
		# self.itemDropQuestionDialog.Close()
		# self.itemDropQuestionDialog = None
		# constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		# if arg == 1:
			# GFHhg54GHGhh45GHGH.SendChatPacket("/user_quick_exit_battlezone")		
		
	# def battlezoneRequestEnter(self,arg):	
		# if not self.itemDropQuestionDialog:
			# return
		# self.itemDropQuestionDialog.Close()
		# self.itemDropQuestionDialog = None
		# constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		# if arg == 1:
			# GFHhg54GHGhh45GHGH.SendChatPacket("/user_enter_battlezone")
		
	# def battlezoneRequestleave(self,arg):
		# if not self.itemDropQuestionDialog:
			# return
		# #chat.AppendChat(chat.CHAT_TYPE_INFO,"battlezoneRequestleave " + str(arg))
		# self.itemDropQuestionDialog.Close()
		# self.itemDropQuestionDialog = None
		# constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
		# if arg == 1:
			# GFHhg54GHGhh45GHGH.SendChatPacket("/user_normal_leave_battlezone")
		# elif arg == 2:
			# #constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)		
			# itemDropQuestionDialog = uiCommon.QuestionDialog()
			# itemDropQuestionDialog.SetText("Achtung! Du wirst samtliche Punkte verlieren beim Sofort verlassen!")
			# itemDropQuestionDialog.SetAcceptEvent(lambda arg=1: self.battlezoneRequestLeaveInstant(arg))
			# itemDropQuestionDialog.SetCancelEvent(lambda arg=2: self.battlezoneRequestLeaveInstant(arg))
			# itemDropQuestionDialog.Open()
			# self.itemDropQuestionDialog = itemDropQuestionDialog
			# constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	# --------------------------------------------------------------------------------
	
	# --------------------------------------------------------------------------------
	# Pet - System - Functions	

	# def GAME_Pet(self,cmdString):
		# cmd = cmdString.split("#")
		# if cmd[0] == "opennamebox":
			# if settinginfo.PET_INFOS["gui_box"] == 1:
				# chat.AppendChat(chat.CHAT_TYPE_INFO,"Das geht immoment nicht.")
				# return
			# settinginfo.PET_INFOS["itemVnum"] 	= int(cmd[1])
			# settinginfo.PET_INFOS["itemIndex"] 	= int(cmd[2])
			# settinginfo.PET_INFOS["price"] 		= int(cmd[3])
			# settinginfo.PET_INFOS["gui_box"] 	= 1
			
			# import uipet
			# uipet.PetBoxBoard().Show()	
		
		# #  Name
		# elif cmd[0] == "name":
			# settinginfo.PET_INFOS["name"] 		= str(cmd[1])
		
		# #  Level
		# elif cmd[0] == "level":
			# settinginfo.PET_INFOS["level"] 		= int(cmd[1])
		
		# #  EXP
		# elif cmd[0] == "mexp":
			# settinginfo.PET_INFOS["exp"] 		= int(cmd[1])
		
		# #  I-EXP
		# elif cmd[0] == "iexp":
			# settinginfo.PET_INFOS["iexp"] 		= int(cmd[1])
			
		# # Sendet die benotigte Menge an iEXP an den Clienten. char.cpp 
		# elif cmd[0] == "nextiexp":
			# settinginfo.PET_INFOS["next_iexp"] 	= int(cmd[1])

	# def opensetting(self):
		# if settinginfo.isGM:
			# import pythonloader


	# --------------------------------------------------------------------------------
	# Achievement - System - Functions	

	def LUA_Achievement(self,cmdString):
		cmd = cmdString.split("#")
		self.AchievementWindow.SendAchievement(cmd[0],cmd[1],cmd[2],cmd[3])
		settinginfo.PLAYER_STATISTIC_DICT[settinginfo.AP_EARNED] = settinginfo.PLAYER_STATISTIC_DICT[settinginfo.AP_EARNED] + int(cmd[1])

	# def LUA_AchievementStatistic(self,cmdString):
		# # achievement_stat add/1/15/8001#30#10#30000#
		# cmd = cmdString.split("/")
		# if cmd[0] == "open":
			# if settinginfo.Achievement_Statistic["status"] == 0:
				# import locutosachievementstat
				# locutosachievementstat.AchievementStatisticBoard().Show()
				
		# elif cmd[0] == "add":
			# settinginfo.Achievement_Statistic[int(cmd[1])][int(cmd[2])] = str(cmd[3])

			
	# def LUA_OpenGMPost(self):
		# import uigmpost
		# uigmpost.GMPostBoard().Show()
			
	# def LUA_DailyCommand(self,cmdString):
		# cmd = cmdString.split("/")
		# if cmd[0] == "qid":
			# settinginfo.DailyQuest_QID = int(cmd[1])
		# elif cmd[0] == "status":
			# self.DailyGUI.SetLayoutType(int(cmd[1]))
			
		# elif cmd[0] == "time":
			# settinginfo.DailyQuest_Time = int(cmd[1])
			
		# elif cmd[0] == "kill":
			# self.DailyGUI.UpdateKillCounter(int(cmd[1]),int(cmd[2]),int(cmd[3]),int(cmd[4]))
			
		# elif cmd[0] == "points":
			# self.DailyGUI.SetRewardAmount(int(cmd[1]))

	# def LUA_MultishopCommand(self,cmdString):
		# cmd = cmdString.split("/")
		# if cmd[0] == "qid":
			# self.MultiShop.SetMultiShopQuestIndex(int(cmd[1]))
			
		# elif cmd[0] == "title":
			# self.MultiShop.SetMultiShopTitle(cmd[1])
			
		# elif cmd[0] == "reset":
			# self.MultiShop.ResetMultiShop()
		
		# elif cmd[0] == "item":
			# self.MultiShop.SetMultiShopItemSlot(int(cmd[1]),int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]))
			
		# elif cmd[0] == "hide_multishop":
			# self.MultiShop.HideMultiShop()
			
		# elif cmd[0] == "open":
			# self.MultiShop.ShowMultiShop()
			
		# elif cmd[0] == "currency":
			# self.MultiShop.SetMultiShopCurrency(int(cmd[1]),int(cmd[2]))
		
		# elif cmd[0] == "index":
			# self.MultiShop.SetMultiShopIndex(int(cmd[1]))
	
	# def LUA_IntroDungeonCommand(self,cmdString):
		# cmd = cmdString.split("/")
		# if cmd[0] == "qid":
			# self.IntroDungeonTextBoard.GAME_SetQuestIndex(int(cmd[1]))	
		# elif cmd[0] == "open":
			# self.IntroDungeonTextBoard.GAME_InitIntroDungeonGUI(int(cmd[1]))
		# elif cmd[1] == "complete":
			# GFHhg54GHGhh45GHGH.SendChatPacket("/cheer2")

	# def GAME_ToggleSidebar(self):
		# self.sideBar.ToggleMinimize()
		
	def LUA_BossMapInfo(self,cmdString):
		cmd = cmdString.split("/")
		if cmd[0] == "open":
			self.interface.wndMiniMap.ShowBossMapInfo()
		
		elif cmd[0] == "uses":
			self.interface.wndMiniMap.UpdateBossMapUsesInfo(int(cmd[1]))
		
		elif cmd[0] == "time":
			settinginfo.bossMapTimer = int(cmd[1])
		
	# def LUA_EventFlagList(self,cmdString):
		# cmd = cmdString.split("/")
		# index = int(cmd[0])
		# settinginfo.event_eventflags_names[index] = str(cmd[1])
		# settinginfo.event_eventflags_indez[index] = int(cmd[2])

	# def LUA_GuideBoard(self,guideIndex):
		# self.GuideDialogBoard.GAME_InitGuideBoard(int(guideIndex))

	# def LUA_BioTimer(self,cmdString):
		# cmd = cmdString.split("/")
		# if cmd[0] == "init":		
			# settinginfo.bio_timer_status = int(cmd[1])
		
		# elif cmd[0] == "time":
			# settinginfo.bio_timer = int(cmd[1])
		
	# def LUA_PetAffectShower(self,status):
		# status = int(status)
		# self.affectShower.ShowPetAffect(status)

	def LUA_isGM(self):
		settinginfo.isGM = True

	def openHallOfFame(self,slot):
		uihalloffame.wnd.OpenRequest()		
		
	def halloffameCmd(self, cmd):
		uihalloffame.wnd.Command(cmd)		
		

	# def ResetActivateButtons(self):
		# constInfo.YangChatStatus = 0
		# constInfo.AntiExpStatus = 0
		# settinginfo.autoPotionStatus = 0
		# constInfo.PET_INFOS["skill_status"] = 0
		
	def DayInfo(self, row):
		self.interface.uidayliquest.WorkWithString(row)	
		
	def __PetInputget1(self):
		constInfo.INPUT_IGNORE = 1
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"<__PetInputget1> " + str(constInfo.INPUT_IGNORE))
		
	def __PetInputget2(self):
		constInfo.INPUT_IGNORE = 0
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"<__PetInputget2> " + str(constInfo.INPUT_IGNORE))
		
	def __PetInputget3(self): 
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"<__PetInputget3> " + str(constInfo.INPUT_CMD))
		GFHhg54GHGhh45GHGH.SendQuestInputStringPacket(constInfo.INPUT_CMD)
		constInfo.INPUT_CMD = 0
		#chat.AppendChat(chat.CHAT_TYPE_INFO,"<__PetInputget3> " + str(constInfo.INPUT_CMD))
				
		
	# def __PetSystem(self,command):
		# cmd = command.split("#")
		# if cmd[0] == "qid":
			# constInfo.PET_INFOS["qid"] = int(cmd[1])
		# elif cmd[0] == "box":
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "box")

			# if constInfo.PET_INFOS["gui_box"] == 0:
				# constInfo.PET_INFOS["itemIndex"] = int(cmd[1])

				# constInfo.PET_INFOS["price"] = int(cmd[2])

				# constInfo.PET_INFOS["itemVnum"] = int(cmd[3])
				# constInfo.PET_INFOS["box_mode"] = int(cmd[4])
				# import uipet
				# uipet.PetBoxBoard().Show()			
		# elif cmd[0] == "name":
			# constInfo.PET_INFOS["name"] = str(cmd[1])
		# elif cmd[0] == "level":
			# if int(cmd[1]) == 0:
				# constInfo.PET_INFOS["skill_status"] = 0
			# constInfo.PET_INFOS["level"] = int(cmd[1])
			# constInfo.PET_INFOS["mob_exp"] = int(cmd[2])
			# constInfo.PET_INFOS["item_exp"] = int(cmd[3])
		# elif cmd[0] == "life":
			# constInfo.PET_INFOS["life"] = int(cmd[1])
		# elif cmd[0] == "attr":
			# constInfo.PET_INFOS["attr"][0] = int(cmd[1])
			# constInfo.PET_INFOS["attr"][1] = int(cmd[2])
			# constInfo.PET_INFOS["attr"][2] = int(cmd[3])
			# constInfo.PET_INFOS["attr"][3] = int(cmd[4])
			# constInfo.PET_INFOS["attr"][4] = int(cmd[5])
			# constInfo.PET_INFOS["attr"][5] = int(cmd[6])
		# elif cmd[0] == "skill":
			# constInfo.PET_INFOS["skill_level"] = int(cmd[1])
		# elif cmd[0] == "skill_status":
			# constInfo.PET_INFOS["skill_status"] = int(cmd[1])
		# elif cmd[0] == "list_constinfo":
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "~~~~~~~~~~~~~~~~~~~~~ Info: ~~~~~~~~~~~~~~~~~~~~~")
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "Name: " + str(constInfo.PET_INFOS["name"]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "Level: " + str(constInfo.PET_INFOS["level"]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "mob_exp: " + str(constInfo.PET_INFOS["mob_exp"]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "item_exp: " + str(constInfo.PET_INFOS["item_exp"]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "life: " + str(constInfo.PET_INFOS["life"]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "~~~~~~~~~~~~~~~~~~~~~ Boni: ~~~~~~~~~~~~~~~~~~~~~")
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "attr00: " + str(constInfo.PET_INFOS["attr"][0]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "attr01: " + str(constInfo.PET_INFOS["attr"][1]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "attr02: " + str(constInfo.PET_INFOS["attr"][2]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "attr03: " + str(constInfo.PET_INFOS["attr"][3]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "attr04: " + str(constInfo.PET_INFOS["attr"][4]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "attr05: " + str(constInfo.PET_INFOS["attr"][5]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "~~~~~~~~~~~~~~~~~~~~~ Skill: ~~~~~~~~~~~~~~~~~~~~~")
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "skill_level: " + str(constInfo.PET_INFOS["skill_level"]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "skill_status: " + str(constInfo.PET_INFOS["skill_status"]))
		# elif cmd[0] == "guiopen":
			# if constInfo.PET_INFOS["level"] == 0:
				# chat.AppendChat(chat.CHAT_TYPE_INFO, "Rufe bitte zuerst dein Pet!")
				# return
			# if constInfo.PET_INFOS["gui"] == 1:
				# constInfo.PET_INFOS["guiclose"] = 1
				# return
			# import uipet
			# uipet.PetBoard().Show()
		# elif cmd[0] == "doubleexp":
			# constInfo.PET_INFOS["double_exp"] = int(cmd[1])
			
	def ManagerBlockItems(self, cmd):
		cmd = cmd.split("|")
		if cmd[0] == "BlockItems":
			constInfo.BlockItemsSystem["Block"] = 1
		elif cmd[0] == "UnBlockItems":
			constInfo.BlockItemsSystem["Block"] = 0
			
	# def LUA_Calender(self,command):
		# cmd = command.split("#")
		# self.Calender.GAME_AddEventInfo(cmd[0],cmd[1],cmd[2],cmd[3])

	# def CalenderButton(self,slot):
		# if self.Calender.GAME_IsShow():
			# self.Calender.GAME_Hide()
		# else:
			# self.Calender.GAME_Show()
	
	def LUA_CostumeAttributeChanger(self,command):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"LUA_CostumeAttributeChanger: " + command)
		cmd = command.split("/")
		if cmd[0] == "qid":
			self.interface.SetCostumeAttributeChangerQID(cmd[1])
		elif cmd[0] == "refresh":
			self.interface.RefreshCostumeAttributeChanger()
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Unknown Command [LUA_CostumeAttributeChanger]: " + str(cmd[0]))
	
	def LUA_Biologist(self,command):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"LUA_Biologist: " + command)
		cmd = command.split("/")
		if cmd[0] == "qid":
			self.interface.AddBiologistQuestIndex(int(cmd[1]))
		elif cmd[0] == "quest":
			self.interface.AddBiologistQuest(int(cmd[1]),int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6]),int(cmd[7]),int(cmd[8]),int(cmd[9]))
		elif cmd[0] == "count":
			self.interface.UpdateBiologistQuest_ITEM_COUNT(int(cmd[1]),int(cmd[2]))
		elif cmd[0] == "time":
			self.interface.UpdateBiologistQuest_TIMER(int(cmd[1]),int(cmd[2]))
		elif cmd[0] == "open":
			self.interface.OpenBiologistWindow()
		elif cmd[0] == "update":
			self.interface.UpdateBiologistQuest(int(cmd[1]),int(cmd[2]))
		elif cmd[0] == "refresh":
			self.interface.RefreshBiologistQuestList()
		elif cmd[0] == "final":
			self.interface.ShowBiologistSuccessOfFailWindow(int(cmd[1]))
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Unknown Command [LUA_Biologist]: " + str(cmd[0]))

	def LUA_Multishop_2019(self,command):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,command)
		cmd = command.split("/")
		if cmd[0] == "qid":
			self.interface.SetMultiShopQuestIndex(int(cmd[1]))
		elif cmd[0] == "index":
			self.interface.SetMultiShopIndex(int(cmd[1]))
		elif cmd[0] == "name":
			self.interface.SetMultiShopName(int(cmd[1]))
		elif cmd[0] == "add_c":
			self.interface.AppendMultiShopCategory(int(cmd[1]))
		elif cmd[0] == "add_i":
			self.interface.AppendMultiShopItem(int(cmd[1]), int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6]),int(cmd[7]),int(cmd[8]))
		elif cmd[0] == "open":
			self.interface.OpenMultiShop()
		elif cmd[0] == "close":
			self.interface.CloseMultiShop()
		elif cmd[0] == "clear":
			self.interface.ClearMultiShop()
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Unknown Command [LUA_Multishop_2019]: " + str(cmd[0]))	
			
	def LUA_Quest(self,command):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,command)
		cmd = command.split("/")
		if cmd[0] == "qd":
			if cmd[1] == "qid":
				self.interface.QuestDialog_SetQuestIndex(cmd[2])
			
			elif cmd[1] == "title":
				self.interface.QuestDialog_Title(cmd[2])
			
			elif cmd[1] == "desc":
				self.interface.QuestDialog_Desc(cmd[2])
			
			elif cmd[1] == "targettitle":
				self.interface.QuestDialog_TargetTitle()
			
			elif cmd[1] == "target":
				self.interface.QuestDialog_Target(cmd[2],cmd[3],cmd[4],cmd[5],cmd[6])
			
			elif cmd[1] == "rewardtitle":
				self.interface.QuestDialog_RewardTitle()
			
			elif cmd[1] == "reward":
				self.interface.QuestDialog_Reward(cmd[2],cmd[3],cmd[4])
			
			elif cmd[1] == "bottom":
				self.interface.QuestDialog_BottomMode(cmd[2])
			
			elif cmd[1] == "clear":
				self.interface.QuestDialog_Clear()
			
			elif cmd[1] == "open":
				self.interface.QuestDialog_Open()
			
			elif cmd[1] == "close":
				self.interface.QuestDialog_Close()
				
			elif cmd[1] == "ddecline":
				self.interface.QuestDialog_DisableDecline()
			
			else:
				chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Unknown QuestCommand: qd/" + cmd[1])
		
		elif cmd[0] == "qw":
			if cmd[1] == "blink":
				self.interface.QuestWindow_Blink()
			elif cmd[1] == "init":
				self.interface.QuestWindow_INIT(int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]),cmd[6],cmd[7])

			elif cmd[1] == "remove":
				self.interface.QuestWindow_Remove(int(cmd[2]),int(cmd[3]))
	
			elif cmd[1] == "target":
				self.interface.QuestWindow_AppendTarget(int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6]),int(cmd[7]),cmd[8])
				
			elif cmd[1] == "update":
				self.interface.QuestWindow_UpdateTarget(int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6]),cmd[7])
				
			elif cmd[1] == "reward":
				self.interface.QuestWindow_AppendReward(int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6]))

			else:
				chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Unknown QuestCommand: qw/" + cmd[1])
		
		elif cmd[0] == "qv":
			if cmd[1] == "init":
				self.interface.QuestView_Init(int(cmd[2]),int(cmd[3]))
				
			elif cmd[1] == "objective":
				self.interface.QuestView_AppendObjective(int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]),int(cmd[6]))
				
			elif cmd[1] == "update":
				self.interface.QuestView_Update(int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]))
			
			elif cmd[1] == "remove":
				self.interface.QuestView_Remove(int(cmd[2]))
				
			elif cmd[1] == "refresh":
				self.interface.QuestView_Refresh()
			
			else:
				chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Unknown QuestCommand: qv/" + cmd[1])
		
	def LUA_GMPanel(self,command):
		cmd = command.split("/")
		if cmd[0] == "qid":
			self.interface.GM_AppendQuestIndex(int(cmd[1]),int(cmd[2]))
		elif cmd[0] == "permission":
			self.interface.GM_InsertPermission(int(cmd[1]))
		elif cmd[0] == "refresh":
			self.interface.GM_RefreshButtons()
		elif cmd[0] == "activate":
			self.interface.GM_ActivateButton(int(cmd[1]))
		elif cmd[0] == "deactivate":
			self.interface.GM_DeactivateButton(int(cmd[1]))
		elif cmd[0] == "eqid":
			self.interface.GM_AppendEventQuestIndex(int(cmd[1]),int(cmd[2]))
	
	def LUA_UserEvent(self,command):
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "command")
		cmd = command.split("/")
		if cmd[0] == "tde":	
			self.interface.AppendTeampDropEventInformation(cmd[1],int(cmd[2]),int(cmd[3]),int(cmd[4]),int(cmd[5]))
			# chat.AppendChat(chat.CHAT_TYPE_INFO, "LUA_UserEvent: " + str(cmd[1]))
			
			
	def LUA_OXEvent(self,command):
		cmd = command.split("#")
		
		if cmd[0] == "init":
			self.OXManager.GAME_Init()
		
		elif cmd[0] == "qid":
			self.OXManager.GAME_SetLUAQuestIndex(cmd[1])
		
		elif cmd[0] == "field":
			self.OXManager.GAME_Answer(cmd[1])
		
		elif cmd[0] == "points":
			self.OXManager.GAME_Points(int(cmd[1]))
			
		elif cmd[0] == "time":
			self.OXManager.GAME_Time(int(cmd[1]))
		
	def DragonCoins(self,points):
		settinginfo.DragonCoins = int(points)
		self.interface.SetDragonCoins(settinginfo.DragonCoins)
		
	# def OpenBugReport(self,slot):
		# self.BugReporter.Manage()
		
	def ForestTimer(self,timer):
		settinginfo.forest_zone_time = int(timer)
		
	# def TestNewWARPUI(self):
		# import uiwarp
		# self.warp = uiwarp.WarpWindow()
		
	def TextButtonProjection(self,vid):
		import uibuttonprojection
		self.buttonProject = uibuttonprojection.ButtonProjection()
		self.buttonProject.Open(int(vid))
		# settinginfo.VID_FORGE_BIND_TEST = int(vid)
		
	# def TestGMPanel(self,slot):
		# self.interface.ShowGMPanelButton()
		
	# def LUA_Biologist(self):
		# self.interface.ShowBiologistWindow()
		
	def SetDebugMode(self,debug):
		self.isDebugMode = int(debug)
		
	def BiologistIconText(self):
		# import uifortunefountain
		# self.interface.ctrlAchievement.AppendAchievement(1,10,3345,5)
		# import uicrafting
		# self.craftingWnd = uicrafting.CraftingWindow()
		# self.advent = uidungeon.DungeonGuideWindow()
		# self.advent.Show()
		# import uichanneltabbar
		# self.wndChannelTabBar = uichanneltabbar.ChannelTabBar()
		import achievementproto
		data = achievementproto.GetAchievementInfo(101)
		if data == False:
			
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Nope...?")
		else:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "data: " + str(len(data)))
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "data: " + str(data[0]))
		
	def __RequestWarpToCharacter(self, name):
		import uiCommon
		questionDialogWarp=uiCommon.QuestionDialog()
		questionDialogWarp.SetText(localeInfo.REQUEST_WARP_TO_CHARACTER % (name))
		questionDialogWarp.SetAcceptEvent(lambda arg=TRUE: self.WarpAcceptEvent(name))
		questionDialogWarp.SetCancelEvent(lambda arg=FALSE: self.WarpCancelEvent())		
		questionDialogWarp.Open()
		self.questionDialogWarp=questionDialogWarp
		return
		
	def WarpAcceptEvent(self, name):
		GFHhg54GHGhh45GHGH.SendMessengerSummonByNamePacket(name)
		self.questionDialogWarp.Close()
		
	def WarpCancelEvent(self):
		self.questionDialogWarp.Close()
		
	def RefreshCharacterNow(self):
		self.interface.RefreshStatus()
		self.interface.RefreshSkill()
		
	def SetPlayerStatistic(self,command):
		cmd = command.split("#")
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "index: " + str(cmd[0]) + ", value: " + str(cmd[1]))
		try:
			index = int(cmd[0])
			
			if index == settinginfo.STONE_KILL_TEMP:
				settinginfo.PLAYER_STATISTIC_DICT[settinginfo.STONE_KILL_TEMP] = settinginfo.PLAYER_STATISTIC_DICT[settinginfo.STONE_KILL_TEMP] + 1
			
			elif index == settinginfo.MONSTER_KILL_TEMP:
				settinginfo.PLAYER_STATISTIC_DICT[settinginfo.MONSTER_KILL_TEMP] = settinginfo.PLAYER_STATISTIC_DICT[settinginfo.MONSTER_KILL_TEMP] + 1
			
			else:
				settinginfo.PLAYER_STATISTIC_DICT[index] = int(cmd[1])	
		except:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Error in PlayerStatistic! Failed to SetData. -> " + command)
		
		
	def InitPickUpFilter(self,index):
		self.interface.GAME_InitPickUpFilter(int(index))
		
		
	def LUA_FloatingDialog(self,command):
		cmd = command.split("#")
		uidialog.MakeNewFloatingDialog(int(cmd[0]),cmd[1],int(cmd[2]))
		
	def LUA_ShowTutorialJoinDialog(self,qid):
		self.interface.wndTutorialJoin.Open(int(qid))
	
	def LUA_HideTutorialJoinDialog(self):
		self.interface.wndTutorialJoin.Close()
	
	def LUA_UpdateAchievementStatistic(self,command):
		cmd = command.split("#")
		self.interface.wndCharacter.UpdateAchievementStatistic(cmd[0], cmd[1], cmd[2])
		
	def GAME_DanceAll(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/dance7")
		
	
		
