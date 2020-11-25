import uiScriptLocale

WINDOW_WIDTH = 500
WINDOW_HEIGTH = 400

window = {
	"name" : "MountWindow",
	"style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

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
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			
			"children" : (
				{
					"name" : "MountHeadBackground",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 9,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : WINDOW_HEIGTH + 5,
				},
			),
		},
	),
}

