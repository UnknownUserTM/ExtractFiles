import uiScriptLocale

window = {
	"name" : "RefineDialog",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 400,
	"y" : 70 * 800 / SCREEN_HEIGHT,

	"width" : 0,
	"height" : 0,

	"children" :
	(
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : 184+30+15-5,
			"color" : "red",

		},
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 0,
			"height" : 0,

			"children" :
			(
				{
					"name" : "SuccessPercentage",
					"type" : "text",
					"text" : uiScriptLocale.REFINE_INFO,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",
					"text_horizontal_align" : "center",
					"x" : 0,
					"y" : 70,
				},
				{
					"name" : "Cost",
					"type" : "text",
					"text" : uiScriptLocale.REFINE_COST,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",
					"text_horizontal_align" : "center",
					"x" : 0,
					"y" : 54,
				},
				{
					"name" : "AcceptButton",
					"type" : "button",

					"x" : -35,
					"y" : 35,

					"text" : uiScriptLocale.OK,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "yamato_button/button_small_n.tga", 
					"over_image" : "yamato_button/button_small_h.tga", 
					"down_image" : "yamato_button/button_small_p.tga", 
				},
				{
					"name" : "CancelButton",
					"type" : "button",

					"x" : 35,
					"y" : 35,

					"text" : uiScriptLocale.CANCEL,
					"horizontal_align" : "center",
					"vertical_align" : "bottom",

					"default_image" : "yamato_button/button_small_n.tga", 
					"over_image" : "yamato_button/button_small_h.tga", 
					"down_image" : "yamato_button/button_small_p.tga",
				},
			),
		},
	),
}