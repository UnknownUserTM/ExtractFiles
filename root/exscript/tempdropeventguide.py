import uiScriptLocale

WINDOW_WIDTH = 400
WINDOW_HEIGTH = 50

window = {
	"name" : "TempDropEventGuide",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60 - 230 + 20,
	"y" : 80,

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
					"name" : "titleBarContent",
					"type" : "horizontalbar",
					
					"x" : 25,
					"y" : 15,
					
					"width" : WINDOW_WIDTH - 20,
				
				
					"children" : (
						{
							"name" : "itemTitleTextLine",
							"type" : "text",
							
							"x" : 8,
							"y" : 2,
							
							"text" : "Item:",
							
							"outline" : 1,
						
						},
						{
							"name" : "mapMonsterTitleTextLine",
							"type" : "text",
							
							"x" : 50,
							"y" : 2,
							
							"text" : "Map / Monster:",
							
							"outline" : 1,
						
						},
						{
							"name" : "durationTitleTextLine",
							"type" : "text",
							
							"x" : WINDOW_WIDTH - 20 - 50,
							"y" : 2,
							
							"text" : "Laufzeit:",
							
							"outline" : 1,
						
						},
					
					),
				},
				{
					"name" : "errorTextLine",
					"type" : "text",
									
					"x" : 0,
					"y" : 5,
									
					"horizontal_align" : "center", 
					"text_horizontal_align":"center",
					"vertical_align" : "center",
					"text_vertical_align" : "center",
					"outline" : 1,
					"text" : "Error: No eventInformation available!",
					
						
				},			
			
			
			),
			
			
		},
	),
}

