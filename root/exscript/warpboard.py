import uiScriptLocale

WINDOW_WIDTH = 760
WINDOW_HEIGTH = 320 + 50

window = {
	"name" : "WarpWindow",
	"style" : ("movable", "float",),

	"x" : 124,
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
					"name" : "nav_board",
					"type" : "board",
					"style" : ("attach",),
					
					"x" : 15,
					"y" : 15,
					
					"width" : 200+20,
					"height" : 355 + 50,
					
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

							"text" : "Reiche (Map1)",
						
						},
						{
							"name" : "nav_button_1",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Reiche (Map2)",
						
						},
						{
							"name" : "nav_button_2",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 30 + 30 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Dungeons",
						
						},
						{
							"name" : "nav_button_3",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 30 + 30 + 30 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Farmmaps",
						
						},
						{
							"name" : "nav_button_4",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 30 + 30 + 30 + 30 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Levelmaps",
						
						},
						{
							"name" : "nav_button_5",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Bossmap",
						
						},
						{
							"name" : "nav_button_6",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30 + 30,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Sonstige",
						
						},
						{
							"name" : "nav_button_7",
							"type" : "button",
							
							"x" : 30,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30 + 60,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Eventmaps",
						
						},
						{
							"name" : "nav_button_save",
							"type" : "toggle_button",
							
							"x" : 30,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30 + 140,
						
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Shortcut verwalten",
						
						},					
					
					
					),
				
				},
				{
					"name" : "warp_window",
					"type" : "window",
					"style" : ("attach",),
					
					"x" : 230,
					"y" : 15,
					
					
					"width": 450 + 60,
					"height": 320 + 50,
				
					"children" : (
					
						{
							"name" : "warp_box_0",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0,
							"y" : 1,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_0",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_0",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_0",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_0",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_0",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_0",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},
						{
							"name" : "warp_box_1",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0 + 130 + 5,
							"y" : 1,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_1",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_1",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_1",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_1",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_1",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_1",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},					
						{
							"name" : "warp_box_2",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0 + 135 + 135,
							"y" : 1,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_2",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_2",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_2",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_2",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_2",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_2",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},					
						{
							"name" : "warp_box_3",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0 + 135 + 135 + 135,
							"y" : 1,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_3",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_3",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_3",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_3",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_3",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_3",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},					

						# second Row
						{
							"name" : "warp_box_4",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0,
							"y" : 1 + 165 - 10,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_4",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_4",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_4",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_4",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_4",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_4",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},
						{
							"name" : "warp_box_5",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0 + 130 + 5,
							"y" : 1 + 165 - 10,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_5",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_5",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_5",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_5",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_5",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_5",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},					
						{
							"name" : "warp_box_6",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0 + 135 + 135,
							"y" : 1 + 165 - 10,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_6",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_6",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_6",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_6",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_6",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_6",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},					
						{
							"name" : "warp_box_7",
							"type" : "image",
							"style" : ("attach",),
							
							"x" : 0 + 135 + 135 + 135,
							"y" : 1 + 165 - 10,
							
							"image" : "images_warp/map_1.tga",
							
							"children" : (
								{
									"name" : "warp_box_frame_7",
									"type" : "image",
									"style" : ("attach",),
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_warp/frame.tga",								
								},
								{
									"name" : "map_name_text_7",
									"type" : "text",
									
									"x" : 65,
									"y" : 11,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Yongan",
								},
								{
									"name" : "itemSlot_7",
									"type" : "slot",
									
									"x" : 65-16,
									"y" : 50,
									
									"width" : 32,
									"height" : 32,
									
									"slot" : (
										{"index":0, "x":0, "y":0, "width":32, "height":32},
									),
								
								},
								{
									"name" : "map_level_text_7",
									"type" : "text",
									
									"x" : 65,
									"y" : 95,
									
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "[ Ab lv.1 ]",
								},
								{
									"name" : "shortcut_button_7",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Shortcut setzen",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},
								{
									"name" : "warp_button_7",
									"type" : "button",
									
									"x" : 18,
									"y" : 110,
									
									"text" : "Teleportieren",
								
									"default_image" : "yamato_helpboard/normal_button_n.tga", 
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",				
								},							
							),
						},	

						{
							"name" : "page_navigation",
							"type" : "image",
							"style" : ("attach",),
									
							"x" : 0,
							"y" : 1 + 165 - 10 + 155,
									
							"image" : "yamato_warp/page_nav_bg.tga",	

							"children" : (
								{
									"name" : "pageNumber_Text",
									"type" : "text",
									"x" : "0",
									"y" : "0",
									"horizontal_align" : "center", 
									"text_horizontal_align":"center",
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"color" : 0xffd8a055,
									"outline" : 1,
									"text" : "1 / 7",
								},
								{
									"name" : "page_button_left",
									"type" : "button",
									"text" : "",
									"x" : 70 + 55,
									"y" : 12,
									"default_image" : "yamato_select/leftrotator_n.tga",
									"over_image" : "yamato_select/leftrotator_h.tga",
									"down_image" : "yamato_select/leftrotator_p.tga",
								},
								{
									"name" : "page_button_right",
									"type" : "button",
									"text" : "",
									"x" : 263 + 60 + 55,
									"y" : 12,
									"default_image" : "yamato_select/rightrotator_n.tga",
									"over_image" : "yamato_select/rightrotator_h.tga",
									"down_image" : "yamato_select/rightrotator_p.tga",
								},							
							
							),
							
						},
					),
				},
				
				
				{
					"name" : "shortcut_background",
					"type" : "bar",
					"style" : ("attach",),
					
					"x" : 25,
					"y" : 15,
					
					"width" : WINDOW_WIDTH - 20, 
					"height" : WINDOW_HEIGTH,
					
					"children" : (
						{
							"name" : "shortcut_desc",
							"type" : "text",
							"x" : 0,
							"y" : 0 - 25,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"vertical_align" : "center",
							"text_vertical_align" : "center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Drücke F5 - F12 um die ausgewählte Map einer Taste zu zuweisen!",
						},
					
						{
							"name" : "shortcut_close_button",
							"type" : "button",
									
							"x" : 0,
							"y" : 25 - 25 + 5,
									
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
				
				
				# {
							
					# "name" : "shortcut_config_board",
					# "type" : "board",
								
					# "x" : 220,
					# "y" : 15,
								
								
					# "width": 450 + 60 + 30 + 20,
					# "height": 320 + 50 + 30 + 5,
							
					# "no_bottom" : 1,
					
					# "children" : (
						# {
							# "name" : "split_box",
							# "type" : "board",
										
							# "x" : 0,
							# "y" : 0,
										
										
							# "width": 290 + 25,
							# "height": 320 + 50 + 30 + 5,
									
							# "no_bottom" : 1,						
						
						
						
						# },
						
						# {
							# "name" : "mapList",
							# "type" : "listbox",
							
							# "x" : 25,
							# "y" : 15,
							
							# "width" : 265,
							# "height" : 320 + 50 + 30 + 5 - 50,								
							
						# },
						# {
							# "name" : "mapListScrollBar",
							# "type" : "scrollbar",
							
							
							# "x" : 265 + 10,
							# "y" : 15,
							
							# "size" : 320 + 50 + 30 + 5 - 50,
						# },
						
						
						# {
							# "name" : "shortcut_F1_Text",
							# "type" : "text",
						
							# "x" : 300,
							# "y" : 15,
							
							# "text" : "[F1]",
							
							# "outline" : 1,
						# }
					
					
					# ),

				# },


				
			),
		},
	),
}

