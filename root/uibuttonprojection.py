import ui
import snd
import shop
import mouseModule
import fgGHGjjFHJghjfFG1545gGG
import chr
import GFHhg54GHGhh45GHGH
import uiCommon
import localeInfo
import chat
import item
import systemSetting #김준호
import fgGHGjjFHJghjfFG1545gGG #김준호
import constInfo


class ButtonProjection(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self)
		self.vid = None
		self.MakeButton()
		
	def __del__(self):
		ui.Window.__del__(self)
		
		
	def MakeButton(self):
		self.button = ui.Button()
		self.button.SetParent(self)
		self.button.SetPosition(0,0)
		self.button.SetUpVisual("yamato_questboard/quest_icon.tga")
		self.button.SetOverVisual("yamato_questboard/quest_icon.tga")
		self.button.SetDownVisual("yamato_questboard/quest_icon.tga")
		self.button.SetEvent(self.OnClickQuestButton)
		self.button.Show()		
		
	def Open(self,vid):
		self.vid = vid
		self.Show()
		self.SetSize(60,117)
		chat.AppendChat(chat.CHAT_TYPE_INFO, "[BUTTON-Projection] vid: " + str(self.vid))

	def OnClickQuestButton(self):
		if not self.vid:
			return
		GFHhg54GHGhh45GHGH.SendOnClickPacket(self.vid)
		
		return True
		
	def OnUpdate(self):
		if not self.vid:
			return

		self.Show()
		x, y = chr.GetProjectPosition(self.vid, 220)
		self.SetPosition(x - self.GetWidth()/2, y - self.GetHeight()/2)
		
	def Destroy(self):
		self.vid = None
		self.button = None
		self.Hide()
		self.__del__()
		