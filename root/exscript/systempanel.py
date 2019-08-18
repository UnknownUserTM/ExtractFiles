import uiScriptLocale

WINDOW_WIDTH = 300
WINDOW_HEIGTH = 550

window = {
	"name" : "CalenderWindow",
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
		},
	),
}

