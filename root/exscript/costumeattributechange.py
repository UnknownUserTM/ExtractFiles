import uiScriptLocale

WINDOW_WIDTH = 400
WINDOW_HEIGTH = 300

window = {
	"name" : "CostumeAttributeChanger",
	"style" : ("movable", "float",),

	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30,

	"children" :
	(				
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : WINDOW_WIDTH+30+15,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			"children" : (
				{
					"name" : "background",
					"type" : "thinboard_circle",
					"style" : ("movable","attach",),
					
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 25 + 15,
					"height" : WINDOW_HEIGTH + 5,
					
					
					"children" : (
						{
							"name" : "costumeBackground",
							"type" : "thinboard_circle",
							
							
							"x" : 0,
							"y" : 0,
							
							"width" : 100,
							"height" : WINDOW_HEIGTH + 5,
							
							"children" : (
								{
									"name" : "costumeTitleBackground",
									"type" : "thinboard_circle",
									
									
									"x" : 0,
									"y" : 0,
									
									"width" : 100,
									"height" : 22,								
								
									"children" : (
										{
														
											"name" : "costumeTitleTitleTextLine",
											"type" : "text",
															
											"x" : 100 / 2,
											"y" : 3,
																								
											"text" : "Kostüm",
											"text_horizontal_align" : "center",
											"outline" : 1,
										},	
									
									),
								},
								{
									"name" : "CostumeSlotBackground",
									"type" : "thinboard_circle",
									
									"x" : 50-16,
									"y" : 35,
									
									"width" : 32,
									"height" : 96,
									
									
									"children" : (
										{
											"name" : "costumeSlot",
											"type" : "grid_table",
						 
											"x" : 0,
											"y" : 0,
											
											"start_index" : 0,
											"x_count" : 1,
											"y_count" : 3,
											"x_step" : 32,
											"y_step" : 32,
										},	
									),
								},

								{
									"name" : "costumeSwitcherSlotBackground",
									"type" : "thinboard_circle",
									
									"x" : 50-16,
									"y" : 35 + 96 + 13,
									
									"width" : 32,
									"height" : 32,
									
									"children" : (
										{
											"name" : "costumeSwitcherSlot",
											"type" : "grid_table",
						 
											"x" : 0,
											"y" : 0,
											
											"start_index" : 0,
											"x_count" : 1,
											"y_count" : 1,
											"x_step" : 32,
											"y_step" : 32,
										},	
									),
									
								},
								{
									"name" : "costumeSpecialSwitcherSlotBackground",
									"type" : "thinboard_circle",
									
									"x" : 50-16,
									"y" : 35 + 96 + 13 +32 +16,
									
									"width" : 32,
									"height" : 32,
									
									"children" : (
										{
											"name" : "specialCostumeSwitcherSlot",
											"type" : "grid_table",
						 
											"x" : 0,
											"y" : 0,
											
											"start_index" : 0,
											"x_count" : 1,
											"y_count" : 1,
											"x_step" : 32,
											"y_step" : 32,
										},	
									),
								},							
							),
						},
						{
							"name" : "bonusChangeBackground",
							"type" : "thinboard_circle",
							
							
							"x" : 100,
							"y" : 0,
							
							"width" : 290,
							"height" : WINDOW_HEIGTH + 5,
							
							"children" : (
								{
									"name" : "bonusChangeTitleBackground",
									"type" : "thinboard_circle",
									
									
									"x" : 0,
									"y" : 0,
									
									"width" : 290,
									"height" : 22,	

									"children" : (
										{
														
											"name" : "bonusChangeTitleTextLine",
											"type" : "text",
															
											"x" : 290 / 2,
											"y" : 3,
																								
											"text" : "Bonus ändern",
											"text_horizontal_align" : "center",
											"outline" : 1,
										},	
									
									),
								
								
								},
								{
									"name" : "systemDescription",
									"type" : "text",
									
									"x" : 12,
									"y" : 35 + 96 + 13,
									
									"multi_line" : 290 - 24,
									"text" : "Hier steht dann später wie alles funktioniert. Ist MultiLine wird automatisch auf mehrere zeilen gesetzt wenn der Text breiter ist als 266px. Hoffentlich klappt das, denn das wäre echt easy dann. So ich brauch noch mehr Text. Den Text hier gibts nur damit dieser Bereich hier nicht so leer ist.",

								},
							
							
							
							),
						},						
					
					
					
					),
					
				},
			
			
			
			),
		},
	),
}

