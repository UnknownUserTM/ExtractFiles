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
				{
					"name" : "toggleButton01BG",
					"type" : "thinboard_circle",
					
					"x" : 350 - 10 - 2 - 5 - 10 - 5 - (BUTTON_SIZE*2),
					"y" : 0,
					
					"width" : BUTTON_SIZE,
					"height" : 22,
					
					"children" : (
						{
							"name" : "greenBar",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},					
						{
							"name" : "enableOptionTitle",
							"type" : "text",
											
							"x" : BUTTON_SIZE / 2,
							"y" : 3,
																				
							"text" : "An",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},	

					),
				},
				{
					"name" : "toggleButton02BG",
					"type" : "thinboard_circle",
					
					"x" : 350 - 10 - 2 - 5 - 10 - 5 - BUTTON_SIZE,
					"y" : 0,
					
					"width" : BUTTON_SIZE,
					"height" : 22,
					
					"children" : (
						{
							"name" : "redBar",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "disableOptionTitle",
							"type" : "text",
											
							"x" : BUTTON_SIZE / 2,
							"y" : 3,
																				
							"text" : "Aus",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},	
						
					),
				},			
			
			),
		},	
	),
}

