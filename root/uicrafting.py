import ui
import chat
import app
import GFHhg54GHGhh45GHGH as net
import snd
import item
import fgGHGjjFHJghjfFG1545gGG as player
import uiToolTip  
import wndMgr 
import time
import grp
import mouseModule  
import constInfo
import event
import localeInfo
from uiGuild import MouseReflector
import systemSetting

	
class CraftingWindow(ui.ScriptWindow):

	MATERIAL_TYPE_ITEM					= 0
	MATERIAL_TYPE_GOLD					= 1
	MATERIAL_TYPE_ACHIEVEMENT_POINTS	= 2
	MATERIAL_TYPE_DUNGEONPOINTS			= 3
	
	# CRAFTING_DATA = [
		# {
			# "title" : "Kategorie 1",
			# "desc"	: "Hier findest du dies und das und auch nichts. Cool oder?",
			# "content" : [
				# {
					# "itemVnum" : 19,
					# "itemCount" : 1,
					
					# "materialList" : [
						# {
							# "type" : MATERIAL_TYPE_ITEM,
							# "vnum" : 10,
							# "count" : 1,
						# },
					# ]
				# }
			# ]	
		# },
	# ]

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/craftingwindow.py")
		except:
			import exception
			exception.Abort("DungeonIntroWindow.LoadWindow.LoadObject")


		self.Show()

	# def AppendCraftingRecipe(self,vnum,count,material
		
	def Destroy(self):
		self.Hide()
			
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if self.IsShow():
			self.Close()
		else:
			self.Show()
		
	def Close(self):
		self.Hide()

