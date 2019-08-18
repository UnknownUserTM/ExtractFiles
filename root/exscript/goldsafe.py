import uiScriptLocale

WINDOW_WIDTH = 25 + 108 + 108 + 108
WINDOW_HEIGTH = 110

window = {
	"name" : "GoldSafe",
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
					"name" : "moneySlot_01",
					"type" : "bar",
				
					"x" : 25,
					"y" : 15,
					
					"width" : 108,
					"height" : WINDOW_HEIGTH- 5,
				
					"children" : (
					
						{
							"name" : "moneySlot_01_slotBG",
							"type" : "image",
							"style" : ("attach",),
									
							"x" : 50-16,
							"y" : 15,
									
							"image" : "images_jewel/red_slot.tga",								
						},

						{
							"name" : "moneySlot_01_slot",
							"type" : "slot",
									
							"x" : 50-16+4,
							"y" : 15+4,
									
							"width" : 32,
							"height" : 32,
									
							"slot" : (
								{"index":0, "x":0, "y":0, "width":32, "height":32},
							),
						},
					
						{
							"name" : "moneySlot_01_button",
							"type" : "button",
									
							"x" : 5,
							"y" : WINDOW_HEIGTH - 40,
																	
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},
					),
				},
				
				{
					"name" : "moneySlot_02",
					"type" : "bar",
				
					"x" : 25 + 110,
					"y" : 15,
					
					"width" : 108,
					"height" : WINDOW_HEIGTH- 5,
				
					"children" : (
					
						{
							"name" : "moneySlot_02_slotBG",
							"type" : "image",
							"style" : ("attach",),
									
							"x" : 50-16,
							"y" : 15,
									
							"image" : "images_jewel/red_slot.tga",								
						},

						{
							"name" : "moneySlot_02_slot",
							"type" : "slot",
									
							"x" : 50-16+4,
							"y" : 15+4,
									
							"width" : 32,
							"height" : 32,
									
							"slot" : (
								{"index":1, "x":0, "y":0, "width":32, "height":32},
							),
						},
					
						{
							"name" : "moneySlot_02_button",
							"type" : "button",
									
							"x" : 5,
							"y" : WINDOW_HEIGTH - 40,
																	
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},
					),
				},
				{
					"name" : "moneySlot_03",
					"type" : "bar",
				
					"x" : 25 + 110 + 110,
					"y" : 15,
					
					"width" : 108,
					"height" : WINDOW_HEIGTH- 5,
				
					"children" : (
					
						{
							"name" : "moneySlot_03_slotBG",
							"type" : "image",
							"style" : ("attach",),
									
							"x" : 50-16,
							"y" : 15,
									
							"image" : "images_jewel/red_slot.tga",								
						},

						{
							"name" : "moneySlot_03_slot",
							"type" : "slot",
									
							"x" : 50-16+4,
							"y" : 15+4,
									
							"width" : 32,
							"height" : 32,
									
							"slot" : (
								{"index":2, "x":0, "y":0, "width":32, "height":32},
							),
						},
					
						{
							"name" : "moneySlot_03_button",
							"type" : "button",
									
							"x" : 5,
							"y" : WINDOW_HEIGTH - 40,
																	
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

