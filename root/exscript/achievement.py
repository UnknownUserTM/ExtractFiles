import uiScriptLocale

WINDOW_WIDTH = 282
WINDOW_HEIGTH = 84

window = {
	"name" : "Achievement",
	"style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGTH,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "image",

			"x" : 0,
			"y" : 0,

			"image" : "yamato_achievement/achievement_de_background.tga",
		},
	),
}

