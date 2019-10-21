import uiScriptLocale

WINDOW_WIDTH = 256
WINDOW_HEIGTH = 331
Y_START = 15
IMAGE_PATH = "yamato_dungeon/"

window = {
	"name" : "DungeonIntroWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60,
	"y" : 110,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGTH,

	"children" :
	(				
		{
			"name" : "box",
			"type" : "image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"image" : IMAGE_PATH + "box.tga",

			"children" : (
			
				{
					"name" : "title_img",
					"type" : "image",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"image" : IMAGE_PATH + "map_title/sadrf.tga",	
				},
				{
					"name" : "seperator_title",
					"type" : "image",
					"style" : ("attach",),

					"x" : Y_START,
					"y" : 35,

					"image" : IMAGE_PATH + "separator.tga",	
				},	
				{
					"name" : "desc_box",
					"type" : "questlistbox",
					
					"x" : Y_START,
					"y" : 45,
					
					"width" : WINDOW_WIDTH - (Y_START * 2),
					"height" : 160,
				},
				{
					"name" : "scrollBar",
					"type" : "small_thin_scrollbar",
					
					"x" : WINDOW_WIDTH - 20,
					"y" : 45,
					
					"size" : 160,
				},	
				{
					"name" : "seperator_desc",
					"type" : "image",
					"style" : ("attach",),

					"x" : Y_START,
					"y" : WINDOW_HEIGTH - 35 - 12 - 55 - 10 - 12,

					"image" : IMAGE_PATH + "separator.tga",	
				},				
				{
				
					"name" : "difficulty_window",
					"type" : "window",
					
					"x" : (WINDOW_WIDTH / 2) - 27 - 15,
					"y" : WINDOW_HEIGTH - 35 - 12 - 55 - 10,

					"width" : 79,
					"height" : 74,
					
					"children" : (
						{
							"name" : "difficulty_bg",
							"type" : "image",
							"style" : ("attach",),

							"x" : 10,
							"y" : 0,

							"image" : IMAGE_PATH + "mask.tga",	
						},	
						{
							"name" : "difficulty_number",
							"type" : "image",
							"style" : ("attach",),

							"x" : 12,
							"y" : 5,

							"image" : IMAGE_PATH + "numbers/1.tga",	
						},	
						{
							"name" : "difficulty_glass",
							"type" : "image",
							"style" : ("attach",),

							"x" : 16,
							"y" : 9,

							"image" : IMAGE_PATH + "portrait_glass.tga",	
						},
						{
							"name" : "difficulty_frame",
							"type" : "image",
							"style" : ("attach",),

							"x" : 0,
							"y" : 0,

							"image" : IMAGE_PATH + "normal_frame.tga",	
						},						
					
					
					),
					
				},
				{
					"name" : "plus_button",
					"type" : "button",
							
					"x" : 50,
					"y" : WINDOW_HEIGTH - 35 - 12 - 55 - 10 + 15,

					"default_image" : IMAGE_PATH + "zin_n.tga",
					"over_image" : IMAGE_PATH + "zin_h.tga",
					"down_image" : IMAGE_PATH + "zin_p.tga",
					"disable_image" : IMAGE_PATH + "zin_d.tga",
				},		
				{
					"name" : "minus_button",
					"type" : "button",
							
					"x" : 50 + 79 + 40,
					"y" : WINDOW_HEIGTH - 35 - 12 - 55 - 10 + 15,
						
						
					"default_image" : IMAGE_PATH + "zout_n.tga",
					"over_image" : IMAGE_PATH + "zout_h.tga",
					"down_image" : IMAGE_PATH + "zout_p.tga",
					"disable_image" : IMAGE_PATH + "zout_d.tga",

				},					
				{
					"name" : "seperator_diff",
					"type" : "image",
					"style" : ("attach",),

					"x" : Y_START,
					"y" : WINDOW_HEIGTH - 35 - 12,

					"image" : IMAGE_PATH + "separator.tga",	
				},			
				{
					"name" : "entry_button",
					"type" : "button",
							
					"x" : 45,
					"y" : WINDOW_HEIGTH - 35,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Betreten",
				},			
			),
		},

	),
}

