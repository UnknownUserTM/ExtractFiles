import uiScriptLocale

window = {
	"name" : "AchievementItem",
	"style" : ("float",),

	"x" : 0,
	"y" : 0,

	"width" : 225,
	"height" : 51,

	"children" :
	(				
		{
			"name" : "board",
			"type" : "thinboard_circle",
			"style" : ("attach",),

			"x" : 5,
			"y" : 0,

			"width" : 215,
			"height" : 51,
			
			"children" : (
				{
					"name" : "achievementImageBackground",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 0,
					
					"width" : 51,
					"height" : 51,
				
					"children" : (
						{
							"name" : "achievementImage",
							"type" : "image",
							
							"x" : 0,
							"y" : 0,
							
							"image" : "images_achievement/691.tga",
						},
					),
				
				},
				{
								
					"name" : "titleTextLine",
					"type" : "text",
									
					"x" : 215 / 2 + 25,
					"y" : 3 + 5,
																		
					"text" : "Oberork getötet",
					"outline" : 1,
					"text_horizontal_align" : "center",
				},	
				{
								
					"name" : "infoTextLine",
					"type" : "text",
									
					"x" : 215 / 2 + 25,
					"y" : 3 + 18 + 5,
																		
					"text" : "Anzahl: 41 | Punkte: 10",
					"outline" : 1,
					"text_horizontal_align" : "center",
				},
			),
		},
	),
}

