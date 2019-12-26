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

							"text" : "Neue Quest",
										
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

							"text" : "Quest erstellen",
										
						},
						{
							"name" : "statusMessage",
							"type" : "text",
							
							"x" : 15,
							"y" : 0,
							
							"text" : "Bereit!",
							"outline" : 1,
						
							"horizontal_align" : "right", 
							"text_horizontal_align":"right",
							"vertical_align" : "center",
							"text_vertical_align" : "center",						
						
						},
						# {
							# "name" : "SaveImportButton",
							# "type" : "button",
											
							# "x" : 7 + 98 + 98,
							# "y" : 7,
										
							# "default_image" : "yamato_helpboard/normal_button_n.tga",
							# "over_image" : "yamato_helpboard/normal_button_h.tga",
							# "down_image" : "yamato_helpboard/normal_button_p.tga",
							# "disable_image" : "yamato_helpboard/normal_button_d.tga",

							# "text" : "Save ImportFile",
						# },	
						# {
							# "name" : "LoadImportButton",
							# "type" : "button",
											
							# "x" : 7 + 98 + 98 + 98,
							# "y" : 7,
										
							# "default_image" : "yamato_helpboard/normal_button_n.tga",
							# "over_image" : "yamato_helpboard/normal_button_h.tga",
							# "down_image" : "yamato_helpboard/normal_button_p.tga",
							# "disable_image" : "yamato_helpboard/normal_button_d.tga",

							# "text" : "Load ImportFile",
						# },							
					
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
							"name" : "stateTypeINITWindow",
							"type" : "window",
							"style" : ("movable","attach",),
							
							"x" : 0,
							"y" : 0,
							
							"width" : 430,
							"height" : WINDOW_HEIGTH - 50,
							
							"children" : (
								{
									"name" : "stateTypeINITTitle",
									"type" : "text",
									
									"x" : 15,
									"y" : 10,
									
									"text" : "STATE: INITIALIZER",
									
									"outline" : 1,
								},
								
								######################################################
								## MIN_LEVEL
								######################################################
								{
									"name" : "stateTypeINITMinLevelTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35,
									
									"text" : "Min-Level:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeINITMinLevelInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITMinLevelEditLine",
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
									"name" : "stateTypeINITMaxLevelTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25,
									
									"text" : "Max-Level:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeINITMaxLevelInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITMaxLevelEditLine",
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
								## JobSelect	
								######################################################								
								{
									"name" : "stateTypeINITJobSelectTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35,
									
									"text" : "Klasse:",
									
									"outline" : 1,
								},

								{
									"name" : "stateTypeINITJobSelectAllTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35,
									
									"text" : "Für Alle:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITJobSelectAllButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},
								## Krieger
								{
									"name" : "stateTypeINITJobSelectWarriorTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35 + 25,
									
									"text" : "Für Krieger:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITJobSelectWarriorButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 + 25 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},
								## Ninja
								{
									"name" : "stateTypeINITJobSelectNinjaTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35 + 25 + 25,
									
									"text" : "Für Ninja:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITJobSelectNinjaButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},
						
								## Sura
								{
									"name" : "stateTypeINITJobSelectSuraTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25,
									
									"text" : "Für Sura:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITJobSelectSuraButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},
								
								## Shaman
								{
									"name" : "stateTypeINITJobSelectShamanTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25,
									
									"text" : "Für Schamanen:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITJobSelectShamanButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},
								######################################################
								## SexSelect	
								######################################################								
								{
									"name" : "stateTypeINITSexSelectTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 + 35,
									
									"text" : "Geschlecht:",
									
									"outline" : 1,
								},

								{
									"name" : "stateTypeINITSexSelectAllTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 + 35 + 25,
									
									"text" : "Alle:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITSexSelectAllButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 + 35 + 25 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},	

								{
									"name" : "stateTypeINITSexSelectMaleTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 + 35 + 25 + 25,
									
									"text" : "Männlich:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITSexSelectMaleButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 + 35 + 25 + 25 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},
								
								{
									"name" : "stateTypeINITSexSelectFemaleTitle",
									"type" : "text",
									
									"x" : 35,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 + 35 + 25 + 25 + 25,
									
									"text" : "Weiblich:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITSexSelectFemaleButton",
									"type" : "button",
											
									"x" : 35 + 80,
									"y" : 35 + 25 + 25 + 35 + 25 + 25 + 25 + 25 + 35 + 25 + 25 + 25 - 3,
																			
									"default_image" : "yamato_button/radio_n.tga",
									"over_image" : "yamato_button/radio_h.tga",
									"down_image" : "yamato_button/radio_n.tga",
									"disable_image" : "yamato_button/radio_p.tga",
								},

								
								######################################################
								## eventflag	
								######################################################
								{
									"name" : "stateTypeINITEventFlagTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35 + 270,
									
									"text" : "Eventflag:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeINITEventFlagInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 35 + 270,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITEventFlagEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "no_flag",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeINITEventFlagInputBoardValue",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 101,
									"y" : 35 + 25 + 35 + 270,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITEventFlagEditLineValue",
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
									"name" : "stateTypeINITQuestFlagTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35 + 25 + 270,
									
									"text" : "Questflag:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeINITQuestFlagQuestInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 35 + 25 + 270,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITQuestFlagQuestEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "no_quest",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeINITQuestFlagFlagInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 100,
									"y" : 35 + 25 + 35 + 25 + 270,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITQuestFlagFlagEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "no_flag",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeINITQuestFlagInputBoardValue",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 101 + 101,
									"y" : 35 + 25 + 35 + 25 + 270,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITQuestFlagEditLineValue",
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
								## OtherQuestProgress	
								######################################################
								{
									"name" : "stateTypeINITOtherQuestProgressTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35 + 25 + 270 + 35,
									
									"text" : "Anderer Questfortschritt:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeINITOtherQuestProgressInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 60,
									"y" : 35 + 25 + 35 + 25 + 270 + 35,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITOtherQuestProgressEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "quest_name",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeINITOtherQuestProgressInputBoardValue",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 101 + 60,
									"y" : 35 + 25 + 35 + 25 + 270 + 35,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITOtherQuestProgressEditLineValue",
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
								## CheckOtherQuestDone	
								######################################################
								{
									"name" : "stateTypeINITCheckOtherQuestDoneTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 35 + 25 + 270 + 35 + 25,
									
									"text" : "Andere Quest abgeschlossen?:",
									
									"outline" : 1,
								},								
								{
									"name" : "stateTypeINITCheckOtherQuestDoneInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 60,
									"y" : 35 + 25 + 35 + 25 + 270 + 35 + 25,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINITCheckOtherQuestDoneEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											
											"text" : "quest_name",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},	
								
								{
									"name" : "stateTypeINITSaveButton",
									"type" : "button",
											
									"x" : 25,
									"y" : 35 + 25 + 35 + 25 + 35 + 35 + 270 + 25,
										
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Speichern",
										
								},								
							),
							
						######################################################
						}, ## STATE_START_END
						######################################################


						{
							"name" : "stateTypeINTROWindow",
							"type" : "window",
							"style" : ("movable","attach",),
							
							"x" : 0,
							"y" : 0,
							
							"width" : 430,
							"height" : WINDOW_HEIGTH - 50,
							
							"children" : (
								{
									"name" : "stateTypeINTROTitle",
									"type" : "text",
									
									"x" : 15,
									"y" : 10,
									
									"text" : "STATE: Intro",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINITMinLevelTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35,
									
									"text" : "Quest Typ:",
									
									"outline" : 1,
								},	
								{
									"name" : "stateTypeINTROTabInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINTROTabEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											"only_number" : 1,
											
											"text" : "Hauptquest",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeINTROTargetTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25,
									
									"text" : "Ziel (NPC Vnum):",
									
									"outline" : 1,
								},	
								{
									"name" : "stateTypeINTROTargetInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25,
											
									"width" : 100,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINTROTargetEditLine",
											"type" : "editline",
													
											"x" : 4,
											"y" : 2,
													
											"input_limit" : 20,
											"only_number" : 1,
											
											"text" : "0",
													
											"width" : 100,
											"height" : 20,
										},
									),
								},
								{
									"name" : "stateTypeINTROLetterTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 25,
									
									"text" : "Brief:",
									
									"outline" : 1,
								},	
								{
									"name" : "stateTypeINTROLetterInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 25,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINTROLetterTitleTextEditLine",
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
								{
									"name" : "stateTypeINTROLetterTextInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 31,
									"y" : 35 + 25 + 25,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINTROLetterTextEditLine",
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
								
								{
									"name" : "stateTypeINTRODialogTitle",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 25 + 35,
									
									"text" : "Dialog:",
									
									"outline" : 1,
								},	
								{
									"name" : "stateTypeINTRODialogInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 25 + 35,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINTRODialogTitleTextEditLine",
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
								{
									"name" : "stateTypeINTRODialogTextInputBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100 + 31,
									"y" : 35 + 25 + 25 + 35,
											
									"width" : 30,
									"height" : 18,
																						
									"children" : (
										{
											"name" : "stateTypeINTRODialogTextEditLine",
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
				
								{
									"name" : "stateTypeINTROTargetList",
									"type" : "text",
									
									"x" : 25,
									"y" : 35 + 25 + 25 + 35 + 35,
									
									"text" : "Ziele:",
									
									"outline" : 1,
								},
								{
									"name" : "stateTypeINTROTargetListBoard",
									"type" : "thinboard_circle",
											
									"x" : 8 + 100,
									"y" : 35 + 25 + 25 + 35 + 35,
											
									"width" : 250,
									"height" : 130,
								},
								
							),
						},
					
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

