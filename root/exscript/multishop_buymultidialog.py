import uiScriptLocale

window = {
	"name" : "QuestionDialog",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH/2 - 125,
	"y" : SCREEN_HEIGHT/2 - 52,

	"width" : 340,
	"height" : 135,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 340,
			"height" : 135,

			"children" :
			(
				{
					"name" : "message",
					"type" : "text",

					"x" : 0,
					"y" : 34,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.MESSAGE,

					"text_horizontal_align" : "center",
					"text_vertical_align" : "center",
				},
				{
					"name" : "inputBackground",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 50,
					
					"width" : 120,
					"height" : 18,
				
					"horizontal_align" : "center",
					
					
					"children" : (
					
						{
							"name" : "inputEditLine",
							"type" : "editline",
													
							"x" : 4,
							"y" : 2,
													
							"input_limit" : 3,
							"only_number" : 1,
													
							"text" : "1",
							
							"width" : 100,
							"height" : 20,
						},
					
					
					
					
					),
				
				
				},
				{
					"name" : "accept",
					"type" : "button",

					"x" : -55,
					"y" : 63 + 20,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.YES,

					"default_image" : "yamato_helpboard/normal_button_n.tga",
					"over_image" : "yamato_helpboard/normal_button_h.tga",
					"down_image" : "yamato_helpboard/normal_button_p.tga",
					"disable_image" : "yamato_helpboard/normal_button_d.tga",
				},
				{
					"name" : "cancel",
					"type" : "button",

					"x" : 55,
					"y" : 63 + 20,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",
					"text" : uiScriptLocale.NO,

					"default_image" : "yamato_helpboard/normal_button_n.tga",
					"over_image" : "yamato_helpboard/normal_button_h.tga",
					"down_image" : "yamato_helpboard/normal_button_p.tga",
					"disable_image" : "yamato_helpboard/normal_button_d.tga",
				},
			),
		},
	),
}