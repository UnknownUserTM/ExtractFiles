import uiScriptLocale

WINDOW_WIDTH = 500
WINDOW_HEIGTH = 40

window = {
	"name" : "TutorialJoinWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 150 - WINDOW_WIDTH,
	"y" : 15,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGTH,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 0,

			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGTH,
			
			"children" : (
				{
					"name" : "infoTextLine",
					"type" : "text",
					
					"x" : 12,
					"y" : 13,
					
					"text" : "Das Tutorial wartet auf dich! Du kannst es bis lv.30 noch betreten.",
					"color" : 0xffd8a055,
					"outline" : 1,
				
				
				
				},
				{
					"name" : "enterButton",
					"type" : "button",
							
					"x" : WINDOW_WIDTH - 170,
					"y" : 7,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Betreten",
						
				},
			
			
			
			),
		},
	),
}

