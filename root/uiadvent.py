import ui
import app
import fgGHGjjFHJghjfFG1545gGG as player
import item
import GFHhg54GHGhh45GHGH as net
import uiToolTip  
import wndMgr 
import grp
import constInfo
import event
import localeInfo
import mouseModule

SPAM_BLOCK_DURATION			= 3		# Spam Schutz damit nicht unnötig befehle an den Server geschickt werden.
CLOSE_ADVENT_ON_DISTANCE	= True	# Wenn True schließt sich der Adventskalender wenn sich der Spieler bewegt wie bei den Shops.
USE_ADVENT_LIMIT_RANGE		= 1000	# Je höher die Zahl umso weiter kann man sich bewegen bevor sich der Adventskalender schließt.
ENABLE_BUTTON_FLASH			= False	# Lässt den aktuellen Tag aufblinken.
ENABLE_DAY_TEXT_LINE		= True	# Zeigt den Aktuellen Tag an den Geschenken an.


class AdventWindow(ui.ScriptWindow):
	BOARD_COLOR = grp.GenerateColor(0.0, 0.0, 0.0, 0.51)
	GET_TEXT_BASE_HEIGHT = 100
	
	xAdventStart = 0
	yAdventStart = 0
	
	cday = 0
	spamBlock = 0
	cqi = 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/adventboard.py")
		except:
			import exception
			exception.Abort("AdventWindow.LoadWindow.LoadObject")

		# self.GetChild("Close_Button").SetEvent(self.Close)
		self.rewardDialog				= self.GetChild("reward_background")
		self.rewardDialogTitle			= self.GetChild("rewardTitle")
		self.rewardDialogItemName		= self.GetChild("rewardItemName")
		self.rewardDialogInfo			= self.GetChild("rewardDialogReminder")
		self.rewardDialogItemImage		= self.GetChild("rewardItemSlot")
		self.rewardDialogCloseButton 	= self.GetChild("Close_RewardDialogButton")
		i = 1
		self.adventDayButtonDict = []
		while i <= 24:
			self.adventDayButtonDict.append(self.GetChild("button_day_0" + str(i)))
			self.adventDayButtonDict[i-1].SetEvent(lambda arg=i: self.OnClickAdventButton(arg))
			self.adventDayButtonDict[i-1].ShowToolTip = lambda arg=i: self.__OverInAdventButton(arg)
			self.adventDayButtonDict[i-1].HideToolTip = lambda arg=i: self.__OverOutAdventButton()
			if ENABLE_DAY_TEXT_LINE:
				self.adventDayButtonDict[i-1].SetText(str(i))
			self.adventDayButtonDict[i-1].Hide()
			i = i + 1		
		
		self.rewardDialog.SetColor(self.BOARD_COLOR)
		self.rewardDialogItemName.SetFontColor(0.5411, 0.7254, 0.5568)
		self.rewardDialogTitle.SetFontColor(0.9490, 0.9058, 0.7568)
		self.rewardDialogCloseButton.SetEvent(self.CloseRewardDialog)
		self.toolTip = uiToolTip.ToolTip()

		# self.explodeTest = Explosion()
		# self.explodeTest.SetParent(self)
		# self.explodeTest.SetPosition(100,100)
		
		
		##################
		## DEV SPÄTER LÖSCHEN!!!
		self.Open()
		
		self.SetCurrentDay(5)
		for i in xrange(24):
			self.InitAdventButton(i+1,app.GetRandom(1,2))
		
		self.OpenRewardDialog(27001,1)
		
	def CloseRewardDialog(self):
		self.rewardDialog.Hide()
		
	def OpenRewardDialog(self,itemVnum,itemCount):
		item.SelectItem(itemVnum)
		itemName = item.GetItemName()
		
		get_text_pos = (item.GetItemSize()[1] * 20) + self.GET_TEXT_BASE_HEIGHT
		
		self.rewardDialogItemName.SetText(str(itemCount) + "x " + str(itemName))
		self.rewardDialogItemName.SetPosition(337,get_text_pos)
		self.rewardDialogInfo.SetPosition(337,get_text_pos + 20)
		self.rewardDialogCloseButton.SetPosition(679 / 2 - 48,get_text_pos+20+30)
		self.rewardDialogItemImage.LoadImage(item.GetIconImageFileName())
		self.rewardDialog.Show()

	def __OverInAdventButton(self,slot):
		self.toolTip.ClearToolTip()
		if slot == self.cday:
			self.toolTip.toolTipWidth = self.toolTip.TOOL_TIP_WIDTH + 20
			self.toolTip.AppendTextLine("Du kannst dieses Geschenk heute öffnen.",self.toolTip.POSITIVE_COLOR)
		else:
			self.toolTip.toolTipWidth = self.toolTip.TOOL_TIP_WIDTH + 60
			self.toolTip.AppendTextLine("Du kannst dieses Geschenk am " + str(slot) + ". Dezember öffnen.",self.toolTip.TITLE_COLOR)
			self.toolTip.ResizeToolTip()
		self.toolTip.ShowToolTip()
	
	def __OverOutAdventButton(self):
		self.toolTip.HideToolTip()	
	
	
	def SetCurrentDay(self,cday):
		self.cday = cday
		
	def InitAdventButton(self,index,enable):
		if index == self.cday and ENABLE_BUTTON_FLASH:
			self.adventDayButtonDict[index-1].Flash()
			
		if enable == 1:
			self.adventDayButtonDict[index-1].Enable()
		else:
			self.adventDayButtonDict[index-1].Disable()
		
		self.adventDayButtonDict[index-1].Show()
		
	def OnClickAdventButton(self,idx):
		return
	
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			return
			
		(self.xAdventStart, self.yAdventStart, z) = player.GetMainCharacterPosition()
		self.Show()

	def Close(self):
		self.rewardDialog.Hide()
		self.Hide()
		
	def OnUpdate(self):
		if CLOSE_ADVENT_ON_DISTANCE:
			USE_ADVENT_LIMIT_RANGE = 1000
			(x, y, z) = player.GetMainCharacterPosition()
			if abs(x - self.xAdventStart) > USE_ADVENT_LIMIT_RANGE or abs(y - self.yAdventStart) > USE_ADVENT_LIMIT_RANGE:
				self.Close()
				
				
# class Explosion(ui.Window):
	
	# LIFE_TIME = 0.5
	
	# def __init__(self):
		# ui.Window.__init__(self)
		# self.SetSize(20,35)
		# self.lifeTime = 0
		# self.MakeArrow()
		# self.Show()
		
	# def __del__(self):
		# ui.Window.__del__(self)

	# def MakeArrow(self):
		# self.arrow = ui.AniImageBox()
		# self.arrow.SetParent(self)
		# self.arrow.SetPosition(0,0)
		# self.arrow.SetDelay(5.0)
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/1.sub")
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/2.sub")
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/3.sub")
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/4.sub")
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/5.sub")
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/6.sub")
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/7.sub")
		# self.arrow.AppendImage("d:/ymir work/ui/explosion/8.sub")
		# self.arrow.Show()
		
		# self.lifeTime = app.GetTime() + self.LIFE_TIME
		
	# def OnUpdate(self):
		# if self.lifeTime > 0:
			# if app.GetTime() > self.lifeTime:
				# self.__del__()
		
		
		
		