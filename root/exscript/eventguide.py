import uiScriptLocale

WINDOW_WIDTH = 180
WINDOW_HEIGTH = 110

window = {
	"name" : "EventGuideWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 330,
	"y" : 80,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGTH,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 0,

			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGTH,
			
			"children" : (
				{
					"name" : "event_button_0",
					"type" : "button",
							
					"x" : 10,
					"y" : 8,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Drop-Event (0)",
				},	
				{
					"name" : "event_button_1",
					"type" : "button",
							
					"x" : 10,
					"y" : 8 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "OX-Wettbewerb",
				},					
			
				{
					"name" : "close_button",
					"type" : "button",
							
					"x" : 10,
					"y" : WINDOW_HEIGTH - 35,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Schlieﬂen",
				},				
			),
		},
	),
}

