ROOT = "d:/ymir work/ui/minimap/"

window = {
	"name" : "MiniMap",

	"x" : SCREEN_WIDTH - 136,
	"y" : 0,

	"width" : 136,
	"height" : 137,

	"children" :
	(
		## OpenWindow
		{
			"name" : "OpenWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 136,
			"height" : 137,

			"children" :
			(
				{
					"name" : "OpenWindowBGI",
					"type" : "image",
					"x" : 0,
					"y" : 0,
					"image" : ROOT + "minimap.sub",
				},
				## MiniMapWindow
				{
					"name" : "MiniMapWindow",
					"type" : "window",

					"x" : 4,
					"y" : 5,

					"width" : 128,
					"height" : 128,
				},
				## ScaleUpButton
				{
					"name" : "ScaleUpButton",
					"type" : "button",

					"x" : 101,
					"y" : 116,

					"default_image" : ROOT + "minimap_scaleup_default.sub",
					"over_image" : ROOT + "minimap_scaleup_over.sub",
					"down_image" : ROOT + "minimap_scaleup_down.sub",
				},
				## ScaleDownButton
				{
					"name" : "ScaleDownButton",
					"type" : "button",

					"x" : 115,
					"y" : 103,

					"default_image" : ROOT + "minimap_scaledown_default.sub",
					"over_image" : ROOT + "minimap_scaledown_over.sub",
					"down_image" : ROOT + "minimap_scaledown_down.sub",
				},
				{
					"name" : "GMPanelButton",
					"type" : "button",

					"x" : 12 - 5 -13,
					"y" : 103 + 5 - 24,

					"default_image" : "yamato_mm/gm_button.tga",
					"over_image" : "yamato_mm/gm_button.tga",
					"down_image" : "yamato_mm/gm_button.tga",
				},
				{
					"name" : "SwitchBotButton",
					"type" : "button",

					"x" : 12 - 5,
					"y" : 103 + 5,

					"default_image" : "yamato_mm/switchbot_button.tga",
					"over_image" : "yamato_mm/switchbot_button.tga",
					"down_image" : "yamato_mm/switchbot_button.tga",
				},
				## MiniMapHideButton
				{
					"name" : "MiniMapHideButton",
					"type" : "button",

					"x" : 111,
					"y" : 6,

					"default_image" : "yamato_button/close_n.dds",
					"over_image" : "yamato_button/close_h.dds",
					"down_image" : "yamato_button/close_p.dds",
				},
				## AtlasShowButton
				{
					"name" : "AtlasShowButton",
					"type" : "button",

					"x" : 12,
					"y" : 12,

					"default_image" : ROOT + "atlas_open_default.sub",
					"over_image" : ROOT + "atlas_open_over.sub",
					"down_image" : ROOT + "atlas_open_down.sub",
				},
				## ServerInfo
				{
					"name" : "ServerInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 140,

					"text" : "",
				},
				## PositionInfo
				{
					"name" : "PositionInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 200,

					"text" : "",
				},
				## BioTimer
				{
					"name" : "BioTimerInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 240,

					"text" : "Bio-Timer",
				},
				## Time
				{
					"name" : "TimeInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 160,

					"text" : "Uhrzeit",
				},
				## MapName
				{
					"name" : "MapNameInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 180,

					"text" : "MapName",
				},				
				
				## Bossmap
				{
					"name" : "bossMapTitle",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 230,

					"text" : "[ Bossmap ]",
				},
				## Bossmap-Uses
				{
					"name" : "bossMapUses",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 245,

					"text" : "0 Rufrollen verbl.",
				},
				## Bossmap-Timer
				{
					"name" : "bossMapTimer",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 260,

					"text" : "0 Min. bis Reset!",
				},

				## ObserverCount
				{
					"name" : "ObserverCount",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 180,

					"text" : "",
				},
			),
		},
		{
			"name" : "CloseWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 132,
			"height" : 48,

			"children" :
			(
				## ShowButton
				{
					"name" : "MiniMapShowButton",
					"type" : "button",

					"x" : 100,
					"y" : 4,

					"default_image" : ROOT + "minimap_open_default.sub",
					"over_image" : ROOT + "minimap_open_default.sub",
					"down_image" : ROOT + "minimap_open_default.sub",
				},
			),
		},
	),
}
