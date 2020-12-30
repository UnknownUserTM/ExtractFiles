import ui
import chat
import app
import GFHhg54GHGhh45GHGH as net
import snd
import item
import fgGHGjjFHJghjfFG1545gGG as player
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import settinginfo


class ChannelTabBar(ui.Window):
	
	CH_COUNT = 4
	
	tab_buttons = {}
	
	def __init__(self):
		ui.Window.__init__(self)
		self.SetSize(32 * self.CH_COUNT,19)
		self.SetPosition(wndMgr.GetScreenWidth() - 260,0)
		self.MakeButton()
		self.Show()
				
	def __del__(self):
		ui.Window.__del__(self)	

	def MakeButton(self):
		for i in xrange(self.CH_COUNT):
			self.tab_buttons[i] = ui.Button()
			self.tab_buttons[i].SetParent(self)
			self.tab_buttons[i].SetPosition(32 * i,0)
			self.tab_buttons[i].SetUpVisual("yamato_button/tab2_pressed.tga")
			self.tab_buttons[i].SetOverVisual("yamato_button/tab2_hovered.tga")
			self.tab_buttons[i].SetDownVisual("yamato_button/tab2_passive.tga")
			self.tab_buttons[i].SetText("CH " + str(i+1))
			#self.tab_buttons[i].SetEvent(self.OpenDungeonGuide)
			self.tab_buttons[i].SetEvent(ui.__mem_func__(self.SwitchChannel), i+1)
			self.tab_buttons[i].Show()

	def SwitchChannel(self, ch):
		settinginfo.realChannel = int(ch)
		net.SendChatPacket("/channel "+str(ch))		
