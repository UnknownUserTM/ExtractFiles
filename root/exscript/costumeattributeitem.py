import uiScriptLocale

window = {
	"name" : "CostumeAttributeItem",
	"style" : ("float",),

	"x" : 0,
	"y" : 0,

	"width" : 290 - 24,
	"height" : 22,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard_circle",
			# "style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 290 - 24,
			"height" : 22,
			
			"children" : (
				{
								
					"name" : "bonusTitleTextLine",
					"type" : "text",
									
					"x" : 8,
					"y" : 3,
																		
					"text" : "Stark gegen Irgendwas",
					# "text_horizontal_align" : "center",
					"outline" : 1,
				},				
				{
								
					"name" : "bonusValueTextLine",
					"type" : "text",
									
					"x" : 8,
					"y" : 3,
																		
					"text" : "0",
					"text_horizontal_align" : "right",
					"horizontal_align" : "right",
					"outline" : 1,
				},				
			
			),
		},	
	),
}

