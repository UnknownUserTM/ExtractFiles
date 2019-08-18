import uiScriptLocale

window = {
	"name" : "QuestionDialog",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2 - 125,
	"y" : SCREEN_HEIGHT/2 - 52,

	"width" : 380,
	"height" : 155,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 380,
			"height" : 155,

			"children" :
			(
				{
					"name" : "title",
					"type" : "text",

					"x" : 0,
					"y" : 15,

					"horizontal_align" : "center",
					"text" : "Kampfzone verlassen",

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "points",
					"type" : "text",

					"x" : 0,
					"y" : 38,

					"horizontal_align" : "center",
					"text" : "0 Punkt(e)",

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "message_line_01",
					"type" : "text",

					"x" : 0,
					"y" : 53,

					"horizontal_align" : "center",
					"text" : "Du hast Punkte gesammelt in der Kampfzone, um diese zu bergen musst du",

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "message_line_02",
					"type" : "text",

					"x" : 0,
					"y" : 68,

					"horizontal_align" : "center",
					"text" : "dich als Ziel makieren lassen. Solltest du dann besiegt werden",

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "message_line_03",
					"type" : "text",

					"x" : 0,
					"y" : 83,

					"horizontal_align" : "center",
					"text" : "verlierst du jedesmal 50% deiner Punkte, oder wähle Sofort",

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "message_line_04",
					"type" : "text",

					"x" : 0,
					"y" : 98,

					"horizontal_align" : "center",
					"text" : "jedoch verlierst du dann sämtliche Punkte, kannst die Zone aber sofort verlassen!",

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "normal",
					"type" : "button",

					"x" : -60,
					"y" : 113,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : "2 Min. Warten",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "instant",
					"type" : "button",

					"x" : 0,
					"y" : 113,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : "Sofort",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "cancel",
					"type" : "button",

					"x" : 60,
					"y" : 113,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : "Abbrechen",

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}