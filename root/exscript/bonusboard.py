import uiScriptLocale

WINDOW_WIDTH = 600 + 40 + 20
WINDOW_HEIGTH = 410

window = {
	"name" : "BonusBoardWindow",
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
					"name" : "navigation_board",
					"type" : "board",
					"style" : ("attach",),
					
					"x" : 15,
					"y" : 15,
					
					"width" : 220,
					"height" : WINDOW_HEIGTH + 35,
					
					"no_bottom" : 1,
					
					"children" : (
					
						{
							"name" : "nav_button_0",
							"type" : "button",
							
							"x" : 30,
							"y" : 15,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Alle anzeigen",
						},
						{
							"name" : "nav_button_1",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 45,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "PVP",
						},
						{
							"name" : "nav_button_2",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 45 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "PVM",
						},					
						{
							"name" : "nav_button_3",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 45 + 30 + 45,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Offensiv",
						},
						{
							"name" : "nav_button_4",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 45 + 30 + 45 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Defensiv",
						},	
						{
							"name" : "nav_button_5",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 45 + 30 + 45 + 30 + 45,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Sonstige",
						},						
					),
				},
				{
					"name" : "bonusboard",
					"type" : "board",
					"style" : ("attach",),

					"x" : 220,
					"y" : 15,
					
					"no_bottom" : 1,
					
					"width" : 395 + 40 + 20,
					"height" : WINDOW_HEIGTH+35,
					
					"children" : (
					
						{
							"name" : "titleTextLine",
							"type" : "text",
							
							"x" : 25,
							"y" : 15,
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "|                  Name                   |  Mein Wert  |  Höchstmögl. Wert  |    Ausgerüstet   |",
						},		
						{
							"name" : "bonus_window_0",
							"type" : "window",
							
							"x" : 0,
							"y" : 35,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_0",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_0",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_0",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_0",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_0",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_0",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_0",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_0",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_1",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_1",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_1",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_1",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_1",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_1",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_1",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_1",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_1",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},					
						{
							"name" : "bonus_window_2",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_2",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_2",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_2",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_2",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_2",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_2",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_2",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_2",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},						
						{
							"name" : "bonus_window_3",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_3",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_3",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_3",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_3",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_3",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_3",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_3",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_3",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},	

						{
							"name" : "bonus_window_4",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_4",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_4",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_4",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_4",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_4",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_4",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_4",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_4",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},	

						{
							"name" : "bonus_window_5",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_5",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_5",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_5",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_5",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_5",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_5",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_5",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_5",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},	
						{
							"name" : "bonus_window_6",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_6",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_6",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_6",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_6",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_6",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_6",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_6",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_6",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_7",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_7",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_7",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_7",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_7",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_7",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_7",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_7",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_7",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_8",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_8",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_8",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_8",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_8",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_8",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_8",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_8",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_8",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_9",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_9",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_9",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_9",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_9",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_9",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_9",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_9",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_9",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_10",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_10",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_10",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_10",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_10",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_10",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_10",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_10",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_10",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},

						{
							"name" : "bonus_window_11",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_11",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_11",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_11",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_11",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_11",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_11",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_11",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_11",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},

						{
							"name" : "bonus_window_12",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_12",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_12",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_12",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_12",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_12",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_12",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_12",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_12",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_13",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_13",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_13",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_13",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_13",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_13",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_13",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_13",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_13",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_14",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_14",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_14",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_14",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_14",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_14",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_14",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_14",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_14",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},
						{
							"name" : "bonus_window_15",
							"type" : "window",
							
							"x" : 0,
							"y" : 35 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23 + 23,
							
							"width" : 395+40,
							"height" : 22,
							
							"children" : (
								{
									"name" : "bonus_name_slot_15",
									"type" : "thinboard_circle",
									
									"x" : 25,
									"y" : 0,
									
									"width" : 140,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_name_textline_15",
											"type" : "text",
											
											"x" : 5,
											"y" : 5,
											
											"text" : "Stark gegen Halbmenschen",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_value_slot_15",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140,
									"y" : 0,
									
									"width" : 65,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_value_textline_15",
											"type" : "text",
											
											"x" : 33,
											"y" : 5,
											
											"text" : "13.500",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								
								{
									"name" : "bonus_max_value_slot_15",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65,
									"y" : 0,
									
									"width" : 95,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_max_value_textline_15",
											"type" : "text",
											
											"x" : 48,
											"y" : 5,
											
											"text" : "24.100",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
								{
									"name" : "bonus_equip_slot_15",
									"type" : "thinboard_circle",
									
									"x" : 25 + 140 + 65 + 95,
									"y" : 0,
									
									"width" : 80,
									"height" : 22,
									
									"children" : (
										{
											"name" : "bonus_equip_textline_15",
											"type" : "text",
											
											"x" : 40,
											"y" : 5,
											
											"text" : "0 / 7",
											
											"text_horizontal_align" : "center",
											
											"outline" : 1,
										},
									),
								},
							),
						},



						{
							"name" : "bonusScrollBar",
							"type" : "scrollbar",
							
							"x" : 395 + 40 - 22,
							"y" : 35,
							
							"size" : WINDOW_HEIGTH - 40,
						
						
						},						
					),
				},			
			
			),
		},

	),
}

