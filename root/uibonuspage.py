#!/usr/bin/python
import ui
import chat
import app
import fgGHGjjFHJghjfFG1545gGG
import snd
import item
import GFHhg54GHGhh45GHGH
import uiinventory
import settinginfo
import localeInfo

class BonusBoardDialog(ui.ScriptWindow):
	# MaxBoni = { "1": 999999, "2": 9999, "3": 9999, "4": 9999, "5": 9999, "6": 9999, "7": 9999, "9": 9999, "10": 9999, "11": 9999, "12": 9999, "13": 9999, "14": 9999, "15": 9999, "16": 9999, "17": 9999, "18": 9999, "19": 9999, "20": 9999, "21": 9999, "22": 9999, "23": 9999, "24": 9999, "27": 9999, "28": 9999, "29": 9999, "30": 9999, "31": 9999, "32": 9999, "33": 9999, "34": 9999, "35": 9999, "36": 9999, "37": 9999, "38": 9999, "90": 9999, "41": 9999, "43": 9999, "44": 9999, "45": 9999, "48": 9999, "53": 9999 }
	BonusDict = ["PvP Bonus", "PvM Bonus"]
	
	
	BonusIDListe = [
	
		["", 0, 0],
		["Bewegungsgeschwindigkeit", 8, 0],
		["TP-Regeneration", 10, 32],
		["MP-Regeneration", 11, 33],
		["Vergiftungschance", 12, 37],
		["Ohnmachtschance", 13, 38],
		["Verlangsamungschance", 14, 39],
		["Kritischer Treffer", 15, 40],
		["Durchbohrender Treffer", 16, 41],
		["Stark ggn Halbmenschen", 17, 43],
		["Stark ggn Luft", 18, 44],
		["Stark ggn Erde", 19, 45],
		["Stark ggn Feuer", 20, 46],
		["Stark ggn Wasser", 22, 48],
		["TP-Absorbierung", 23, 63],
		["MP-Absorbierung", 24, 64],
		["Chance auf Manaraub", 25, 65],
		["Chance MP-Regeneration", 26, 66],
		["Nahkampf-Angriff blocken", 27, 67],
		["Pfeilangriff ausweichen", 28, 68],
		["Schwertverteidigung", 29, 69],
		["Zweihandverteidigung", 30, 70],
		["Dolchverteidigung", 31, 71],
		["Glockenverteidigung", 32, 72],
		["Fächerverteidigung", 33, 73],
		["Pfeilwiderstand", 34, 74],
		["Feuerwiderstand", 35, 75],
		["Blitzwiderstand", 36, 76],
		["Magieverteidigung", 37, 77],
		["Windverteidigung", 38, 78],
		["Wiederstand gegen Kritische Treffer", 39, 79],
		["Fluch reflektieren", 40, 80],
		["Giftwiderstand", 41, 81],
		["Chance MP wiederherzustellen", 42, 82],
		["Exp-Bonus", 43, 83],
		["Yang-Drop", 44, 84],
		["Item-Drop", 45, 85],
		["steigernde Trankwirkung", 46, 86],
		["Chance TP wiederherzustellen", 47, 87],
		["Immun gegen Ohnmacht", 48, 88],
		["Immun gegen Verlangsamung", 49, 89],
		["Immun gegen Stürzen", 50, 90],
		["APPLY_SKILL", 51, 0],["Pfeilreichweite", 52, 95],["Verteidigungswert", 54, 96],["Magischer Angriffswert", 55, 97],["Magischer Verteidigungswert", 56, 98],["", 57, 0],["Max. Ausdauer", 58, 0],["Stark gegen Monster", 63, 53],["Itemshop Angriffswert", 64, 114],["Itemshop Verteidigungswert", 65, 115],["Itemshop Exp-Bonus", 66, 116],["Itemshop Item-Bonus", 67, 117],["Itemshop Yang-Bonus", 68, 118],["APPLY_MAX_HP_PCT", 69, 119],["APPLY_MAX_SP_PCT", 70, 120],["Fertigkeitsschaden Widerstand", 73, 123],["Durchschn. Schadenswiderstand", 74, 124],["", 75, 0],["iCafe EXP-Bonus", 76, 125],["iCafe Item-Bonus", 77, 126],["Krit. Treffer Widerstand", 78, 136],["Durchb. Treffer Widerstand", 79, 137]]
	
	
	
	
	SpecialBoni = { 1: "Norm.State", 2: "Norm.State", 3: "Norm.State", 4: "Norm.State", 5: "Norm.State", 6: "Norm.State", 55: "Norm.State", 56: "Norm.State", 58: "Norm.State" }
	
	PvPOffenseBoni = [
		localeInfo.BONUS_BOARD_BONUS_HALFHUMAN, 
		localeInfo.BONUS_BOARD_BONUS_CRITICAL, 
		localeInfo.BONUS_BOARD_BONUS_PENETRATE,
		localeInfo.BONUS_BOARD_BONUS_CRIT_DEF, 
		
	]
	
	PvPDefenseBoni = [
		"Schwertverteidigung", 
		"Zweihandverteidigung", 
		"Dolchverteidigung", 
		"Glockenverteidigung", 
		"Fächerverteidigung", 
		"Pfeilwiderstand", 
		"Pfeilangriff ausweichen", 
		"Magieverteidigung", 
		"Giftwiderstand", 
		"Nahkampf-Angriff blocken"
	]
	
	PvMOffenseBoni = [
		"Stark gegen Monster", 
		"Stark ggn Wasser", 
		"Stark ggn Luft", 
		"Stark ggn Erde", 
		"Stark ggn Feuer", 
		"Ohnmachtschance", 
		"Vergiftungschance"
	]
	
	PvMDefenseBoni = [
		"Nahkampf-Angriff blocken",
		"TP-Regeneration", 
		"MP-Regeneration", 
		"TP-Absorbierung", 
		"MP-Absorbierung", 
		"Exp-Bonus", 
		"Yang-Drop", 
		"Item-Drop", 
		"Krit. Treffer Widerstand", 
		"Durchb. Treffer Widerstand"
	]

	BonusList = []
	UI = []
	
	TestSystem = 0
	ProcessTimeStamp = 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadUI()
		
		
	def __del__(self):
		settinginfo.BonusBoardOpen = 0
		ui.ScriptWindow.__del__(self)
		self.Board.Hide()
		
		#uiinventory.BPisLoaded = 0

	def LoadUI(self):
		settinginfo.BonusBoardOpen = 1
		self.Board = ui.BoardWithRoofBar()
		self.Board.SetSize(313, 400)
		self.Board.SetCenterPosition()
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		# self.Board.SetTitleName("BonusBoard")
		self.Board.SetCloseEvent(self.__del__)
		self.Board.Show()
		
		Vertical = ui.Line()
		Vertical.SetParent(self.Board)
		Vertical.SetPosition(8 + 15, 90)
		Vertical.SetSize(297, 0)
		Vertical.SetColor(CTOA("ff777777"))
		Vertical.Show()
		self.UI.append(Vertical)

		VerticalBottom = ui.Line()
		VerticalBottom.SetParent(self.Board)
		VerticalBottom.SetPosition(8 + 15, 390 + 35)
		VerticalBottom.SetSize(297, 0)
		VerticalBottom.SetColor(CTOA("ff777777"))
		VerticalBottom.Show()
		self.UI.append(VerticalBottom)
		
		x = 75
		for i in xrange(2):
			ChangeBonusDict = ui.Button()
			ChangeBonusDict.SetParent(self.Board)
			ChangeBonusDict.SetUpVisual("yamato_helpboard/normal_button_n.tga")
			ChangeBonusDict.SetOverVisual("yamato_helpboard/normal_button_h.tga")
			ChangeBonusDict.SetDownVisual("yamato_helpboard/normal_button_p.tga")
			ChangeBonusDict.SetDisableVisual("yamato_helpboard/normal_button_d.tga")
			ChangeBonusDict.SetText(self.BonusDict[i])
			ChangeBonusDict.SetPosition(x, 400 + 32)
			ChangeBonusDict.SetEvent(lambda arg = ChangeBonusDict.GetText(): self.ChangeBonusDict(arg))
			ChangeBonusDict.Show()
			x += 100
			self.UI.append(ChangeBonusDict)
		
		x = 85
		Type = ["Angriff", "Verteidigung"]
		for i in xrange(2):
			BonusDescription = ui.TextLine()
			BonusDescription.SetParent(self.Board)
			BonusDescription.SetPosition(x, 65)
			BonusDescription.SetText(str(Type[i]))
			BonusDescription.SetFontColor(1.0, 0.63, 0)
			BonusDescription.Show()			
			x += 130
			self.UI.append(BonusDescription)

		self.SetBoni(self.BonusDict[0])
		self.dict = self.BonusDict[0]
		
	def SetBoni(self, type):
		Offense = [[25, 70], [25, 100], [25, 130], [25, 160], [25, 190], [25, 220], [25, 250], [25, 280], [25, 310], [25, 340]]
		Defense = [[170, 70], [170, 100], [170, 130], [170, 160], [170, 190], [170, 220], [170, 250], [170, 280], [170, 310], [170, 340]]
		for bonus in self.BonusIDListe:
			if type == self.BonusDict[0]:
				self.CheckBonus(bonus, self.PvPOffenseBoni, Offense)
				self.CheckBonus(bonus, self.PvPDefenseBoni, Defense)
			elif type == self.BonusDict[1]:
				self.CheckBonus(bonus, self.PvMOffenseBoni, Offense)
				self.CheckBonus(bonus, self.PvMDefenseBoni, Defense)
			else:
				return
				
	def CheckBonus(self, bonus, bonuslist, offset):
		for boni in bonuslist:
			if bonus[0] == boni:
				try:
					Index = bonuslist.index(boni)
					BonusDescription = ui.TextLine()
					BonusDescription.SetParent(self.Board)
					BonusDescription.SetPosition(offset[Index][0] + 20, offset[Index][1] + 35)
					BonusDescription.SetText(str(bonus[0]))
					BonusDescription.Show()
					
					BonusSlotBar = ui.SlotBar()
					BonusSlotBar.SetParent(self.Board)
					BonusSlotBar.SetSize(115, 15)
					BonusSlotBar.SetPosition(offset[Index][0] + 20, offset[Index][1] + 15 + 35)
					BonusSlotBar.Show()
					
					BonusAttrLine = ui.TextLine()
					BonusAttrLine.SetParent(self.Board)
					BonusAttrLine.SetPosition(offset[Index][0] + 5 + 20, offset[Index][1] + 15 + 35)
					
					try:
						Type = self.SpecialBoni[bonus[1]]
						Attribute = self.EquipAttribute(bonus)
					except:
						Attribute = fgGHGjjFHJghjfFG1545gGG.GetStatus(int(bonus[2]))
					if self.TestSystem != 1:
						BonusAttrLine.SetText(str(Attribute))
						# try:
							# if int(Attribute) >= int(self.MaxBoni[str(bonus[1])]):
								# BonusAttrLine.SetFontColor(1.0, 0.63, 0)
							# else:
								# BonusAttrLine.SetFontColor(1, 1, 1)
						# except:
							# BonusAttrLine.SetFontColor(1, 1, 1)
					else:
						BonusAttrLine.SetText("Test system is active")
						BonusAttrLine.SetFontColor(0.1, 0.7, 1.0)
					
					BonusAttrLine.Show()
					self.BonusList.append([BonusDescription, BonusAttrLine, BonusSlotBar])
				except:
					pass		
				
	def EquipAttribute(self, bonus):
		value = 0
		for slot in xrange(90, 101):
			for attr in xrange(0, 7):
				attr, val = fgGHGjjFHJghjfFG1545gGG.GetItemAttribute(slot, attr)
				if int(attr) == bonus[1]:
					value += int(val)
		return int(value)

	def ChangeBonusDict(self, dict):
		self.dict = dict
		for bonus in self.BonusList:
			try:
				for array in bonus:
					array.Hide()
			except:
				pass			
		self.SetBoni(dict)
		
		# if type == self.BonusDict[0]:
			# self.UI[2].Disable()
			
			
		# else:
			
		
	def OnUpdate(self):
		import item
		if int(app.GetTime()) > int(self.ProcessTimeStamp) + 6:
			self.SetBoni(self.dict)
			self.ProcessTimeStamp = app.GetTime()

			
	def OnPressEscapeKey(self):
		self.__del__()
		return TRUE

	def OnPressExitKey(self):		
		self.__del__()
		return TRUE
			
#BonusBoardDialog().Show()
