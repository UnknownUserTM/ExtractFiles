import localeInfo
import fgGHGjjFHJghjfFG1545gGG
import chrmgr
import chr

EMOTION_VERSION = 2

if EMOTION_VERSION == 2:
	EMOTION_CLAP = 1
	EMOTION_CONGRATULATION = 2
	EMOTION_FORGIVE = 3
	EMOTION_ANGRY = 4
	EMOTION_ATTRACTIVE = 5
	EMOTION_SAD = 6
	EMOTION_SHY = 7
	EMOTION_CHEERUP = 8
	EMOTION_BANTER = 9
	EMOTION_JOY = 10
	EMOTION_CHEERS_1 = 11
	EMOTION_CHEERS_2 = 12
	EMOTION_DANCE_1 = 13
	EMOTION_DANCE_2 = 14
	EMOTION_DANCE_3 = 15
	EMOTION_DANCE_4 = 16
	EMOTION_DANCE_5 = 17
	EMOTION_DANCE_6 = 18
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DOZE = 61
	EMOTION_EXERCISE = 62
	EMOTION_PUSHUP = 63
	EMOTION_SELFIE = 64
	EMOTION_DANCE_7 = 65
	EMOTION_BUSY = 66
	
	EMOTION_EFFECT_HUNGRY = 67
	EMOTION_EFFECT_CALL = 68
	EMOTION_EFFECT_ALCOHOL = 69
	EMOTION_EFFECT_CELEBRATION = 70
	EMOTION_EFFECT_CHARGING = 71
	EMOTION_EFFECT_LETTER = 72
	EMOTION_EFFECT_NOSAY = 73
	EMOTION_EFFECT_SIREN = 74
	EMOTION_EFFECT_WEATHER_1 = 75
	EMOTION_EFFECT_WEATHER_2 = 76
	EMOTION_EFFECT_WEATHER_3 = 77
	EMOTION_EFFECT_WHIRL = 78
	
	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_DANCE_1 :		{"name": localeInfo.EMOTION_DANCE_1, 	"command":"/dance1"},
		EMOTION_DANCE_2 :		{"name": localeInfo.EMOTION_DANCE_2, 	"command":"/dance2"},
		EMOTION_DANCE_3 :		{"name": localeInfo.EMOTION_DANCE_3, 	"command":"/dance3"},
		EMOTION_DANCE_4 :		{"name": localeInfo.EMOTION_DANCE_4, 	"command":"/dance4"},
		EMOTION_DANCE_5 :		{"name": localeInfo.EMOTION_DANCE_5, 	"command":"/dance5"},
		EMOTION_DANCE_6 :		{"name": localeInfo.EMOTION_DANCE_6, 	"command":"/dance6"},
		EMOTION_CONGRATULATION :	{"name": localeInfo.EMOTION_CONGRATULATION,	"command":"/congratulation"},
		EMOTION_FORGIVE :		{"name": localeInfo.EMOTION_FORGIVE, 	"command":"/forgive"},
		EMOTION_ANGRY :			{"name": localeInfo.EMOTION_ANGRY, 		"command":"/angry"},
		EMOTION_ATTRACTIVE :		{"name": localeInfo.EMOTION_ATTRACTIVE, 	"command":"/attractive"},
		EMOTION_SAD :			{"name": localeInfo.EMOTION_SAD, 		"command":"/sad"},
		EMOTION_SHY :			{"name": localeInfo.EMOTION_SHY, 		"command":"/shy"},
		EMOTION_CHEERUP :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/cheerup"},
		EMOTION_BANTER :		{"name": localeInfo.EMOTION_BANTER, 	"command":"/banter"},
		EMOTION_JOY :			{"name": localeInfo.EMOTION_JOY, 		"command":"/joy"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
		

		# NEU
		EMOTION_DOZE :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/doze"},
		EMOTION_EXERCISE :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/exercise"},
		EMOTION_PUSHUP :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/pushup"},
		EMOTION_SELFIE :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/selfie"},
		EMOTION_DANCE_7 :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/dance7"},
		EMOTION_BUSY :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(busy)"},
		

		EMOTION_EFFECT_HUNGRY :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(hungry)"},
		EMOTION_EFFECT_CALL :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(call)"},
		EMOTION_EFFECT_ALCOHOL :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(alcohol)"},
		EMOTION_EFFECT_CELEBRATION :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(celebration)"},
		EMOTION_EFFECT_CHARGING :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(charging)"},
		EMOTION_EFFECT_LETTER :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(letter)"},
		
		EMOTION_EFFECT_NOSAY :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(nosay)"},
		EMOTION_EFFECT_SIREN :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(siren)"},
		EMOTION_EFFECT_WEATHER_1 :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(weather1)"},
		EMOTION_EFFECT_WEATHER_2 :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(weather2)"},
		EMOTION_EFFECT_WEATHER_3 :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(weather3)"},
		EMOTION_EFFECT_WHIRL :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"(whirl)"},

		
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"d:/ymir work/ui/game/windows/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"d:/ymir work/ui/game/windows/emotion_cheers_1.sub",
		EMOTION_CHEERS_2	:	"d:/ymir work/ui/game/windows/emotion_cheers_2.sub",

		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",

		EMOTION_CONGRATULATION	:	"icon/action/congratulation.tga",
		EMOTION_FORGIVE		:	"icon/action/forgive.tga",
		EMOTION_ANGRY		:	"icon/action/angry.tga",
		EMOTION_ATTRACTIVE	:	"icon/action/attractive.tga",
		EMOTION_SAD		:	"icon/action/sad.tga",
		EMOTION_SHY		:	"icon/action/shy.tga",
		EMOTION_CHEERUP		:	"icon/action/cheerup.tga",
		EMOTION_BANTER		:	"icon/action/banter.tga",
		EMOTION_JOY		:	"icon/action/joy.tga",
		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",
		EMOTION_DANCE_3		:	"icon/action/dance3.tga",
		EMOTION_DANCE_4		:	"icon/action/dance4.tga",
		EMOTION_DANCE_5		:	"icon/action/dance5.tga",
		EMOTION_DANCE_6		:	"icon/action/dance6.tga",

		EMOTION_KISS		:	"d:/ymir work/ui/game/windows/emotion_kiss.sub",
		EMOTION_FRENCH_KISS	:	"d:/ymir work/ui/game/windows/emotion_french_kiss.sub",
		EMOTION_SLAP		:	"d:/ymir work/ui/game/windows/emotion_slap.sub",
		
		# NEU
		EMOTION_DOZE		:	"icon/action/doze.tga",
		EMOTION_EXERCISE		:	"icon/action/exercise.tga",
		EMOTION_PUSHUP		:	"icon/action/pushup.tga",
		EMOTION_SELFIE		:	"icon/action/selfie.tga",
		EMOTION_BUSY		:	"icon/action/busy.tga",
		EMOTION_DANCE_7		:	"icon/action/dance7.tga",
		
		EMOTION_EFFECT_HUNGRY		:	"icon/action/hungry.tga",
		EMOTION_EFFECT_CALL		:	"icon/action/call.tga",
		EMOTION_EFFECT_ALCOHOL		:	"icon/action/alcohol.tga",
		EMOTION_EFFECT_CELEBRATION		:	"icon/action/celebration.tga",
		EMOTION_EFFECT_CHARGING		:	"icon/action/charging.tga",
		EMOTION_EFFECT_LETTER		:	"icon/action/letter.tga",
		
		EMOTION_EFFECT_NOSAY		:	"icon/action/nosay.tga",
		EMOTION_EFFECT_SIREN		:	"icon/action/siren.tga",
		EMOTION_EFFECT_WEATHER_1		:	"icon/action/weather1.tga",
		EMOTION_EFFECT_WEATHER_2		:	"icon/action/weather2.tga",
		EMOTION_EFFECT_WEATHER_3		:	"icon/action/weather3.tga",
		EMOTION_EFFECT_WHIRL		:	"icon/action/whirl.tga",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_DANCE_1 :			"dance_1.msa",
		chr.MOTION_DANCE_2 :			"dance_2.msa",
		chr.MOTION_DANCE_3 :			"dance_3.msa",
		chr.MOTION_DANCE_4 :			"dance_4.msa",
		chr.MOTION_DANCE_5 :			"dance_5.msa",
		chr.MOTION_DANCE_6 :			"dance_6.msa",
		chr.MOTION_CONGRATULATION :		"congratulation.msa",
		chr.MOTION_FORGIVE :			"forgive.msa",
		chr.MOTION_ANGRY :			"angry.msa",
		chr.MOTION_ATTRACTIVE :			"attractive.msa",
		chr.MOTION_SAD :			"sad.msa",
		chr.MOTION_SHY :			"shy.msa",
		chr.MOTION_CHEERUP :			"cheerup.msa",
		chr.MOTION_BANTER :			"banter.msa",
		chr.MOTION_JOY :			"joy.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
		
		chr.MOTION_NEW_DOZE :	"doze.msa",
		chr.MOTION_NEW_EXERCISE :	"exercise.msa",
		chr.MOTION_NEW_PUSHUP :	"pushup.msa",
		chr.MOTION_NEW_SELFIE :	"selfie.msa",
		# chr.MOTION_NEW_BUSY :	"doze.msa",
		chr.MOTION_NEW_DANCE_7 :	"dance_7.msa",
	}

elif EMOTION_VERSION == 1:
	EMOTION_CLAP = 1
	EMOTION_CHEERS_1 = 2
	EMOTION_CHEERS_2 = 3
	EMOTION_DANCE_1 = 4
	EMOTION_DANCE_2 = 5
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_DANCE_1 :		{"name": localeInfo.EMOTION_DANCE_1, 	"command":"/dance1"},
		EMOTION_DANCE_2 :		{"name": localeInfo.EMOTION_DANCE_2, 	"command":"/dance2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"d:/ymir work/ui/game/windows/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"d:/ymir work/ui/game/windows/emotion_cheers_1.sub",
		EMOTION_CHEERS_2	:	"d:/ymir work/ui/game/windows/emotion_cheers_2.sub",

		EMOTION_DANCE_1		:	"icon/action/dance1.tga",
		EMOTION_DANCE_2		:	"icon/action/dance2.tga",

		EMOTION_KISS		:	"d:/ymir work/ui/game/windows/emotion_kiss.sub",
		EMOTION_FRENCH_KISS	:	"d:/ymir work/ui/game/windows/emotion_french_kiss.sub",
		EMOTION_SLAP		:	"d:/ymir work/ui/game/windows/emotion_slap.sub",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_DANCE_1 :			"dance_1.msa",
		chr.MOTION_DANCE_2 :			"dance_2.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
	}
else:
	EMOTION_CLAP = 1
	EMOTION_CHEERS_1 = 2
	EMOTION_CHEERS_2 = 3
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"d:/ymir work/ui/game/windows/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"d:/ymir work/ui/game/windows/emotion_cheers_1.sub",
		EMOTION_CHEERS_2	:	"d:/ymir work/ui/game/windows/emotion_cheers_2.sub",

		EMOTION_KISS		:	"d:/ymir work/ui/game/windows/emotion_kiss.sub",
		EMOTION_FRENCH_KISS	:	"d:/ymir work/ui/game/windows/emotion_french_kiss.sub",
		EMOTION_SLAP		:	"d:/ymir work/ui/game/windows/emotion_slap.sub",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
	}


def __RegisterSharedEmotionAnis(mode, path):
	chrmgr.SetPathName(path)
	chrmgr.RegisterMotionMode(mode)

	for key, val in ANI_DICT.items():
		chrmgr.RegisterMotionData(mode, key, val)

def RegisterEmotionAnis(path):
	actionPath = path + "action/"
	weddingPath = path + "wedding/"

	__RegisterSharedEmotionAnis(chr.MOTION_MODE_GENERAL, actionPath)
	__RegisterSharedEmotionAnis(chr.MOTION_MODE_WEDDING_DRESS, actionPath)

	chrmgr.SetPathName(weddingPath)
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_WEDDING_DRESS)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_WAIT, "wait.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_WALK, "walk.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_RUN, "walk.msa")

def RegisterEmotionIcons():
	for key, val in ICON_DICT.items():
		fgGHGjjFHJghjfFG1545gGG.RegisterEmotionIcon(key, val)

