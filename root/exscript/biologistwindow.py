import uiScriptLocale

WINDOW_WIDTH = 180
WINDOW_HEIGTH = 230

window = {
	"name" : "BiologistWindow",
	"style" : ("movable", "float",),

	"x" : 440,
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
			
				{ # Row 1
					"name" : "slot_bg_01_01",
					"type" : "image",
					
					"x" : 25,
					"y" : 15,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_01_02",
					"type" : "image",
					
					"x" : 25 + 32,
					"y" : 15,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},			
				{
					"name" : "slot_bg_01_03",
					"type" : "image",
					
					"x" : 25 + 32 + 32,
					"y" : 15,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},	
				{
					"name" : "slot_bg_01_04",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32,
					"y" : 15,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_01_05",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32 + 32,
					"y" : 15,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{ # Row 2
					"name" : "slot_bg_02_01",
					"type" : "image",
					
					"x" : 25,
					"y" : 15 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_02_02",
					"type" : "image",
					
					"x" : 25 + 32,
					"y" : 15 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},			
				{
					"name" : "slot_bg_02_03",
					"type" : "image",
					
					"x" : 25 + 32 + 32,
					"y" : 15 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},	
				{
					"name" : "slot_bg_02_04",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32,
					"y" : 15 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_02_05",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32 + 32,
					"y" : 15 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},				
				{ # Row 3
					"name" : "slot_bg_03_01",
					"type" : "image",
					
					"x" : 25,
					"y" : 15 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_03_02",
					"type" : "image",
					
					"x" : 25 + 32,
					"y" : 15 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},			
				{
					"name" : "slot_bg_03_03",
					"type" : "image",
					
					"x" : 25 + 32 + 32,
					"y" : 15 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},	
				{
					"name" : "slot_bg_03_04",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32,
					"y" : 15 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_03_05",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32 + 32,
					"y" : 15 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},				
				{ # Row 4
					"name" : "slot_bg_04_01",
					"type" : "image",
					
					"x" : 25,
					"y" : 15 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_04_02",
					"type" : "image",
					
					"x" : 25 + 32,
					"y" : 15 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},			
				{
					"name" : "slot_bg_04_03",
					"type" : "image",
					
					"x" : 25 + 32 + 32,
					"y" : 15 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},	
				{
					"name" : "slot_bg_04_04",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32,
					"y" : 15 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_04_05",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32 + 32,
					"y" : 15 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},				
				{ # Row 5
					"name" : "slot_bg_05_01",
					"type" : "image",
					
					"x" : 25,
					"y" : 15 + 32 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_05_02",
					"type" : "image",
					
					"x" : 25 + 32,
					"y" : 15 + 32 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},			
				{
					"name" : "slot_bg_05_03",
					"type" : "image",
					
					"x" : 25 + 32 + 32,
					"y" : 15 + 32 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},	
				{
					"name" : "slot_bg_05_04",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32,
					"y" : 15 + 32 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},
				{
					"name" : "slot_bg_05_05",
					"type" : "image",
					
					"x" : 25 + 32 + 32 + 32 + 32,
					"y" : 15 + 32 + 32 + 32 + 32,
					
					"image" : "d:/ymir work/ui/public/slot_base.sub",
				},				
				
                {
                    "name" : "ItemSlot",
                    "type" : "grid_table",
 
					# "x" : 23,
					# "y" : 244-20 + 20,
					"x" : 25,
					"y" : 15,
					
                    "start_index" : 0,
                    "x_count" : 5,
                    "y_count" : 5,
                    "x_step" : 32,
                    "y_step" : 32,

                    # "image" : "d:/ymir work/ui/dragonsoul/cap.tga",
					"image" : "d:/ymir work/ui/public/slot_base.sub"
                    # "image" : "yamato_slot/slot_main.dds"
                },	
				{
					"name" : "estimated_Time",
					"type" : "text",
					
					"x" : 105,
					"y" : 15 + 32 + 32 + 32 + 32 + 32 + 10, 
					
					"text" : "Forschungszeit: 00:00:00",
					
					"outline" : 1,
					
					"color" : 0xffd8a055,
					"text_horizontal_align" : "center",
				
				},
				{
					"name" : "start_research",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 32 + 32 + 32 + 32 + 32 + 10 + 20, 
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Untersuchung starten",
				},				

				
			
			),
		},
	),
}

