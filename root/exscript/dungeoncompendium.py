import uiScriptLocale

WINDOW_WIDTH = 570
WINDOW_HEIGTH = 498

INFO_BOARD_WIDTH = 200

window = {
	"name" : "DungeonGuideWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - WINDOW_WIDTH - 60,
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
					"name" : "selectBackground",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 9,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : WINDOW_HEIGTH + 5,
					
					"children" : (
						{
							"name" : "dungeonScrollBar",
							"type" : "small_thin_scrollbar",
							
							"x" : WINDOW_WIDTH - 10 - 15 + 1,
							"y" : 0,
							
							"size" : WINDOW_HEIGTH + 5,
						},					
						{
							"name" : "dungeon_0",
							"type" : "button",
											
							"x" : 5,
							"y" : 5,
									
							"default_image" : "yamato_dungeoncompendium\dungeon_image/dungeon_dragon_n.tga",
							"over_image" : "yamato_dungeoncompendium\dungeon_image/dungeon_dragon_h.tga",
							"down_image" : "yamato_dungeoncompendium\dungeon_image/dungeon_dragon_p.tga",
							
							"children" : (
								{
									"name" : "dungeon_0_title",
									"type" : "text",
									
									"x" : 15,
									"y" : 0 - 3,
									
									"fontsize" : "LARGE",
									
									"vertical_align" : "center",
									"text_vertical_align" : "center",
									"text" : "Verlies des Roten Drachen",
									"outline" : 1,
								},
							),
						},
					),
				},
			
				{
					"name" : "infoBackground",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 9,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : WINDOW_HEIGTH + 5,
					
					"children" : (
					
					
						{
							"name" : "dungeonDescBox",
							"type" : "ruleslistbox",
							
							"x" : 5,
							"y" : 0,
							
							"width" : WINDOW_WIDTH - 10 - INFO_BOARD_WIDTH - 5,
							"height" : WINDOW_HEIGTH + 5,
						},
						{
							"name" : "descScrollBar",
							"type" : "small_thin_scrollbar",
							
							"x" : WINDOW_WIDTH - 10 - INFO_BOARD_WIDTH - 15 + 1,
							"y" : 0,
							
							"size" : WINDOW_HEIGTH + 5,
						},
					
						{
							"name" : "dungeonInfoBoard",
							"type" : "thinboard_circle",
							
							"x" : WINDOW_WIDTH - 10 - INFO_BOARD_WIDTH,
							"y" : 0,
							
							"width" : INFO_BOARD_WIDTH,
							"height" : WINDOW_HEIGTH + 5,
							
							"children" : (
								{
									"name" : "informationHorizontalBar",
									"type" : "horizontalbar",
									
									"x" : 1,
									"y" : 1,
									
									"width" : INFO_BOARD_WIDTH - 2,
								},
								{
									"name" : "informationTitleTextLine",
									"type" : "text",
									
									"x" : INFO_BOARD_WIDTH / 2,
									"y" : 3,
									
									"color" : 0xffd8a055,
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Informationen:",
								},	
								{
									"name" : "minLevelBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "minLevelTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Min. Level:",
										},									
										{
											"name" : "minLevelValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "30",
										},										
									),
								},

								{
									"name" : "maxLevelBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "maxLevelTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Max. Level:",
										},									
										{
											"name" : "maxLevelValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "90",
										},										
									),
								},

								{
									"name" : "partyBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "partyTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Gruppe benötigt:",
										},									
										{
											"name" : "partyValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "Ja",
										},										
									),
								},



								{
									"name" : "cooldownBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "cooldownTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Abklingzeit:",
										},									
										{
											"name" : "cooldownValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "7 Jahre",
										},										
									),
								},
								
								{
									"name" : "effBonusBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "effBonusTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Effektiver Bonus:",
										},									
										{
											"name" : "effBonusValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "Untote",
										},										
									),
								},
								
								{
									"name" : "defBonusBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "defBonusTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Widerstand:",
										},									
										{
											"name" : "defBonusValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "Dunkelheit",
										},										
									),
								},

								{
									"name" : "dungeonPointsBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "dungeonPointsTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Dungeonpoints:",
										},									
										{
											"name" : "dungeonPointsValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "|Eemoji/dungeon_icon|e 300",
										},										
									),
								},

								{
									"name" : "itemBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 40,
								
									"children" : (
										{
											"name" : "itemTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 0,
											
											# "horizontal_align" : "left",
											"vertical_align" : "center",
											"text_vertical_align" : "center",
											"outline" : 1,
											"text" : "Benötigter Gegenstand:",
										},
										{
											"name" : "itemBackgroundSlot",
											"type" : "thinboard_circle",
											
											"x" : INFO_BOARD_WIDTH - 10 - 32 - 4,
											"y" : 4,
											
											"width" : 32,
											"height" : 32,
											
											"children" : (
												{
													"name" : "itemSlot",
													"type" : "slot",
													
													"x" : 0,
													"y" : 0,
													
													"width" : 32,
													"height" : 32,
													
													"slot" : (
														{"index":0, "x":0, "y":0, "width":32, "height":32},
													),
												},
												{
													"name" : "itemSlotCoverIcon",
													"type" : "image",
													
													"x" : 0,
													"y" : 0,
													
													"image" : "yamato_dungeoncompendium/no_item.tga",
												},
											),
										},
									),
								},


								{
									"name" : "statisticHorizontalBar",
									"type" : "horizontalbar",
									
									"x" : 1,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22+ 42 + 25,
									
									"width" : INFO_BOARD_WIDTH - 2,
								},
								{
									"name" : "statisticTitleTextLine",
									"type" : "text",
									
									"x" : INFO_BOARD_WIDTH / 2,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22+ 42 + 25 + 3,
									
									"color" : 0xffd8a055,
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Statistik (Persöhnlich):",
								},
								{
									"name" : "personalCooldownBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "personalCooldownTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Abklingzeit:",
										},									
										{
											"name" : "personalCooldownValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "Bereit!",
										},										
									),
								},					
								{
									"name" : "personalCountBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "personalCountTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Abgeschlossen:",
										},									
										{
											"name" : "personalCountValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "8",
										},										
									),
								},
								{
									"name" : "personalBestTimeBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "personalBestTimeTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Bestzeit:",
										},									
										{
											"name" : "personalBestTimeValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "8 Min. 38 Sek.",
										},										
									),
								},
								{
									"name" : "personalMonsterKillCountBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "personalMonsterKillCountTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Monster-Kills:",
										},									
										{
											"name" : "personalMonsterKillCountValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "17.832",
										},										
									),
								},
								{
									"name" : "personalBossKillCountBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "personalBossKillCountTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Boss-Kills:",
										},									
										{
											"name" : "personalBossKillCountValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "28",
										},										
									),
								},
								{
									"name" : "personalStoneKillCountBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "personalStoneKillCountTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Metin-Kills:",
										},									
										{
											"name" : "personalStoneKillCountValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "284",
										},										
									),
								},	

								{
									"name" : "statisticServerHorizontalBar",
									"type" : "horizontalbar",
									
									"x" : 1,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22 + 22 + 22 + 25,
									
									"width" : INFO_BOARD_WIDTH - 2,
								},
								{
									"name" : "statisticServerTitleTextLine",
									"type" : "text",
									
									"x" : INFO_BOARD_WIDTH / 2,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22 + 22 + 22 + 25 + 3,
									
									"color" : 0xffd8a055,
									"text_horizontal_align" : "center",
									"outline" : 1,
									"text" : "Statistik (Server):",
								},


								{
									"name" : "serverCountBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22 + 22 + 22 + 25 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "serverCountTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Abgeschlossen:",
										},									
										{
											"name" : "serverCountValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "284.322",
										},										
									),
								},
								{
									"name" : "serverBestTimeBackground",
									"type" : "thinboard_circle",
									
									"x" : 5,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22 + 22 + 22 + 25 + 22 + 22,
									
									"width" : INFO_BOARD_WIDTH - 10,
									"height" : 20,
								
									"children" : (
										{
											"name" : "serverBestTimeTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "left",
											"outline" : 1,
											"text" : "Bestzeit:",
										},									
										{
											"name" : "serverBestTimeValueTextLine",
											"type" : "text",
											
											"x" : 5,
											"y" : 3,
											
											"horizontal_align" : "right",
											"text_horizontal_align":"right",
											"outline" : 1,
											"text" : "4 Min. 3 Sek. von Geisterweide",
										},										
									),
								},	

								{
									"name" : "warpToDungeonButton",
									"type" : "button",
											
									"x" : 0,
									"y" : 20 + 22 + 22 + 22 + 22 + 22 + 22 + 42 + 25 + 22 + 22 + 22 + 22 + 22 + 22 + 25 + 22 + 22 + 25 + 10,
									
									"horizontal_align" : "center",
										
									"default_image" : "yamato_helpboard/wide_button_n.tga",
									"over_image" : "yamato_helpboard/wide_button_h.tga",
									"down_image" : "yamato_helpboard/wide_button_p.tga",
									"disable_image" : "yamato_helpboard/wide_button_d.tga",

									"text" : "Teleportieren",
										
								},
								
							),
						
						},
					
					
					),
				},
			),
		},
		
		{

			"name" : "backButton",
			"type" : "button",
											
			"x" : 25,
			"y" : 30,
																			
			"default_image" : "yamato_dungeoncompendium/rotateleft_n.tga",
			"over_image" : "yamato_dungeoncompendium/rotateleft_h.tga",
			"down_image" : "yamato_dungeoncompendium/rotateleft_p.tga",
			"disable_image" : "yamato_dungeoncompendium/rotateleft_d.tga",
			
			"tooltip_text" : "Zurück zur Übersicht",

		},
		{

			"name" : "forwardButton",
			"type" : "button",
											
			"x" : 25 + 30,
			"y" : 30,
																			
			"default_image" : "yamato_dungeoncompendium/rotateright_n.tga",
			"over_image" : "yamato_dungeoncompendium/rotateright_h.tga",
			"down_image" : "yamato_dungeoncompendium/rotateright_p.tga",
			"disable_image" : "yamato_dungeoncompendium/rotateright_d.tga",
			
			"tooltip_text" : "Zurück zum letzten Dungeon",

		},
	),
}

