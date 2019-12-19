import uiScriptLocale

WINDOW_WIDTH = 655
WINDOW_HEIGTH = 600

window = {
	"name" : "QuestMakerWindow",
	"style" : ("movable", "float",),

	"x" : 25,#SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60 - 230,
	"y" : 110,

	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30+40,

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
					"name" : "mainFunctionBackground",
					"type" : "thinboard_circle",
					"style" : ("movable","attach",),
					
					"x" : 25,
					"y" : 15,
					
					"width" : 200 + 430,
					"height" : 40,
					
					"children" : (
					
						{
							"name" : "NewButton",
							"type" : "button",
											
							"x" : 7,
							"y" : 7,
										
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "New Quest",
										
						},	
						{
							"name" : "MakeButton",
							"type" : "button",
											
							"x" : 7 + 98,
							"y" : 7,
										
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Make quest",
										
						},
						{
							"name" : "SaveImportButton",
							"type" : "button",
											
							"x" : 7 + 98 + 98,
							"y" : 7,
										
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Save ImportFile",
						},	
						{
							"name" : "LoadImportButton",
							"type" : "button",
											
							"x" : 7 + 98 + 98 + 98,
							"y" : 7,
										
							"default_image" : "yamato_helpboard/normal_button_n.tga",
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",

							"text" : "Load ImportFile",
						},							
					
					),
				},
				{
					"name" : "stateListBackground",
					"type" : "thinboard_circle",
					"style" : ("movable","attach",),
					
					"x" : 25,
					"y" : 15 + 40,
					
					"width" : 200,
					"height" : WINDOW_HEIGTH - 50,
				
					"children" : (
						{
							"name" : "stateListBox",
							"type" : "listbox",
							
							"x" : 0,
							"y" : 0,
							
							"width" : 200,
							"height" : WINDOW_HEIGTH - 50 - 70,
						},
						{
							"name" : "scrollBar",
							"type" : "small_thin_scrollbar",
							
							"x" : 185,
							"y" : 0,
							
							"size" : WINDOW_HEIGTH - 50 - 70,
						},
						{
							"name" : "bottomButtonBox",
							"type" : "thinboard_circle",
							"style" : ("movable","attach",),
							
							
							"x" : 0,
							"y" : WINDOW_HEIGTH - 50 - 70,
							
							
							"width" : 200,
							"height" : 70,
							
							"children" : (
							
								{
									"name" : "AddStateButton",
									"type" : "button",
											
									"x" : 20,
									"y" : 7,
										
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Hinzufügen",
										
								},
								{
									"name" : "DeleteStateButton",
									"type" : "button",
											
									"x" : 20,
									"y" : 7 + 30,
										
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Entfernen",
										
								},							
							
							),
						
						},
					
					
					
					),
				},
			
				{
					"name" : "stateEditBackground",
					"type" : "thinboard_circle",
					"style" : ("movable","attach",),
					
					"x" : 225,
					"y" : 15 + 40,
					
					"width" : 430,
					"height" : WINDOW_HEIGTH - 50,

					"children" : (
						{
							"name" : "stateTypeSTARTWindow",
							"type" : "window",
							"style" : ("movable","attach",),
							
							"x" : 0,
							"y" : 0,
							
							"width" : 430,
							"height" : WINDOW_HEIGTH - 50,
							
							"children" : (
								{
									"name" : "stateTypeSTARTTitle",
									"type" : "text",
									
									"x" : 15,
									"y" : 10,
									
									"text" : "STATE: start",
									
									"outline" : 1,
								},
								
								######################################################
								## MIN_LEVEL
								######################################################
								{
									"name" : "stateTypeSTARTMinLevelTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35,
									
									"text" : "Min-Level:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeSTARTMinLevelInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeSTARTMinLevelEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											"only_number" : 1,
											
											"text" : "1",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								######################################################
								## MAX_LEVEL	
								######################################################
								{
									"name" : "stateTypeSTARTMaxLevelTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25,
									
									"text" : "Max-Level:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeSTARTMaxLevelInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeSTARTMaxLevelEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											"only_number" : 1,
											
											"text" : "135",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								######################################################
								## eventflag	
								######################################################
								{
									"name" : "stateTypeSTARTEventFlagTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35,
									
									"text" : "Eventflag:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeSTARTEventFlagInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 35,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeSTARTEventFlagEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "flag-name",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeSTARTEventFlagInputBoardValue",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 101,
									"y" : 35 + 25 + 35,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeSTARTEventFlagEditLineValue",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											"only_number" : 1,
											"text" : "0",
													
											"width" : 30,
											"height" : 20,
										},
									),
								},
								######################################################
								## questFlag	
								######################################################
								{
									"name" : "stateTypeSTARTQuestFlagTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35 + 25,
									
									"text" : "Questflag:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeSTARTQuestFlagInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 35 + 25,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeSTARTQuestFlagEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "flag-name",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeSTARTQuestFlagInputBoardValue",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 101,
									"y" : 35 + 25 + 35 + 25,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeSTARTQuestFlagEditLineValue",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											"only_number" : 1,
											"text" : "0",
													
											"width" : 30,
											"height" : 20,
										},
									),
								},
								######################################################
								## questFlag	
								######################################################
								{
									"name" : "stateTypeSTARTQuestStateTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35 + 25 + 35,
									
									"text" : "Quest-State:",
									
									"outline" : 1,
								},	
								{
									"name" : "stateTypeSTARTQuestStateInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 35 + 25 + 35,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeSTARTQuestStateEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "0",
											"only_number" : 1,
													
											"width" : 30,
											"height" : 20,
										},
									),
								},	
								
								{
									"name" : "stateTypeSTARTSaveButton",
									"type" : "button",
											
									"x" : 25,
									"y" : 35 + 25 + 35 + 25 + 35 + 35,
										
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Save changes",
										
								},								
							),
							
						######################################################
						}, ## STATE_START_END
						######################################################
					
					
					),
			
				},
				{
					"name" : "stateSelectBackground",
					"type" : "bar",
					"style" : ("attach",),
					
					"x" : 25,
					"y" : 15,
					
					"width" : WINDOW_WIDTH - 20, 
					"height" : WINDOW_HEIGTH,
					
					"children" : (
						{
							"name" : "statepick_desc",
							"type" : "text",
							"x" : 0,
							"y" : 0 - 25 - 160,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"vertical_align" : "center",
							"text_vertical_align" : "center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Choose a QuestType for your new state!",
						},
						
						{
							"name" : "statePickNameBackground",
							"type" : "thinboard_circle",
							
							"x" : 0,
							"y" : 150 - 20,

							# "vertical_align" : "center",
							"horizontal_align" : "center",							

							"width" : 150,
							"height" : 19,
							
							"children" : (
								{
									"name" : "statePickNameEditLine",
									"type" : "editline",
													
									"x" : 4,
									"y" : 2,
													
									"input_limit" : 20,
									"text" : "",
													
									"width" : 150,
									"height" : 20,
								},
							),
						},
						
						{
							"name" : "statePickBackground",
							"type" : "thinboard_circle",
							
							"x" : 0,
							"y" : 170 - 20,

							# "vertical_align" : "center",
							"horizontal_align" : "center",							

							"width" : 150,
							"height" : 110,
							
							"children" : (
								{
									"name" : "statePickListBox",
									"type" : "listbox",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 150,
									"height" : 110,
								},
							),
						},
						{
							"name" : "statepick_add",
							"type" : "button",
									
							"x" : 0,
							"y" : 25 - 25 + 5 - 30 + 15,
									
							"text" : "Auswählen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},	
					
						{
							"name" : "statepick_close",
							"type" : "button",
									
							"x" : 0,
							"y" : 25 - 25 + 5 + 15,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},						
					),
				},
				{
					"name" : "makeNewQuestBackground",
					"type" : "bar",
					"style" : ("attach",),
					
					"x" : 25,
					"y" : 15,
					
					"width" : WINDOW_WIDTH - 20, 
					"height" : WINDOW_HEIGTH,
					
					"children" : (
						{
							"name" : "makeNewQuestInfo",
							"type" : "text",
							"x" : 0,
							"y" : 0 - 25 - 160,
							"horizontal_align" : "center", 
							"text_horizontal_align":"center",
							"vertical_align" : "center",
							"text_vertical_align" : "center",
							"color" : 0xffd8a055,
							"outline" : 1,
							"text" : "Are you sure you want do Make a new Quest? All Data will be purged!",
						},
						{
							"name" : "makeNewQuestYESButton",
							"type" : "button",
									
							"x" : -55,
							"y" : 0 - 25 - 130,
									
							"text" : "Ja",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},	
					
						{
							"name" : "makeNewQuestNOButton",
							"type" : "button",
									
							"x" : 55,
							"y" : 0 - 25 - 130,
									
							"text" : "Nein",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",				
						},	
					),
				},
			),
		},
	),
}

