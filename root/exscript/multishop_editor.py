import uiScriptLocale

WINDOW_WIDTH = 350 - 40 + 150 
WINDOW_HEIGTH = 250 + 20 + 50

window = {
	"name" : "MultiShopWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60 - 230,
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
			"name" : "saveShopDialogButton",
			"type" : "button",
													
			"x" : 20,
			"y" : 20,
												
			"default_image" : "buttons/button_save_n.tga",
			"over_image" : "buttons/button_save_h.tga",
			"down_image" : "buttons/button_save_d.tga",
			"disable_image" : "buttons/button_save_d.tga",

			"text" : "",
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
											
							"text" : "ShopName",
											
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
					"name" : "itemMakerBoard",
					"type" : "thinboard_circle",
					
					"x" : 200 - 40 + 160,
					"y" : 10,
					
					"width" : 150,
					"height" : 18,
					
					"children" : (
					
						{
							"name" : "itemMakerTextLine",
							"type" : "text",
											
							"x" : 80,
							"y" : 2, 
											
							"text" : "Item erstellen:",
											
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
							"height" : WINDOW_HEIGTH + 5 - 70,
						
						},
						{
							"name" : "QuestListScrollBar",
							"type" : "small_thin_scrollbar",
											
							"x" : 180 - 15 - 40,
							"y" : 1,
											
							"size" : WINDOW_HEIGTH + 5 - 70,
						},
						{
							"name" : "makeNewCategory",
							"type" : "button",
													
							"x" : 25,
							"y" : WINDOW_HEIGTH - 50,
												
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "New Category",
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
						{
							"name" : "deleteItem",
							"type" : "toggle_button",
													
							"x" : 30,
							"y" : WINDOW_HEIGTH - 50,
												
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Delete",
						},						
					
					),
				},
				{
					"name" : "itemCreaterBG",
					"type" : "thinboard_circle",
					
					"x" : 200 - 40 + 160,
					"y" : 10 + 18,
					
					"width" : 150,
					"height" : WINDOW_HEIGTH + 5 - 20,
					
					
					"children" : (
						{
							"name" : "vnumTitleTextLine",
							"type" : "text",
							
							"x" : 5,
							"y" : 22,
							
							"text" : "ItemVnum:",
						
						
						},
						{
							"name" : "vnumInputBox",
							"type" : "thinboard_circle",
							
							"x" : 150 - 60 - 5,
							"y" : 20,
							
							"width" : 60,
							"height" : 20,
							
							
							"children" : (
								{
									"name" : "vnumInputEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									
									
													
									"width" : 60,
									"height" : 20,
								},
							),
						},
					
						{
							"name" : "countTitleTextLine",
							"type" : "text",
							
							"x" : 5,
							"y" : 22 + 25,
							
							"text" : "Count:",
						
						
						},
						{
							"name" : "countInputBox",
							"type" : "thinboard_circle",
							
							"x" : 150 - 60 - 5,
							"y" : 20 + 25,
							
							"width" : 60,
							"height" : 20,
							
							
							"children" : (
								{
									"name" : "countInputEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									
									"text" : "1",
													
									"width" : 60,
									"height" : 20,
								},
							),
						},

						{
							"name" : "currencySelectTitle",
							"type" : "text",
							"x" : 0,
							"y" : 20 + 25 + 25,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Currency:",							
						},
						{
							"name" : "selectCurrencyBox",
							"type" : "thinboard_circle",
							
							"x" : 5,
							"y" : 20 + 25 + 45,
							
							
							"width" : 140,
							"height" : 18*5,
							
							"children" : (
								{
									"name" : "currencyListBox",
									"type" : "listbox",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 140,
									"height" : 18*5,
								},
							),
						},
						
						{
							"name" : "currencyVnumTitleTextLine",
							"type" : "text",
							
							"x" : 5,
							"y" : 20 + 25 + 45 + 95 + 2,
							
							"text" : "CurrencyVnum:",
						
						
						},
						{
							"name" : "currencyVnumInputBox",
							"type" : "thinboard_circle",
							
							"x" : 150 - 60 - 5,
							"y" : 20 + 25 + 45 + 95,
							
							"width" : 60,
							"height" : 20,
							
							
							"children" : (
								{
									"name" : "currencyVnumInputEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									
									"text" : "0",
													
									"width" : 60,
									"height" : 20,
								},
							),
						},
						{
							"name" : "currencyCountTitleTextLine",
							"type" : "text",
							
							"x" : 5,
							"y" : 20 + 25 + 45 + 95 + 25 + 2,
							
							"text" : "CurrencyCount:",
						
						
						},
						{
							"name" : "currencyCountInputBox",
							"type" : "thinboard_circle",
							
							"x" : 150 - 60 - 5,
							"y" : 20 + 25 + 45 + 95 + 25,
							
							"width" : 60,
							"height" : 20,
							
							
							"children" : (
								{
									"name" : "currencyCountInputEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									"text" : "1",				
									"width" : 60,
									"height" : 20,
								},
							),
						},

						{
							"name" : "attachVirtualItemButton",
							"type" : "button",
													
							"x" : 30,
							"y" : 20 + 25 + 45 + 95 + 25 + 60,
												
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Attach V-Item",
						},						
						
					),
				},
				
				{
					"name" : "newCategoryNameBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : WINDOW_HEIGTH + 5,
					
					"children" : (

						{
							"name" : "newCategoryTitleTextLine",
							"type" : "text",
							"x" : 0,
							"y" : 150 - 20 - 20,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							# "vertical_align" : "center",
							# "text_vertical_align" : "center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "stringIndex: ",
						},
						
						{
							"name" : "newCategoryBackgroundInput",
							"type" : "thinboard_circle",
							
							"x" : 0,
							"y" : 150 - 20,

							# "vertical_align" : "center",
							"horizontal_align" : "center",							

							"width" : 150,
							"height" : 19,
							
							"children" : (
								{
									"name" : "newCategoryBackgroundInputEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									"text" : "",
													
									"width" : 150,
									"height" : 20,
								},
							),
						},
						{
							"name" : "addCategoryButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 25 - 25 + 5 - 30 + 15 + 15,
									
							"text" : "Hinzufügen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},	
					
						{
							"name" : "closeCategoryNameBoard",
							"type" : "button",
									
							"x" : 0,
							"y" : 25 - 25 + 5 + 15 + 15,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},					
					
					
					),
				},
				
				{
					"name" : "saveShopBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : WINDOW_HEIGTH + 5,
					
					"children" : (
						{
							"name" : "saveShopIndexTitle",
							"type" : "text",
							"x" : 0,
							"y" : 150 - 20 - 20 - 50,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							# "vertical_align" : "center",
							# "text_vertical_align" : "center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "ShopIndex: ",
						},
						
						{
							"name" : "saveShopIndexBackgroundInput",
							"type" : "thinboard_circle",
							
							"x" : 0,
							"y" : 150 - 20 - 50,

							# "vertical_align" : "center",
							"horizontal_align" : "center",							

							"width" : 150,
							"height" : 19,
							
							"children" : (
								{
									"name" : "saveShopIndexBackgroundInputEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									"text" : "",
													
									"width" : 150,
									"height" : 20,
								},
							),
						},
						{
							"name" : "saveShopTitle",
							"type" : "text",
							"x" : 0,
							"y" : 150 - 20 - 20,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							# "vertical_align" : "center",
							# "text_vertical_align" : "center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "ShopTitle Number: ",
						},
						
						{
							"name" : "saveShopBackgroundInput",
							"type" : "thinboard_circle",
							
							"x" : 0,
							"y" : 150 - 20,

							# "vertical_align" : "center",
							"horizontal_align" : "center",							

							"width" : 150,
							"height" : 19,
							
							"children" : (
								{
									"name" : "saveShopBackgroundInputEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									"text" : "",
													
									"width" : 150,
									"height" : 20,
								},
							),
						},
						{
							"name" : "saveShop",
							"type" : "button",
									
							"x" : 0,
							"y" : 25 - 25 + 5 - 30 + 15 + 15,
									
							"text" : "Speichern",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},	
					
						{
							"name" : "closeShopSaveDialog",
							"type" : "button",
									
							"x" : 0,
							"y" : 25 - 25 + 5 + 15 + 15,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},					
					
					
					),
				},
				
			),
		},
	),
}

