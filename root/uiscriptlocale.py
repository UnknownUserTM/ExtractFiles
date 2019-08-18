import app

AUTOBAN_QUIZ_ANSWER = "ANSWER"
AUTOBAN_QUIZ_REFRESH = "REFRESH"
AUTOBAN_QUIZ_REST_TIME = "REST_TIME"
OPTION_SHADOW = "SHADOW"
CODEPAGE = str(app.GetDefaultCodePage())
name = app.GetLocalePath()

def LoadLanguageLocaleFile(srcFileName, localeDict):
	localeDict["CUBE_INFO_TITLE"] = "Recipe"
	localeDict["CUBE_REQUIRE_MATERIAL"] = "Requirements"
	localeDict["CUBE_REQUIRE_MATERIAL_OR"] = "or"
	
	#srcRealFileName = "{0}{1}".format("locale/{0}/{1}/".format(app.MAIN_LOCALE_LANGUAGE, app.GetLanguage()), srcFileName)
	srcRealFileName = "%s/%s" % (name, srcFileName)
	try:
		lines = pack_open(srcRealFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadUIScriptLocaleError(%(srcRealFileName)s)" % locals())
		app.Abort()

	for line in lines:
		tokens = line[:-1].split("\t")
		if len(tokens) >= 2:
			localeDict[tokens[0]] = tokens[1]			
		else:
			print len(tokens), lines.index(line), line
			
LOCALE_UISCRIPT_PATH = "%s/ui/" % (name)
LOGIN_PATH = "%s/ui/login/" % (name)
EMPIRE_PATH = "%s/ui/empire/" % (name)
GUILD_PATH = "%s/ui/guild/" % (name)
SELECT_PATH = "%s/ui/select/" % (name)
WINDOWS_PATH = "%s/ui/windows/" % (name)
MAPNAME_PATH = "%s/ui/mapname/" % (name)
JOBDESC_WARRIOR_PATH = "%s/jobdesc_warrior.txt" % (name)
JOBDESC_ASSASSIN_PATH = "%s/jobdesc_assassin.txt" % (name)
JOBDESC_SURA_PATH = "%s/jobdesc_sura.txt" % (name)
JOBDESC_SHAMAN_PATH = "%s/jobdesc_shaman.txt" % (name)
EMPIREDESC_A = "%s/empiredesc_a.txt" % (name)
EMPIREDESC_B = "%s/empiredesc_b.txt" % (name)
EMPIREDESC_C = "%s/empiredesc_c.txt" % (name)

LoadLanguageLocaleFile("locale_interface.txt", locals())