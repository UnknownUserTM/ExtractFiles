import grp
import localeInfo
import app

X_ADD_SPACE = 40
BOARD_X = X_ADD_SPACE * 12 + 20
BOARD_Y = 200
COLOR_LINE = 0xff5b5e5e
BOARD_TYPE_WIDTH = 120
BOARD_TYPE_HEIGHT = 101

window = {
	"name" : "AnnouncementBoard",
	"x" : 0,
	"y" : 0,
	"style" : ("movable", "float",),
	"width" : BOARD_X + 91,
	"height" : BOARD_Y,
	"children" :
	(
		{
			"name" : "AnnouncementTypeBoard",
			"type" : "board",
			"style" : ("attach",),
			"x" : BOARD_X-30,
			"y" : 10,
			"vertical_align":"center",
			"width" : BOARD_TYPE_WIDTH,
			"height" : BOARD_TYPE_HEIGHT,
			"children" :
			(
				{
					"name" : "backgroundBar",
					"type" : "bar",
					"x" : 9,
					"y" : 5,
					"width" : BOARD_TYPE_WIDTH-17,
					"height" : BOARD_TYPE_HEIGHT-12,
					"color" : grp.GenerateColor(0.0, 0.0, 0.0, 0.5),
				},
				
				{
					"name" : "btnNotice",
					"type" : "radio_button",
					"x" : 25,
					"y" : 7,
					"text" : localeInfo.ANNOUNCEMENT_MANAGER_NOTICE,
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				{
					"name" : "btnBigNotice",
					"type" : "radio_button",
					"x" : 25,
					"y" : 7 + 22,
					"text" : localeInfo.ANNOUNCEMENT_MANAGER_BIG_NOTICE,
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				{
					"name" : "btnMapNotice",
					"type" : "radio_button",
					"x" : 25,
					"y" : 7 + (22 * 2),
					"text" : localeInfo.ANNOUNCEMENT_MANAGER_MAP_NOTICE,
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				
				{
					"name" : "btnWhisper",
					"type" : "radio_button",
					"x" : 25,
					"y" : 7 + (22 * 3),
					"text" : localeInfo.ANNOUNCEMENT_MANAGER_WHISPER,
					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			),
		},
	
		{
			"name" : "board",
			"type" : "board",
			"x" : 0,
			"y" : 0,
			"width" : BOARD_X,
			"height" : BOARD_Y,
			"children" :
			(
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 8,
					"y" : 8,
					"width" : BOARD_X - 13,
					"color" : "gray",
					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"x" : 0,
							"y" : 3,
							"horizontal_align" : "center",
							"text" : localeInfo.ANNOUNCEMENT_MANAGER_TITLE_NAME,
							"text_horizontal_align":"center"
						},
					),
				},

				{
					"name" : "bg1",
					"type" : "bar",
					"x" : 9,
					"y" : 32,
					"width" : BOARD_X - 19,
					"height" : BOARD_Y - 42,
					"color" : grp.GenerateColor(0.0, 0.0, 0.0, 0.5),
				},
				
				{
					"name" : "bg2",
					"type" : "bar",
					"x" : 9,
					"y" : 95,
					"width" : BOARD_X-20,
					"height" : BOARD_Y-133,
					"color" : grp.GenerateColor(0.0, 0.0, 0.0, 0.9),
				},
				
				{ "name" : "renderLine_0", "type" : "line", "x" : 8, "y" : 30, "width" : 0, "height" : BOARD_Y-40, "color" : COLOR_LINE, },
				{ "name" : "renderLine_1", "type" : "line", "x" : BOARD_X-10, "y" : 30, "width" : 0, "height" : BOARD_Y-40, "color" : COLOR_LINE, },
				{ "name" : "renderLine_2", "type" : "line", "x" : 8, "y" : BOARD_Y-10, "width" : BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },
				{ "name" : "renderLine_3", "type" : "line", "x" : 8, "y" : 30, "width" : BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },		
				{ "name" : "renderLine_4", "type" : "line", "x" : 8, "y" : 49, "width" : BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },	
				{ "name" : "renderLine_5", "type" : "line", "x" : 8, "y" : 72, "width" : BOARD_X-17, "height" : 0, "color" : COLOR_LINE, },	
				{ "name" : "renderLine_6", "type" : "line", "x" : 9, "y" : 93, "width" : BOARD_X-19, "height" : 0, "color" : COLOR_LINE, },
				{ "name" : "renderLine_7", "type" : "line", "x" : 9, "y" : 159, "width" : BOARD_X-19, "height" : 0, "color" : COLOR_LINE, },	
				
				{
					"name": "horizontalbar",
					"type":"horizontalbar",
					"x": 9,
					"y": 75,
					"width": 0,
					"children" :
					(
						{
							"name":"textLine1",
							"type":"text",
							"x": 5,
							"y": 1,
							"text": "",
							"color" : 0xffc3b168,
						},
						{
							"name":"textLine2",
							"type":"text",
							"x": 290,
							"y": 1,
							"text": "",
							"color" : 0xffc3b168,
						},
					),
				},
				
				{
					"name" : "currentLine_Value",
					"type" : "editline",
					"x" : 15,
					"y" : 95,
					"width" : 540,
					"height" : 80,
					"input_limit" : 512,
					"multi_line" : 1,
					"limit_width" : 0,
				},
				
				{
					"name" : "accept_button",
					"type" : "button",
					"x" : 16,
					"y" : 163,
					"text": localeInfo.ANNOUNCEMENT_MANAGER_SEND,
					"default_image" : "d:/ymir work/ui/public/Xlarge_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Xlarge_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Xlarge_button_03.sub",
				},

				{
					"name" : "clear_button",
					"type" : "button",
					"x" : 16+289,
					"y" : 163,
					"text": localeInfo.ANNOUNCEMENT_MANAGER_CLEAR_TEXT,
					"default_image" : "d:/ymir work/ui/public/Xlarge_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/Xlarge_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/Xlarge_button_03.sub",
				},
			),
		},
	),
}