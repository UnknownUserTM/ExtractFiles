import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"
YAMATO_WIDTH = 50
window = {
	"name" : "SystemDialog",
	"style" : ("float",),

	"x" : SCREEN_WIDTH/2 - 100,
	"y" : SCREEN_HEIGHT/2 - 114 -50,

	"width" : 280,
	"height" : 400,

	"children" :
	(
		{
			"name" : "board",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : "yamato_menu/mm_partial_merge_1.tga",

			"children" :
			(
				# {
					# "name" : "system_chhange_button",
					# "type" : "button",

					# "x" : 10,
					# "y" : 7,

					# "text" : "Channel wechseln",

					# "default_image" : ROOT + "XLarge_Button_01.sub",
					# "over_image" : ROOT + "XLarge_Button_02.sub",
					# "down_image" : ROOT + "XLarge_Button_03.sub",
				# },
				{
					"name" : "system_chhange_1_button",
					"type" : "button",

					"x" : 12 + YAMATO_WIDTH + 20,
					"y" : 7 + 15,

					"text" : "CH 1",


					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
				},				
				{
					"name" : "system_chhange_2_button",
					"type" : "button",

					"x" : 12 + 31 + YAMATO_WIDTH + 20,
					"y" : 7 + 15,

					"text" : "CH 2",


					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
				},
				{
					"name" : "system_chhange_3_button",
					"type" : "button",

					"x" : 12 + 31 + 31 + YAMATO_WIDTH + 20,
					"y" : 7 + 15,

					"text" : "CH 3",


					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
				},				
				{
					"name" : "system_chhange_4_button",
					"type" : "button",

					"x" : 12 + 31 + 31 + 31 + YAMATO_WIDTH + 20,
					"y" : 7 + 15,

					"text" : "CH 4",


					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
				},					
				{
					"name" : "openBrowser_WikiButton",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 65,

					"text" : "Vote4Gift",
					"text_color" : 0xffF8BF24,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},				
				{
					"name" : "system_option_button",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 87 + 15,

					"text" : uiScriptLocale.SYSTEMOPTION_TITLE,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},
				{
					"name" : "game_option_button",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 87 + 45 - 30,

					"text" : uiScriptLocale.GAMEOPTION_TITLE,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},
				{
					"name" : "change_button",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 117 + 70 - 30,

					"text" : uiScriptLocale.SYSTEM_CHANGE,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},
				{
					"name" : "logout_button",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 177 + 50 - 30,

					"text" : uiScriptLocale.SYSTEM_LOGOUT,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},

				{
					"name" : "exit_button",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 207 + 50 - 30,

					"text" : uiScriptLocale.SYSTEM_EXIT,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},
				{
					"name" : "sofort_button",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 237 + 50 - 30,

					"text" : uiScriptLocale.SYSTEM_KILL,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 10 + YAMATO_WIDTH,
					"y" : 267 + 70 - 30,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
				},
			),
		},
	),
}
