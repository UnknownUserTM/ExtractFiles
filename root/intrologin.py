import app
import GFHhg54GHGhh45GHGH
import ui
import snd
import wndMgr
import musicInfo
import systemSetting
import localeInfo
import constInfo
import ime
import uiScriptLocale
import os
import dbg
from _weakref import proxy
import serverInfo2
import ServerStateChecker

import binascii			
import _winreg
REG_PATH = r"SOFTWARE\Origins"

class SentryDialog(ui.ScriptWindow):

	def __init__(self, event):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog(event)
		self.accept_button = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self, event):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/sentrydialog.py")

			self.board = self.GetChild("board")
			self.accept_button = self.GetChild("accept_button")
			self.titleBar = self.GetChild("TitleBar")

			if self.accept_button is not None:
				self.accept_button.SetEvent(ui.__mem_func__(event))

			self.titleBar.SetCloseEvent(ui.__mem_func__(event))

		except:
			import exception
			exception.Abort("ConnectingDialog.LoadDialog.BindObject")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()
		self.ClearDictionary()

def set_reg(name, value):
    try:
        _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
        _winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return str(value)
    except WindowsError:
        return None		
		
class LoginWindow(ui.ScriptWindow):

	IS_TEST = GFHhg54GHGhh45GHGH.IsTest()
	
	class AccountButton(ui.Bar):
		def __init__(self, owner, arg):
			ui.Bar.__init__(self)
			self.owner = owner
			self.arg = arg
			
		def OnMouseOverIn(self):
			self.SetColor(0x207D1717)
			
		def OnMouseOverOut(self):
			self.SetColor(0x00000000)
			
		def OnMouseLeftButtonDown(self):
			if self.owner.channelID != self.arg:
				self.owner.SetChannel(self.arg)

	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		
		GFHhg54GHGhh45GHGH.SetPhaseWindow(GFHhg54GHGhh45GHGH.PHASE_WINDOW_LOGIN, self)
		GFHhg54GHGhh45GHGH.SetAccountConnectorHandler(self)

		self.stream = stream
		
		self.accountLabel = {}
		self.channelLabel = {}
		self.channelID = 0
		self.position = [17, 70]
		
		self.sentryDialog = None
		
		self.channelButton = None
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
		GFHhg54GHGhh45GHGH.ClearPhaseWindow(GFHhg54GHGhh45GHGH.PHASE_WINDOW_LOGIN, self)
		GFHhg54GHGhh45GHGH.SetAccountConnectorHandler(0)

	def Open(self):
		ServerStateChecker.Create(self)
		
		print "LOGIN WINDOW OPEN ----------------------------------------------------------------------------"
		
		self.loginFailureMsgDict={

			"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: localeInfo.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
			"REBOOT"	: localeInfo.LOGIN_CONNECT_REBOOT,
			"PWCHANGE"	: localeInfo.LOGIN_CONNECT_PWCHANGE,
			"SBLOCK"	: localeInfo.LOGIN_CONNECT_SBLOCK,
			"BOT"		: localeInfo.LOGIN_CONNECT_BOT,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: localeInfo.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: localeInfo.LOGIN_FAILURE_WEB_BLOCK,
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: app.Exit,
		}

		if app.NEW_CLIENT_VERSION_CHECK:
			self.loginFailureMsgDict["WRONGVER"] = localeInfo.LOGIN_FAILURE_WRONG_VERSION
			self.loginFailureFuncDict["WRONGVER"] = app.Exit
		
		self.__RequestServerStateList()
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")

		self.__LoadScript("tbx/ui/loginwindow.py")
		
		for i in xrange(4):
			self.CreateChannel(i)
			
		self.CheckAccount()
		
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/" + musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
		
		self.SetChannel(0)
		
		self.Show()
		app.ShowCursor()		

	def __RequestServerStateList(self):
		regionID = 0
		serverID = 1

		try:
			channelDict = serverInfo2.REGION_DICT[regionID][serverID]["channel"]
		except:
			print " __RequestServerStateList - serverInfo.REGION_DICT(%d, %d)" % (regionID, serverID)
			return

		channelDict = serverInfo2.REGION_DICT[regionID][serverID]["channel"]
		ServerStateChecker.Initialize();
		for id, channelDataDict in channelDict.items():
			key=channelDataDict["key"]
			ip=channelDataDict["ip"]
			udp_port=channelDataDict["udp_port"]
			ServerStateChecker.AddChannel(key, ip, udp_port)
		
		ServerStateChecker.Request()

	def Close(self):
		ServerStateChecker.Initialize(self)
		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)
	
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
	
		self.Hide()
		app.HideCursor()
		ime.ClearExceptKey()

	def NotifyChannelState(self, addrKey, state):
		try:
			stateName=serverInfo2.STATE_DICT[state]
		except:
			stateName=serverInfo2.STATE_NONE
		
		regionID=0
		serverID=1
		channelID=addrKey%10
		try:
			serverInfo2.REGION_DICT[regionID][serverID]["channel"][channelID]["state"] = stateName
		except:
			import exception
			exception.Abort(localeInfo.CHANNEL_NOT_FIND_INFO)

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.EmptyFunc)

	def OnHandShake(self):
		snd.PlaySound("sound/ui/loginok.wav")
		self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)
		
	def OnExitSentryDialog(self):
		if self.sentryDialog:
			self.sentryDialog.Close()
		self.sentryDialog = None

	def OnLoginFailure(self, error):
		if error == "SENTRY":
			self.stream.popupWindow.Close()
			if not self.sentryDialog:
				self.sentryDialog = SentryDialog(self.OnExitSentryDialog)

			self.sentryDialog.Open()
			snd.PlaySound("sound/ui/loginfail.wav")

			return
			
		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
		
			loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN  + error

		loginFailureFunc = self.loginFailureFuncDict.get(error, self.EmptyFunc)

		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			self.scrollBoard = self.GetChild("board")
			self.pasteBoard = self.GetChild("pasteBoard")
			self.idEditLine = self.GetChild("id")
			self.pwdEditLine = self.GetChild("pwd")
			self.enterButton = self.GetChild("enter_button")
			self.saveButton = self.GetChild("save_button")
			self.deleteButton = self.GetChild("delete_main_button")
			self.exitButton = self.GetChild("exit_button")
			self.loginLanguageBoard = self.GetChild("LanguageBoard")
			self.showPasteBoardButton = self.GetChild("new_secure_register_button")
			self.closePasteBoardButton = self.GetChild("cancelPasteButton")
			# self.scrollBoard.SetPosition(0,wndMgr.GetScreenHeight())
			# self.scrollAnimation = 1
			# self.scrollStartHeight = wndMgr.GetScreenHeight()
			# self.scrollEndHeight = 50
			self.closePasteBoardButton.SetEvent(self.ClosePasteBoard)
			self.showPasteBoardButton.SetEvent(self.OpenPasteBoard)
			self.pasteBoard.Hide()
			self.fKeyTextLine = []
			for i in xrange(8):
				self.fKeyTextLine.append(self.GetChild("account_button_textline_" + str(i)))
				self.fKeyTextLine[i].Hide()
			
			self.accountButton = []
			for i in xrange(8):
				self.accountButton.append(self.GetChild("account_button_" + str(i)))
				self.accountButton[i].SetEvent(ui.__mem_func__(self.LoadAccount), i)
				self.accountButton[i].Disable()
				
			self.accountDeleteButton = []
			for i in xrange(8):
				self.accountDeleteButton.append(self.GetChild("account_delete_button_" + str(i)))
				self.accountDeleteButton[i].SetEvent(ui.__mem_func__(self.DeleteAccount), i)
				self.accountDeleteButton[i].Disable()
			
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")
		
		self.enterButton.SetText(localeInfo.LOGIN_LOGIN)
		self.saveButton.SetText(localeInfo.LOGIN_SAVE)
		self.exitButton.SetText(localeInfo.LOGIN_CLOSE)
		self.deleteButton.Hide()
		self.enterButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.saveButton.SetEvent(ui.__mem_func__(self.SaveAccount))
		self.deleteButton.SetEvent(ui.__mem_func__(self.OnDeleteAccount))
		self.exitButton.SetEvent(ui.__mem_func__(self.OnPressExitKey))
		
		self.idEditLine.SetReturnEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.idEditLine.SetTabEvent(ui.__mem_func__(self.pwdEditLine.SetFocus))
		self.pwdEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.pwdEditLine.SetTabEvent(ui.__mem_func__(self.idEditLine.SetFocus))
		self.idEditLine.SetFocus()
		self.__RequestServerStateList()
		self.InitLanguageBoard()
	
	def OpenPasteBoard(self):
		self.scrollBoard.Hide()
		self.pasteBoard.Show()

	def ClosePasteBoard(self):
		self.scrollBoard.Show()
		self.pasteBoard.Hide()		


	def InitLanguageBoard(self):
		self.Y_START = 7
		self.X_SPACE = self.Y_START
		self.WIDTH_FLAG = 36

		self.typeButtonList, languageList, groupButtonDict = [], app.GetLanguageList(), {}

		for i in xrange(len(languageList)):
			bLanguage = languageList[i]

			groupButtonDict[i] = ui.RadioButton()
			groupButtonDict[i].SetParent(self.loginLanguageBoard)
			groupButtonDict[i].SetPosition(self.X_SPACE, 8)
			groupButtonDict[i].SetUpVisual("d:/ymir work/ui/language_system/login_language/flag_%s_norm.tga" % bLanguage)
			groupButtonDict[i].SetOverVisual("d:/ymir work/ui/language_system/login_language/flag_%s_over.tga" % bLanguage)
			groupButtonDict[i].SetDownVisual("d:/ymir work/ui/language_system/login_language/flag_%s_down.tga" % bLanguage)
			groupButtonDict[i].SAFE_SetEvent(self.OnSelectLanguageButton, bLanguage)
			groupButtonDict[i].Show()

			self.typeButtonList.append(groupButtonDict[i])
			self.X_SPACE += self.WIDTH_FLAG
			
		self.loginLanguageBoard.SetSize(self.Y_START + (self.WIDTH_FLAG * len(groupButtonDict)) + 4, self.loginLanguageBoard.GetHeight())
		self.ClickRadioButton(self.typeButtonList, app.GetLanguageIndex(app.GetLanguage()))
		
	def ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton = buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()
		
	def OnSelectLanguageButton(self, bLanguage):
		app.SetLanguage(bLanguage)

	def SaveAccount(self):
		for i in xrange(8):
			if not get_reg("acc_%d" % i):
				if (self.idEditLine.GetText() != "") or (self.pwdEditLine.GetText() != ""):
					set_reg("acc_%d" % i, "%s|%s" % (self.idEditLine.GetText(), self.pwdEditLine.GetText()))
					self.PopupNotifyMessage("Account wurde hinzugefügt.", self.EmptyFunc)
				else:
					self.PopupNotifyMessage("Gib deine Login-ID ein.", self.EmptyFunc)
				self.CheckAccount()
				return
			else:
				self.PopupNotifyMessage("Kein Platz für weitere Accounts.", self.EmptyFunc)
				
	def OnDeleteAccount(self):
		self.deleteButton.Down()
		self.deleteButton.Disable()
		
		for i in xrange(8):
			if get_reg("acc_%d" % i):
				self.accountLabel[i][1].SetUpVisual("tbx/loginwindow/delete_0.tga")
				self.accountLabel[i][1].SetOverVisual("tbx/loginwindow/delete_1.tga")
				self.accountLabel[i][1].SetDownVisual("tbx/loginwindow/delete_2.tga")
				self.accountLabel[i][1].SetEvent(ui.__mem_func__(self.DeleteAccount), i)

	def CheckAccount(self):
		# self.accountLabel = {}
		# self.position[1] = 70
		slots = 0
		for i in xrange(8):
			if get_reg("acc_%d" % i):
				self.accountButton[i].SetText(get_reg("acc_%d" % i).split("|")[0])
				self.accountButton[i].Enable()
				self.accountDeleteButton[i].Enable()
				self.fKeyTextLine[i].Show()
				
			else:
				self.accountButton[i].SetText(localeInfo.LOGIN_EMPTY)
				self.accountButton[i].Disable()
				self.accountDeleteButton[i].Disable()	
				self.fKeyTextLine[i].Hide()
				slots = slots + 1
		# self.deleteButton.SetUp()
		# self.deleteButton.Enable()
		if slots == 0:
			self.saveButton.Disable()
		else:
			self.saveButton.Enable()

		
	def DeleteAccount(self, key):
		if get_reg("acc_%d" % key):
			set_reg("acc_%d" % key, "")
			# self.PopupNotifyMessage("Account wurde gelöscht.")
			self.CheckAccount()
		else:
			self.PopupNotifyMessage("Account kann nicht gelöscht werden.")
			
	def CreateAccount(self, i):
		image = ui.ImageBox()
		image.SetParent(self.GetChild("board"))
		image.SetPosition(85, self.position[1])
		image.LoadImage("tbx/loginwindow/slotbar_small.tga")
		image.Show()
		text = ui.TextLine()
		text.SetParent(image)
		text.SetPosition(2, 0)
		text.SetHorizontalAlignCenter()
		text.SetVerticalAlignCenter()
		text.SetWindowHorizontalAlignCenter()
		text.SetWindowVerticalAlignCenter()
		text.SetText(get_reg("acc_%d" % i).split("|")[0])
		text.Show()
		button = ui.Button()
		button.SetParent(self.GetChild("board"))
		button.SetPosition(100, self.position[1]+35)
		button.SetUpVisual("tbx/loginwindow/load_0.tga")
		button.SetOverVisual("tbx/loginwindow/load_1.tga")
		button.SetDownVisual("tbx/loginwindow/load_2.tga")
		button.SetEvent(ui.__mem_func__(self.LoadAccount), i)
		button.Show()
		
		self.position[1] += 75
		self.accountLabel[i] = (image, button, text)
				
	def CreateChannel(self, i):
		window = self.AccountButton(proxy(self), i)
		window.SetParent(self.GetChild("channel_background"))
		window.SetPosition(12, self.position[0])
		window.SetColor(0x00000000)
		window.SetSize(190, 20)
		window.Show()
		text = ui.TextLine()
		text.SetParent(window)
		text.SetPosition(0, 0)
		text.SetHorizontalAlignCenter()
		text.SetVerticalAlignCenter()
		text.SetWindowHorizontalAlignCenter()
		text.SetWindowVerticalAlignCenter()
		text.SetText("CHANNEL %d" % (i+1))
		text.Show()
		
		self.position[0] += 24
		self.channelLabel[i] = (window, text)
		
	def LoadAccount(self, i):
		self.Connect(get_reg("acc_%d" % i).split("|")[0], get_reg("acc_%d" % i).split("|")[1])

		
	def OnKeyUp(self, key):
		try:
			
			fKeyIndex = {}
			
			fKeyIndex[app.DIK_F1] = 0
			fKeyIndex[app.DIK_F2] = 1
			fKeyIndex[app.DIK_F3] = 2
			fKeyIndex[app.DIK_F4] = 3
			fKeyIndex[app.DIK_F5] = 4
			fKeyIndex[app.DIK_F6] = 5
			fKeyIndex[app.DIK_F7] = 6
			fKeyIndex[app.DIK_F8] = 7
		
			self.LoadAccount(fKeyIndex[key])

		except KeyError:
			pass
		except:
			raise

		return TRUE
		
	def SetChannel(self, ch):
		self.channelID = ch
		for i in xrange(4):
			if not self.channelID == i:
				self.channelLabel[i][0].SetColor(0x00000000)
				self.channelLabel[i][1].SetOutline(0)

		self.stream.SetConnectInfo("167.86.91.179", self.ChannelPort(ch, 0), "167.86.91.179", self.ChannelPort("LOGIN"))
		GFHhg54GHGhh45GHGH.SetMarkServer("167.86.91.179", self.ChannelPort("LOGO"))
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")
		GFHhg54GHGhh45GHGH.SetServerInfo(self.ChannelPort(ch, 2))
		
	def ChannelPort(self, ch, value=0):
		channel = {
			0	:	[10101, "|cFFDAA520|h Yunari2", "Channel 1"],
			1	:	[10201, "|cFFDAA520|h Yunari2", "Channel 2"],
			2	:	[10301, "|cFFDAA520|h Yunari2", "Channel 3"],
			3	:	[10401, "|cFFDAA520|h Yunari2", "Channel 4"]
			}
		
		if ch == "LOGIN":
			return 10508
		elif ch == "LOGO":
			return channel[0][0]
		elif value == 2:
			return "%s, %s" % (channel[ch][1], channel[ch][2])
		else:
			return channel[ch][value]
				
	def Connect(self, id, pwd):
		GFHhg54GHGhh45GHGH.ACC_ID = id
		GFHhg54GHGhh45GHGH.ACC_PWD = pwd
		
		if constInfo.SEQUENCE_PACKET_ENABLE:
			GFHhg54GHGhh45GHGH.SetPacketSequenceMode()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.EmptyFunc, localeInfo.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd)
		self.stream.Connect()
		
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func = self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def EmptyFunc(self):
		pass
		
	def OnUpdate(self):
		ServerStateChecker.Update()
		if self.channelLabel[self.channelID]:
			self.channelLabel[self.channelID][1].SetOutline(1)
			self.channelLabel[self.channelID][0].SetColor(0x307D1717)
		
		
		
		# if self.scrollAnimation == 1:
			# self.scrollStartHeight = self.scrollStartHeight - 1
			# if self.scrollStartHeight >= self.scrollEndHeight:
				# self.scrollAnimation = 0
				# self.scrollBoard.SetPosition(0,50)
			# else:
				# self.scrollBoard.SetPosition(0,self.scrollStartHeight)
			
		
		
		
	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()

		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.EmptyFunc)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.EmptyFunc)
			return

		self.Connect(id, pwd)
