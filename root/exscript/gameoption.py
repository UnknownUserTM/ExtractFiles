import uiScriptLocale

WINDOW_WIDTH = 365
WINDOW_HEIGTH = 400

window = {
	"name" : "GameOptionWindow",
	"style" : ("movable", "float",),

	"x" : (SCREEN_WIDTH/2) - (WINDOW_WIDTH/2) + 30,
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
					"name" : "background",
					"type" : "thinboard_circle",
					"style" : ("movable","attach",),
					
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 25 + 15,
					"height" : WINDOW_HEIGTH + 5,
					
				},
				{
					"name" : "scrollBar",
					"type" : "small_thin_scrollbar",
											
					"x" : WINDOW_WIDTH - 20 + 15,
					"y" : 10,
											
					"size" : WINDOW_HEIGTH + 5,
				},
				{
					"name" : "devTextLine",
					"type" : "text",
					
					"x" : WINDOW_WIDTH + 30,
					"y" : 10,
					
					"text" : "0",
					"outline" : 1,
				
				
				
				
				},
			
			
			
			),
		},
	),
}
