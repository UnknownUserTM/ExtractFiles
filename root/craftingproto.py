import app
import constInfo
import chat

CRAFTING_PROTO = []

def LoadCraftingProto():
	# try:
	srcRealFileName	= "locale/%s/%s" % (app.GetLanguage(), "crafting_proto.txt")
	lines			= pack_open(srcRealFileName, "r").readlines()
	i				= 0
	thisSection		= 0
	isSection		= False
	
	for line in lines:
		tab = line.split("\t")
		chat.AppendChat(chat.CHAT_TYPE_DEBUG, tab[0])
		if tab[0] == "NEW_SECTION":
			# if isSection == True:
				# import dbg
				# dbg.LogBox("Error in Crafting-Proto Line: " + str(i) + " " + tab[0])
				# app.Abort()				
				
			section = {
				"INDEX" : tab[1],
				"TITLE" : tab[2],
				"CONTENT" : [],
			}
			isSection = True
			thisSection = len(CRAFTING_PROTO)
			CRAFTING_PROTO.append(section)
				
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "thisSection " + str(thisSection))
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "NEW_SECTION " + tab[1])
		
		elif tab[0] == "END_SECTION":
			isSection = False
			thisSection	= 0
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "END_SECTION tab")
			
			
		elif tab[0] == "TITLE":
			titleItem = {
				"type" : "title",
				"text" : tab[1],
			}
			
			CRAFTING_PROTO[thisSection]["CONTENT"].append(titleItem)
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "AppendTitleItem")
			
		elif tab[0] == "EMPTY":
			emptyItem = {
				"type" : "empty",
			}
			
			CRAFTING_PROTO[thisSection]["CONTENT"].append(emptyItem)
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "AppendEmptyItem")
			
		elif tab[0] == "ITEM":
			item = {
				"type" : "item",
				"itemVnum" : int(tab[1]),
				"itemCount" : int(tab[2]),
				
				"baseChance" : int(tab[3]),
				
				"gold"		: int(tab[4]),
				
				"materialList" : [],
			}
			
			materialString = tab[5].split("#")
			for a in xrange(len(materialString)):
				matieralSplit = materialString[a].split("/")
				materialItem = {
					"item"		: int(matieralSplit[0]),
					"itemCount" : int(matieralSplit[1]),
				}
				
				item["materialList"].append(materialItem)			
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "AppendItem")
			chat.AppendChat(chat.CHAT_TYPE_DEBUG, "MATERIAL_COUNT: " + str(len(item["materialList"])))
			CRAFTING_PROTO[thisSection]["CONTENT"].append(item)
			
			
		i = i + 1
	
	# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "CRAFTING_PROTO: " + str(len(CRAFTING_PROTO)))

LoadCraftingProto()

def GetCraftingProto(name):
	for i in xrange(len(CRAFTING_PROTO)):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "GetCraftingProto: " + CRAFTING_PROTO[i]["INDEX"] + " =? " + name)
		if CRAFTING_PROTO[i]["INDEX"] == name:
			return CRAFTING_PROTO[i]
			
	return False
