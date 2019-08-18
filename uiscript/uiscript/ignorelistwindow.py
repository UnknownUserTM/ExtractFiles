####  Released by d3m0n3  #####

import uiScriptLocale

window = {
	"name" : "IgnoreListWindow",

	"x" : SCREEN_WIDTH - 170,
	"y" : SCREEN_HEIGHT - 400 - 50,

	"style" : ("movable", "float",),

	"width" : 170,
	"height" : 300,

	"children" :
	(

		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 170,
			"height" : 300,
			"title" : "Block System",
		},

		{
			"name" : "ScrollBar",
			"type" : "scrollbar",

			"x" : 27,
			"y" : 40,
			"size" : 220,
			"horizontal_align" : "right",
		},

		{
			"name" : "sblocca",
			"type" : "button",

			"x" : 15,
			"y" : 265,

			"width" : 61,
			"height" : 21,

			"text" : "Entsperren",

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
		{
			"name" : "blocca",
			"type" : "button",

			"x" : 60,
			"y" : 265,

			"width" : 41,
			"height" : 21,

			"text" : "Sperren",

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},

		{
			"name" : "aggiorna",
			"type" : "button",

			"x" : 115,
			"y" : 265,

			"width" : 41,
			"height" : 21,

			"text" : "Aktualisieren",

			"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
		},
	)
}
