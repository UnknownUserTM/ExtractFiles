import uiScriptLocale

WINDOW_WIDTH = 400
WINDOW_HEIGTH = 50

window = {
	"name" : "TempDropEventGuide",
	# "style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

	"width" : 380,
	"height" : 40,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard",
			# "style" : ("movable","attach",),

			"x" : 0,
			"y" : 0,

			"width" : 380,
			"height" : 40,
			
			"children" : (
				{
					"name" : "itemSlot",
					"type" : "slot",
									
					"x" : 4,
					"y" : 4,
									
					"width" : 32,
					"height" : 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
									
					"slot" : (
						{"index":0, "x":0, "y":0, "width":32, "height":32},
					),
				},			

				{
					"name" : "targetTextLine",
					"type" : "text",
							
					"x" : 8 + 36,
					"y" : 12,
							
					"text" : "Sturm auf die Runenfestung",
							
					"outline" : 1,
						
				},
				{
					"name" : "runTimeTextLine",
					"type" : "text",
							
					"x" : 12,
					"y" : 12,
							
					"text" : "00:00:00",
					"text_horizontal_align":"right",		
					"horizontal_align":"right",		
					"outline" : 1,
						
				},
		
			
			
			),
			
			
		},
	),
}

