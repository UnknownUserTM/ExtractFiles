import uiScriptLocale

WINDOW_WIDTH = 370
WINDOW_HEIGTH = 530

window = {
	"name" : "RegenMaker",
	"style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30,

	"children" :
	(				
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : WINDOW_WIDTH+30+15,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			"children" : (
				{
					"name" : "file_config_bar",
					"type" : "bar",
					
					
					"x" : 25,
					"y" : 15,
					
					"width" : 350,
					"height" : 70,
					
					"children" : (
						{
							"name" : "fileNameTextLine",
							"type" : "text",
							"x" : "0",
							"y" : "8",
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Name of TextFile:",							
						},
						{
							"name" : "fileInputEditLineBoard",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 25,
							
							"width" : 320,
							"height" : 18,
							
							"children" : (
								{
									"name" : "fileNameEditLine",
									"type" : "editline",
									
									"x" : 4,
									"y" : 2,
									
									"input_limit" : 20,
									
									"width" : 320-8,
									"height" : 20,
								
								
								},
							
							),
						},
					
					
					
					),

				},
				
				{
					"name" : "vnum_bar",
					"type" : "bar",
					
					
					"x" : 25,
					"y" : 15 + 70 + 5,
					
					"width" : 350,
					"height" : 100,
					
					"children" : (
					
						{
							"name" : "vnumTextLine",
							"type" : "text",
							"x" : "0",
							"y" : "8",
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Vnum:",							
						},
						{
							"name" : "vnumInputEditLineBoard",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 25,
							
							"width" : 320,
							"height" : 18,
							
							"children" : (
								{
									"name" : "vnumEditLine",
									"type" : "editline",
									
									"x" : 4,
									"y" : 2,
									
									"input_limit" : 20,
									
									"width" : 320-8,
									"height" : 20,
								},
							),
						},
						{
							"name" : "m_button",
							"type" : "button",
									
							"x" : 25,
							"y" : 50,
								
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Single Mob / NPC",
								
						},
						{
							"name" : "g_button",
							"type" : "button",
									
							"x" : 25 + 100,
							"y" : 50,
								
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Group",
								
						},							
						{
							"name" : "r_button",
							"type" : "button",
									
							"x" : 25 + 100 + 100,
							"y" : 50,
								
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Random Group",
								
						},						
					),
				},
				{
					"name" : "rotation_bar",
					"type" : "bar",
					
					
					"x" : 25,
					"y" : 15 + 70 + 5 + 100 + 5,
					
					"width" : 350,
					"height" : 200,
					
					"children" : (
					
						{
							"name" : "rotationTextLine",
							"type" : "text",
							"x" : "0",
							"y" : "8",
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Rotation (Funktioniert nur bei m):",							
						},
						{
							"name" : "minimap_frame",
							"type" : "image",
							
							"x" : 0,
							"y" : 35,
							"horizontal_align" : "center", 
							"image" : "d:/ymir work/ui/minimap/minimap.sub",
						},
						
						{
							"name" : "rotation_button_0",
							"type" : "button",
									
							"x" : 0,
							"y" : 92,
							
							"tooltip_text" : "Random",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},	
						{
							"name" : "rotation_button_1",
							"type" : "button",
									
							"x" : 0,
							"y" : 92 + 70,
							
							"tooltip_text" : "South",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},
						{
							"name" : "rotation_button_5",
							"type" : "button",
									
							"x" : 0,
							"y" : 92 - 70 + 5,
							
							"tooltip_text" : "North",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},		
						
						{
							"name" : "rotation_button_3",
							"type" : "button",
									
							"x" : 0 + 70,
							"y" : 92,
							
							"tooltip_text" : "East",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},	
						{
							"name" : "rotation_button_7",
							"type" : "button",
									
							"x" : 0 - 70,
							"y" : 92,
							
							"tooltip_text" : "West",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},	
						
						{
							"name" : "rotation_button_4",
							"type" : "button",
									
							"x" : 0 + 50,
							"y" : 92 - 50,
							
							"tooltip_text" : "Northeast",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},	
						{
							"name" : "rotation_button_6",
							"type" : "button",
									
							"x" : 0 - 50,
							"y" : 92 - 50,
							
							"tooltip_text" : "Northwest",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},	

						{
							"name" : "rotation_button_2",
							"type" : "button",
									
							"x" : 0 + 50,
							"y" : 92 + 50,
							
							"tooltip_text" : "Southeast",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},	
						{
							"name" : "rotation_button_8",
							"type" : "button",
									
							"x" : 0 - 50,
							"y" : 92 + 50,
							
							"tooltip_text" : "Southwest",
							"horizontal_align" : "center", 
								
							"default_image" : "yamato_button/radio_n.tga",
							"over_image" : "yamato_button/radio_h.tga",
							"down_image" : "yamato_button/radio_n.tga",
							"disable_image" : "yamato_button/radio_p.tga",
						},

						
					),
				},
				{
					"name" : "random_bar",
					"type" : "bar",
					
					
					"x" : 25,
					"y" : 15 + 70 + 5 + 100 + 5 + 200 + 5,
					
					"width" : 350,
					"height" : 70 + 20,
					
					"children" : (
					
						{
							"name" : "randomTextLine",
							"type" : "text",
							"x" : "0",
							"y" : "8",
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Random Value:",							
						},

						{
							"name" : "randomInputEditLineBoard",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 25,
							
							"width" : 320,
							"height" : 18,
							
							"children" : (
								{
									"name" : "randomEditLine",
									"type" : "editline",
									
									"x" : 4,
									"y" : 2,
									
									"input_limit" : 20,
									
									"only_number" : 1,
									
									"text" : "0",
									
									"width" : 320-8,
									"height" : 20,
								},
							),
						},

						{
							"name" : "respawnTimeTextLine",
							"type" : "text",
							"x" : 0,
							"y" : 45,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Respawn Zeit:",							
						},
						{
							"name" : "randomInputEditLineBoard",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 45 + 17,
							
							"width" : 320,
							"height" : 18,
							
							"children" : (
								{
									"name" : "respawnTimeEditLine",
									"type" : "editline",
									
									"x" : 4,
									"y" : 2,
									
									"input_limit" : 20,
									
									"only_number" : 1,
									
									"text" : "0",
									
									"width" : 320-8,
									"height" : 20,
								},
							),
						},
						
					),
				},
				
				{
					"name" : "place_bar",
					"type" : "bar",
					
					
					"x" : 25,
					"y" : 15 + 70 + 5 + 100 + 5 + 200 + 5 + 70 + 5 + 20,
					
					"width" : 350,
					"height" : 45,
					
					"children" : (
						{
							"name" : "place_button",
							"type" : "button",
									
							"x" : 0,
							"y" : 10,
							
							
							
							"horizontal_align" : "center", 
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Place!",
								
						},					
					
					
					),
				},
			),
		},
	),
}

