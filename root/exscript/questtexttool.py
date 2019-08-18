import uiScriptLocale

WINDOW_WIDTH = 320
WINDOW_HEIGTH = 430
IMAGE_PATH = "yamato_questboard/"

window = {
	"name" : "QuestTextTool",
	"style" : ("movable", "float",),

	# "x" : SCREEN_WIDTH - WINDOW_WIDTH - 250,
	# "y" : (SCREEN_HEIGHT - WINDOW_HEIGTH) / 2 - 180,
	"x" : SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60 - 230,
	"y" : 110,
	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30,

	"children" :
	(				
		{
			"name" : "TitleBar",
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
			"style" : ("attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			"children" : (
				{
					"name" : "questTextInputBoard",
					"type" : "thinboard_circle",
											
					"x" : 25,
					"y" : 15,
											
					"width" : 300 - 20,
					"height" : 20,
																						
					"children" : (
						{
							"name" : "questText_EditLine",
							"type" : "editline",
													
							"x" : 4,
							"y" : 2,
													
							"input_limit" : 150,
													
							"width" : 270, #300 - 20,
							"height" : 20,
						},
					),
				},
				{
					"name" : "addTextButton",
					"type" : "button",
					
					"x" : 325 - 20,
					"y" : 15,
					
					"default_image" : "d:/ymir work/ui/game/taskbar/Send_Chat_Button_01.sub",
					"over_image" : "d:/ymir work/ui/game/taskbar/Send_Chat_Button_02.sub",
					"down_image" : "d:/ymir work/ui/game/taskbar/Send_Chat_Button_03.sub",
				},
				{
					"name":"QuestBottomBar_0",
					"type":"image",
					"style" : ("attach",),

					"x" : 25,
					"y" : 15 + 360 + 2 + 30,

					"image" : IMAGE_PATH + "bottom_texture_tab.tga",
							
							
					"children" : 
					(
						{
							"name" : "SaveButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 5,
									
							"text" : "Save",
							# "tooltip_text" : "Klicke hier um die Quest anzunehmen.",
									
							"default_image" : IMAGE_PATH + "normal_button_n.tga",
							"over_image" : IMAGE_PATH + "normal_button_h.tga",
							"down_image" : IMAGE_PATH + "normal_button_p.tga",
							"disable_image" : IMAGE_PATH + "normal_button_d.tga",
						},
						{
							"name" : "ClearButton",
							"type" : "button",
									
							"x" : 0 + 95 + 5,
							"y" : 5,
									
							"text" : "Clear All",
							# "tooltip_text" : "Klicke hier um die Quest abzulehnen.",
									
							"default_image" : IMAGE_PATH + "normal_button_n.tga",
							"over_image" : IMAGE_PATH + "normal_button_h.tga",
							"down_image" : IMAGE_PATH + "normal_button_p.tga",
							"disable_image" : IMAGE_PATH + "normal_button_d.tga",
						},
						{
							"name" : "BackButton",
							"type" : "button",
									
							"x" : 0 + 95 + 5 + 95 + 5,
							"y" : 5,
									
							"text" : "Clear Last",
							# "tooltip_text" : "Klicke hier um die Quest abzulehnen.",
									
							"default_image" : IMAGE_PATH + "normal_button_n.tga",
							"over_image" : IMAGE_PATH + "normal_button_h.tga",
							"down_image" : IMAGE_PATH + "normal_button_p.tga",
							"disable_image" : IMAGE_PATH + "normal_button_d.tga",
						},
					),
				},			
			),
		},
	),
}

