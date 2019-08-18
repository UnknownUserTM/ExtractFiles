###########  released by d3m0n3  ###########

import app
import os
import chat
import ui
import locale
import uiScriptLocale
import uiCommon
import snd


class IgnoredItem(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName)

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.textLine.GetText()

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6*len(self.textLine.GetText()) + 4, height)

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(5, 0)

		textLine.SetText(fileName)
		textLine.Show()
		return textLine

class PopupDialog(ui.ScriptWindow):
	def __init__(self, parent):
		print "NEW POPUP WINDOW   ----------------------------------------------------------------------------"	
		ui.ScriptWindow.__init__(self)

		self.__Load()
		self.__Bind()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE POPUP WINDOW"

	def __Load(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")
		except:
			import exception
			exception.Abort("PopupDialog.__Load")

	def __Bind(self):
		try:
			self.textLine=self.GetChild("message")
			self.okButton=self.GetChild("accept")
		except:
			import exception
			exception.Abort("PopupDialog.__Bind")

		self.okButton.SAFE_SetEvent(self.__OnOK)

	def Open(self, msg):
		self.textLine.SetText(msg)
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def __OnOK(self):
		self.Hide()

class IgnoreListDialog(ui.ScriptWindow):
	def __init__(self):
		print "NEW LIST DIALOG   ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)

		self.isLoaded=0
		self.selectEvent=None
		self.fileListBox=None

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE LIST DIALOG"

	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__Load()

		ui.ScriptWindow.Show(self)

	def Open(self):
		self.Show()
		self.SetCenterPosition()
		self.SetTop()

	def Close(self):
		self.popupDialog.Hide()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def SAFE_SetSelectEvent(self, event):
		self.selectEvent=ui.__mem_func__(event)

	def __CreateFileListBox(self):
		fileListBox=ui.ListBoxEx()
		fileListBox.SetParent(self)
		fileListBox.SetPosition(15, 50)

		fileListBox.Show()
		return fileListBox

	def __Load(self):
		self.popupDialog=PopupDialog(self)
		
		self.__Load_LoadScript("UIScript/ignorelistwindow.py")
		self.__Load_BindObject()
		
		self.refreshButton.SAFE_SetEvent(self.__OnRefresh)
		self.IgnoreButton.SAFE_SetEvent(self.__OnIgnore)
		self.DeleteIgnoreButton.SAFE_SetEvent(self.__OnDeleteIgnore)
		self.board.SetCloseEvent(ui.__mem_func__(self.__OnCancel))
		self.UpdateRect()

		self.__RefreshFileList()

	def __Load_LoadScript(self, ignoreName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, ignoreName)
		except:
			import exception
			exception.Abort("fileListBox.__Load")

	def __Load_BindObject(self):
		try:
			self.fileListBox=self.__CreateFileListBox()
			self.fileListBox.SetScrollBar(self.GetChild("ScrollBar"))

			self.board=self.GetChild("board")
			self.DeleteIgnoreButton=self.GetChild("sblocca")
			self.IgnoreButton=self.GetChild("blocca")
			self.refreshButton=self.GetChild("aggiorna")
			self.popupText = self.popupDialog.GetChild("message")

		except:
			import exception
			exception.Abort("fileListBox.__Bind")

	def __PopupMessage(self, msg):
		self.popupDialog.Open(msg)

	def __OnDeleteIgnore(self):
		if self.fileListBox.IsEmpty():
			self.__PopupMessage("[Block System]: Die Liste ist leer!")
		else:
			selItem=self.fileListBox.GetSelectedItem()
			if selItem:
				selected = self.fileListBox.GetSelectedItem()
				text = selected.GetText()
				old = open("ignore.cfg", "r+")
				oldList = old.read()
				newList = str(oldList).replace(str(text + ",\n"), str(""))
				old.close()
				new = open("ignore.cfg", "w+")
				new.write(newList)
				new.close()
				self.__RefreshFileList()
				self.__PopupMessage("[Block System]: %s wurde entsperrt!" % text)
			else:
				self.__PopupMessage("[Block System]: Es wurde kein Name ausgewählt!")
			
	def __OnIgnore(self):
		ignoreNameBoard = uiCommon.InputDialog()
		ignoreNameBoard.SetTitle("Block System")
		ignoreNameBoard.SetAcceptEvent(ui.__mem_func__(self.OnAddIgnore))
		ignoreNameBoard.SetCancelEvent(ui.__mem_func__(self.OnCancelAddIgnore))
		ignoreNameBoard.Open()
		self.ignoreNameBoard = ignoreNameBoard

	def OnAddIgnore(self):
		text = self.ignoreNameBoard.GetText()
		if text:
			if os.path.exists("ignore.cfg"):
				ignoredTest = open("ignore.cfg", "r")
				ignoredList = ignoredTest.read()
				ignoredPlayer = ignoredList.split(",\n")
				ignoredTest.close()
				for i in xrange(str(ignoredList).count(",\n")):
					if str(ignoredPlayer[i]) != text:
						pass
					else:
						self.__PopupMessage("[Block System]: %s ist bereits gesperrt!" % text)
						self.ignoreNameBoard.Close()
						return
					
				ignored = open("ignore.cfg", "a")
				ignored.write("%s,\n" % text)
				ignored.close()
			else:
				ignored = open("ignore.cfg", "w+")
				ignored.write("%s,\n" % text)
				ignored.close()
	
		self.__PopupMessage("[Block System]: %s wurde blockiert!" % text)
		self.ignoreNameBoard.Close()
		self.__RefreshFileList()
		
	def OnCancelAddIgnore(self):
		self.ignoreNameBoard.Close()
		self.ignoreNameBoard = None
		return TRUE

	def __OnCancel(self):
		self.Hide()

	def __OnRefresh(self):
		self.__RefreshFileList()

	def __RefreshFileList(self):
		self.__ClearFileList()
		self.__AppendFileList()
		
	def __ClearFileList(self):
		self.fileListBox.RemoveAllItems()
		
	def __AppendFileList(self):
		Ignored = open("ignore.cfg", "r+")
		IgnoredList = Ignored.read()
		ignoredFilter = str(IgnoredList).replace("\n", "")
		ignoredPlayer = str(ignoredFilter).split(",")
		for i in xrange(int(str(IgnoredList).count(","))):
			self.fileListBox.AppendItem(IgnoredItem(ignoredPlayer[i]))
			
