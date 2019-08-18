import uiScriptLocale

window = {
	"name" : "BiologistItem",
	# "style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : 302 - 13,
	"height" : 80,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "bar",
			# "style" : ("movable","attach",),

			"x" : 0,
			"y" : 0,

			"width" : 302 - 13,
			"height" : 80,
			
			"children" : (
				{
								
					"name" : "progressPercent",
					"type" : "text",
									
					"x" : 302 - 13 - 10,
					"y" : 60 - 3,
									
					"fontsize" : "LARGE",
									
					"text" : "70%",
					"text_horizontal_align" : "right",
					"outline" : 1,
				},				
			
			
			),
		},
		# {
			# "name" : "frameImage",
			# "type" : "image",
			
			# "x" : 0,
			# "y" : 0,
			
			# "image" : "yamato_bio/image_frame.tga",
		# },
		{
			"name" : "questName",
			"type" : "text",
			
			"x" : 15,
			"y" : 5 + 3,
			
			"text" : "Die Orkzahnforschungen",
			"outline" : 1,
		},
		{
			"name" : "timer",
			"type" : "text",
			
			"x" : 15,
			"y" : 22 + 3,
			
			"text" : "Bereit!",
			"outline" : 1,
		},
		{
			"name" : "progress",
			"type" : "text",
			
			"x" : 15,
			"y" : 22 + 3 + 15,
			
			"text" : "0 / 10",
			"outline" : 1,
		},
		{
			"name" : "itemSlot",
			"type" : "slot",
									
			"x" : 302 - 13 - 1 - 32 - 5,
			"y" : 8,
									
			"width" : 32,
			"height" : 32,
									
			"slot" : (
				{"index":0, "x":0, "y":0, "width":32, "height":32},
			),
								
		},


		# {
						
			# "name" : "progressPercent",
			# "type" : "text",
							
			# "x" : 15,
			# "y" : 60,
							
			# "fontsize" : "LARGE",
							
			# "text" : "70%",
			# "text_horizontal_align" : "right",
			# "outline" : 1,
		# },	
	),
}

