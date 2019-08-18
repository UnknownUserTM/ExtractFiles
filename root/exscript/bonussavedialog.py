import uiScriptLocale

WINDOW_WIDTH = 250
WINDOW_HEIGTH = 100

window = {
	"name" : "BonusSaveDialog",
	# "style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30,

	"children" :
	(				
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			# "style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : WINDOW_WIDTH+30+15,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			# "style" : ("movable","attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			
			"children" : (
				
				{
					"name" : "inputBackground",
					"type" : "bar",
					
					"x" : 25,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 20,
					"height" : WINDOW_HEIGTH,
				
					"children" : (
					
						{
							"name" : "nameyourset_TextLine",
							"type" : "text",
							"x" : 0,
							"y" : 8,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Name your bonus set: (0/20)",							
						},	
						{
							"name" : "nameyourset_EditLineBoard",
							"type" : "thinboard_circle",
											
							"x" : 0,
							"y" : 28,
							
							"horizontal_align" : "center", 
											
							"width" : 100,
							"height" : 18,
																						
							"children" : (
								{
									"name" : "nameyourset_EditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
													
									"width" : 100,
									"height" : 20,
								},
							),
						},
				
						{
							"name" : "saveButton",
							"type" : "button",
													
							"x" : 20,
							"y" : 60,
												
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Save",
												
						},	
						{
							"name" : "closeButton",
							"type" : "button",
													
							"x" : 20 + 95,
							"y" : 60,
												
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Close",
												
						},						
					
					),
				
				},
			
			
			
			
			),
		},
	),
}

