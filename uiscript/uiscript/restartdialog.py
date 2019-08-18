import uiScriptLocale

ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "RestartDialog",
	"style" : ("float",),

	"x" : 250,
	"y" : 50,

	"width" : 200 - 15 - 3,
	"height" : 75,

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinboard",

			"x" : 0,
			"y" : 0,

			"width" : 200 - 15 - 3,
			"height" : 75,

			"r" : 0.3333,
			"g" : 0.2941,
			"b" : 0.2588,
			"a" : 1.0,

			"children" :
			(
				{
					"name" : "restart_here_button",
					"type" : "button",

					"x" : 10,
					"y" : 10,

					"text" : uiScriptLocale.RESTART_HERE,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",
				},
				{
					"name" : "restart_town_button",
					"type" : "button",

					"x" : 10,
					"y" : 40,

					"text" : uiScriptLocale.RESTART_TOWN,

					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",
				},
			),
		},
	),
}
