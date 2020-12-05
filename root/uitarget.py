import app
import ui
import fgGHGjjFHJghjfFG1545gGG
import GFHhg54GHGhh45GHGH
import wndMgr
import messenger
import guild
import chr
import nonplayer
import localeInfo
import constInfo
import uiChatBlock
import uiToolTip 
import settinginfo
import chat
import item
import uiToolTip

if app.ENABLE_SEND_TARGET_INFO:
	def HAS_FLAG(value, flag):
		return (value & flag) == flag
		
if app.ENABLE_VIEW_ELEMENT:
	ELEMENT_IMAGE_DIC = {1: "elect", 2: "fire", 3: "ice", 4: "wind", 5: "earth", 6 : "dark"}

# class DropBoard(ui.ThinBoard):
	
	# slotIMG = {}
	# mobName = 0
	# dropGuide_Index = 0
	# itemToolTipIndex = {}
	
	# def __init__(self):
		# ui.ThinBoard.__init__(self)
		
		# self.itemtooltip = uiToolTip.ItemToolTip()  
		# self.itemtooltip.HideToolTip()			
		# self.SetPosition(wndMgr.GetScreenWidth()/2 - 150, 50)
		# self.SetSize(300,110)
		
		
		
		
		# #self.Show()
	# def CreateSlot(self):
	
		# if len(self.slotIMG) > 0:
			# for i in xrange(len(self.slotIMG)):
				# self.slotIMG[i].Hide()
	
		# i = 0
		# width = 20
		# height = 8
		
		# dropGuideIndex = settinginfo.DropGuide_Index[self.dropGuide_Index]
		# line_count = 8 # Max. Slots in einer reihe
		# line = 0 # Slot Count
		# line_max = dropGuideIndex[0][2]
		# slot_count = line_count * line_max 
		
		# newWindowHeight = 8 + (line_max*32) + 8
		# self.SetSize(300,newWindowHeight)
		
		
		# while i < slot_count:
			
			# self.slotIMG[i] = ui.ImageBox()
			# self.slotIMG[i].SetParent(self)
			# self.slotIMG[i].SetPosition(width,height)
			# self.slotIMG[i].LoadImage("d:/ymir work/ui/public/slot_base.sub")
			# self.slotIMG[i].Show()		
		
			# i = i + 1
			# width = width + 32
			# line = line + 1
			
			# if line == line_count:
				# width = 20
				# height = height + 32
				# line = 0
		
		# self.dropGuideGridSlot = ui.GridSlotWindow()  
		# self.dropGuideGridSlot.SetParent(self)  
		# self.dropGuideGridSlot.ArrangeSlot(0,line_count,line_max,32,32,0,0)  
		# self.dropGuideGridSlot.SetPosition(20, 8)  
		# self.dropGuideGridSlot.SetOverInItemEvent(ui.__mem_func__(self.ShowToolTip))  
		# self.dropGuideGridSlot.SetOverOutItemEvent(ui.__mem_func__(self.HideToolTip))  
		# self.dropGuideGridSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.add_slot))  
		# self.dropGuideGridSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.del_slot))  
		# self.dropGuideGridSlot.Show()
		
		# aSlotsUsed = []
		# aItems = dropGuideIndex[1]
		# slot = 0
		# for i in xrange(len(aItems)):
			
			# if slot in aSlotsUsed:
				# #chat.AppendChat(chat.CHAT_TYPE_INFO, str(slot) + "Used")
				# for a in xrange(slot_count):
					# if slot in aSlotsUsed:
						# slot = slot + 1
						# continue
					# else:
						# #chat.AppendChat(chat.CHAT_TYPE_INFO, str(slot) + "Set")
						# break
					
					# #slot = slot + 1
				
				
				
			# item.SelectItem(aItems[i][0])
				
			# self.dropGuideGridSlot.ClearSlot(slot)
			# self.dropGuideGridSlot.SetItemSlot(slot, aItems[i][0], aItems[i][1])
			# self.dropGuideGridSlot.RefreshSlot()
			
			# self.itemToolTipIndex[slot] = aItems[i][0]

			# aSlotsUsed.append(slot)
			# (widthi, heighti) = item.GetItemSize()
			# #chat.AppendChat(chat.CHAT_TYPE_INFO, str(heighti))
			# if heighti == 1:
				# aSlotsUsed.append(slot)
			# elif heighti == 2:
				# aSlotsUsed.append(slot)
				# aSlotsUsed.append(slot+8)
			# elif heighti == 3:
				# aSlotsUsed.append(slot)
				# aSlotsUsed.append(slot+8)
				# aSlotsUsed.append(slot+16)
				
				# #for b in xrange(len(aSlotsUsed)):
				# #	chat.AppendChat(chat.CHAT_TYPE_INFO, str(aSlotsUsed[b]))
			
			# slot = slot + 1
				
		# #chat.AppendChat(chat.CHAT_TYPE_INFO, str(len(aSlotsUsed)))
		
		
	# def ShowToolTip(self,slot):
		# dropGuideIndex = settinginfo.DropGuide_Index[self.dropGuide_Index]
		# aItems = dropGuideIndex[1]
		
		# self.itemtooltip.ClearToolTip()
		# self.itemtooltip.AddItemData(self.itemToolTipIndex[slot], [0, 0, 0])
		# self.itemtooltip.ShowToolTip()		
		
		
		
	# def HideToolTip(self):
		# self.itemtooltip.HideToolTip()
		
	# def add_slot(self,slot):
		# return
		
	# def del_slot(self,slot):
		# return
		
	# def SetInfos(self,mobName,dropIndex):
		# self.mobName = str(mobName)
		# self.dropGuide_Index = int(dropIndex)
		# #self.mobNameTest.SetText("Name: " + str(self.mobName))
		# self.CreateSlot()
		
		
	# def Destroy(self):

			
		# self.mobName = 0
		# self.dropGuide_Index = 0
		# self.Hide()		
		
		
class TargetBoard(ui.ThinBoard):

	if app.ENABLE_SEND_TARGET_INFO:
		class InfoBoard(ui.ThinBoard):
			class ItemListBoxItem(ui.ListBoxExNew.Item):
				def __init__(self, width):
					ui.ListBoxExNew.Item.__init__(self)

					image = ui.ExpandedImageBox()
					image.SetParent(self)
					image.Show()
					self.image = image

					nameLine = ui.TextLine()
					nameLine.SetParent(self)
					nameLine.SetPosition(32 + 5, 0)
					nameLine.Show()
					self.nameLine = nameLine

					# if app.ENABLE_SEND_TARGET_INFO_EXTENDED:
					rarity = ui.TextLine()
					rarity.SetParent(self)
					rarity.SetPosition(32 + 5, 11)
					rarity.Show()
					self.rarity = rarity

					self.SetSize(width, 32 + 5)

				def LoadImage(self, image, name = None):
					self.image.LoadImage(image)
					self.SetSize(self.GetWidth(), self.image.GetHeight() + 5 * (self.image.GetHeight() / 32))
					if name != None:
						self.SetText(name)

				def SetText(self, text):
					self.nameLine.SetText(text)

				# if app.ENABLE_SEND_TARGET_INFO_EXTENDED:
				def SetRarity(self, rarity):
					if rarity <= 0:
						return

					real_rarity = rarity / 10000
					self.rarity.SetText(str(self.GetRarity(real_rarity)))

				def GetRarity(self, rarity):
					if rarity >= 100:
						return "|cFFFFFFFFGuaranteed|r"
					elif rarity < 100 and rarity >= 70:
						return "|cFFFFFFFFCommon|r"
					elif rarity < 70 and rarity >= 50:
						return "|cFF32CD32Uncommon|r"
					elif rarity < 50 and rarity >= 30:
						return "|cFF9400D3Mythic|r"
					elif rarity < 30 and rarity >= 11:
						return "|cFF1E90FFRare|r"
					elif rarity <= 10:
						return "|cFFFFD700Legendary|r"
							
					return ""

				def RefreshHeight(self):
					ui.ListBoxExNew.Item.RefreshHeight(self)
					self.image.SetRenderingRect(0.0, 0.0 - float(self.removeTop) / float(self.GetHeight()), 0.0, 0.0 - float(self.removeBottom) / float(self.GetHeight()))
					self.image.SetPosition(0, - self.removeTop)

			MAX_ITEM_COUNT = 5

			EXP_BASE_LVDELTA = [
				1,  #  -15 0
				5,  #  -14 1
				10, #  -13 2
				20, #  -12 3
				30, #  -11 4
				50, #  -10 5
				70, #  -9  6
				80, #  -8  7
				85, #  -7  8
				90, #  -6  9
				92, #  -5  10
				94, #  -4  11
				96, #  -3  12
				98, #  -2  13
				100,	#  -1  14
				100,	#  0   15
				105,	#  1   16
				110,	#  2   17
				115,	#  3   18
				120,	#  4   19
				125,	#  5   20
				130,	#  6   21
				135,	#  7   22
				140,	#  8   23
				145,	#  9   24
				150,	#  10  25
				155,	#  11  26
				160,	#  12  27
				165,	#  13  28
				170,	#  14  29
				180,	#  15  30
			]

			RACE_FLAG_TO_NAME = {
				1 << 0  : localeInfo.TARGET_INFO_RACE_ANIMAL,
				1 << 1 	: localeInfo.TARGET_INFO_RACE_UNDEAD,
				1 << 2  : localeInfo.TARGET_INFO_RACE_DEVIL,
				1 << 3  : localeInfo.TARGET_INFO_RACE_HUMAN,
				1 << 4  : localeInfo.TARGET_INFO_RACE_ORC,
				1 << 5  : localeInfo.TARGET_INFO_RACE_MILGYO,
			}

			SUB_RACE_FLAG_TO_NAME = {
				1 << 11 : localeInfo.TARGET_INFO_RACE_ELEC,
				1 << 12 : localeInfo.TARGET_INFO_RACE_FIRE,
				1 << 13 : localeInfo.TARGET_INFO_RACE_ICE,
				1 << 14 : localeInfo.TARGET_INFO_RACE_WIND,
				1 << 15 : localeInfo.TARGET_INFO_RACE_EARTH,
				1 << 16 : localeInfo.TARGET_INFO_RACE_DARK,
			}

			STONE_START_VNUM = 28030
			STONE_LAST_VNUM = 28042

			BOARD_WIDTH = 250

			def __init__(self):
				ui.ThinBoard.__init__(self)

				self.HideCorners(self.LT)
				self.HideCorners(self.RT)
				self.HideLine(self.T)

				self.race = 0
				self.hasItems = False

				self.itemTooltip = uiToolTip.ItemToolTip()
				self.itemTooltip.HideToolTip()

				self.stoneImg = None
				self.stoneVnum = None
				self.lastStoneVnum = 0
				self.nextStoneIconChange = 0

				self.SetSize(self.BOARD_WIDTH, 0)

			def __del__(self):
				ui.ThinBoard.__del__(self)

			def __UpdatePosition(self, targetBoard):
				self.SetPosition(targetBoard.GetLeft() + (targetBoard.GetWidth() - self.GetWidth()) / 2, targetBoard.GetBottom() - 17)

			def Open(self, targetBoard, race):
				self.__LoadInformation(race)

				self.SetSize(self.BOARD_WIDTH, self.yPos + 10)
				self.__UpdatePosition(targetBoard)

				self.Show()

			def Refresh(self):
				self.__LoadInformation(self.race)
				self.SetSize(self.BOARD_WIDTH, self.yPos + 10)

			def Close(self):
				self.itemTooltip.HideToolTip()
				self.Hide()

			def __LoadInformation(self, race):
				self.yPos = 7
				self.children = []
				self.race = race
				self.stoneImg = None
				self.stoneVnum = None
				self.nextStoneIconChange = 0

				self.__LoadInformation_Default(race)
				self.__LoadInformation_Race(race)
				self.__LoadInformation_Drops(race)

			def __LoadInformation_Default_GetHitRate(self, race):
				attacker_dx = nonplayer.GetMonsterDX(race)
				attacker_level = nonplayer.GetMonsterLevel(race)

				self_dx = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.DX)
				self_level = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)

				iARSrc = min(90, (attacker_dx * 4 + attacker_level * 2) / 6)
				iERSrc = min(90, (self_dx * 4 + self_level * 2) / 6)

				fAR = (float(iARSrc) + 210.0) / 300.0
				fER = (float(iERSrc) * 2 + 5) / (float(iERSrc) + 95) * 3.0 / 10.0

				return fAR - fER

			def __LoadInformation_Default(self, race):
				self.AppendSeperator()
				self.AppendTextLine(localeInfo.TARGET_INFO_MAX_HP % constInfo.NumberToPointString(nonplayer.GetMonsterMaxHP(race)))

				# calc att damage
#				monsterLevel = nonplayer.GetMonsterLevel(race)
#				fHitRate = self.__LoadInformation_Default_GetHitRate(race)
#				iDamMin, iDamMax = nonplayer.GetMonsterDamage(race)
#				iDamMin = int((iDamMin + nonplayer.GetMonsterST(race)) * 2 * fHitRate) + monsterLevel * 2
#				iDamMax = int((iDamMax + nonplayer.GetMonsterST(race)) * 2 * fHitRate) + monsterLevel * 2
#				iDef = fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.DEF_GRADE) * (100 + fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.DEF_BONUS)) / 100
#				fDamMulti = nonplayer.GetMonsterDamageMultiply(race)
#				iDamMin = int(max(0, iDamMin - iDef) * fDamMulti)
#				iDamMax = int(max(0, iDamMax - iDef) * fDamMulti)
#				if iDamMin < 1:
#					iDamMin = 1
#				if iDamMax < 5:
#					iDamMax = 5
				self.AppendTextLine("Schaden : Keine Angaben")

#				idx = min(len(self.EXP_BASE_LVDELTA) - 1, max(0, (monsterLevel + 15) - fgGHGjjFHJghjfFG1545gGG.GetStatus(fgGHGjjFHJghjfFG1545gGG.LEVEL)))
#				iExp = nonplayer.GetMonsterExp(race) * self.EXP_BASE_LVDELTA[idx] / 100
				self.AppendTextLine("Erfahrung : Keine Angaben")

			def __LoadInformation_Race(self, race):
				dwRaceFlag = nonplayer.GetMonsterRaceFlag(race)
				self.AppendSeperator()

				mainrace = ""
				subrace = ""
				for i in xrange(17):
					curFlag = 1 << i
					if HAS_FLAG(dwRaceFlag, curFlag):
						if self.RACE_FLAG_TO_NAME.has_key(curFlag):
							mainrace += self.RACE_FLAG_TO_NAME[curFlag] + ", "
						elif self.SUB_RACE_FLAG_TO_NAME.has_key(curFlag):
							subrace += self.SUB_RACE_FLAG_TO_NAME[curFlag] + ", "
				if nonplayer.IsMonsterStone(race):
					mainrace += localeInfo.TARGET_INFO_RACE_METIN + ", "
				if mainrace == "":
					mainrace = localeInfo.TARGET_INFO_NO_RACE
				else:
					mainrace = mainrace[:-2]
				if subrace == "":
					subrace = localeInfo.TARGET_INFO_NO_RACE
				else:
					subrace = subrace[:-2]

				self.AppendTextLine(localeInfo.TARGET_INFO_MAINRACE % mainrace)
				self.AppendTextLine(localeInfo.TARGET_INFO_SUBRACE % subrace)

			def __LoadInformation_Drops(self, race):
				self.AppendSeperator()

				if race in constInfo.MONSTER_INFO_DATA:
					if len(constInfo.MONSTER_INFO_DATA[race]["items"]) == 0:
						self.AppendTextLine(localeInfo.TARGET_INFO_NO_ITEM_TEXT)
					else:
						itemListBox = ui.ListBoxExNew(32 + 5, self.MAX_ITEM_COUNT)
						itemListBox.SetSize(self.GetWidth() - 15 * 2 - ui.ScrollBar.SCROLLBAR_WIDTH, (32 + 5) * self.MAX_ITEM_COUNT)
						height = 0
						for curItem in constInfo.MONSTER_INFO_DATA[race]["items"]:
							if curItem.has_key("vnum_list"):
								height += self.AppendItem(itemListBox, curItem["vnum_list"], curItem["count"])
							else:
								height += self.AppendItem(itemListBox, curItem["vnum"], curItem["count"])
						if height < itemListBox.GetHeight():
							itemListBox.SetSize(itemListBox.GetWidth(), height)
						self.AppendWindow(itemListBox, 15)
						itemListBox.SetBasePos(0)

						if len(constInfo.MONSTER_INFO_DATA[race]["items"]) > itemListBox.GetViewItemCount():
							itemScrollBar = ui.ScrollBar()
							itemScrollBar.SetParent(self)
							itemScrollBar.SetPosition(itemListBox.GetRight(), itemListBox.GetTop())
							itemScrollBar.SetScrollBarSize(32 * self.MAX_ITEM_COUNT + 5 * (self.MAX_ITEM_COUNT - 1))
							itemScrollBar.SetMiddleBarSize(float(self.MAX_ITEM_COUNT) / float(height / (32 + 5)))
							itemScrollBar.Show()
							itemListBox.SetScrollBar(itemScrollBar)
				else:
					self.AppendTextLine(localeInfo.TARGET_INFO_NO_ITEM_TEXT)

			def AppendTextLine(self, text):
				textLine = ui.TextLine()
				textLine.SetParent(self)
				textLine.SetWindowHorizontalAlignCenter()
				textLine.SetHorizontalAlignCenter()
				textLine.SetText(text)
				textLine.SetPosition(0, self.yPos)
				textLine.Show()

				self.children.append(textLine)
				self.yPos += 17

			def AppendSeperator(self):
				img = ui.ImageBox()
				img.LoadImage("d:/ymir work/ui/seperator.tga")
				self.AppendWindow(img)
				img.SetPosition(img.GetLeft(), img.GetTop() - 15)
				self.yPos -= 15

			# def AppendItem(self, listBox, vnums, count):
			def AppendItem(self, listBox, vnums, count, rarity = 0):
				if type(vnums) == int:
					vnum = vnums
				else:
					vnum = vnums[0]

				item.SelectItem(vnum)
				itemName = item.GetItemName()
				if type(vnums) != int and len(vnums) > 1:
					vnums = sorted(vnums)
					realName = itemName[:itemName.find("+")]
					if item.GetItemType() == item.ITEM_TYPE_METIN:
						realName = localeInfo.TARGET_INFO_STONE_NAME
						itemName = realName + "+0 - +4"
					else:
						itemName = realName + "+" + str(vnums[0] % 10) + " - +" + str(vnums[len(vnums) - 1] % 10)
					vnum = vnums[len(vnums) - 1]

				myItem = self.ItemListBoxItem(listBox.GetWidth())
				myItem.LoadImage(item.GetIconImageFileName())
				if count <= 1:
					myItem.SetText(itemName)
				else:
					myItem.SetText("%dx %s" % (count, itemName))
					
				# if app.ENABLE_SEND_TARGET_INFO_EXTENDED:
				myItem.SetRarity(rarity)
					
				myItem.SAFE_SetOverInEvent(self.OnShowItemTooltip, vnum)
				myItem.SAFE_SetOverOutEvent(self.OnHideItemTooltip)
				listBox.AppendItem(myItem)

				if item.GetItemType() == item.ITEM_TYPE_METIN:
					self.stoneImg = myItem
					self.stoneVnum = vnums
					self.lastStoneVnum = self.STONE_LAST_VNUM + vnums[len(vnums) - 1] % 1000 / 100 * 100

				return myItem.GetHeight()

			def OnShowItemTooltip(self, vnum):
				item.SelectItem(vnum)
				if item.GetItemType() == item.ITEM_TYPE_METIN:
					self.itemTooltip.isStone = True
					self.itemTooltip.isBook = False
					self.itemTooltip.isBook2 = False
					self.itemTooltip.SetItemToolTip(self.lastStoneVnum)
				else:
					self.itemTooltip.isStone = False
					self.itemTooltip.isBook = True
					self.itemTooltip.isBook2 = True
					self.itemTooltip.SetItemToolTip(vnum)

			def OnHideItemTooltip(self):
				self.itemTooltip.HideToolTip()

			def AppendWindow(self, wnd, x = 0, width = 0, height = 0):
				if width == 0:
					width = wnd.GetWidth()
				if height == 0:
					height = wnd.GetHeight()

				wnd.SetParent(self)
				if x == 0:
					wnd.SetPosition((self.GetWidth() - width) / 2, self.yPos)
				else:
					wnd.SetPosition(x, self.yPos)
				wnd.Show()

				self.children.append(wnd)
				self.yPos += height + 5

			def OnUpdate(self):
				if self.stoneImg != None and self.stoneVnum != None and app.GetTime() >= self.nextStoneIconChange:
					nextImg = self.lastStoneVnum + 1
					if nextImg % 100 > self.STONE_LAST_VNUM % 100:
						nextImg -= (self.STONE_LAST_VNUM - self.STONE_START_VNUM) + 1
					self.lastStoneVnum = nextImg
					self.nextStoneIconChange = app.GetTime() + 2.5

					item.SelectItem(nextImg)
					itemName = item.GetItemName()
					realName = itemName[:itemName.find("+")]
					realName = realName + "+0 - +4"
					self.stoneImg.LoadImage(item.GetIconImageFileName(), realName)

					if self.itemTooltip.IsShow() and self.itemTooltip.isStone:
						self.itemTooltip.SetItemToolTip(nextImg)

	BUTTON_NAME_LIST = ( 
		localeInfo.TARGET_BUTTON_WHISPER, 
		localeInfo.TARGET_BUTTON_EXCHANGE, 
		localeInfo.TARGET_BUTTON_FIGHT, 
		localeInfo.TARGET_BUTTON_ACCEPT_FIGHT, 
		localeInfo.TARGET_BUTTON_AVENGE, 
		localeInfo.TARGET_BUTTON_FRIEND, 
		localeInfo.TARGET_BUTTON_INVITE_PARTY, 
		localeInfo.TARGET_BUTTON_LEAVE_PARTY, 
		localeInfo.TARGET_BUTTON_EXCLUDE, 
		localeInfo.TARGET_BUTTON_INVITE_GUILD,
		localeInfo.TARGET_BUTTON_DISMOUNT,
		localeInfo.TARGET_BUTTON_EXIT_OBSERVER,
		localeInfo.TARGET_BUTTON_VIEW_EQUIPMENT,
		localeInfo.TARGET_BUTTON_REQUEST_ENTER_PARTY,
		localeInfo.TARGET_BUTTON_BUILDING_DESTROY,
		localeInfo.TARGET_BUTTON_EMOTION_ALLOW,
		localeInfo.TARGET_BUTTON_BLOCK,
		localeInfo.TARGET_BUTTON_UNBLOCK,
		"VOTE_BLOCK_CHAT",
		"Kick",
		"ChatBlock",
	)

	GRADE_NAME =	{
						nonplayer.PAWN : localeInfo.TARGET_LEVEL_PAWN,
						nonplayer.S_PAWN : localeInfo.TARGET_LEVEL_S_PAWN,
						nonplayer.KNIGHT : localeInfo.TARGET_LEVEL_KNIGHT,
						nonplayer.S_KNIGHT : localeInfo.TARGET_LEVEL_S_KNIGHT,
						nonplayer.BOSS : localeInfo.TARGET_LEVEL_BOSS,
						nonplayer.KING : localeInfo.TARGET_LEVEL_KING,
					}
	EXCHANGE_LIMIT_RANGE = 3000
	
	# DROP_GUIDE = 0
	
	def __init__(self):
		ui.ThinBoard.__init__(self)

		name = ui.TextLine()
		name.SetParent(self)
		name.SetDefaultFontName()
		name.SetOutline()
		name.Show()

		hpGauge = ui.Gauge()
		hpGauge.SetParent(self)
		hpGauge.MakeGauge(130, "red")
		hpGauge.Hide()
		
		if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
			hpDecimal = ui.TextLine()
			hpDecimal.SetParent(hpGauge)
			hpDecimal.SetDefaultFontName()
			hpDecimal.SetPosition(5, 5)
			hpDecimal.SetOutline()
			hpDecimal.Hide()
			
		hpPercenttxt = ui.TextLine()
		hpPercenttxt.SetParent(self)
		hpPercenttxt.SetPosition(150, 13)
		hpPercenttxt.SetText("")
		hpPercenttxt.SetOutline()
		hpPercenttxt.Hide()
		
		#curHPtxt = ui.TextLine()
		#curHPtxt.SetParent(self)
		#curHPtxt.SetPosition(120, 3)
		#curHPtxt.SetText("")
		#curHPtxt.SetWindowHorizontalAlignRight()
		#curHPtxt.SetHorizontalAlignCenter()
		#curHPtxt.SetDefaultFontName()
		#curHPtxt.SetOutline()
		#curHPtxt.Hide()
		
		closeButton = ui.Button()
		closeButton.SetParent(self)
		closeButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		closeButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		closeButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		closeButton.SetPosition(30, 13)
		
		# dropGuideButton = ui.Button()
		# dropGuideButton.SetParent(self)
		# dropGuideButton.SetUpVisual("locale/de/ui/interfaces/droppgui/droppgui_01.dds")
		# dropGuideButton.SetOverVisual("locale/de/ui/interfaces/droppgui/droppgui_02.dds")
		# dropGuideButton.SetDownVisual("locale/de/ui/interfaces/droppgui/droppgui_02.dds")
		# dropGuideButton.SetPosition(50, 13)
		# dropGuideButton.SetEvent(ui.__mem_func__(self.OnPressedDropGuideButton))
		# dropGuideButton.Hide()

			
		# self.sideBar = DropBoard()
		#self.sideBar.Show()	
		if localeInfo.IsARABIC():
			hpGauge.SetPosition(55, 17)
			hpGauge.SetWindowHorizontalAlignLeft()
			closeButton.SetWindowHorizontalAlignLeft()
		else:
			hpGauge.SetPosition(185, 17)
			hpGauge.SetWindowHorizontalAlignRight()
			closeButton.SetWindowHorizontalAlignRight()
		if app.ENABLE_SEND_TARGET_INFO:
			infoButton = ui.Button()
			infoButton.SetParent(self)
			infoButton.SetUpVisual("d:/ymir work/ui/pattern/q_mark_01.tga")
			infoButton.SetOverVisual("d:/ymir work/ui/pattern/q_mark_02.tga")
			infoButton.SetDownVisual("d:/ymir work/ui/pattern/q_mark_01.tga")
			infoButton.SetEvent(ui.__mem_func__(self.OnPressedInfoButton))
			infoButton.Hide()

			infoBoard = self.InfoBoard()
			infoBoard.Hide()
			infoButton.showWnd = infoBoard
			# dropGuideButton.SetWindowHorizontalAlignRight()

		closeButton.SetEvent(ui.__mem_func__(self.OnPressedCloseButton))
		closeButton.Show()

		self.buttonDict = {}
		self.showingButtonList = []
		for buttonName in self.BUTTON_NAME_LIST:
			button = ui.Button()
			button.SetParent(self)
		
			if localeInfo.IsARABIC():
				button.SetUpVisual("d:/ymir work/ui/public/Small_Button_01.sub")
				button.SetOverVisual("d:/ymir work/ui/public/Small_Button_02.sub")
				button.SetDownVisual("d:/ymir work/ui/public/Small_Button_03.sub")
			else:
				button.SetUpVisual("d:/ymir work/ui/public/small_thin_button_01.sub")
				button.SetOverVisual("d:/ymir work/ui/public/small_thin_button_02.sub")
				button.SetDownVisual("d:/ymir work/ui/public/small_thin_button_03.sub")
			
			button.SetWindowHorizontalAlignCenter()
			button.SetText(buttonName)
			button.Hide()
			self.buttonDict[buttonName] = button
			self.showingButtonList.append(button)

		self.buttonDict[localeInfo.TARGET_BUTTON_WHISPER].SetEvent(ui.__mem_func__(self.OnWhisper))
		if app.ENABLE_MESSENGER_BLOCK:
			self.buttonDict[localeInfo.TARGET_BUTTON_BLOCK].SetEvent(ui.__mem_func__(self.OnAppendToBlockMessenger))
			self.buttonDict[localeInfo.TARGET_BUTTON_UNBLOCK].SetEvent(ui.__mem_func__(self.OnRemoveToBlockMessenger))

		self.buttonDict[localeInfo.TARGET_BUTTON_EXCHANGE].SetEvent(ui.__mem_func__(self.OnExchange))
		self.buttonDict[localeInfo.TARGET_BUTTON_FIGHT].SetEvent(ui.__mem_func__(self.OnPVP))
		self.buttonDict[localeInfo.TARGET_BUTTON_ACCEPT_FIGHT].SetEvent(ui.__mem_func__(self.OnPVP))
		self.buttonDict[localeInfo.TARGET_BUTTON_AVENGE].SetEvent(ui.__mem_func__(self.OnPVP))
		self.buttonDict[localeInfo.TARGET_BUTTON_FRIEND].SetEvent(ui.__mem_func__(self.OnAppendToMessenger))
		self.buttonDict[localeInfo.TARGET_BUTTON_FRIEND].SetEvent(ui.__mem_func__(self.OnAppendToMessenger))
		self.buttonDict[localeInfo.TARGET_BUTTON_INVITE_PARTY].SetEvent(ui.__mem_func__(self.OnPartyInvite))
		self.buttonDict[localeInfo.TARGET_BUTTON_LEAVE_PARTY].SetEvent(ui.__mem_func__(self.OnPartyExit))
		self.buttonDict[localeInfo.TARGET_BUTTON_EXCLUDE].SetEvent(ui.__mem_func__(self.OnPartyRemove))

		self.buttonDict[localeInfo.TARGET_BUTTON_INVITE_GUILD].SAFE_SetEvent(self.__OnGuildAddMember)
		self.buttonDict[localeInfo.TARGET_BUTTON_DISMOUNT].SAFE_SetEvent(self.__OnDismount)
		self.buttonDict[localeInfo.TARGET_BUTTON_EXIT_OBSERVER].SAFE_SetEvent(self.__OnExitObserver)
		self.buttonDict[localeInfo.TARGET_BUTTON_VIEW_EQUIPMENT].SAFE_SetEvent(self.__OnViewEquipment)
		self.buttonDict[localeInfo.TARGET_BUTTON_REQUEST_ENTER_PARTY].SAFE_SetEvent(self.__OnRequestParty)
		self.buttonDict[localeInfo.TARGET_BUTTON_BUILDING_DESTROY].SAFE_SetEvent(self.__OnDestroyBuilding)
		self.buttonDict[localeInfo.TARGET_BUTTON_EMOTION_ALLOW].SAFE_SetEvent(self.__OnEmotionAllow)
		
		self.buttonDict["VOTE_BLOCK_CHAT"].SetEvent(ui.__mem_func__(self.__OnVoteBlockChat))
		
		self.buttonDict["Kick"].SetEvent(ui.__mem_func__(self.OnKick))
		self.buttonDict["ChatBlock"].SetEvent(ui.__mem_func__(self.OnChatBlock))

		self.name = name
		self.hpGauge = hpGauge
		if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
			self.hpDecimal = hpDecimal
		if app.ENABLE_SEND_TARGET_INFO:
			self.infoButton = infoButton
		if app.ENABLE_SEND_TARGET_INFO:
			self.vnum = 0
		self.hpPercenttxt = hpPercenttxt
		#self.curHPtxt = curHPtxt
		self.closeButton = closeButton
		# self.dropGuideButton = dropGuideButton
		self.nameString = 0
		self.nameLength = 0
		self.vid = 0
		self.eventWhisper = None
		self.isShowButton = False

		if app.ENABLE_VIEW_ELEMENT:
			self.elementImage = None
			self.itemtooltip = uiToolTip.ItemToolTip()  
			self.itemtooltip.HideToolTip()
			self.__Initialize()
			self.ResetTargetBoard()
		
		dlgChatBlock = uiChatBlock.ChatBlockDialog()
		dlgChatBlock.LoadDialog()
		dlgChatBlock.SetTitleName("ChatBlock")
		dlgChatBlock.Hide()
		self.dlgChatBlock = dlgChatBlock

	def __del__(self):
		ui.ThinBoard.__del__(self)

		print "===================================================== DESTROYED TARGET BOARD"

	def __Initialize(self):
		self.nameString = ""
		self.nameLength = 0
		self.vid = 0
		if app.ENABLE_SEND_TARGET_INFO:
			self.vnum = 0
		self.isShowButton = False
		# self.sideBar.Destroy()
	def Destroy(self):
		self.eventWhisper = None
		if app.ENABLE_SEND_TARGET_INFO:
			self.infoButton = None
		self.closeButton = None
		# self.dropGuideButton = None
		self.showingButtonList = None
		self.buttonDict = None
		self.name = None
		self.hpGauge = None
		if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
			self.hpDecimal = None
		self.hpPercenttxt = None
		self.__Initialize()
		if app.ENABLE_VIEW_ELEMENT:
			self.elementImage = None

	if app.ENABLE_SEND_TARGET_INFO:
		def RefreshMonsterInfoBoard(self):
			if not self.infoButton.showWnd.IsShow():
				return

			self.infoButton.showWnd.Refresh()

		def OnPressedInfoButton(self):
			GFHhg54GHGhh45GHGH.SendTargetInfoLoad(fgGHGjjFHJghjfFG1545gGG.GetTargetVID())
			if self.infoButton.showWnd.IsShow():
				self.infoButton.showWnd.Close()
			elif self.vnum != 0:
				self.infoButton.showWnd.Open(self, self.vnum)
		# self.sideBar.Destroy()
		# self.sideBar = None
		# self.DROP_GUIDE = 0
			# self.dlgChatBlock.Destroy()
			# self.dlgChatBlock = 0

	def OnPressedCloseButton(self):
		# self.sideBar.Destroy()
		#self.sideBar = 0
		# self.DROP_GUIDE = 0
		fgGHGjjFHJghjfFG1545gGG.ClearTarget()
		self.Close()

	def Close(self):
		self.__Initialize()
		if app.ENABLE_SEND_TARGET_INFO:
			self.infoButton.showWnd.Close()
		self.Hide()

	def Open(self, vid, name):
		if vid:
			if not constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD():
				if not fgGHGjjFHJghjfFG1545gGG.IsSameEmpire(vid):
					self.Hide()
					return

			if vid != self.GetTargetVID():
				self.ResetTargetBoard()
				self.SetTargetVID(vid)
				self.SetTargetName(name)

			if fgGHGjjFHJghjfFG1545gGG.IsMainCharacterIndex(vid):
				self.__ShowMainCharacterMenu()		
			elif chr.INSTANCE_TYPE_BUILDING == chr.GetInstanceType(self.vid):
				self.Hide()
			else:
				self.RefreshButton()
				self.Show()
		else:
			self.HideAllButton()
			self.__ShowButton(localeInfo.TARGET_BUTTON_WHISPER)
			self.__ShowButton("VOTE_BLOCK_CHAT")
			self.__ArrangeButtonPosition()
			self.SetTargetName(name)
			self.Show()
	
	# def OnPressedDropGuideButton(self):
		# if self.DROP_GUIDE == 0:
			# mobName = chr.GetNameByVID(self.vid)
			# mobHasDrop = 0
			# dropIndex = 0
			# dropGuideIndexA = settinginfo.DropGuide_Index
			# for i in xrange(len(dropGuideIndexA)):
				# if dropGuideIndexA[i][0][0] == mobName:
					# mobHasDrop = 1
					# dropIndex = i
			
			# if mobHasDrop == 0:
				# chat.AppendChat(chat.CHAT_TYPE_INFO, "Dieses Monster trägt keine Beute bei sich!")
				# return
			
			# self.sideBar.Show()
			# self.sideBar.SetInfos(mobName,dropIndex)
			# self.DROP_GUIDE = 1
		# else:
			# self.sideBar.Destroy()
			# #self.sideBar = 0
			# self.DROP_GUIDE = 0
	
	def Refresh(self):
		if self.IsShow():
			if self.IsShowButton():			
				self.RefreshButton()		

	def RefreshByVID(self, vid):
		if vid == self.GetTargetVID():			
			self.Refresh()
			
	def RefreshByName(self, name):
		if name == self.GetTargetName():
			self.Refresh()

	def __ShowMainCharacterMenu(self):
		canShow=0

		self.HideAllButton()

		if fgGHGjjFHJghjfFG1545gGG.IsMountingHorse():
			self.__ShowButton(localeInfo.TARGET_BUTTON_DISMOUNT)
			canShow=1

		if fgGHGjjFHJghjfFG1545gGG.IsObserverMode():
			self.__ShowButton(localeInfo.TARGET_BUTTON_EXIT_OBSERVER)
			canShow=1

		if canShow:
			self.__ArrangeButtonPosition()
			self.Show()
		else:
			self.Hide()
			
	def __ShowNameOnlyMenu(self):
		self.HideAllButton()

	def SetWhisperEvent(self, event):
		self.eventWhisper = event

	def UpdatePosition(self):
		self.SetPosition(wndMgr.GetScreenWidth()/2 - self.GetWidth()/2, 10)

	def ResetTargetBoard(self):

		for btn in self.buttonDict.values():
			btn.Hide()

		self.__Initialize()

		self.name.SetPosition(0, 13)
		self.name.SetHorizontalAlignCenter()
		self.name.SetWindowHorizontalAlignCenter()
		self.hpGauge.Hide()
		if app.ENABLE_VIEW_ELEMENT and self.elementImage:
			self.elementImage = None
		if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
			self.hpDecimal.Hide()
		if app.ENABLE_SEND_TARGET_INFO:
			self.infoButton.Hide()
			self.infoButton.showWnd.Close()
		self.hpPercenttxt.Hide()
		# self.dropGuideButton.Hide()
		self.SetSize(250, 40)
		# self.sideBar.Destroy()
		#self.sideBar = 0
		
		# self.DROP_GUIDE = 0

	def SetTargetVID(self, vid):
		self.vid = vid
		
		if app.ENABLE_SEND_TARGET_INFO:
			self.vnum = 0

	def SetEnemyVID(self, vid):
		self.SetTargetVID(vid)
		
		if app.ENABLE_SEND_TARGET_INFO:
			vnum = nonplayer.GetRaceNumByVID(vid)

		name = chr.GetNameByVID(vid)
		level = nonplayer.GetLevelByVID(vid)
		grade = nonplayer.GetGradeByVID(vid)

		nameFront = ""
		if -1 != level:
			nameFront += "Lv." + str(level) + " "
		if self.GRADE_NAME.has_key(grade):
			nameFront += "(" + self.GRADE_NAME[grade] + ") "

		self.SetTargetName(nameFront + name)
		
		if app.ENABLE_SEND_TARGET_INFO:
			(textWidth, textHeight) = self.name.GetTextSize()

			self.infoButton.SetPosition(textWidth + 25, 12)
			self.infoButton.SetWindowHorizontalAlignLeft()

			self.vnum = vnum
			self.infoButton.Show()

	def GetTargetVID(self):
		return self.vid

	def GetTargetName(self):
		return self.nameString

	def SetTargetName(self, name):
		self.nameString = name
		self.nameLength = len(name)
		self.name.SetText(name)

	if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
		def SetHP(self, hpPercentage, iMinHP, iMaxHP):
			if not self.hpGauge.IsShow():
				if app.ENABLE_VIEW_TARGET_PLAYER_HP:
					showingButtonCount = len(self.showingButtonList)
					if showingButtonCount > 0:
						if chr.GetInstanceType(self.vid) == chr.INSTANCE_TYPE_PLAYER:
							self.SetSize(max(150 + 75 * 3, showingButtonCount * 75), self.GetHeight())
						else:
							self.SetSize(200 + 7*self.nameLength, self.GetHeight())
					else:
						self.SetSize(230 + 7*self.nameLength, self.GetHeight())
				else:
					self.SetSize(200 + 7*self.nameLength, self.GetHeight())
				
				if localeInfo.IsARABIC():
					self.name.SetPosition( self.GetWidth()-23, 13)
				else:
					self.name.SetPosition(23, 13)
				
				self.name.SetWindowHorizontalAlignLeft()
				self.name.SetHorizontalAlignLeft()
				self.hpGauge.Show()
				self.UpdatePosition()
				
				self.hpPercenttxt.Show()
			
			self.hpGauge.SetPercentage(hpPercentage, 100)
			self.hpPercenttxt.SetText("%d%%" % (hpPercentage))
			if chr.GetInstanceType(self.vid) != chr.INSTANCE_TYPE_PLAYER:
				# self.dropGuideButton.Show()
				self.hpPercenttxt.SetWindowHorizontalAlignRight()
				self.hpPercenttxt.SetPosition(215, 13)
			else:
				self.hpPercenttxt.SetWindowHorizontalAlignRight()
				self.hpPercenttxt.SetPosition(215, 13)
			
			
			if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
				iMinHPText = '.'.join([i - 3 < 0 and str(iMinHP)[:i] or str(iMinHP)[i-3:i] for i in range(len(str(iMinHP)) % 3, len(str(iMinHP))+1, 3) if i])
				iMaxHPText = '.'.join([i - 3 < 0 and str(iMaxHP)[:i] or str(iMaxHP)[i-3:i] for i in range(len(str(iMaxHP)) % 3, len(str(iMaxHP))+1, 3) if i])
				self.hpDecimal.SetText(str(iMinHPText) + "/" + str(iMaxHPText))
				(textWidth, textHeight)=self.hpDecimal.GetTextSize()
				if localeInfo.IsARABIC():
					self.hpDecimal.SetPosition(120 / 2 + textWidth / 2, -13)
				else:
					self.hpDecimal.SetPosition(130 / 2 - textWidth / 2, -13)
				
				self.hpDecimal.Show()
	else:
		def SetHP(self, hpPercentage):
			if not self.hpGauge.IsShow():
				if app.ENABLE_VIEW_TARGET_PLAYER_HP:
					showingButtonCount = len(self.showingButtonList)
					if showingButtonCount > 0:
						if chr.GetInstanceType(self.GetTargetVID) != chr.INSTANCE_TYPE_PLAYER:
							if showingButtonCount != 1:
								self.SetSize(max(150, showingButtonCount * 75), self.GetHeight())
							else:
								self.SetSize(max(150, 2 * 75), self.GetHeight())
						else:
							self.SetSize(200 + 7*self.nameLength, self.GetHeight())
					else:
						self.SetSize(200 + 7*self.nameLength, self.GetHeight())
				else:
					self.SetSize(200 + 7*self.nameLength, self.GetHeight())

				if localeInfo.IsARABIC():
					self.name.SetPosition( self.GetWidth()-23, 13)
				else:
					self.name.SetPosition(23, 13)

				self.name.SetWindowHorizontalAlignLeft()
				self.name.SetHorizontalAlignLeft()
				self.hpGauge.Show()
				self.UpdatePosition()
				self.hpPercenttxt.SetPosition(200 + 7*self.nameLength-205, 13)
				self.hpPercenttxt.Show()
		
		
	def ShowDefaultButton(self):

		self.isShowButton = True
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_WHISPER])
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_EXCHANGE])
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_FIGHT])
		self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_EMOTION_ALLOW])
		if str(fgGHGjjFHJghjfFG1545gGG.GetName())[0] == "[":
			self.showingButtonList.append(self.buttonDict[localeInfo.TARGET_BUTTON_VIEW_EQUIPMENT]) 
		
		for button in self.showingButtonList:
			button.Show()

	def HideAllButton(self):
		self.isShowButton = False
		for button in self.showingButtonList:
			button.Hide()
		self.showingButtonList = []

	def __ShowButton(self, name):

		if not self.buttonDict.has_key(name):
			return

		self.buttonDict[name].Show()
		self.showingButtonList.append(self.buttonDict[name])

	def __HideButton(self, name):

		if not self.buttonDict.has_key(name):
			return

		button = self.buttonDict[name]
		button.Hide()

		for btnInList in self.showingButtonList:
			if btnInList == button:
				self.showingButtonList.remove(button)
				break

	def OnWhisper(self):
		# return
		if None != self.eventWhisper:
			self.eventWhisper(self.nameString)

	def OnExchange(self):
		GFHhg54GHGhh45GHGH.SendExchangeStartPacket(self.vid)

	def OnPVP(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/pvp %d" % (self.vid))

	def OnAppendToMessenger(self):
		GFHhg54GHGhh45GHGH.SendMessengerAddByVIDPacket(self.vid)
	if app.ENABLE_MESSENGER_BLOCK:
		def OnAppendToBlockMessenger(self):
			GFHhg54GHGhh45GHGH.SendMessengerAddBlockByVIDPacket(self.vid)
		def OnRemoveToBlockMessenger(self):
			messenger.RemoveBlock(constInfo.ME_KEY)
			GFHhg54GHGhh45GHGH.SendMessengerRemoveBlockPacket(constInfo.ME_KEY, chr.GetNameByVID(self.vid))
	def OnPartyInvite(self):
		GFHhg54GHGhh45GHGH.SendPartyInvitePacket(self.vid)

	def OnPartyExit(self):
		GFHhg54GHGhh45GHGH.SendPartyExitPacket()

	def OnPartyRemove(self):
		GFHhg54GHGhh45GHGH.SendPartyRemovePacket(self.vid)

	def __OnGuildAddMember(self):
		GFHhg54GHGhh45GHGH.SendGuildAddMemberPacket(self.vid)

	def __OnDismount(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/unmount")

	def __OnExitObserver(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/observer_exit")

	def __OnViewEquipment(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/view_equip " + str(self.vid))

	def __OnRequestParty(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/party_request " + str(self.vid))

	def __OnDestroyBuilding(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/build d %d" % (self.vid))

	def __OnEmotionAllow(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/emotion_allow %d" % (self.vid))
		
	def __OnVoteBlockChat(self):
		cmd = "/vote_block_chat %s" % (self.nameString)
		GFHhg54GHGhh45GHGH.SendChatPacket(cmd)

	def OnPressEscapeKey(self):
		self.OnPressedCloseButton()
		return True

	def IsShowButton(self):
		return self.isShowButton

	def RefreshButton(self):

		self.HideAllButton()

		if chr.INSTANCE_TYPE_BUILDING == chr.GetInstanceType(self.vid):
			#self.__ShowButton(localeInfo.TARGET_BUTTON_BUILDING_DESTROY)
			#self.__ArrangeButtonPosition()
			return
		
		if fgGHGjjFHJghjfFG1545gGG.IsPVPInstance(self.vid) or fgGHGjjFHJghjfFG1545gGG.IsObserverMode():
			# PVP_INFO_SIZE_BUG_FIX
			self.SetSize(200 + 7*self.nameLength, 40)
			self.UpdatePosition()
			# END_OF_PVP_INFO_SIZE_BUG_FIX			
			return	

		self.ShowDefaultButton()
		
		if str(fgGHGjjFHJghjfFG1545gGG.GetName())[0] == "[":
			self.__ShowButton("Kick")
			self.__ShowButton("ChatBlock")

		if guild.MainPlayerHasAuthority(guild.AUTH_ADD_MEMBER):
			if not guild.IsMemberByName(self.nameString):
				if 0 == chr.GetGuildID(self.vid):
					self.__ShowButton(localeInfo.TARGET_BUTTON_INVITE_GUILD)

		if not messenger.IsFriendByName(self.nameString):
			self.__ShowButton(localeInfo.TARGET_BUTTON_FRIEND)
			
		if app.ENABLE_MESSENGER_BLOCK and not str(self.nameString)[0] == "[":
			if not messenger.IsBlockByName(self.nameString):
				self.__ShowButton(localeInfo.TARGET_BUTTON_BLOCK)
				self.__HideButton(localeInfo.TARGET_BUTTON_UNBLOCK)
			else:
				self.__ShowButton(localeInfo.TARGET_BUTTON_UNBLOCK)
				self.__HideButton(localeInfo.TARGET_BUTTON_BLOCK)
				
		if fgGHGjjFHJghjfFG1545gGG.IsPartyMember(self.vid):

			self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)

			if fgGHGjjFHJghjfFG1545gGG.IsPartyLeader(self.vid):
				self.__ShowButton(localeInfo.TARGET_BUTTON_LEAVE_PARTY)
			elif fgGHGjjFHJghjfFG1545gGG.IsPartyLeader(fgGHGjjFHJghjfFG1545gGG.GetMainCharacterIndex()):
				self.__ShowButton(localeInfo.TARGET_BUTTON_EXCLUDE)

		else:
			if fgGHGjjFHJghjfFG1545gGG.IsPartyMember(fgGHGjjFHJghjfFG1545gGG.GetMainCharacterIndex()):
				if fgGHGjjFHJghjfFG1545gGG.IsPartyLeader(fgGHGjjFHJghjfFG1545gGG.GetMainCharacterIndex()):
					self.__ShowButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)
			else:
				if chr.IsPartyMember(self.vid):
					self.__ShowButton(localeInfo.TARGET_BUTTON_REQUEST_ENTER_PARTY)
				else:
					self.__ShowButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)

			if fgGHGjjFHJghjfFG1545gGG.IsRevengeInstance(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)
				self.__ShowButton(localeInfo.TARGET_BUTTON_AVENGE)
			elif fgGHGjjFHJghjfFG1545gGG.IsChallengeInstance(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)
				self.__ShowButton(localeInfo.TARGET_BUTTON_ACCEPT_FIGHT)
			elif fgGHGjjFHJghjfFG1545gGG.IsCantFightInstance(self.vid):
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)

			if not fgGHGjjFHJghjfFG1545gGG.IsSameEmpire(self.vid):
				# self.__HideButton(localeInfo.TARGET_BUTTON_INVITE_PARTY)
				self.__HideButton(localeInfo.TARGET_BUTTON_FRIEND)
				self.__HideButton(localeInfo.TARGET_BUTTON_FIGHT)

		distance = fgGHGjjFHJghjfFG1545gGG.GetCharacterDistance(self.vid)
		if distance > self.EXCHANGE_LIMIT_RANGE:
			self.__HideButton(localeInfo.TARGET_BUTTON_EXCHANGE)
			self.__ArrangeButtonPosition()

		self.__ArrangeButtonPosition()

	def __ArrangeButtonPosition(self):
		showingButtonCount = len(self.showingButtonList)
		pos = -(showingButtonCount / 2) * 68
		if 0 == showingButtonCount % 2:
			pos += 34

		for button in self.showingButtonList:
			button.SetPosition(pos, 33)
			pos += 68
		
		if app.ENABLE_VIEW_TARGET_PLAYER_HP:
			if showingButtonCount <= 2:
				self.SetSize(max(150 + 125, showingButtonCount * 75), 65)
			else:
				self.SetSize(max(150, showingButtonCount * 75), 65)
		else:
			self.SetSize(max(150, showingButtonCount * 75), 65)
		
		self.UpdatePosition()

	def OnUpdate(self):

		if self.isShowButton:

			exchangeButton = self.buttonDict[localeInfo.TARGET_BUTTON_EXCHANGE]
			distance = fgGHGjjFHJghjfFG1545gGG.GetCharacterDistance(self.vid)

			if distance < 0:
				return

			if exchangeButton.IsShow():
				if distance > self.EXCHANGE_LIMIT_RANGE:
					self.RefreshButton()

			else:
				if distance < self.EXCHANGE_LIMIT_RANGE:
					self.RefreshButton()
					
	def OnKick(self):
		GFHhg54GHGhh45GHGH.SendChatPacket("/dc " + str(chr.GetNameByVID(self.vid)))

	def OnChatBlock(self):
		if str(fgGHGjjFHJghjfFG1545gGG.GetName())[0] == "[":
			self.dlgChatBlock.SetTitleName("ChatBlock: " + str(chr.GetNameByVID(self.vid)))
			self.dlgChatBlock.Open(str(chr.GetNameByVID(self.vid)))
			
if app.ENABLE_VIEW_ELEMENT:
	def SetElementImage(self,elementId):
		try:
			if elementId > 0 and elementId in ELEMENT_IMAGE_DIC.keys():
				self.elementImage = ui.ImageBox()
				self.elementImage.SetParent(self.name)
				self.elementImage.SetPosition(-60,-12)
				self.elementImage.LoadImage("d:/ymir work/ui/game/12zi/element/%s.sub" % (ELEMENT_IMAGE_DIC[elementId]))
				self.elementImage.Show()
		except:
			pass
