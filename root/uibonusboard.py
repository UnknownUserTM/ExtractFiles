import ui
import chat
import app
import fgGHGjjFHJghjfFG1545gGG
import snd
import item
import GFHhg54GHGhh45GHGH
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo

SORT_ALL		= 0
SORT_PVP		= 1
SORT_PVM		= 2
SORT_OFFENSIVE	= 3
SORT_DEFENSIVE	= 4
SORT_OTHERS		= 5
SORT_COUNT		= 6

ATTR_WEAPON	= 0
ATTR_BODY	= 1
ATTR_WRIST	= 2
ATTR_FOOTS	= 3
ATTR_NECK	= 4
ATTR_HEAD	= 5
ATTR_SHIELD	= 6
ATTR_EAR	= 7

BONUS_NAME		= 0
BONUS_VALUE		= 1
BONUS_MAX_VALUE	= 2
BONUS_SORT_LIST	= 3

BOARD_COUNT = 16

class BonusBoardWindow(ui.ScriptWindow):
	
	def SetDefaultBonusPage(self):
	
		self.BonusBoard = [
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_ATTBONUS_HUMAN,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_CRITICAL,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			[
				localeInfo.BONUS_BOARD_BONUS_HALFHUMAN,
				item.APPLY_CRITICAL_PCT,
				0,
				[SORT_ALL,SORT_PVP,SORT_OFFENSIVE],
				[ATTR_WEAPON],
			],
			
		]
	
	
	sortPage = 0
	updateTimer = 0
	updateWait = 1
	
	curPageContent = []
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		#constInfo.CALOPEN = 1
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/bonusboard.py")
		except:
			import exception
			exception.Abort("CalenderWindow.LoadWindow.LoadObject")

		self.GetChild("TitleBar").SetCloseEvent(self.Close)
		
		self.sortButtonList = []
		self.sortButtonList.append(self.GetChild("nav_button_0"))
		self.sortButtonList.append(self.GetChild("nav_button_1"))
		self.sortButtonList.append(self.GetChild("nav_button_2"))
		self.sortButtonList.append(self.GetChild("nav_button_3"))
		self.sortButtonList.append(self.GetChild("nav_button_4"))
		self.sortButtonList.append(self.GetChild("nav_button_5"))

		self.sortButtonList[SORT_ALL].SetEvent(lambda arg=SORT_ALL: self.LoadPage(arg))
		self.sortButtonList[SORT_PVP].SetEvent(lambda arg=SORT_PVP: self.LoadPage(arg))
		self.sortButtonList[SORT_PVM].SetEvent(lambda arg=SORT_PVM: self.LoadPage(arg))
		self.sortButtonList[SORT_OFFENSIVE].SetEvent(lambda arg=SORT_OFFENSIVE: self.LoadPage(arg))
		self.sortButtonList[SORT_DEFENSIVE].SetEvent(lambda arg=SORT_DEFENSIVE: self.LoadPage(arg))
		self.sortButtonList[SORT_OTHERS].SetEvent(lambda arg=SORT_OTHERS: self.LoadPage(arg))
		
		
		self.bonusWindow			= []
		self.bonusNameTextLine		= []
		self.bonusValueTextLine		= []
		self.bonusMaxValueTextLine	= []
		self.bonusEquipedTextLine	= []
		
		for i in xrange(BOARD_COUNT):
			self.bonusWindow.append(self.GetChild("bonus_window_" + str(i)))
			self.bonusNameTextLine.append(self.GetChild("bonus_name_textline_" + str(i)))
			self.bonusValueTextLine.append(self.GetChild("bonus_value_textline_" + str(i)))
			self.bonusMaxValueTextLine.append(self.GetChild("bonus_max_value_textline_" + str(i)))
			self.bonusEquipedTextLine.append(self.GetChild("bonus_equip_textline_" + str(i)))
		
		
		self.scrollBar = self.GetChild("bonusScrollBar")
		self.scrollBar.SetScrollEvent(self.OnScroll)
		self.SetDefaultBonusPage()
		self.LoadPage(0)
		# self.Open()
		# self.eventDayImage[12].Show()
	
	
	def LoadPage(self,idx):
		self.sortPage = idx
		for i in xrange(SORT_COUNT):
			if i == idx:
				self.sortButtonList[i].Disable()
			else:
				self.sortButtonList[i].Enable()
		self.Clear()
		self.SortBonusList()
		self.InitBonusList()

		
	def SortBonusList(self):
		for i in xrange(len(self.BonusBoard)):
			if self.sortPage in self.BonusBoard[i][BONUS_SORT_LIST]:
				self.curPageContent.append(i)
			
	def InitBonusList(self):
		count = min(BOARD_COUNT,len(self.curPageContent))
		for i in xrange(count):
			bonusIndex = self.curPageContent[i]
			self.bonusNameTextLine[i].SetText(self.BonusBoard[bonusIndex][BONUS_NAME])
			self.bonusValueTextLine[i].SetText(self.CheckBonusValueByID(self.BonusBoard[bonusIndex][BONUS_VALUE]))
			self.bonusWindow[i].Show()
		
		if len(self.curPageContent) > BOARD_COUNT:

			self.scrollBar.SetPos(0)
			self.scrollBar.SetMiddleBarSize(float(BOARD_COUNT) / float(len(self.curPageContent)))
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()

		
		
		
	def OnScroll(self):
		pos = int(self.scrollBar.GetPos() * (len(self.curPageContent) - BOARD_COUNT)) ##Aktuelle Position der Scrollbar
		#self.Board.SetTitleName("Achievement-Statistik (Pos: " + str(pos) + ")")
		for i in xrange(BOARD_COUNT):
			realPos = i + pos
			if realPos < len(self.curPageContent):
				bonusIndex = self.curPageContent[realPos]
				self.bonusNameTextLine[i].SetText(self.BonusBoard[realPos][BONUS_NAME])
				self.bonusValueTextLine[i].SetText(self.CheckBonusValueByID(self.BonusBoard[realPos][BONUS_VALUE]))
				
				
	def CheckBonusValueByID(self,id):
		value = 0
		for slot in xrange(90, 101):
			for attr in xrange(0, 7):
				attr, val = fgGHGjjFHJghjfFG1545gGG.GetItemAttribute(slot, attr)
				if int(attr) == id:
					value += int(val)
		return str(value)
			
	def Clear(self):
		self.scrollBar.SetPos(0)
		self.curPageContent = []
		self.scrollBar.Hide()
		for i in xrange(BOARD_COUNT):
			self.bonusWindow[i].Hide()
			
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
		
		
	def Close(self):
		self.Hide()

