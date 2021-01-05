import app
import constInfo
import chat

ACHIEVEMENT_PROTO = []

VNUM = 0
DESC = 1
TYPE = 2
POINTS = 3
MAX_POINTS = 4

TYPE_BOSS = 0
TYPE_STONE = 1
TYPE_DUNGEON = 1 #-- 100000
TYPE_LEVEL = 2 #-- 110000
TYPE_REFINE = 3 #-- 120000
TYPE_ONE_TIME = 4 #-- 130000

CATEGORY_BOSS = 0
CATEGORY_STONE = 1
CATEGORY_DUNGEON = 2
CATEGORY_LEVEL = 3
CATEGORY_REFINE = 4
CATEGORY_ONE_TIME = 5

def LoadAchievementProto():
	# try:
	srcRealFileName = "locale/%s/%s" % (app.GetLanguage(), "achievement_proto.txt")
	lines = pack_open(srcRealFileName, "r").readlines()
	for line in lines:
		tab = line.split("\t")
		if tab[0] != "VNUM":
				
			tempList = []
			tempList.append(int(tab[0]))
			tempList.append(tab[1])
			tempList.append(int(tab[2]))
			tempList.append(int(tab[3]))
			tempList.append(int(tab[4]))
				
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, tab[0])
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, tab[1])
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, tab[2])
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, tab[3])
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, tab[4])
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, tab[5])
				
				
			index = int(tab[0])
			ACHIEVEMENT_PROTO.append(tempList)
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG, ACHIEVEMENT_PROTO[0])
		
	# except IOError:
		# import dbg
		# dbg.LogBox(srcRealFileName)
		# app.Abort()

LoadAchievementProto()


def GetAchievementInfo(index):
	for i in xrange(len(ACHIEVEMENT_PROTO)):
		if ACHIEVEMENT_PROTO[i][0] == index:
			return ACHIEVEMENT_PROTO[i]
	
	return False





