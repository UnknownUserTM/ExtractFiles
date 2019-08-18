import ui
import localeInfo
import chat
import uiToolTip


def StringBoolToRealBool(boolString):
	if boolString == "true":
		return True
		
	return False
	
def SecondToDHMS(time):
	if time < 60:
		return str(int(time)) + " " + localeInfo.SECOND
		
	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:
		text += str(day) + " " + localeInfo.DAY
		text += " "

	if hour > 0:
		text += str(hour) + " " + localeInfo.HOUR
		text += " "

	if minute > 0:
		text += str(minute) + " " + localeInfo.MINUTE

	return text

class PointArrow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self)
		self.SetSize(20,35)
		
		self.MakeArrow()
		self.Show()
		
	def __del__(self):
		ui.Window.__del__(self)
		
		
	def MakeArrow(self):
		self.arrow = ui.AniImageBox()
		self.arrow.SetParent(self)
		self.arrow.SetPosition(0,0)
		self.arrow.SetDelay(10.0)
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/1.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/2.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/3.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/4.sub")
		self.arrow.AppendImage("d:/ymir work/ui/minigame/yutnori/move_arrow/5.sub")
		self.arrow.Show()

class HelpButtonWindow(ui.Window):
	
	def __init__(self):
		ui.Window.__init__(self)
		self.button = None
		self.SetSize(17,17)
		# self.MakeToolTip()
		self.MakeButton()

		
	def __del__(self):
		ui.Window.__del__(self)

	def MakeButton(self):
	
		self.toolTip = uiToolTip.ToolTip()  
		self.toolTip.HideToolTip()	
		
		self.button = ui.Button()
		self.button.SetParent(self)
		self.button.SetPosition(0,0)
		self.button.SetUpVisual("yamato_button/q_mark_01.tga")
		self.button.SetOverVisual("yamato_button/q_mark_02.tga")
		self.button.SetDownVisual("yamato_button/q_mark_02.tga")
		self.button.ShowToolTip = lambda arg=1: self.ShowToolTip(arg)
		self.button.HideToolTip = lambda arg=1: self.HideToolTip()
		self.button.Show()		
	
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "QMARK DONE!")
		# self.DefineToolTipContent("test")
	
	# def ToggleToolTipBox(self):
		# if self.toolTip.IsShow():
			# self.HideToolTip()
		# else:
			# self.ShowToolTip()
	
	
	def ShowToolTip(self,arg):
		self.toolTip.ShowToolTip()
	
	def HideToolTip(self):
		self.toolTip.HideToolTip()
		
	def DefineToolTipContent(self,localeString):
		self.toolTip.ClearToolTip()
		# self.toolTip.SetTitle("Hallo Welt!")
		self.toolTip.AppendSpace(5)
		self.toolTip.AppendDescription(localeString,26)
		self.toolTip.AppendSpace(10)
		self.toolTip.ResizeToolTip()		
	
	
	def MakeToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.Show()
		self.toolTip = toolTip
		
		
	def Destroy(self):
		self.button = None
		self.Hide()
		self.__del__()
		