import background
import fgGHGjjFHJghjfFG1545gGG
import chat
import localeInfo
import app
# ----------------------------------------------------------------------------------------------
# Inhaltsverzeichnis
# 1.) 	variablenListe kleiner Systeme
# 2.) 	Pet-System
# 3.) 	UppItemItemToolTips
# 4.) 	Bio-System
# 5.) 	Mount-System
# 6.) 	DropGuide
# 7.) 	AttrSort Function
# 8.) 	MaxPlusStone
# 9.) 	ApCoupons
# 10.) 	Daily-System
# 11.) 	UppItem Lager
# 12.) 	SkillbookStorage
# 13.) 	MapNameList
# 14.) 	treasureChest System
# 15.) 	Dungeon System
# 16.)	MultiShopSystem
# 17.)	IntroDungeon
# 18.)	GuideBoard
# 19.)	Schmiedehandbuch
# 20.)	Switchbot


TIP_TEXT = {
	1 : localeInfo.TIP01,


}

def GetTipText():
	random = app.GetRandom(1,len(TIP_TEXT))
	return TIP_TEXT[random]

PREVIEW_CHEST_LIST = [50082]

# Statistik
GOLD_EARNED = 0
AP_EARNED = 1
STONE_KILL_TEMP = 2
MONSTER_KILL_TEMP = 3
PLAYER_PLAYTIME = 4
PVP_DUELL = 5
PVP_DUELL_WON = 6
PVP_DUELL_LOST = 7
PVP_SHINSOO_KILL = 8
PVP_CHUNJO_KILL = 9
PVP_JINNO_KILL = 10
PVM_MONSTER_KILL = 11
PVM_STONE_KILL = 12
PVM_DUNGEON_COMPL = 13
PVM_ACHIEVEMENT = 14

PLAYER_STATISTIC_DICT = [
	0, # GOLD_EARNED
	0, # AP_EARNED
	0, # STONE_KILL_TEMP
	0, # MONSTER_KILL_TEMP
	0, # PLAYER_PLAYTIME
	0, # PVP_DUELL
	0, # PVP_DUELL_WON
	0, # PVP_DUELL_LOST
	0, # PVP_SHINSOO_KILL
	0, # PVP_CHUNJO_KILL
	0, # PVP_JINNO_KILL
	0, # PVM_MONSTER_KILL
	0, # PVM_STONE_KILL
	0, # PVM_DUNGEON_COMPL
	0, # PVM_ACHIEVEMENT

]

isGM = False
DragonCoins = 0
GoldStorageQID = 0
realChannel = 0
autoPotionStatus = 0
autoPotionQID = 0
forest_zone_time = 0

AUTO_POTION_LIST = [
	# type,point,itemVnum
	[510,40,71044], # Krit
	[510,41,71045], # DB
	
	[510,93,72031], # Drachengott-Angriff
	[510,115,72034], # Drachengott-Verteidigung
	[510,119,72037], # Drachengott-Lebenskraft
	
	[531,95,50826], # WTau
	[531,96,50825], # BTau	

	[201,17,27101],
	[201,17,27053],
]

# ----------------------------------------------------------------------------------------------
# 1.) variablenListe kleiner Systeme

SchmiedehandbuchOpen 	= 0 # Aktueller Status des Schmiedehandbuchs: 1:Offen, 0:Geschlossen
SchmiedehandbuchPVPOpen 	= 0 # Aktueller Status des Schmiedehandbuchs: 1:Offen, 0:Geschlossen
BonusBoardOpen			= 0 # Aktueller Status des BonusBoards.

OpenBoxQID 				= 0 # QuestIndex des Truhen öffners
BoxOpenerOpen 			= 0 # Aktueller Status des Truhen Öffners: 1:Offen, 0:Geschlossen

SkillBookQID 			= 0 # QuestIndex des FertigkeitsbuchLagers
SkillBookStorageOpen 	= 0 # Aktueller Status des FertigkeitsbuchLagers: 1:Offen, 0:Geschlossen

battlezonePoints 		= 0	# Kampfzonen Punkte
battlezoneLeaveTime 	= 0 # Zeit zum verlassen der Kampfzone
battlezoneIsExit 		= 0 # Ist ExitMode active?

cooldownOverlayItems 	= {71158} # Items erhalten CooldownOverlay
tickqid = 0
bossMapTimer			= 0

# def isGameMaster()
	# playerName = fgGHGjjFHJghjfFG1545gGG.GetName()
	# if playerName[1] == "Y":
		# return True
	# else:
		# return False
		


event_eventflags_names		= {}
event_eventflags_indez		= {}

def searchForEventFlag(flagName,flagNumber):
	for i in xrange(len(event_eventflags_names)):
		if event_eventflags_names[i+1] == flagName:
			if event_eventflags_indez[i+1] == flagNumber:
				return True
			
	return False	
		
		
bio_timer = 0
bio_timer_status = 0		

# ----------------------------------------------------------------------------------------------
# 2.) Pet-System
PET_INFOS = {
	# Burtkasten
	"gui_box"		: 0, # Status der GUIBox
	"itemIndex"		: 0, # itemID des PEt-Ei's
	"price"			: 0, # Preis zum ausbrüten
	"itemVnum"		: 0, # itemVnum des Pet-Ei's
	"qid"			: 0, # QuestIndex von pet_2016.lua
	
	# Pet-Main
	"name"			: "", # PetName
	"level"			: 0,  # PetLevel
	"exp"			: 0,  # PetEXP
	"iexp"			: 0,  # PetItemEXP
	"next_iexp"		: 0,  # Benötigte Item-EXP
		
}


PET_SEALS 		= [91236,91237,91238,91239,91240,91241] # Alle Pet-Siegel
PET_EGGS		= [91230,91231,91232,91233,91234,91235] # Alle Pet-Eier
PET_ITEM_EXP	= [91250,91251,91252] 					# Alle Item-EXP ItemVnums
PET_INT_BOOK	= 91253	# itemVnum des Intelligenzbuches

PET_ITEM_EXP_TABLE = [
	0,
	15,
	40,
	75,
	125,
	215,
	360,
	550,
	850,
	1200,
	1350,	# 10
	2150,
	2900,
	3800,
	5000,
	6500,
	8450,
	10950,
	14150,
	18250,
	23600,	# 20
	30500,
	35250,
	40650,
	46850,
	53850,
	61850,
	70900,
	81200,
	92850,
	106100,	# 30
	121500,
	138050,
	157250,
	179000,
	203650,
	231600,
	255300,
	285850,
	313200,
	341850,	# 40
	380000,
	413700,
	449500,
	487650,
	528000,
	570500,
	616000,
	663500,
	714000,
	767000	# 50	
]

PET_INTELLIGENCE_BONUS = [
	0,
	25,
	50,
	90,
	140,
	200,
	275,
	375,
	500,
	650,
	850,
	1100,
	1400,
	1775,
	2250,
	2850,
	3600,
	4550,
	5700,
	7200,
	9000,
	11300,
	14200,
	17800,
	22300,
	24900
]


# ----------------------------------------------------------------------------------------------
# 3.) UppItemItemToolTips
UppItemItemToolTips = [
	[
		[27987], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Tu-Young",
					"Metin Jeon-Un",
					"Truhe der Seele",
					"Truhe der Schattens",
					"Truhe der Seele",
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Keine Dropps bekannt",
				]
			]
		]
	],
	[
		[27992], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Tu-Young",
					"Metin Jeon-Un",
					"Truhe der Seele",		
					"Truhe des Schattens",						
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Oberork-Truhe",
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
				]
			]
		]
	],
	[
		[27993], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Tu-Young",
					"Metin Jeon-Un",
					"Truhe der Seele",		
					"Truhe des Schattens",						
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Oberork-Truhe",
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
				]
			]
		]
	],
	[
		[27994], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Tu-Young",
					"Metin Jeon-Un",
					"Truhe der Seele",		
					"Truhe des Schattens",						
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Oberork-Truhe",
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
				]
			]
		]
	],
	[
		[70031], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Feuer der Macht Truhe",
					"Truhe des Berges",
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Keine Dropps bekannt",
				]
			]
		]
	],
	[
		
		[91145], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Tu-Young",
					"Metin Jeon-Un",
					"Truhe der Seele",
					"Truhe des Schattens",
					"Truhe des Berges",
					"Truhe der Schlangen",
					"Truhe der Unoten",
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Oberork-Truhe",
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
					"Truhe des Roten Drachen",
				]
			]
		]
	],
	[
		[91256], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Keine Dropps bekannt",			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Fraktal-Truhe",
				]
			]
		]
	],
	[
		
		[91257], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Keine Dropps bekannt",			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Fraktal-Truhe",
				]
			]
		]
	],
	[
		
		[91130], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Tu-Young",
					"Metin Jeon-Un",
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Oberork-Truhe",
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
					"Truhe des Roten Drachen",
					"Truhe der Verfluchten Eis Kreatur",
					"Truhe der Eisschlangenkönigin",
					"Truhe des Brutalen Eisungeheuers",
				]
			]
		]
	],
	[
		
		[91131], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Jeon-Un",
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
					"Truhe des Roten Drachen",
					"Truhe der verfluchten Eis Kreatur",
					"Truhe der Eisschlangenkönigin",
					"Truhe des brutalen Eisungeheuers",
				]
			]
		]
	],
	[
		[91132], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des Roten Drachen",
					"Truhe der verfluchten Eis Kreatur",
					"Truhe der Eisschlangenkönigin",
					"Truhe des brutalen Eisungeheuers",
					"Truhe der gnadenlosen Monsterkrabbe",
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		
		[91133], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe der Eisschlangenkönigin",
					"Truhe des brutalen Eisungeheuers",
					"Truhe der gnadenlosen Monsterkrabbe",
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		[91134], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Tu-Young",
					"Metin Jeon-Un",
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Oberork-Truhe",
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
					"Truhe des Roten Drachen",
					"Truhe der Verfluchten Eis Kreatur",
					"Truhe der Eisschlangenkönigin",
					"Truhe des Brutalen Eisungeheuers",
				]
			]
		]
	],
	[
		
		[91135], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Metin Jeon-Un",
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Neunschwanz-Truhe",
					"Tigergeist-Truhe",
					"Flammenkönig-Truhe",
					"Grosse Eishexe-Truhe",
					"Truhe des Roten Drachen",
					"Truhe der verfluchten Eis Kreatur",
					"Truhe der Eisschlangenkönigin",
					"Truhe des brutalen Eisungeheuers",
				]
			]
		]
	],
	[
		[91136], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des Roten Drachen",
					"Truhe der verfluchten Eis Kreatur",
					"Truhe der Eisschlangenkönigin",
					"Truhe des brutalen Eisungeheuers",
					"Truhe der gnadenlosen Monsterkrabbe",
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		
		[91137], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Feuer der Macht Truhe",	
					"Truhe des Berges",			
					"Truhe der Schlangen",
					"Truhe des Sumpfes",					
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe der Eisschlangenkönigin",
					"Truhe des brutalen Eisungeheuers",
					"Truhe der gnadenlosen Monsterkrabbe",
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		[71129], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe der Schlangen",
					"Truhe des Sumpfes",
					"Feuer der Macht Truhe",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des Roten Drachen",
					"Beran-Setaou",
				]
			]
		]
	],
	[
		
		[71123], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe der Schlangen",
					"Truhe des Sumpfes",
					"Feuer der Macht Truhe",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des Roten Drachen",
					"Beran-Setaou",
				]
			]
		]
	],
	[
		[30165], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe der Schlangen",
					"Truhe des Sumpfes",
					"Feuer der Macht Truhe",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe der gnadenlosen Monsterkrabbe",
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		
		[30167], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe der Schlangen",
					"Truhe des Sumpfes",
					"Feuer der Macht Truhe",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe der gnadenlosen Monsterkrabbe",
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		[91148], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Legendäre Verschlossene Truhe",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Azrael",
					"Runenlord",
					"Razador",
					

				]
			]
		]
	],
	[
		
		[91149], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Wird aus dem Yunari Stein+2 geuppt",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Wird aus dem Yunari Stein+2 geuppt",
				]
			]
		]
	],
	[
		[91150], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Wird aus dem Yunari Stein+3 geuppt",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Wird aus dem Yunari Stein+3 geuppt",
				]
			]
		]
	],
	[
		
		[91151], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Wird aus dem Yunari Stein+4 geuppt",
			
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Wird aus dem Yunari Stein+4 geuppt",
				]
			]
		]
	],
	[
		[91138], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe des Sumpfes",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe der gnadenlosen Monsterkrabbe",
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe der erbarmungslosen Bienenkönigin",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		
		[91139], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe des Sumpfes",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des gewaltsamen Riesenkäfers",
					"Truhe der erbarmungslosen Bienenkönigin",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		[91140], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe des Sumpfes",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe der erbarmungslosen Bienenkönigin",
					"Truhe des besessenen Eisskorpions",
					"Truhe des besessenen Dämonentotems",
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		
		[91141], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Roter Stoff ist nur bei Nemere Droppbar. Man kann ihn aber auch Craften",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Nemere",	
				]
			]
		]
	],
	[
		[91171], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe des Sumpfes",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des besessenen Eisskorpions",
				]
			]
		]
	],
	[
		
		[91172], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe des Sumpfes",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des besessenen Dämonentotems",
				]
			]
		]
	],
	[
		[91173], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"Truhe des Sumpfes",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Truhe des gnadenlosen Halbmenschens",
				]
			]
		]
	],
	[
		[91145], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"-",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Beran-Setaou",
				]
			]
		]
	],
	[
		[91144], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"-",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Runenlord",
				]
			]
		]
	],
	[
		[91143], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"-",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Nur Craftbar beim Craftingschmied",
				]
			]
		]
	],
	[
		[91142], # ItemVnums
		[
			[
				["[ Truhen und Metins ]"],
				[
					"-",				
				]

			],
			[
				["[ Dungeons und Bosse ]"],
				[
					"Nur Craftbar beim Craftingschmied",
				]
			]
		]
	]
]

# ----------------------------------------------------------------------------------------------
# 4.) Bio-System
BioQuestIndex 	= 0
BioItem 		= 0
BioQuestPhase 	= 0
# ----------------------------------------------------------------------------------------------
# 5.) Mount-System
# ACHTUNG: Auf korrekte reihenfolge achten! Siehe char_item.cpp
MountNames = [
	"Keiler", 				# 20210
	"Wolf", 				# 20111,
	"Tiger", 				# 20112,
	"Löwe", 				# 20113,
	"Weißer Löwe",			# 20114,
	"Kriegskeiler", 		# 20115,
	"Streitwolf", 			# 20116,
	"Sturmtiger", 			# 20117,
	"Schlachtenlöwe", 		# 20118,
	"Edler Rappe", 			# 20119,
	"Königstiger (Blau)", 	# 20120,
	"Königstiger (Rot)", 	# 20121,
	"Königstiger (Gold)", 	# 20122,
	"Königstiger (Grün)", 	# 20123,
	"Königstiger (Grau)", 	# 20124,
	"Königstiger (Weiß)", 	# 20125,
	"Tapferer Keiler", 		# 20209,
	"Tapferer Wolf", 		# 20210,
	"Tapferer Tiger", 		# 20211,
	"Tapferer Löwe", 		# 20212,
	"Rentier", 				# 20213,
	"Wildes Rentier", 		# 20214,
	"Tapferes Rentier", 	# 20215
	"Equus Purpur", 		# 20219,
	"Polarprädator", 		# 20221,
	"Panzerpanda", 			# 20222,
	"Wilder Raptor", 		# 20224,
	"Edler Raptor", 		# 20225,
	"Nachtmahr", 			# 20226,
	"Weißes Einhorn", 		# 20227,
	"Wilder Moa" , 			# 20229,
	"Tapferer Moa", 		# 20230,
	"Schwarzer Panther", 	# 20231,
	"Leopard", 				# 20232,
	"Silberwolf", 			# 50715,
	"Schwarzer Panther", 	# 20407,
	"Schwarzer Löwe", 		# 20408
]

# ----------------------------------------------------------------------------------------------
# 6.) DropGuide
DropGuide_Index = [
	[	
		# MonsterName (Auf korrekte Schreibweise achten!!!), placeholder einfach immer "", SlotReihen.
		["Metin des Kummers","",1],
		[
			# itemVnum, itemCount
			[80003,1],
			[91107,1],
			[91108,1],
			[91109,1],
			[91110,1]
			
		
		]
	
	],
	[
		["Metin des Kampfs","",1],
		[
			# itemVnum, itemCount
			[80003,1],
			[91107,1],
			[91108,1],
			[91109,1],
			[91110,1]
			
		
		]
	
	],
	[
		["Metin der Schlacht","",1],
		[
			# itemVnum, itemCount
			[80003,1],
			[91107,1],
			[91108,1],
			[91109,1],
			[91110,1]
			
		
		]
	
	],
	[
		["Metin der Gier","",1],
		[
			# itemVnum, itemCount
			[80003,1],
			[91107,1],
			[91108,1],
			[91109,1],
			[91110,1]
			
		
		]
	
	],
	[
		["Metin der Schwärze","",1],
		[
			# itemVnum, itemCount
			[80003,1],
			[91107,1],
			[91108,1],
			[91109,1],
			[91110,1]
			
		
		]
	
	],


]
# ----------------------------------------------------------------------------------------------
# 7.) AttrSort Function
AttributeIndex = [
	[
		[localeInfo.TOOLTIP_ATTRIBUTE_DEFENSIVE],
		[
			[1,3500],
			[2,3500],
			[7,12],
			[8,20],
			[9,20],
			[10,20],
			[11,20],
			[48,1],
			[49,1],
			[23,10],
			[24,10],
			[25,10],
			[27,15],
			[28,15],
			[41,10],
			[90,10],
			[91,10]
		]
	],
	[
		[localeInfo.TOOLTIP_ATTRIBUTE_OFFENSIVE],
		[
			[3,12],
			[4,12],
			[5,12],
			[6,12],
			
			[12,8],
			[13,8],
			[14,8],
			[15,10],
			[16,10],
			[53,50]
		]
	],	
	[
		[localeInfo.TOOLTIP_ATTRIBUTE_PVM],
		[
			[18,20],
			[19,20],
			[20,20],
			
			[21,20],
			[44,20],
			[45,20],
			[22,20]

		]
	],	
	[
		[localeInfo.TOOLTIP_ATTRIBUTE_PVP],
		[
			[29,15],
			[17,12],
			[30,15],
			[31,15],
			[32,15],
			
			[33,15],
			[34,15],
			[35,15],
			[36,15],
			[37,15],
			[38,50],
			[39,50],
			[40,50]
		]
	]	
]

# 8.) MaxPlusStone
MaxPlusStone = [28600,28601,28602,28603,28604,28605,28606,28607,28608,28609,28610,28611,28612,28613,91254,91255] # Steine eintragen für Goldenen BGSlot.


# ----------------------------------------------------------------------------------------------
# 9.) ApCoupons
# Achievement-Gutscheine. value0 wird ausgelesen für den wert.
APCoupons = [ 
	91167,
	91168,
	91169,
	91170

]


# ----------------------------------------------------------------------------------------------
# 10.) Daily-System
# DailyQuest_QID 			= 0		# QuestIndex des Daily-Systems
# DailyQuest_Monster 		= {}	# Liste der Monster die besiegt werden müssen als itemVnum.
# DailyQuest_Count 		= {}	# Anzahl der verbleibenden Monster

# DailyQuest_Reward 		= {}	# itemVnum's der Belohnungen
# DailyQuest_RewardCount 	= {} 	# itemCount's der Belohnungen

# DailyQuest_Time 		= 0		# verbl. Zeit.
# DailyQuest_Status 		= 0 	# 1:Quest // 0:Cooldown 24h
# DailyQuest_GUI 			= 0 	# Status der GUI.

DailyQuest_QID 			= 0		# QuestIndex des Daily-Systems
# DailyQuest_Status		= 3
DailyQuest_Time			= 0
# DailyQuest_Target		= {}
# DailyQuest_Count		= {}
# DailyQuest_Type			= {}	# 1:töten, 2:zerstören



# ----------------------------------------------------------------------------------------------
# 11.) UppItem Lager
UppItemStorageNormal 	= {}	# Liste mit anzahl der Normalen UppItems
UppItemStorageUsually 	= {}	# Liste mit anzahl der Gewöhnlichen UppItems
UppItemStorageRare 		= {}	# Liste mit anzahl der Seltenen UppItems

UppItemStorageItemList = [
	[],
	[ # Normal
		27987,	
		27992,	
		27993,	
		27994,	
		70031,
		91145,
		91256,
		91257,
	
	],
	[ # Gewöhnlich
		91130,
		91131,	
		91132,	
		91133,	
		91134,	
		91135,	
		91136,	
		91137,	
		71129,	
		71123,
	],
	[ # Selten
		30165,
		30167,	
		91148,
		91149,
		91150,
		91151,
		91138,	
		91139,	
		91140,	
		91141,
		91171,
		91172,
		91173,
		91142,
		91143,
		91144
		
	
	]
]


def GetUppItemCountByItemVnum_NEW(itemVnum):
	itemCount 	= 0
	i 			= 1
	
	while i < 4:
		if itemVnum in UppItemStorageItemList[i]:
			for b in xrange(len(UppItemStorageItemList[i])):
				if itemVnum == UppItemStorageItemList[i][b]:
					itemCount = GetUppItemCountByCategory(i,b+1)
		i = i + 1
	return itemCount
	
	
	
def GetUppItemCountByCategory(category,slot):
	if category == 1:
		return UppItemStorageNormal[slot]
		
	elif category == 2:
		return UppItemStorageUsually[slot]
		
	elif category == 3:
		return UppItemStorageRare[slot]
	
	else:
		chat.AppendChat(chat.CHAT_TYPE_INFO,"UnknownError in settinginfo GetUppItemCountByCategory")

	
	
	
## Alt.
def GetUppItemStorageIndexByItemVnum(itemVnum):
	i = 0
	category = 1
	info = [0,0]
	chat.AppendChat(chat.CHAT_TYPE_INFO,"------------------------------------------------")
	chat.AppendChat(chat.CHAT_TYPE_INFO,"GetUppItemStorageIndexByItemVnum: " + str(itemVnum))
	while i < 3:
		
		chat.AppendChat(chat.CHAT_TYPE_INFO,"GetUppItemStorageIndexByItemVnum: i="+str(i))
		
		for a in xrange(len(UppItemStorageItemList[category])):
			chat.AppendChat(chat.CHAT_TYPE_INFO,"GetUppItemStorageIndexByItemVnum: a="+str(a))
			if UppItemStorageItemList[category][a] == itemVnum:
				info[0] = i 
				info[1] = a
				
				chat.AppendChat(chat.CHAT_TYPE_INFO,"GetUppItemStorageIndexByItemVnum: info[0]="+str(info[0]))
				chat.AppendChat(chat.CHAT_TYPE_INFO,"GetUppItemStorageIndexByItemVnum: info[1]="+str(info[1]))
		i = i + 1
		
	chat.AppendChat(chat.CHAT_TYPE_INFO,"------------------------------------------------")
	return info
	
	
def GetUppItemCountByItemVnum(itemVnum):
	(itemCategory,itemPos) = GetUppItemStorageIndexByItemVnum(itemVnum)
	
#	chat.AppendChat(chat.CHAT_TYPE_INFO,"GetUppItemCountByItemVnum: itemCategory: + " + str(itemCategory) + ", " + str(itemPos))

	itemCategory = itemCategory - 1
	chat.AppendChat(chat.CHAT_TYPE_INFO,"itemCategory: " + str(itemCategory))
	chat.AppendChat(chat.CHAT_TYPE_INFO,"itemPos: " + str(itemPos+1))
	if itemCategory == 1:
		return UppItemStorageNormal[itemPos+1]
	
	elif itemCategory == 2:
		return UppItemStorageUsually[itemPos+1]
	
	elif itemCategory == 3:
		return UppItemStorageRare[itemPos+1]
	
	else:
		return 0


UppItemStorageQID 	= 0	# QuestIndex der Uppitem Lagers
UppItemStorageOpen 	= 0	# Status der UppItemLager Gui.



# ----------------------------------------------------------------------------------------------
# 12.) SkillbookStorage
SkillBookGoldPrice 	= 500000	# Tooltip Preis eines Fertigkeitsbuches
SkillBookCount 		= {}	# Liste mit der anzahl der vorhandenen Fertigkeitsbücher
SkillBookItemVnumList = [
	0,
	# Körperkrieger
	50401, # 1
	50402, # 2
	50403, # 3
	50404, # 4
	50405, # 5
	0, # 6
	
	# MentalKrieger
	50416, # 7 
	50417, # 8
	50418, # 9
	50419, # 10
	50420, # 11
	0, # 12
	
	# NahkampfNinja
	50431, # 13 
	50432, # 14
	50433, # 15
	50434, # 16
	50435, # 17
	0, # 18
	
	# FernkampfNinja
	50446, # 19 
	50447, # 20
	50448, # 21
	50449, # 22
	50450, # 23
	0, # 24
	
	# WaffenSura
	50461, # 25
	50462, # 26
	50463, # 27
	50464, # 28
	50465, # 29
	50466, # 30
	
	# MagieSura
	50476, # 31
	50477, # 32
	50478, # 33
	50479, # 34
	50480, # 35
	50481, # 36
	
	# DrachenSchamane
	50491, # 37
	50492, # 38
	50493, # 39
	50494, # 40
	50495, # 41
	50496, # 42
	
	# HeilSchamane
	50506, # 43
	50507, # 44
	50508, # 45
	50509, # 46
	50510, # 47
	50511 # 48

]


# ----------------------------------------------------------------------------------------------
# 13.) MapNameList
WODMapNameList={

	"metin2_map_a1"							: "Yongan",
	"metin2_map_a3"							: "Jayang",
	"metin2_map_b1"							: "Joan",
	"metin2_map_b3"							: "Bokjung",
	"metin2_map_c1"							: "Pyungmoo",
	"metin2_map_c3"							: "Bakra",
			
	"metin2_map_milgyo"						: "Hwang-Tempel",
	"metin2_map_n_desert_01"				: "Yongbi-Wüste",
	"metin2_map_n_flame_01"					: "Doyyumhwain",
	"metin2_map_spiderdungeon"				: "Spinnenhöhlen 1",
	"metin2_map_spiderdungeon_02"			: "Spinnenhöhlen 2",
	"metin2_map_spiderdungeon_03"			: "Spinnenhöhlen 3",
			
	"metin2_map_monkeydungeon"				: "Hasun-Dong",
	"metin2_map_monkeydungeon_02"			: "Jungsun-Dong",
	"metin2_map_monkeydungeon_03"			: "Sangsun-Dong",
			
	"metin2_map_wedding_01"					: "Hochzeit",
			
	"metin2_map_guild_01"					: "Jungrang",
	"metin2_map_guild_02"					: "Waryoung",
	"metin2_map_guild_03"					: "Imha",
			
	"metin2_map_trent"						: "Geisterwald",
	"metin2_map_trent02"					: "Roter Wald",
			
	"metin2_map_duel"						: "Arena",
			
	"metin2_map_WL_01"						: "Schlangenfeld",
	"metin2_map_nusluck01"					: "Land der Riesen",
			
	"metin2_map_oxevent"					: "OX-Wettbewerb",
	"metin2_map_sungzi"						: "Tal von Sungzi",
			
			
	"metin2_map_bf"							: "Gildenriegs-Gelände",
	"metin2_map_bf_02"						: "Gildenriegs-Gelände",
	"metin2_map_bf_03"						: "Gildenriegs-Gelände",
			
	"map_n_snowm_01"						: "Berg-Sohan",
			
	"metin2_map_skipia_dungeon_01"			: "Grotte der Verbannung 1",
	"metin2_map_skipia_dungeon_02"			: "Grotte der verbannung 2",
			
	"metin2_map_capedragonhead"				: "Kap des Drachenfeuers",
	"metin2_map_mt_thunder"					: "Donnerberge",
	"metin2_map_dawnmistwood"				: "Gautamakliff",
	"metin2_map_bayblacksand"				: "Nephritbucht",
	"metin2_map_naga1"						: "Ahn-Kahet",


	# Dungeons
	"map_dungeon_nephrit"					: "Schiffbruchtal",
	"map_dungeon_spidercave"				: "Spinnengruft",
	"map_dungeon_runerun"					: "Sturm auf die Runenfestung",
	"map_dungeon_bluedead"					: "Blauer Tod",
	"map_dungeon_razador"					: "Razador's Hort",
	"map_dungeon_start"						: "Übungsgelände",
	"map_dungeon_catacomb"						: "Katakomben",
	"metin2_map_deviltower1"				: "Dämonenturm",
	"metin2_map_skipia_dungeon_boss"		: "Drachenraum",
	"metin2_map_skipia_dungeon_boss2"		: "Drachenraum",
	"map_login"								: "Übungsgelände - Eingang",
	"map_intro"								: "Übungsgelände",
	"metin2_map_n_flame_dungeon_01"			: "Rotdrachen-Festung",
	"metin2_map_n_snow_dungeon_01"			: "Nemere's Warte",
	
	# Farmmaps & Bossmap
	"map_farm_1_blau"						: "Farmmap 1 (Blau)",
	"map_farm_1_gelb"						: "Farmmap 1 (Gelb)",
	"map_farm_1_rot"						: "Farmmap 1 (Rot)",
	"map_farm_2_blau"						: "Farmmap 2 (Blau)",
	"map_farm_2_gelb"						: "Farmmap 2 (Gelb)",
	"map_farm_2_rot"						: "Farmmap 2 (Rot)",
	"map_farm_3_all_empires"				: "Farmmap 3",
	"map_farm_4_all_empires"				: "Farmmap 4",
	"map_farm_5_all_empires"				: "Farmmap 5",
	"map_ayu_bossmap"						: "Bossmap",
	"metin2_map_dawnmist_dungeon_01"		: "Verwunschener Wald"

}

def GetMapNameByMapFolderName(self):
	if background.GetCurrentMapName() in WODMapNameList:
		return WODMapNameList[background.GetCurrentMapName()]
	else:
		return ""


# Zeigt MapName in Goldener Schrift unter Minimap an.		
WODSpecialMap = [
	"map_farm_1_blau",
	"map_farm_1_gelb",
	"map_farm_1_rot",
	"map_farm_2_blau",
	"map_farm_2_gelb",
	"map_farm_2_rot",
	"map_farm_3_all_empires",
	"map_farm_4_all_empires",
	"map_farm_5_all_empires",
	"map_ayu_bossmap",
	"map_dungeon_nephrit",				
	"map_dungeon_spidercave",				
	"map_dungeon_runerun",		
	"map_dungeon_bluedead",	
	"map_dungeon_razador",
	"map_dungeon_start",						
	"map_dungeon_catacomb",						
	"metin2_map_deviltower1",		
	"metin2_map_skipia_dungeon_boss",
	"metin2_map_skipia_dungeon_boss2",
	"metin2_map_n_snow_dungeon_01",
	"metin2_map_n_flame_dungeon_01"
]

def MapIsSpecialMap(self):
	if background.GetCurrentMapName() in WODSpecialMap:
		return TRUE
	else:
		return FALSE




		
# ----------------------------------------------------------------------------------------------
# 14.) treasureChest System

treasure_chest_map_block_info = [
	"do_not_remove", # <- Diesen Eintrag nicht entfernen.
	"Diese Truhe kann nur in Map1 geöffnet werden!"
]

# Truhen hier werden in der "Truhen öffnen" GUI angezeigt.
treasure_chest_vnum = [
	91116, # Akaya Truhe
	# 91107, # Krieger Fertigkeitsbücher <- Anderes System! Kann nicht mit Truhen-Öffner geöffnet werden.
	# 91108, # Ninja Fertigkeitsbücher
	# 91109, # Sura Fertigkeitsbücher
	# 91110, # Schamanen Fertigkeitsbücher
	91111, # Truhe der Seele
	91112, # Truhe des Schattens
	55214, # Truhe des Schattens v2
	91113, # Truhe des Berges
	91114, # Truhe der Schlangen
	91115, # Truhe des Sumpfes
	50070, # Oberork Truhe
	50077, # Neunschwanz Truhe
	50078, # Tigergeist Truhe
	50079, # Flammenkönig Truhe
	50138, # Truhe der großen Eishexe
	50080, # Truhe des roten Drachen
	38050, # Truhe des Feuers (FDM)
	91258, # Truhe der Verfluchten Eis-Kreatur
	91259, # Truhe der Eisschlangenkönigin
	91260, # Truhe des brutalen Eisungeheuers
	91261, # Truhe der knadenlosen Monstergrabbe
	91262, # Truhe des gewaltsamen Risenkäfers
	91263, # Truhe der erbarmungslosen Bienenköniging
	91264, # Truhe des bessesenen Eisskorpions
	91265, # Truhe des bessenen Dämonentotems
	91266, # Truhe des knadenlosen Halbmenschens
	50011 # Mondi

]

# Truhen hier bekommen einen Tooltip. aus treasure_chest_content.
treasure_chest_vnum_tooltip = [
	91116, # Akaya Truhe
	91111, # Truhe der Seele
	91112, # Truhe des Schattens
	55214, # Truhe des Schattens v2
	91113, # Truhe des Berges
	91114, # Truhe der Schlangen
	91115 # Truhe des Sumpfes

]

treasure_chest_content = [
	# -------------------------------------------------------
	[ # DevTruhe 1
		[93001],[
			[27003,50],
			[27002,80],
			[70030,1],
			[93002,1],
			[27004,30],
			[27005,10],
			[27006,180]
			
		]
	],
	# -------------------------------------------------------
	[ # Akaya2 Truhe
		[91116],[
			[30251,1],
			[25041,1],
			[91145,1],
			[71052,1],
			[91167,1],
			[91152,1],
			[91153,1],
			[50182,1],
			[91126,1],
			[91163,1],
			[50513,1],
			[27987,1]
			
		]
	],
	# -------------------------------------------------------
	[ # Truhe der Seele
		[91111],[
			[27987,1],
			[27992,1],
			[27993,1],
			[27994,1],
			[91145,1],
			[71051,1],
			[71052,1],
			[25041,1],
			[91117,1],
			[80003,1]
			
		]
	],
	# -------------------------------------------------------
	[ # Truhe des Schattens
		[91112],[
			[27987,1],
			[27992,1],
			[27993,1],
			[27994,1],
			[25041,1],
			[71052,1],
			[91119,1],
			[91121,1],
			[91118,1],
			[91123,1],
			[91124,1],
			[91145,1],
			[60002,1]
			
		]
	],
	# -------------------------------------------------------
	[ # Truhe des Schattens v2
		[55214],[
			[27987,1],
			[27992,1],
			[27993,1],
			[27994,1],
			[25041,1],
			[71052,1],
			[91119,1],
			[91121,1],
			[91118,1],
			[91123,1],
			[91124,1],
			[91145,1]
			
		]
	],
	# -------------------------------------------------------
	[ # Truhe des Berges
		[91113],[
			[71052,1],
			[91130,1],
			[91131,1],
			[91132,1],
			[91133,1],
			[91134,1],
			[91135,1],
			[91136,1],
			[91137,1],
			[91125,1],
			[70031,1],
			[91163,1],
			[50513,1],
			[91145,1],
			[160465,1]
			
		]
	],
	# -------------------------------------------------------
	[ # Truhe der Schlangen
		[91114],[
			[91130,1],
			[91131,1],
			[91132,1],
			[91133,1],
			[91134,1],
			[91135,1],
			[91136,1],
			[91137,1],
			[70031,1],
			[71052,1],
			[71123,1],
			[71129,1],
			[30165,1],
			[30167,1],
			[91163,1],
			[91145,1],
			[160466,1],
			[91148,1]
			
		]
	],
	# -------------------------------------------------------
	[ # Truhe der Sumpfgrotte
		[91115],[
			[91130,1],
			[91131,1],
			[91132,1],
			[91133,1],
			[91134,1],
			[91135,1],
			[91136,1],
			[91137,1],
			[70031,1],
			[71052,1],
			[71123,1],
			[71129,1],
			[30165,1],
			[30167,1],
			[91163,1],
			[91138,1],
			[91139,1],
			[91140,1],
			[91145,1],
			[91171,1],
			[91172,1],
			[91173,1],
			[160467,1]
		]
	],

]

# ----------------------------------------------------------------------------------------------
# 15.) Dungeon System

DungeonCooldown 	= {}
DungeonMainSettings = [
	[
	
		["Bruthöhle"],
		[50,"Arachnidenschlüssel","Nein","dungeon_spidercave.tga"],
		[
			["title","Ebene 1"],
			["normal","Zerstört den Metin des Unbehagens um das Tor zu öffnen."],
			["break",20],
			["title","Ebene 2"],
			["normal","Tötet die Monster um Schlüsselsteine zu erbeuten! Findet den richtigen für das Siegel."],
			["break",20],
			["title","Ebene 3"],
			["normal","Besiegt den Spinnenbaron."],
			["break",20],			
			["title","Ebene 4"],
			["normal","Besiegt die Spinnenbaroness."],
			["warning","Die Spinnebaroness spawnt je schwächer sie wird immer mehr Monster!"],
			["break",20]
		],
		[91050,91051],
		[True,0]
	],
	[
		["Dämonenturm (Unten)"],
		[40,"","Nein / Offen","dungeon_deviltower.tga"],
		[
			["title","Ebene 1"],
			["normal","Besiegt den Dämonenkönig."],
			["break",20],
			["title","Ebene 2"],
			["normal","Zerstört den richtigen Metinstein"],
			["break",20],
			["title","Ebene 3"],
			["normal","Öffnet die 4 Siegel mit den Schlüsselsteinen"],
			["break",20],
			["title","Ebene 4"],
			["normal","Besiegt den Stolzen Dämonenkönig."],
			["break",20],
			["title","Ebene 5"],
			["normal","Zerstört alle Metinsteine und erbeutet dann die Zin-Grotten Karte"],
			["break",20],
		],
		[91052],
		[True,1]
	],
	[
		["Dämonenturm (Oben)"],
		[60,"","Nein / Offen","dungeon_deviltower.tga"],
		[
			
			["title","Ebene 1"],
			["normal","Erbeutet von den Monstern den Zin-Bong-In Schlüssel und öffnet das Grabmal"],
			["break",20],
			
			["title","Ebene 2"],
			["normal","Besiegt den Sensenmann."],
			["break",20],
		],
		[91052,91053],
		[False,1]
	],
	[
		["Drachenraum"],
		[75,"","Nein","dungeon_dragonroom.tga"],
		[
			["normal","Besiegt Beran-Setaou!"],
			["break",20],
		],
		[91065],
		[True,2]
	],
	[
		["Katakomben"],
		[90,"","Nein","dungeon_anglar.tga"],
		[
			["title","Ebene 1"],
			["normal","Den richtigen Metin der Vergeltung finden und zerstören."],
			["break",20],
			["title","Ebene 2"],
			["normal","Besiegt alle Monsterwellen und Tartaros!"],
			["break",20],
			["title","Ebene 3"],
			["normal","Besiegt Charon!"],
			["break",20],
			["title","Ebene 4"],
			["normal","Besiegt Azrael!"],
			["break",20],
		],
		[91054,91055],
		[True,3]		
	],
	[
		["Sturm auf die Runenfestung"],
		[100,"","Nein","dungeon_runefortress.tga"],
		[
			["title","Ebene 1"],
			["normal","Zerstört den richtigen Runenfelsen!"],
			["break",20],
			["title","Ebene 2"],
			["normal","Rettet alle verletzten Soldaten aus der Wüste."],
			["break",20],	
			["title","Ebene 3"],
			["normal","Besiegt die 3 Runen-Waldhexer!"],
			["break",20],		
			["title","Ebene 4"],
			["normal","Besiegt den Runenlord!"],
			["break",20],			
		],
		[91056,91057],
		[True,4]
	],
	[
		["Rotdrachen-Festung"],
		[110,"","Nein","dungeon_razador.tga"],
		[
			["title","Ebene 1"],
			["normal","Alle Monster töten."],
			["title","Ebene 2"],
			["normal","Das Alte Siegel öffnen mit den Zahnrädern."],
			["title","Ebene 3"],
			["normal","Alle Monster töten."],
			["title","Ebene 4"],
			["normal","Den Inquisitor besiegen!"],
			["title","Ebene 5"],
			["normal","Alle Siegel in der richtigen reihenfolge öffnen."],
			["title","Ebene 6"],
			["normal","Den Metin des Fegefeuers zerstören."],
			["attention","Der ablauf der ersten 6 Ebene wird zufallsgeneriert!"],
			["title","Boss"],
			["normal","Razador besiegen!"],
		],
		[91059],
		[True,5]
	],
	[
		["Nemere's Warte"],
		[110,"","Nein","dungeon_citadell.tga"],
		[
			["normal","[ Ebene 1 ] : Finde den richtigen Weg."],
			["break",10],
			["normal","[ Ebene 2 ] : Den richtigen Frostschlüssel finden und abgeben."],
			["break",10],
			["normal","[ Ebene 3 ] : Zerstöre den Metinstein."],
			["break",10],
			["normal","[ Ebene 4 ] : Besiege alle Szel Wellen."],
			["break",10],
			["normal","[ Ebene 5 ] : Überlebe 5 Minuten (max. 5 Tode)"],
			["break",10],	
			["normal","[ Ebene 6 ] : Töte Nemere!"],
			["break",10],			
		],
		[91060,91061],
		[True,6]
	]
	# [
		# ["Schiffbruchtal"],
		# [120,"","Ja!","dungeon_shipbreakbay.tga"],
		# [
			# ["title"," Ebene 1"],
			# ["normal","Solange Monster töten bis ihr zur Mitte teleportiert werdet und dann den Metin zerstören!"],
			# ["break",15],
			
			# ["title"," Ebene 2"],
			# ["normal","Den richtigen Metinstein finden und zerstören."],
			# ["break",15],

			# ["title"," Ebene 3"],
			# ["normal","Die Schiffbruchbestie besiegen!"],
			# ["break",15],		

			# ["title"," Ebene 4"],
			# ["normal","Den Schiffbruchlord und seine Monster besiegen!"],
			# ["break",15],	

			# ["title"," Ebene 5"],
			# ["normal","Den Leviathan besiegen!"],
			# ["warning","Spawnt Metinsteine die seinen Schaden und Verteidigung erhöhen!"],
			# ["break",15]
			
		# ],
		# [91062,91063,91064]
	# ]
]	



DungeonBossDrops = [
	[
		[27001,27002],
		[
			"Schwert+9",
			"Seelenstein",
			"Geiststeine+4",
			"Passierschein"
		
		]
	]
]




# ----------------------------------------------------------------------------------------------
# 16.) AchievementSystem & MultiShopSystem


Achievement_Names = {

##	-- METINSTEINE BEGIN --
	8005 : "Metin der Schwärze",
	8006 : "Metin der Dunkelheit",
	8007 : "Metin der Eifersucht",
	8008 : "Metin der Seele",
	8009 : "Metin des Schattens",
	8010 : "Metin der Härte",
	8011 : "Metin des Teufel",
	8012 : "Metin des Sturzes",
	8014 : "Metin des Mordes",
	8018 : "Metin des Todes",
	8024 : "Metin Pung-Ma",
	8025 : "Metin Ma-An",
	8026 : "Metin Tu-Young",
	8027 : "Metin Jeon-Un",
	35020 : "Kimiko Eisberg",
	35019 : "Kimiko Schlangenei",
	8059 : "Metin der Sumpfgrotte",
	8065 : "Metin des Todes v2",
	8066 : "Metin des Mordes v2",
	8067 : "Metin Pung-Ma v2",
	8068 : "Metin Ma-An v2",
##	-- METINSTEINE END --

##	-- BOSSE BEGIN --
	691 : "Oberork",
	1901 : "Neunschwanz",
	1304 : "Gelber Tigergeist",
	2206 : "Flammenkönig",
	1192 : "Große Eishexe",
	2291 : "Roter Drache",
	50699 : "Brutales Eisungeheuer",
	50698 : "Eisschlangenkönigin",
	50696 : "Besessener Eisskorpion",
	50691 : "Gewaltsamer Riesenkäfer",
	50692 : "Erbarmungslos Bienenkönigin",
	50690 : "Knadenlose Monstergrabbe",
	50697 : "Verfluchte Eis-Kreatur",
	50695 : "Knadenloser Halbmensch",
	50694 : "Besessener Dämonentotem",
##	-- BOSSE END --

##	-- DUNGEONS BEGIN --
	10000 : "Spinnengruft",
	10001 : "Dämonenturm",
	10002 : "Drachenraum",
	10003 : "Katakomben",
	10004 : "Runenfestung",
	10005 : "Rotdrachen-Festung",
	10006 : "Nemeres Warte",

	
	
##	-- DUNGEONS END --

##	-- GUTSCHEINE BEGIN --
	10100 : "Gutschein eingelöst",
	10101 : "Gutschein eingelöst",
	10102 : "Gutschein eingelöst",
	10103 : "Gutschein eingelöst"

##	-- GUTSCHEINE END --

}

Achievement_Statistic = {

	1 			: {},
	2 			: {},
	3 			: {},
	"status"	: 0,

}



# Achievement = {
	# "statistic" : {"boss" : {},"stone" : {},"dungeons" : {}}

	
# }


# Multishop = {
	# # pos # itemVnum # slot0 # slot1 # slot2 # currencyType # currencyAmount
	# "itemInformation" : {"page0" : {},"page1" : {},"page2" : {}}
	# "shopName" : "",
	# "shopIndex" : 0,
	
# }






# ----------------------------------------------------------------------------------------------
# 17.) IntroDungeon

IntroDungeonQuestIndex		= 0
IntroDungeonQuestBoxIndex	= 0
IntroDungeonQuestBoxStatus	= 0
IntroDungeonTextLines = [
	
	[ # pc.intro_textbox(0)
		[
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Noch ein Titel","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"]		
		],
		[
			["achievement","head_img"],
			["----------------------------------------------------------------------------","title","center"],
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur elitr, sed diam","no_align"],
			["Lorem ipsum  sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit , consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],		
		]
	],
	[ # pc.intro_textbox(1)
		[
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Noch ein Titel","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"]		
		],
		[
			["achievement","head_img"],
			["----------------------------------------------------------------------------","title","center"],
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur elitr, sed diam","no_align"],
			["Lorem ipsum  sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit , consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],		
		]
	],	
	[ # pc.intro_textbox(2)
		[
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Noch ein Titel","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"]		
		],
		[
			["achievement","head_img"],
			["----------------------------------------------------------------------------","title","center"],
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur elitr, sed diam","no_align"],
			["Lorem ipsum  sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit , consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],		
		]
	],	
	[ # pc.intro_textbox(3)
		[
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Noch ein Titel","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"]		
		],
		[
			["achievement","head_img"],
			["----------------------------------------------------------------------------","title","center"],
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur elitr, sed diam","no_align"],
			["Lorem ipsum  sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit , consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],		
		]
	],	
	[ # pc.intro_textbox(4)
		[
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Noch ein Titel","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"]		
		],
		[
			["achievement","head_img"],
			["----------------------------------------------------------------------------","title","center"],
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur elitr, sed diam","no_align"],
			["Lorem ipsum  sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit , consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],		
		]
	],	
	[ # pc.intro_textbox(5)
		[
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Noch ein Titel","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor in","normal_color","no_align"]		
		],
		[
			["achievement","head_img"],
			["----------------------------------------------------------------------------","title","center"],
			["achievement","head_img"],
			["Einleitung","title","center"],
			["----------------------------------------------------------------------------","title","center"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur elitr, sed diam","no_align"],
			["Lorem ipsum  sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit , consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["Lorem dolor sit amet, consetetur sadipscing elitr, sed diam","normal_color","no_align"],
			["","normal_color","no_align"],
			["","normal_color","no_align"],
			["Sonstiger Title","title","center"],		
		]
	]
	
]


# ----------------------------------------------------------------------------------------------
# 18.) GuideBoard



GuideBoardTextLines = [
	
	[ # pc.open_guide(0) -- AH-YU DIETRICH SYSTEM
		[
			["dietrich_guide","head_img"],
			["Was ist das Dietrich System?","title"],
			["----------------------------------------------------------------------------","warning"],
			["Mit dem Dietrichsystem auf Kimiko hast du die Möglichkeit verschlossene Truhen","attention"],
			["zu öffnen. Diese Truhen gibt es in 5 verschiedenen Stufen.","attention"],
			["Der Dietrich ist auch auf maximal Stufe 5 levelbar.","attention"],
			["----------------------------------------------------------------------------","warning"],
			["","normal_color"],
			["","normal_color"],
			["Wo bekomme ich den Dietrich und die Kisten?","title"],
			["----------------------------------------------------------------------------","warning"],
			["Den Dietrich bekommst du mit Level 30 automatisch in dein Inventar gelegt.","attention"],
			["Die verschlossenen Truhen werden als Alternativdropp fallen gelassen.","attention"],
			["Information: Es droppt immer eine Truhe mit zufälliger Stufe!","title"],
			["Du kannst die Truhen auch auf dem Markt verkaufen.","attention"],
			["----------------------------------------------------------------------------","warning"],
			["","normal_color"],
			["","normal_color"],
			["Wie öffnet man eine verschlossene Truhe?","title"],
			["----------------------------------------------------------------------------","warning"],
			["Ziehe deinen Dietrich auf die verschlossene Truhe.","attention"],
			["Du kannst jedoch nur Truhen entsprechend deiner Stufe öffnen.","attention"],
			["Durch das öffnen einer Truhe, steigen die Punkte des Dietrichs.","attention"],
			["----------------------------------------------------------------------------","warning"],
		],
		[
			["dietrich_guide","head_img"],
			["Wie kann ich meinen Dietrich verbessern?","title"],
			["----------------------------------------------------------------------------","warning"],
			["Hat dein Dietrich die maximale Punkteanzahl erreicht,","attention"],
			["kannst du ihn bei Ah-Yu auf die nächste Stufe verbessern lassen.","attention"],
			["Information: Das verbessern kann fehlschlagen!","title"],
			["Bei einem Fehlschlag werden Punkte von deinem Dietrich abgezogen!","title"],
			["Verschlossene Truhen die unter deinem Stufenrank liegen,","attention"],
			["lassen sich öffnen. Truhen über deinem Dietrichrank nicht.","attention"],
			["----------------------------------------------------------------------------","warning"],
			["","normal_color"],
			["","normal_color"],
		]
	],
	[
		[
			["achievement","head_img"],
			["Einleitung","title"],
			["----------------------------------------------------------------------------","title"],
			["Die Kampfzone erlaubt es dir dein können im PVP zu beweisen,","normal_color"],
			["tritt gegen 3 weitere Spieler an und erreiche die höchste Punktzahl","normal_color"],
			["","normal_color"]
		]
	]
]




# ----------------------------------------------------------------------------------------------
# 18.) Schmiedehandbuch



SchmiedeHandBuchInfos = [
	[
		[
			["Krieger",67],
			[
				[ ## Nymphenschwert
					[160],
					[ # +1
						[27987,1]
					],
					[ # +2
						[27987,1]
					],
					[ # +3
						[27987,1]
					],
					[ # +4
						[27987,1],
						[27992,1]
					],
					[ # +5
						[27987,1],
						[27992,1]
					],
					[ # +6
						[27987,1],
						[27993,1]
					],
					[ # +7
						[27987,1],
						[27993,1]
					],
					[ # +8
						[27987,1],
						[27994,1]
					],
					[ # +9
						[27987,1],
						[27994,1]
					]
				],
				[ ## Giftschwert
					[180],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +3
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +4
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +5
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +6
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +7
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +8
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +9
						[27992,5],
						[27993,5],
						[27994,5]
					]
				],
				[ ## Halbmondklinge
					[400],
					[ # +1
						[91130,1],
						[27992,3],
						[27993,3],
						[27993,3]
					],
					[ # +2
						[91130,1],
						[27993,3],
						[27994,1],
						[27993,3]
					],
					[ # +3
						[91130,2],
						[91131,1],
						[27994,4]
					],
					[ # +4
						[91130,2],
						[91131,1],
						[27994,5]
					],
					[ # +5
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +6
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +7
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +8
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +9
						[91131,1],
						[71123,1],
						[71129,1]
					]
				],
				[ ## Heiliges Götterschwert
					[7300],
					[ # +1
						[91130,1],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +4
						[91130,2],
						[91131,2],
						[91134,2]
					],        
					[ # +5
						[91130,3],
						[91131,2],
						[91135,2]
					],
					[ # +6
						[91130,3],
						[91131,3],
						[91135,2]
					],
					[ # +7
						[91131,2],
						[91134,2],
						[91135,2]
					],
					[ # +8
						[91131,3],
						[91134,2],
						[91135,2]
					],
					[ # +9
						[91132,2],
						[71123,2],
						[71129,2]
					]
				],
				[ ## Giftige Klinge
					[35330],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],        
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71123,3],
						[71129,3]
					]
				],
				[ ## Grünaugen Schwert
					[35140],
					[ # +1
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +2
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +3
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +4
						[91131,3],
						[91132,3],
						[91135,3]
					],        
					[ # +5
						[91132,2],
						[91133,2],
						[91136,2]
					],
					[ # +6
						[91132,3],
						[91133,3],
						[91136,2]
					],
					[ # +7
						[91133,3],
						[91135,3],
						[91136,3]
					],
					[ # +8
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +9
						[91133,3],
						[30165,1],
						[30167,1]
					]
				],
				[ ## Rauchstahlschwert
					[54130],
					[ # +1
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +2
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +3
						[91131,3],
						[91132,3],
						[91135,3]
					],
					[ # +4
						[91131,4],
						[91132,4],
						[91135,4]
					],        
					[ # +5
						[91132,3],
						[91133,3],
						[91136,3]
					],
					[ # +6
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +7
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +8
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +9
						[91133,3],
						[30165,2],
						[30167,2]
					]
				],
				[ ## Albtraumschwert
					[54060],
					[ # +1
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +2
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +3
						[91131,4],
						[91132,4],
						[91135,4]
					],
					[ # +4
						[91131,5],
						[91132,5],
						[91135,5]
					],        
					[ # +5
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +6
						[91132,5],
						[91133,5],
						[91136,5]
					],
					[ # +7
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +8
						[91133,5],
						[91136,5],
						[91137,5]
					],
					[ # +9
						[91133,4],
						[30165,3],
						[30167,3]
					]
				],
				[ ## Rubin Runenschwert
					[54200],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],        
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71123,20],
						[71129,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubinschwert
					[54210],
					[ # +1
						[91130,10],
						[91131,10],
						[91134,10]
					],
					[ # +2
						[91131,10],
						[91132,10],
						[91135,10]
					],
					[ # +3
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +4
						[91148,1],
						[91133,10],
						[91137,10]
					],        
					[ # +5
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +6
						[91150,1],
						[30165,20],
						[30167,20]
					],
					[ # +7
						[91151,1],
						[91138,5],
						[91139,1]
					],
					[ # +8
						[91138,10],
						[91139,2],
						[91140,1]
					],
					[ # +9
						[91139,8],
						[91140,4],
						[91141,1]
					]
				],
				[ ## Magnetische Klinge
					[3140],
					[ # +1
						[27987,1]
					],
					[ # +2
						[27987,1]
					],
					[ # +3
						[27987,1]
					],
					[ # +4
						[27987,1],
						[27992,1]
					],
					[ # +5
						[27987,1],
						[27992,1]
					],
					[ # +6
						[27987,1],
						[27993,1]
					],
					[ # +7
						[27987,1],
						[27993,1]
					],
					[ # +8
						[27987,1],
						[27994,1]
					],
					[ # +9
						[27987,1],
						[27994,1]
					]
				],
				[ ## Grollschwert
					[3160],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +3
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +4
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +5
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +6
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +7
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +8
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +9
						[27992,5],
						[27993,5],
						[27994,5]
					]
				],
				[ ## Drachengottspalter
					[3200],
					[ # +1
						[91130,1],
						[27992,3],
						[27993,3]
					],
					[ # +2
						[91130,1],
						[27993,3],
						[27994,3]
					],
					[ # +3
						[91130,2],
						[91131,1],
						[27994,4]
					],
					[ # +4
						[91130,2],
						[91131,1],
						[27994,5]
					],
					[ # +5
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +6
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +7
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +8
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +9
						[91131,1],
						[71123,1],
						[71129,1]
					]
				],
				[ ## Untergangsspalter
					[35170],
					[ # +1
						[91130,1],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +4
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +5
						[91130,3],
						[91131,2],
						[91135,2]
					],
					[ # +6
						[91130,3],
						[91131,3],
						[91135,2]
					],
					[ # +7
						[91131,2],
						[91134,2],
						[91135,2]
					],
					[ # +8
						[91131,3],
						[91134,2],
						[91135,2]
					],
					[ # +9
						[91132,2],
						[71123,2],
						[71129,2]
					]
				],
				[ ## Blauer Drachenspalter
					[35150],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71123,3],
						[71129,3]
					]
				],
				[ ## Geistlicher Spalter
					[35160],
					[ # +1
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +2
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +3
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +4
						[91131,3],
						[91132,3],
						[91135,3]
					],
					[ # +5
						[91132,2],
						[91133,2],
						[91136,2]
					],
					[ # +6
						[91132,3],
						[91133,3],
						[91136,2]
					],
					[ # +7
						[91133,3],
						[91135,3],
						[91136,3]
					],
					[ # +8
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +9
						[91133,3],
						[30165,1],
						[30167,1]
					]
				],
				[ ## Rauchstahlspalter
					[54140],
					[ # +1
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +2
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +3
						[91131,3],
						[91132,3],
						[91135,3]
					],
					[ # +4
						[91131,4],
						[91132,4],
						[91135,4]
					],
					[ # +5
						[91132,3],
						[91133,3],
						[91136,3]
					],
					[ # +6
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +7
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +8
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +9
						[91133,3],
						[30165,2],
						[30167,2]
					]
				],
				[ ## Albtaumspalter
					[54070],
					[ # +1
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +2
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +3
						[91131,4],
						[91132,4],
						[91135,4]
					],
					[ # +4
						[91131,5],
						[91132,5],
						[91135,5]
					],
					[ # +5
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +6
						[91132,5],
						[91133,5],
						[91136,5]
					],
					[ # +7
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +8
						[91133,5],
						[91136,5],
						[91137,5]
					],
					[ # +9
						[91133,4],
						[30165,3],
						[30167,3]
					]
				],
				[ ## Roter Königsspalter
					[54230],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71123,20],
						[71129,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubinspalter
					[54220],
					[ # +1
						[91130,10],
						[91131,10],
						[91134,10]
					],
					[ # +2
						[91131,10],
						[91132,10],
						[91135,10]
					],
					[ # +3
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +4
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +5
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +6
						[91150,1],
						[30165,20],
						[30167,20]
					],
					[ # +7
						[91151,1],
						[91138,5],
						[91139,1]
					],
					[ # +8
						[91138,10],
						[91139,2],
						[91140,1]
					],
					[ # +9
						[91139,8],
						[91140,4],
						[91141,1]
					]
				],
			]
		],
		[
			["Ninja",63],
			[
				[ ## Blitzmesser
					[1110],
					[ # +1
						[27987,1]
					],
					[ # +2
						[27987,1]
					],
					[ # +3
						[27987,1]
					],
					[ # +4
						[27987,1],
						[27992,1]
					],
					[ # +5
						[27987,1],
						[27992,1]
					],
					[ # +6
						[27987,1],
						[27993,1]
					],
					[ # +7
						[27987,1],
						[27993,1]
					],
					[ # +8
						[27987,1],
						[27994,1]
					],
					[ # +9
						[27987,1],
						[27994,1]
					]
				],
				[ ## Teufelsflügel-Chakram
					[1130],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +3
						[27992,2],
						[27993,3],
						[27994,2]
					],
					[ # +4
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +5
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +6
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +7
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +8
						[27992,3],
						[27994,3],
						[27994,3]
					],
					[ # +9
						[27992,5],
						[27993,5],
						[27994,5]
					]
				],
				[ ## Aqua Messer
					[8080],
					[ # +1
						[91130,1],
						[27992,3],
						[27993,3],
					],
					[ # +2
						[91130,1],
						[27993,3],
						[27994,3],
					],
					[ # +3
						[91130,2],
						[91131,1],
						[27994,4]
					],
					[ # +4
						[91130,2],
						[91131,1],
						[27994,5]
					],
					[ # +5
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +6
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +7
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +8
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +9
						[91131,1],
						[71123,1],
						[71129,1]
					]
				],
				[ ## Spitz Messer
					[35010],
					[ # +1
						[91130,1],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +4
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +5
						[91130,3],
						[91131,2],
						[91135,2]
					],
					[ # +6
						[91130,3],
						[91131,3],
						[91135,2]
					],
					[ # +7
						[91131,2],
						[91134,2],
						[91135,2]
					],
					[ # +8
						[91131,3],
						[91134,2],
						[91135,2]
					],
					[ # +9
						[91132,2],
						[71123,2],
						[71129,2]
					]
				],
				[ ## Dreikant Messer
					[35040],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71123,3],
						[71129,3]
					]
				],
				[ ## Drachen Dolche
					[35020],
					[ # +1
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +2
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +3
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +4
						[91131,3],
						[91132,3],
						[91135,3]
					],
					[ # +5
						[91132,2],
						[91133,2],
						[91136,2]
					],
					[ # +6
						[91132,3],
						[91133,3],
						[91136,2]
					],
					[ # +7
						[91133,3],
						[91135,3],
						[91136,3]
					],
					[ # +8
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +9
						[91133,3],
						[30165,1],
						[30167,1]
					]
				],
				[ ## Rauchstahldolche
					[54150],
					[ # +1
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +2
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +3
						[91131,3],
						[91132,3],
						[91135,3]
					],
					[ # +4
						[91131,4],
						[91132,4],
						[91135,4]
					],
					[ # +5
						[91132,3],
						[91133,3],
						[91136,3]
					],
					[ # +6
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +7
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +8
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +9
						[91133,3],
						[30165,2],
						[30167,2]
					]
				],
				[ ## Albtraumdolche
					[54080],
					[ # +1
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +2
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +3
						[91131,4],
						[91132,4],
						[91135,4]
					],
					[ # +4
						[91131,5],
						[91132,5],
						[91135,5]
					],
					[ # +5
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +6
						[91132,5],
						[91133,5],
						[91136,5]
					],
					[ # +7
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +8
						[91133,5],
						[91136,5],
						[91137,5]
					],
					[ # +9
						[91133,4],
						[30165,3],
						[30167,3]
					]
				],
				[ ## Rubin Fünf Elemete Klinge
					[54240],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71123,20],
						[71129,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubindolche
					[54250],
					[ # +1
						[91130,10],
						[91131,10],
						[91134,10]
					],
					[ # +2
						[91131,10],
						[91132,10],
						[91135,10]
					],
					[ # +3
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +4
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +5
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +6
						[91150,1],
						[30165,20],
						[30167,20]
					],
					[ # +7
						[91151,1],
						[91138,5],
						[91139,1]
					],
					[ # +8
						[91138,10],
						[91139,2],
						[91140,1]
					],
					[ # +9
						[91139,8],
						[91140,4],
						[91141,1]
					]
				],
			]
		],
		[
			["Sura",73],
			[
				[ ## Nymphenschwert
					[160],
					[ # +1
						[27987,1]
					],
					[ # +2
						[27987,1]
					],
					[ # +3
						[27987,1]
					],
					[ # +4
						[27987,1],
						[27992,1]
					],
					[ # +5
						[27987,1],
						[27992,1]
					],
					[ # +6
						[27987,1],
						[27993,1]
					],
					[ # +7
						[27987,1],
						[27993,1]
					],
					[ # +8
						[27987,1],
						[27994,1]
					],
					[ # +9
						[27987,1],
						[27994,1]
					]
				],
				[ ## Giftschwert
					[180],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +3
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +4
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +5
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +6
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +7
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +8
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +9
						[27992,5],
						[27993,5],
						[27994,5]
					]
				],
				[ ## Halbmondklinge
					[400],
					[ # +1
						[91130,1],
						[27992,3],
						[27993,3],
						[27993,3]
					],
					[ # +2
						[91130,1],
						[27993,3],
						[27994,1],
						[27993,3]
					],
					[ # +3
						[91130,2],
						[91131,1],
						[27994,4]
					],
					[ # +4
						[91130,2],
						[91131,1],
						[27994,5]
					],
					[ # +5
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +6
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +7
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +8
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +9
						[91131,1],
						[71123,1],
						[71129,1]
					]
				],
				[ ## Heiliges Götterschwert
					[7300],
					[ # +1
						[91130,1],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +4
						[91130,2],
						[91131,2],
						[91134,2]
					],        
					[ # +5
						[91130,3],
						[91131,2],
						[91135,2]
					],
					[ # +6
						[91130,3],
						[91131,3],
						[91135,2]
					],
					[ # +7
						[91131,2],
						[91134,2],
						[91135,2]
					],
					[ # +8
						[91131,3],
						[91134,2],
						[91135,2]
					],
					[ # +9
						[91132,2],
						[71123,2],
						[71129,2]
					]
				],
				[ ## Giftige Klinge
					[35330],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],        
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71123,3],
						[71129,3]
					]
				],
				[ ## Grünaugen Schwert
					[35140],
					[ # +1
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +2
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +3
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +4
						[91131,3],
						[91132,3],
						[91135,3]
					],        
					[ # +5
						[91132,2],
						[91133,2],
						[91136,2]
					],
					[ # +6
						[91132,3],
						[91133,3],
						[91136,2]
					],
					[ # +7
						[91133,3],
						[91135,3],
						[91136,3]
					],
					[ # +8
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +9
						[91133,3],
						[30165,1],
						[30167,1]
					]
				],
				[ ## Rauchstahlschwert
					[54130],
					[ # +1
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +2
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +3
						[91131,3],
						[91132,3],
						[91135,3]
					],
					[ # +4
						[91131,4],
						[91132,4],
						[91135,4]
					],        
					[ # +5
						[91132,3],
						[91133,3],
						[91136,3]
					],
					[ # +6
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +7
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +8
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +9
						[91133,3],
						[30165,2],
						[30167,2]
					]
				],
				[ ## Albtraumschwert
					[54060],
					[ # +1
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +2
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +3
						[91131,4],
						[91132,4],
						[91135,4]
					],
					[ # +4
						[91131,5],
						[91132,5],
						[91135,5]
					],        
					[ # +5
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +6
						[91132,5],
						[91133,5],
						[91136,5]
					],
					[ # +7
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +8
						[91133,5],
						[91136,5],
						[91137,5]
					],
					[ # +9
						[91133,4],
						[30165,3],
						[30167,3]
					]
				],
				[ ## Rubin Runenschwert
					[54200],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],        
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71123,20],
						[71129,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubinschwert
					[54210],
					[ # +1
						[91130,10],
						[91131,10],
						[91134,10]
					],
					[ # +2
						[91131,10],
						[91132,10],
						[91135,10]
					],
					[ # +3
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +4
						[91148,1],
						[91133,10],
						[91137,10]
					],        
					[ # +5
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +6
						[91150,1],
						[30165,20],
						[30167,20]
					],
					[ # +7
						[91151,1],
						[91138,5],
						[91139,1]
					],
					[ # +8
						[91138,10],
						[91139,2],
						[91140,1]
					],
					[ # +9
						[91139,8],
						[91140,4],
						[91141,1]
					]
				],
			]
		],
		[
			["Schamane",74],
			[
				[ ## Donnervogelglocke
					[5090],
					[ # +1
						[27987,1]
					],
					[ # +2
						[27987,1]
					],
					[ # +3
						[27987,1]
					],
					[ # +4
						[27987,1],
						[27992,1]
					],
					[ # +5
						[27987,1],
						[27992,1]
					],
					[ # +6
						[27987,1],
						[27993,1]
					],
					[ # +7
						[27987,1],
						[27993,1]
					],
					[ # +8
						[27987,1],
						[27994,1]
					],
					[ # +9
						[27987,1],
						[27994,1]
					]
				],
				[ ## Orchideenglocke
					[5120],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +3
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +4
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +5
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +6
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +7
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +8
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +9
						[27992,5],
						[27993,5],
						[27994,5]
					]
				],
				[ ## Schnitterglocke
					[5130],
					[ # +1
						[91130,1],
						[27992,3],
						[27993,3],
					],
					[ # +2
						[91130,1],
						[27993,3],
						[27994,3],
					],
					[ # +3
						[91130,2],
						[91131,1],
						[27994,4]
					],
					[ # +4
						[91130,2],
						[91131,1],
						[27994,5]
					],
					[ # +5
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +6
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +7
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +8
						[91130,2],
						[91131,2],
						[91135,1]
					],
					[ # +9
						[91131,1],
						[71123,1],
						[71129,1]
					]
				],
				[ ## Drachenteufelsglocke
					[570],
					[ # +1
						[91130,1],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +4
						[91130,2],
						[91131,2],
						[91134,2]
					],        
					[ # +5
						[91130,3],
						[91131,2],
						[91135,2]
					],
					[ # +6
						[91130,3],
						[91131,3],
						[91135,2]
					],
					[ # +7
						[91131,2],
						[91134,2],
						[91135,2]
					],
					[ # +8
						[91131,3],
						[91134,2],
						[91135,2]
					],
					[ # +9
						[91132,2],
						[71123,2],
						[71129,2]
					]
				],
				[ ## Feuervogel Glocke
					[35230],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],        
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71123,3],
						[71129,3]
					]
				],
				[ ## Spinnen Glocke
					[35240],
					[ # +1
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +2
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +3
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +4
						[91131,3],
						[91132,3],
						[91135,3]
					],        
					[ # +5
						[91132,2],
						[91133,2],
						[91136,2]
					],
					[ # +6
						[91132,3],
						[91133,3],
						[91136,2]
					],
					[ # +7
						[91133,3],
						[91135,3],
						[91136,3]
					],
					[ # +8
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +9
						[91133,3],
						[30165,1],
						[30167,1]
					]
				],
				[ ## Rauchstahlglocke
					[54190],
					[ # +1
						[91130,3],
						[91131,3],
						[91134,3]
					],
					[ # +2
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +3
						[91131,3],
						[91132,3],
						[91135,3]
					],
					[ # +4
						[91131,4],
						[91132,4],
						[91135,4]
					],        
					[ # +5
						[91132,3],
						[91133,3],
						[91136,3]
					],
					[ # +6
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +7
						[91133,3],
						[91136,3],
						[91137,3]
					],
					[ # +8
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +9
						[91133,3],
						[30165,2],
						[30167,2]
					]
				],
				[ ## Albtraumglocke
					[54120],
					[ # +1
						[91130,4],
						[91131,4],
						[91134,4]
					],
					[ # +2
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +3
						[91131,4],
						[91132,4],
						[91135,4]
					],
					[ # +4
						[91131,5],
						[91132,5],
						[91135,5]
					],        
					[ # +5
						[91132,4],
						[91133,4],
						[91136,4]
					],
					[ # +6
						[91132,5],
						[91133,5],
						[91136,5]
					],
					[ # +7
						[91133,4],
						[91136,4],
						[91137,4]
					],
					[ # +8
						[91133,5],
						[91136,5],
						[91137,5]
					],
					[ # +9
						[91133,4],
						[30165,3],
						[30167,3]
					]
				],
				[ ## Rubin Drachengeistglocke
					[54260],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],        
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71123,20],
						[71129,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubinglocke
					[54270],
					[ # +1
						[91130,10],
						[91131,10],
						[91134,10]
					],
					[ # +2
						[91131,10],
						[91132,10],
						[91135,10]
					],
					[ # +3
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +4
						[91148,1],
						[91133,10],
						[91137,10]
					],        
					[ # +5
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +6
						[91150,1],
						[30165,20],
						[30167,20]
					],
					[ # +7
						[91151,1],
						[91138,5],
						[91139,1]
					],
					[ # +8
						[91138,10],
						[91139,2],
						[91140,1]
					],
					[ # +9
						[91139,8],
						[91140,4],
						[91141,1]
					]
				],
			]
		],
		#########################################################################################
		[
			["Rüstungen",65],
			[
				[ ## Rubinrüstung
					[15550],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubinanzug
					[15570],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubinpanzer
					[15590],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
				[ ## Rubinkleidung
					[15610],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				]
			]
		],
		#########################################################################################
		[
			["Schilde",74],
			[
				[ ## PvM-Schild
					[91330],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +3
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +4
						[27992,5],
						[27993,5],
						[27994,5]
					],
					[ # +5
						[27992,5],
						[91130,1],
						[91134,1]
					],
					[ # +6
						[27993,5],
						[91130,2],
						[91134,2]
					],
					[ # +7
						[27994,5],
						[91130,3],
						[91134,3]
					],
					[ # +8
						[91130,5],
						[91131,1],
						[91135,1]
					],
					[ # +9
						[91130,5],
						[91131,2],
						[91135,2]
					]
				],
				[ ## Citrinschild
					[91340],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71129,3],
						[71123,3]
					]
				],
				[ ## Rubinschild
					[91350],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],		
			]
		],	
		#########################################################################################
		[
			["Schuhe",74],
			[
			
				[ ## Phönix Schuhe
					[15200],
					[ # +1

					],
					[ # +2

					],
					[ # +3

					],
					[ # +4

					],
					[ # +5

					],
					[ # +6

					],
					[ # +7

						[27992,1],
					],
					[ # +8

						[27993,1],
					],
					[ # +9
						[27994,1],

					]
				],
			
				[ ## Kimiko Schuhe
					[91390],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +3
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +4
						[27992,5],
						[27993,5],
						[27994,5]
					],
					[ # +5
						[27992,5],
						[91130,1],
						[91134,1]
					],
					[ # +6
						[27993,5],
						[91130,2],
						[91134,2]
					],
					[ # +7
						[27994,5],
						[91130,3],
						[91134,3]
					],
					[ # +8
						[91130,5],
						[91131,1],
						[91135,1]
					],
					[ # +9
						[91134,5],
						[91131,2],
						[91135,2]
					]
				],
				[ ## Citrinschuhe
					[91400],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71129,3],
						[71123,3]
					]
				],
				[ ## Rubinschuhe
					[91410],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
			]
		],	
		#########################################################################################
		[
			["Armbänder",65],
			[
			
				[ ## HTA Arbmband
					[14200],
					[ # +1

					],
					[ # +2

					],
					[ # +3

					],
					[ # +4

					],
					[ # +5

					],
					[ # +6

					],
					[ # +7

						[27992,1],
					],
					[ # +8

						[27993,1],
					],
					[ # +9
						[27994,1],
					]
				],
			
				[ ## Kimiko Arbmband
					[91480],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +3
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +4
						[27992,5],
						[27993,5],
						[27994,5]
					],
					[ # +5
						[27992,5],
						[91130,1],
						[91134,1]
					],
					[ # +6
						[27993,5],
						[91130,2],
						[91134,2]
					],
					[ # +7
						[27994,5],
						[91130,3],
						[91134,3]
					],
					[ # +8
						[91130,5],
						[91131,1],
						[91135,1]
					],
					[ # +9
						[91134,5],
						[91131,2],
						[91135,2]
					]
				],
				[ ## Citrinarmband
					[91490],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71129,3],
						[71123,3]
					]
				],
				[ ## Rubinarmband
					[91500],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
			]
		],
		#########################################################################################
		[
			["Halsketten",66],
			[
			
				[ ## HTK
					[16200],
					[ # +1

					],
					[ # +2

					],
					[ # +3

					],
					[ # +4

					],
					[ # +5

					],
					[ # +6

					],
					[ # +7

						[27992,1],
					],
					[ # +8

						[27993,1],
					],
					[ # +9
						[27994,1],
					]
				],
			
				[ ## Kimiko Kette
					[91450],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +3
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +4
						[27992,5],
						[27993,5],
						[27994,5]
					],
					[ # +5
						[27992,5],
						[91130,1],
						[91134,1]
					],
					[ # +6
						[27993,5],
						[91130,2],
						[91134,2]
					],
					[ # +7
						[27994,5],
						[91130,3],
						[91134,3]
					],
					[ # +8
						[91130,5],
						[91131,1],
						[91135,1]
					],
					[ # +9
						[91134,5],
						[91131,2],
						[91135,2]
					]
				],
				[ ## Citrinhalskette
					[91460],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71129,3],
						[71123,3]
					]
				],
				[ ## Rubinkette
					[91470],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],	
			]
		],	
		#########################################################################################
		[
			["Ohrringe",69],
			[
			
				[ ## HTO
					[17200],
					[ # +1

					],
					[ # +2

					],
					[ # +3

					],
					[ # +4

					],
					[ # +5

					],
					[ # +6

					],
					[ # +7

						[27992,1],
					],
					[ # +8

						[27993,1],
					],
					[ # +9
						[27994,1],
					]
				],
			
				[ ## Kimiko Ohrringe
					[91360],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +3
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +4
						[27992,5],
						[27993,5],
						[27994,5]
					],
					[ # +5
						[27992,5],
						[91130,1],
						[91134,1]
					],
					[ # +6
						[27993,5],
						[91130,2],
						[91134,2]
					],
					[ # +7
						[27994,5],
						[91130,3],
						[91134,3]
					],
					[ # +8
						[91130,5],
						[91131,1],
						[91135,1]
					],
					[ # +9
						[91134,5],
						[91131,2],
						[91135,2]
					]
				],
				[ ## Citrinohrringe
					[91370],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71129,3],
						[71123,3]
					]
				],
				[ ## Rubinohrringe
					[91380],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],		
			]
		],	
		#########################################################################################
		[
			["Helme",75],
			[
				[ ## PvM Helm
					[91300],
					[ # +1
						[27992,1],
						[27993,1],
						[27994,1]
					],
					[ # +2
						[27992,2],
						[27993,2],
						[27994,2]
					],
					[ # +3
						[27992,3],
						[27993,3],
						[27994,3]
					],
					[ # +4
						[27992,5],
						[27993,5],
						[27994,5]
					],
					[ # +5
						[27992,5],
						[91130,1],
						[91134,1]
					],
					[ # +6
						[27993,5],
						[91130,2],
						[91134,2]
					],
					[ # +7
						[27994,5],
						[91130,3],
						[91134,3]
					],
					[ # +8
						[91130,5],
						[91131,1],
						[91135,1]
					],
					[ # +9
						[91130,5],
						[91131,2],
						[91135,2]
					]
				],
				[ ## Citrinhelm
					[91310],
					[ # +1
						[91130,2],
						[91131,1],
						[91134,1]
					],
					[ # +2
						[91130,2],
						[91131,2],
						[91134,1]
					],
					[ # +3
						[91130,2],
						[91131,2],
						[91134,2]
					],
					[ # +4
						[91131,2],
						[91132,2],
						[91134,2]
					],
					[ # +5
						[91131,2],
						[91132,2],
						[91135,2]
					],
					[ # +6
						[91131,3],
						[91132,2],
						[91135,2]
					],
					[ # +7
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +8
						[91131,3],
						[91134,3],
						[91135,3]
					],
					[ # +9
						[91132,3],
						[71129,3],
						[71123,3]
					]
				],
				[ ## Rubinhelm
					[91320],
					[ # +1
						[91130,5],
						[91131,5],
						[91134,5]
					],
					[ # +2
						[91130,6],
						[91131,6],
						[91134,6]
					],
					[ # +3
						[91131,7],
						[91132,7],
						[91135,7]
					],
					[ # +4
						[91131,8],
						[91132,8],
						[91135,8]
					],
					[ # +5
						[91132,9],
						[91133,9],
						[91136,9]
					],
					[ # +6
						[91132,10],
						[91133,10],
						[91136,10]
					],
					[ # +7
						[91148,1],
						[91133,10],
						[91137,10]
					],
					[ # +8
						[91149,1],
						[71129,20],
						[71123,20]
					],
					[ # +9
						[91150,1],
						[30165,10],
						[30167,10]
					]
				],
			]
		],

		[
			["Sonstiges",75],
			[
				[ ## Stein des Durchbruchs
					[28230],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein des Todesstoß
					[28231],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein der Wiederkehr
					[28232],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein gegen Krieger
					[28233],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein gegen Ninja
					[28234],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein gegen Sura
					[28235],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein gegen Schamanen
					[28236],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein der Monster
					[28237],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein des Ausweichens
					[28238],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein des Duckens
					[28239],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein der Magie
					[28240],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein der Lebenskraft
					[28241],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## Stein des Schutzes
					[28242],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,1]
					],
					[ # +6
						[91145,10]
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## AK Stein+2
					[91148],
					[ # +1
					],
					[ # +2
					],
					[ # +3
						[91145,2],
						[91144,1]
					],
					[ # +4
					],
					[ # +5
					],
					[ # +6
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## AK Stein+3
					[91149],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
						[91145,8],
						[91143,1]
					],
					[ # +5
					],
					[ # +6
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				],
				[ ## AK Stein+4
					[91150],
					[ # +1
					],
					[ # +2
					],
					[ # +3
					],
					[ # +4
					],
					[ # +5
						[91145,16],
						[91142,1]
					],
					[ # +6
					],
					[ # +7
					],
					[ # +8
					],
					[ # +9
					]
				]

			]
		]
	],
	[
		[
		["Krieger",67],
		[
			[ ## Schlachtschwert
				[140],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Tritonschwert
				[270],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +3
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +4
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +5
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +6
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +7
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +8
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +9
					[27992,5],
					[27993,5],
					[27994,5]
				]
			],
			[ ## Mythrilschwert Jetzt Bellumschwert
            [480],
            [ # +1
                [91130,1],
                [27992,3],
                [27993,3],
                [27993,3]
            ],
            [ # +2
                [91130,1],
                [27993,3],
                [27994,3]
            ],
            [ # +3
                [91130,2],
                [91131,1],
                [27994,4]
            ],
            [ # +4
                [91130,2],
                [91131,1],
                [27994,5]
            ],
            [ # +5
                [91130,2],
                [91131,1],
                [91134,1]
            ],
            [ # +6
                [91130,2],
                [91131,1],
                [91134,1]
            ],
            [ # +7
                [91130,2],
                [91131,2],
                [91135,1]
            ],
            [ # +8
                [91130,2],
                [91131,2],
                [91135,1]
            ],
            [ # +9
                [91131,1],
                [71123,1],
                [71129,1]
            ]
        ],
			[ ## Graustahlschwert
				[490],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],        
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91131,2],
					[91134,2],
					[91135,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Teufelsschwert
				[500],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],        
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],
			[ ## Tödliches Giftschwert
				[510],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],        
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Blaueisenschwert
				[520],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],        
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Drachenhautschwert
				[530],
				[ # +1
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +2
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +3
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +4
					[91131,5],
					[91132,5],
					[91135,5]
				],        
				[ # +5
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +6
					[91132,5],
					[91133,5],
					[91136,5]
				],
				[ # +7
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +8
					[91133,5],
					[91136,5],
					[91137,5]
				],
				[ # +9
					[91133,4],
					[30165,3],
					[30167,3]
				]
			],
			[ ## Saphir Runenschwert
				[540],
				[ # +1
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +2
					[91130,6],
					[91131,6],
					[91134,6]
				],
				[ # +3
					[91131,7],
					[91132,7],
					[91135,7]
				],
				[ # +4
					[91131,8],
					[91132,8],
					[91135,8]
				],        
				[ # +5
					[91132,9],
					[91133,9],
					[91136,9]
				],
				[ # +6
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +7
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +8
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +9
					[91150,1],
					[30165,10],
					[30167,10]
				]
			],
			[ ## Saphirschwert
				[550],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],        
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
			[ ## Partisane
				[3130],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Halbmenschklinge
				[3150],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +3
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +4
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +5
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +6
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +7
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +8
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +9
					[27992,5],
					[27993,5],
					[27994,5]
				]
			],
			[ ## Mythrilspalter
				[3220],
				[ # +1
					[91130,1],
					[27992,3],
					[27993,3]
				],
				[ # +2
					[91130,1],
					[27993,3],
					[27994,3]
				],
				[ # +3
					[91130,2],
					[91131,1],
					[27994,4]
				],
				[ # +4
					[91130,2],
					[91131,1],
					[27994,5]
				],
				[ # +5
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +6
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +7
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +8
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +9
					[91131,1],
					[71123,1],
					[71129,1]
				]
			],
			[ ## Graustahlspalter
				[3230],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91131,2],
					[91134,2],
					[91135,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Teufelsspalter
				[3240],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],
			[ ## Tödlicher Giftspalter
				[3250],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Blaueisenspalter
				[3260],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Drachenhautspalter
				[3270],
				[ # +1
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +2
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +3
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +4
					[91131,5],
					[91132,5],
					[91135,5]
				],
				[ # +5
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +6
					[91132,5],
					[91133,5],
					[91136,5]
				],
				[ # +7
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +8
					[91133,5],
					[91136,5],
					[91137,5]
				],
				[ # +9
					[91133,4],
					[30165,3],
					[30167,3]
				]
			],
			[ ## Blauer Königsspalter
				[3290],
				[ # +1
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +2
					[91130,6],
					[91131,6],
					[91134,6]
				],
				[ # +3
					[91131,7],
					[91132,7],
					[91135,7]
				],
				[ # +4
					[91131,8],
					[91132,8],
					[91135,8]
				],
				[ # +5
					[91132,9],
					[91133,9],
					[91136,9]
				],
				[ # +6
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +7
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +8
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +9
					[91150,1],
					[30165,10],
					[30167,10]
				]
			],
			[ ## Saphirspalter
				[3280],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
		]
	],
	[
		["Ninja",63],
		[
			[ ## Drachenmesser
				[1100],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
 [ ## Seelenloses Messer
            [4040],
            [ # +1
                [27992,1],
                [27993,1],
                [27994,1]
            ],
            [ # +2
                [27992,1],
                [27993,1],
                [27994,1]
            ],
            [ # +3
                [27992,2],
                [27993,2],
                [27994,2]
            ],
            [ # +4
                [27992,2],
                [27993,2],
                [27994,2]
            ],
            [ # +5
                [27992,2],
                [27993,2],
                [27994,2]
            ],
            [ # +6
                [27992,3],
                [27993,3],
                [27994,3]
            ],
            [ # +7
                [27992,3],
                [27993,3],
                [27994,3]
            ],
            [ # +8
                [27992,3],
                [27993,3],
                [27994,3]
            ],
            [ # +9
                [27992,5],
                [27993,5],
                [27994,5]
            ]
        ],
			[ ## Mythrildolche
				[1350],
				[ # +1
					[91130,1],
					[27992,3],
					[27993,3],
				],
				[ # +2
					[91130,1],
					[27993,3],
					[27994,3],
				],
				[ # +3
					[91130,2],
					[91131,1],
					[27994,4]
				],
				[ # +4
					[91130,2],
					[91131,1],
					[27994,5]
				],
				[ # +5
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +6
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +7
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +8
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +9
					[91131,1],
					[71123,1],
					[71129,1]
				]
			],
			[ ## Graustahldolche
				[1360],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91131,2],
					[91134,2],
					[91135,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Teufelsdolche
				[1370],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],
			[ ## Blaue Königsdolche
				[1380],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Blaumonddolche
				[1390],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Drachenhautdolche
				[1400],
				[ # +1
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +2
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +3
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +4
					[91131,5],
					[91132,5],
					[91135,5]
				],
				[ # +5
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +6
					[91132,5],
					[91133,5],
					[91136,5]
				],
				[ # +7
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +8
					[91133,5],
					[91136,5],
					[91137,5]
				],
				[ # +9
					[91133,4],
					[30165,3],
					[30167,3]
				]
			],
			[ ## Saphir Fünf Elemete Klinge
				[1410],
				[ # +1
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +2
					[91130,6],
					[91131,6],
					[91134,6]
				],
				[ # +3
					[91131,7],
					[91132,7],
					[91135,7]
				],
				[ # +4
					[91131,8],
					[91132,8],
					[91135,8]
				],
				[ # +5
					[91132,9],
					[91133,9],
					[91136,9]
				],
				[ # +6
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +7
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +8
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +9
					[91150,1],
					[30165,10],
					[30167,10]
				]
			],
			[ ## Saphirdolche
				[1420],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
									]
			],
			[ ## Großgelbdrachen Bogen
				[2140],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Großteufelbogen
				[2160],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +3
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +4
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +5
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +6
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +7
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +8
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +9
					[27992,5],
					[27993,5],
					[27994,5]
				]
			],
			[ ## Bogen des Himmels
				[2380],
				[ # +1
					[91130,1],
					[27992,3],
					[27993,3]
				],
				[ # +2
					[91130,1],
					[27993,3],
					[27994,3]
				],
				[ # +3
					[91130,2],
					[91131,1],
					[27994,4]
				],
				[ # +4
					[91130,2],
					[91131,1],
					[27994,5]
				],
				[ # +5
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +6
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +7
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +8
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +9
					[91131,1],
					[71123,1],
					[71129,1]
				]
			],
			[ ## Oberster Bogen
				[2390],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91131,2],
					[91134,2],
					[91135,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Flammenbogen
				[2400],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],
			[ ## Blaufeder Bogen
				[2410],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Drachenhautbogen
				[2420],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Breitlings Bogen
				[2430],
				[ # +1
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +2
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +3
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +4
					[91131,5],
					[91132,5],
					[91135,5]
				],
				[ # +5
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +6
					[91132,5],
					[91133,5],
					[91136,5]
				],
				[ # +7
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +8
					[91133,5],
					[91136,5],
					[91137,5]
				],
				[ # +9
					[91133,4],
					[30165,3],
					[30167,3]
				]
			],
			[ ## Saphir Phönixbogen
				[2440],
				[ # +1
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +2
					[91130,6],
					[91131,6],
					[91134,6]
				],
				[ # +3
					[91131,7],
					[91132,7],
					[91135,7]
				],
				[ # +4
					[91131,8],
					[91132,8],
					[91135,8]
				],
				[ # +5
					[91132,9],
					[91133,9],
					[91136,9]
				],
				[ # +6
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +7
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +8
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +9
					[91150,1],
					[30165,10],
					[30167,10]
				]
			],
			[ ## Saphirbogen
				[2450],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
		]
	],
	[
		["Sura",73],
		[
			[ ## Geisterzahnklinge
				[150],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Heiliges Schwert
				[280],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +3
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +4
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +5
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +6
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +7
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +8
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +9
					[27992,5],
					[27993,5],
					[27994,5]
				]
			],
			[ ## Spitzenklinge
				[800],
				[ # +1
					[91130,1],
					[27992,3],
					[27993,3],
					[27993,3]
				],
				[ # +2
					[91130,1],
					[27993,3],
					[27994,1],
					[27993,3]
				],
				[ # +3
					[91130,2],
					[91131,1],
					[27994,4]
				],
				[ # +4
					[91130,2],
					[91131,1],
					[27994,5]
				],
				[ # +5
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +6
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +7
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +8
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +9
					[91131,1],
					[71123,1],
					[71129,1]
				]
			],
			[ ## Spinnen Klinge
				[810],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],        
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91131,2],
					[91134,2],
					[91135,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Teufelsklinge
				[820],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],        
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],
			[ ## Tödliche Giftklinge
				[830],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],        
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Schwarzstahl Klinge
				[840],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],        
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Drachenhautklinge
				[850],
				[ # +1
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +2
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +3
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +4
					[91131,5],
					[91132,5],
					[91135,5]
				],        
				[ # +5
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +6
					[91132,5],
					[91133,5],
					[91136,5]
				],
				[ # +7
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +8
					[91133,5],
					[91136,5],
					[91137,5]
				],
				[ # +9
					[91133,4],
					[30165,3],
					[30167,3]
				]
			],
			[ ## Drachenzahnklinge
				[860],
				[ # +1
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +2
					[91130,6],
					[91131,6],
					[91134,6]
				],
				[ # +3
					[91131,7],
					[91132,7],
					[91135,7]
				],
				[ # +4
					[91131,8],
					[91132,8],
					[91135,8]
				],        
				[ # +5
					[91132,9],
					[91133,9],
					[91136,9]
				],
				[ # +6
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +7
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +8
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +9
					[91150,1],
					[30165,10],
					[30167,10]
				]
			],
			[ ## Saphirklinge
				[870],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],        
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
		]
	],
	[
		["Schamane",74],
		[
			[ ## Erlösungsfächer
				[7140],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Dämonenfächer
				[7190],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +3
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +4
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +5
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +6
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +7
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +8
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +9
					[27992,5],
					[27993,5],
					[27994,5]
				]
			],
			[ ## Mythrilfächer
				[7380],
				[ # +1
					[91130,1],
					[27992,3],
					[27993,3],
				],
				[ # +2
					[91130,1],
					[27993,3],
					[27994,3],
				],
				[ # +3
					[91130,2],
					[91131,1],
					[27994,4]
				],
				[ # +4
					[91130,2],
					[91131,1],
					[27994,5]
				],
				[ # +5
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +6
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +7
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +8
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +9
					[91131,1],
					[71123,1],
					[71129,1]
				]
			],
			[ ## Blaumondfächer
				[7390],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],        
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91131,2],
					[91134,2],
					[91135,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Teufelsfächer
				[7400],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],        
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],
			[ ## Graustahlfächer
				[7410],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],        
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Drachenhautfächer
				[7420],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],        
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Himmelsfächer
				[620],
				[ # +1
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +2
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +3
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +4
					[91131,5],
					[91132,5],
					[91135,5]
				],        
				[ # +5
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +6
					[91132,5],
					[91133,5],
					[91136,5]
				],
				[ # +7
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +8
					[91133,5],
					[91136,5],
					[91137,5]
				],
				[ # +9
					[91133,4],
					[30165,3],
					[30167,3]
				]
			],
			[ ## Saphir Drachenfächer
				[7440],
				[ # +1
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +2
					[91130,6],
					[91131,6],
					[91134,6]
				],
				[ # +3
					[91131,7],
					[91132,7],
					[91135,7]
				],
				[ # +4
					[91131,8],
					[91132,8],
					[91135,8]
				],        
				[ # +5
					[91132,9],
					[91133,9],
					[91136,9]
				],
				[ # +6
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +7
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +8
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +9
					[91150,1],
					[30165,10],
					[30167,10]
				]
			],
			[ ## Saphirfächer
				[7450],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],        
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
			[ ## Himmel u Erde glocke
				[5100],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Drachenmaul
				[5330],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +3
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +4
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +5
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +6
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +7
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +8
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +9
					[27992,5],
					[27993,5],
					[27994,5]
				]
			],
			[ ## Mythrilglocke
				[5370],
				[ # +1
					[91130,1],
					[27992,3],
					[27993,3],
				],
				[ # +2
					[91130,1],
					[27993,3],
					[27994,3],
				],
				[ # +3
					[91130,2],
					[91131,1],
					[27994,4]
				],
				[ # +4
					[91130,2],
					[91131,1],
					[27994,5]
				],
				[ # +5
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +6
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +7
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +8
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +9
					[91131,1],
					[71123,1],
					[71129,1]
				]
			],
			[ ## Graustahlglocke
				[5380],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],        
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91131,2],
					[91134,2],
					[91135,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Teufelsglocke
				[5390],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],        
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],
			[ ## Blaueisenglocke
				[5420],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],        
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Drachenhautglocke
				[5400],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],        
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Tödl Giftglocke
				[5410],
				[ # +1
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +2
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +3
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +4
					[91131,5],
					[91132,5],
					[91135,5]
				],        
				[ # +5
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +6
					[91132,5],
					[91133,5],
					[91136,5]
				],
				[ # +7
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +8
					[91133,5],
					[91136,5],
					[91137,5]
				],
				[ # +9
					[91133,4],
					[30165,3],
					[30167,3]
				]
			],
			[ ## Saphir Drachenfächer
				[5430],
				[ # +1
					[91130,5],
					[91131,5],
					[91134,5]
				],
				[ # +2
					[91130,6],
					[91131,6],
					[91134,6]
				],
				[ # +3
					[91131,7],
					[91132,7],
					[91135,7]
				],
				[ # +4
					[91131,8],
					[91132,8],
					[91135,8]
				],        
				[ # +5
					[91132,9],
					[91133,9],
					[91136,9]
				],
				[ # +6
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +7
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +8
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +9
					[91150,1],
					[30165,10],
					[30167,10]
				]
			],
			[ ## Saphirfächer
				[5440],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],        
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
		]
	],
	#########################################################################################
	[
		["Rüstungen",65],
		[
			[ ## Schwarzstahl-Panzer
				[11290],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Drachenrüstung
				[11080],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91135,2],
					[91134,2],
					[91131,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Göttliche Rüstung
				[11140],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Saphirrüstung
				[15660],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
			[ ## Schwarzwind-Anzug
				[11490],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Drachenanzug
				[11090],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91135,2],
					[91134,2],
					[91131,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Göttlicher Anzug
				[11150],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Saphiranzug
				[15670],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
			[ ## Magie-Plattenpanzer
				[11690],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Drachenpanzer
				[11110],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91135,2],
					[91134,2],
					[91131,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Göttlicher Panzer
				[11160],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Saphirpanzer
				[15680],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
			[ ## Schwarze Kleidung
				[11890],
				[ # +1
					[27987,1]
				],
				[ # +2
					[27987,1]
				],
				[ # +3
					[27987,1]
				],
				[ # +4
					[27987,1],
					[27992,1]
				],
				[ # +5
					[27987,1],
					[27992,1]
				],
				[ # +6
					[27987,1],
					[27993,1]
				],
				[ # +7
					[27987,1],
					[27993,1]
				],
				[ # +8
					[27987,1],
					[27994,1]
				],
				[ # +9
					[27987,1],
					[27994,1]
				]
			],
			[ ## Drachenkleidung
				[11120],
				[ # +1
					[91130,1],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +4
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +5
					[91130,3],
					[91131,2],
					[91135,2]
				],
				[ # +6
					[91130,3],
					[91131,3],
					[91135,2]
				],
				[ # +7
					[91135,2],
					[91134,2],
					[91131,2]
				],
				[ # +8
					[91131,3],
					[91134,2],
					[91135,2]
				],
				[ # +9
					[91132,2],
					[71123,2],
					[71129,2]
				]
			],
			[ ## Göttliche Kleidung
				[11170],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Saphirkleidung
				[15690],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
		]
	],
	#########################################################################################
	[
		["Schilde",74],
		[
			[ ## Falkenschild
				[13060],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

				],
				[ # +8
					[27987,1],

				],
				[ # +9
					[27987,1],

				]
			],
			[ ## Tigerschild
				[13080],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

				],
				[ # +8
					[27987,1],
				],
				[ # +9
					[27987,1],
				]
			],
			[ ## Löwenkantenschild
				[13100],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

				],
				[ # +8
					[27987,1],
				],
				[ # +9
					[27987,1],
				]
			],
			[ ## Drachenschuppenschild
				[13120],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

				],
				[ # +8
					[27987,1],
				],
				[ # +9
					[27987,1],
				]
			],
			[ ## Strahlendes Schild
				[91551],
				[ # +1
					[91130,1],
					[27992,3],
					[27993,3]
				],
				[ # +2
					[91130,1],
					[27993,3],
					[27994,3]
				],
				[ # +3
					[91130,2],
					[91131,1],
					[27994,4]
				],
				[ # +4
					[91130,2],
					[91131,1],
					[27994,5]
				],
				[ # +5
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +6
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +7
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +8
					[91130,2],
					[91131,2],
					[91135,1]
				],
				[ # +9
					[91131,1],
					[71123,1],
					[71129,1]
				]
			],
			[ ## Titanenschild
				[91560],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71123,3],
					[71129,3]
				]
			],		
			[ ## Drachengottschild
				[91570],
				[ # +1
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +2
					[91130,4],
					[91131,4],
					[91134,4]
				],
				[ # +3
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +4
					[91131,4],
					[91132,4],
					[91135,4]
				],
				[ # +5
					[91132,3],
					[91133,3],
					[91136,3]
				],
				[ # +6
					[91132,4],
					[91133,4],
					[91136,4]
				],
				[ # +7
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +8
					[91133,4],
					[91136,4],
					[91137,4]
				],
				[ # +9
					[91133,3],
					[30165,2],
					[30167,2]
				]
			],
			[ ## Saphirschild
				[91580],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71123,20],
					[71129,20]
				],
				[ # +6
					[91150,1],
					[30165,20],
					[30167,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			]
		]
	],	
	#########################################################################################
	[
		["Schuhe",74],
		[
		
			[ ## Phönix Schuhe
				[15200],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

					[27992,1],
				],
				[ # +8

					[27993,1],
				],
				[ # +9
					[27994,1],

				]
			],
		
			[ ## Kimiko Schuhe
				[91390],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +3
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +4
					[27992,5],
					[27993,5],
					[27994,5]
				],
				[ # +5
					[27992,5],
					[91130,1],
					[91134,1]
				],
				[ # +6
					[27993,5],
					[91130,2],
					[91134,2]
				],
				[ # +7
					[27994,5],
					[91130,3],
					[91134,3]
				],
				[ # +8
					[91130,5],
					[91131,1],
					[91135,1]
				],
				[ # +9
					[91134,5],
					[91131,2],
					[91135,2]
				]
			],
			[ ## Citrinschuhe
				[91400],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71129,3],
					[71123,3]
				]
			],
			[ ## Saphirschuhe
				[91600],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
		]
	],	
	#########################################################################################
	[
		["Armbänder",65],
		[
		
			[ ## HTA Arbmband
				[14200],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

					[27992,1],
				],
				[ # +8

					[27993,1],
				],
				[ # +9
					[27994,1],
				]
			],
		
			[ ## Kimiko Arbmband
				[91480],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +3
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +4
					[27992,5],
					[27993,5],
					[27994,5]
				],
				[ # +5
					[27992,5],
					[91130,1],
					[91134,1]
				],
				[ # +6
					[27993,5],
					[91130,2],
					[91134,2]
				],
				[ # +7
					[27994,5],
					[91130,3],
					[91134,3]
				],
				[ # +8
					[91130,5],
					[91131,1],
					[91135,1]
				],
				[ # +9
					[91134,5],
					[91131,2],
					[91135,2]
				]
			],
			[ ## Citrinarmband
				[91490],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71129,3],
					[71123,3]
				]
			],
			[ ## Saphirarmband
				[91620],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],
		]
	],
	#########################################################################################
	[
		["Halsketten",66],
		[
		
			[ ## HTK
				[16200],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

					[27992,1],
				],
				[ # +8

					[27993,1],
				],
				[ # +9
					[27994,1],
				]
			],
		
			[ ## Kimiko Kette
				[91450],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +3
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +4
					[27992,5],
					[27993,5],
					[27994,5]
				],
				[ # +5
					[27992,5],
					[91130,1],
					[91134,1]
				],
				[ # +6
					[27993,5],
					[91130,2],
					[91134,2]
				],
				[ # +7
					[27994,5],
					[91130,3],
					[91134,3]
				],
				[ # +8
					[91130,5],
					[91131,1],
					[91135,1]
				],
				[ # +9
					[91134,5],
					[91131,2],
					[91135,2]
				]
			],
			[ ## Citrinhalskette
				[91460],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71129,3],
					[71123,3]
				]
			],
			[ ## Saphirhalskette
				[91610],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],	
		]
	],	
	#########################################################################################
	[
		["Ohrringe",69],
		[
		
			[ ## HTO
				[17200],
				[ # +1

				],
				[ # +2

				],
				[ # +3

				],
				[ # +4

				],
				[ # +5

				],
				[ # +6

				],
				[ # +7

					[27992,1],
				],
				[ # +8

					[27993,1],
				],
				[ # +9
					[27994,1],
				]
			],
		
			[ ## Kimiko Ohrringe
				[91360],
				[ # +1
					[27992,1],
					[27993,1],
					[27994,1]
				],
				[ # +2
					[27992,2],
					[27993,2],
					[27994,2]
				],
				[ # +3
					[27992,3],
					[27993,3],
					[27994,3]
				],
				[ # +4
					[27992,5],
					[27993,5],
					[27994,5]
				],
				[ # +5
					[27992,5],
					[91130,1],
					[91134,1]
				],
				[ # +6
					[27993,5],
					[91130,2],
					[91134,2]
				],
				[ # +7
					[27994,5],
					[91130,3],
					[91134,3]
				],
				[ # +8
					[91130,5],
					[91131,1],
					[91135,1]
				],
				[ # +9
					[91134,5],
					[91131,2],
					[91135,2]
				]
			],
			[ ## Citrinohrringe
				[91370],
				[ # +1
					[91130,2],
					[91131,1],
					[91134,1]
				],
				[ # +2
					[91130,2],
					[91131,2],
					[91134,1]
				],
				[ # +3
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +4
					[91131,2],
					[91132,2],
					[91134,2]
				],
				[ # +5
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +6
					[91131,3],
					[91132,2],
					[91135,2]
				],
				[ # +7
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +8
					[91131,3],
					[91134,3],
					[91135,3]
				],
				[ # +9
					[91132,3],
					[71129,3],
					[71123,3]
				]
			],
			[ ## Saphirohrringe
				[91590],
				[ # +1
					[91130,10],
					[91131,10],
					[91134,10]
				],
				[ # +2
					[91131,10],
					[91132,10],
					[91135,10]
				],
				[ # +3
					[91132,10],
					[91133,10],
					[91136,10]
				],
				[ # +4
					[91148,1],
					[91133,10],
					[91137,10]
				],
				[ # +5
					[91149,1],
					[71129,20],
					[71123,20]
				],
				[ # +6
					[91150,1],
					[30167,20],
					[30165,20]
				],
				[ # +7
					[91151,1],
					[91138,5],
					[91139,1]
				],
				[ # +8
					[91138,10],
					[91139,2],
					[91140,1]
				],
				[ # +9
					[91139,8],
					[91140,4],
					[91141,1]
				]
			],		
		]
	],	
	#########################################################################################
	[
		["Helme",75],
		[
			[ ## Geistermaskenschaller
				[12240],
				[ # +1
					[27987,1],

				],
				[ # +2
					[27987,1],

				],
				[ # +3
					[27987,1],

				],
				[ # +4
					[27987,1],
					[27992,1],

				],
				[ # +5
					[27987,1],
					[27992,1],

				],
				[ # +6
					[27987,1],
					[27993,1],

				],
				[ # +7
					[27987,1],
					[27993,1],

				],
				[ # +8
					[27987,1],
					[27994,1],

				],
				[ # +9
					[27987,1],
					[27994,1],

				]
			],
			[ ## Krieger Saphirhelm
				[91510],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Stahlkapuze
				[12380],
				[ # +1
					[27987,1],

				],
				[ # +2
					[27987,1],

				],
				[ # +3
					[27987,1],

				],
				[ # +4
					[27987,1],
					[27992,1],

				],
				[ # +5
					[27987,1],
					[27992,1],

				],
				[ # +6
					[27987,1],
					[27993,1],

				],
				[ # +7
					[27987,1],
					[27993,1],

				],
				[ # +8
					[27987,1],
					[27994,1],

				],
				[ # +9
					[27987,1],
					[27994,1],

				]
			],
			[ ## Ninja Saphirkspuze
				[91520],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Burghelm
				[12520],
				[ # +1
					[27987,1],

				],
				[ # +2
					[27987,1],

				],
				[ # +3
					[27987,1],

				],
				[ # +4
					[27987,1],
					[27992,1],

				],
				[ # +5
					[27987,1],
					[27992,1],

				],
				[ # +6
					[27987,1],
					[27993,1],

				],
				[ # +7
					[27987,1],
					[27993,1],

				],
				[ # +8
					[27987,1],
					[27994,1],

				],
				[ # +9
					[27987,1],
					[27994,1],

				]
			],
			[ ## Sura Saphirburghelm
				[91530],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
			[ ## Sonnenlichthut
				[12660],
				[ # +1
					[27987,1],

				],
				[ # +2
					[27987,1],

				],
				[ # +3
					[27987,1],

				],
				[ # +4
					[27987,1],
					[27992,1],

				],
				[ # +5
					[27987,1],
					[27992,1],

				],
				[ # +6
					[27987,1],
					[27993,1],

				],
				[ # +7
					[27987,1],
					[27993,1],

				],
				[ # +8
					[27987,1],
					[27994,1],

				],
				[ # +9
					[27987,1],
					[27994,1],

				]
			],
			[ ## Schamanen Saphirhut
				[91540],
				[ # +1
					[91130,2],
					[91131,2],
					[91134,2]
				],
				[ # +2
					[91130,3],
					[91131,3],
					[91134,3]
				],
				[ # +3
					[91131,2],
					[91132,2],
					[91135,2]
				],
				[ # +4
					[91131,3],
					[91132,3],
					[91135,3]
				],
				[ # +5
					[91132,2],
					[91133,2],
					[91136,2]
				],
				[ # +6
					[91132,3],
					[91133,3],
					[91136,2]
				],
				[ # +7
					[91133,3],
					[91135,3],
					[91136,3]
				],
				[ # +8
					[91133,3],
					[91136,3],
					[91137,3]
				],
				[ # +9
					[91133,3],
					[30165,1],
					[30167,1]
				]
			],
		],
		],

		[
		["Sonstiges",75],
		[
			[ ## Stein des Durchbruchs
				[28230],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein des Todesstoß
				[28231],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein der Wiederkehr
				[28232],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein gegen Krieger
				[28233],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein gegen Ninja
				[28234],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein gegen Sura
				[28235],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein gegen Schamanen
				[28236],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein der Monster
				[28237],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein des Ausweichens
				[28238],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein des Duckens
				[28239],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein der Magie
				[28240],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein der Lebenskraft
				[28241],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## Stein des Schutzes
				[28242],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,1]
				],
				[ # +6
					[91145,10]
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## AK Stein+2
				[91148],
				[ # +1
				],
				[ # +2
				],
				[ # +3
					[91145,2],
					[91144,1]
				],
				[ # +4
				],
				[ # +5
				],
				[ # +6
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## AK Stein+3
				[91149],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
					[91145,8],
					[91143,1]
				],
				[ # +5
				],
				[ # +6
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			],
			[ ## AK Stein+4
				[91150],
				[ # +1
				],
				[ # +2
				],
				[ # +3
				],
				[ # +4
				],
				[ # +5
					[91145,16],
					[91142,1]
				],
				[ # +6
				],
				[ # +7
				],
				[ # +8
				],
				[ # +9
				]
			]

		]
	]
]
]

switchbot = 0
switchbot_minimize = 0
switchbot_Slots = [-1,-1,-1,-1,-1]
switchbot_switch_count = [0,0,0,0,0]
itemSwitchVnum = 71084
itemSwitchVnum2 = 76014
itemAttrType = [
	[1,0,0], #Schwert
	[1,4,0], # Glocken
	[1,1,0], # Dolche
	[1,5,0], # Fächer
	[1,2,0], # Bögen
	[1,3,0], # Zweihänder
	
	[2,0,1], # Rüstungen
	[2,1,5], # Helme
	[2,2,6], # Schilde
	[2,3,2], # Armbänder
	[2,4,3], # Schuhe
	[2,5,4], # Halsketten
	[2,6,7] # Ohrringe

]

itemAttrTypeName = [

	localeInfo.SWITCHBOT_UI_WEAPON,
	localeInfo.SWITCHBOT_UI_ARMOR,
	localeInfo.SWITCHBOT_UI_WRIST,
	localeInfo.SWITCHBOT_UI_SHOE,
	localeInfo.SWITCHBOT_UI_NECK,
	localeInfo.SWITCHBOT_UI_HEAD,
	localeInfo.SWITCHBOT_UI_SHIELD,
	localeInfo.SWITCHBOT_UI_EAR
	
]

# 0:weapon
# 1:body
# 2:wrist
# 3:foots
# 4:neck
# 5:head
# 6:shield
# 7:ear
Switchbot_BonusList = [
	
	[					# TP
		[1,localeInfo.SWITCHBOT_BONUS_TP],		# BonusIndex, BonusNameFürListe	<- BoniNummer und Name wie er in der Liste stehen soll.
		[1,2,3,4],			# bonusTypeList					<- Siehe Liste oben. Wenn die nummer hier steht kann der Boni in den ItemType.
		[2000,3000,3500],		# valueList						<- Alle Bonistufen eintragen.
	],
	[					
		[3,localeInfo.SWITCHBOT_BONUS_VIT],
		[0,6],			
		[8,10,12],		
	],
	[					
		[4,localeInfo.SWITCHBOT_BONUS_INT],
		[0,6],
		[8,10,12],
	],
	[					
		[5,localeInfo.SWITCHBOT_BONUS_STR],
		[0,6],
		[8,10,12],
	],
	[					
		[9,localeInfo.SWITCHBOT_BONUS_CASTSPEED],
		[0,1],
		[10,20],
	],
	[					
		[6,localeInfo.SWITCHBOT_BONUS_DEX],
		[0,6],
		[8,10,12],
	],
	[					
		[10,localeInfo.SWITCHBOT_BONUS_TP_REG],
		[4,5],
		[10,20],
	],
	[					
		[11,localeInfo.SWITCHBOT_BONUS_MP_REG],
		[4,5],
		[10,20],
	],
	[					
		[12,localeInfo.SWITCHBOT_BONUS_POISON],
		[0,5],
		[5,8],
	],
	[					
		[13,localeInfo.SWITCHBOT_BONUS_STUN],
		[0,3,4],
		[5,8],
	],
	[					
		[15,localeInfo.SWITCHBOT_BONUS_CRIT],
		[0,3,4],
		[5,10],
	],
	[					
		[16,localeInfo.SWITCHBOT_BONUS_PENE],
		[0,2,4],
		[5,10],
	],
	[					
		[17,localeInfo.SWITCHBOT_BONUS_HUMAN],
		[0,2,5,6,7],
		[8,10,12],
	],
	[					
		[23,localeInfo.SWITCHBOT_BONUS_STEAL_TP],
		[1,2],
		[5,10],
	],
	[					
		[24,localeInfo.SWITCHBOT_BONUS_STEAL_MP],
		[1,5],
		[5,10],
	],
	[					
		[27,localeInfo.SWITCHBOT_BONUS_BLOCK],
		[6],
		[10,12,15],
	],
	[					
		[28,localeInfo.SWITCHBOT_BONUS_ARROW_BLOCK],
		[3,5],
		[10,12,15],
	],
	[					
		[29,localeInfo.SWITCHBOT_BONUS_SWORD_DEF],
		[1,3,4,7],
		[10,15],
	],
	[					
		[30,localeInfo.SWITCHBOT_BONUS_2HAND_DEF],
		[1,3,4,7],
		[10,15],
	],
	[					
		[31,localeInfo.SWITCHBOT_BONUS_DAGGER_DEF],
		[1,3,4,7],
		[10,15],
	],
	[					
		[32,localeInfo.SWITCHBOT_BONUS_BELL_DEF],
		[1,3,4,7],
		[10,15],
	],
	[					
		[33,localeInfo.SWITCHBOT_BONUS_FAN_DEF],
		[1,3,4,7],
		[10,15],
	],
	[					
		[34,localeInfo.SWITCHBOT_BONUS_ARROW_DEF],
		[1,3,4,7],
		[10,15],
	],
	[					
		[37,localeInfo.SWITCHBOT_BONUS_MAGIC_DEF],
		[1,2,5],
		[10,15],
	],
	[					
		[41,localeInfo.SWITCHBOT_BONUS_POISON_DEF],
		[7],
		[5,10],
	],
	[					
		[44,localeInfo.SWITCHBOT_BONUS_DOUBLE_GOLD],
		[3,4,6],
		[20],
	],
	[					
		[45,localeInfo.SWITCHBOT_BONUS_DOUBLE_ITEM],
		[2,7],
		[20],
	],
	[					
		[48,localeInfo.SWITCHBOT_BONUS_IMMUNE_STUN],
		[6],
		[1],
	],
	[					
		[53,localeInfo.SWITCHBOT_BONUS_ATT],
		[1],
		[30,50],
	],
	[					
		[90,localeInfo.SWITCHBOT_BONUS_CRITICAL_DEF],
		[1,6],
		[5,10],
	],
	[					
		[91,localeInfo.SWITCHBOT_BONUS_PENETRATE_DEF],
		[2],
		[5,10],
	],
	
]


ItemMaker_BonusList67 = [
	
	[					# TP
		[1,localeInfo.SWITCHBOT_BONUS_TP],		# BonusIndex, BonusNameFürListe	<- BoniNummer und Name wie er in der Liste stehen soll.
		[0],			# bonusTypeList					<- Siehe Liste oben. Wenn die nummer hier steht kann der Boni in den ItemType.
		[2000,3000,3500],		# valueList						<- Alle Bonistufen eintragen.
	],
	[					
		[63,"Stark gegen Monster"],
		[0],			
		[5,5,5],		
	],
	[					
		[17,localeInfo.SWITCHBOT_BONUS_HUMAN],
		[0],
		[5,5,5],
	],
	[					
		[41,"Giftwiderstand"],
		[0],
		[5,5,5],
	],
	[					
		[22,"Stark gegen Teufel?"],
		[0],
		[5,5,5],
	],
	[					
		[18,"Stark gegen Tiere?"],
		[0],
		[5,5,5],
	],
	[					
		[20,"Stark gegen Mylgios? <- Wieso sind die alle durcheinander?"],
		[0],
		[5,5,5],
	],
	[					
		[15,"Chance auf krit. Treffer <- Kann in settinginfo.ItemMaker_BonusList67 bearbeitet werden."],
		[0],
		[5,5,5],
	],
	[					
		[19,"Stark gegen Orks? <- So legt man keine neuen Boni an!!!"],
		[0],
		[5,5,5],
	],
]










