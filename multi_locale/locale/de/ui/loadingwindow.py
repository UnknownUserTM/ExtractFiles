import uiScriptLocale

window = {

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/intro/pattern/Line_Pattern.tga",

			"x_scale" : float(SCREEN_WIDTH) / 800.0,
			"y_scale" : float(SCREEN_HEIGHT) / 600.0,
		},
		{
			"name" : "BackGround_Shadow",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "yamato_load/art_mask_full.tga",

			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
		},
		{ 
			"name":"ErrorMessage", 
			"type":"text", "x":10, "y":10, 
			"text": uiScriptLocale.LOAD_ERROR, 
		},
		{
			"name" : "tipTextLine",
			"type" : "text",
			
			"x" : SCREEN_WIDTH / 2,
			"y" : 18,
			
			
			"text" : "Wusstest du schon das der Mönch dir die möglichkeit bietet Achievement-Points einzutauschen? Nein? Besuch ihn doch einfach mal.",
		
			"text_horizontal_align" : "center",
			
			"outline" : 1,
		
		},
		
		{
			"name" : "GageBoard",
			"type" : "window",
                        "style" : ("ltr",),
			"x" : float(SCREEN_WIDTH) * 400 / 800.0 - 475,
			"y" : float(SCREEN_HEIGHT) * 500 / 600.0 + 50,
			"width" : 400, 
			"height": 80,

			"children" :
			(
			
				{
					"name" : "BackGage",
					"type" : "expanded_image",

					"x" : 40,
					"y" : 25,

					"image" : "yamato_load/loading_bar_empty_frame.tga",
				},
				{
					"name" : "FullGage",
					"type" : "expanded_image",

					"x" : 75,
					"y" : 50,

					"image" : "yamato_load/loading_fill.tga",
				},
			),
		},
	),
}
