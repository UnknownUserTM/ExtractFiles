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
	
	# TUTORIAL SECTION
	
	1	: TUTORIAL_INTRO_TITLE,
	2	: TUTORIAL_INTRO_LETTER,
	3	: TUTORIAL_INTRO_TALK_OLDMAN,
	4	: TUTORIAL_INTRO_TITLE2,
	5	: TUTORIAL_INTRO_LETTER2,
	6	: TUTORIAL_INTRO_TALK_TRAINER_TITLE,
	7	: TUTORIAL_INTRO_TALK_TRAINER,
	8	: TUTORIAL_INTRO_TALK_TRAINER_TITLE,
	
	9	: TUTORIAL_INTRO_TITLE3,
	10	: TUTORIAL_INTRO_LETTER3,
	11	: TUTORIAL_INTRO_TALK_CITYGUARD,
	
	12	: TUTORIAL_OBJECTIVE_LV5,
	13	: TUTORIAL_OBJECTIVE_TEACHER,
	14	: TUTORIAL_OBJECTIVE_LV10,
	15	: TUTORIAL_OBJECTIVE_LV20,
	16	: TUTORIAL_OBJECTIVE_LV30,
	17	: TUTORIAL_OBJECTIVE_LISTEN,


}



def GetQuestString(index):
	if index in questStringTable:
		return questStringTable[index]
	else:
		return questStringTable[0]






