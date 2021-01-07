import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"

Y_ADD_POSITION = 0

window = {
	"name" : "PlayerFrame",
	
	"style" : ("movable", "float",),
	
	"x" : 10,
	"y" : 45,

	"width" : 223,
	"height" : 74,

	"children" :
	(
		{
			"name" : "PlayerFrameMask",
			"type" : "expanded_image",

			"x" : 13,
			"y" : 8,
			
			"width" : 223,
			"height" : 74,
			
			"rect" : (0.0, 0.0, 0.0, 0.0),

			"image" : "yamato_playerframe/player_frame_mask.tga",
		},
		{
			"name" : "PlayerFrameIcon",
			"type" : "expanded_image",

			"x" : 15,
			"y" : 13,
			
			"width" : 223,
			"height" : 74,
			
			"rect" : (0.0, 0.0, 0.0, 0.0),

			"image" : ROOT + "windows/face_warrior.sub",
		},
		{
			"name" : "PlayerFrameBase",
			"type" : "expanded_image",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,
			
			"width" : 223,
			"height" : 74,
			
			"rect" : (0.0, 0.0, 0.0, 0.0),

			"image" : "yamato_taskbar/pframe_full_merge.tga",
		},
		
		{
			"name" : "statisticTriggerWindow",
			"type" : "window",
			
			"x" : 13,
			"y" : 8,

			"width" : 53,
			"height" : 53,
		
		},
		
		
		## TP Anzeige
		{
			"name" : "HPGauge_Board",
			"type" : "window",

			"x" : 80,
			"y" : 20,

			"width" : 114,
			"height" : 11,

			"children" :
			(
				{
					"name" : "HPRecoveryGaugeBar",
					"type" : "bar",

					"x" : 0,
					"y" : 0,
					"width" : 114,
					"height" : 11,
					"color" : 0x55ff0000,
				},
				{
					"name" : "HPGauge",
					"type" : "ani_image",

					"x" : 0,
					"y" : 0,

					"delay" : 6,

					"images" :
					(
						"yamato_taskbar/player_resource_hp.tga",
						"yamato_taskbar/player_resource_hp.tga",
						"yamato_taskbar/player_resource_hp.tga",
					),
				},
				{
					"name" : "HPInfoTextLine",
					"type" : "text",
		 
					"x" : 57,
					"y" : 3-5,
					
					"outline" : 1,
		 
					"text_horizontal_align" : "center",
		 
					"text" : "100.00%",
				},
			),
		},
		## MP Anzeige
		{
			"name" : "MPGauge_Board",
			"type" : "window",

			"x" : 80,
			"y" : 40,

			"width" : 112,
			"height" : 11,

			"children" :
			(
				{
					"name" : "MPRecoveryGaugeBar",
					"type" : "bar",

					"x" : 0,
					"y" : 0,
					"width" : 105,
					"height" : 11,
					"color" : 0x550000ff,
				},
				{
					"name" : "MPGauge",
					"type" : "ani_image",

					"x" : 0,
					"y" : 0,

					"delay" : 6,

					"images" :
					(
						"yamato_taskbar/player_resource_mana.tga",
						"yamato_taskbar/player_resource_mana.tga",
						"yamato_taskbar/player_resource_mana.tga",
					),
				},
				{
					"name" : "MPInfoTextLine",
					"type" : "text",
		 
					"x" : 52,
					"y" : 3-5,
					
					"outline" : 1,
		 
					"text_horizontal_align" : "center",
		 
					"text" : "100.00%",
				},
			),
		},
		{
			"name" : "PlayerLevel",
			"type" : "text",
 
			"x" : 67,
			"y" : 51,
			
			"outline" : 1,
 
			"text_horizontal_align" : "center",
 
			"text" : "99",
		},
		{
			"name" : "EXPGauge",
			"type" : "ani_image",

			"x" : 67 + 5 + 10 + 10 - 4,
			"y" : 51 + 10 - 1,

			"delay" : 6,

			"images" :
			(
				"yamato_taskbar/xp_fill.tga",
				"yamato_taskbar/xp_fill.tga",
				"yamato_taskbar/xp_fill.tga",
			),
		},
		{
			"name" : "EXPInfoTextLine",
			"type" : "text",
		 
			"x" : 67 + 5 + 10 + 10 - 4 + 15,
			"y" : 51 + 10 - 1 + 20 - 8,
					
			"outline" : 1,
		 
			"text_horizontal_align" : "center",
		 
			"text" : "100.00%",
		},
		
	),
}











