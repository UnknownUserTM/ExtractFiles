import ui
import snd
import systemSetting
import GFHhg54GHGhh45GHGH
import chat
import app
import localeInfo
import constInfo
import chrmgr
import fgGHGjjFHJghjfFG1545gGG
import uiWhisper
import interfacemodule

#D&T-Board © Darmani Goro, 2012

class MenuDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()
		self.lastcontact = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __Initialize(self):
		self.titleBar = 0

	def Destroy(self):
		self.Hide()
		return TRUE
		
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, "uiscript/evo2board.py")
		except:
			import exception
			exception.Abort("MenuDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			self.titleBar = self.GetChild("titlebar")
			self.Gamemasta1 = self.GetChild("Gamemasta1")
			self.Gamemasta1PN = self.GetChild("Gamemasta1PN")
			self.Gamemasta2 = self.GetChild("Gamemasta2")
			self.Gamemasta2PN = self.GetChild("Gamemasta2PN")
			self.Gamemasta3 = self.GetChild("Gamemasta3")
			self.Gamemasta3PN = self.GetChild("Gamemasta3PN")
			self.Gamemasta4 = self.GetChild("Gamemasta4")
			self.Gamemasta4PN = self.GetChild("Gamemasta4PN")
			self.Gamemasta5 = self.GetChild("Gamemasta5")
			self.Gamemasta5PN = self.GetChild("Gamemasta5PN")
			self.Gamemasta6 = self.GetChild("Gamemasta6")
			self.Gamemasta6PN = self.GetChild("Gamemasta6PN")
			self.Gamemasta7 = self.GetChild("Gamemasta7")
			self.Gamemasta7PN = self.GetChild("Gamemasta7PN")
			self.Gamemasta8 = self.GetChild("Gamemasta8")
			self.Gamemasta8PN = self.GetChild("Gamemasta8PN")
			self.Gamemasta9 = self.GetChild("Gamemasta9")
			self.Gamemasta9PN = self.GetChild("Gamemasta9PN")
			self.Gamemasta10 = self.GetChild("Gamemasta10")
			self.Gamemasta10PN = self.GetChild("Gamemasta10PN")
			self.Gamemasta11 = self.GetChild("Gamemasta11")
			self.Gamemasta11PN = self.GetChild("Gamemasta11PN")
			self.Gamemasta12 = self.GetChild("Gamemasta12")
			self.Gamemasta12PN = self.GetChild("Gamemasta12PN")
			self.Gamemasta13 = self.GetChild("Gamemasta13")
			self.Gamemasta13PN = self.GetChild("Gamemasta13PN")
			self.Gamemasta14 = self.GetChild("Gamemasta14")
			self.Gamemasta14PN = self.GetChild("Gamemasta14PN")
			self.Gamemasta15 = self.GetChild("Gamemasta15")
			self.Gamemasta15PN = self.GetChild("Gamemasta15PN")
			self.Gamemasta16 = self.GetChild("Gamemasta16")
			self.Gamemasta16PN = self.GetChild("Gamemasta16PN")
			self.Aktualisieren = self.GetChild("Aktualisieren")
			self.gm1 = self.GetChild("imagegm1")
			self.gm2 = self.GetChild("imagegm2")
			self.gm3 = self.GetChild("imagegm3")
			self.gm4 = self.GetChild("imagegm4")
			self.gm5 = self.GetChild("imagegm5")
			self.gm6 = self.GetChild("imagegm6")
			self.gm7 = self.GetChild("imagegm7")
			self.gm8 = self.GetChild("imagegm8")
			self.gm9 = self.GetChild("imagegm9")
			self.gm10 = self.GetChild("imagegm10")
			self.gm11 = self.GetChild("imagegm11")
			self.gm12 = self.GetChild("imagegm12")
			self.gm13 = self.GetChild("imagegm13")
			self.gm14 = self.GetChild("imagegm14")
			self.gm15 = self.GetChild("imagegm15")
			self.gm16 = self.GetChild("imagegm16")

		except:
			import exception
			exception.Abort("MenuDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/evo2board.py")
		
		self.__Load_BindObject()

		self.SetCenterPosition()
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.Gamemasta1PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta1))
		self.Gamemasta2PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta2))
		self.Gamemasta3PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta3))
		self.Gamemasta4PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta4))
		self.Gamemasta5PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta5))
		self.Gamemasta6PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta6))
		self.Gamemasta7PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta7))
		self.Gamemasta8PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta8))
		self.Gamemasta9PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta9))
		self.Gamemasta10PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta10))
		self.Gamemasta11PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta11))
		self.Gamemasta12PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta12))
		self.Gamemasta13PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta13))
		self.Gamemasta14PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta14))
		self.Gamemasta15PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta15))
		self.Gamemasta16PN.SetEvent(ui.__mem_func__(self.OnContactGamemasta16))
		self.Aktualisieren.SetEvent(ui.__mem_func__(self.OnAktualisieren))
		
	def OnAktualisieren(self):
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		Gamemaster1 = str(constInfo.GM1Name)
		Gamemaster2 = str(constInfo.GM2Name)
		Gamemaster3 = str(constInfo.GM3Name)
		Gamemaster4 = str(constInfo.GM4Name)
		Gamemaster5 = str(constInfo.GM5Name)
		Gamemaster6 = str(constInfo.GM6Name)
		Gamemaster7 = str(constInfo.GM7Name)
		Gamemaster8 = str(constInfo.GM8Name)
		Gamemaster9 = str(constInfo.GM9Name)
		Gamemaster10 = str(constInfo.GM10Name)
		Gamemaster11 = str(constInfo.GM11Name)
		Gamemaster12 = str(constInfo.GM12Name)
		Gamemaster13 = str(constInfo.GM13Name)
		Gamemaster14 = str(constInfo.GM14Name)
		Gamemaster15 = str(constInfo.GM15Name)
		Gamemaster16 = str(constInfo.GM16Name)
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster1, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster2, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster3, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster4, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster5, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster6, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster7, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster8, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster9, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster10, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster11, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster12, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster13, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster14, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster15, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster16, "Hallo bist du online?")
		
		if constInfo.GM1Online == 1 and pname != Gamemaster1:
			self.gm1.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM1Online == 0 and pname != Gamemaster1:
			self.gm1.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM1Online == 0 or constInfo.GM1Online == 1) and pname == Gamemaster1:
			self.gm1.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM2Online == 1 and pname != Gamemaster2:
			self.gm2.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM2Online == 0 and pname != Gamemaster2:
			self.gm2.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM2Online == 0 or constInfo.GM2Online == 1) and pname == Gamemaster2:
			self.gm2.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM3Online == 1 and pname != Gamemaster3:
			self.gm3.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM3Online == 0 and pname != Gamemaster3:
			self.gm3.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM3Online == 0 or constInfo.GM3Online == 1) and pname == Gamemaster3:
			self.gm3.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM4Online == 1 and pname != Gamemaster4:
			self.gm4.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM4Online == 0 and pname != Gamemaster4:
			self.gm4.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM4Online == 0 or constInfo.GM4Online == 1) and pname == Gamemaster4:
			self.gm4.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM5Online == 1 and pname != Gamemaster5:
			self.gm5.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM5Online == 0 and pname != Gamemaster5:
			self.gm5.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM5Online == 0 or constInfo.GM5Online == 1) and pname == Gamemaster5:
			self.gm5.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM6Online == 1 and pname != Gamemaster6:
			self.gm6.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM6Online == 0 and pname != Gamemaster6:
			self.gm6.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM6Online == 0 or constInfo.GM6Online == 1) and pname == Gamemaster6:
			self.gm6.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM7Online == 1 and pname != Gamemaster7:
			self.gm7.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM7Online == 0 and pname != Gamemaster7:
			self.gm7.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM7Online == 0 or constInfo.GM7Online == 1) and pname == Gamemaster7:
			self.gm7.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM8Online == 1 and pname != Gamemaster8:
			self.gm8.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM8Online == 0 and pname != Gamemaster8:
			self.gm8.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM8Online == 0 or constInfo.GM8Online == 1) and pname == Gamemaster8:
			self.gm8.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")	
		if constInfo.GM9Online == 1 and pname != Gamemaster9:
			self.gm9.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM9Online == 0 and pname != Gamemaster9:
			self.gm9.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM9Online == 0 or constInfo.GM9Online == 1) and pname == Gamemaster9:
			self.gm9.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM10Online == 1 and pname != Gamemaster10:
			self.gm10.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM10Online == 0 and pname != Gamemaster10:
			self.gm10.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM10Online == 0 or constInfo.GM10Online == 1) and pname == Gamemaster2:
			self.gm10.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM11Online == 1 and pname != Gamemaster11:
			self.gm11.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM11Online == 0 and pname != Gamemaster11:
			self.gm11.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM11Online == 0 or constInfo.GM11Online == 1) and pname == Gamemaster11:
			self.gm11.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM12Online == 1 and pname != Gamemaster12:
			self.gm12.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM12Online == 0 and pname != Gamemaster12:
			self.gm12.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM12Online == 0 or constInfo.GM12Online == 1) and pname == Gamemaster12:
			self.gm12.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM13Online == 1 and pname != Gamemaster13:
			self.gm13.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM13Online == 0 and pname != Gamemaster13:
			self.gm13.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM13Online == 0 or constInfo.GM13Online == 1) and pname == Gamemaster13:
			self.gm13.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM14Online == 1 and pname != Gamemaster14:
			self.gm14.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM14Online == 0 and pname != Gamemaster14:
			self.gm14.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM14Online == 0 or constInfo.GM14Online == 1) and pname == Gamemaster14:
			self.gm14.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM15Online == 1 and pname != Gamemaster15:
			self.gm15.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM15Online == 0 and pname != Gamemaster15:
			self.gm15.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM15Online == 0 or constInfo.GM15Online == 1) and pname == Gamemaster15:
			self.gm15.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM16Online == 1 and pname != Gamemaster16:
			self.gm16.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM16Online == 0 and pname != Gamemaster16:
			self.gm16.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM16Online == 0 or constInfo.GM16Online == 1) and pname == Gamemaster16:
			self.gm16.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")	
		
	def OnContactGamemasta1(self):
		Gamemaster1 = str(constInfo.GM1Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 30:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte 30 Sekunden, bevor du " + Gamemaster1 + " nochmal kontaktierst!")
			return
		elif constInfo.GM1Online == 0 and pname != Gamemaster1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster1 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")	
		elif (constInfo.GM1Online == 0 or constInfo.GM1Online == 1) and pname == Gamemaster1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster1)
			chat.SetWhisperBoxSize(Gamemaster1, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster1, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
		
	def OnContactGamemasta2(self):
		Gamemaster2 = str(constInfo.GM2Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster2 + " nochmal kontaktierst!")
			return
		elif constInfo.GM2Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster2 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM2Online == 0 or constInfo.GM2Online == 1) and pname == Gamemaster2:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster2)
			chat.SetWhisperBoxSize(Gamemaster2, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster2, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()

	def OnContactGamemasta3(self):
		Gamemaster3 = str(constInfo.GM3Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster3 + " nochmal kontaktierst!")
			return
		elif constInfo.GM3Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster3 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM3Online == 0 or constInfo.GM3Online == 1) and pname == Gamemaster3:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster3)
			chat.SetWhisperBoxSize(Gamemaster3, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster3, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
		
	def OnContactGamemasta4(self):
		Gamemaster4 = str(constInfo.GM4Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster4 + " nochmal kontaktierst!")
			return
		elif constInfo.GM4Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster4 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM4Online == 0 or constInfo.GM4Online == 1) and pname == Gamemaster4:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster4)
			chat.SetWhisperBoxSize(Gamemaster4, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster4, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
	def OnContactGamemasta5(self):
		Gamemaster5 = str(constInfo.GM1Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 30:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte 30 Sekunden, bevor du " + Gamemaster5 + " nochmal kontaktierst!")
			return
		elif constInfo.GM5Online == 0 and pname != Gamemaster5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster5 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")	
		elif (constInfo.GM5Online == 0 or constInfo.GM5Online == 1) and pname == Gamemaster5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster5)
			chat.SetWhisperBoxSize(Gamemaster5, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster5, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
		
	def OnContactGamemasta6(self):
		Gamemaster6 = str(constInfo.GM6Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster2 + " nochmal kontaktierst!")
			return
		elif constInfo.GM6Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster6 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM6Online == 0 or constInfo.GM6Online == 1) and pname == Gamemaster6:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster6)
			chat.SetWhisperBoxSize(Gamemaster6, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster6, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()

	def OnContactGamemasta7(self):
		Gamemaster7 = str(constInfo.GM7Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster3 + " nochmal kontaktierst!")
			return
		elif constInfo.GM7Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster7 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM7Online == 0 or constInfo.GM7Online == 1) and pname == Gamemaster7:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster7)
			chat.SetWhisperBoxSize(Gamemaster7, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster7, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
		
	def OnContactGamemasta8(self):
		Gamemaster8 = str(constInfo.GM8Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster3 + " nochmal kontaktierst!")
			return
		elif constInfo.GM8Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster8 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM8Online == 0 or constInfo.GM3Online == 1) and pname == Gamemaster8:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster8)
			chat.SetWhisperBoxSize(Gamemaster8, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster8, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()	
		
	def OnContactGamemasta9(self):
		Gamemaster9 = str(constInfo.GM9Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 30:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte 30 Sekunden, bevor du " + Gamemaster9 + " nochmal kontaktierst!")
			return
		elif constInfo.GM9Online == 0 and pname != Gamemaster9:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster9 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")	
		elif (constInfo.GM9Online == 0 or constInfo.GM9Online == 1) and pname == Gamemaster9:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster9)
			chat.SetWhisperBoxSize(Gamemaster9, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster9, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
		
	def OnContactGamemasta10(self):
		Gamemaster10 = str(constInfo.GM10Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster10 + " nochmal kontaktierst!")
			return
		elif constInfo.GM10Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster10 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM10Online == 0 or constInfo.GM10Online == 1) and pname == Gamemaster10:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster10)
			chat.SetWhisperBoxSize(Gamemaster10, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster10, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()

	def OnContactGamemasta11(self):
		Gamemaster11 = str(constInfo.GM11Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster11 + " nochmal kontaktierst!")
			return
		elif constInfo.GM11Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster11 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM11Online == 0 or constInfo.GM11Online == 1) and pname == Gamemaster11:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster11)
			chat.SetWhisperBoxSize(Gamemaster11, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster11, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
		
	def OnContactGamemasta12(self):
		Gamemaster12 = str(constInfo.GM12Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster12 + " nochmal kontaktierst!")
			return
		elif constInfo.GM12Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster12 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM12Online == 0 or constInfo.GM12Online == 1) and pname == Gamemaster12:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster12)
			chat.SetWhisperBoxSize(Gamemaster12, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster12, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
	def OnContactGamemasta13(self):
		Gamemaster13 = str(constInfo.GM1Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 30:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte 30 Sekunden, bevor du " + Gamemaster13 + " nochmal kontaktierst!")
			return
		elif constInfo.GM13Online == 0 and pname != Gamemaster13:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster13 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")	
		elif (constInfo.GM13Online == 0 or constInfo.GM13Online == 1) and pname == Gamemaster13:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster13)
			chat.SetWhisperBoxSize(Gamemaster13, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster13, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()
		
	def OnContactGamemasta14(self):
		Gamemaster14 = str(constInfo.GM14Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster2 + " nochmal kontaktierst!")
			return
		elif constInfo.GM14Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster14 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM14Online == 0 or constInfo.GM14Online == 1) and pname == Gamemaster14:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster14)
			chat.SetWhisperBoxSize(Gamemaster14, self.GetWidth() - 140, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster14, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()

	def OnContactGamemasta15(self):
		Gamemaster15 = str(constInfo.GM15Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster3 + " nochmal kontaktierst!")
			return
		elif constInfo.GM15Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster15 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM15Online == 0 or constInfo.GM15Online == 1) and pname == Gamemaster15:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster15)
			chat.SetWhisperBoxSize(Gamemaster15, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster15, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()	
		
	def OnContactGamemasta16(self):
		Gamemaster16 = str(constInfo.GM16Name)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		if app.GetTime() < self.lastcontact + 5:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Warte bitte ein paar Sekunden, bevor du " + Gamemaster4 + " nochmal kontaktierst!")
			return
		elif constInfo.GM16Online == 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Das Teammitglied " + Gamemaster16 + " ist im Moment nicht online!")		
			chat.AppendChat(chat.CHAT_TYPE_INFO, "              bitte probiere es später wieder!")		
		elif (constInfo.GM16Online == 0 or constInfo.GM16Online == 1) and pname == Gamemaster16:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Information: Du kannst dich nicht selber anschreiben!")					
		else:
			chat.CreateWhisper(Gamemaster16)
			chat.SetWhisperBoxSize(Gamemaster16, self.GetWidth() - 60, self.GetHeight() - 90)
			GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster16, "Der Spieler " + pname + " möchte Kontakt mit ihnen aufnehmen")
		
		self.lastcontact = app.GetTime()	
		
	def Show(self):
		ui.ScriptWindow.Show(self)
		pname = fgGHGjjFHJghjfFG1545gGG.GetName()
		Gamemaster1 = str(constInfo.GM1Name)
		Gamemaster2 = str(constInfo.GM2Name)
		Gamemaster3 = str(constInfo.GM3Name)
		Gamemaster4 = str(constInfo.GM4Name)
		Gamemaster5 = str(constInfo.GM5Name)
		Gamemaster6 = str(constInfo.GM6Name)
		Gamemaster7 = str(constInfo.GM7Name)
		Gamemaster8 = str(constInfo.GM8Name)
		Gamemaster9 = str(constInfo.GM9Name)
		Gamemaster10 = str(constInfo.GM10Name)
		Gamemaster11 = str(constInfo.GM11Name)
		Gamemaster12 = str(constInfo.GM12Name)
		Gamemaster13 = str(constInfo.GM13Name)
		Gamemaster14 = str(constInfo.GM14Name)
		Gamemaster15 = str(constInfo.GM15Name)
		Gamemaster16 = str(constInfo.GM16Name)
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster1, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster2, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster3, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster4, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster5, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster6, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster7, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster8, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster9, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster10, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster11, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster12, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster13, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster14, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster15, "Hallo bist du online?")
		GFHhg54GHGhh45GHGH.SendWhisperPacket(Gamemaster16, "Hallo bist du online?")
		if constInfo.GM1Online == 1 and pname != Gamemaster1:
			self.gm1.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM1Online == 0 and pname != Gamemaster1:
			self.gm1.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM1Online == 0 or constInfo.GM1Online == 1) and pname == Gamemaster1:
			self.gm1.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM2Online == 1 and pname != Gamemaster2:
			self.gm2.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM2Online == 0 and pname != Gamemaster2:
			self.gm2.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM2Online == 0 or constInfo.GM2Online == 1) and pname == Gamemaster2:
			self.gm2.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM3Online == 1 and pname != Gamemaster3:
			self.gm3.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM3Online == 0 and pname != Gamemaster3:
			self.gm3.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM3Online == 0 or constInfo.GM3Online == 1) and pname == Gamemaster3:
			self.gm3.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM4Online == 1 and pname != Gamemaster4:
			self.gm4.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM4Online == 0 and pname != Gamemaster4:
			self.gm4.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM4Online == 0 or constInfo.GM4Online == 1) and pname == Gamemaster4:
			self.gm4.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM5Online == 1 and pname != Gamemaster5:
			self.gm5.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM5Online == 0 and pname != Gamemaster5:
			self.gm5.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM5Online == 0 or constInfo.GM5Online == 1) and pname == Gamemaster5:
			self.gm5.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM6Online == 1 and pname != Gamemaster6:
			self.gm6.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM6Online == 0 and pname != Gamemaster6:
			self.gm6.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM6Online == 0 or constInfo.GM6Online == 1) and pname == Gamemaster6:
			self.gm6.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM7Online == 1 and pname != Gamemaster7:
			self.gm7.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM7Online == 0 and pname != Gamemaster7:
			self.gm7.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM7Online == 0 or constInfo.GM3Online == 1) and pname == Gamemaster7:
			self.gm7.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM8Online == 1 and pname != Gamemaster8:
			self.gm8.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM8Online == 0 and pname != Gamemaster8:
			self.gm8.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM8Online == 0 or constInfo.GM8Online == 1) and pname == Gamemaster8:
			self.gm8.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")	
		if constInfo.GM9Online == 1 and pname != Gamemaster9:
			self.gm9.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM9Online == 0 and pname != Gamemaster9:
			self.gm9.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM9Online == 0 or constInfo.GM9Online == 1) and pname == Gamemaster9:
			self.gm9.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM10Online == 1 and pname != Gamemaster10:
			self.gm10.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM10Online == 0 and pname != Gamemaster10:
			self.gm10.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM10Online == 0 or constInfo.GM10Online == 1) and pname == Gamemaster10:
			self.gm10.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM11Online == 1 and pname != Gamemaster11:
			self.gm11.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM11Online == 0 and pname != Gamemaster11:
			self.gm11.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM11Online == 0 or constInfo.GM11Online == 1) and pname == Gamemaster11:
			self.gm11.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM12Online == 1 and pname != Gamemaster12:
			self.gm12.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM12Online == 0 and pname != Gamemaster12:
			self.gm12.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM12Online == 0 or constInfo.GM12Online == 1) and pname == Gamemaster12:
			self.gm12.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM13Online == 1 and pname != Gamemaster13:
			self.gm13.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM13Online == 0 and pname != Gamemaster13:
			self.gm13.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM13Online == 0 or constInfo.GM13Online == 1) and pname == Gamemaster13:
			self.gm13.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM14Online == 1 and pname != Gamemaster14:
			self.gm14.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM14Online == 0 and pname != Gamemaster14:
			self.gm14.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM14Online == 0 or constInfo.GM14Online == 1) and pname == Gamemaster14:
			self.gm14.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM15Online == 1 and pname != Gamemaster15:
			self.gm15.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM15Online == 0 and pname != Gamemaster15:
			self.gm15.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")
		elif (constInfo.GM15Online == 0 or constInfo.GM3Online == 1) and pname == Gamemaster15:
			self.gm15.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		if constInfo.GM16Online == 1 and pname != Gamemaster16:
			self.gm16.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")
		elif constInfo.GM16Online == 0 and pname != Gamemaster16:
			self.gm16.LoadImage("d:/ymir work/ui/game/windows/messenger_list_offline.sub")			
		elif (constInfo.GM16Online == 0 or constInfo.GM16Online == 1) and pname == Gamemaster16:
			self.gm16.LoadImage("d:/ymir work/ui/game/windows/messenger_list_online.sub")		
		self.Gamemasta1.SetText(Gamemaster1)
		self.Gamemasta2.SetText(Gamemaster2)
		self.Gamemasta3.SetText(Gamemaster3)
		self.Gamemasta4.SetText(Gamemaster4)
		self.Gamemasta5.SetText(Gamemaster5)
		self.Gamemasta6.SetText(Gamemaster6)
		self.Gamemasta7.SetText(Gamemaster7)
		self.Gamemasta8.SetText(Gamemaster8)
		self.Gamemasta9.SetText(Gamemaster9)
		self.Gamemasta10.SetText(Gamemaster10)
		self.Gamemasta11.SetText(Gamemaster11)
		self.Gamemasta12.SetText(Gamemaster12)
		self.Gamemasta13.SetText(Gamemaster13)
		self.Gamemasta14.SetText(Gamemaster14)
		self.Gamemasta15.SetText(Gamemaster15)
		self.Gamemasta16.SetText(Gamemaster16)
	
	def OnPressEscapeKey(self):
		self.Hide()
		return TRUE
		
	def Close(self):
		self.Hide()
		return TRUE
