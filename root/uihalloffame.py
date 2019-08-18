import ui
import chat
import event
import GFHhg54GHGhh45GHGH
import uiToolTip

HALL_OF_FAME_PATH = 'locale/de/ui/hall_of_fame/'

class HallOfFame(ui.ScriptWindow):

	def SetDefaultStatistic(self):
		self.statistic = {
			'categorys' : [
				{
					'name' : 'Bosse',
					'sub_category' : [
						{ #0
							'name' : 'Oberork',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #1
							'name' : 'Neunschwanz',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #2
							'name' : 'Gelber Tigergeist',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #3
							'name' : 'Flammenkönig',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #4
							'name' : 'Große Eishexe',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #5
							'name' : 'Roter Drache',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #6
							'name' : 'Brutales Eis-Ungeheuer',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #7
							'name' : 'Eisschlangenkönigin',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #8
							'name' : 'Besessener Eisskorpion',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #9
							'name' : 'Gewaltsamer Riesenkäfer',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #10
							'name' : 'Erbarmungslose Bienenkönigin',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #11
							'name' : 'Gnadenlose Monstergrabbe',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #12
							'name' : 'Verfluchte Eis-Kreatur',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #13
							'name' : 'Gnadenloser Halbmensch',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{ #14
							'name' : 'Besessener Dämonen-Totem',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
					],
				},
				{
					'name' : 'Metins',
					'sub_category' : [
						{
							'name' : 'Metin Tu-Young',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{
							'name' : 'Metin Jeon-Un',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{
							'name' : 'Yunari2 Eisbergstück',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{
							'name' : 'Yunari2 Schlangenei',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
						{
							'name' : 'Metin der Untoten',
							'achievement_value_name' : 'Kills',
							'players' : [],
						},
					],
				},
				{
					'name' : 'Dungeons',
					'sub_category' : [
						{
							'name' : 'Bruthöhle',
							'achievement_value_name' : 'Absolviert',
							'players' : [],
						},
						{
							'name' : 'Dämonenturm',
							'achievement_value_name' : 'Absolviert',
							'players' : [],
						},
						{
							'name' : 'Beran Setaou',
							'achievement_value_name' : 'Absolviert',
							'players' : [],
						},
						{
							'name' : 'Katakomben',
							'achievement_value_name' : 'Absolviert',
							'players' : [],
						},
						{
							'name' : 'Sturm auf die Runenfestung',
							'achievement_value_name' : 'Absolviert',
							'players' : [],
						},
						{
							'name' : 'Rotdrachenfestung',
							'achievement_value_name' : 'Absolviert',
							'players' : [],
						},
						{
							'name' : 'Nemeres Warte',
							'achievement_value_name' : 'Absolviert',
							'players' : [],
						},
					],
				},
				{
					'name' : 'Angeln',
					'sub_category' : [
						{
							'name' : 'Fische gefangen',
							'achievement_value_name' : 'Gefangen',
							'players' : [],
						},
						
					]
				}
			],
		}

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		if FALSE == self.isLoaded:
			self.__LoadScript()
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, 'uiscript/halloffame.py')
		except:
			import exception
			exception.Abort('hall_of_fame.__LoadScript.LoadScriptFile')

		try:
			self.__LoadVariables()
		except:
			import exception
			exception.Abort('hall_of_fame.__LoadScript.LoadVariables')

		try:
			self.__LoadUi()
		except:
			import exception
			exception.Abort('hall_of_fame.__LoadScript.LoadUi')

		try:
			self.__LoadEvents()
		except:
			import exception
			exception.Abort('hall_of_fame.__LoadScript.LoadEvents')
		
		self.isLoaded = TRUE

	def __LoadVariables(self):
		self.SetDefaultStatistic()
		self.SetDefaultPageVar()
		self.loadingBar = LoadingBar()
		self.quest_cmd = ''
		self.qid = 0
		self.last_update = 0
		self.toolTip = uiToolTip.ToolTip()

	def SetDefaultPageVar(self):
		self.page = {
				'current_category' : 0,
				'current_sub_category' : 0,
				'current_scrollbar_pos' : 0,
			}

	def __LoadUi(self):
		self.elements = {
			'title_bar' : {
				'bar' : self.GetChild('TitleBar'),
				# 'text' : self.GetChild('title_name'),
			},
			'menue': {
				'board' : {
					'nav_board' : self.GetChild('board_category_menue'),
				},
				'buttons' : {
					'menue_0' : self.GetChild('btn_category_menue_0'),
					'menue_1' : self.GetChild('btn_category_menue_1'),
					'menue_2' : self.GetChild('btn_category_menue_2'),
					'menue_3' : self.GetChild('btn_category_menue_3'),
				},
			},
			'sub_menue' : {
				'buttons' : {
					'left' : self.GetChild('btn_sub_category_left'),
					'right' : self.GetChild('btn_sub_category_right'),
				},
				'labels' : {
					'sub_category_name' : self.GetChild('lb_sub_category'),
					'sub_category_bg' : self.GetChild('thboard_subcategory_menue'),
				}
			},
			'statistic' : {
				'scrollbar'	: self.GetChild('scrollbar_statistic'),
				'achievement_value_name' : self.GetChild('lb_statistic_row_head_2'),
			}
		}

		self.elements['statistic']['row'] = []
		self.elements['statistic']['row_line'] = []
		self.elements['menue']['board']['nav_board'].HideBottom()
		self.elements['menue']['buttons']['menue_0'].Disable()
		
		for i in xrange(14):
			temp_statistic_row = {
				'column_0' : self.GetChild('lb_statistic_row_%d_column_0' %i),
				'column_1' : self.GetChild('lb_statistic_row_%d_column_1' %i),
				'column_2' : self.GetChild('lb_statistic_row_%d_column_2' %i),
				'column_3' : self.GetChild('lb_statistic_row_%d_column_3' %i),
				'column_4' : self.GetChild('lb_statistic_row_%d_column_4' %i),
			}


			self.elements['statistic']['row'].append(temp_statistic_row)
			self.elements['statistic']['row_line'].append(self.GetChild('row_%d' %i))


	def __LoadEvents(self):
		self.elements['title_bar']['bar'].SetCloseEvent(self.Close)

		self.elements['menue']['buttons']['menue_0'].SetEvent(self.ChangeCategory, 0)
		self.elements['menue']['buttons']['menue_1'].SetEvent(self.ChangeCategory, 1)
		self.elements['menue']['buttons']['menue_2'].SetEvent(self.ChangeCategory, 2)
		self.elements['menue']['buttons']['menue_3'].SetEvent(self.ChangeCategory, 3)

		self.elements['sub_menue']['buttons']['left'].SetEvent(self.ChangeSubCategory, 'left')
		self.elements['sub_menue']['buttons']['right'].SetEvent(self.ChangeSubCategory, 'right')

		self.elements['statistic']['scrollbar'].SetScrollEvent(self.ScrollStatistic)

	## STATISTIC COLUMNS START ##

	def ShowStatisticRow(self, row):
		self.elements['statistic']['row_line'][row].Show()

	def HideStatisticRow(self, row):
		self.elements['statistic']['row_line'][row].Hide()

	def SetStatistic(self, row, column, value):
		self.elements['statistic']['row'][row]['column_%d'%column].SetText(value)

	def SetStatisticAchievementValueName(self, name):
		self.elements['statistic']['achievement_value_name'].SetText(name)

	## STATISTIC COLUMNS END ##

	## SUB CATEGORY START ##

	def SetSubCategoryName(self, name):
		self.elements['sub_menue']['labels']['sub_category_name'].SetText(name)

	def GetSubCategoryNameByIds(self, category_id, sub_category_id):
		return self.statistic['categorys'][category_id]['sub_category'][sub_category_id]['name']

	## SUB CATEGORY END ##

	## SCROLLBAR START ##
	def ShowStatisticScrollbar(self):
		return self.elements['statistic']['scrollbar'].Show()

	def HideStatisticScrollbar(self):
		return self.elements['statistic']['scrollbar'].Hide()

	def GetStatisticScrollbarPos(self):
		return self.elements['statistic']['scrollbar'].GetPos()

	def SetStatisticScrollbarPos(self, pos):
		self.elements['statistic']['scrollbar'].SetPos(pos)

	def SetStatisticScrollbarMiddleBarSize(self, size):
		self.elements['statistic']['scrollbar'].SetMiddleBarSize(size)

	## SCROLLBAR END ##

	## MAIN FUNCTIONS START ##

	def ChangeCategory(self, category_id):
		try:
			self.page['current_category'] = category_id
			self.SetStatisticScrollbarPos(0)
			self.page['current_sub_category'] = 0
			self.RebuildStatistic()
			
			for i in xrange(len(self.elements['menue']['buttons'])):
				if i == category_id:
					self.elements['menue']['buttons']['menue_%d'%i].Disable()
				else:
					self.elements['menue']['buttons']['menue_%d'%i].Enable()
			
			
			
		except:
			print('ChangeCategory() failed')
	
	
	def BuildSubCategoryToolTip(self):
		
		self.toolTip.ClearToolTip()
		categoryList = self.statistic['categorys'][self.page['current_category']]['sub_category']
		for i in xrange(len(categoryList)):
			
			if i == self.page['current_sub_category']:
				self.toolTip.AppendHorizontalLine()
				self.toolTip.AppendSpace(3)
				self.toolTip.AppendTextLine(self.statistic['categorys'][self.page['current_category']]['sub_category'][i]['name'],self.toolTip.POSITIVE_COLOR)
				self.toolTip.AppendSpace(3)
				self.toolTip.AppendHorizontalLine()
			
			else:
				self.toolTip.AppendTextLine(self.statistic['categorys'][self.page['current_category']]['sub_category'][i]['name'],self.toolTip.NEGATIVE_COLOR)
		
		
		self.toolTip.ShowToolTip()
		
	def HideSubCategoryToolTip(self):
		self.toolTip.HideToolTip()
		
	def OnUpdate(self):
		if self.elements['sub_menue']['buttons']['left'].IsIn() or self.elements['sub_menue']['buttons']['right'].IsIn():
			self.BuildSubCategoryToolTip()
		else:
			self.HideSubCategoryToolTip()
	
	def ChangeSubCategory(self, dir):
		try:
			max_tab = len(self.statistic['categorys'][self.page['current_category']]['sub_category'])-1

			if dir == 'left':
				if self.page['current_sub_category']-1 < 0:
					self.page['current_sub_category'] = max_tab
				else:
					self.page['current_sub_category'] -= 1
			elif dir == 'right':
				if self.page['current_sub_category']+1 > max_tab:
					self.page['current_sub_category'] = 0
				else:
					self.page['current_sub_category'] += 1

			self.SetStatisticScrollbarPos(0)
			self.RebuildStatistic()
		except:
			print('ChangeSubCategory() failed')

	def ScrollStatistic(self):
		try:
			self.page['current_scrollbar_pos'] = self.GetStatisticScrollbarPos()
			self.RebuildStatistic()
		except:
			print('ScrollStatistic() failed')

	def RebuildStatistic(self):
		try:
			current_statistic = self.statistic['categorys'][self.page['current_category']]['sub_category'][self.page['current_sub_category']]
			current_statistic_len = len(current_statistic['players'])
		
			self.SetSubCategoryName(self.GetSubCategoryNameByIds(self.page['current_category'], self.page['current_sub_category']))
			self.SetStatisticAchievementValueName(current_statistic['achievement_value_name']+':')

			start_index = int(self.page['current_scrollbar_pos'] * (current_statistic_len-14))

			for i in xrange(14):
				self.HideStatisticRow(i)
			
			for i in xrange(min(current_statistic_len,14)):
				real_index = i + start_index 
				self.SetStatistic(i,0,'%d.'%(real_index+1))
				self.SetStatistic(i,1,current_statistic['players'][real_index]['name'])
				self.SetStatistic(i,2,current_statistic['players'][real_index]['achievement_value'])
				self.SetStatistic(i,3,current_statistic['players'][real_index]['level'])
				self.SetStatistic(i,4,current_statistic['players'][real_index]['empire'])
				self.ShowStatisticRow(i)

			if current_statistic_len <= 14:
				self.HideStatisticScrollbar()
			else:
				self.SetStatisticScrollbarMiddleBarSize(float(14)/float(current_statistic_len))
				self.ShowStatisticScrollbar()
		except:
			print('RebuildStatistic() failed')


	## MAIN FUNCTIONS END ##

	def Command(self, received_cmd):
		received_cmd = received_cmd.split('/')
		cmd = received_cmd[0]
		param = received_cmd[1:]
		
		if cmd == 'OPEN':
			self.Open(int(param[0]))

		elif cmd == 'SET_QID':
			self.qid = int(param[0])
			
		elif cmd == 'GET_QUESTCMD':
			GFHhg54GHGhh45GHGH.SendQuestInputStringPacket(self.quest_cmd)
			self.quest_cmd = 'NULL#'
		
		elif cmd == 'SET_LOADINGBAR_PERCENT':
			self.loadingBar.SetPercent(int(param[0]))

		elif cmd == 'ADD_STATISTIC_PLAYER':
			self.AddStatisticPlayer(int(param[0]), int(param[1]), param[2], param[3], param[4], param[5])

		elif cmd == 'CLEAR_STATISTIC':
			self.SetDefaultStatistic()

	## QUEST FUNCTIONS START ##

	def AddStatisticPlayer(self, category_id, sub_category_id, name, level, empire, achievement_value):
		temp_player = {
						'name' : name,
						'level' : level,
						'empire' : empire,
						'achievement_value': achievement_value,
					}

		self.statistic['categorys'][category_id]['sub_category'][sub_category_id]['players'].append(temp_player)

	## QUEST FUNCTIONS END ##

	def SendQuestCommand(self, cmd):
		self.quest_cmd = cmd
		##self.SendSystemChat('Sending command: %s to qid: %d ' % (cmd, self.qid))
		event.QuestButtonClick(self.qid)
			
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Hide()

	def OpenRequest(self):
		if self.IsShow():
			self.Close()
		else:
		
			self.loadingBar.Open()
			self.SetDefaultPageVar()
			self.SetStatisticScrollbarPos(0)
			self.SendQuestCommand('OPEN#%d' %self.last_update)

	def Open(self, last_update = 0):
		if last_update:
			self.last_update = last_update
		self.RebuildStatistic()
			
		self.SetTop()
		self.Show()
		
	def Close(self):
		self.Hide()

	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, '<hall_of_fame>: ' + str(text))

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE

class LoadingBar(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE

	def __LoadScript(self):
		try: 
			self.BindObjects()
		except:
			import exception
			exception.Abort('hall_of_fame.LoadingBar.__LoadScript.BindObjects')
			
		self.isLoaded = TRUE

	def BindObjects(self):
		global HALL_OF_FAME_PATH

		# self.board = ui.ThinBoard()
		# self.board.SetSize(260,30)
		# self.board.SetCenterPosition()
		# self.board.Show()
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "exscript/halloffameloading.py")
		except:
			import exception
			exception.Abort("LoadingWindow.LoadWindow.LoadObject")
		
		self.board = self.GetChild("loading_bg")
			
		self.progressBarActualFile = ui.AniImageBox()
		self.progressBarActualFile.SetParent(self.board)
		self.progressBarActualFile.AppendImage("yamato_halloffame/pcb_fill.tga")
		self.progressBarActualFile.SetPosition(16, 17)
		self.progressBarActualFile.SetDelay(90)
		self.progressBarActualFile.SetPercentage(0, 100)
		self.progressBarActualFile.Show()

		self.lb_load = ui.TextLine()
		self.lb_load.SetParent(self.board)
		self.lb_load.SetPosition(18,12)
		self.lb_load.SetText('Laden')
		self.lb_load.SetOutline()
		self.lb_load.Show()

		self.lb_percent = ui.TextLine()
		self.lb_percent.SetParent(self.board)
		self.lb_percent.SetPosition(235,12)
		self.lb_percent.SetText('0%')
		self.lb_percent.SetOutline()
		self.lb_percent.Show()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Hide()

	def SetPercent(self, percent):
		if percent >= 100:
			self.board.Hide()
		else:
			# self.board.SetTop()
			self.board.Show()
			self.progressBarActualFile.SetPercentage(percent, 100)
			self.lb_percent.SetText(str(percent) +'%')

	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE


wnd = HallOfFame()
#wnd.Open()
