import uiScriptLocale

ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = uiScriptLocale.EMPIRE_PATH
JEX_RESOURCE_IMGS = "locale/de/ui/re/"

ATALS_X = SCREEN_WIDTH * (282) / 800
ATALS_Y = SCREEN_HEIGHT * (170) / 600

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
			"x_scale" : float(SCREEN_WIDTH) / 1280.0, "y_scale" : float(SCREEN_HEIGHT) / 720.0,
			"image" : "locale/de/ui/re/bg.tga",
		},

		## Alpha
		{
			"name" : "Alpha",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/intro/select/background_alpha.sub",

			"x_scale" : float(SCREEN_WIDTH) / 100.0,
			"y_scale" : float(SCREEN_HEIGHT) / 69.0,
		},

		## Top & Bottom Line
		{
			"name" : "Top_Line",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/ui/intro/pattern/line_pattern.tga",

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 50) / 50.0, 0.0),
		},
		{
			"name" : "Bottom_Line",
			"type" : "expanded_image",

			"x" : 0,
			"y" : SCREEN_HEIGHT - 42,

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 50) / 50.0, 0.0),
		},

		## Title
		{
			"name" : "Title",
			"type" : "expanded_image",

			"x" : SCREEN_WIDTH * (410 - 346/2) / 800,
			"y" : SCREEN_HEIGHT * (114 - 136/2) / 600,
			"x_scale" : float(SCREEN_WIDTH) / 800.0,
			"y_scale" : float(SCREEN_HEIGHT) / 600.0,
		},
		
		## Buttons
		{
			"name" : "select_button",
			"type" : "button",

			"x" : 10,
			"y" : 295,
			"horizontal_align" : "center",
			"vertical_align" : "center",

			"default_image" : JEX_RESOURCE_IMGS + "select.tga",
			"over_image" : JEX_RESOURCE_IMGS + "select1.tga",
			"down_image" : JEX_RESOURCE_IMGS + "select2.tga",
		},
		{
			"name" : "exit_button",
			"type" : "button",

			"x" : 10,
			"y" : 220,
			"horizontal_align" : "center",
			"vertical_align" : "center",

			"default_image" : JEX_RESOURCE_IMGS + "close.tga",
			"over_image" : JEX_RESOURCE_IMGS + "close1.tga",
			"down_image" : JEX_RESOURCE_IMGS + "close2.tga",
		},

		## Atlas +reinos
		{
			"name" : "Atlas",
			"type" : "image",

			"x" : 8,
			"y" : -20,
			"horizontal_align" : "center",
			"vertical_align" : "center",

			"image" : JEX_RESOURCE_IMGS + "atlas.tga",

			"children" :
			(
				## Empire Image
				{
					"name" : "EmpireArea_A",
					"type" : "expanded_image",

					"x" : 563,
					"y" : 0,

					"image" : JEX_RESOURCE_IMGS + "shinsoo.tga",
				},
				{
					"name" : "EmpireArea_B",
					"type" : "expanded_image",

					"x" : 10,
					"y" : 0,

					"image" : JEX_RESOURCE_IMGS + "chunjo.tga",
				},
				{
					"name" : "EmpireArea_C",
					"type" : "expanded_image",

					"x" : 286,
					"y" : 0,

					"image" : JEX_RESOURCE_IMGS + "jinno.tga",
				},

				## Empire Flag
				{
					"name" : "EmpireAreaFlag_A",
					"type" : "expanded_image",

					"x" : 167,
					"y" : 235,

				},
				{
					"name" : "EmpireAreaFlag_B",
					"type" : "expanded_image",

					"x" : 70,
					"y" : 42,

				},
				{
					"name" : "EmpireAreaFlag_C",
					"type" : "expanded_image",

					"x" : 357,
					"y" : 78,

				},
			),
		},

		## Buttons
		{
			"name" : "left_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (450 - 22*3) / 1300,
			"y" : SCREEN_HEIGHT * (505) / 645,
		},
		{
			"name" : "right_button",
			"type" : "button",

			"x" : SCREEN_WIDTH * (580 - 22) / 920,
			"y" : SCREEN_HEIGHT * (505) / 645,
		},

		## Character Board
		{
			"name" : "empire_board",
			"type" : "image",

			"x" : SCREEN_WIDTH * (40) / 800,
			"y" : SCREEN_HEIGHT * (211) / 600,

			"width" : 208,
			"height" : 314,

			"children" :
			(
				## Bar
				{
					"name" : "flag_board",
					"type" : "bar",

					"x" : 24,
					"y" : 17,
					"width" : 159,
					"height" : 119,

					"children" :
					(
						## Empire Flag
						{
							"name" : "EmpireFlag_A",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,
							"horizontal_align" : "center",
							"vertical_align" : "center",

						},
						{
							"name" : "EmpireFlag_B",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,
							"horizontal_align" : "center",
							"vertical_align" : "center",

						},
						{
							"name" : "EmpireFlag_C",
							"type" : "expanded_image",

							"x" : 0,
							"y" : 0,
							"horizontal_align" : "center",
							"vertical_align" : "center",

						},
					),

				},
				{
					"name" : "text_board",
					"type" : "bar",

					"x" : 10,
					"y" : 146,

					"width" : 189,
					"height" : 122,

					"children" :
					(
						{
							"name" : "prev_text_button",
							"type" : "button",

							"x" : 95,
							"y" : 95,

							"text" : "",

							"default_image" : ROOT_PATH + "Small_Button_01.sub",
							"over_image" : ROOT_PATH + "Small_Button_02.sub",
							"down_image" : ROOT_PATH + "Small_Button_03.sub",
						},
						{
							"name" : "next_text_button",
							"type" : "button",

							"x" : 140,
							"y" : 95,

							"text" : "",

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
			),
		},
	),
}
