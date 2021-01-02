import uiScriptLocale

window = {
	"name" : "BonusItem",
	"style" : ("float",),

	"x" : 0,
	"y" : 0,

	"width" : 225,
	"height" : 22,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard_circle",
			"style" : ("attach",),

			"x" : 5,
			"y" : 0,

			"width" : 215,
			"height" : 22,
			
			"children" : (
				{
								
					"name" : "titleTextLine",
					"type" : "text",
									
					"x" : 5,
					"y" : 3,
																		
					"text" : "Title",
					"outline" : 1,
				},	
				{
					"name" : "valueBackground",
					"type" : "thinboard_circle",
					
					"x" : 215 - 40,
					"y" : 0,
					
					"width" : 40,
					"height" : 22,
					
					"children" : (
					
						{
										
							"name" : "bonusValueTextLine",
							"type" : "text",
											
							"x" : 40 / 2,
							"y" : 3,
																				
							"text" : "1440",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},						
					
					),
				
				
				},

			),
		},
		{
			"name" : "toolTipWindow",
			"type" : "window",
			
			"x" : 0,
			"y" : 0,
		
			"width" : 225,
			"height" : 22,		
		},
	),
}

