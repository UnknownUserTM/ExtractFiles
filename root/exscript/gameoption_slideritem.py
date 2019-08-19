import uiScriptLocale

BUTTON_SIZE = 60

window = {
	"name" : "GameOptionTitle",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 350 - 10 - 2,
	"height" : 22,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard_circle",
			"style" : ("movable","attach",),

			"x" : 7,
			"y" : 0,

			"width" : 350 - 10 - 2 - 5 - 10 - 5,
			"height" : 22,
			
			"children" : (
				{
								
					"name" : "titleTextLine",
					"type" : "text",
									
					"x" : 8,
					"y" : 3,
																		
					"text" : "Keine Ahnung",
					# "text_horizontal_align" : "center",
					"outline" : 1,
				},
				# {
								
					# "name" : "percentTextLine",
					# "type" : "text",
									
					# "x" : 350 - 10 - 2 - 5 - 10 - 5 - 165 - 15,
					# "y" : 3,
																		
					# "text" : "0%",
					# "text_horizontal_align" : "rigth",
					# "outline" : 1,
				# },
				{
					"name" : "slideBar",
					"type" : "sliderbar",

					"x" : 350 - 10 - 2 - 5 - 10 - 5 - 165,
					"y" : 3,
				},			
			
			),
		},	
	),
}

