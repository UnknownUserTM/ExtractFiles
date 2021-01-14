import app
import constInfo
import chat

REFINE_PROTO = {}

def LoadRefineProto():
	# try:
	srcRealFileName = "locale/%s/%s" % (app.GetLanguage(), "refine_proto.txt")
	lines = pack_open(srcRealFileName, "r").readlines()
	for line in lines:
		tab = line.split("\t")
		if tab[0] == "REFINE":
			tempList = []
			tempList.append(int(tab[1])) # id 0
			
			
			tempList.append(int(tab[2])) # vnum0 1
			tempList.append(int(tab[3])) # count0 2
			
			tempList.append(int(tab[4])) # vnum1 3 
			tempList.append(int(tab[5])) # count0 4
			
			tempList.append(int(tab[6])) # vnum2 5
			tempList.append(int(tab[7])) # count2 6
			
			tempList.append(int(tab[8])) # vnum3 7
			tempList.append(int(tab[9])) # count3 8

			tempList.append(int(tab[10])) # vnum4 9
			tempList.append(int(tab[11])) # count4 10

			tempList.append(int(tab[12])) # cost 11
			tempList.append(int(tab[13])) # prob 12	 		
			
			
			REFINE_PROTO[int(tab[1])] = tempList
	
	# chat.AppendChat(chat.CHAT_TYPE_DEBUG, "REFINE_PROTO: " +str(len(REFINE_PROTO)))

LoadRefineProto()

def GetRefineInfo(setId):
	if setId in REFINE_PROTO:
		return REFINE_PROTO[setId]
		
	return False
	
def GetRefineItemData(arr, slot):
	slotList = [1,3,5,7,9]
	itemVnum = slotList[slot]
	itemCount = slotList[slot] + 1
	return [arr[itemVnum], arr[itemCount]]

def GetRefineCost(arr):
	return arr[11]

def GetRefineProb(arr):
	return arr[12]
