import uiScriptLocale

WINDOW_WIDTH = 300
WINDOW_HEIGTH = 350

window = {
	"name" : "SupportWindow",
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
			"style" : ("attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
		},

		
		{
			"name" : "backGroundBar0",
			"type" : "bar",
			"style" : ("attach",),
			
			"x" : 25,
			"y" : 65,
			
			"width" : 280,
			"height" : 40,
		},		

		{
			"name" : "updateButton",
			"type" : "button",
			
			"x" : 20 + 5 + 10,
			"y" : 60 + 10,
			
			"default_image" : "yamato_helpboard/normal_button_n.tga", 
			"over_image" : "yamato_helpboard/normal_button_h.tga",
			"down_image" : "yamato_helpboard/normal_button_p.tga",
							
			"text" : "Update",

			"tooltip" : "Lädt neue Anfragen vom Server.",
		},
		{
			"name" : "lastUpdateTextLine",
			"type" : "text",
			
			"x" : 130 + 10,
			"y" : 65 + 10,
			
			"outline" : 1,
			
			"text" : "Letztes Update: 1 Min.",			
		},
		{
			"name" : "backGroundBar",
			"type" : "bar",
			"style" : ("attach",),
			
			"x" : 25,
			"y" : 65 + 40 + 5,
			
			"width" : 280,
			"height" : 250,
			
			"children" : (
				
				{
					"name" : "playerListBox",
					"type" : "listbox",

					"x" : 0,
					"y" : 12,
							
					"width" : 280,
					"height" : 250,
							
				},
				{
					"name" : "scrollBar",
					"type" : "scrollbar",

					"x" : 20,
					"y" : 12,
					"size" : 230,
					"horizontal_align" : "right",
				},				
			),
		},
		
		{
			"name" : "backGroundBar02",
			"type" : "bar",
			"style" : ("attach",),
			
			"x" : 25,
			"y" : 65 + 40 + 5 + 250 + 5,
			
			"width" : 280,
			"height" : 40,
			
			"children" : (

				{
					"name" : "messageButton",
					"type" : "button",
					
					"x" : 40,
					"y" : 8,
					
					"default_image" : "yamato_helpboard/normal_button_n.tga", 
					"over_image" : "yamato_helpboard/normal_button_h.tga",
					"down_image" : "yamato_helpboard/normal_button_p.tga",
					"disable_image" : "yamato_helpboard/normal_button_d.tga",
									
					"text" : "Annehmen",

				},
				{
					"name" : "deleteButton",
					"type" : "button",
					
					"x" : 40 + 100,
					"y" : 8,
					
					"default_image" : "yamato_helpboard/normal_button_n.tga", 
					"over_image" : "yamato_helpboard/normal_button_h.tga",
					"down_image" : "yamato_helpboard/normal_button_p.tga",
					"disable_image" : "yamato_helpboard/normal_button_d.tga",
									
					"text" : "Löschen",

				},
			
			
			),
			
		},
		
		
		
		
	),
}
