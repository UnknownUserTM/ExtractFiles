import uiScriptLocale

WINDOW_WIDTH = 305
WINDOW_HEIGTH = 400

window = {
	"name" : "MountWindow",
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
					"name" : "MountHeadBackground",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 9,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : WINDOW_HEIGTH + 5,
					
					"children" : (
					
					
						{
							"name" : "mountWindowTitleBar",
							"type" : "horizontalbar",
							"style" : ("attach",),

							"x" : 1,
							"y" : 1,

							"width" : WINDOW_WIDTH - 10 - 2,
							"color" : "red",

							"children" :
							(
								{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":"Reittier-Information", "all_align":"center" },
							),
						},
					
						{
							"name" : "mountSkinImageBackground",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 15 + 15,
							
							"width" : 46,
							"height" : 46,
							
							"children" : (
								{
									"name" : "mountSkinImage",
									"type" : "image",
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_mount/mount.tga",
								
								
								},
							
							),
						},
						{
							"name" : "mountNameBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 45 + 10,
							"y" : 15 + 15,
							
							"width" : 210,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "mountNameTextLine",
									"type" : "text",
													
									"x" : 210 / 2,
									"y" : 4,
																						
									"text" : "Geisterweide",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),
						},					

						{
							"name" : "mountLevelBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 45 + 10,
							"y" : 15 + 22 + 2 + 15,
							
							"width" : 45,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "mountLevelTextLine",
									"type" : "text",
													
									"x" : 45 / 2,
									"y" : 4,
																						
									"text" : "8",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),
							
						},
						{
							"name" : "mountEXPBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 45 + 10 + 45,
							"y" : 15 + 22 + 2 + 15,
							
							"width" : 165,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "mountEXPTextLine",
									"type" : "text",
													
									"x" : 165 / 2,
									"y" : 4,
																						
									"text" : "8.741 / 831.000",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),
							
						},	

						{
							"name" : "mountStatusTitleBar",
							"type" : "horizontalbar",
							"style" : ("attach",),

							"x" : 1,
							"y" : 15 + 22 + 2 + 15 + 22 + 13,

							"width" : WINDOW_WIDTH - 10 - 2,

							"children" :
							(
								{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":"Status", "all_align":"center" },
								{ "name":"mountStatusPointTextLine", "type":"text", "x":108, "y":-1, "text":"verbleibend [10]", "all_align":"right" },
							),
						},
						
						{
						
							"name" : "lpImage",
							"type" : "image",
							
							"x" : 15,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5,
							
							
							"image" : "yamato_mount/lp.tga",
						},
						{
							"name" : "lpNumberBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 30 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5,
						
							"width" : 30,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "lpNumberTextLine",
									"type" : "text",
													
									"x" : 30 / 2,
									"y" : 4,
																						
									"text" : "8",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),
						
						},
						{
							"name" : "lpUpButtonBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 3,
							
							"width" : 16,
							"height" : 16,
							
							
							"children" : (
								{
									"name" : "lpPlusButton",
									"type" : "button",
									
									"x" : 2,
									"y" : 2,
									
									"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
									"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
									"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
									"disable_image" : "d:/ymir work/ui/game/windows/btn_plus_dis.sub",
								},
							),
						},
						{
							"name" : "lpDownButtonBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 3,
							
							"width" : 16,
							"height" : 16,
							
							
							"children" : (
								{
									"name" : "lpMinusButton",
									"type" : "button",
									
									"x" : 2,
									"y" : 2,
									
									"default_image" : "d:/ymir work/ui/game/windows/btn_minus_up.sub",
									"over_image" : "d:/ymir work/ui/game/windows/btn_minus_over.sub",
									"down_image" : "d:/ymir work/ui/game/windows/btn_minus_down.sub",
									"disable_image" : "d:/ymir work/ui/game/windows/btn_minus_dis.sub",
								},
							),
						},
						{
							"name" : "healthBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 + 22,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5,							
							
							"width" : 155,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "healthTitleTextLine",
									"type" : "text",
													
									"x" : 8,
									"y" : 4,
																						
									"text" : "Gesundheit:",
									# "text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),						
						},
						{
							"name" : "healthNumberBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 + 22 + 95,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5,							
							
							"width" : 60,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "healthNumberTextLine",
									"type" : "text",
													
									"x" : 60 / 2,
									"y" : 4,
																						
									"text" : "84 / 210",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),						
						},	
						# ######################################################### #

						{
						
							"name" : "apImage",
							"type" : "image",
							
							"x" : 15,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25,
							
							
							"image" : "yamato_mount/ap.tga",
						},
						{
							"name" : "apNumberBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 30 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25,
						
							"width" : 30,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "apNumberTextLine",
									"type" : "text",
													
									"x" : 30 / 2,
									"y" : 4,
																						
									"text" : "8",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),
						
						},
						{
							"name" : "lpapButtonBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 3 + 25,
							
							"width" : 16,
							"height" : 16,
							
							
							"children" : (
								{
									"name" : "apPlusButton",
									"type" : "button",
									
									"x" : 2,
									"y" : 2,
									
									"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
									"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
									"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
									"disable_image" : "d:/ymir work/ui/game/windows/btn_plus_dis.sub",
								},
							),
						},
						{
							"name" : "apDownButtonBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 3 + 25,
							
							"width" : 16,
							"height" : 16,
							
							
							"children" : (
								{
									"name" : "apMinusButton",
									"type" : "button",
									
									"x" : 2,
									"y" : 2,
									
									"default_image" : "d:/ymir work/ui/game/windows/btn_minus_up.sub",
									"over_image" : "d:/ymir work/ui/game/windows/btn_minus_over.sub",
									"down_image" : "d:/ymir work/ui/game/windows/btn_minus_down.sub",
									"disable_image" : "d:/ymir work/ui/game/windows/btn_minus_dis.sub",
								},
							),
						},
						{
							"name" : "staminaBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 + 22,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25,							
							
							"width" : 155,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "staminaTitleTextLine",
									"type" : "text",
													
									"x" : 8,
									"y" : 4,
																						
									"text" : "Ausdauer:",
									# "text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),						
						},
						{
							"name" : "staminaNumberBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 + 22 + 95,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25,							
							
							"width" : 60,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "staminaNumberTextLine",
									"type" : "text",
													
									"x" : 60 / 2,
									"y" : 4,
																						
									"text" : "98%",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),						
						},	
						# ######################################################### #

						{
						
							"name" : "epImage",
							"type" : "image",
							
							"x" : 15,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25,
							
							
							"image" : "yamato_mount/ep.tga",
						},
						{
							"name" : "epNumberBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 30 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25,
						
							"width" : 30,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "epNumberTextLine",
									"type" : "text",
													
									"x" : 30 / 2,
									"y" : 4,
																						
									"text" : "8",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),
						
						},
						{
							"name" : "epButtonBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 3 + 25 + 25,
							
							"width" : 16,
							"height" : 16,
							
							
							"children" : (
								{
									"name" : "epPlusButton",
									"type" : "button",
									
									"x" : 2,
									"y" : 2,
									
									"default_image" : "d:/ymir work/ui/game/windows/btn_plus_up.sub",
									"over_image" : "d:/ymir work/ui/game/windows/btn_plus_over.sub",
									"down_image" : "d:/ymir work/ui/game/windows/btn_plus_down.sub",
									"disable_image" : "d:/ymir work/ui/game/windows/btn_plus_dis.sub",
								},
							),
						},
						{
							"name" : "epDownButtonBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 - 5,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 3 + 25 + 25,
							
							"width" : 16,
							"height" : 16,
							
							
							"children" : (
								{
									"name" : "epMinusButton",
									"type" : "button",
									
									"x" : 2,
									"y" : 2,
									
									"default_image" : "d:/ymir work/ui/game/windows/btn_minus_up.sub",
									"over_image" : "d:/ymir work/ui/game/windows/btn_minus_over.sub",
									"down_image" : "d:/ymir work/ui/game/windows/btn_minus_down.sub",
									"disable_image" : "d:/ymir work/ui/game/windows/btn_minus_dis.sub",
								},
							),
						},
						{
							"name" : "expBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 + 22,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25,							
							
							"width" : 155,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "expTitleTextLine",
									"type" : "text",
													
									"x" : 8,
									"y" : 4,
																						
									"text" : "Intelligenz:",
									# "text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),						
						},
						{
							"name" : "expNumberBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 22 + 5 + 13 + 30+ 17 + 22 + 95,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25,							
							
							"width" : 60,
							"height" : 22,
							
							"children" : (
								{
												
									"name" : "expNumberTextLine",
									"type" : "text",
													
									"x" : 60 / 2,
									"y" : 4,
																						
									"text" : "10%",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
							
							),						
						},	
						
						{
							"name" : "mountRuneTitleBar",
							"type" : "horizontalbar",
							"style" : ("attach",),

							"x" : 1,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30,

							"width" : WINDOW_WIDTH - 10 - 2,

							"children" :
							(
								{ "name":"TitleName", "type":"text", "x":0, "y":-1, "text":"Kampfrunen", "all_align":"center" },
							),
						},

						{
							"name" : "battleRune_0_Background",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30 + 25,
						
							"width" : 45,
							"height" : 45,
							
							"children" : (
								{
									"name" : "battleRune_0_RuneImage",
									"type" : "image",
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_mount/demo_rune.tga",
								},
							),
						},
						{
							"name" : "battleRune_0_InfoBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 45,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30 + 25,
						
							"width" : 220,
							"height" : 45,
							
							"children" : (
								{
												
									"name" : "runeNameTextLine",
									"type" : "text",
													
									"x" : 220 / 2,
									"y" : 4,
																						
									"text" : "Seltene Stärkerune",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},	
								{
												
									"name" : "runeBonusTextLine",
									"type" : "text",
													
									"x" : 220 / 2,
									"y" : 4 + 18,
																						
									"text" : "Erhöht die Stärke beim Reiten um 12.",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},							
							),	
							
						},
						
						{
							"name" : "battleRune_1_Background",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30 + 25 + 45 + 5,
						
							"width" : 45,
							"height" : 45,
							
							"children" : (
								{
									"name" : "battleRune_1_RuneImage",
									"type" : "image",
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_mount/quest.tga",
								},
							),
						},
						{
							"name" : "battleRune_1_InfoBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 45,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30 + 25 + 45 + 5,
						
							"width" : 220,
							"height" : 45,
							
							"children" : (
								{
												
									"name" : "runeQuestTextLine",
									"type" : "text",
													
									"x" : 220 / 2,
									"y" : 4,
																						
									"text" : "Macht der Runen II verfügbar!",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},

								{
									"name" : "questButton",
									"type" : "button",
											
									"x" : (220 / 2) - (95 / 2),
									"y" : 4 + 14,
									
									"default_image" : "yamato_helpboard/normal_button_n.tga",
									"over_image" : "yamato_helpboard/normal_button_h.tga",
									"down_image" : "yamato_helpboard/normal_button_p.tga",
									"disable_image" : "yamato_helpboard/normal_button_d.tga",

									"text" : "Quest starten!",
										
								},															
							),	
							
						},






						{
							"name" : "battleRune_2_Background",
							"type" : "thinboard_circle",
							
							"x" : 15,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30 + 25 + 45 + 5 + 45 + 5,
						
							"width" : 45,
							"height" : 45,
							
							"children" : (
								{
									"name" : "battleRune_2_RuneImage",
									"type" : "image",
									
									"x" : 0,
									"y" : 0,
									
									"image" : "yamato_mount/90.tga",
								},
							),
						},
						{
							"name" : "battleRune_2_InfoBackground",
							"type" : "thinboard_circle",
							
							"x" : 15 + 45,
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30 + 25 + 45 + 5 + 45 + 5,
						
							"width" : 220,
							"height" : 45,
							
							"children" : (
								{
												
									"name" : "runeName2TextLine",
									"type" : "text",
													
									"x" : 220 / 2,
									"y" : 4,
																						
									"text" : "Macht der Runen III",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},

								{
												
									"name" : "runeName3TextLine",
									"type" : "text",
													
									"x" : 220 / 2,
									"y" : 4 + 18,
																						
									"text" : "Erreiche Lv.90 um die Quest zu starten.",
									"text_horizontal_align" : "center",
									"outline" : 1,
								},															
							),	
							
						},

						{
							"name" : "questButton",
							"type" : "button",
											
							"x" : ((WINDOW_WIDTH - 10) / 2) - (161 / 2),
							"y" : 15 + 22 + 2 + 15 + 22 + 13 + 15 + 5 + 25 + 25 + 30 + 25 + 45 + 5 + 45 + 5 + 45 + 10,
									
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",

							"text" : "Reittier rufen!",
										
						},

						
					),
				},
			),
		},
	),
}

