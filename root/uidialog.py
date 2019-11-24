import ui
import snd
import shop
import mouseModule
import chr
import GFHhg54GHGhh45GHGH as net 
import uiCommon
import localeInfo
import chat
import item
import systemSetting #김준호
import fgGHGjjFHJghjfFG1545gGG as player
import app
import constInfo
import event

floatingDialogDict = {}

def MakeNewFloatingDialog(vid,textFile,qid):
	if floatingDialogDict.has_key(vid):
		floatingDialogDict[vid].SetQid(qid)
		floatingDialogDict[vid].LoadTextFile(textFile)
		floatingDialogDict[vid].Open(vid)
	else:
		dialog = FloatingDialogWindow()
		dialog.SetQid(qid)
		dialog.LoadTextFile(textFile)
		dialog.Open(vid)	
		floatingDialogDict[vid] = dialog

class FloatingDialogWindow(ui.ThinBoard):

	textTimerLength = {
		"NORMAL"	: 5,
		"LONG"		: 10,
		"VERY_LONG"	: 15,
	}

	def __init__(self):
		ui.ThinBoard.__init__(self, "UI_BOTTOM")
		self.vid = None
		self.textDict = []
		self.step = 0
		self.timer = 0
		self.qid = 0
		self.__MakeTextLine()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def __MakeTextLine(self):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetWindowHorizontalAlignCenter()
		self.textLine.SetWindowVerticalAlignCenter()
		self.textLine.SetHorizontalAlignCenter()
		self.textLine.SetVerticalAlignCenter()
		self.textLine.Show()
		
	def LoadTextFile(self,file):
		try:
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,app.GetLocalePath() + "/textfile/" + str(file) + ".txt")
			lines = pack_open(app.GetLocalePath() + "/textfile/" + str(file) + ".txt", "r").readlines()
		except IOError:
			chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Error: No File: " + str(file) + " found.")
			return
		
		i = 0
		for line in lines:
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				length_key = tokens[1]
				info = {
					"text" : tokens[0],
					"timer" : self.textTimerLength[length_key],
				
				}
				# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"Line: " + str(i) + ": " + str(tokens[0]) + ", " + str(tokens[1]))
				self.textDict.append(info)

			i = i + 1		
		
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"textDict: " + str(len(self.textDict)))
	
	def LoadNextStep(self):
		# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"textDict: " + str(len(self.textDict)))
		if self.step < len(self.textDict):
			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,"step: " + str(self.step))
			self.textLine.SetText(self.textDict[self.step]["text"] + " (" + str(self.step + 1) + "/" + str(len(self.textDict))+")")
			self.textLine.UpdateRect()
			# self.textLine.SetPackedFontColor(0xffd8a055)
			self.textLine.SetOutline()
			self.SetSize(len(self.textDict[self.step]["text"])*6 + 10*2, 20)		

			# chat.AppendChat(chat.CHAT_TYPE_DEBUG,str(self.textDict[self.step]["timer"]))
			self.timer = app.GetTime() + int(self.textDict[self.step]["timer"])
			self.step = self.step + 1
		else:
			self.vid = None
			self.timer = 0
			self.step = 0
			self.textDict = []
			self.Hide()
			if self.qid > 0:
				constInfo.INPUT_CMD = "floatingdialog_done/"
				event.QuestButtonClick(self.qid)	
				self.qid = 0
	
	def SetQid(self, qid):
		self.qid = qid
	
	def Open(self, vid):
		self.vid = vid
		self.LoadNextStep()
		self.Show() 
						
	def OnMouseLeftButtonUp(self):
		if not self.vid:
			return
		self.LoadNextStep()
		
		return True
		
	def OnUpdate(self):
		if not self.vid:
			return

		self.Show()
		x, y = chr.GetProjectPosition(self.vid, 220)
		self.SetPosition(x - self.GetWidth()/2, y - self.GetHeight()/2)
		
		if self.timer < app.GetTime():
			self.LoadNextStep()
