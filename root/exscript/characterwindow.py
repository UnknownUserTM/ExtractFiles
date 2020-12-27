import uiScriptLocale

QUEST_ICON_BACKGROUND = 'd:/ymir work/ui/game/quest/slot_base.sub'

SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_00.sub"
MIDDLE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
ICON_SLOT_FILE = "d:/ymir work/ui/public/Slot_Base.sub"
FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"
ROOT_PATH = "d:/ymir work/ui/game/windows/"

LOCALE_PATH = uiScriptLocale.WINDOWS_PATH


WINDOW_WIDTH = 253+30
WINDOW_HEIGHT = 361+50+30

ADD_YAMATO_SPACE = 200

ADD_OLD_WINDOW_WITH = 15
ADD_OLD_WINDOW_HEIGTH = 6

EXP_WINDOW_WIDTH = 85

window = {
	"name" : "CharacterWindow",
	"style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - 361) / 2,

	"width" : WINDOW_WIDTH + ADD_YAMATO_SPACE + 50,
	"height" : WINDOW_HEIGHT+ 30,

	"children" :
	(				
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : WINDOW_WIDTH+15 +30+ ADD_YAMATO_SPACE,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach", "movable",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30 + ADD_YAMATO_SPACE,
			"height" : 361+30+ 30,

			"children" :
			(
			
				{
					"name" : "navigation_board",
					"type" : "board",
					# "style" : ("attach",),
					
					"x" : 15,
					"y" : 15,
					
					"width" : 220,
					"height" : WINDOW_HEIGHT - 45+ 30,
					
					"no_bottom" : 1,
					
					"children" : (
						{
							"name" : "klapptsJetztWindow",
							"type" : "window",
							
							"x" : 0,
							"y" : 0,
							
							"width" : 220,
							"height" : WINDOW_HEIGHT - 45+ 30,							
							
							"children" : (
							
								{
									"name" : "nav_button_0",
									"type" : "button",
									
									"x" : 30,
									"y" : 15,
								
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Charakter",
								},
								{
									"name" : "nav_button_1",
									"type" : "button",
									
									"x" : 30,
									"y" : 15 + 30,
								
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Fertigkeiten",
								},
								{
									"name" : "nav_button_2",
									"type" : "button",
									
									"x" : 30,
									"y" : 15 + 30 + 30,
								
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Emotionen",
								},					
								{
									"name" : "nav_button_3",
									"type" : "button",
									
									"x" : 30,
									"y" : 15 + 30 + 30 + 30,
								
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Achievements",
								},
								{
									"name" : "nav_button_4",
									"type" : "button",
									
									"x" : 30,
									"y" : 15 + 30 + 30 + 30 + 30,
								
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Bonusliste",
								},							
							
							),
						},
					
							
					),
				},
			

				# {
					# "name" : "TabControl",
					# "type" : "window",

					# "x" : 15,
					# "y" : 328,

					# "width" : 250,
					# "height" : 50,

					# "children" :
					# (
						# {
							# "name" : "Tab_Button_01",
							# "type" : "button",

							# "x" : 0+32,
							# "y" : 5,
							
							# "text" : "Status",
							
							# "default_image" : "yamato_button/button_small_n.tga", 
							# "over_image" : "yamato_button/button_small_h.tga", 
							# "down_image" : "yamato_button/button_small_p.tga", 
						# },
						# {
							# "name" : "Tab_Button_02",
							# "type" : "button",

							# "x" : 0+63+32,
							# "y" : 5,
							
							# "text" : uiScriptLocale.CHARACTER_SKILL,
							
							# "default_image" : "yamato_button/button_small_n.tga", 
							# "over_image" : "yamato_button/button_small_h.tga", 
							# "down_image" : "yamato_button/button_small_p.tga", 
						# },
						# {
							# "name" : "Tab_Button_03",
							# "type" : "button",

							# "x" : 0+63+63+32,
							# "y" : 5,
							
							# "text" : uiScriptLocale.CHARACTER_ACTION,
							
							# "default_image" : "yamato_button/button_small_n.tga", 
							# "over_image" : "yamato_button/button_small_h.tga", 
							# "down_image" : "yamato_button/button_small_p.tga", 
						# },
						# {
							# "name" : "Tab_Button_04",
							# "type" : "button",

							# "x" : 0+32+32,
							# "y" : 5+18,
							
							# "text" : "Quest",
							
							# "default_image" : "yamato_button/button_small_n.tga", 
							# "over_image" : "yamato_button/button_small_h.tga", 
							# "down_image" : "yamato_button/button_small_p.tga", 
						# },
					# ),
				# },
				## Page Area
				## Page Area
				# {
					# "name" : "Character_Page",
					# "type" : "window",
					# "style" : ("attach",),

					# "x" : 15 + ADD_YAMATO_SPACE + 15,
					# "y" : 15,

					# "width" : 250,
					# "height" : 304,

					# "children" :
					# (

						# ## Title Area
						# # {
							# # "name" : "Character_TitleBar", "type" : "titlebar", "style" : ("attach",), "x" : 61, "y" : 7, "width" : 185, "color" : "red",
							# # "children" :
							# # (
								# # #{ "name" : "TitleName", "type" : "image", "style" : ("attach",), "x" : 70, "y" : 1, "image" : LOCALE_PATH+"title_status.sub", },
								# # { "name" : "TitleName", "type":"text", "x":0, "y":-1, "text":uiScriptLocale.CHARACTER_MAIN, "all_align":"center" },
							# # ),
						# # },

						# ## Guild Name Slot
						# {
							# "name" : "Guild_Name_Slot",
							# "type" : "image",
							# "x" : 60,
							# "y" :27+7,
							# "image" : LARGE_VALUE_FILE,

							# "children" :
							# (
								# {
									# "name" : "Guild_Name",
									# "type":"text",
									# "text":"길드 이름",
									# "x":0,
									# "y":0,
									# "r":1.0,
									# "g":1.0,
									# "b":1.0,
									# "a":1.0,
									# "all_align" : "center",
								# },
							# ),
						# },

						# ## Character Name Slot
						# {
							# "name" : "Character_Name_Slot",
							# "type" : "image",
							# "x" : 153,
							# "y" :27+7,
							# "image" : LARGE_VALUE_FILE,

							# "children" :
							# (
								# {
									# "name" : "Character_Name",
									# "type":"text",
									# "text":"캐릭터 이름",
									# "x":0,
									# "y":0,
									# "r":1.0,
									# "g":1.0,
									# "b":1.0,
									# "a":1.0,
									# "all_align" : "center",
								# },
							# ),
						# },

						# ## Header
						# { 
							# "name":"Status_Header", "type":"window", "x":3, "y":31, "width":0, "height":0, 
							# "children" :
							# (
								# ## Lv
								# {
									# "name":"Status_Lv", "type":"window", "x":9, "y":30, "width":37, "height":42, 
									# "children" :
									# (
										# { "name":"Level_Header", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_level.sub" },
										# { "name":"Level_Value", "type":"text", "x":19, "y":19, "fontsize":"LARGE", "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# ),
								# },

								# ## EXP
								# {
									# "name":"Status_CurExp", "type":"window", "x":53, "y":30, "width":87, "height":42,
									# "children" :
									# (
										# { "name":"Exp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_cur_exp.sub" },
										# { "name":"Exp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },									),
								# },

								# ## REXP
								# {
									# "name":"Status_RestExp", "type":"window", "x":150, "y":30, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"RestExp_Slot", "type":"image", "x":0, "y":0, "image":LOCALE_PATH+"label_last_exp.sub" },
										# { "name":"RestExp_Value", "type":"text", "x":46, "y":19, "fontsize":"LARGE", "text":"12345678901", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# ),
								# },
							# ),
						# },

						# ## Face Slot
						# { "name" : "Face_Image", "type" : "image", "x" : 11, "y" : 11, "image" : "d:/ymir work/ui/game/windows/face_warrior.sub" },
						# { "name" : "Face_Slot", "type" : "image", "x" : 7, "y" : 7, "image" : FACE_SLOT_FILE, },

						# ## 기본 능력
						# {
							# "name":"Status_Standard", "type":"window", "x":3, "y":100, "width":200, "height":250,
							# "children" :
							# (
								# ## 기본 능력 제목
								# { "name":"Character_Bar_01", "type":"horizontalbar", "x":12, "y":8, "width":223, },
								# { "name":"Character_Bar_01_Text", "type" : "image", "x" : 13, "y" : 9, "image" : LOCALE_PATH+"label_std.sub", },
								
								# ## 능력 수련 수치
								# { 
									# "name":"Status_Plus_Label", 
									# "type":"image", 
									# "x":150, "y":11, 
									# "image":LOCALE_PATH+"label_uppt.sub", 
									
									# "children" :
									# (
										# { "name":"Status_Plus_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# ),
								# },

								# ## 기본 능력 아이템 리스트
								# {"name":"Status_Standard_ItemList1", "type" : "image", "x":17, "y":31, "image" : LOCALE_PATH+"label_std_item1.sub", },
								# {"name":"Status_Standard_ItemList2", "type" : "image", "x":100, "y":30, "image" : LOCALE_PATH+"label_std_item2.sub", },

								# ## HTH
								# {
									# "name":"HTH_Label", "type":"window", "x":50, "y":32, "width":60, "height":20,
									# "children" :
									# (
										# { "name":"HTH_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										# { "name":"HTH_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										# { "name":"HTH_Plus", "type" : "button", "x":41, "y":3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									# ),
								# },
								# ## INT
								# {
									# "name":"INT_Label", "type":"window", "x":50, "y":32+23, "width":60, "height":20,
									# "children" :
									# (
										# { "name":"INT_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										# { "name":"INT_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										# { "name":"INT_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									# )
								# },
								# ## STR
								# {
									# "name":"STR_Label", "type":"window", "x":50, "y":32+23*2, "width":60, "height":20,
									# "children" :
									# (
										# { "name":"STR_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										# { "name":"STR_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										# { "name":"STR_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									# )
								# },
								# ## DEX
								# {
									# "name":"DEX_Label", "type":"window", "x":50, "y":32+23*3, "width":60, "height":20, 
									# "children" :
									# (
										# { "name":"DEX_Slot", "type":"image", "x":0, "y":0, "image":SMALL_VALUE_FILE },
										# { "name":"DEX_Value", "type":"text", "x":20, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
										# { "name":"DEX_Plus", "type" : "button", "x" : 41, "y" : 3, "default_image" : ROOT_PATH+"btn_plus_up.sub", "over_image" : ROOT_PATH+"btn_plus_over.sub", "down_image" : ROOT_PATH+"btn_plus_down.sub", },
									# )
								# },

								# { "name":"HTH_Minus", "type" : "button", "x":9, "y":35, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								# { "name":"INT_Minus", "type" : "button", "x":9, "y":35+23, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								# { "name":"STR_Minus", "type" : "button", "x":9, "y":35+23*2, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },
								# { "name":"DEX_Minus", "type" : "button", "x":9, "y":35+23*3, "default_image" : ROOT_PATH+"btn_minus_up.sub", "over_image" : ROOT_PATH+"btn_minus_over.sub", "down_image" : ROOT_PATH+"btn_minus_down.sub", },

								# ####

								# ## HP
								# {
									# "name":"HEL_Label", "type":"window", "x":145, "y":32, "width":50, "height":20,
									# "children" :
									# (
										# { "name":"HP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										# { "name":"HP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# ),
								# },
								# ## SP
								# {
									# "name":"SP_Label", "type":"window", "x":145, "y":32+23, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"SP_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										# { "name":"SP_Value", "type":"text", "x":45, "y":3, "text":"9999/9999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },
								# ## ATT
								# {
									# "name":"ATT_Label", "type":"window", "x":145, "y":32+23*2, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"ATT_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										# { "name":"ATT_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# ),
								# },
								# ## DEF
								# {
									# "name":"DEF_Label", "type":"window", "x":145, "y":32+23*3, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"DEF_Slot", "type":"image", "x":0, "y":0, "image":LARGE_VALUE_FILE },
										# { "name":"DEF_Value", "type":"text", "x":45, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },
							# ),
						# },
						
						# ## 부가 능력
						# { 
							# "name":"Status_Extent", "type":"window", "x":3, "y":221, "width":200, "height":50, 
							# "children" :
							# (

								# ## 부가 능력 제목
								# { "name":"Status_Extent_Bar", "type":"horizontalbar", "x":12, "y":6, "width":223, },
								# { "name":"Status_Extent_Label", "type" : "image", "x" : 15, "y" : 6, "image" : LOCALE_PATH+"label_ext.sub", },

								# ## 기본 능력 아이템 리스트
								# {"name":"Status_Extent_ItemList1", "type" : "image", "x":11, "y":31, "image" : LOCALE_PATH+"label_ext_item1.sub", },
								# {"name":"Status_Extent_ItemList2", "type" : "image", "x":128, "y":32, "image" : LOCALE_PATH+"label_ext_item2.sub", },

								# ## MSPD - 이동 속도
								# {
									# "name":"MOV_Label", "type":"window", "x":66, "y":33, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"MSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										# { "name":"MSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },

								# ## ASPD - 공격 속도
								# {
									# "name":"ASPD_Label", "type":"window", "x":66, "y":33+23, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"ASPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										# { "name":"ASPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },

								# ## CSPD - 주문 속도
								# {
									# "name":"CSPD_Label", "type":"window", "x":66, "y":33+23*2, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"CSPD_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										# { "name":"CSPD_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },

								# ## MATT - 마법 공격력
								# {
									# "name":"MATT_Label", "type":"window", "x":183, "y":33, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"MATT_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										# { "name":"MATT_Value", "type":"text", "x":26, "y":3, "text":"999-999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },

								# ## MDEF - 마법 방어력
								# {
									# "name":"MDEF_Label", "type":"window", "x":183, "y":33+23, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"MDEF_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										# { "name":"MDEF_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },

								# ## 회피율
								# {
									# "name":"ER_Label", "type":"window", "x":183, "y":33+23*2, "width":50, "height":20, 
									# "children" :
									# (
										# { "name":"ER_Slot", "type":"image", "x":0, "y":0, "image":MIDDLE_VALUE_FILE },
										# { "name":"ER_Value", "type":"text", "x":26, "y":3, "text":"999", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									# )
								# },

							# ),
						# },
					# ),
				# },				
				{
					"name" : "Character_Page_NEW",
					"type" : "window",
					"style" : ("attach",),

					"x" : 15 + ADD_YAMATO_SPACE + 15 + 2,
					"y" : 15,

					"width" : 260,
					"height" : 350 + 35,

					"children" :
					(
						{
							"name" : "backgroundBoard",
							"type" : "thinboard_circle",
							
							"x" : 0,
							"y" : 0,
							
							"width" : 250,
							"height" : 350 + 35,
							
							"children" : (
								{
									"name" : "characterProtraitBackground",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 8,
									
									"width" : 45,
									"height" : 45,		

									"children" : (
									
										{ "name" : "Face_Image", "type" : "image", "x" : 1, "y" : 1, "image" : "d:/ymir work/ui/game/windows/face_warrior.sub" },

									),
								},
								{
									"name" : "characterNameBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 8,
									
									"width" : 250 - 8 - 45 - 8 - 8 + 3,
									"height" : 22,
									
									"children" : (
										{
											"name" : "characterNameTextLine",
											"type" : "text",
											
											"x" : (250 - 8 - 45 - 8 - 8) / 2,
											"y" : 4, 
											
											"text" : "SehrLangerCharacterNameM",
											
											"outline" : 1,
											
											"color" : 0xffd8a055,
											"text_horizontal_align" : "center",
										},
									),
								
								},
								{
									"name" : "guildNameBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 8 + 24, 
									
									"width" : (250 - 8 - 45 - 8 - 8 + 3) / 2 - 5,
									"height" : 21,
									
									"children" : (
										{
											"name" : "guildNameTextLine",
											"type" : "text",
											
											"x" : ((250 - 8 - 45 - 8 - 8 + 3) / 2) / 2,
											"y" : 3, 
											
											"text" : "Gildenname",
											
											"outline" : 1,
											
											"text_horizontal_align" : "center",
										},
									),
								
								},
								{
									"name" : "rankNameBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + ((250 - 8 - 45 - 8 - 8 + 3) / 2 - 5) + 5,
									"y" : 8 + 24, 
									
									"width" : (250 - 8 - 45 - 8 - 8 + 3) / 2 - 5 + 5,
									"height" : 21,
									
									"children" : (
										{
											"name" : "rankNameTextLine",
											"type" : "text",
											
											"x" : ((250 - 8 - 45 - 8 - 8 + 3) / 2) / 2 + 5,
											"y" : 3, 
											
											"text" : "Freundlich",
											
											"outline" : 1,
											
											"text_horizontal_align" : "center",
										},
									),
								
								},
								
								{
									"name" : "levelTitleBackground",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5,
									
									"width" : 45,
									"height" : 21,
									
									"children" : (
										{
											"name" : "levelTitleTextLine",
											"type" : "text",
											
											"x" : 45 / 2,
											"y" : 3, 
											
											"text" : "Level",
											
											"outline" : 1,
											
											"color" : 0xffd8a055,
											"text_horizontal_align" : "center",
										},
									),									
								},
								{
									"name" : "levelBackground",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21,
									
									"width" : 45,
									"height" : 35,
									
									"children" : (
										{
											"name" : "levelTextLine",
											"type" : "text",
											
											"x" : 45 / 2,
											"y" : 35 / 2, 
											
											"text" : "45",
											
											"outline" : 1,
											
											"fontsize" : "LARGE",
											
											"text_horizontal_align" : "center",
											"text_vertical_align" : "center",
										},
									),									
								},
								{
									"name" : "expTitleBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 12 + 45 + 5,
									
									"width" : EXP_WINDOW_WIDTH + 2,
									"height" : 21,
									
									"children" : (
										{
											"name" : "expTitleTextLine",
											"type" : "text",
											
											"x" : (EXP_WINDOW_WIDTH+2) / 2,
											"y" : 3, 
											
											"text" : "EXP",
											
											"outline" : 1,
											
											"color" : 0xffd8a055,
											"text_horizontal_align" : "center",
										},
									),									
								},
								{
									"name" : "expBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 12 + 45 + 5 + 21,
									
									"width" : EXP_WINDOW_WIDTH + 2,
									"height" : 35,
									
									"children" : (
										{
											"name" : "expTextLine",
											"type" : "text",
											
											"x" : (EXP_WINDOW_WIDTH+2) / 2,
											"y" : 35 / 2, 
											
											"text" : "4.000.000.000",
											
											"outline" : 1,
											
											"fontsize" : "LARGE",
											
											"text_horizontal_align" : "center",
											"text_vertical_align" : "center",
										},
									),									
								},							
								{
									"name" : "expNeedTitleBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 5 + EXP_WINDOW_WIDTH + 2,
									"y" : 12 + 45 + 5,
									
									"width" : EXP_WINDOW_WIDTH + 6,
									"height" : 21,
									
									"children" : (
										{
											"name" : "expNeedTitleTextLine",
											"type" : "text",
											
											"x" : EXP_WINDOW_WIDTH / 2,
											"y" : 3, 
											
											"text" : "EXP benotigt",
											
											"outline" : 1,
											
											"color" : 0xffd8a055,
											"text_horizontal_align" : "center",
										},
									),									
								},
								{
									"name" : "expNeedBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 5 + EXP_WINDOW_WIDTH + 2,
									"y" : 12 + 45 + 5 + 21,
									
									"width" : EXP_WINDOW_WIDTH + 6,
									"height" : 35,
									
									"children" : (
										{
											"name" : "expNeedTextLine",
											"type" : "text",
											
											"x" : EXP_WINDOW_WIDTH / 2 + 3,
											"y" : 35 / 2, 
											
											"text" : "5.000.000.000",
											
											"outline" : 1,
											
											"fontsize" : "LARGE",
											
											"text_horizontal_align" : "center",
											"text_vertical_align" : "center",
										},
									),									
								},
								# Statuspunkte 
								# VIT
								{
									"name" : "statusPointsVITImage",
									"type" : "image",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8,
									
									"image" : "yamato_character/vit.tga",
								},
								{
									"name" : "statusPointsVITBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 12 + 45 + 5 + 21 + 35 + 8,
									
									"width" : 30,
									"height" : 20,
									
									"children" : (
									
										{
											"name" : "statusPointsVITTextLine",
											"type" : "text",
											
											"x" : 30 / 2,
											"y" : (20 / 2) - 1, 
											
											"text" : "90",
											
											"outline" : 1,
											
											"fontsize" : "LARGE",
											
											"text_horizontal_align" : "center",
											"text_vertical_align" : "center",
										},
									
									),
								
								},
								{
									"name" : "statusPointsVITButtonBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 2,
									
									"width" : 16,
									"height" : 16,
									
									
									"children" : (
										{
											"name" : "statusPointsVITButton",
											"type" : "button",
											
											"x" : 2,
											"y" : 2,
											
											"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
											"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
											"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
											"disable_image" : "d:/ymir work/ui/game/windows/btn_plus_dis.sub",
										},
									),
								},
								{
									"name" : "pointTPBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 16 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8,
									
									"width" : 125 + 6,
									"height" : 20,
									
									"children" : (
										{
											"name" : "pointTPTitleTextLine",
											"type" : "text",
											
											"x" : 4,
											"y" : 3,
											
											"text" : "TP : ",
										
										},
										{
											"name" : "pointTPBackground2",
											"type" : "thinboard_circle",
											
											"x" : 45 + 6,
											"y" : 0,
											
											"width" : 80,
											"height" : 20,										
										
											"children" : (
												{
													"name" : "pointTPTextLine",
													"type" : "text",
													
													"x" : 80 / 2,
													"y" : (20 / 2) - 1, 
													
													"text" : "16.390 / 16.390",
													
													"outline" : 1,
													
													
													"text_horizontal_align" : "center",
													"text_vertical_align" : "center",
												},											
											
											),
										},

									),
								
								},
								# INT
								{
									"name" : "statusPointsINTImage",
									"type" : "image",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25,
									
									"image" : "yamato_character/int.tga",
								},
								{
									"name" : "statusPointsINTBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25,
									
									"width" : 30,
									"height" : 20,
									
									"children" : (
									
										{
											"name" : "statusPointsINTTextLine",
											"type" : "text",
											
											"x" : 30 / 2,
											"y" : (20 / 2) - 1, 
											
											"text" : "90",
											
											"outline" : 1,
											
											"fontsize" : "LARGE",
											
											"text_horizontal_align" : "center",
											"text_vertical_align" : "center",
										},
									
									),
								
								},
								{
									"name" : "statusPointsINTButtonBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 2 + 25,
									
									"width" : 16,
									"height" : 16,
									
									
									"children" : (
										{
											"name" : "statusPointsINTButton",
											"type" : "button",
											
											"x" : 2,
											"y" : 2,
											
											"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
											"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
											"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
											"disable_image" : "d:/ymir work/ui/game/windows/btn_plus_dis.sub",
										},
									),
								},
								{
									"name" : "pointMPBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 16 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25,
									
									"width" : 125 + 6,
									"height" : 20,
									
									"children" : (
										{
											"name" : "pointMPTitleTextLine",
											"type" : "text",
											
											"x" : 4,
											"y" : 3,
											
											"text" : "MP : ",
										
										},
										{
											"name" : "pointMPBackground2",
											"type" : "thinboard_circle",
											
											"x" : 45 + 6,
											"y" : 0,
											
											"width" : 80,
											"height" : 20,										
										
											"children" : (
												{
													"name" : "pointMPTextLine",
													"type" : "text",
													
													"x" : 80 / 2,
													"y" : (20 / 2) - 1, 
													
													"text" : "6.390 / 6.390",
													
													"outline" : 1,
													
													
													"text_horizontal_align" : "center",
													"text_vertical_align" : "center",
												},											
											
											),
										},

									),
								
								},
								# STR
								{
									"name" : "statusPointsSTRImage",
									"type" : "image",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25,
									
									"image" : "yamato_character/str.tga",
								},
								{
									"name" : "statusPointsSTRBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25,
									
									"width" : 30,
									"height" : 20,
									
									"children" : (
									
										{
											"name" : "statusPointsSTRTextLine",
											"type" : "text",
											
											"x" : 30 / 2,
											"y" : (20 / 2) - 1, 
											
											"text" : "90",
											
											"outline" : 1,
											
											"fontsize" : "LARGE",
											
											"text_horizontal_align" : "center",
											"text_vertical_align" : "center",
										},
									
									),
								
								},
								{
									"name" : "statusPointsSTRButtonBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 2 + 25 + 25,
									
									"width" : 16,
									"height" : 16,
									
									
									"children" : (
										{
											"name" : "statusPointsSTRButton",
											"type" : "button",
											
											"x" : 2,
											"y" : 2,
											
											"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
											"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
											"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
											"disable_image" : "d:/ymir work/ui/game/windows/btn_plus_dis.sub",
										},
									),
								},
								{
									"name" : "pointDMGBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 16 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25,
									
									"width" : 125 + 6,
									"height" : 20,
									
									"children" : (
										{
											"name" : "pointDMGTitleTextLine",
											"type" : "text",
											
											"x" : 4,
											"y" : 3,
											
											"text" : "Angriff : ",
										
										},
										{
											"name" : "pointDMGBackground2",
											"type" : "thinboard_circle",
											
											"x" : 45 + 6,
											"y" : 0,
											
											"width" : 80,
											"height" : 20,										
										
											"children" : (
												{
													"name" : "pointDMGTextLine",
													"type" : "text",
													
													"x" : 80 / 2,
													"y" : (20 / 2) - 1, 
													
													"text" : "1.390 - 2.390",
													
													"outline" : 1,
													
													
													"text_horizontal_align" : "center",
													"text_vertical_align" : "center",
												},											
											
											),
										},

									),
								
								},
								# DEX
								{
									"name" : "statusPointsDEXImage",
									"type" : "image",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25,
									
									"image" : "yamato_character/dex.tga",
								},
								{
									"name" : "statusPointsDEXBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25,
									
									"width" : 30,
									"height" : 20,
									
									"children" : (
									
										{
											"name" : "statusPointsDEXTextLine",
											"type" : "text",
											
											"x" : 30 / 2,
											"y" : (20 / 2) - 1, 
											
											"text" : "90",
											
											"outline" : 1,
											
											"fontsize" : "LARGE",
											
											"text_horizontal_align" : "center",
											"text_vertical_align" : "center",
										},
									
									),
								
								},
								{
									"name" : "statusPointsDEXButtonBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 2 + 25 + 25 + 25,
									
									"width" : 16,
									"height" : 16,
									
									
									"children" : (
										{
											"name" : "statusPointsDEXButton",
											"type" : "button",
											
											"x" : 2,
											"y" : 2,
											
											"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
											"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
											"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
											"disable_image" : "d:/ymir work/ui/game/windows/btn_plus_dis.sub",
										},
									),
								},
								{
									"name" : "pointDEFBackground",
									"type" : "thinboard_circle",
									
									"x" : 8 + 45 + 5 + 16 + 5 + 30,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25,
									
									"width" : 125 + 6,
									"height" : 20,
									
									"children" : (
										{
											"name" : "pointDEFTitleTextLine",
											"type" : "text",
											
											"x" : 4,
											"y" : 3,
											
											"text" : "Verteidigung : ",
										
										},
										{
											"name" : "pointDEFBackground2",
											"type" : "thinboard_circle",
											
											"x" : 45 + 6 + 20,
											"y" : 0,
											
											"width" : 80 - 20,
											"height" : 20,										
										
											"children" : (
												{
													"name" : "pointDEFTextLine",
													"type" : "text",
													
													"x" : 60 / 2,
													"y" : (20 / 2) - 1, 
													
													"text" : "1.390",
													
													"outline" : 1,
													
													
													"text_horizontal_align" : "center",
													"text_vertical_align" : "center",
												},											
											
											),
										},

									),
								
								},
								
								{
									"name" : "moveSpeedBoard",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25 + 30,									
									
									"width" : 232,
									"height" : 20,
									
									"children" : (
										{
											"name" : "moveSpeedTitleTextLine",
											"type" : "text",
											
											"x" : 8,
											"y" : 3,
											
											"text" : "Bewegungsgeschwindigkeit : ",
										
										},
										{
											"name" : "moveSpeedValueBackground",
											"type" : "thinboard_circle",
											
											"x" : 232 - 60,
											"y" : 0,
											
											"width" : 60,
											"height" : 20,
											
											"children" : (
												{
													"name" : "moveSpeedValueTextLine",
													"type" : "text",
													
													"x" : 60 / 2,
													"y" : 3,
													
													"text" : "200",	

													"text_horizontal_align" : "center",
												},
											),
										},
									),
								},
								
								{
									"name" : "atkSpeedBoard",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25 + 30 + 25,									
									
									"width" : 232,
									"height" : 20,
									
									"children" : (
										{
											"name" : "atkSpeedTitleTextLine",
											"type" : "text",
											
											"x" : 8,
											"y" : 3,
											
											"text" : "Angriffsgeschwindigkeit : ",
										
										},
										{
											"name" : "atkSpeedValueBackground",
											"type" : "thinboard_circle",
											
											"x" : 232 - 60,
											"y" : 0,
											
											"width" : 60,
											"height" : 20,
											
											"children" : (
												{
													"name" : "atkSpeedValueTextLine",
													"type" : "text",
													
													"x" : 60 / 2,
													"y" : 3,
													
													"text" : "100",	

													"text_horizontal_align" : "center",
												},
											),
										},
									),
								},
								{
									"name" : "magicSpeedBoard",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25 + 30 + 25 + 25,									
									
									"width" : 232,
									"height" : 20,
									
									"children" : (
										{
											"name" : "magicSpeedTitleTextLine",
											"type" : "text",
											
											"x" : 8,
											"y" : 3,
											
											"text" : "Zaubergeschwindigkeit : ",
										
										},
										{
											"name" : "magicSpeedValueBackground",
											"type" : "thinboard_circle",
											
											"x" : 232 - 60,
											"y" : 0,
											
											"width" : 60,
											"height" : 20,
											
											"children" : (
												{
													"name" : "magicSpeedValueTextLine",
													"type" : "text",
													
													"x" : 60 / 2,
													"y" : 3,
													
													"text" : "100",	

													"text_horizontal_align" : "center",
												},
											),
										},
									),
								},	

								{
									"name" : "magicAtkBoard",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25 + 30 + 25 + 25 + 25,									
									
									"width" : 232,
									"height" : 20,
									
									"children" : (
										{
											"name" : "magicAtkTitleTextLine",
											"type" : "text",
											
											"x" : 8,
											"y" : 3,
											
											"text" : "Magie-Angriffswert : ",
										
										},
										{
											"name" : "magicAtkValueBackground",
											"type" : "thinboard_circle",
											
											"x" : 232 - 60,
											"y" : 0,
											
											"width" : 60,
											"height" : 20,
											
											"children" : (
												{
													"name" : "magicAtkValueTextLine",
													"type" : "text",
													
													"x" : 60 / 2,
													"y" : 3,
													
													"text" : "100",	

													"text_horizontal_align" : "center",
												},
											),
										},
									),
								},	
								{
									"name" : "magicDefBoard",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25 + 30 + 25 + 25 + 25 + 25,									
									
									"width" : 232,
									"height" : 20,
									
									"children" : (
										{
											"name" : "magicDefTitleTextLine",
											"type" : "text",
											
											"x" : 8,
											"y" : 3,
											
											"text" : "Magie-Verteidigung : ",
										
										},
										{
											"name" : "magicDefValueBackground",
											"type" : "thinboard_circle",
											
											"x" : 232 - 60,
											"y" : 0,
											
											"width" : 60,
											"height" : 20,
											
											"children" : (
												{
													"name" : "magicDefValueTextLine",
													"type" : "text",
													
													"x" : 60 / 2,
													"y" : 3,
													
													"text" : "100",	

													"text_horizontal_align" : "center",
												},
											),
										},
									),
								},	
								{
									"name" : "evadeBoard",
									"type" : "thinboard_circle",
									
									"x" : 8,
									"y" : 12 + 45 + 5 + 21 + 35 + 8 + 25 + 25 + 25 + 30 + 25 + 25 + 25 + 25 + 25,									
									
									"width" : 232,
									"height" : 20,
									
									"children" : (
										{
											"name" : "evadeTitleTextLine",
											"type" : "text",
											
											"x" : 8,
											"y" : 3,
											
											"text" : "Ausweichwert : ",
										
										},
										{
											"name" : "evadeValueBackground",
											"type" : "thinboard_circle",
											
											"x" : 232 - 60,
											"y" : 0,
											
											"width" : 60,
											"height" : 20,
											
											"children" : (
												{
													"name" : "evadeValueTextLine",
													"type" : "text",
													
													"x" : 60 / 2,
													"y" : 3,
													
													"text" : "100",	

													"text_horizontal_align" : "center",
												},
											),
										},
									),
								},								
							),
						
						},
					
					),
				},

				{
					"name" : "Skill_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 15 + ADD_YAMATO_SPACE + ADD_OLD_WINDOW_WITH,
					"y" : 0 + ADD_OLD_WINDOW_HEIGTH,

					"width" : 250,
					"height" : 304,

					"children" :
					(

						{
							"name":"Skill_Active_Title_Bar", "type":"horizontalbar", "x":15, "y":17, "width":223,

							"children" :
							(
								{ 
									"name":"Active_Skill_Point_Label", "type":"image", "x":145, "y":3, "image":LOCALE_PATH+"label_uppt.sub",
									"children" :
									(
										{ "name":"Active_Skill_Point_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},

								## Group Button
								{
									"name" : "Skill_Group_Button_1",
									"type" : "radio_button",

									"x" : 5,
									"y" : 2,

									"text" : "Group1",
									"text_color" : 0xFFFFE3AD,

									"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
								},

								{
									"name" : "Skill_Group_Button_2",
									"type" : "radio_button",

									"x" : 50,
									"y" : 2,

									"text" : "Group2",
									"text_color" : 0xFFFFE3AD,

									"default_image" : "d:/ymir work/ui/game/windows/skill_tab_button_01.sub",
									"over_image" : "d:/ymir work/ui/game/windows/skill_tab_button_02.sub",
									"down_image" : "d:/ymir work/ui/game/windows/skill_tab_button_03.sub",
								},

								{
									"name" : "Active_Skill_Group_Name",
									"type" : "text",

									"x" : 7,
									"y" : 1,
									"text" : "Active",

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"color" : 0xFFFFE3AD,
								},

							),
						},

						{
							"name":"Skill_ETC_Title_Bar", "type":"horizontalbar", "x":15, "y":200, "width":223,

							"children" :
							(
								{
									"name" : "Support_Skill_Group_Name",
									"type" : "text",

									"x" : 7,
									"y" : 1,
									"text" : uiScriptLocale.SKILL_SUPPORT_TITLE,

									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"color" : 0xFFFFE3AD,
								},

								{ 
									"name":"Support_Skill_Point_Label", "type":"image", "x":145, "y":3, "image":LOCALE_PATH+"label_uppt.sub",
									"children" :
									(
										{ "name":"Support_Skill_Point_Value", "type":"text", "x":62, "y":0, "text":"99", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "text_horizontal_align":"center" },
									),
								},
							),
						},
						{ "name":"Skill_Board", "type":"image", "x":13, "y":38, "image":"d:/ymir work/ui/game/windows/skill_board.sub", },

						## Active Slot
						{
							"name" : "Skill_Active_Slot",
							"type" : "slot",

							"x" : 0 + 16,
							"y" : 0 + 15 + 23,

							"width" : 223,
							"height" : 223,
							"image" : ICON_SLOT_FILE,

							"slot" :	(
											{"index": 1, "x": 1, "y":  4, "width":32, "height":32},
											{"index":21, "x":38, "y":  4, "width":32, "height":32},
											{"index":41, "x":75, "y":  4, "width":32, "height":32},

											{"index": 3, "x": 1, "y": 40, "width":32, "height":32},
											{"index":23, "x":38, "y": 40, "width":32, "height":32},
											{"index":43, "x":75, "y": 40, "width":32, "height":32},

											{"index": 5, "x": 1, "y": 76, "width":32, "height":32},
											{"index":25, "x":38, "y": 76, "width":32, "height":32},
											{"index":45, "x":75, "y": 76, "width":32, "height":32},

											{"index": 7, "x": 1, "y":112, "width":32, "height":32},
											{"index":27, "x":38, "y":112, "width":32, "height":32},
											{"index":47, "x":75, "y":112, "width":32, "height":32},

											####

											{"index": 2, "x":113, "y":  4, "width":32, "height":32},
											{"index":22, "x":150, "y":  4, "width":32, "height":32},
											{"index":42, "x":187, "y":  4, "width":32, "height":32},

											{"index": 4, "x":113, "y": 40, "width":32, "height":32},
											{"index":24, "x":150, "y": 40, "width":32, "height":32},
											{"index":44, "x":187, "y": 40, "width":32, "height":32},

											{"index": 6, "x":113, "y": 76, "width":32, "height":32},
											{"index":26, "x":150, "y": 76, "width":32, "height":32},
											{"index":46, "x":187, "y": 76, "width":32, "height":32},

											{"index": 8, "x":113, "y":112, "width":32, "height":32},
											{"index":28, "x":150, "y":112, "width":32, "height":32},
											{"index":48, "x":187, "y":112, "width":32, "height":32},
										),
						},

						## ETC Slot
						{
							"name" : "Skill_ETC_Slot",
							"type" : "grid_table",
							"x" : 18,
							"y" : 221,
							"start_index" : 101,
							"x_count" : 6,
							"y_count" : 2,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 5,
							"y_blank" : 4,
							"image" : ICON_SLOT_FILE,
						},

					),
				},
				{
					"name" : "Emoticon_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 15 + ADD_YAMATO_SPACE + ADD_OLD_WINDOW_WITH,
					"y" : 0 + ADD_OLD_WINDOW_HEIGTH,

					"width" : 250,
					"height" : 314,

					"children" :
					(
						## 기본 액션 제목
						{ "name":"Action_Bar", "type":"horizontalbar", "x":12, "y":11, "width":223, },
						{ "name":"Action_Bar_Text", "type":"text", "x":15, "y":13, "text":uiScriptLocale.CHARACTER_NORMAL_ACTION },

						## Basis Action Slot
						{
							"name" : "SoloEmotionSlot",
							"type" : "grid_table",
							"x" : 30,
							"y" : 33,
							"horizontal_align" : "center",
							"start_index" : 1,
							"x_count" : 6,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,
							"image" : ICON_SLOT_FILE,
						},

						## 상호 액션 제목
						{ "name":"Reaction_Bar", "type":"horizontalbar", "x":12, "y":8+150 - 20, "width":223, },
						{ "name":"Reaction_Bar_Text", "type":"text", "x":15, "y":10+150 - 20, "text":uiScriptLocale.CHARACTER_MUTUAL_ACTION },

						## Reaction Slot
						{
							"name" : "DualEmotionSlot",
							"type" : "grid_table",
							"x" : 30,
							"y" : 180 - 20,
							"start_index" : 51,
							"x_count" : 6,
							"y_count" : 1,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,
							"image" : ICON_SLOT_FILE,
						},
						
						{ "name":"NewAction_Bar", "type":"horizontalbar", "x":12, "y":8+150+50 - 5, "width":223, },
						{ "name":"NewAction_Bar_Text", "type":"text", "x":15, "y":10+150+50 - 5, "text":"Neue Aktionen", },
						{
							"name" : "NewEmotionSlot",
							"type" : "grid_table",
							"x" : 30,
							"y" : 180 + 50 - 5,
							"start_index" : 61,
							"x_count" : 6,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,
							"image" : ICON_SLOT_FILE,
						},						
					),
				},
				{
					"name" : "Quest_Page",
					"type" : "window",
					"style" : ("attach",),

					"x" : 15,
					"y" : 0,

					"width" : 250,
					"height" : 304,

					"children" :
					(
						{
							"name" : "Quest_Slot",
							"type" : "grid_table",
							"x" : 18,
							"y" : 20,
							"start_index" : 0,
							"x_count" : 1,
							"y_count" : 5,
							"x_step" : 32,
							"y_step" : 32,
							"y_blank" : 28,
							"image" : QUEST_ICON_BACKGROUND,
						},

						{
							"name" : "Quest_ScrollBar",
							"type" : "scrollbar",

							"x" : 25,
							"y" : 12,
							"size" : 290,
							"horizontal_align" : "right",
						},

						{ "name" : "Quest_Name_00", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 14 },
						{ "name" : "Quest_LastTime_00", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 30 },
						{ "name" : "Quest_LastCount_00", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 46 },

						{ "name" : "Quest_Name_01", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 74 },
						{ "name" : "Quest_LastTime_01", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 90 },
						{ "name" : "Quest_LastCount_01", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 106 },

						{ "name" : "Quest_Name_02", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 134 },
						{ "name" : "Quest_LastTime_02", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 150 },
						{ "name" : "Quest_LastCount_02", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 166 },

						{ "name" : "Quest_Name_03", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 194 },
						{ "name" : "Quest_LastTime_03", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 210 },
						{ "name" : "Quest_LastCount_03", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 226 },

						{ "name" : "Quest_Name_04", "type" : "text", "text" : "이름입니다", "x" : 60, "y" : 254 },
						{ "name" : "Quest_LastTime_04", "type" : "text", "text" : "남은 시간 입니다", "x" : 60, "y" : 270 },
						{ "name" : "Quest_LastCount_04", "type" : "text", "text" : "남은 개수 입니다", "x" : 60, "y" : 286 },

					),
				},
			),
		},
	),
}
