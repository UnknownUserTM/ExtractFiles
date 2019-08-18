import ui
import shop
import GFHhg54GHGhh45GHGH
import chat
import constInfo
import event
import chr

class GuiCreator(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		
	def __LoadScript(self):
		self.board = ui.BoardWithTitleBar()
		self.board.SetPosition(10,10)
		self.board.SetSize(185, 190)
		self.board.AddFlag("movable")
		self.board.SetTitleName("Gildenlager Bumser")
		self.board.Show()
		
		self.addItem = ui.Button()
		self.addItem.SetParent(self.board)
		self.addItem.SetUpVisual("d:/ymir work/ui/public/xsmall_button_01.sub")
		self.addItem.SetOverVisual("d:/ymir work/ui/public/xsmall_button_02.sub")
		self.addItem.SetDownVisual("d:/ymir work/ui/public/xsmall_button_03.sub")
		self.addItem.SetPosition(20,50)
		self.addItem.SetEvent(ui.__mem_func__(self.addItemToGuildstorage))
		self.addItem.SetText('addItem')
		self.addItem.Show()
		
		self.takeItem = ui.Button()
		self.takeItem.SetParent(self.board)
		self.takeItem.SetUpVisual("d:/ymir work/ui/public/xsmall_button_01.sub")
		self.takeItem.SetOverVisual("d:/ymir work/ui/public/xsmall_button_02.sub")
		self.takeItem.SetDownVisual("d:/ymir work/ui/public/xsmall_button_03.sub")
		self.takeItem.SetPosition(70,50)
		self.takeItem.SetEvent(ui.__mem_func__(self.takeItemFromGuildstorage))
		self.takeItem.SetText('takeItem')
		self.takeItem.Show()
		
		self.isLoaded = TRUE
		
	def addItemToGuildstorage(self):
		attachedSlotPos = 1
		selectedSlotPos = 117
		tab = 7
		constInfo.GUILDSTORAGE["questCMD"] = "MOVE_ITEM#INVENTORY#"+str(attachedSlotPos)+"#"+str(selectedSlotPos)+"#"+str(tab)
		event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Item eingelagert in Slot 840")
		
	def takeItemFromGuildstorage(self):
		attachedSlotPos = 117
		selectedSlotPos = 120
		tab = 7
		constInfo.GUILDSTORAGE["questCMD"] = "TAKE_ITEM#"+str(attachedSlotPos)+"#"+str(tab)
		event.QuestButtonClick(int(constInfo.GUILDSTORAGE["qid"]))
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Item rausgenommen aus Slot 840")
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Hide()
		
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.SetTop()
		self.Show()
		
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
wnd = GuiCreator()
wnd.Open()