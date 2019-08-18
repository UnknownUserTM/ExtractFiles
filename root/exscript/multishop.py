import uiScriptLocale

WINDOW_WIDTH = 350 - 40 
WINDOW_HEIGTH = 250 + 20

window = {
	"name" : "MultiShopWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 550,
	"y" : 110,

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
					"name" : "shopTitleBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : 180 - 40,
					"height" : 18,
					
					"children" : (
					
						{
							"name" : "shopTitleTextLine",
							"type" : "text",
											
							"x" : 70,
							"y" : 2, 
											
							"text" : "Achievementshop:",
											
							"outline" : 1,
											
							"color" : 0xffd8a055,
							"text_horizontal_align" : "center",
						},
					
					
					
					),
				},
				{
					"name" : "shopCategoryBoard",
					"type" : "thinboard_circle",
					
					"x" : 200 - 40,
					"y" : 10,
					
					"width" : 160,
					"height" : 18,
					
					"children" : (
					
						{
							"name" : "shopCategoryTextLine",
							"type" : "text",
											
							"x" : 80,
							"y" : 2, 
											
							"text" : "Rüstungen:",
											
							"outline" : 1,
											
							"color" : 0xffd8a055,
							"text_horizontal_align" : "center",
						},
					
					
					
					),
					
				},
				{
					"name" : "navigationBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10 + 18,
					
					"width" : 180 - 40,
					"height" : WINDOW_HEIGTH + 5 - 20 + 1,
					
					"children" : (
						{
							"name" : "navigationListBox",
							"type" : "listbox",
							
							
							"x" : 1,
							"y" : 1,
							
							"width" : 178 - 40,
							"height" : WINDOW_HEIGTH + 5,
						
						},
						{
							"name" : "QuestListScrollBar",
							"type" : "small_thin_scrollbar",
											
							"x" : 180 - 15 - 40,
							"y" : 1,
											
							"size" : WINDOW_HEIGTH + 5,
						},

					),

				},
				{
					"name" : "slotBackground",
					"type" : "thinboard_circle",
					
					"x" : 200 - 40,
					"y" : 10 + 18,
					
					"width" : 160,
					"height" : WINDOW_HEIGTH + 5 - 20,
					
					"children" : (
						
						{ "name":"slot_bg_line_0_slot_0", "type":"thinboard_circle", "x":0, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_1", "type":"thinboard_circle", "x":32, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_2", "type":"thinboard_circle", "x":64, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_3", "type":"thinboard_circle", "x":96, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_4", "type":"thinboard_circle", "x":128, "y":0, "width":32, "height":32, },
						# { "name":"slot_bg_line_0_slot_5", "type":"thinboard_circle", "x":160, "y":0, "width":32, "height":32, },
						# { "name":"slot_bg_line_0_slot_6", "type":"thinboard_circle", "x":192, "y":0, "width":32, "height":32, },
						# { "name":"slot_bg_line_0_slot_7", "type":"thinboard_circle", "x":224, "y":0, "width":32, "height":32, },
						# { "name":"slot_bg_line_0_slot_8", "type":"thinboard_circle", "x":256, "y":0, "width":32, "height":32, },
					
						{ "name":"slot_bg_line_1_slot_0", "type":"thinboard_circle", "x":0, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_1", "type":"thinboard_circle", "x":32, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_2", "type":"thinboard_circle", "x":64, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_3", "type":"thinboard_circle", "x":96, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_4", "type":"thinboard_circle", "x":128, "y":32, "width":32, "height":32, },
						# { "name":"slot_bg_line_1_slot_5", "type":"thinboard_circle", "x":160, "y":32, "width":32, "height":32, },
						# { "name":"slot_bg_line_1_slot_6", "type":"thinboard_circle", "x":192, "y":32, "width":32, "height":32, },
						# { "name":"slot_bg_line_1_slot_7", "type":"thinboard_circle", "x":224, "y":32, "width":32, "height":32, },
						# { "name":"slot_bg_line_1_slot_8", "type":"thinboard_circle", "x":256, "y":32, "width":32, "height":32, },
					
						{ "name":"slot_bg_line_2_slot_0", "type":"thinboard_circle", "x":0, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_1", "type":"thinboard_circle", "x":32, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_2", "type":"thinboard_circle", "x":64, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_3", "type":"thinboard_circle", "x":96, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_4", "type":"thinboard_circle", "x":128, "y":64, "width":32, "height":32, },
						# { "name":"slot_bg_line_2_slot_5", "type":"thinboard_circle", "x":160, "y":64, "width":32, "height":32, },
						# { "name":"slot_bg_line_2_slot_6", "type":"thinboard_circle", "x":192, "y":64, "width":32, "height":32, },
						# { "name":"slot_bg_line_2_slot_7", "type":"thinboard_circle", "x":224, "y":64, "width":32, "height":32, },
						# { "name":"slot_bg_line_2_slot_8", "type":"thinboard_circle", "x":256, "y":64, "width":32, "height":32, },
					
						{ "name":"slot_bg_line_3_slot_0", "type":"thinboard_circle", "x":0, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_1", "type":"thinboard_circle", "x":32, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_2", "type":"thinboard_circle", "x":64, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_3", "type":"thinboard_circle", "x":96, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_4", "type":"thinboard_circle", "x":128, "y":96, "width":32, "height":32, },
						# { "name":"slot_bg_line_3_slot_5", "type":"thinboard_circle", "x":160, "y":96, "width":32, "height":32, },
						# { "name":"slot_bg_line_3_slot_6", "type":"thinboard_circle", "x":192, "y":96, "width":32, "height":32, },
						# { "name":"slot_bg_line_3_slot_7", "type":"thinboard_circle", "x":224, "y":96, "width":32, "height":32, },
						# { "name":"slot_bg_line_3_slot_8", "type":"thinboard_circle", "x":256, "y":96, "width":32, "height":32, },
					
						{ "name":"slot_bg_line_4_slot_0", "type":"thinboard_circle", "x":0, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_1", "type":"thinboard_circle", "x":32, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_2", "type":"thinboard_circle", "x":64, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_3", "type":"thinboard_circle", "x":96, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_4", "type":"thinboard_circle", "x":128, "y":128, "width":32, "height":32, },
						# { "name":"slot_bg_line_4_slot_5", "type":"thinboard_circle", "x":160, "y":128, "width":32, "height":32, },
						# { "name":"slot_bg_line_4_slot_6", "type":"thinboard_circle", "x":192, "y":128, "width":32, "height":32, },
						# { "name":"slot_bg_line_4_slot_7", "type":"thinboard_circle", "x":224, "y":128, "width":32, "height":32, },
						# { "name":"slot_bg_line_4_slot_8", "type":"thinboard_circle", "x":256, "y":128, "width":32, "height":32, },
					
						{ "name":"slot_bg_line_5_slot_0", "type":"thinboard_circle", "x":0, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_1", "type":"thinboard_circle", "x":32, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_2", "type":"thinboard_circle", "x":64, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_3", "type":"thinboard_circle", "x":96, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_4", "type":"thinboard_circle", "x":128, "y":160, "width":32, "height":32, },
						# { "name":"slot_bg_line_5_slot_5", "type":"thinboard_circle", "x":160, "y":160, "width":32, "height":32, },
						# { "name":"slot_bg_line_5_slot_6", "type":"thinboard_circle", "x":192, "y":160, "width":32, "height":32, },
						# { "name":"slot_bg_line_5_slot_7", "type":"thinboard_circle", "x":224, "y":160, "width":32, "height":32, },
						# { "name":"slot_bg_line_5_slot_8", "type":"thinboard_circle", "x":256, "y":160, "width":32, "height":32, },
					
						{ "name":"slot_bg_line_6_slot_0", "type":"thinboard_circle", "x":0, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_1", "type":"thinboard_circle", "x":32, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_2", "type":"thinboard_circle", "x":64, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_3", "type":"thinboard_circle", "x":96, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_4", "type":"thinboard_circle", "x":128, "y":192, "width":32, "height":32, },
						# { "name":"slot_bg_line_6_slot_5", "type":"thinboard_circle", "x":160, "y":192, "width":32, "height":32, },
						# { "name":"slot_bg_line_6_slot_6", "type":"thinboard_circle", "x":192, "y":192, "width":32, "height":32, },
						# { "name":"slot_bg_line_6_slot_7", "type":"thinboard_circle", "x":224, "y":192, "width":32, "height":32, },
						# { "name":"slot_bg_line_6_slot_8", "type":"thinboard_circle", "x":256, "y":192, "width":32, "height":32, },
					
						{ "name":"slot_bg_line_7_slot_0", "type":"thinboard_circle", "x":0, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_1", "type":"thinboard_circle", "x":32, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_2", "type":"thinboard_circle", "x":64, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_3", "type":"thinboard_circle", "x":96, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_4", "type":"thinboard_circle", "x":128, "y":224, "width":32, "height":32, },
						# { "name":"slot_bg_line_7_slot_5", "type":"thinboard_circle", "x":160, "y":224, "width":32, "height":32, },
						# { "name":"slot_bg_line_7_slot_6", "type":"thinboard_circle", "x":192, "y":224, "width":32, "height":32, },
						# { "name":"slot_bg_line_7_slot_7", "type":"thinboard_circle", "x":224, "y":224, "width":32, "height":32, },
						# { "name":"slot_bg_line_7_slot_8", "type":"thinboard_circle", "x":256, "y":224, "width":32, "height":32, },
					
						# { "name":"slot_bg_line_8_slot_0", "type":"thinboard_circle", "x":0, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_1", "type":"thinboard_circle", "x":32, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_2", "type":"thinboard_circle", "x":64, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_3", "type":"thinboard_circle", "x":96, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_4", "type":"thinboard_circle", "x":128, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_5", "type":"thinboard_circle", "x":160, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_6", "type":"thinboard_circle", "x":192, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_7", "type":"thinboard_circle", "x":224, "y":256, "width":32, "height":32, },
						# { "name":"slot_bg_line_8_slot_8", "type":"thinboard_circle", "x":256, "y":256, "width":32, "height":32, },
					
						# { "name":"slot_bg_line_9_slot_0", "type":"thinboard_circle", "x":0, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_1", "type":"thinboard_circle", "x":32, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_2", "type":"thinboard_circle", "x":64, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_3", "type":"thinboard_circle", "x":96, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_4", "type":"thinboard_circle", "x":128, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_5", "type":"thinboard_circle", "x":160, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_6", "type":"thinboard_circle", "x":192, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_7", "type":"thinboard_circle", "x":224, "y":288, "width":32, "height":32, },
						# { "name":"slot_bg_line_9_slot_8", "type":"thinboard_circle", "x":256, "y":288, "width":32, "height":32, },
					
						# { "name":"slot_bg_line_10_slot_0", "type":"thinboard_circle", "x":0, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_1", "type":"thinboard_circle", "x":32, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_2", "type":"thinboard_circle", "x":64, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_3", "type":"thinboard_circle", "x":96, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_4", "type":"thinboard_circle", "x":128, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_5", "type":"thinboard_circle", "x":160, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_6", "type":"thinboard_circle", "x":192, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_7", "type":"thinboard_circle", "x":224, "y":320, "width":32, "height":32, },
						# { "name":"slot_bg_line_10_slot_8", "type":"thinboard_circle", "x":256, "y":320, "width":32, "height":32, },
					
						{
							"name" : "itemSlot",
							"type" : "grid_table",
		 
							"x" : 0,
							"y" : 0,
		 
							"start_index" : 0,
							"x_count" : 5,
							"y_count" : 8,
							"x_step" : 32,
							"y_step" : 32,
		 
							# "image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},					
					
					),
				},
			),
		},
	),
}

