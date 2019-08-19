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
					
					"x" : 350 - 10 - 2 - 5 - 10 - 5 - (BUTTON_SIZE*4),
					"y" : 0,
					
					"width" : BUTTON_SIZE,
					"height" : 22,
					
					"children" : (
						{
							"name" : "redBar01",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "greenBar01",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},				
						{
							"name" : "OptionTitle01",
							"type" : "text",
											
							"x" : BUTTON_SIZE / 2,
							"y" : 3,
																				
							"text" : "Frieden",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},	

					),
				},
				{
					"name" : "toggleButton02BG",
					"type" : "thinboard_circle",
					
					"x" : 350 - 10 - 2 - 5 - 10 - 5 - (BUTTON_SIZE*3),
					"y" : 0,
					
					"width" : BUTTON_SIZE,
					"height" : 22,
					
					"children" : (
						{
							"name" : "redBar02",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "greenBar02",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "OptionTitle02",
							"type" : "text",
											
							"x" : BUTTON_SIZE / 2,
							"y" : 3,
																				
							"text" : "Feindlich",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},	
						
					),
				},	
				{
					"name" : "toggleButton03BG",
					"type" : "thinboard_circle",
					
					"x" : 350 - 10 - 2 - 5 - 10 - 5 - (BUTTON_SIZE*2),
					"y" : 0,
					
					"width" : BUTTON_SIZE,
					"height" : 22,
					
					"children" : (
						{
							"name" : "redBar03",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "greenBar03",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "OptionTitle03",
							"type" : "text",
											
							"x" : BUTTON_SIZE / 2,
							"y" : 3,
																				
							"text" : "Gilde",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},	
						
					),
				},
				{
					"name" : "toggleButton04BG",
					"type" : "thinboard_circle",
					
					"x" : 350 - 10 - 2 - 5 - 10 - 5 - BUTTON_SIZE,
					"y" : 0,
					
					"width" : BUTTON_SIZE,
					"height" : 22,
					
					"children" : (
						{
							"name" : "redBar04",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "greenBar04",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BUTTON_SIZE,
							"height" : 22,
						},
						{
							"name" : "OptionTitle04",
							"type" : "text",
											
							"x" : BUTTON_SIZE / 2,
							"y" : 3,
																				
							"text" : "Frei",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},	
						
					),
				},				
			
			),
		},	
	),
}

