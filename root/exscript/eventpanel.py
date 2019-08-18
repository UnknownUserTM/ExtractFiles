import uiScriptLocale

WINDOW_WIDTH = 550
WINDOW_HEIGTH = 300

window = {
	"name" : "EventPanelWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60 - 230,
	"y" : 110,

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
					"name" : "nav_board",
					"type" : "board",
					
					"x" : 15,
					"y" : 15,
					
					"width" : 210,
					"height" : WINDOW_HEIGTH+35,
					
					"no_bottom" : 1,
				
					"children" : (
					
						{
							"name" : "event_button_0",
							"type" : "button",
									
							"x" : 25,
							"y" : 15,
								
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Temp. Drop-Event",
						},
						{
							"name" : "event_button_1",
							"type" : "button",
									
							"x" : 25,
							"y" : 15 + 30,
								
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "OX-Event",
						},
						{
							"name" : "event_button_2",
							"type" : "button",
									
							"x" : 25,
							"y" : 15 + 30 + 30,
								
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Treasure-Hunt",
						},
						{
							"name" : "event_button_3",
							"type" : "button",
									
							"x" : 25,
							"y" : 15 + 30 + 30 + 30,
								
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Moonlight-Treasure",
						},					
						{
							"name" : "event_button_4",
							"type" : "button",
									
							"x" : 25,
							"y" : 15 + 30 + 30 + 30 + 30,
								
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Fish-Event",
						},
						{
							"name" : "event_button_5",
							"type" : "button",
									
							"x" : 25,
							"y" : 15 + 30 + 30 + 30 + 30 + 30,
								
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Castle-Siege",
						},	
						{
							"name" : "event_button_6",
							"type" : "button",
									
							"x" : 25,
							"y" : 15 + 30 + 30 + 30 + 30 + 30 + 30,
								
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Empire Pillage",
						},							
					),
				
				},
				{
					"name" : "temp_event_window",
					"type" : "window",
					
					"x" : 15 + 210 + 5 - 15 + 5,
					"y" : 15 + 5 - 3,
					
					"width" : 335,
					"height" : WINDOW_HEIGTH - 10,
				
					"children" : (
						{
							"name" : "te_background_bar",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : 335,
							"height" : WINDOW_HEIGTH - 10,	
							
							"children" : (
							
								{
									"name" : "tempDropTitleTextLine",
									"type" : "text",
									"x" : 0,
									"y" : 8,
									"horizontal_align" : "center", 
									"text_horizontal_align":"center",
									"color" : 0xffd8a055,
									"outline" : 1,
									"text" : "Temp. Drop-Event:",							
								},
								{
									"name" : "tempDropTitleTextLine_Line",
									"type" : "line",
									
									"x" : 17,
									"y" : 23,
									"width" : 300,
									"height" : 0,
									"color" : 0xffd8a055,
								},
								{
									"name" : "addNewEventWindow",
									"type" : "window",
									
									"x" : 17,
									"y" : 25,
									
									"width" : 300,
									"height" : 230,
									
									
									"children" : (
										{
											"name" : "tempDropEvent_Add_NameTextLine",
											"type" : "text",
											"x" : 8,
											"y" : 15,
											"color" : 0xffd8a055,
											"outline" : 1,
											"text" : "Event-Name :",							
										},
										{
											"name" : "tempDropEvent_Add_TargetVnumTextLine",
											"type" : "text",
											"x" : 8,
											"y" : 15 + 30,
											"color" : 0xffd8a055,
											"outline" : 1,
											"text" : "Target-Vnum :",							
										},
										{
											"name" : "tempDropEvent_Add_ItemVnumTextLine",
											"type" : "text",
											"x" : 8,
											"y" : 15 + 30 + 30,
											"color" : 0xffd8a055,
											"outline" : 1,
											"text" : "Item-Vnum :",							
										},
										{
											"name" : "tempDropEvent_Add_TimeTextLine",
											"type" : "text",
											"x" : 8,
											"y" : 15 + 30 + 30 + 30,
											"color" : 0xffd8a055,
											"outline" : 1,
											"text" : "Duration :",							
										},
										{
											"name" : "tempDropEvent_Add_ChanceTextLine",
											"type" : "text",
											"x" : 8,
											"y" : 15 + 30 + 30 + 30 + 30,
											"color" : 0xffd8a055,
											"outline" : 1,
											"text" : "Drop-Chance :",							
										},
										{
											"name" : "tempDropEvent_Add_LevelRangeTextLine",
											"type" : "text",
											"x" : 8,
											"y" : 15 + 30 + 30 + 30 + 30 + 30,
											"color" : 0xffd8a055,
											"outline" : 1,
											"text" : "Level-Range :",							
										},
										{
											"name" : "tempDropEvent_Add_NameEditLineBoard",
											"type" : "thinboard_circle",
											
											"x" : 8 + 100,
											"y" : 15,
											
											"width" : 100,
											"height" : 18,
																						
											"children" : (
												{
													"name" : "tempDropEvent_Add_NameEditLine",
													"type" : "editline",
													
													"x" : 4,
													"y" : 2,
													
													"input_limit" : 20,
													
													"width" : 100,
													"height" : 20,
												},
											),
										},
										{
											"name" : "tempDropEvent_Add_TargetEditLineBoard",
											"type" : "thinboard_circle",
											
											"x" : 8 + 100,
											"y" : 15 + 30,
											
											"width" : 100,
											"height" : 18,
																						
											"children" : (
												{
													"name" : "tempDropEvent_Add_TargetEditLine",
													"type" : "editline",
													
													"x" : 4,
													"y" : 2,
													
													"input_limit" : 20,
													"only_number" : 1,
													
													"width" : 100,
													"height" : 20,
												},
											),
										},										
										{
											"name" : "tempDropEvent_Add_VnumEditLineBoard",
											"type" : "thinboard_circle",
											
											"x" : 8 + 100,
											"y" : 15 + 30 + 30,
											
											"width" : 100,
											"height" : 18,
																						
											"children" : (
												{
													"name" : "tempDropEvent_Add_VnumEditLine",
													"type" : "editline",
													
													"x" : 4,
													"y" : 2,
													
													"input_limit" : 20,
													"only_number" : 1,
													
													"width" : 100,
													"height" : 20,
												},
											),
										},										
										{
											"name" : "tempDropEvent_Add_TimeEditLineBoard",
											"type" : "thinboard_circle",
											
											"x" : 8 + 100,
											"y" : 15 + 30 + 30 + 30,
											
											"width" : 100,
											"height" : 18,
																						
											"children" : (
												{
													"name" : "tempDropEvent_Add_TimeEditLine",
													"type" : "editline",
													
													"x" : 4,
													"y" : 2,
													
													"input_limit" : 20,
													"only_number" : 1,
													
													"width" : 100,
													"height" : 20,
												},
											),
										},	
										{
											"name" : "tempDropEvent_Add_ChanceEditLineBoard",
											"type" : "thinboard_circle",
											
											"x" : 8 + 100,
											"y" : 15 + 30 + 30 + 30 + 30,
											
											"width" : 100,
											"height" : 18,
																						
											"children" : (
												{
													"name" : "tempDropEvent_Add_ChanceEditLine",
													"type" : "editline",
													
													"x" : 4,
													"y" : 2,
													
													"input_limit" : 20,
													"only_number" : 1,
													"width" : 100,
													"height" : 20,
												},
											),
										},
										
										{
											"name" : "tempDropEvent_Add_MinLevelEditLineBoard",
											"type" : "thinboard_circle",
											
											"x" : 8 + 100,
											"y" : 15 + 30 + 30 + 30 + 30 + 30,
											
											"width" : 50,
											"height" : 18,
																						
											"children" : (
												{
													"name" : "tempDropEvent_Add_MinLevelEditLine",
													"type" : "editline",
													
													"x" : 4,
													"y" : 2,
													
													"input_limit" : 3,
													
													"only_number" : 1,
													
													"text" : 1,
													
													"width" : 50,
													"height" : 20,
												},
											),
										},
										{
											"name" : "tempDropEvent_Add_MaxLevelEditLineBoard",
											"type" : "thinboard_circle",
											
											"x" : 8 + 100 + 50,
											"y" : 15 + 30 + 30 + 30 + 30 + 30,
											
											"width" : 50,
											"height" : 18,
																						
											"children" : (
												{
													"name" : "tempDropEvent_Add_MaxLevelEditLine",
													"type" : "editline",
													
													"x" : 4,
													"y" : 2,
													
													"input_limit" : 3,
													
													"only_number" : 1,
													
													"text" : 135,
													
													"width" : 50,
													"height" : 20,
												},
											),
										},
										{
											"name" : "tempDropEvent_Add_SendButton",
											"type" : "button",
													
											"x" : 8,
											"y" : 15 + 30 + 30 + 30 + 40 + 30 + 15,
												
											"default_image" : "yamato_helpboard/normal_button_n.tga",
											"over_image" : "yamato_helpboard/normal_button_h.tga",
											"down_image" : "yamato_helpboard/normal_button_p.tga",
											"disable_image" : "yamato_helpboard/normal_button_d.tga",

											"text" : "Add new Event",
												
										},
										{
											"name" : "tempDropEvent_Add_ClearButton",
											"type" : "button",
													
											"x" : 8 + 95,
											"y" : 15 + 30 + 30 + 30 + 40 + 30 + 15,
												
											"default_image" : "yamato_helpboard/normal_button_n.tga",
											"over_image" : "yamato_helpboard/normal_button_h.tga",
											"down_image" : "yamato_helpboard/normal_button_p.tga",
											"disable_image" : "yamato_helpboard/normal_button_d.tga",

											"text" : "Clear",
										},	
										{
											"name" : "tempDropEvent_Add_DropTypeButton",
											"type" : "button",
													
											"x" : 8 + 95 + 95,
											"y" : 15 + 30 + 30 + 30 + 40 + 30 + 15,
												
											"default_image" : "yamato_helpboard/normal_button_n.tga",
											"over_image" : "yamato_helpboard/normal_button_h.tga",
											"down_image" : "yamato_helpboard/normal_button_p.tga",
											"disable_image" : "yamato_helpboard/normal_button_d.tga",

											"text" : "Single-Target",
										},
									),
								},
								{
									"name" : "manageEventWindow",
									"type" : "window",
									
									"x" : 17,
									"y" : 25,
									
									"width" : 300,
									"height" : 230,
									
									
									"children" : (
									
										{
											"name" : "tempDropEvent_MANAGE_ListBox",
											"type" : "listbox",
											
											"x" : 8,
											"y" : 15,
											
											"width" : 270,
											"height" : 15 + 30 + 30 + 30 + 40 + 30,
										},
										
										{
											"name" : "tempDropEvent_MANAGE_Scrollbar",
											"type" : "scrollbar",
											
											"x" : 270,
											"y" : 15,
											
											"size" : 15 + 30 + 30 + 30 + 40 + 30,
										
										
										},
									
										{
											"name" : "tempDropEvent_MANAGE_LoadButton",
											"type" : "button",
													
											"x" : 8,
											"y" : 15 + 30 + 30 + 30 + 40 + 30 + 15,
												
											"default_image" : "yamato_helpboard/normal_button_n.tga",
											"over_image" : "yamato_helpboard/normal_button_h.tga",
											"down_image" : "yamato_helpboard/normal_button_p.tga",
											"disable_image" : "yamato_helpboard/normal_button_d.tga",

											"text" : "Load",
												
										},
										{
											"name" : "tempDropEvent_MANAGE_DeleteButton",
											"type" : "button",
													
											"x" : 8 + 95,
											"y" : 15 + 30 + 30 + 30 + 40 + 30 + 15,
												
											"default_image" : "yamato_helpboard/normal_button_n.tga",
											"over_image" : "yamato_helpboard/normal_button_h.tga",
											"down_image" : "yamato_helpboard/normal_button_p.tga",
											"disable_image" : "yamato_helpboard/normal_button_d.tga",

											"text" : "Delete",
										},	
									
									
									),
								},
									
								{
									"name" : "tempDropBottmLine",
									"type" : "line",
									
									"x" : 17,
									"y" : 15 + 205 + 40 - 5,
									"width" : 300,
									"height" : 0,
									"color" : 0xffd8a055,
								},
								{
									"name" : "addTempEventButton",
									"type" : "button",
											
									"x" : 17,
									"y" : 15 + 205 + 40,
										
									"default_image" : "yamato_helpboard/normal_button_n.tga",
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",

									"text" : "Add",
										
								},								
								{
									"name" : "manageTempEventButton",
									"type" : "button",
											
									"x" : 17 + 95,
									"y" : 15 + 205 + 40,
										
									"default_image" : "yamato_helpboard/normal_button_n.tga",
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",

									"text" : "Manage",
										
								},								
							),
						},
					),
				},
			),
		},
	),
}

