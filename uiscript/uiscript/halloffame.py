import uiScriptLocale

WINDOW_WIDTH = 655
WINDOW_HEIGTH = 560
HALL_OF_FAME_PATH = "locale/de/ui/hall_of_fame/"

window = {
	"name" : "CalenderWindow",
	"style" : ("movable", "float",),

	"x" : 70,
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
			"children" :
			(
				{
					"name" : "board_category_menue",
					"type" : "board",
					"style" : ("movable", "attach",),
					"x" : 20,
					"y" : 35-20,
					"width" : 220,
					"height" : WINDOW_HEIGTH+34,
					
					# "image" : "yamato_halloffame/nav_bg.tga",
					"children" :
					(
						{
							"name" : "btn_category_menue_0",
							"type" : "button",
							"text" : "Bosse",
							"x" : 10+20,
							"y" : 15,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						{
							"name" : "btn_category_menue_1",
							"type" : "button",
							"text" : "Metins",
							"x" : 10+20,
							"y" : 15 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						{
							"name" : "btn_category_menue_2",
							"type" : "button",
							"text" : "Dungeons",
							"x" : 10+20,
							"y" : 15 + 30 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						{
							"name" : "btn_category_menue_3",
							"type" : "button",
							"text" : "Angeln",
							"x" : 10+20,
							"y" : 15 + 30 + 30 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						{
							"name" : "btn_category_menue_4",
							"type" : "button",
							"text" : "Duelle",
							"x" : 10+20,
							"y" : 15 + 30 + 30 + 30 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						{
							"name" : "btn_category_menue_5",
							"type" : "button",
							"text" : "Quests",
							"x" : 10+20,
							"y" : 15 + 30 + 30 + 30 + 30 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						
						{
							"name" : "btn_category_menue_6",
							"type" : "button",
							"text" : "Dailys",
							"x" : 10+20,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						{
							"name" : "btn_category_menue_7",
							"type" : "button",
							"text" : "Herausforderungen",
							"x" : 10+20,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
						{
							"name" : "btn_category_menue_8",
							"type" : "button",
							"text" : "Events",
							"x" : 10+20,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30 + 30 + 30,
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},

					),
				},
				{
					"name" : "thboard_header",
					"type" : "image",
					"style" : ("movable", "attach",),
					"x" : 220+10,
					"y" : 35-20,
					# "width" : "425",
					# "height" : "80",
					
					"image" : HALL_OF_FAME_PATH+"header.tga",
					
					"children" : (
						{
							"name" : "img_header",
							"type" : "image",
							"style" : ("attach",),
							
							"image" : "yamato_halloffame/image_frame.tga",
							"x" : 2,
							"y" : 2,
						},
					),
				},
				{
					"name" : "thboard_statistic",
					"type" : "image",
					"style" : ("movable", "attach",),
					"x" : 220+10,
					"y" : 120-20,
					# "width" : "425",
					# "height" : "410",
					
					"image" : "yamato_halloffame/hall_bg.tga",
					"children" : (
						{
							"name" : "statistic_row_head_0",
							"style" : ("float",),

							"x" : 15,
							"y" : 22,

							"width" : 20,
							"height" : 20,

							"children" :
							(
								{
									"name" : "lb_statistic_row_head_0",
									"type" : "text",
									"text" : "Platz:",
									"x" : 0,
									"y" : 0,
									
									"outline" : 1,

									"horizontal_align" : "center", 
									"text_horizontal_align":"center",
								},
							),
						},
						{
							"name" : "statistic_row_head_1",
							"style" : ("float",),

							"x" : 40,
							"y" : 22,

							"width" : 100,
							"height" : 20,

							"children" :
							(
								{
									"name" : "lb_statistic_row_head_1",
									"type" : "text",
									"text" : "Name:",
									"x" : 0,
									"y" : 0,
									
									"outline" : 1,

									"horizontal_align" : "center", 
									"text_horizontal_align":"center",
								},
							),
						},
						{
							"name" : "statistic_row_head_2",
							"style" : ("float",),

							"x" : 145,
							"y" : 22,

							"width" : 100,
							"height" : 20,

							"children" :
							(
								{
									"name" : "lb_statistic_row_head_2",
									"type" : "text",
									"text" : "Kills:",
									"x" : 0,
									"y" : 0,
									
									"outline" : 1,

									"horizontal_align" : "center", 
									"text_horizontal_align":"center",
								},
							),
						},
						{
							"name" : "statistic_row_head_3",
							"style" : ("float",),

							"x" : 250,
							"y" : 22,

							"width" : 40,
							"height" : 20,

							"children" :
							(
								{
									"name" : "lb_statistic_row_head_3",
									"type" : "text",
									"text" : "Level:",
									"x" : 0,
									"y" : 0,
									
									"outline" : 1,

									"horizontal_align" : "center", 
									"text_horizontal_align":"center",
								},
							),
						},
						{
							"name" : "statistic_row_head_4",
							"style" : ("float",),

							"x" : 295,
							"y" : 22,

							"width" : 100,
							"height" : 20,

							"children" :
							(
								{
									"name" : "lb_statistic_row_head_4",
									"type" : "text",
									"text" : "Reich:",
									"x" : 0,
									"y" : 0,
									"outline" : 1,
									"horizontal_align" : "center", 
									"text_horizontal_align":"center",
								},
							),
						},
						{
							"name" : "row_0",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*0,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_0_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_0_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_0_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_0_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_0_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_0_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_0_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_0_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_0_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_0_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_1",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*1,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_1_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_1_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_1_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_1_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_1_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_1_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_1_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_1_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_1_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_1_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_2",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*2,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_2_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_2_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_2_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_2_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_2_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_2_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_2_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_2_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_2_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_2_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_3",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*3,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_3_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_3_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_3_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_3_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_3_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_3_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_3_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_3_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_3_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_3_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_4",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*4,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_4_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_4_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_4_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_4_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_4_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_4_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_4_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_4_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_4_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_4_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						
						{
							"name" : "row_5",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*5,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_5_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_5_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_5_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_5_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_5_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_5_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_5_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_5_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_5_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_5_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_6",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*6,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_6_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_6_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_6_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_6_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_6_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_6_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_6_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_6_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_6_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_6_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_7",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*7,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_7_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_7_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_7_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_7_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_7_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_7_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_7_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_7_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_7_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_7_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_8",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*8,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_8_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_8_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_8_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_8_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_8_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_8_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_8_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_8_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_8_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_8_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_9",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*9,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_9_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_9_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_9_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_9_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_9_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_9_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_9_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_9_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_9_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_9_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_10",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*10,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_10_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_10_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_10_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_10_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_10_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_10_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_10_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_10_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_10_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_10_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_11",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*11,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_11_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_11_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_11_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_11_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_11_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_11_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_11_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_11_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_11_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_11_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_12",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*12,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_12_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_12_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_12_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_12_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_12_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_12_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_12_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_12_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_12_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_12_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						{
							"name" : "row_13",
							"style" : ("float",),

							"x" : 15,
							"y" : 40+25*13,

							"width" : 385,
							"height" : 20,

							"children" :
							(
								{
									"name" : "sb_statistic_row_13_column_0",
									"type" : "slotbar",
									"x" : 0,
									"y" : 0,
									
									"width" : 20,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_13_column_0",
											"type" : "text",
											"text" : "1.",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_13_column_1",
									"type" : "slotbar",
									"x" : 25,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_13_column_1",
											"type" : "text",
											"text" : "ProfEnte",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_13_column_2",
									"type" : "slotbar",
									"x" : 130,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_13_column_2",
											"type" : "text",
											"text" : "9000",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_13_column_3",
									"type" : "slotbar",
									"x" : 235,
									"y" : 0,
									
									"width" : 40,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_13_column_3",
											"type" : "text",
											"text" : "99",
											"x" : 2,
											"y" : 2,
										},
									),
								},
								{
									"name" : "sb_statistic_row_13_column_4",
									"type" : "slotbar",
									"x" : 280,
									"y" : 0,
									
									"width" : 100,
									"height" : 20,
									
									"children" :
									(
										{
											"name" : "lb_statistic_row_13_column_4",
											"type" : "text",
											"text" : "Shinsoo-Reich",
											"x" : 2,
											"y" : 2,
										},
									),
								},
							),
						},
						
						{
							"name" : "scrollbar_statistic",
							"type" : "scrollbar",

							"x" : 400,
							"y" : 38,

							"size" : 350,
						},
					),
				},
				{
					"name" : "thboard_subcategory_menue",
					"type" : "image",
					"style" : ("movable", "attach",),
					"x" : 220+10,
					"y" : 535-20,
					# "width" : "425",
					# "height" : "55",
					
					"image" : "yamato_halloffame/subnav_bg.tga",
					"children" :
					(
						{
							"name" : "lb_sub_category",
							"type" : "text",
							"text" : "sub_category",
							"x" : "0",
							"y" : "0",
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"vertical_align" : "center",
							"text_vertical_align" : "center",
							"color" : 0xffd8a055,
						},
						{
							"name" : "btn_sub_category_left",
							"type" : "button",
							"text" : "",
							"x" : 70,
							"y" : 12,
							"default_image" : "yamato_select/leftrotator_n.tga",
							"over_image" : "yamato_select/leftrotator_h.tga",
							"down_image" : "yamato_select/leftrotator_p.tga",
						},
						{
							"name" : "btn_sub_category_right",
							"type" : "button",
							"text" : "",
							"x" : 263 + 60,
							"y" : 12,
							"default_image" : "yamato_select/rightrotator_n.tga",
							"over_image" : "yamato_select/rightrotator_h.tga",
							"down_image" : "yamato_select/rightrotator_p.tga",
						},
					),
				},
			),
		},
	),
}
