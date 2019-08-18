import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"

Y_ADD_POSITION = 0

window = {
	"name" : "LoadingWindow",

	"x" : (SCREEN_WIDTH / 2) - (273/2),
	"y" : SCREEN_HEIGHT / 2,

	"width" : 273,
	"height" : 41,

	"children" :
	(
		{
			"name" : "loading_bg",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,
			
			"width" : 223,
			"height" : 74,
			
			"rect" : (0.0, 0.0, 0.0, 0.0),

			"image" : "yamato_halloffame/pcb_empty.tga",
		},
	),
}











