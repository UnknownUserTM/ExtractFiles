import uiScriptLocale

window = {
	"name" : "GameOptionTitle",
	"style" : ("float",),

	"x" : 0,
	"y" : 0,

	"width" : 350 - 10 - 2,
	"height" : 22,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard_circle",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 350 - 10 - 2 - 5,
			"height" : 22,
			
			"children" : (
				{
								
					"name" : "titleTextLine",
					"type" : "text",
									
					"x" : 338 / 2,
					"y" : 3,
																		
					"text" : "Title",
					"text_horizontal_align" : "center",
					"outline" : 1,
				},				
			
			
			),
		},	
	),
}

