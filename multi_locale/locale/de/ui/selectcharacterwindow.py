import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = uiScriptLocale.SELECT_PATH
JEX_RESOURCE_IMGS = "locale/de/ui/se/"

BOARD_X = SCREEN_WIDTH * (65) / 800
BOARD_Y = SCREEN_HEIGHT * (220) / 600

BOARD_ITEM_ADD_POSITION = -40

window = {
	"name" : "SelectCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround", "type" : "expanded_image", "x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
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
			"name" : "start_button",
			"type" : "button",

			"x" : 0 + 30,
			"y" : 365,
			"horizontal_align" : "center",
			"vertical_align" : "center",

			#"text" : "",
			#"text_height" : 6,

			"default_image" : JEX_RESOURCE_IMGS + "start.tga",
			"over_image" : JEX_RESOURCE_IMGS + "start1.tga",
			"down_image" : JEX_RESOURCE_IMGS + "start2.tga",
		},
		{
			"name" : "create_button",
			"type" : "button",

			"x" : 0 + 30,
			"y" : 365,
			"horizontal_align" : "center",
			"vertical_align" : "center",

			#"text" : uiScriptLocale.SELECT_CREATE,
			#"text_height" : 6,

			"default_image" : JEX_RESOURCE_IMGS + "create.tga",
			"over_image" : JEX_RESOURCE_IMGS + "create2.tga",
			"down_image" : JEX_RESOURCE_IMGS + "create1.tga",
		},

		## Character Board
		{
			"name" : "character_board",
			"type" : "image",

			"x" : -340,
			"y" : 0,
			"horizontal_align" : "center",
			"vertical_align" : "center",

			"image" : "yamato_select/ccbox_complete_merge.tga",

			"children" :
			(

				## Empire Flag
				{
					"name" : "EmpireFlag_A",
					"type" : "image",

					"x" : 85,
					"y" : 60,
					#"x_scale" : 0.9,
					#"y_scale" : 0.9,

					"image" : JEX_RESOURCE_IMGS + "chunjo.tga",
				},
				{
					"name" : "EmpireFlag_B",
					"type" : "image",

					"x" : 85,
					"y" : 60,
					#"x_scale" : 0.5,
					#"y_scale" : 0.5,

					"image" : JEX_RESOURCE_IMGS + "shinsoo.tga",
				},
				{
					"name" : "EmpireFlag_C",
					"type" : "image",

					"x" : 85,
					"y" : 60,
					#"x_scale" : 0.9,
					#"y_scale" : 0.9,

					"image" : JEX_RESOURCE_IMGS + "jinno.tga",
				},
				
				{
					"name" : "EmpireSplit",
					"type" : "image",

					"x" : 0,
					"y" : 60 + 70,
					#"x_scale" : 0.9,
					#"y_scale" : 0.9,

					"image" : "yamato_select/split.tga",
				},
				
				{
					"name" : "EmpireName_Title",
					"type" : "text",

					"x" : 40,
					"y" : 168,

					"text" : uiScriptLocale.SELECT_TITLE_EMPIRE,
					
					"outline" : 1,

				},
				{
					"name" : "Name_Title",
					"type" : "text",

					"x" : 40,
					"y" : 168 + 27,

					"text" : uiScriptLocale.SELECT_TITLE_NAME,
					
					"outline" : 1,

				},
				{
					"name" : "Level_Title",
					"type" : "text",

					"x" : 40,
					"y" : 168 + 29 + 26,

					"text" : uiScriptLocale.SELECT_TITLE_LEVEL,
					
					"outline" : 1,

				},
				{
					"name" : "Playtime_Title",
					"type" : "text",

					"x" : 40,
					"y" : 168 + 29 + 29 + 25,

					"text" : uiScriptLocale.SELECT_TITLE_PLAYTIME,
					
					"outline" : 1,

				},
				{
					"name" : "Guild_Title",
					"type" : "text",

					"x" : 40,
					"y" : 168 + 29 + 29 + 29 + 24,

					"text" : uiScriptLocale.SELECT_TITLE_GUILD,
					
					"outline" : 1,

				},
				

				{
					"name" : "EmpireNameSlot",
					"type" : "image",

					"x" : 162,
					"y" : 166,

					"image" : JEX_RESOURCE_IMGS + "etc.tga",

					"children" :
					(
						{
							"name" : "EmpireName",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"text" : uiScriptLocale.SELECT_EMPIRE_NAME,

							"all_align" : "center",
						},
					),
				},

				{
					"name" : "GuildNameSlot",
					"type" : "image",

					"x" : 162,
					"y" : 275,

					"image" : JEX_RESOURCE_IMGS + "etc.tga",

					"children" :
					(
						{
							"name" : "GuildName",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"text" : uiScriptLocale.SELECT_NO_GUILD,

							"all_align" : "center",
						},
					),
				},
				{
					"name" : "StatSplit",
					"type" : "image",

					"x" : 0,
					"y" : 302 - 10,
					#"x_scale" : 0.9,
					#"y_scale" : 0.9,

					"image" : "yamato_select/split.tga",
				},

				{
					"name" : "character_name",
					"type" : "text",

					"x" : 119,
					"y" : 195,

					"text" : "",

					"children" :
					(
						{
							"name" : "character_name_slot",
							"type" : "image",

							"x" : 43,
							"y" : -2,

							"image" : JEX_RESOURCE_IMGS + "etc.tga",
						},
						{
							"name" : "character_name_value",
							"type" : "text",

							"x" : 36 + 130/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_level",
					"type" : "text",

					"x" : 119,
					"y" : 222,

					"text" : "",

					"children" :
					(
						{
							"name" : "character_level_slot",
							"type" : "image",

							"x" : 43,
							"y" : -2,

							"image" : JEX_RESOURCE_IMGS + "etc.tga",
						},
						{
							"name" : "character_level_value",
							"type" : "text",

							"x" : 36 + 130/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "character_play_time",
					"type" : "text",

					"x" : 79,
					"y" : 249,

					"text" : "",

					"children" :
					(
						{
							"name" : "character_play_time_slot",
							"type" : "image",

							"x" : 83,
							"y" : -2,

							"image" : JEX_RESOURCE_IMGS + "etc.tga",
						},
						{
							"name" : "character_play_time_value",
							"type" : "text",

							"x" : 96 + 91/2,
							"y" : 0,

							"text" : "",

							"text_horizontal_align" : "center",
						},
					),
				},
				
				{
					"name" : "hth_Title",
					"type" : "text",

					"x" : 40 - 10,
					"y" : 330,

					"text" : "VIT",
					
					"outline" : 1,
				},
				{
					"name" : "int_Title",
					"type" : "text",

					"x" : 40 - 10,
					"y" : 330 + 26,

					"text" : "INT",
					
					"outline" : 1,
				},
				{
					"name" : "str_Title",
					"type" : "text",

					"x" : 40 - 10,
					"y" : 330 + 26 + 26,

					"text" : "STR",
					
					"outline" : 1,
				},
				{
					"name" : "dex_Title",
					"type" : "text",

					"x" : 40 - 10,
					"y" : 330 + 26 + 26 + 26,

					"text" : "DEX",
					
					"outline" : 1,
				},

				
				{
					"name" : "character_hth_gauge",
					"type" : "image",

					"x" : 60 - 10,
					"y" : 331,

					"image" : "yamato_select/empty_frame.tga",
					
					
					"children" : (
						{
							"name" : "character_hth_gauge_fill",
							"type" : "expanded_image",
							
							"x" : 2,
							"y" : 3,
							
							"image" : "yamato_select/red_fill.tga",
						
						
						
						},
						{
							"name" : "character_hth_gauge_deco",
							"type" : "image",
							
							"x" : -2,
							"y" : -2,
							
							"image" : "yamato_select/skills_segments.tga",
						},					
					
					),
				},
				{
					"name" : "character_int_gauge",
					"type" : "image",

					"x" : 60 - 10,
					"y" : 357,

					"image" : "yamato_select/empty_frame.tga",
					
					
					"children" : (
						{
							"name" : "character_int_gauge_fill",
							"type" : "expanded_image",
							
							"x" : 2,
							"y" : 3,
							
							"image" : "yamato_select/blue_fill.tga",
						
						
						
						},
						{
							"name" : "character_int_gauge_deco",
							"type" : "image",
							
							"x" : -2,
							"y" : -2,
							
							"image" : "yamato_select/skills_segments.tga",
						},					
					
					),
				},
				{
					"name" : "character_str_gauge",
					"type" : "image",

					"x" : 60 - 10,
					"y" : 383,

					"image" : "yamato_select/empty_frame.tga",
					
					
					"children" : (
						{
							"name" : "character_str_gauge_fill",
							"type" : "expanded_image",
							
							"x" : 2,
							"y" : 3,
							
							"image" : "yamato_select/purple_fill.tga",
						
						
						
						},
						{
							"name" : "character_str_gauge_deco",
							"type" : "image",
							
							"x" : -2,
							"y" : -2,
							
							"image" : "yamato_select/skills_segments.tga",
						},					
					
					),
				},
				{
					"name" : "character_dex_gauge",
					"type" : "image",

					"x" : 60 - 10,
					"y" : 330 + 26 + 26 + 26 + 1,

					"image" : "yamato_select/empty_frame.tga",
					
					
					"children" : (
						{
							"name" : "character_dex_gauge_fill",
							"type" : "expanded_image",
							
							"x" : 2,
							"y" : 3,
							
							"image" : "yamato_select/green_fill.tga",
						
						
						
						},
						{
							"name" : "character_dex_gauge_deco",
							"type" : "image",
							
							"x" : -2,
							"y" : -2,
							
							"image" : "yamato_select/skills_segments.tga",
						},					
					
					),
				},				
				# {
					# "name" : "character_hth",
					# "type" : "text",

					# "x" : 96,
					# "y" : 328 + 300,

					# "text" : "",

					# "children" :
					# (
						# {
							# "name" : "gauge_hth",
							# "type" : "gauge",

							# "x" : 16,
							# "y" : 4,

							# "width" : 100,
							# "color" : "red",
						# },
						# {
							# "name" : "character_hth_slot",
							# "type" : "image",

							# "x" : 134,
							# "y" : -2,

							# #"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						# },
						# {
							# "name" : "character_hth_value",
							# "type" : "text",

							# "x" : 134 + 39/2,
							# "y" : 0,

							# "text" : "",

							# "text_horizontal_align" : "center",
						# },
					# ),
				# },
				# {
					# "name" : "character_int",
					# "type" : "text",

					# "x" : 96,
					# "y" : 352 + 300,

					# "text" : "",

					# "children" :
					# (
						# {
							# "name" : "gauge_int",
							# "type" : "gauge",

							# "x" : 16,
							# "y" : 4,

							# "width" : 100,
							# "color" : "pink",
						# },
						# {
							# "name" : "character_int_slot",
							# "type" : "image",

							# "x" : 134,
							# "y" : -2,

							# #"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						# },
						# {
							# "name" : "character_int_value",
							# "type" : "text",

							# "x" : 134 + 39/2,
							# "y" : 0,

							# "text" : "",

							# "text_horizontal_align" : "center",
						# },
					# ),
				# },
				# {
					# "name" : "character_str",
					# "type" : "text",

					# "x" : 96,
					# "y" : 378 + 300,

					# "text" : "",

					# "children" :
					# (
						# {
							# "name" : "gauge_str",
							# "type" : "gauge",

							# "x" : 16,
							# "y" : 4,

							# "width" : 100,
							# "color" : "purple",
						# },
						# {
							# "name" : "character_str_slot",
							# "type" : "image",

							# "x" : 134,
							# "y" : -2,

							# #"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						# },
						# {
							# "name" : "character_str_value",
							# "type" : "text",

							# "x" : 134 + 39/2,
							# "y" : 0,

							# "text" : "",

							# "text_horizontal_align" : "center",
						# },
					# ),
				# },
				# {
					# "name" : "character_dex",
					# "type" : "text",

					# "x" : 96,
					# "y" : 406 + 300,

					# "text" : "",

					# "children" :
					# (
						# {
							# "name" : "gauge_dex",
							# "type" : "gauge",

							# "x" : 16,
							# "y" : 4,

							# "width" : 100,
							# "color" : "blue",
						# },
						# {
							# "name" : "character_dex_slot",
							# "type" : "image",

							# "x" : 134,
							# "y" : -2,

							# #"image" : "d:/ymir work/ui/public/Parameter_Slot_00.sub",
						# },
						# {
							# "name" : "character_dex_value",
							# "type" : "text",

							# "x" : 134 + 39/2,
							# "y" : 0,

							# "text" : "",

							# "text_horizontal_align" : "center",
						# },
					# ),
				# },

				## Buttons
				{
					"name" : "exit_button",
					"type" : "button",

					"x" : -65,
					"y" : 440,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.SELECT_EXIT,

					"default_image" : "yamato_helpboard/normal_button_n.tga", 
					"over_image" : "yamato_helpboard/normal_button_h.tga",
					"down_image" : "yamato_helpboard/normal_button_p.tga",
				},
				{
					"name" : "delete_button",
					"type" : "button",

					"x" : 65,
					"y" : 440,
					"horizontal_align" : "center",

					"text" : uiScriptLocale.SELECT_DELETE,

					"default_image" : "yamato_helpboard/normal_button_n.tga", 
					"over_image" : "yamato_helpboard/normal_button_h.tga",
					"down_image" : "yamato_helpboard/normal_button_p.tga",
					"disable_image" : "yamato_helpboard/normal_button_d.tga",
				},
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
