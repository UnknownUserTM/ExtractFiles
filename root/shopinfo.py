import app
import constInfo

# def mapping(**kwargs): return kwargs

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


LoadLanguageLocaleFile("locale_shop.txt", locals())


shopStringTable = {
	# Achievement Shop
	1 : RUESTUNGSNPC_SHOP,
	2 : RUESTUNGSNPC_SHOP2,
	3 : RUESTUNGSNPC_SHOP3,
	4 : WAFFENNPC_SHOP,
	5 : WAFFENNPC_SHOP2,
	6 : WAFFENNPC_SHOP3,
	7 : BIOLOGENNPC_SHOP,
	8 : BIOLOGENNPC_SHOP2,
	9 : BIOLOGENNPC_SHOP3,
	10 : BIOLOGENNPC_SHOP4,
	11 : GEMINPC_SHOP,
	12 : GEMINPC_SHOP2,

}



