import uiScriptLocale

window = {
	"name" : "evo2board",
	"style" : ("movable", "float",),

	"x" : 100,
	"y" : 100,

	"width" : 600,
	"height" : 300,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 600,
			"height" : 300,

			"children" :
			(
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 580,
					"color" : "gray",

					"children" :
					(
						{ 
						"name":"titlename", 
						"type":"text", 
						
						"x":0, 
						"y":3, 
						
						"horizontal_align":"center", 
						"text_horizontal_align":"center",
						
						"text": "DragonRise-Online Board", 
						 },
					),
				},
			## Überschrift
				{
					"name" : "Überschrift",
					"type" : "text",

					"x" : 20,
					"y" : 34,

					"text" : "Wähle aus wen du kontaktieren möchtest:",
				},
			## Gamemasta1 Zeugs
				{
					"name" : "Gamemasta1",
					"type" : "button",

					"x" : 30,
					"y" : 54,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta1PN",
					"type" : "button",

					"x" : 130,
					"y" : 54,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm1",
					"type" : "image",

					"x" : 15,
					"y" : 54,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
				
			## Gamemasta2 Zeugs
				{
					"name" : "Gamemasta2",
					"type" : "button",

					"x" : 30,
					"y" : 78,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta2PN",
					"type" : "button",

					"x" : 130,
					"y" : 78,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm2",
					"type" : "image",

					"x" : 15,
					"y" : 78,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta3 Zeugs
				{
					"name" : "Gamemasta3",
					"type" : "button",

					"x" : 30,
					"y" : 102,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta3PN",
					"type" : "button",

					"x" : 130,
					"y" : 102,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm3",
					"type" : "image",

					"x" : 15,
					"y" : 102,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta4 Zeugs
				{
					"name" : "Gamemasta4",
					"type" : "button",

					"x" : 30,
					"y" : 126,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta4PN",
					"type" : "button",

					"x" : 130,
					"y" : 126,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm4",
					"type" : "image",

					"x" : 15,
					"y" : 126,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta5 Zeugs
				{
					"name" : "Gamemasta5",
					"type" : "button",

					"x" : 30,
					"y" : 150,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta5PN",
					"type" : "button",

					"x" : 130,
					"y" : 150,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm5",
					"type" : "image",

					"x" : 15,
					"y" : 150,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta6 Zeugs
				{
					"name" : "Gamemasta6",
					"type" : "button",

					"x" : 30,
					"y" : 174,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta6PN",
					"type" : "button",

					"x" : 130,
					"y" : 174,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm6",
					"type" : "image",

					"x" : 15,
					"y" : 174,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta7 Zeugs
				{
					"name" : "Gamemasta7",
					"type" : "button",

					"x" : 30,
					"y" : 198,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta7PN",
					"type" : "button",

					"x" : 130,
					"y" : 198,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm7",
					"type" : "image",

					"x" : 15,
					"y" : 198,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta8 Zeugs
				{
					"name" : "Gamemasta8",
					"type" : "button",

					"x" : 30,
					"y" : 222,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta8PN",
					"type" : "button",

					"x" : 130,
					"y" : 222,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm8",
					"type" : "image",

					"x" : 15,
					"y" : 222,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},		
			## Gamemasta9 Zeugs
				{
					"name" : "Gamemasta9",
					"type" : "button",

					"x" : 330,
					"y" : 54,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta9PN",
					"type" : "button",

					"x" : 430,
					"y" : 54,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm9",
					"type" : "image",

					"x" : 315,
					"y" : 54,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
				
			## Gamemasta10 Zeugs
				{
					"name" : "Gamemasta10",
					"type" : "button",

					"x" : 330,
					"y" : 78,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta10PN",
					"type" : "button",

					"x" : 430,
					"y" : 78,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm10",
					"type" : "image",

					"x" : 315,
					"y" : 78,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta11 Zeugs
				{
					"name" : "Gamemasta11",
					"type" : "button",

					"x" : 330,
					"y" : 102,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta11PN",
					"type" : "button",

					"x" : 430,
					"y" : 102,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm11",
					"type" : "image",

					"x" : 315,
					"y" : 102,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta12 Zeugs
				{
					"name" : "Gamemasta12",
					"type" : "button",

					"x" : 330,
					"y" : 126,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta12PN",
					"type" : "button",

					"x" : 430,
					"y" : 126,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm12",
					"type" : "image",

					"x" : 315,
					"y" : 126,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta13 Zeugs
				{
					"name" : "Gamemasta13",
					"type" : "button",

					"x" : 330,
					"y" : 150,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta13PN",
					"type" : "button",

					"x" : 430,
					"y" : 150,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm13",
					"type" : "image",

					"x" : 315,
					"y" : 150,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta14 Zeugs
				{
					"name" : "Gamemasta14",
					"type" : "button",

					"x" : 330,
					"y" : 174,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta14PN",
					"type" : "button",

					"x" : 430,
					"y" : 174,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm14",
					"type" : "image",

					"x" : 315,
					"y" : 174,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta15 Zeugs
				{
					"name" : "Gamemasta15",
					"type" : "button",

					"x" : 330,
					"y" : 198,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta15PN",
					"type" : "button",

					"x" : 430,
					"y" : 198,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm15",
					"type" : "image",

					"x" : 315,
					"y" : 198,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},
			## Gamemasta16 Zeugs
				{
					"name" : "Gamemasta16",
					"type" : "button",

					"x" : 330,
					"y" : 222,

					"text" : "Gamemaster",

					"default_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_02.sub",
				},
				{
					"name" : "Gamemasta16PN",
					"type" : "button",

					"x" : 430,
					"y" : 222,

					"text" : "Anschreiben",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "imagegm16",
					"type" : "image",

					"x" : 315,
					"y" : 222,

					"image" : "d:/ymir work/ui/game/windows/messenger_list_offline.sub",
				},					

			##Aktualisieren Button
				{
					"name" : "Aktualisieren",
					"type" : "button",

					"x" : 20,
					"y" : 255,

					"text" : "Aktualisieren",

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
			## Copyright
				{
					"name" : "Überschrift",
					"type" : "text",

					"x" : 520,
					"y" : 255,

					"text" : "© DargonRise",
				},
			),
		},
	),
}
