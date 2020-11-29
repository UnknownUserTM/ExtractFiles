import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"

TEMPORARY_X = +16
BUTTON_TEMPORARY_X = 5
PVP_X = -10

LINE_LABEL_X 	= 30
LINE_LABEL_X_TITLE 	= 60
LINE_DATA_X 	= 90
LINE_STEP	= 0
SMALL_BUTTON_WIDTH 	= 45
MIDDLE_BUTTON_WIDTH 	= 65


WINDOW_WIDTH = 280
WINDOW_HEIGTH = 450
YAMATO_HEIGHT_SUB = 25
window = {
	"name" : "GameOptionDialog",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30,

	"children" :
	(
		{
			"name" : "titlebar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : WINDOW_WIDTH+30+15,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			"children" : (
				## 이름색
				{
					"name" : "name_color",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 40+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_NAME_COLOR,
				},
				{
					"name" : "name_color_normal",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 40 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_NAME_COLOR_NORMAL,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "name_color_empire",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 40 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_NAME_COLOR_EMPIRE,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				## 타겟창
				{
					"name" : "target_board",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 65+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD,
				},
				{
					"name" : "target_board_no_view",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 65 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD_NO_VIEW,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},
				{
					"name" : "target_board_view",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 65 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_TARGET_BOARD_VIEW,

					"default_image" : ROOT_PATH + "Middle_Button_01.sub",
					"over_image" : ROOT_PATH + "Middle_Button_02.sub",
					"down_image" : ROOT_PATH + "Middle_Button_03.sub",
				},

				
				## PvP Mode
				{
					"name" : "pvp_mode",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 90+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_PVPMODE,
				},
				{
					"name" : "pvp_peace",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*0,
					"y" : 90 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_PVPMODE_PEACE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_PEACE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_revenge",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*1,
					"y" : 90 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_PVPMODE_REVENGE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_REVENGE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_guild",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*2,
					"y" : 90 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_PVPMODE_GUILD,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_GUILD_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},
				{
					"name" : "pvp_free",
					"type" : "radio_button",

					"x" : LINE_DATA_X+SMALL_BUTTON_WIDTH*3,
					"y" : 90 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_PVPMODE_FREE,
					"tooltip_text" : uiScriptLocale.OPTION_PVPMODE_FREE_TOOLTIP,

					"default_image" : ROOT_PATH + "small_Button_01.sub",
					"over_image" : ROOT_PATH + "small_Button_02.sub",
					"down_image" : ROOT_PATH + "small_Button_03.sub",
				},

				## Block
				{
					"name" : "block",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 115+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_BLOCK,
				},
				{
					"name" : "block_exchange_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 115 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_BLOCK_EXCHANGE,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_party_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 115 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_BLOCK_PARTY,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_guild_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 115 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_BLOCK_GUILD,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_whisper_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*0,
					"y" : 140 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_BLOCK_WHISPER,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_friend_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*1,
					"y" : 140 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_BLOCK_FRIEND,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "block_party_request_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH*2,
					"y" : 140 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_BLOCK_PARTY_REQUEST,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Chat
				{
					"name" : "chat",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 165+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT,
				},
				{
					"name" : "view_chat_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 165 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "view_chat_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 165 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Always Show Name
				{
					"name" : "always_show_name",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 190+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME,
				},
				{
					"name" : "always_show_name_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 190 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "always_show_name_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 190 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## Effect On/Off
				{
					"name" : "effect_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 215+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_EFFECT,
				},
				{
					"name" : "show_damage_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 215 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "show_damage_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 215 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_VIEW_CHAT_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				## 판매문구
				{
					"name" : "salestext_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 240+2 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_SALESTEXT,
				},
				{
					"name" : "salestext_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 240 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_ON,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "salestext_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 240 - YAMATO_HEIGHT_SUB,

					"text" : uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF,

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				## Render Target An/Aus
				{
					"name" : "RenderTarget",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 260+2,

					"text" : "Render Target",
				},
				{
					"name" : "RenderTarget_on_off",
					"type" : "toggle_button",

					"x" : LINE_DATA_X,
					"y" : 265,

					"text" : "ON / OFF",
					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				## Show Mob Info List
				{
					"name" : "show_mob_info",
					"type" : "text",

					"multi_line" : 1,

					"x" : LINE_LABEL_X,
					"y" : 265+2 - YAMATO_HEIGHT_SUB,

					"text" : "Monster Info",
				},
				{
					"name" : "show_mob_level_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X,
					"y" : 265 - YAMATO_HEIGHT_SUB,

					"text" : "Level",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "show_mob_AI_flag_button",
					"type" : "toggle_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 265 - YAMATO_HEIGHT_SUB,

					"text" : "Aggressive",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				
				# Tageszeit
				{
					"name" : "showNight_on_off",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 290+2 - YAMATO_HEIGHT_SUB,

					"text" : "Tageszeit",
				},
				# Nacht
				{
					"name" : "showNight_on_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y"	: 290 - YAMATO_HEIGHT_SUB,

					"text" : "Nacht",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				# Tag
				{
					"name" : "showNight_off_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 290 - YAMATO_HEIGHT_SUB,

					"text" : "Tag",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},

				# Kost?e ausblenden
				{
					"name" : "CostumeHideButtons",
					"type" : "text",

					"x" : LINE_LABEL_X_TITLE,
					"y" : 325+2 - YAMATO_HEIGHT_SUB,

					"text" : " Aus/Einblenden von Kost?en",
				},
				{
					"name" : "Costume_Armor",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 350+2 - YAMATO_HEIGHT_SUB,

					"text" : "R?tung",
				},
				{
					"name" : "costumeHide_hide_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 350 - YAMATO_HEIGHT_SUB,

					"text" : "Ausblenden",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "costumeHide_show_button",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 350 - YAMATO_HEIGHT_SUB,

					"text" : "Einblenden",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "Costume_Armor",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 375+2 - YAMATO_HEIGHT_SUB,

					"text" : "Waffe",
				},
				{
					"name" : "costumeHide_hide_button2",
					"type" : "radio_button",

					"x" : LINE_DATA_X,
					"y" : 375 - YAMATO_HEIGHT_SUB,

					"text" : "Ausblenden",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "costumeHide_show_button2",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH,
					"y" : 375 - YAMATO_HEIGHT_SUB
					,

					"text" : "Einblenden",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},	
				
				
				{
					"name" : "CostumeHideButtons",
					"type" : "text",

					"x" : LINE_LABEL_X_TITLE,
					"y" : 325+2 - YAMATO_HEIGHT_SUB,

					"text" : " Aus/Einblenden von Kost?en",
				},
				{
					"name" : "extra_OptionTitle",
					"type" : "text",

					"x" : LINE_LABEL_X_TITLE,
					"y" : 375+15 + 15 - YAMATO_HEIGHT_SUB,

					"text" : "Noch mehr Optionen, Juhuuu! ^^",
				},
				{
					"name" : "bindMultiShop_Title",
					"type" : "text",

					"x" : LINE_LABEL_X,
					"y" : 375+2 + 15 + 15 + 15 + 10 - YAMATO_HEIGHT_SUB,

					"text" : "Shop an Inventar binden",
				},
				{
					"name" : "bindMultiShop_RadioButton_Bind",
					"type" : "radio_button",

					"x" : LINE_DATA_X + 60,
					"y" : 375 + 15 + 15 + 15 + 10 - YAMATO_HEIGHT_SUB,

					"text" : "Binden",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},
				{
					"name" : "bindMultiShop_RadioButton_UnBind",
					"type" : "radio_button",

					"x" : LINE_DATA_X+MIDDLE_BUTTON_WIDTH + 60,
					"y" : 375 + 15 + 15 + 15 + 10 - YAMATO_HEIGHT_SUB,

					"text" : "Nicht binden",

					"default_image" : ROOT_PATH + "middle_button_01.sub",
					"over_image" : ROOT_PATH + "middle_button_02.sub",
					"down_image" : ROOT_PATH + "middle_button_03.sub",
				},				
			),
		},
	),
}
