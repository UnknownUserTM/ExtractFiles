import uiScriptLocale

WINDOW_WIDTH = 315
WINDOW_HEIGTH = 395 + 6

window = {
	"name" : "CalenderWindow",
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
				
					"name" : "QuestListWindow",
					"type" : "window",
					"style" : ("movable","attach",),
					
					"x" : 20,
					"y" : 10,
					
					"width" : 305,
					"height" : 400 + 6,
					
					"children" : (
						{
							"name" : "QuestListBackground",
							"type" : "thinboard_circle",
							"style" : ("movable","attach",),
							
							"x" : 0,
							"y" : 0,
							
							"width" : 305,
							"height" : 400 + 6,	

							"children" : (
							
								{
									"name" : "QuestListScrollBar",
									"type" : "small_thin_scrollbar",
											
									"x" : 305 - 15,
									"y" : 1,
											
									"size" : 404,
								},
							
							
							),
						},
					),
				},
				{
				
					"name" : "QuestDescWindow",
					"type" : "window",
					"style" : ("movable","attach",),
					
					"x" : 20,
					"y" : 10,
					
					"width" : 305,
					"height" : 400 + 6,
					
					"children" : (
						{
							"name" : "QuestListBackground",
							"type" : "thinboard_circle",
							"style" : ("movable","attach",),
							
							"x" : 0,
							"y" : 0,
							
							"width" : 305,
							"height" : 400 + 6,	

							"children" : (
								{
									"name" : "QuestTitleBackground",
									"type" : "thinboard_circle",
									"style" : ("movable","attach",),
									
									"x" : 0,
									"y" : 0,
									
									"width" : 305,
									"height" : 18,									
								
									"children" : (
										{
											"name" : "QuestTitle",
											"type" : "text",
											
											"x" : 152,
											"y" : 2, 
											
											"text" : "Orkzahnforschung:",
											
											"outline" : 1,
											
											"color" : 0xffd8a055,
											"text_horizontal_align" : "center",
										},									
									),
								},
								
								{
									"name" : "QuestDescriptionBackground",
									"type" : "thinboard_circle",
									"style" : ("movable","attach",),
									
									"x" : 0,
									"y" : 18,
									
									"width" : 305,
									"height" : 150,
									
									"children" : (
									
										{
											"name" : "QuestContentListBox",
											"type" : "questlistbox",
											
											"x" : 4,
											"y" : 1,
											
											"width" : 303,
											"height" : 148,
										},
										{
											"name" : "scrollBar",
											"type" : "small_thin_scrollbar",
											
											"x" : 305 - 15,
											"y" : 1,
											
											"size" : 148,
										},
									
									),
									
									
								},
								{
									"name" : "QuestResearchBackground",
									"type" : "thinboard_circle",
									"style" : ("movable","attach",),
									
									"x" : 0,
									"y" : 18 + 150,
									
									"width" : 305,
									"height" : 18,									
								
									"children" : (
										{
											"name" : "QuestResearchTitle",
											"type" : "text",
											
											"x" : 152,
											"y" : 2, 
											
											"text" : "Forschungsübersicht:",
											
											"outline" : 1,
											
											"color" : 0xffd8a055,
											"text_horizontal_align" : "center",
										},									
									),
								},
								{
									"name" : "QuestResearchInfoBackground",
									"type" : "thinboard_circle",
									"style" : ("movable","attach",),
									
									"x" : 0,
									"y" : 18 + 150 + 18,
									
									"width" : 305,
									"height" : 40,
									
									"children" : (
										{
											"name" : "itemSlot",
											"type" : "slot",
																	
											"x" : 4,
											"y" : 4,
																	
											"width" : 32,
											"height" : 32,
																	
											"slot" : (
												{"index":0, "x":0, "y":0, "width":32, "height":32},
											),
																
										},	
										{
											"name" : "itemName",
											"type" : "text",
											
											"x" : 4 + 32 + 5,
											"y" : 4,
											
											"text" : "Name: Orkzahn",
											"outline" : 1,
										},
										{
											"name" : "itemCount",
											"type" : "text",
											
											"x" : 4 + 32 + 5,
											"y" : 4 + 15,
											
											"text" : "Anzahl: 0 / 10",
											"outline" : 1,
										},	

										{
											"name" : "researchTime",
											"type" : "text",
											
											"x" : 4 + 32 + 5 + 130,
											"y" : 4,
											
											"text" : "Forschungsdauer: 10 Min.",
											"outline" : 1,
										},
										{
											"name" : "researchChance",
											"type" : "text",
											
											"x" : 4 + 32 + 5 + 130,
											"y" : 4 + 15,
											
											"text" : "Erfolgschance: 80%",
											"outline" : 1,
										},										
									
									),
								},
								{
									"name" : "QuestResearchTable",
									"type" : "thinboard_circle",
									"style" : ("movable","attach",),
									
									"x" : 0,
									"y" : 18 + 150 + 18 + 40,
									
									"width" : 305,
									"height" : 18,									
								
									"children" : (
										{
											"name" : "QuestResearchTableTitle",
											"type" : "text",
											
											"x" : 152,
											"y" : 2, 
											
											"text" : "Untersuchungen:",
											
											"outline" : 1,
											
											"color" : 0xffd8a055,
											"text_horizontal_align" : "center",
										},	

									),
								},
								{
									"name" : "QuestResearchExecute",
									"type" : "thinboard_circle",
									"style" : ("movable","attach",),
									
									"x" : 0,
									"y" : 18 + 150 + 18 + 40 + 18,
									
									"width" : 305,
									"height" : 160,
									
									"children" : (
										{
											"name" : "researchWindow",
											"type" : "window",
											
											"x" : 0,
											"y" : 15,
											
											"horizontal_align" : "center", 
											
											"width" : 240,
											"height" : 100,
											
											
											"children" : (
												{
													"name" : "targetItemBackground",
													"type" : "thinboard_circle",
													
													"x" : 0,
													"y" : 0,
													
													"width" : 80,
													"height" : 70,
													
													"children" : (
														{
															"name" : "targetItemTitleBackground",
															"type" : "thinboard_circle",
															
															"x" : 0,
															"y" : 0,
															
															"width" : 80,
															"height" : 18,	
															
															"children" : (
																{
																	"name" : "targetItemTitleTextLine",
																	"type" : "text",
																	
																	"x" : 40,
																	"y" : 2, 
																	
																	"text" : "Zielitem:",
																	
																	"outline" : 1,
																	
																	"color" : 0xffd8a055,
																	"text_horizontal_align" : "center",
																},	
															),
														},
														{
															"name" : "targetItemSlot",
															"type" : "slot",
																					
															"x" : 34 - 8,
															"y" : 25,

															"width" : 32,
															"height" : 32,
															
															"image" : "d:/ymir work/ui/public/slot_base.sub",
															"slot" : (
																{"index":0, "x":0, "y":0, "width":32, "height":32},
															),
														},
													),
												},
												{
													"name" : "timeItemBackground",
													"type" : "thinboard_circle",
													
													"x" : 80,
													"y" : 0,
													
													"width" : 80,
													"height" : 70,
													
													"children" : (
														{
															"name" : "timeItemTitleBackground",
															"type" : "thinboard_circle",
															
															"x" : 0,
															"y" : 0,
															
															"width" : 80,
															"height" : 18,	
															
															"children" : (
																{
																	"name" : "timeItemTitleTextLine",
																	"type" : "text",
																	
																	"x" : 40,
																	"y" : 2, 
																	
																	"text" : "Akzelerator:",
																	
																	"outline" : 1,
																	
																	"color" : 0xffd8a055,
																	"text_horizontal_align" : "center",
																},	
															),
														},
														{
															"name" : "timeItemSlot",
															"type" : "slot",
																					
															"x" : 34 - 8,
															"y" : 25,

															"width" : 32,
															"height" : 32,
															
															"image" : "d:/ymir work/ui/public/slot_base.sub",
															"slot" : (
																{"index":0, "x":0, "y":0, "width":32, "height":32},
															),
														},
													),
												},
												{
													"name" : "chanceItemBackground",
													"type" : "thinboard_circle",
													
													"x" : 80 + 80,
													"y" : 0,
													
													"width" : 80,
													"height" : 70,
													
													"children" : (
														{
															"name" : "chanceItemTitleBackground",
															"type" : "thinboard_circle",
															
															"x" : 0,
															"y" : 0,
															
															"width" : 80,
															"height" : 18,	
															
															"children" : (
																{
																	"name" : "chanceItemTitleTextLine",
																	"type" : "text",
																	
																	"x" : 40,
																	"y" : 2, 
																	
																	"text" : "Ergänzung:",
																	
																	"outline" : 1,
																	
																	"color" : 0xffd8a055,
																	"text_horizontal_align" : "center",
																},	
															),
														},
														{
															"name" : "chanceItemSlot",
															"type" : "slot",
																					
															"x" : 34 - 8,
															"y" : 25,

															"width" : 32,
															"height" : 32,
															
															"image" : "d:/ymir work/ui/public/slot_base.sub",
															"slot" : (
																{"index":0, "x":0, "y":0, "width":32, "height":32},
															),
														},														
													),
												},
												{
													"name" : "bottomBackground",
													"type" : "thinboard_circle",
															
													"x" : 0,
													"y" : 70,
															
													"width" : 240,
													"height" : 30,
													
													"children" : (
													
														{
															"name" : "researchInfoTextLine",
															"type" : "text",
																	
															"x" : 120,
															"y" : 8, 
																	
															"text" : "Erfolgschance: 100%, Forschungsdauer: 120 Min.",
																	
															"outline" : 1,
																	
															# "color" : 0xffd8a055,
															"text_horizontal_align" : "center",
														},	
													
													
													),
												},												
											),
										},
										{
											"name" : "BackToQuestListButton",
											"type" : "button",
													
											"x" : -55,
											"y" : 160 - 35,
													
											"text" : "Zurück",
											
											# "vertical_align" : "center",
											"horizontal_align" : "center", 
											
											"default_image" : "yamato_helpboard/normal_button_n.tga", 
											"over_image" : "yamato_helpboard/normal_button_h.tga",
											"down_image" : "yamato_helpboard/normal_button_p.tga",
											"disable_image" : "yamato_helpboard/normal_button_d.tga",				
										},	
									
										{
											"name" : "StartResearchButton",
											"type" : "button",
													
											"x" : 55,
											"y" : 160 - 35,
													
											"text" : "Untersuchen",
											
											# "vertical_align" : "center",
											"horizontal_align" : "center", 
											
											"default_image" : "yamato_helpboard/normal_button_n.tga", 
											"over_image" : "yamato_helpboard/normal_button_h.tga",
											"down_image" : "yamato_helpboard/normal_button_p.tga",
											"disable_image" : "yamato_helpboard/normal_button_d.tga",				
										},	
										# {
											# "name" : "StartResearchButton",
											# "type" : "button",
													
											# "x" : 0,
											# "y" : 160 - 35,
													
											# "text" : "Untersuchen",
											
											# # "vertical_align" : "center",
											# "horizontal_align" : "center", 
											
											# "default_image" : "yamato_helpboard/normal_button_n.tga", 
											# "over_image" : "yamato_helpboard/normal_button_h.tga",
											# "down_image" : "yamato_helpboard/normal_button_p.tga",
											# "disable_image" : "yamato_helpboard/normal_button_d.tga",				
										# },										
									),
								},
								# {
									# "name" : "BackToQuestListButton",
									# "type" : "button",
											
									# "x" : 0,
									# "y" : 406 - 30 + 1,
											
									# "text" : "Untersuchen",
									
									# # "vertical_align" : "center",
									# "horizontal_align" : "center", 
									
									# "default_image" : "yamato_helpboard/normal_button_n.tga", 
									# "over_image" : "yamato_helpboard/normal_button_h.tga",
									# "down_image" : "yamato_helpboard/normal_button_p.tga",
									# "disable_image" : "yamato_helpboard/normal_button_d.tga",				
								# },
							
							
							),
						},
					),
				},
			),
		},
	),
}

