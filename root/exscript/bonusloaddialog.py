import uiScriptLocale

WINDOW_WIDTH = 250
WINDOW_HEIGTH = 200

window = {
	"name" : "BonusLoadDialog",
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
							"name" : "choose_TextLine",
							"type" : "text",
							"x" : 0,
							"y" : 8,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Choose your bonus set!",							
						},	
						{
							"name" : "list_box",
							"type" : "listbox",
							
							"x" : 5,
							"y" : 22,
							
							"width" : WINDOW_WIDTH - 20 - 15,
							"height" : WINDOW_HEIGTH - 30 - 15 - 10,
						},
						{
							"name" : "scrollbar",
							"type" : "small_thin_scrollbar",
							
							"x" : WINDOW_WIDTH - 20 - 15,
							"y" : 22,
							
							"size" : WINDOW_HEIGTH - 30 - 15,
						
						
						
						
						},
				
						{
							"name" : "loadButton",
							"type" : "button",
													
							"x" : 20,
							"y" : 170,
												
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Load",
												
						},	
						{
							"name" : "closeButton",
							"type" : "button",
													
							"x" : 20 + 95,
							"y" : 170,
												
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

