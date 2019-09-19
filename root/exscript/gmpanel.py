import uiScriptLocale

WINDOW_WIDTH = 180
WINDOW_HEIGTH = 390

window = {
	"name" : "GMPanel",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60,
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
					"name" : "gm_panel_0",
					"type" : "button",
							
					"x" : 25,
					"y" : 15,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Support-Panel",
						
				},			
				{
					"name" : "gm_panel_1",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Announcement-Panel",
						
				},
				{
					"name" : "gm_panel_2",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Event-Panel",
						
				},
				{
					"name" : "gm_panel_3",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Invincibility",
						
				},
				{
					"name" : "gm_panel_4",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "BIG DAMAGE",
						
				},
				{
					"name" : "gm_panel_5",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30 + 45,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Debug-Mode",
						
				},
				{
					"name" : "gm_panel_6",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30 + 45 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "System Manager",
						
				},
				{
					"name" : "gm_panel_7",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Regen Maker",
						
				},
				{
					"name" : "gm_panel_8",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Quest Maker",
						
				},
				{
					"name" : "gm_panel_9",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 30 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "QuestText Maker",
						
				},	
				{
					"name" : "gm_panel_10",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 30 + 30 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "MultiShopEditor",
						
				},	
				# {
					# "name" : "gm_panel_11",
					# "type" : "button",
							
					# "x" : 25,
					# "y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 30 + 30 + 30 + 30,
						
					# "default_image" : "yamato_helpboard/wide_button_n.tga",
					# "over_image" : "yamato_helpboard/wide_button_h.tga",
					# "down_image" : "yamato_helpboard/wide_button_p.tga",
					# "disable_image" : "yamato_helpboard/wide_button_d.tga",

					# "text" : "BioQuest Maker",
						
				# },	
				{
					"name" : "gm_panel_11",
					"type" : "button",
							
					"x" : 25,
					"y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 30 + 30 + 30 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",

					"text" : "Item Maker",
						
				},				
				# {
					# "name" : "gm_panel_9",
					# "type" : "button",
							
					# "x" : 25,
					# "y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 45,
						
					# "default_image" : "yamato_helpboard/wide_button_n.tga",
					# "over_image" : "yamato_helpboard/wide_button_h.tga",
					# "down_image" : "yamato_helpboard/wide_button_p.tga",
					# "disable_image" : "yamato_helpboard/wide_button_d.tga",

					# "text" : "Debug-Mode",
						
				# },			
				# {
					# "name" : "gm_panel_10",
					# "type" : "button",
							
					# "x" : 25,
					# "y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 45 + 30,
						
					# "default_image" : "yamato_helpboard/wide_button_n.tga",
					# "over_image" : "yamato_helpboard/wide_button_h.tga",
					# "down_image" : "yamato_helpboard/wide_button_p.tga",
					# "disable_image" : "yamato_helpboard/wide_button_d.tga",

					# "text" : "Regen-Maker",
						
				# },			
				# {
					# "name" : "gm_panel_11",
					# "type" : "button",
							
					# "x" : 25,
					# "y" : 15 + 30 + 30 + 45 + 30 + 45 + 30 + 30 + 45 + 30 + 30,
						
					# "default_image" : "yamato_helpboard/wide_button_n.tga",
					# "over_image" : "yamato_helpboard/wide_button_h.tga",
					# "down_image" : "yamato_helpboard/wide_button_p.tga",
					# "disable_image" : "yamato_helpboard/wide_button_d.tga",

					# "text" : "Pythonloader",
						
				# },				
			
			),
		},
	),
}

