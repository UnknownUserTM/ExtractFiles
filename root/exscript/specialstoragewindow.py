import uiScriptLocale
import app

# window = {
	# "name" : "SpecialStorageWindow",

	# "x" : SCREEN_WIDTH - 400,
	# "y" : 10,

	# "style" : ("movable", "float",),

	# "width" : 184,
	# "height" : 328+32+30,

	# "children" :
	# (
		# {
			# "name" : "board",
			# "type" : "board",
			# "style" : ("attach",),

			# "x" : 0,
			# "y" : 0,

			# "width" : 184,
			# "height" : 328+32+30,
WINDOW_WIDTH = 167
WINDOW_HEIGTH = 328+32+30-30


window = {
	"name" : "SpecialStorageWindow",
	"style" : ("movable", "float",),

	# "x" : 24,
	# "y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,
	
	"x" : SCREEN_WIDTH - 226 + 5 - 22 - 30 - WINDOW_WIDTH,
	"y" : SCREEN_HEIGHT - 715 +	20 - 15,
	
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
				# ## Title
				# {
					# "name" : "TitleBar",
					# "type" : "titlebar",
					# "style" : ("attach",),

					# "x" : 8,
					# "y" : 8,

					# "width" : 169,
					# "color" : "gray",

					# "children" :
					# (
						# { "name":"TitleName", "type":"text", "x":84, "y":4, "text":"NoName", "text_horizontal_align":"center" },
					# ),
				# },
				{
					"name" : "titleBackground",
					"type" : "thinboard_circle",
					
					"x" : 18,
					"y" : 8,
					
					"width" : 160,
					"height" : 22,
					
					"children" : (
						{
												
							"name" : "titleTextLine",
							"type" : "text",
													
							"x" : 160 / 2,
							"y" : 4,
																						
							"text" : "UppItem-Lager",
							"text_horizontal_align" : "center",
							"outline" : 1,
						},							
					),
				},
				{
					"name" : "slotBackground",
					"type" : "thinboard_circle",
					
					"x" : 18,
					"y" : 8 + 22,
					
					"width" : 160,
					"height" : 288,
					
					"children" : (
						
						{ "name":"slot_bg_line_0_slot_0", "type":"thinboard_circle", "x":0, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_1", "type":"thinboard_circle", "x":32, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_2", "type":"thinboard_circle", "x":64, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_3", "type":"thinboard_circle", "x":96, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_4", "type":"thinboard_circle", "x":128, "y":0, "width":32, "height":32, },
						
						{ "name":"slot_bg_line_1_slot_0", "type":"thinboard_circle", "x":0, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_1", "type":"thinboard_circle", "x":32, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_2", "type":"thinboard_circle", "x":64, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_3", "type":"thinboard_circle", "x":96, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_4", "type":"thinboard_circle", "x":128, "y":32, "width":32, "height":32, },

						{ "name":"slot_bg_line_2_slot_0", "type":"thinboard_circle", "x":0, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_1", "type":"thinboard_circle", "x":32, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_2", "type":"thinboard_circle", "x":64, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_3", "type":"thinboard_circle", "x":96, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_4", "type":"thinboard_circle", "x":128, "y":64, "width":32, "height":32, },						
						
						{ "name":"slot_bg_line_3_slot_0", "type":"thinboard_circle", "x":0, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_1", "type":"thinboard_circle", "x":32, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_2", "type":"thinboard_circle", "x":64, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_3", "type":"thinboard_circle", "x":96, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_4", "type":"thinboard_circle", "x":128, "y":96, "width":32, "height":32, },

						{ "name":"slot_bg_line_4_slot_0", "type":"thinboard_circle", "x":0, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_1", "type":"thinboard_circle", "x":32, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_2", "type":"thinboard_circle", "x":64, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_3", "type":"thinboard_circle", "x":96, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_4", "type":"thinboard_circle", "x":128, "y":128, "width":32, "height":32, },

						{ "name":"slot_bg_line_5_slot_0", "type":"thinboard_circle", "x":0, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_1", "type":"thinboard_circle", "x":32, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_2", "type":"thinboard_circle", "x":64, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_3", "type":"thinboard_circle", "x":96, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_4", "type":"thinboard_circle", "x":128, "y":160, "width":32, "height":32, },

						{ "name":"slot_bg_line_6_slot_0", "type":"thinboard_circle", "x":0, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_1", "type":"thinboard_circle", "x":32, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_2", "type":"thinboard_circle", "x":64, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_3", "type":"thinboard_circle", "x":96, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_4", "type":"thinboard_circle", "x":128, "y":192, "width":32, "height":32, },

						{ "name":"slot_bg_line_7_slot_0", "type":"thinboard_circle", "x":0, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_1", "type":"thinboard_circle", "x":32, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_2", "type":"thinboard_circle", "x":64, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_3", "type":"thinboard_circle", "x":96, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_4", "type":"thinboard_circle", "x":128, "y":224, "width":32, "height":32, },
						
						{ "name":"slot_bg_line_8_slot_0", "type":"thinboard_circle", "x":0, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_1", "type":"thinboard_circle", "x":32, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_2", "type":"thinboard_circle", "x":64, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_3", "type":"thinboard_circle", "x":96, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_4", "type":"thinboard_circle", "x":128, "y":256, "width":32, "height":32, },						
						## Item Slot
						{
							"name" : "ItemSlot",
							"type" : "grid_table",

							"x" : 0,
							"y" : 0,

							"start_index" : 0,
							"x_count" : 5,
							"y_count" : 9,
							"x_step" : 32,
							"y_step" : 32,

							# "image" : "d:/ymir work/ui/public/Slot_Base.sub",
						},					
					
					),
				},

				
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 19,
					"y" : 295+32 - 5,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_03.sub",

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 19 + 78,
					"y" : 295+32 - 5,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_03.sub",

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},
				
				{
					"name" : "Category_Tab_01",
					"type" : "radio_button",

					"x" : 19,
					"y" : 295+32+30 - 10,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Category_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "Upgrades",
						},
					),
				},
					
				{
					"name" : "Category_Tab_02",
					"type" : "radio_button",

					"x" : 19+52,
					"y" : 295+32+30 - 10,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Category_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "Books",
						},
					),
				},
				
				{
					"name" : "Category_Tab_03",
					"type" : "radio_button",

					"x" : 19+52+52,
					"y" : 295+32+30 - 10,

					"default_image" : "d:/ymir work/ui/game/windows/tab_button_middle_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_middle_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_middle_03.sub",

					"children" :
					(
						{
							"name" : "Category_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "Stones",
						},
					),
				},
			),
		},
	),
}