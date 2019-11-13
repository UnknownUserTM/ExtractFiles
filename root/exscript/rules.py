import uiScriptLocale

TITLE_HEIGHT = 80
CONTENT_HEIGHT = 600

LISTBOX_SPACE = 8

WINDOW_WIDTH = 500
WINDOW_HEIGTH = TITLE_HEIGHT + CONTENT_HEIGHT

WINDOW_WIDTH2 = 510
WINDOW_HEIGTH2 = TITLE_HEIGHT + CONTENT_HEIGHT
window = {
	"name" : "RulesWindow",
	# "style" : ("movable", "float",),

	"x" : (SCREEN_WIDTH / 2) - (WINDOW_WIDTH / 2),
	"y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

	"width" : WINDOW_WIDTH2+30,
	"height" : WINDOW_HEIGTH2+50+30,

	"children" :
	(	
	
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,
			
			"hide_close_button" : 1,

			"width" : WINDOW_WIDTH2+30+15,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH2+30,
			"height" : WINDOW_HEIGTH2+30,
			
			"children" : (
				{
					"name" : "background",
					"type" : "bar",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH,
					"height" : WINDOW_HEIGTH,			
				},
				{
					"name" : "headerImage",
					"type" : "image",

					"x" : 20,
					"y" : 10,

					"image" : "images_rules/header.tga",
				},
				{
					"name" : "headerBoard",
					"type" : "thinboard",

					"x" : 20,
					"y" : 10,

					"width" : WINDOW_WIDTH,
					"height" : TITLE_HEIGHT,
				},
				{
					"name" : "titleImage",
					"type" : "image",

					"x" : 20,
					"y" : 10,

					"image" : "images_rules/title_de.tga",
				},
				{
					"name" : "contentBoard",
					"type" : "thinboard",

					"x" : 20,
					"y" : TITLE_HEIGHT + 10,

					"width" : WINDOW_WIDTH,
					"height" : CONTENT_HEIGHT,
					
					"children" : (
						{
							"name" : "rulesListBox",
							"type" : "ruleslistbox",
							
							"x" : LISTBOX_SPACE,
							"y" : 0,
							
							"width" : WINDOW_WIDTH - LISTBOX_SPACE,
							"height" : CONTENT_HEIGHT,
						},
						{
							"name" : "scrollBar",
							"type" : "small_thin_scrollbar",
							
							"x" : WINDOW_WIDTH - 15,
							"y" : 0,
							
							"size" : CONTENT_HEIGHT,
						},
						{
							"name" : "acceptButton",
							"type" : "button",
							
							"x" : (WINDOW_WIDTH/2) - 165,
							"y" : CONTENT_HEIGHT - 40,
							
							"text" : "Aktzeptieren",
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",							
						},
						{
							"name" : "declineButton",
							"type" : "button",
							
							"x" : (WINDOW_WIDTH/2) + 5,
							"y" : CONTENT_HEIGHT - 40,
							
							"text" : "Ablehnen",
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",							
						},					
					),
				},
			),
		},	
	
	
	
	
	
	
	
	
	
	
	
	),
}

