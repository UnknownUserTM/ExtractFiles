import GFHhg54GHGhh45GHGH
import app
import ui
import uiOption
import uiSystemOption
import uiGameOption
import uiScriptLocale
import networkModule
import constInfo
import localeInfo
# import uianyshop
import settinginfo

SYSTEM_MENU_FOR_PORTAL = FALSE

###################################################################################################
## System
class SystemDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
	
	def __Initialize(self):
		self.eventOpenHelpWindow = None
		self.systemOptionDlg = None
		self.gameOptionDlg = None
		
		
	def LoadDialog(self):	
		if SYSTEM_MENU_FOR_PORTAL:
			self.__LoadSystemMenu_ForPortal()
		else:
			self.__LoadSystemMenu_Default()
			
	def __LoadSystemMenu_Default(self):
		pyScrLoader = ui.PythonScriptLoader()
		if constInfo.IN_GAME_SHOP_ENABLE:
			pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog.py")
		else:
			pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog.py")

		#self.chswitch = UiChannel.ChannelBoard()
		self.GetChild("system_option_button").SAFE_SetEvent(self.__ClickSystemOptionButton)
		self.GetChild("game_option_button").SAFE_SetEvent(self.__ClickGameOptionButton)
		self.GetChild("change_button").SAFE_SetEvent(self.__ClickChangeCharacterButton)
		self.GetChild("logout_button").SAFE_SetEvent(self.__ClickLogOutButton)
		self.GetChild("exit_button").SAFE_SetEvent(self.__ClickExitButton)
#		self.GetChild("help_button").SAFE_SetEvent(self.__ClickHelpButton)
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)
		self.GetChild("sofort_button").SAFE_SetEvent(self.__ClickSofortButton)
		#self.GetChild("system_chhange_button").SAFE_SetEvent(self.__ClickChangeChannelButton)
		self.GetChild("openBrowser_WikiButton").SAFE_SetEvent(self.openBrowser_WikiButton)

		self.GetChild("system_chhange_1_button").SetEvent(self.__OnClickChannelSwitch,1)
		self.GetChild("system_chhange_2_button").SetEvent(self.__OnClickChannelSwitch,2)
		self.GetChild("system_chhange_3_button").SetEvent(self.__OnClickChannelSwitch,3)
		self.GetChild("system_chhange_4_button").SetEvent(self.__OnClickChannelSwitch,4)

		
		
##		if constInfo.IN_GAME_SHOP_ENABLE:
##			self.GetChild("mall_button").SAFE_SetEvent(self.__ClickInGameShopButton)
		

	def __LoadSystemMenu_ForPortal(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog_forportal.py")

		self.GetChild("system_option_button").SAFE_SetEvent(self.__ClickSystemOptionButton)
		self.GetChild("game_option_button").SAFE_SetEvent(self.__ClickGameOptionButton)
		self.GetChild("change_button").SAFE_SetEvent(self.__ClickChangeCharacterButton)
		self.GetChild("exit_button").SAFE_SetEvent(self.__ClickExitButton)
#		self.GetChild("help_button").SAFE_SetEvent(self.__ClickHelpButton)
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)
		
	def __OnClickChannelSwitch(self,ch):
		self.Close()
		settinginfo.realChannel = int(ch)
		GFHhg54GHGhh45GHGH.SendChatPacket("/channel "+str(ch))

	def Destroy(self):
		self.ClearDictionary()
		

		
		if self.gameOptionDlg:
			self.gameOptionDlg.Destroy()
			
		if self.systemOptionDlg:
			self.systemOptionDlg.Destroy()
			
		self.__Initialize()

	def SetOpenHelpWindowEvent(self, event):
		self.eventOpenHelpWindow = event

	def OpenDialog(self):
		self.Show()

	def __ClickChangeCharacterButton(self):
		self.Close()

		GFHhg54GHGhh45GHGH.ExitGame()

	def __OnClosePopupDialog(self):
		self.popup = None		

	def __ClickLogOutButton(self):
		if SYSTEM_MENU_FOR_PORTAL: 
			if app.loggined:
				self.Close()
				GFHhg54GHGhh45GHGH.ExitApplication()
			else:
				self.Close()
				GFHhg54GHGhh45GHGH.LogOutGame()
		else:
			self.Close()
			GFHhg54GHGhh45GHGH.LogOutGame()


	def __ClickExitButton(self):
		self.Close()
		GFHhg54GHGhh45GHGH.ExitApplication()
		
	def __ClickSystemOptionButton(self):
		self.Close()

		if not self.systemOptionDlg:
			self.systemOptionDlg = uiSystemOption.OptionDialog()

		self.systemOptionDlg.Show()

	def __ClickGameOptionButton(self):
		self.Close()

		if not self.gameOptionDlg:
			self.gameOptionDlg = uiGameOption.OptionDialog()

		self.gameOptionDlg.Show()

	def __ClickSofortButton(self):
		self.Close()
		app.Exit()
		
#	def __ClickHelpButton(self):
#		self.Close()

		if None != self.eventOpenHelpWindow:
			self.eventOpenHelpWindow()

	def __ClickInGameShopButton(self):
		self.Close()

		GFHhg54GHGhh45GHGH.SendChatPacket("/in_game_mall")

	def Close(self):
		self.Hide()
		return TRUE

	def RefreshMobile(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.RefreshMobile()
		#self.optionDialog.RefreshMobile()

	def OnMobileAuthority(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnMobileAuthority()
		#self.optionDialog.OnMobileAuthority()

	def OnBlockMode(self, mode):
		uiGameOption.blockMode = mode
		if self.gameOptionDlg:
			self.gameOptionDlg.OnBlockMode(mode)
		#self.optionDialog.OnBlockMode(mode)

	def OnChangePKMode(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnChangePKMode()
		#self.optionDialog.OnChangePKMode()
	
	def OnPressExitKey(self):
		self.Close()
		return TRUE

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
	# def __ClickChangeChannelButton(self):
		# self.Close()
		# import uiChannel
		# a = uiChannel.ChannelBoard()
		# a.Show()
		
	def openBrowser_WikiButton(self):
		import os
		url="https://yunari2.net/index.php?s=vote"
		os.popen("start %s" % (url))

if __name__ == "__main__":

	import app
	import wndMgr
	import systemSetting
	import mouseModule
	import grp
	import ui
	import chr
	import background
	import fgGHGjjFHJghjfFG1545gGG

	#wndMgr.SetOutlineFlag(TRUE)

	app.SetMouseHandler(mouseModule.mouseController)
	app.SetHairColorEnable(TRUE)
	wndMgr.SetMouseHandler(mouseModule.mouseController)
	wndMgr.SetScreenSize(systemSetting.GetWidth(), systemSetting.GetHeight())
	app.Create("Yunari2", systemSetting.GetWidth(), systemSetting.GetHeight(), 1)
	mouseModule.mouseController.Create()


	wnd = SystemDialog()
	wnd.LoadDialog()
	wnd.Show()

	app.Loop()
