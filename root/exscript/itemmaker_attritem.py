import uiScriptLocale
WINDOW_WIDTH = 350
window = {
	"name" : "ItemMakerSocketItem",
	"style" : ("float",),

	"x" : 0,
	"y" : 0,

	"width" : WINDOW_WIDTH - 30 + 20 - 20,
	"height" : 20,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard_circle",

			"x" : 0,
			"y" : 0,
			
			"width" : WINDOW_WIDTH - 30 + 20 - 20,
			"height" : 20,
			
			"children" : (
				{
					"name" : "attrIndexTextLine",
					"type" : "text",
									
					"x" : 8,
					"y" : 4,
								
					"text" : "0",
					"outline" : 1,
					"text_horizontal_align" : "left",
					"horizontal_align" : "left",								
				},	
				{
					"name" : "attrValueBoard",
					"type" : "thinboard_circle",
					
					
					"x" : WINDOW_WIDTH - 30 + 20 - 20 - 60,
					"y" : 0,
					
					"width" : 60,
					"height" : 20,
					
					"children" : (
					
						{
							"name" : "attrValueTextLine",
							"type" : "text",
											
							"x" : 0,
							"y" : 4,
										
							"text" : "0",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
						},					
					),
				},
					
			),
		},	
	),
}

