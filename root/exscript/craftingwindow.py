import uiScriptLocale

WINDOW_WIDTH = 329
WINDOW_HEIGTH = 521

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

			"children" : (
				{
					"name" : "dungeonSelectBackground",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 9,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : WINDOW_HEIGTH + 5,
					
					"children" : (
					

						{
							"name" : "craftSlotWindow",
							"type" : "image",
							
							"x" : 1,
							"y" : WINDOW_HEIGTH + 5 - 138 - 1,
							
							"image" : "d:/ymir work/ui/game/cube/cube_slot_bg.sub",

						},					
					
						{
							"name" : "craftingSelectBoard",
							"type" : "thinboard_circle",
							
							"x" : 0,
							"y" : 1,
							
							"width" : WINDOW_WIDTH - 10,
							"height" : WINDOW_HEIGTH + 5 - 138 - 1,
					
						},					
					),
				},
			),

		},
	),
}

