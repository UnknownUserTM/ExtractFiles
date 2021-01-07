import ui
import uiScriptLocale
import app
import GFHhg54GHGhh45GHGH as net
import dbg
import snd
import fgGHGjjFHJghjfFG1545gGG as player
import mouseModule
import wndMgr
import skill
import playerSettingModule
import quest
import localeInfo
import uiToolTip
import constInfo
import emotion
import chr
import chat
import achievementproto
import nonplayer
import guild

SHOW_ONLY_ACTIVE_SKILL = False
SHOW_LIMIT_SUPPORT_SKILL_LIST = []
HIDE_SUPPORT_SKILL_POINT = False

if localeInfo.IsYMIR():
	SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 124, 126, 127, 129, 128, 131, 137, 138, 139, 140,141,142]
	if not localeInfo.IsCHEONMA():
		HIDE_SUPPORT_SKILL_POINT = True 
		SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 124, 126, 127, 129, 128, 131, 137, 138, 139, 140,141,142]
elif localeInfo.IsJAPAN() or   (localeInfo.IsEUROPE() and app.GetLocalePath() != "locale/ca") and (localeInfo.IsEUROPE() and app.GetLocalePath() != "locale/br"):
	HIDE_SUPPORT_SKILL_POINT = True	
	# SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 124, 126, 127, 129, 128, 131, 137, 138, 139, 140]
	SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 137, 138, 139, 140]
else:
	HIDE_SUPPORT_SKILL_POINT = True

FACE_IMAGE_DICT = {
	playerSettingModule.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
	playerSettingModule.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
	playerSettingModule.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
	playerSettingModule.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
	playerSettingModule.RACE_SURA_M		: "icon/face/sura_m.tga",
	playerSettingModule.RACE_SURA_W		: "icon/face/sura_w.tga",
	playerSettingModule.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
	playerSettingModule.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
}

BONUS_ATTR_WEAPON = 0
BONUS_ATTR_BODY = 1
BONUS_ATTR_WRIST = 2
BONUS_ATTR_FOOTS = 3
BONUS_ATTR_NECK = 4
BONUS_ATTR_HEAD = 5
BONUS_ATTR_SHIELD = 6
BONUS_ATTR_EAR = 7

BONUS_ATTR_TRANSLATE_LIST = {
	BONUS_ATTR_WEAPON : "Waffen",
	BONUS_ATTR_BODY 	: "Rustungen",
	BONUS_ATTR_WRIST 	: "Armbander",
	BONUS_ATTR_FOOTS 	: "Fuße",
	BONUS_ATTR_NECK 	: "Halsketten",
	BONUS_ATTR_HEAD 	: "Kopfe",
	BONUS_ATTR_SHIELD 	: "Schilder",
	BONUS_ATTR_EAR 	: "Ohren",
	

}

BONUS_ATTR_SLOT_LIST = {
	BONUS_ATTR_WEAPON	: 184,
	BONUS_ATTR_BODY 	: 180,
	BONUS_ATTR_WRIST 	: 183,
	BONUS_ATTR_FOOTS 	: 182,
	BONUS_ATTR_NECK 	: 185,
	BONUS_ATTR_HEAD 	: 181,
	BONUS_ATTR_SHIELD 	: 190,
	BONUS_ATTR_EAR 		: 186,
	

}

BONUS_BOARD_ITEM_LIST = [
	{
		"type" : "title",
		"text" : "Offensive Boni",
	
	},
	

	{
		"type" : "bonus",
		"text" : "Vitalitat",
		
		"bonus" : player.HT,
		
		"applicable_to" : [BONUS_ATTR_WEAPON,BONUS_ATTR_BODY],
	},
	{
		"type" : "bonus",
		"text" : "Intelligenz",
		
		"bonus" : player.IQ,
		
		"applicable_to" : [],
	},
	{
		"type" : "bonus",
		"text" : "Starke",
		
		"bonus" : player.ST,
		"applicable_to" : [],
	},
	{
		"type" : "bonus",
		"text" : "Beweglichkeit",
		
		"bonus" : player.DX,
		"applicable_to" : [],
	},


	{
		"type" : "bonus",
		"text" : "Krit. Trefferchance",
		
		"bonus" : player.POINT_CRITICAL_PCT,
		"applicable_to" : [],
	},
	{
		"type" : "bonus",
		"text" : "Durchb. Trefferchance",
		
		"bonus" : player.POINT_PENETRATE_PCT,
		"applicable_to" : [],
	},	
	
	{
		"type" : "bonus",
		"text" : "Stark gegen Menschen",
		
		"bonus" : player.POINT_ATTBONUS_HUMAN,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Tiere",
		
		"bonus" : player.POINT_ATTBONUS_ANIMAL,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Orkse",
		
		"bonus" : player.POINT_ATTBONUS_ORC,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Esotypen",
		
		"bonus" : player.POINT_ATTBONUS_MILGYO,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Untote",
		
		"bonus" : player.POINT_ATTBONUS_UNDEAD,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Teufel",
		
		"bonus" : player.POINT_ATTBONUS_DEVIL,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Insekten?? Gibts das?",
		
		"bonus" : player.POINT_ATTBONUS_INSECT,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Metinsteine",
		
		"bonus" : player.POINT_ATTBONUS_STONE,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Stark gegen Bosse",
		
		"bonus" : player.POINT_ATTBONUS_BOSS,
		"applicable_to" : [],
	},
	{
		"type" : "bonus",
		"text" : "Stark gegen Spieler",
		
		"bonus" : player.POINT_ATTBONUS_PLAYER,
		"applicable_to" : [],
	},	
	{
		"type" : "title",
		"text" : "Defensive Boni",
	
	},


	{
		"type" : "bonus",
		"text" : "Schwrtwiderstand",
		
		"bonus" : player.POINT_RESIST_SWORD,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Zweihandwiderstand",
		
		"bonus" : player.POINT_RESIST_TWOHAND,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Dolchwiderstand",
		
		"bonus" : player.POINT_RESIST_DAGGER,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Glockendef",
		
		"bonus" : player.POINT_RESIST_BELL,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Fan Def? ",
		
		"bonus" : player.POINT_RESIST_FAN,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Bogenwiderstand",
		
		"bonus" : player.POINT_RESIST_BOW,
		"applicable_to" : [],
	},	

	
	{
		"type" : "bonus",
		"text" : "Spielzeit",
		
		"bonus" : player.PLAYTIME,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "Bogendistanz",
		
		"bonus" : player.BOW_DISTANCE,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "TP-Regeneration",
		
		"bonus" : player.HP_RECOVERY,
		"applicable_to" : [],
	},	
	{
		"type" : "bonus",
		"text" : "MP-Regeneration",
		
		"bonus" : player.SP_RECOVERY,
		"applicable_to" : [],
	},
	{
		"type" : "title",
		"text" : "Passive Boni",
	
	},
	{
		"type" : "bonus",
		"text" : "Goooold!!!",
		
		"bonus" : player.ELK,
		"applicable_to" : [],
	},
	{
		"type" : "bonus",
		"text" : "Spielerlevel",
		
		"bonus" : player.LEVEL,
		"applicable_to" : [],
	},
]



def unsigned32(n):
	return n & 0xFFFFFFFFL
	
class CharacterWindow(ui.ScriptWindow):

	ACTIVE_PAGE_SLOT_COUNT = 8
	SUPPORT_PAGE_SLOT_COUNT = 12

	PAGE_SLOT_COUNT = 12
	PAGE_HORSE = 2

	SKILL_GROUP_NAME_DICT = {
		playerSettingModule.JOB_WARRIOR	: { 1 : localeInfo.SKILL_GROUP_WARRIOR_1,	2 : localeInfo.SKILL_GROUP_WARRIOR_2, },
		playerSettingModule.JOB_ASSASSIN	: { 1 : localeInfo.SKILL_GROUP_ASSASSIN_1,	2 : localeInfo.SKILL_GROUP_ASSASSIN_2, },
		playerSettingModule.JOB_SURA		: { 1 : localeInfo.SKILL_GROUP_SURA_1,		2 : localeInfo.SKILL_GROUP_SURA_2, },
		playerSettingModule.JOB_SHAMAN		: { 1 : localeInfo.SKILL_GROUP_SHAMAN_1,	2 : localeInfo.SKILL_GROUP_SHAMAN_2, },
	}

	STAT_DESCRIPTION =	{
		"HTH" : localeInfo.STAT_TOOLTIP_CON,
		"INT" : localeInfo.STAT_TOOLTIP_INT,
		"STR" : localeInfo.STAT_TOOLTIP_STR,
		"DEX" : localeInfo.STAT_TOOLTIP_DEX,
	}


	STAT_MINUS_DESCRIPTION = localeInfo.STAT_MINUS_DESCRIPTION

	def __init__(self, interface):
		ui.ScriptWindow.__init__(self)
		self.state = "STATUS"
		self.isLoaded = 0
		self.interface = interface
		self.toolTipSkill = 0
				
		self.__Initialize()
		self.__LoadWindow()

		self.statusPlusCommandDict={
			"HTH" : "/stat_val ht ",
			"INT" : "/stat_val iq ",
			"STR" : "/stat_val st ",
			"DEX" : "/stat_val dx ",
		}

		self.statusMinusCommandDict={
			"HTH-" : "/stat- ht",
			"INT-" : "/stat- iq",
			"STR-" : "/stat- st",
			"DEX-" : "/stat- dx",
		}

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __Initialize(self):
		self.refreshToolTip = 0
		self.curSelectedSkillGroup = 0
		self.canUseHorseSkill = -1

		self.toolTip = None
		self.toolTipJob = None
		self.toolTipAlignment = None
		self.toolTipSkill = None

		self.faceImage = None
		# self.statusPlusLabel = None
		self.statusPlusValue = None
		self.activeSlot = None
		self.tabDict = None
		self.tabButtonDict = None
		self.pageDict = None
		self.titleBarDict = None
		self.statusPlusButtonDict = None
		# self.statusMinusButtonDict = None

		self.skillPageDict = None
		self.questShowingStartIndex = 0
		self.questScrollBar = None
		self.questSlot = None
		self.questNameList = None
		self.questLastTimeList = None
		self.questLastCountList = None
		self.skillGroupButton = ()

		self.activeSlot = None
		self.activeSkillPointValue = None
		self.supportSkillPointValue = None
		self.skillGroupButton1 = None
		self.skillGroupButton2 = None
		self.activeSkillGroupName = None

		self.guildNameSlot = None
		self.guildNameValue = None
		self.characterNameSlot = None
		self.characterNameValue = None

		self.emotionToolTip = None
		self.soloEmotionSlot = None
		self.dualEmotionSlot = None
		
		self.bonusItemList = {}
		self.skillUPMSpamBlock = 0
		
	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

	def __LoadScript(self, fileName):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, fileName)	
		
	def __BindObject(self):
		self.toolTip = uiToolTip.ToolTip()
		self.toolTipJob = uiToolTip.ToolTip()
		self.toolTipAlignment = uiToolTip.ToolTip(130)		
		self.toolTipGuild = uiToolTip.ToolTip()

		self.faceImage = self.GetChild("Face_Image")
		self.titleBar = self.GetChild("TitleBar")
		self.titleBar.SetCloseEvent(self.Hide)
		# faceSlot=self.GetChild("Face_Slot")
		# if 949 == app.GetDefaultCodePage():
			# faceSlot.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowJobToolTip)
			# faceSlot.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideJobToolTip)

		# self.statusPlusLabel = self.GetChild("Status_Plus_Label")
		self.statusPlusValue = self.GetChild("statusPointsValueTextLine")		

		self.characterNameSlot = self.GetChild("characterNameBackground")			
		self.characterNameValue = self.GetChild("characterNameTextLine")
		self.guildNameSlot = self.GetChild("guildNameBackground")
		self.guildNameSlot.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowGuildToolTip)
		self.guildNameSlot.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideGuildToolTip)
		self.guildNameSlot.SetOnClickEvent(self.OpenGuildWindow)
		self.guildNameValue = self.GetChild("guildNameTextLine")
		self.alignmentNameSlot = self.GetChild("rankNameBackground")
		self.alignmentNameValue = self.GetChild("rankNameTextLine")
		self.alignmentNameSlot.SAFE_SetStringEvent("MOUSE_OVER_IN", self.__ShowAlignmentToolTip)
		self.alignmentNameSlot.SAFE_SetStringEvent("MOUSE_OVER_OUT", self.__HideAlignmentToolTip)

		self.activeSlot = self.GetChild("Skill_Active_Slot")
		self.activeSkillPointValue = self.GetChild("Active_Skill_Point_Value")
		self.supportSkillPointValue = self.GetChild("Support_Skill_Point_Value")
		self.skillGroupButton1 = self.GetChild("Skill_Group_Button_1")
		self.skillGroupButton2 = self.GetChild("Skill_Group_Button_2")
		self.activeSkillGroupName = self.GetChild("Active_Skill_Group_Name")
		self.GetChild("Quest_Page").Hide()
		
		# self.achievementNavigationBoard = self.GetChild("apNavigationBackground")
		# self.achievementNavigationBoard.Hide()
		
		# self.achievementNavigationListBox = self.GetChild("apNavigationListBox")
		# self.achievementNavigationScrollBar = self.GetChild("apScrollBar")
		
		# self.achievementNavigationMaxItem = 6
		
		# self.achievementNavigationListBox.InsertItem(0,"Bosse")
		# self.achievementNavigationListBox.InsertItem(1,"Metins")
		# self.achievementNavigationListBox.InsertItem(2,"Dungeons")
		# self.achievementNavigationListBox.InsertItem(3,"Level")
		# self.achievementNavigationListBox.InsertItem(4,"Verbesserungen")
		# self.achievementNavigationListBox.InsertItem(5,"Einmalige")
		# self.achievementNavigationListBox.InsertItem(6,"Sonstige")
		
		# self.tabDict = {
			# "STATUS"	: self.GetChild("Tab_01"),
			# "SKILL"		: self.GetChild("Tab_02"),
			# "EMOTICON"	: self.GetChild("Tab_03"),
			# "QUEST"		: self.GetChild("Tab_04"),
		# }
		
		# self.oldCharacterPage = self.GetChild("Character_Page")
		# self.oldCharacterPage.Hide()
		
		self.tabButtonDict = {
			"STATUS"	: self.GetChild("nav_button_0"),
			"SKILL"		: self.GetChild("nav_button_1"),
			"EMOTICON"	: self.GetChild("nav_button_2"),
			"ACHIEVEMENT" : self.GetChild("nav_button_3"),
			"BONUS" 	: self.GetChild("nav_button_4"),
			"MOUNT" 	: self.GetChild("nav_button_5"),
			# "QUEST"		: self.GetChild("Tab_Button_04")
		}
		
		# self.tabButtonDict["QUEST"].Hide()

		self.pageDict = {
			"STATUS"	: self.GetChild("Character_Page_NEW"),
			"SKILL"		: self.GetChild("Skill_Page"),
			"EMOTICON"	: self.GetChild("Emoticon_Page"),
			"ACHIEVEMENT" : self.GetChild("Achievement_Page"),
			"BONUS"		: self.GetChild("Bonus_Page"),
			"MOUNT"		: self.GetChild("Mount_Page"),
			# "QUEST"		: self.GetChild("Quest_Page")
		}

		# self.titleBarDict = {
			# "STATUS"	: self.GetChild("Character_TitleBar"),
			# "SKILL"		: self.GetChild("Skill_TitleBar"),
			# "EMOTICON"	: self.GetChild("Emoticon_TitleBar"),
			# "QUEST"		: self.GetChild("Quest_TitleBar")
		# }

		self.statusPlusButtonDict = {
			"HTH"		: self.GetChild("statusPointsVITButton"),
			"INT"		: self.GetChild("statusPointsINTButton"),
			"STR"		: self.GetChild("statusPointsSTRButton"),
			"DEX"		: self.GetChild("statusPointsDEXButton"),
		}

		# self.statusMinusButtonDict = {
			# "HTH-"		: self.GetChild("HTH_Minus"),
			# "INT-"		: self.GetChild("INT_Minus"),
			# "STR-"		: self.GetChild("STR_Minus"),
			# "DEX-"		: self.GetChild("DEX_Minus"),
		# }

		self.skillPageDict = {
			"ACTIVE" : self.GetChild("Skill_Active_Slot"),
			"SUPPORT" : self.GetChild("Skill_ETC_Slot"),
			"HORSE" : self.GetChild("Skill_Active_Slot"),
		}

		self.skillPageStatDict = {
			"SUPPORT"	: player.SKILL_SUPPORT,
			"ACTIVE"	: player.SKILL_ACTIVE,
			"HORSE"		: player.SKILL_HORSE,
		}

		self.skillGroupButton = (
			self.GetChild("Skill_Group_Button_1"),
			self.GetChild("Skill_Group_Button_2"),
		)

		
		global SHOW_ONLY_ACTIVE_SKILL
		global HIDE_SUPPORT_SKILL_POINT
		if SHOW_ONLY_ACTIVE_SKILL or HIDE_SUPPORT_SKILL_POINT:	
			self.GetChild("Support_Skill_Point_Label").Hide()

		self.soloEmotionSlot = self.GetChild("SoloEmotionSlot")
		self.dualEmotionSlot = self.GetChild("DualEmotionSlot")
		self.newEmotionSlot = self.GetChild("NewEmotionSlot")
		self.__SetEmotionSlot()

		self.questShowingStartIndex = 0
		self.questScrollBar = self.GetChild("Quest_ScrollBar")
		self.questScrollBar.SetScrollEvent(ui.__mem_func__(self.OnQuestScroll))
		self.questSlot = self.GetChild("Quest_Slot")
		for i in xrange(quest.QUEST_MAX_NUM):
			self.questSlot.HideSlotBaseImage(i)
			self.questSlot.SetCoverButton(i,\
											"d:/ymir work/ui/game/quest/slot_button_01.sub",\
											"d:/ymir work/ui/game/quest/slot_button_02.sub",\
											"d:/ymir work/ui/game/quest/slot_button_03.sub",\
											"d:/ymir work/ui/game/quest/slot_button_03.sub", True)

		self.questNameList = []
		self.questLastTimeList = []
		self.questLastCountList = []
		for i in xrange(quest.QUEST_MAX_NUM):
			self.questNameList.append(self.GetChild("Quest_Name_0" + str(i)))
			self.questLastTimeList.append(self.GetChild("Quest_LastTime_0" + str(i)))
			self.questLastCountList.append(self.GetChild("Quest_LastCount_0" + str(i)))
		
		self.BindAchievementBoard()
		self.BindBonusBoard()
		
		
	def __SetSkillSlotEvent(self):
		for skillPageValue in self.skillPageDict.itervalues():
			skillPageValue.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			skillPageValue.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectSkill))
			skillPageValue.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			skillPageValue.SetUnselectItemSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetUseSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			skillPageValue.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			skillPageValue.SetPressedSlotButtonEvent(ui.__mem_func__(self.OnPressedSlotButton))
			skillPageValue.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_down.sub")

	def __SetEmotionSlot(self):

		self.emotionToolTip = uiToolTip.ToolTip()

		for slot in (self.soloEmotionSlot, self.dualEmotionSlot, self.newEmotionSlot):
			slot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			slot.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectEmotion))
			slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
			slot.SetUseSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
			slot.SetOverInItemEvent(ui.__mem_func__(self.__OverInEmotion))
			slot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutEmotion))
			slot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_down.sub")

		for slotIdx, datadict in emotion.EMOTION_DICT.items():
			emotionIdx = slotIdx

			slot = self.soloEmotionSlot
			if slotIdx > 50 and slotIdx <= 60:
				slot = self.dualEmotionSlot
			elif slotIdx >= 61:
				slot = self.newEmotionSlot
			
			slot.SetEmotionSlot(slotIdx, emotionIdx)
			slot.SetCoverButton(slotIdx)

	def __SelectEmotion(self, slotIndex):
		if not slotIndex in emotion.EMOTION_DICT:
			return

		if app.IsPressed(app.DIK_LCONTROL):
			player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_EMOTION, slotIndex)
			return

		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_EMOTION, slotIndex, slotIndex)

	def __ClickEmotionSlot(self, slotIndex):
		print "click emotion"
		if not slotIndex in emotion.EMOTION_DICT:
			return

		print "check acting"
		if player.IsActingEmotion():
			return

		command = emotion.EMOTION_DICT[slotIndex]["command"]
		print "command", command

		if slotIndex > 50 and slotIndex < 61:
			vid = player.GetTargetVID()

			if 0 == vid or vid == player.GetMainCharacterIndex() or chr.IsNPC(vid) or chr.IsEnemy(vid):
				import chat
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EMOTION_CHOOSE_ONE)
				return

			command += " " + chr.GetNameByVID(vid)
		if slotIndex >= 66:
			net.SendChatPacket(command)
		else:
			print "send_command", command
			net.SendChatPacket(command)

	def ActEmotion(self, emotionIndex):
		self.__ClickEmotionSlot(emotionIndex)

	def __OverInEmotion(self, slotIndex):
		if self.emotionToolTip:

			if not slotIndex in emotion.EMOTION_DICT:
				return

			self.emotionToolTip.ClearToolTip()
			self.emotionToolTip.SetTitle(emotion.EMOTION_DICT[slotIndex]["name"])
			self.emotionToolTip.AlignHorizonalCenter()
			self.emotionToolTip.ShowToolTip()

	def __OverOutEmotion(self):
		if self.emotionToolTip:
			self.emotionToolTip.HideToolTip()

	def __BindEvent(self):
		for i in xrange(len(self.skillGroupButton)):
			self.skillGroupButton[i].SetEvent(lambda arg=i: self.__SelectSkillGroup(arg))

		self.RefreshQuest()
		self.__HideJobToolTip()

		for (tabKey, tabButton) in self.tabButtonDict.items():
			tabButton.SetEvent(ui.__mem_func__(self.__OnClickTabButton), tabKey)

		for (statusPlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.SAFE_SetEvent(self.__OnClickStatusPlusButton, statusPlusKey)
			statusPlusButton.ShowToolTip = lambda arg=statusPlusKey: self.__OverInStatButton(arg)
			statusPlusButton.HideToolTip = lambda arg=statusPlusKey: self.__OverOutStatButton()

		# for (statusMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			# statusMinusButton.SAFE_SetEvent(self.__OnClickStatusMinusButton, statusMinusKey)
			# statusMinusButton.ShowToolTip = lambda arg=statusMinusKey: self.__OverInStatMinusButton(arg)
			# statusMinusButton.HideToolTip = lambda arg=statusMinusKey: self.__OverOutStatMinusButton()

		# for titleBarValue in self.titleBarDict.itervalues():
			# titleBarValue.SetCloseEvent(ui.__mem_func__(self.Hide))

		self.questSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectQuest))

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			if localeInfo.IsARABIC() or localeInfo.IsVIETNAM() or localeInfo.IsJAPAN():
				self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "CharacterWindow.py")
			else:
				self.__LoadScript("exscript/CharacterWindow.py")
				
			self.__BindObject()
			self.__BindEvent()
		except:
			import exception
			exception.Abort("CharacterWindow.__LoadWindow")

		#self.tabButtonDict["EMOTICON"].Disable()
		self.SetState("STATUS")

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()

	def Close(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.Hide()

		self.Hide()

	def SetSkillToolTip(self, toolTipSkill):
		self.toolTipSkill = toolTipSkill

	# def __OnClickStatusPlusButton(self, statusKey):
		# try:
			# statusPlusCommand=self.statusPlusCommandDict[statusKey]
			# net.SendChatPacket(statusPlusCommand)
		# except KeyError, msg:
			# dbg.TraceError("CharacterWindow.__OnClickStatusPlusButton KeyError: %s", msg)

	def __OnClickStatusPlusButton(self, statusKey):
		cmd = self.statusPlusCommandDict[statusKey]

		if app.IsPressed(app.DIK_LCONTROL):
			cmd = cmd + "10"
		else:
			cmd = cmd + "1"
			
		net.SendChatPacket(cmd)

	def __OnClickStatusMinusButton(self, statusKey):
		try:
			statusMinusCommand=self.statusMinusCommandDict[statusKey]
			net.SendChatPacket(statusMinusCommand)
		except KeyError, msg:
			dbg.TraceError("CharacterWindow.__OnClickStatusMinusButton KeyError: %s", msg)


	def __OnClickTabButton(self, stateKey):
		self.SetState(stateKey)

	def SetState(self, stateKey):
		
		self.state = stateKey

		for (tabKey, tabButton) in self.tabButtonDict.items():
			if stateKey!=tabKey:
				tabButton.Enable()
			else:
				tabButton.Disable()
		
		
		if stateKey == "ACHIEVEMENT":
			self.achievementNavigationBoard.Show()
			self.tabButtonDict["BONUS"].SetPosition(30, 15 + 30 + 30 + 30 + 30 + 30 + 120)
		else:
			self.achievementNavigationBoard.Hide()
			self.tabButtonDict["BONUS"].SetPosition(30, 15 + 30 + 30 + 30 + 30 + 30)		
		
		
		# for tabValue in self.tabDict.itervalues():
			# tabValue.Hide()

		for pageValue in self.pageDict.itervalues():
			pageValue.Hide()

		# for titleBarValue in self.titleBarDict.itervalues():
			# titleBarValue.Hide()

		# self.titleBarDict[stateKey].Show()
		# self.tabDict[stateKey].Show()
		self.pageDict[stateKey].Show()
		

	def GetState(self):
		return self.state

	def __GetTotalAtkText(self):
		minAtk=player.GetStatus(player.ATT_MIN)
		maxAtk=player.GetStatus(player.ATT_MAX)
		atkBonus=player.GetStatus(player.ATT_BONUS)
		attackerBonus=player.GetStatus(player.ATTACKER_BONUS)

		if minAtk==maxAtk:
			atkValue = minAtk+atkBonus+attackerBonus
			return constInfo.NumberToPointString(atkValue)
		else:
			# return "%d-%d" % (minAtk+atkBonus+attackerBonus, maxAtk+atkBonus+attackerBonus)
			minatkValue = minAtk+atkBonus+attackerBonus 
			maxatkValue = maxAtk+atkBonus+attackerBonus
			return constInfo.NumberToPointString(minatkValue) + "-" + constInfo.NumberToPointString(maxatkValue)

	def __GetTotalMagAtkText(self):
		minMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MIN_MAGIC_WEP)
		maxMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MAX_MAGIC_WEP)

		if minMagAtk==maxMagAtk:
			return "%d" % (minMagAtk)
		else:
			return "%d-%d" % (minMagAtk, maxMagAtk)

	def __GetTotalDefText(self):
		defValue=player.GetStatus(player.DEF_GRADE)
		if constInfo.ADD_DEF_BONUS_ENABLE:
			defValue+=player.GetStatus(player.DEF_BONUS)
		return "%d" % (defValue)
	
	def RefreshStatus(self):
		if self.isLoaded==0:
			return

		try:
			self.GetChild("levelTextLine").SetText(str(player.GetStatus(player.LEVEL)))
			# self.GetChild("expTextLine").SetText(unsigned32(player.GetEXP())))
			self.GetChild("expTextLine").SetText(constInfo.NumberToPointString(player.GetEXP()))
			# self.GetChild("expNeedTextLine").SetText(unsigned32(player.GetStatus(player.NEXT_EXP)) - unsigned32(player.GetStatus(player.EXP))))
			
			expNeed = unsigned32(player.GetStatus(player.NEXT_EXP)) - unsigned32(player.GetStatus(player.EXP))
			self.GetChild("expNeedTextLine").SetText(constInfo.NumberToPointString(expNeed))
			self.GetChild("pointTPTextLine").SetText(constInfo.NumberToPointString(player.GetStatus(player.HP)) + '/' + str(constInfo.NumberToPointString(player.GetStatus(player.MAX_HP))))
			self.GetChild("pointMPTextLine").SetText(constInfo.NumberToPointString(player.GetStatus(player.SP)) + '/' + str(constInfo.NumberToPointString(player.GetStatus(player.MAX_SP))))

			self.GetChild("statusPointsVITTextLine").SetText(str(player.GetStatus(player.HT)))
			self.GetChild("statusPointsINTTextLine").SetText(str(player.GetStatus(player.IQ)))
			self.GetChild("statusPointsSTRTextLine").SetText(str(player.GetStatus(player.ST)))
			self.GetChild("statusPointsDEXTextLine").SetText(str(player.GetStatus(player.DX)))

			self.GetChild("pointDMGTextLine").SetText(self.__GetTotalAtkText())
			self.GetChild("pointDEFTextLine").SetText(self.__GetTotalDefText())

			self.GetChild("magicAtkValueTextLine").SetText(self.__GetTotalMagAtkText())
			#self.GetChild("MATT_Value").SetText(str(player.GetStatus(player.MAG_ATT)))

			self.GetChild("magicDefValueTextLine").SetText(str(player.GetStatus(player.MAG_DEF)))
			self.GetChild("atkSpeedValueTextLine").SetText(str(player.GetStatus(player.ATT_SPEED)))
			self.GetChild("moveSpeedValueTextLine").SetText(str(player.GetStatus(player.MOVING_SPEED)))
			self.GetChild("magicSpeedValueTextLine").SetText(str(player.GetStatus(player.CASTING_SPEED)))
			self.GetChild("evadeValueTextLine").SetText(str(player.GetStatus(player.EVADE_RATE)))

		except:
			#import exception
			#exception.Abort("CharacterWindow.RefreshStatus.BindObject")
			## 게임이 튕겨 버림
			pass

		self.__RefreshStatusPlusButtonList()
		self.__RefreshStatusMinusButtonList()
		self.RefreshAlignment()

		if self.refreshToolTip:
			self.refreshToolTip()

	def __RefreshStatusPlusButtonList(self):
		if self.isLoaded==0:
			return

		statusPlusPoint=player.GetStatus(player.STAT)

		if statusPlusPoint>0:
			self.statusPlusValue.SetText(str(statusPlusPoint))
			# self.statusPlusLabel.Show()
			self.ShowStatusPlusButtonList()
		else:
			self.statusPlusValue.SetText(str(0))
			# self.statusPlusLabel.Hide()
			self.HideStatusPlusButtonList()

	def __RefreshStatusMinusButtonList(self):
		if self.isLoaded==0:
			return

		statusMinusPoint=self.__GetStatMinusPoint()

		if statusMinusPoint>0:
			self.__ShowStatusMinusButtonList()
		else:
			self.__HideStatusMinusButtonList()

	def RefreshAlignment(self):
		point, grade = player.GetAlignmentData()

		import colorInfo
		COLOR_DICT = {	0 : colorInfo.TITLE_RGB_GOOD_4,
						1 : colorInfo.TITLE_RGB_GOOD_3,
						2 : colorInfo.TITLE_RGB_GOOD_2,
						3 : colorInfo.TITLE_RGB_GOOD_1,
						4 : colorInfo.TITLE_RGB_NORMAL,
						5 : colorInfo.TITLE_RGB_EVIL_1,
						6 : colorInfo.TITLE_RGB_EVIL_2,
						7 : colorInfo.TITLE_RGB_EVIL_3,
						8 : colorInfo.TITLE_RGB_EVIL_4, }
		colorList = COLOR_DICT.get(grade, colorInfo.TITLE_RGB_NORMAL)
		gradeColor = ui.GenerateColor(colorList[0], colorList[1], colorList[2])
		
		
		self.alignmentNameValue.SetText(localeInfo.TITLE_NAME_LIST[grade])
		if grade == 0:
			self.alignmentNameValue.SetFontColor(0.0, 0.8, 1.0)
		elif grade == 1:
			self.alignmentNameValue.SetFontColor(0.0, 0.5647, 1.0)
		elif grade == 2:
			self.alignmentNameValue.SetFontColor(0.3607, 0.4313, 1.0)
		elif grade == 3:
			self.alignmentNameValue.SetFontColor(0.6078, 0.6078, 1.0)
		elif grade == 4:
			self.alignmentNameValue.SetFontColor(1.0, 1.0, 1.0)
		elif grade == 5:
			self.alignmentNameValue.SetFontColor(0.8117, 0.4588, 0.0)
		elif grade == 6:
			self.alignmentNameValue.SetFontColor(0.9215, 0.3254, 0.0)
		elif grade == 7:
			self.alignmentNameValue.SetFontColor(0.8901, 0.0, 0.0)
		elif grade == 8:
			self.alignmentNameValue.SetFontColor(1.0, 0.0, 0.0)

		self.toolTipAlignment.ClearToolTip()
		self.toolTipAlignment.AutoAppendTextLine(localeInfo.TITLE_NAME_LIST[grade], gradeColor)
		self.toolTipAlignment.AutoAppendTextLine(localeInfo.ALIGNMENT_NAME + str(point))
		self.toolTipAlignment.AlignHorizonalCenter()

	def __ShowStatusMinusButtonList(self):
		return
		# for (stateMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			# statusMinusButton.Show()

	def __HideStatusMinusButtonList(self):
		return
		# for (stateMinusKey, statusMinusButton) in self.statusMinusButtonDict.items():
			# statusMinusButton.Hide()

	def ShowStatusPlusButtonList(self):
		for (statePlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.Enable()

	def HideStatusPlusButtonList(self):
		for (statePlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.Disable()

	def SelectSkill(self, skillSlotIndex):

		mouseController = mouseModule.mouseController

		if False == mouseController.isAttached():

			srcSlotIndex = self.__RealSkillSlotToSourceSlot(skillSlotIndex)
			selectedSkillIndex = player.GetSkillIndex(srcSlotIndex)

			if skill.CanUseSkill(selectedSkillIndex):

				if app.IsPressed(app.DIK_LCONTROL):

					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SKILL, srcSlotIndex)
					return

				mouseController.AttachObject(self, player.SLOT_TYPE_SKILL, srcSlotIndex, selectedSkillIndex)

		else:

			mouseController.DeattachObject()

	def SelectEmptySlot(self, SlotIndex):
		mouseModule.mouseController.DeattachObject()

	## ToolTip
	def OverInItem(self, slotNumber):
		#skilltooltip
		if mouseModule.mouseController.isAttached():
			return

		if 0 == self.toolTipSkill:
			return
		
		self.toolTipSkill.ClearToolTip()
		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillLevel = player.GetSkillLevel(srcSlotIndex)
		skillGrade = player.GetSkillGrade(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			overInSkillGrade = self.__GetSkillGradeFromSlot(slotNumber)

			if overInSkillGrade == skill.SKILL_GRADE_COUNT-1 and skillGrade == skill.SKILL_GRADE_COUNT:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)
			elif overInSkillGrade == skillGrade:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, overInSkillGrade, skillLevel)
			
				statPoint = player.GetStatus(player.SKILL_ACTIVE)
				if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
					if skillLevel < 17 and skillGrade == 0:
						self.toolTipSkill.AppendSpace(5)
						self.toolTipSkill.AppendTextLine(localeInfo.EMOJI_CHARACTER_SKILL_TO_M)
			else:
				self.toolTipSkill.SetSkillOnlyName(srcSlotIndex, skillIndex, overInSkillGrade)
			
			# statPoint = player.GetStatus(player.SKILL_ACTIVE)
			# if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
				# if skillLevel < 17 and skillGrade == 0:
					# self.toolTipSkill.AppendSpace(5)
					# self.toolTipSkill.AppendTextLine("STRG+LClick zum Meistern ; " + str(skillGrade))
			
		else:
			self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)

	def OverOutItem(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.HideToolTip()

	## Quest
	def __SelectQuest(self, slotIndex):
		questIndex = quest.GetQuestIndex(self.questShowingStartIndex+slotIndex)

		import event
		event.QuestButtonClick(-2147483648 + questIndex)

	def RefreshQuest(self):

		if self.isLoaded==0:
			return

		questCount = quest.GetQuestCount()
		questRange = range(quest.QUEST_MAX_NUM)

		if questCount > quest.QUEST_MAX_NUM:
			self.questScrollBar.Show()
		else:
			self.questScrollBar.Hide()

		for i in questRange[:questCount]:
			(questName, questIcon, questCounterName, questCounterValue) = quest.GetQuestData(self.questShowingStartIndex+i)

			self.questNameList[i].SetText(questName)
			self.questNameList[i].Show()
			self.questLastCountList[i].Show()
			self.questLastTimeList[i].Show()

			if len(questCounterName) > 0:
				self.questLastCountList[i].SetText("%s : %d" % (questCounterName, questCounterValue))
			else:
				self.questLastCountList[i].SetText("")

			## Icon
			self.questSlot.SetSlot(i, i, 1, 1, questIcon)

		for i in questRange[questCount:]:
			self.questNameList[i].Hide()
			self.questLastTimeList[i].Hide()
			self.questLastCountList[i].Hide()
			self.questSlot.ClearSlot(i)
			self.questSlot.HideSlotBaseImage(i)

		self.__UpdateQuestClock()

	def __UpdateQuestClock(self):
		if "QUEST" == self.state:
			# QUEST_LIMIT_COUNT_BUG_FIX
			for i in xrange(min(quest.GetQuestCount(), quest.QUEST_MAX_NUM)):
			# END_OF_QUEST_LIMIT_COUNT_BUG_FIX
				(lastName, lastTime) = quest.GetQuestLastTime(i)

				clockText = localeInfo.QUEST_UNLIMITED_TIME
				if len(lastName) > 0:

					if lastTime <= 0:
						clockText = localeInfo.QUEST_TIMEOVER

					else:
						questLastMinute = lastTime / 60
						questLastSecond = lastTime % 60

						clockText = lastName + " : "

						if questLastMinute > 0:
							clockText += str(questLastMinute) + localeInfo.QUEST_MIN
							if questLastSecond > 0:
								clockText += " "

						if questLastSecond > 0:
							clockText += str(questLastSecond) + localeInfo.QUEST_SEC

				self.questLastTimeList[i].SetText(clockText)

	def __GetStatMinusPoint(self):
		POINT_STAT_RESET_COUNT = 112
		return player.GetStatus(POINT_STAT_RESET_COUNT)

	def __OverInStatMinusButton(self, stat):
		try:
			self.__ShowStatToolTip(self.STAT_MINUS_DESCRIPTION[stat] % self.__GetStatMinusPoint())
		except KeyError:
			pass

		self.refreshToolTip = lambda arg=stat: self.__OverInStatMinusButton(arg) 

	def __OverOutStatMinusButton(self):
		self.__HideStatToolTip()
		self.refreshToolTip = 0

	# def __OverInStatButton(self, stat):	
		# try:
			# self.__ShowStatToolTip(self.STAT_DESCRIPTION[stat])
		# except KeyError:
			# pass

	def __OverInStatButton(self, stat):	
		try:
			self.__ShowStatToolTip(self.STAT_DESCRIPTION[stat], localeInfo.EMOJI_CHARACTER_STATS_ADD, True)
		except KeyError:
			pass

	def __OverOutStatButton(self):
		self.__HideStatToolTip()

	# def __ShowStatToolTip(self, statDesc):
		# self.toolTip.ClearToolTip()
		# self.toolTip.AppendTextLine(statDesc)
		# self.toolTip.Show()

	def __ShowStatToolTip(self, statDesc, statDesc2 = False, arg2 = False):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendTextLine(statDesc)
		
		if arg2 == True:
			self.toolTip.AppendTextLine(statDesc2)
			
		self.toolTip.Show()

	def __HideStatToolTip(self):
		self.toolTip.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnUpdate(self):
		self.__UpdateQuestClock()

	## Skill Process
	def __RefreshSkillPage(self, name, slotCount):
		global SHOW_LIMIT_SUPPORT_SKILL_LIST

		skillPage = self.skillPageDict[name]

		startSlotIndex = skillPage.GetStartIndex()
		if "ACTIVE" == name:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				startSlotIndex += slotCount

		getSkillType=skill.GetSkillType
		getSkillIndex=player.GetSkillIndex
		getSkillGrade=player.GetSkillGrade
		getSkillLevel=player.GetSkillLevel
		getSkillLevelUpPoint=skill.GetSkillLevelUpPoint
		getSkillMaxLevel=skill.GetSkillMaxLevel
		
		for i in xrange(slotCount+1):

			slotIndex = i + startSlotIndex
			skillIndex = getSkillIndex(slotIndex)

			for j in xrange(skill.SKILL_GRADE_COUNT):
				skillPage.ClearSlot(self.__GetRealSkillSlot(j, i))

			if 0 == skillIndex:
				continue

			skillGrade = getSkillGrade(slotIndex)
			skillLevel = getSkillLevel(slotIndex)
			skillType = getSkillType(skillIndex)

			## 승마 스킬 예외 처리
			# if player.SKILL_INDEX_RIDING == skillIndex:
				# if 1 == skillGrade:
					# skillLevel += 19
				# elif 2 == skillGrade:
					# skillLevel += 29
				# elif 3 == skillGrade:
					# skillLevel = 40

				# skillPage.SetSkillSlotNew(slotIndex, skillIndex, max(skillLevel-1, 0), skillLevel)
				# skillPage.SetSlotCount(slotIndex, skillLevel)

			## ACTIVE
			if skill.SKILL_TYPE_ACTIVE == skillType:
				for j in xrange(skill.SKILL_GRADE_COUNT):
					realSlotIndex = self.__GetRealSkillSlot(j, slotIndex)
					skillPage.SetSkillSlotNew(realSlotIndex, skillIndex, j, skillLevel)
					skillPage.SetCoverButton(realSlotIndex)

					if (skillGrade == skill.SKILL_GRADE_COUNT) and j == (skill.SKILL_GRADE_COUNT-1):
						skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)
					elif (not self.__CanUseSkillNow()) or (skillGrade != j):
						skillPage.SetSlotCount(realSlotIndex, 0)
						skillPage.DisableCoverButton(realSlotIndex)
					else:
						skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)

			## 그외
			else:
				if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
					realSlotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)
					skillPage.SetSkillSlot(realSlotIndex, skillIndex, skillLevel)
					skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)

					if skill.CanUseSkill(skillIndex):
						skillPage.SetCoverButton(realSlotIndex)

			skillPage.RefreshSlot()


	def RefreshSkill(self):

		if self.isLoaded==0:
			return

		if self.__IsChangedHorseRidingSkillLevel():
			self.RefreshCharacter()
			return


		global SHOW_ONLY_ACTIVE_SKILL
		if SHOW_ONLY_ACTIVE_SKILL:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
		else:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
			self.__RefreshSkillPage("SUPPORT", self.SUPPORT_PAGE_SLOT_COUNT)

		self.RefreshSkillPlusButtonList()

	def CanShowPlusButton(self, skillIndex, skillLevel, curStatPoint):

		## 스킬이 있으면
		if 0 == skillIndex:
			return False

		## 레벨업 조건을 만족한다면
		if not skill.CanLevelUpSkill(skillIndex, skillLevel):
			return False

		return True

	def __RefreshSkillPlusButton(self, name):
		global HIDE_SUPPORT_SKILL_POINT
		if HIDE_SUPPORT_SKILL_POINT and "SUPPORT" == name:
			return

		slotWindow = self.skillPageDict[name]
		slotWindow.HideAllSlotButton()

		slotStatType = self.skillPageStatDict[name]
		if 0 == slotStatType:
			return

		statPoint = player.GetStatus(slotStatType) # player.SKILL_ACTIVE
		startSlotIndex = slotWindow.GetStartIndex()
		if "HORSE" == name:
			startSlotIndex += self.ACTIVE_PAGE_SLOT_COUNT

		if statPoint > 0:
			for i in xrange(self.PAGE_SLOT_COUNT):
				slotIndex = i + startSlotIndex
				skillIndex = player.GetSkillIndex(slotIndex)
				skillGrade = player.GetSkillGrade(slotIndex)
				skillLevel = player.GetSkillLevel(slotIndex)

				if skillIndex == 0:
					continue
				if skillGrade != 0:
					continue

				if name == "HORSE":
					if player.GetStatus(player.LEVEL) >= skill.GetSkillLevelLimit(skillIndex):
						if skillLevel < 20:
							slotWindow.ShowSlotButton(self.__GetETCSkillRealSlotIndex(slotIndex))

				else:
					if "SUPPORT" == name:						
						if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
							if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
								slotWindow.ShowSlotButton(slotIndex)
					else:
						if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
							slotWindow.ShowSlotButton(slotIndex)
					

	def RefreshSkillPlusButtonList(self):

		if self.isLoaded==0:
			return

		self.RefreshSkillPlusPointLabel()

		if not self.__CanUseSkillNow():
			return

		try:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				self.__RefreshSkillPlusButton("HORSE")
			else:
				self.__RefreshSkillPlusButton("ACTIVE")

			self.__RefreshSkillPlusButton("SUPPORT")

		except:
			import exception
			exception.Abort("CharacterWindow.RefreshSkillPlusButtonList.BindObject")

	def RefreshSkillPlusPointLabel(self):
		if self.isLoaded==0:
			return

		if self.PAGE_HORSE == self.curSelectedSkillGroup:
			activeStatPoint = player.GetStatus(player.SKILL_HORSE)
			self.activeSkillPointValue.SetText(str(activeStatPoint))

		else:
			activeStatPoint = player.GetStatus(player.SKILL_ACTIVE)
			self.activeSkillPointValue.SetText(str(activeStatPoint))

		supportStatPoint = max(0, player.GetStatus(player.SKILL_SUPPORT))
		self.supportSkillPointValue.SetText(str(supportStatPoint))

	## Skill Level Up Button
	def OnPressedSlotButton(self, slotNumber):
		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)

		skillIndex = player.GetSkillIndex(srcSlotIndex)
		curLevel = player.GetSkillLevel(srcSlotIndex)
		maxLevel = skill.GetSkillMaxLevel(skillIndex)
		
		if self.skillUPMSpamBlock < app.GetTime():
			if app.IsPressed(app.DIK_LCONTROL):
				self.skillUPMSpamBlock = app.GetTime() + 2		
				net.SendChatPacket("/skillupm " + str(skillIndex))
			else:
				net.SendChatPacket("/skillup " + str(skillIndex))
			
	## Use Skill
	def ClickSkillSlot(self, slotIndex):

		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotIndex)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		if not self.__CanUseSkillNow():
			if skill.SKILL_TYPE_ACTIVE == skillType:
				return

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				if skill.CanUseSkill(skillIndex):
					player.ClickSkillSlot(srcSlotIndex)
					return

		mouseModule.mouseController.DeattachObject()

	## FIXME : 스킬을 사용했을때 슬롯 번호를 가지고 해당 슬롯을 찾아서 업데이트 한다.
	##         매우 불합리. 구조 자체를 개선해야 할듯.
	def OnUseSkill(self, slotIndex, coolTime):

		skillIndex = player.GetSkillIndex(slotIndex)
		skillType = skill.GetSkillType(skillIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			skillGrade = player.GetSkillGrade(slotIndex)
			slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)
		## ETC
		else:
			slotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.SetSlotCoolTime(slotIndex, coolTime)
				return

	def OnActivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.ActivateSlot(slotIndex)
				return

	def OnDeactivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.DeactivateSlot(slotIndex)
				return

	def __ShowJobToolTip(self):
		self.toolTipJob.ShowToolTip()

	def __HideJobToolTip(self):
		self.toolTipJob.HideToolTip()

	def __SetJobText(self, mainJob, subJob):
		if player.GetStatus(player.LEVEL)<5:
			subJob=0

		if 949 == app.GetDefaultCodePage():
			self.toolTipJob.ClearToolTip()

			try:
				jobInfoTitle=localeInfo.JOBINFO_TITLE[mainJob][subJob]
				jobInfoData=localeInfo.JOBINFO_DATA_LIST[mainJob][subJob]
			except IndexError:
				print "uiCharacter.CharacterWindow.__SetJobText(mainJob=%d, subJob=%d)" % (mainJob, subJob)
				return

			self.toolTipJob.AutoAppendTextLine(jobInfoTitle)
			self.toolTipJob.AppendSpace(5)

			for jobInfoDataLine in jobInfoData:
				self.toolTipJob.AutoAppendTextLine(jobInfoDataLine)

			self.toolTipJob.AlignHorizonalCenter()
	
	
	def OpenGuildWindow(self):
		self.interface.ToggleGuildWindow()
	
	def __ShowGuildToolTip(self):
		guildName = player.GetGuildName()
		if not guildName:
			return 
			
		self.toolTipGuild.ClearToolTip()
		self.toolTipGuild.AppendTextLine(localeInfo.CHARACTER_GUILD_TOOLTIP_MASTER + guild.GetGuildMasterName())
		self.toolTipGuild.AppendHorizontalLine()
		self.toolTipGuild.AppendSpace(5)
		self.toolTipGuild.AppendTextLine(localeInfo.CHARACTER_GUILD_TOOLTIP_LEVEL + str(guild.GetGuildLevel()) + " / 5")
		
		curExp, lastExp = guild.GetGuildExperience()
		curExp *= 100
		lastExp *= 100
		self.toolTipGuild.AppendTextLine(localeInfo.CHARACTER_GUILD_TOOLTIP_EXP + str(curExp) + " / " + str(lastExp))
		self.toolTipGuild.AppendHorizontalLine()
		self.toolTipGuild.AppendSpace(5)
		self.toolTipGuild.AppendTextLine(localeInfo.CHARACTER_GUILD_TOOLTIP_OPEN_WINDOW)
		self.toolTipGuild.ShowToolTip()
		
	def __HideGuildToolTip(self):
		self.toolTipGuild.HideToolTip()
	
	def __ShowAlignmentToolTip(self):
		self.toolTipAlignment.ShowToolTip()

	def __HideAlignmentToolTip(self):
		self.toolTipAlignment.HideToolTip()

	def RefreshCharacter(self):

		if self.isLoaded==0:
			return

		## Name
		try:
			characterName = player.GetName()
			guildName = player.GetGuildName()
			self.characterNameValue.SetText(characterName)
			self.guildNameValue.SetText(guildName)
			if not guildName:
				self.guildNameValue.SetText("Keine Gilde")
				# if localeInfo.IsARABIC():
					# self.characterNameSlot.SetPosition(190, 34)
				# else:
					# self.characterNameSlot.SetPosition(109, 34)

				# self.guildNameSlot.Hide()
			# else:
				# if localeInfo.IsJAPAN():
					# self.characterNameSlot.SetPosition(143, 34)
				# else:
					# self.characterNameSlot.SetPosition(153, 34)
				# self.guildNameSlot.Show()
		except:
			import exception
			exception.Abort("CharacterWindow.RefreshCharacter.BindObject")

		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()

		## Job Text
		job = chr.RaceToJob(race)
		self.__SetJobText(job, group)

		## FaceImage
		try:
			faceImageName = FACE_IMAGE_DICT[race]

			try:
				self.faceImage.LoadImage(faceImageName)
			except:
				print "CharacterWindow.RefreshCharacter(race=%d, faceImageName=%s)" % (race, faceImageName)
				self.faceImage.Hide()

		except KeyError:
			self.faceImage.Hide()

		## GroupName
		self.__SetSkillGroupName(race, group)

		## Skill
		if 0 == group:
			self.__SelectSkillGroup(0)

		else:
			self.__SetSkillSlotData(race, group, empire)

			if self.__CanUseHorseSkill():
				self.__SelectSkillGroup(0)

	def __SetSkillGroupName(self, race, group):

		job = chr.RaceToJob(race)

		if not self.SKILL_GROUP_NAME_DICT.has_key(job):
			return

		nameList = self.SKILL_GROUP_NAME_DICT[job]

		if 0 == group:
			self.skillGroupButton1.SetText(nameList[1])
			self.skillGroupButton2.SetText(nameList[2])
			self.skillGroupButton1.Show()
			self.skillGroupButton2.Show()
			self.activeSkillGroupName.Hide()

		else:

			if self.__CanUseHorseSkill():
				self.activeSkillGroupName.Hide()
				self.skillGroupButton1.SetText(nameList.get(group, "Noname"))
				self.skillGroupButton2.SetText(localeInfo.SKILL_GROUP_HORSE)
				self.skillGroupButton1.Show()
				self.skillGroupButton2.Show()

			else:
				self.activeSkillGroupName.SetText(nameList.get(group, "Noname"))
				self.activeSkillGroupName.Show()
				self.skillGroupButton1.Hide()
				self.skillGroupButton2.Hide()

	def __SetSkillSlotData(self, race, group, empire=0):

		## SkillIndex
		playerSettingModule.RegisterSkill(race, group, empire)

		## Event
		self.__SetSkillSlotEvent()

		## Refresh
		self.RefreshSkill()

	def __SelectSkillGroup(self, index):
		for btn in self.skillGroupButton:
			btn.SetUp()
		self.skillGroupButton[index].Down()

		if self.__CanUseHorseSkill():
			if 0 == index:
				index = net.GetMainActorSkillGroup()-1
			elif 1 == index:
				index = self.PAGE_HORSE

		self.curSelectedSkillGroup = index
		self.__SetSkillSlotData(net.GetMainActorRace(), index+1, net.GetMainActorEmpire())

	def __CanUseSkillNow(self):
		if 0 == net.GetMainActorSkillGroup():
			return False

		return True

	def __CanUseHorseSkill(self):

		slotIndex = player.GetSkillSlotIndex(player.SKILL_INDEX_RIDING)

		if not slotIndex:
			return False

		grade = player.GetSkillGrade(slotIndex)
		level = player.GetSkillLevel(slotIndex)
		if level < 0:
			level *= -1
		if grade >= 1 and level >= 1:
			return True

		return False

	def __IsChangedHorseRidingSkillLevel(self):
		ret = False

		if -1 == self.canUseHorseSkill:
			self.canUseHorseSkill = self.__CanUseHorseSkill()

		if self.canUseHorseSkill != self.__CanUseHorseSkill():
			ret = True

		self.canUseHorseSkill = self.__CanUseHorseSkill()
		return ret

	def __GetRealSkillSlot(self, skillGrade, skillSlot):
		return skillSlot + min(skill.SKILL_GRADE_COUNT-1, skillGrade)*skill.SKILL_GRADE_STEP_COUNT

	def __GetETCSkillRealSlotIndex(self, skillSlot):
		if skillSlot > 100:
			return skillSlot
		return skillSlot % self.ACTIVE_PAGE_SLOT_COUNT

	def __RealSkillSlotToSourceSlot(self, realSkillSlot):
		if realSkillSlot > 100:
			return realSkillSlot
		if self.PAGE_HORSE == self.curSelectedSkillGroup:
			return realSkillSlot + self.ACTIVE_PAGE_SLOT_COUNT
		return realSkillSlot % skill.SKILL_GRADE_STEP_COUNT

	def __GetSkillGradeFromSlot(self, skillSlot):
		return int(skillSlot / skill.SKILL_GRADE_STEP_COUNT)

	def SelectSkillGroup(self, index):
		self.__SelectSkillGroup(index)

	def OnQuestScroll(self):
		questCount = quest.GetQuestCount()
		scrollLineCount = max(0, questCount - quest.QUEST_MAX_NUM)
		startIndex = int(scrollLineCount * self.questScrollBar.GetPos())

		if startIndex != self.questShowingStartIndex:
			self.questShowingStartIndex = startIndex
			self.RefreshQuest()
	
	
	
	def BindAchievementBoard(self):
		
		self.achievementStatisticCategoryList = {
			
			achievementproto.CATEGORY_BOSS		: [localeInfo.ACHIEVEMENT_CATEGORY_BOSS,	[], []],
			achievementproto.CATEGORY_STONE		: [localeInfo.ACHIEVEMENT_CATEGORY_STONES,	[], []],
			achievementproto.CATEGORY_DUNGEON	: [localeInfo.ACHIEVEMENT_CATEGORY_DUNGEON,	[], []],
			achievementproto.CATEGORY_LEVEL		: [localeInfo.ACHIEVEMENT_CATEGORY_LEVEL,	[], []],
			achievementproto.CATEGORY_REFINE	: [localeInfo.ACHIEVEMENT_CATEGORY_REFINE,	[], []],
			achievementproto.CATEGORY_ONE_TIME	: [localeInfo.ACHIEVEMENT_CATEGORY_ONE_TIME,[], []],

		}
		
		
		self.achievementNavigationBoard = self.GetChild("apNavigationBackground")
		self.achievementNavigationBoard.Hide()
		
		self.achievementNavigationListBox = self.GetChild("apNavigationListBox")
		self.achievementNavigationListBox.SetEvent(ui.__mem_func__(self.OnSelectAchievementStatistic))
		self.achievementNavigationScrollBar = self.GetChild("apScrollBar")
		self.achievementNavigationScrollBar.Hide()
		
		self.achievementNavigationMaxItem = 6
		
		
		miniListboxItemCount = 0
		for i in xrange(len(self.achievementStatisticCategoryList)):
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, str(i) + " " + str(self.achievementStatisticCategoryList[i][0]))
			self.achievementNavigationListBox.InsertItem(i, self.achievementStatisticCategoryList[i][0])
			miniListboxItemCount = miniListboxItemCount + 1
		
		if miniListboxItemCount > self.achievementNavigationMaxItem:
			self.achievementNavigationScrollBar.Show()
		
	
		self.achievementBoard = self.GetChild("achievementBackgroundBoard")
		self.achievementCategoryTextLine = self.GetChild("achievementCategoryTitleTextLine")
		self.achievementScrollBar = self.GetChild("achievementScrollBar")
		self.achievementScrollBar.Hide()
		self.achievementScrollBar.SetScrollEvent(ui.__mem_func__(self.RenderAchievementStatistic))
		
		self.achievementCategory = 0
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "AchievementProto.txt wird geladen...")
		srcRealFileName = "locale/%s/%s" % (app.GetLanguage(), "achievement_proto.txt")
		lines = pack_open(srcRealFileName, "r").readlines()
		for line in lines:
			tab = line.split("\t")
			if tab[0] != "VNUM":
				data = {
					"vnum"		: int(tab[0]),
					"desc"		: str(tab[1]),
					"type"		: int(tab[2]),
					"points"	: int(tab[3]),
					"max_count" : int(tab[4]),
					"category"	: int(tab[5]),
					"count" : 0,
				}
				
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Achievement Statistik: Achievement " + str(tab[0]) + " geladen!")
				self.achievementStatisticCategoryList[int(tab[5])][1].append(data)

		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "AchievementProto.txt fertig geladen...")

		for i in xrange(len(self.achievementStatisticCategoryList)):
			for a in xrange(len(self.achievementStatisticCategoryList[i][1])):
				data = self.achievementStatisticCategoryList[i][1][a]
				if data["max_count"] == 0:
					item = AchievementItem()
					item.SetParent(self.achievementBoard)
					item.SetPosition(5,5 + 22)
					if data["desc"] == "MONSTER":
						item.SetTitle(nonplayer.GetMonsterName(data["vnum"]))
					else:
						item.SetTitle(data["desc"])
					item.SetCount(0)
					item.SetPoints(data["points"])
					item.SetScrollBarMode(0)
					item.Hide()	

					self.achievementStatisticCategoryList[i][2].append(item)
				
				else:
					item = AchievementProgressItem()
					item.SetParent(self.achievementBoard)
					item.SetPosition(5,5 + 22)
					if data["desc"] == "MONSTER":
						item.SetTitle(nonplayer.GetMonsterName(data["vnum"]))
					else:
						item.SetTitle(data["desc"])
					item.SetCount(0)
					item.SetMaxCount(data["max_count"])
					item.SetPoints(data["points"])
					item.SetScrollBarMode(0)
					item.Hide()	

					self.achievementStatisticCategoryList[i][2].append(item)					
		
		self.achievementNavigationListBox.SelectItem(0)
		
	
	def UpdateAchievementStatistic(self, index, new_count, cat):
		data = self.achievementStatisticCategoryList[int(cat)][1]
		for i in xrange(len(data)):
			if data[i]["vnum"] == int(index):
				self.achievementStatisticCategoryList[int(cat)][1][i]["count"] = int(new_count)
				break
				
		self.RenderAchievementStatistic()
	
	def OnSelectAchievementStatistic(self):
		cat = self.achievementNavigationListBox.GetSelectedItem()
		self.SetAchievementCategory(cat)


	def SetAchievementCategory(self, cat):
		self.HideAllAchievementItems()
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Category " + str(cat) + " selected!")
		self.achievementCategory = cat
		self.achievementCategoryTextLine.SetText(self.achievementStatisticCategoryList[cat][0])
		itemCount = len(self.achievementStatisticCategoryList[cat][2])
		self.AchievementScrollMode = False
		self.achievementScrollBar.SetPos(0)
		if itemCount > 6:
			self.achievementScrollBar.Show()
			self.AchievementScrollMode = True
		else:
			self.achievementScrollBar.Hide()
			
		self.RenderAchievementStatistic()	
			
	def RenderAchievementStatistic(self):
		self.HideAllAchievementItems()
		
		# self.achievementScrollBar.Hide()
		cat = self.achievementCategory
		itemCount = len(self.achievementStatisticCategoryList[cat][2])
		pos = int(self.achievementScrollBar.GetPos() * (len(self.achievementStatisticCategoryList[cat][2]) - 6)) 
		start_height = 5 + 22
		
		if itemCount > 6:
			max_count = 6
		else:
			max_count = itemCount
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "itemCount: " + str(max_count))
		for i in xrange(max_count):
			realPos = pos + i
			self.achievementStatisticCategoryList[cat][2][realPos].SetPosition(5,start_height)

			self.achievementStatisticCategoryList[cat][2][realPos].SetCount(self.achievementStatisticCategoryList[cat][1][realPos]["count"])
			if self.AchievementScrollMode:
				self.achievementStatisticCategoryList[cat][2][realPos].SetScrollBarMode(1)
			else:
				self.achievementStatisticCategoryList[cat][2][realPos].SetScrollBarMode(0)
			
			self.achievementStatisticCategoryList[cat][2][realPos].Show()
			start_height = start_height + 51 + 10			
	
	def HideAllAchievementItems(self):
		cat = self.achievementCategory
		for i in xrange(len(self.achievementStatisticCategoryList[cat][2])):
			self.achievementStatisticCategoryList[cat][2][i].Hide()
		
	# BONUS BOARD
	def BindBonusBoard(self):
		self.bonusBackground = self.GetChild("bonusBackgroundBoard")
		self.bonusScrollBar = self.GetChild("scrollBar")
		self.bonusBoardMaxItems = 16
		self.bonusScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		#value = player.GetStatus(type)
		for i in xrange(len(BONUS_BOARD_ITEM_LIST)):
			
			if BONUS_BOARD_ITEM_LIST[i]["type"] == "title":
				self.bonusItemList[i] = BonusTitleItem()
				self.bonusItemList[i].SetParent(self.bonusBackground)
				self.bonusItemList[i].SetPosition(5,5)
				self.bonusItemList[i].SetTitle(BONUS_BOARD_ITEM_LIST[i]["text"])
				self.bonusItemList[i].Show()
				
			elif BONUS_BOARD_ITEM_LIST[i]["type"] == "bonus":
				self.bonusItemList[i] = BonusItem()
				self.bonusItemList[i].SetParent(self.bonusBackground)
				self.bonusItemList[i].SetPosition(5,5)
				self.bonusItemList[i].SetTitle(BONUS_BOARD_ITEM_LIST[i]["text"])
				self.bonusItemList[i].SetBonus(BONUS_BOARD_ITEM_LIST[i]["bonus"])
				self.bonusItemList[i].SetApplicableList(BONUS_BOARD_ITEM_LIST[i]["applicable_to"])
				self.bonusItemList[i].Show()

				
		self.HideAllItems()
		self.RenderBonusList()
		
	def OnRunMouseWheel(self, nLen):
		if self.state == "ACHIEVEMENT":
			if nLen > 0:
				self.achievementScrollBar.OnUp()
			else:
				self.achievementScrollBar.OnDown()

		elif self.state == "BONUS":
			if nLen > 0:
				self.bonusScrollBar.OnUp()
			else:
				self.bonusScrollBar.OnDown()

	def HideAllItems(self):
		for i in xrange(len(self.bonusItemList)):
			self.bonusItemList[i].Hide()
	
	def RenderBonusList(self):
		pos = int(self.bonusScrollBar.GetPos() * (len(self.bonusItemList) - self.bonusBoardMaxItems)) 
		start_height = 5
		for i in xrange(self.bonusBoardMaxItems):
			realPos = pos + i
			self.bonusItemList[realPos].SetPosition(5,start_height)
			self.bonusItemList[realPos].Show()
			start_height = start_height + 25
			
	def OnScroll(self):
		self.HideAllItems()
		self.RenderBonusList()		


class AchievementItem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.points = 0
		self.count = 0
		
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/achievement_item.py")
		except:
			import exception
			exception.Abort("AchievementItem.LoadWindow.LoadObject")

		self.title = self.GetChild("titleTextLine")
		self.board = self.GetChild("board")
		self.info = self.GetChild("infoTextLine")
		self.Show()
	
	def SetScrollBarMode(self, mode):
		if mode == 1:
			self.SetSize(225, 51)
			self.board.SetSize(225, 51)
			self.scrollBarMode = 1 # an
		else:
			self.SetSize(225 + 5, 51)
			self.board.SetSize(225 + 5, 51)
			self.scrollBarMode = 0 # aus			

	def SetTitle(self,title):
		self.title.SetText(title)
	
	def SetCount(self,count):
		self.count = int(count)
		self.UpdateItem()
		
	def SetPoints(self,points):
		self.points = int(points)
		self.UpdateItem()
	
	def UpdateItem(self):
		realPoints = self.count * self.points
		self.info.SetText(localeInfo.ACHIEVEMENT_STAT_UI_INFO_COUNT + constInfo.NumberToPointString(self.count) + localeInfo.ACHIEVEMENT_STAT_UI_INFO_POINTS + constInfo.NumberToPointString(realPoints))


class AchievementProgressItem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.points = 0
		self.count = 0
		self.max_count = 0
		
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/achievement_progress_item.py")
		except:
			import exception
			exception.Abort("AchievementItem.LoadWindow.LoadObject")
		
		# Fortschritt 0 / 10 | Punkte: 10
		self.title = self.GetChild("titleTextLine")
		self.board = self.GetChild("board")
		self.info = self.GetChild("infoTextLine")
		self.Show()
	
	def SetScrollBarMode(self, mode):
		if mode == 1:
			self.SetSize(225, 51)
			self.board.SetSize(225, 51)
			self.scrollBarMode = 1 # an
		else:
			self.SetSize(225 + 5, 51)
			self.board.SetSize(225 + 5, 51)
			self.scrollBarMode = 0 # aus			

	def SetTitle(self,title):
		self.title.SetText(title)
	
	def SetCount(self,count):
		self.count = int(count)
		self.UpdateItem()
		
	def SetMaxCount(self, max_count):
		self.max_count = int(max_count)
		self.UpdateItem()
		
	def SetPoints(self,points):
		self.points = int(points)
		self.UpdateItem()
	
	def UpdateItem(self):
		# realPoints = self.count * self.points
		if self.count == self.max_count:
			self.info.SetText("Abgeschlossen | Punkte: " + str(self.points))
			self.info.SetFontColor(0.5411, 0.7254, 0.5568)		
		else:
			self.info.SetText("Fortschritt: " + str(self.count) + " / " + str(self.max_count) + " | Punkte: " + str(self.points))
			self.info.SetFontColor(0.9, 0.4745, 0.4627)
			
			
			
class BonusTitleItem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/bonus_title.py")
		except:
			import exception
			exception.Abort("BonusTitleItem.LoadWindow.LoadObject")

		self.title = self.GetChild("titleTextLine")
		self.Show()

	def SetTitle(self,title):
		self.title.SetText(title)

class BonusItem(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.bonus = 0
		self.appList = []
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/bonus_item.py")
		except:
			import exception
			exception.Abort("BonusItem.LoadWindow.LoadObject")
		
		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.HideToolTip()
		
		self.title		= self.GetChild("titleTextLine")
		self.value		= self.GetChild("bonusValueTextLine")
		self.ttWindow	= self.GetChild("toolTipWindow")
		self.Show()

	def SetTitle(self,title):
		self.title.SetText(title)

	def SetBonus(self, bonus):
		self.bonus = int(bonus)
	
	
	def SetApplicableList(self, list):
		self.appList = list
	
	def OnUpdate(self):
		value = player.GetStatus(self.bonus)
		self.value.SetText(constInfo.NumberToPointString(value))
		if self.ttWindow.IsIn():
			self.toolTip.ClearToolTip()
			if len(self.appList) == 0:
				self.toolTip.AppendTextLine("Kann nicht geswitched werden!")
			else:
				self.toolTip.AppendTextLine("Kann in Equipment geswitched werden:")
				self.toolTip.AppendSpace(5)
				for i in xrange(len(self.appList)):
					attrIndex = self.appList[i]
					self.toolTip.AppendTextLine(BONUS_ATTR_TRANSLATE_LIST[attrIndex])
			self.toolTip.ShowToolTip()
		else:
			self.toolTip.HideToolTip()
			

		
		
		