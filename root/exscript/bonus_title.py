import uiScriptLocale

window = {
	"name" : "BonusTitle",
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

			"x" : 0,
			"y" : 0,

			"width" : 225,
			"height" : 22,
			
			"children" : (
				{
								
					"name" : "titleTextLine",
					"type" : "text",
									
					"x" : 225 / 2,
					"y" : 3,
																		
					"text" : "Title",
					"text_horizontal_align" : "center",
					"outline" : 1,
					"color" : 0xffd8a055,
				},				
			
			
			),
		},	
	),
}

