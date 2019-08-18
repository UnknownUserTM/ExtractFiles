import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = "locale/de/ui/select/"
BOARD_X = SCREEN_WIDTH * (65) / 800
BOARD_Y = SCREEN_HEIGHT * (215) / 600
JEX_RESOURCE_IMGS = "locale/de/ui/cr/"

PLUS_BUTTON_WIDTH = 20
TEMPORARY_HEIGHT = 24 + 5

window = {
	"name" : "CreateCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : "yamato_select/bg.jpg",
		},
		## Name
		{
			"name" : "name_warrior",
			"type" : "image",

			"x" :(SCREEN_WIDTH / 2) + (220),
			"y" : BOARD_Y + 150,

			"image" : JEX_RESOURCE_IMGS+"g.tga",
		},
		{
			"name" : "name_assassin",
			"type" : "image",

			"x" :(SCREEN_WIDTH / 2) + (220),
			"y" : BOARD_Y + 150,

			"image" : JEX_RESOURCE_IMGS+"n.tga",
		},
		{
			"name" : "name_sura",
			"type" : "image",

			"x" :(SCREEN_WIDTH / 2) + (220),
			"y" : BOARD_Y + 150,

			"image" : JEX_RESOURCE_IMGS+"s.tga",
		},
		{
			"name" : "name_shaman",
			"type" : "image",

			"x" :(SCREEN_WIDTH / 2) + (220),
			"y" : BOARD_Y + 150,

			"image" : JEX_RESOURCE_IMGS+"c.tga",
		},
		{
			"name" : "name_wolfman",
			"type" : "image",

			"x" : BOARD_X + 780,
			"y" : BOARD_Y + 100,

			#"image" : JEX_RESOURCE_IMGS+"w.tga",
		},
		{
			"name" : "create_button",
			"type" : "button",

			"x" : 0,
			"y" : 365,
			"horizontal_align" : "center",
			"vertical_align" : "center",

			"text" : "",

			"default_image" : JEX_RESOURCE_IMGS+"create.tga",
			"over_image" : JEX_RESOURCE_IMGS+"create2.tga",
			"down_image" : JEX_RESOURCE_IMGS+"create1.tga",
		},
		
		## Character Board
		{
			"name" : "character_board",
			"type" : "image",

			"x" : -340,
			"y" : 0,
			"horizontal_align" : "center",
			"vertical_align" : "center",
			
			"image" : "yamato_create/ccbox_complete_merge.tga",

			"children" :
			(
				{
					"name" : "text_board",
					"type" : "bar",

					"x" : -999,
					"y" : -999,

					"width" : 189,
					"height" : 122,

					"children" :
					(
						{
							"name" : "prev_button",
							"type" : "button",

							"x" : 95,
							"y" : 95,

							"text" : uiScriptLocale.CREATE_PREV,

							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "next_button",
							"type" : "button",

							"x" : 140,
							"y" : 95,

							"text" : uiScriptLocale.CREATE_NEXT,

							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "right_line",
							"type" : "line",

							"x" : 189-1,
							"y" : -1,

							"width" : 0,
							"height" : 122,

							"color" : 0xffAAA6A1,
						},
						{
							"name" : "bottom_line",
							"type" : "line",

							"x" : 0,
							"y" : 122-1,

							"width" : 189,
							"height" : 0,

							"color" : 0xffAAA6A1,
						},
						{
							"name" : "left_line",
							"type" : "line",

							"x" : 0,
							"y" : 0,

							"width" : 0,
							"height" : 122-1,

							"color" : 0xff2A2521,
						},
						{
							"name" : "top_line",
							"type" : "line",

							"x" : 0,
							"y" : 0,

							"width" : 189,
							"height" : 0,

							"color" : 0xff2A2521,
						},
					),
				},
				{
					"name" : "hth",
					"type" : "text",

					"x" : -999,
					"y" : -999,

					"text" : uiScriptLocale.CREATE_HP,

					"children" :
					(
						{
							"name" : "hth_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "red",
						},
						{
							"name" : "hth_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "hth_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},
				{
					"name" : "int",
					"type" : "text",

					"x" : -999,
					"y" : -999,

					"text" : uiScriptLocale.CREATE_SP,

					"children" :
					(
						{
							"name" : "int_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "pink",
						},
						{
							"name" : "int_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "int_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},
				{
					"name" : "str",
					"type" : "text",

					"x" : -999,
					"y" : -999,

					"text" : uiScriptLocale.CREATE_ATT_GRADE,

					"children" :
					(
						{
							"name" : "str_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "purple",
						},
						{
							"name" : "str_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "str_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},
				{
					"name" : "dex",
					"type" : "text",

					"x" : -999,
					"y" : -999,

					"text" : uiScriptLocale.CREATE_DEX_GRADE,

					"children" :
					(
						{
							"name" : "dex_gauge",
							"type" : "gauge",

							"x" : 30,
							"y" : 4,

							"width" : 100 + PLUS_BUTTON_WIDTH,
							"color" : "blue",
						},
						{
							"name" : "dex_slot",
							"type" : "slotbar",

							"x" : 137 + PLUS_BUTTON_WIDTH,
							"y" : -1,
							"width" : 24,
							"height" : 16,

							"children" :
							(
								{
									"name" : "dex_value",
									"type" : "text",

									"x" : 0,
									"y" : 1,
									"all_align" : "center",

									"text" : "99",
								},
							),
						},
					),
				},

				{
					"name" : "hth_button",
					"type" : "button",

					"x" : 184,
					"y" : 139,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},
				{
					"name" : "int_button",
					"type" : "button",

					"x" : 184,
					"y" : 158,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},
				{
					"name" : "str_button",
					"type" : "button",

					"x" : 184,
					"y" : 177,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},
				{
					"name" : "dex_button",
					"type" : "button",

					"x" : 184,
					"y" : 196,

					"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
					"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
					"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
				},
				
				{
					"name" : "character_name_window",
					"type" : "image",
					
					"x" : 20 + 25 + 3,
					
					"y" : 180,
				
					"image" : "yamato_create/name_form.tga",	
				
					"children" : (
						{
							"name" : "character_name_value",
							"type" : "editline",

							"x" : 20,
							"y" : 38,

							"input_limit" : 12,

							"width" : 90,
							"height" : 20,
						},
					),
				},
				
				{
			
					"name" : "character_gender_option_holder",
					"type" : "image",
					
					"x" : 45 - 10 + 5,
					
					"y" : 280,
				
					"image" : "yamato_create/options_holder.tga",				
								
					
					"children" : (
						{
							"name" : "character_gender_option_holder",
							"type" : "image",
							
							"x" : 15,
							
							"y" : 15,
						
							"image" : "yamato_create/options_form.tga",				
					
							"children" : (
								{
								
									"name" : "character_gender",
									"type" : "text",

									"x" : 100,
									"y" : 8,

									"text" : "Männlich",

									"text_horizontal_align" : "center",								
								
								
								
								},
								{
									"name" : "gender_button_01",
									"type" : "radio_button",

									"x" : 3,
									"y" : 3,

									"text" : "",

									"default_image" : "yamato_create/left_n.tga",
									"over_image"	: "yamato_create/left_h.tga",
									"down_image"	: "yamato_create/left_p.tga",
								},
								{
									"name" : "gender_button_02",
									"type" : "radio_button",

									"x" : 201 - 26,
									"y" : 3,

									"text" : "",

									"default_image" : "yamato_create/right_n.tga",
									"over_image"	: "yamato_create/right_h.tga",
									"down_image"	: "yamato_create/right_p.tga",
								},									
							),
						},
					),
				},
				{
			
					"name" : "character_style_option_holder",
					"type" : "image",
					
					"x" : 45 - 10 + 5,
					
					"y" : 280  + 95,
				
					"image" : "yamato_create/options_holder.tga",				
								
					
					"children" : (
						{
							"name" : "character_style_option_holder",
							"type" : "image",
							
							"x" : 15,
							
							"y" : 15,
						
							"image" : "yamato_create/options_form.tga",				
					
							"children" : (
								{
								
									"name" : "character_style",
									"type" : "text",

									"x" : 100,
									"y" : 8,

									"text" : "Standart",

									"text_horizontal_align" : "center",								
								
								
								
								},
								{
									"name" : "shape_button_01",
									"type" : "radio_button",

									"x" : 3,
									"y" : 3,

									"text" : "",

									"default_image" : "yamato_create/left_n.tga",
									"over_image"	: "yamato_create/left_h.tga",
									"down_image"	: "yamato_create/left_p.tga",
								},
								{
									"name" : "shape_button_02",
									"type" : "radio_button",

									"x" : 201 - 26,
									"y" : 3,

									"text" : "",

									"default_image" : "yamato_create/right_n.tga",
									"over_image"	: "yamato_create/right_h.tga",
									"down_image"	: "yamato_create/right_p.tga",
								},									
							),
						},
					),
				},				
				{
					"name" : "character_gender_symbol_frame",
					"type" : "image",
					
					"x" : 45+ 10 + 40 + 10+ 3,
					
					"y" : 250,
					"image" : "yamato_create/symbol_frame_morf.tga",				
				
				},
				{
					"name" : "character_style_symbol_frame",
					"type" : "image",
					
					"x" : 45+ 10 + 40 + 10+ 3,
					
					"y" : 250 + 95,
					"image" : "yamato_create/symbol_frame_style.tga",				
				
				},
				{
					"name" : "character_name",
					"type" : "text",

					"x" : 103,
					"y" : 306,

					"text" : "",

					"text_horizontal_align" : "center",

					"children" :
					(
						{
							"name" : "character_name_slot",
							"type" : "image",

							"x" : 40 - 1,
							"y" : -2,

							#"image" : "d:/ymir work/ui/public/parameter_slot_04.sub",
						},
					),
				},

				# {
					# "name" : "character_gender",
					# "type" : "text",

					# "x" : 43,
					# "y" : 247,

					# "text" : "",

					# "text_horizontal_align" : "center",
				# },


				{
					"name" : "character_shape",
					"type" : "text",

					"x" : 43,
					"y" : 270,

					"text" : "",

					"text_horizontal_align" : "center",
				},
				# {
					# "name" : "shape_button_01",
					# "type" : "radio_button",

					# "x" : 250,
					# "y" : 363,

					# "text" : "",

					# "default_image" : "yamato_create/left_n.tga",
					# "over_image"	: "yamato_create/left_h.tga",
					# "down_image"	: "yamato_create/left_p.tga",
				# },
				# {
					# "name" : "shape_button_02",
					# "type" : "radio_button",

					# "x" : 270,
					# "y" : 363,

					# "text" : "",

					# "default_image" : "yamato_create/right_n.tga",
					# "over_image"	: "yamato_create/right_h.tga",
					# "down_image"	: "yamato_create/right_p.tga",
				# },
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 0,
					"y" : 460 - 30 + 10,
					"horizontal_align" : "center",

					"text" : "Zurück",

					"default_image" : "yamato_helpboard/normal_button_n.tga", 
					"over_image" : "yamato_helpboard/normal_button_h.tga",
					"down_image" : "yamato_helpboard/normal_button_p.tga",
				},
				##des raza
#				{
#					"name" : "name_warriordes",
#					"type" : "image",
#
#					"x" : 20,
#					"y" : 40,
#
#					"image" : JEX_RESOURCE_IMGS+"desw.tga",
#				},
#				{
#					"name" : "name_assassindes",
#					"type" : "image",
#
#					"x" : 20,
#					"y" : 40,
#
#					"image" : JEX_RESOURCE_IMGS+"desn.tga",
#				},
#				{
#					"name" : "name_surades",
#					"type" : "image",
#
#					"x" : 20,
#					"y" : 40,
#
#					"image" : JEX_RESOURCE_IMGS+"dess.tga",
#				},
#				{
#					"name" : "name_shamandes",
#					"type" : "image",
#
#					"x" : 20,
#					"y" : 40,
#
#					"image" : JEX_RESOURCE_IMGS+"desc.tga",
#				},
#				{
#					"name" : "name_wolfmandes",
#					"type" : "image",
#
#					"x" : BOARD_X - 65,
#					"y" : BOARD_Y + - 195,

					#"image" : JEX_RESOURCE_IMGS+"desl.tga",
#				},
				##end des raza
				##img raza
				{
					"name" : "name_warriorimg",
					"type" : "image",

					"x" : 40 -20,
					"y" : 70 - 25,

					"image" : JEX_RESOURCE_IMGS+"war.tga",
				},
				{
					"name" : "name_assassinimg",
					"type" : "image",

					"x" : 40 -20,
					"y" : 70 - 25,

					"image" : JEX_RESOURCE_IMGS+"ninja.tga",
				},
				{
					"name" : "name_suraimg",
					"type" : "image",

					"x" : 40 -20,
					"y" : 70 - 25,

					"image" : JEX_RESOURCE_IMGS+"sura.tga",
				},
				{
					"name" : "name_shamanimg",
					"type" : "image",

					"x" : 40 -20,
					"y" : 70 - 25,

					"image" : JEX_RESOURCE_IMGS+"shaman.tga",
				},
				{
					"name" : "name_wolfmanimg",
					"type" : "image",

					"x" : BOARD_X - 70,
					"y" : BOARD_Y + -115,

					#"image" : JEX_RESOURCE_IMGS+"shaman.tga",
				},
				##end img raza
			),
		},

		## Buttons
		{
			"name" : "left_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (450 - 22*3) / 950 + 100,
			"y" : SCREEN_HEIGHT * (505) / 700,

			"default_image" : "yamato_select/leftrotator_n.tga",
			"over_image" : "yamato_select/leftrotator_h.tga",
			"down_image" : "yamato_select/leftrotator_p.tga",
		},
		{
			"name" : "right_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (580 - 22) / 845,
			"y" : SCREEN_HEIGHT * (505) / 700,
			"default_image" : "yamato_select/rightrotator_n.tga",
			"over_image" : "yamato_select/rightrotator_h.tga",
			"down_image" : "yamato_select/rightrotator_p.tga",
		},


	),
}
