import ui
import playerSettingModule
import chr
import app
import grp
import fgGHGjjFHJghjfFG1545gGG as player
import background
import constInfo
import nonplayer
import chrmgr

class NonplayerModule(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		
		playerSettingModule.LoadGameData("INIT")			
		playerSettingModule.LoadGameData("NPC")
		playerSettingModule.LoadGameData("EFFECT")
		playerSettingModule.LoadGameData("ENEMY")			
		playerSettingModule.LoadGameData("SKILL")
		
		self.board = ui.Board()
		self.board.SetCenterPosition()
		self.board.SetSize(300,100)
		self.board.AddFlag("movable")
		self.board.Show()
		
		self.guerrero = ui.Button()
		self.guerrero.SetParent(self.board)
		self.guerrero.SetPosition(30,20)
		self.guerrero.SetUpVisual('d:/ymir work/ui/game/windows/tab_button_small_01.sub')
		self.guerrero.SetOverVisual('d:/ymir work/ui/game/windows/tab_button_small_02.sub')
		self.guerrero.SetDownVisual('d:/ymir work/ui/game/windows/tab_button_small_03.sub')
		self.guerrero.SetEvent(ui.__mem_func__(self.__Guerrero))
		self.guerrero.SetText("Guerrero")
		self.guerrero.Show()
		
		self.sura = ui.Button()
		self.sura.SetParent(self.board)
		self.sura.SetPosition(70,20)
		self.sura.SetUpVisual('d:/ymir work/ui/game/windows/tab_button_small_01.sub')
		self.sura.SetOverVisual('d:/ymir work/ui/game/windows/tab_button_small_02.sub')
		self.sura.SetDownVisual('d:/ymir work/ui/game/windows/tab_button_small_03.sub')
		self.sura.SetEvent(ui.__mem_func__(self.__Sura))
		self.sura.SetText("Sura")
		self.sura.Show()
		
		self.ninja = ui.Button()
		self.ninja.SetParent(self.board)
		self.ninja.SetPosition(110,20)
		self.ninja.SetUpVisual('d:/ymir work/ui/game/windows/tab_button_small_01.sub')
		self.ninja.SetOverVisual('d:/ymir work/ui/game/windows/tab_button_small_02.sub')
		self.ninja.SetDownVisual('d:/ymir work/ui/game/windows/tab_button_small_03.sub')
		self.ninja.SetEvent(ui.__mem_func__(self.__Ninja))
		self.ninja.SetText("ninja")
		self.ninja.Show()
		
		self.chamana = ui.Button()
		self.chamana.SetParent(self.board)
		self.chamana.SetPosition(150,20)
		self.chamana.SetUpVisual('d:/ymir work/ui/game/windows/tab_button_small_01.sub')
		self.chamana.SetOverVisual('d:/ymir work/ui/game/windows/tab_button_small_02.sub')
		self.chamana.SetDownVisual('d:/ymir work/ui/game/windows/tab_button_small_03.sub')
		self.chamana.SetEvent(ui.__mem_func__(self.__Chamana))
		self.chamana.SetText("Chamana")
		self.chamana.Show()
		
		self.emocion = ui.Button()
		self.emocion.SetParent(self.board)
		self.emocion.SetPosition(30,60)
		self.emocion.SetUpVisual('d:/ymir work/ui/game/windows/tab_button_small_01.sub')
		self.emocion.SetOverVisual('d:/ymir work/ui/game/windows/tab_button_small_02.sub')
		self.emocion.SetDownVisual('d:/ymir work/ui/game/windows/tab_button_small_03.sub')
		self.emocion.SetEvent(ui.__mem_func__(self.__Emocion))
		self.emocion.SetText("Emocion")
		self.emocion.Show()
		
		self.normal = ui.Button()
		self.normal.SetParent(self.board)
		self.normal.SetPosition(70,60)
		self.normal.SetUpVisual('d:/ymir work/ui/game/windows/tab_button_small_01.sub')
		self.normal.SetOverVisual('d:/ymir work/ui/game/windows/tab_button_small_02.sub')
		self.normal.SetDownVisual('d:/ymir work/ui/game/windows/tab_button_small_03.sub')
		self.normal.SetEvent(ui.__mem_func__(self.__Normal))
		self.normal.SetText("Normal")
		self.normal.Show()
		
	def __Emocion(self):
		chr.PushOnceMotion(chr.MOTION_DEAD, 0.1)
		
	def __Normal(self):
		chr.SetLoopMotion(chr.MOTION_MODE_GENERAL)
		
	def __Guerrero(self):
		
		x = 41800 #Position x ( in the map )
		y = 69400 #Position y ( in the map )		
		for i in xrange(15):

			self.__MakeCharacter(0,x, y)
			chr.SetArmor(20009)
			chr.SetHair(1009)
			chr.SetWeapon(279)	
			#chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
			chr.SetLoopMotion(chr.MOTION_MODE_GENERAL)
			#chr.Refresh()
			x = x + 15

	def __Sura(self):
		x = 41800
		y = 69600
		self.__MakeCharacter(2,x, y)
		chr.SetArmor(11299)
		chr.SetWeapon(149)	
		#chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_MODE_GENERAL)
		#chr.Refresh()

	def __Ninja(self):
		x = 41800
		y = 69800
		self.__MakeCharacter(1,x, y)
		chr.SetArmor(11299)
		chr.SetWeapon(2169)
		#chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_MODE_GENERAL)
		#chr.Refresh()
	
	def __Chamana(self):
		x = 41800
		y = 70000 
		self.__MakeCharacter(3,x, y)	
		chr.SetArmor(11299)
		chr.SetWeapon(7199)
		#chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		chr.SetLoopMotion(chr.MOTION_MODE_GENERAL)
		#chr.Refresh()

	def __MakeCharacter(self, race, x, y):
		nonplayer.GetEventType(1) 
		nonplayer.GetGradeByVID(1)
		nonplayer.GetLevelByVID(100)
		nonplayer.GetMonsterName("SeMa Test")
		
		nonplayer.LoadNonPlayerData()
		
		chr.CreateInstance(race)
		chr.SetInstanceType(chr.INSTANCE_TYPE_NPC)
		chr.SelectInstance(race)
		chr.SetVirtualID(race)
		chr.SetRace(1)
		chr.SetNameString("Test SeMa")

		chr.Refresh()
		#chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
		#chr.SetLoopMotion(chr.MOTION_MODE_GENERAL)

		chr.SetPixelPosition(x, y)
		chr.SetDirection(chr.DIR_SOUTHEAST)
		chr.SetMoveSpeed(300)
		chr.Render()
		grp.RestoreViewport()
		grp.PopState()
		grp.SetInterfaceRenderState()
		chr.Show()

	def OnUpdate(self):
		None


x = NonplayerModule()