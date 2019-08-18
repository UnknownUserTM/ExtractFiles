import app
import constInfo

# def mapping(**kwargs): return kwargs


def GetTestString():
	return ALIGNMENT_NAME

def SNA(text):	
	def f(x):
		return text
	return f

def SA(text):
	def f(x):
		return text % x
	return f
	
def LoadLanguageLocaleFile(srcFileName, localeDict):
	funcDict = {"SA":SA, "SNA":SNA}
	lineIndex = 1

	#srcRealFileName = "{0}{1}".format("locale/{0}/{1}/".format(app.MAIN_LOCALE_LANGUAGE, app.GetLanguage()), srcFileName)
	srcRealFileName = "locale/%s/%s" % (app.GetLanguage(), srcFileName)
	
	try:
		lines = pack_open(srcRealFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox(srcRealFileName)
		app.Abort()

	for line in lines:
		try:		
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				localeDict[tokens[0]] = tokens[1]		
			elif len(tokens) >= 3:
				type = tokens[2].strip()
				if type:
					localeDict[tokens[0]] = funcDict[type](tokens[1])
				else:
					localeDict[tokens[0]] = tokens[1]
			else:
				raise RuntimeError, "Unknown TokenSize"

			lineIndex += 1
		except:
			import dbg
			dbg.LogBox("%s: line(%d): %s" % (srcRealFileName, lineIndex, line), "Error")
			raise


LoadLanguageLocaleFile("locale_quest.txt", locals())


questStringTable = {
	
	0	: ERROR_NO_STRING_FOUND,
	
	# INTRO_QUEST
	1	: FIRST_QUEST_INTRO_TITLE,
	2	: FIRST_QUEST_INTRO_DESC,
	3	: FIRST_QUEST_INTRO_TALK,
	4	: FIRST_QUEST_KILL_TITLE,
	5	: FIRST_QUEST_KILL_DESC,
	6	: FIRST_QUEST_REWARD_LETTER,
	7	: FIRST_QUEST_REWARD_TITLE,
	8	: FIRST_QUEST_REWARD_TALK,
	
	
	# BIO
	9	: BIOLOGIST_TITLE,
	10	: BIOLOGIST_DESC_INTRO,
	11	: BIOLOGIST_TALK_INTRO,
	12	: BIOLOGIST_ACTIVE_LETTER,
	

	


}



def GetQuestString(index):
	if index in questStringTable:
		return questStringTable[index]
	else:
		return questStringTable[0]






