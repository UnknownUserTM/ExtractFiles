import uiScriptLocale

WINDOW_WIDTH = 250
WINDOW_HEIGTH = 150

window = {
	"name" : "CalenderWindow",
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
					"name" : "raceSelectBoard",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 8,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : 20,

					"horizontal_align" : "center",			
					
					"children" : (
					
						{
							"name" : "raceSelectTextLine",
							"type" : "text",
									
							"x" : 0,
							"y" : 4,
								
							"text" : "Wähle eine Klasse",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
								
						},						
					),
				},
				# {
					# "name" : "raceSelectDropDownBoard",
					# "type" : "thinboard_circle",
					
					# "x" : 0,
					# "y" : 8,
					
					# "width" : WINDOW_WIDTH - 10,
					# "height" : 18 * 4,

					# "horizontal_align" : "center",					
				
				
					# "children" : (
						# {
							# "name" : "raceSelectListBox",
							# "type" : "listbox",
							
							# "x" : 0,
							# "y" : 0,
							
							# "width" : WINDOW_WIDTH - 11,
							# "height" : 17 * 4,
						# },
					
					# ),
				
				# },
			
				{
					"name" : "sexSelectBoard",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 8 + 22,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : 20,

					"horizontal_align" : "center",			
					
					"children" : (
					
						{
							"name" : "sexSelectTextLine",
							"type" : "text",
									
							"x" : 0,
							"y" : 4,
								
							"text" : "Wähle das Geschlecht",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
								
						},						
					),
				},			
				# {
					# "name" : "sexSelectDropDownBoard",
					# "type" : "thinboard_circle",
					
					# "x" : 0,
					# "y" : 8,
					
					# "width" : WINDOW_WIDTH - 10,
					# "height" : 18 * 4,

					# "horizontal_align" : "center",					
				
				
					# "children" : (
						# {
							# "name" : "sexSelectListBox",
							# "type" : "listbox",
							
							# "x" : 0,
							# "y" : 0,
							
							# "width" : WINDOW_WIDTH - 11,
							# "height" : 17 * 4,
						# },
					
					# ),
				
				# },
				
				{
					"name" : "skillGroupSelectBoard",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 8 + 22 + 22,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : 20,

					"horizontal_align" : "center",			
					
					"children" : (
						{
							"name" : "skillGroupSelectBoardRedBar",
							"type" : "bar",
							
							"x" : 0,
							"y" : 0,
							
							"width" : WINDOW_WIDTH - 10,
							"height" : 20,
						
						},
					
						{
							"name" : "skillGroupSelectTextLine",
							"type" : "text",
									
							"x" : 0,
							"y" : 4,
								
							"text" : "Wähle die Skillgruppe",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
								
						},						
					),
				},

				{
					"name" : "changeButton",
					"type" : "button",
							
					"x" : 0,
					"y" : 8 + 22 + 22 + 22 + 30,
						
					"default_image" : "yamato_helpboard/wide_button_n.tga",
					"over_image" : "yamato_helpboard/wide_button_h.tga",
					"down_image" : "yamato_helpboard/wide_button_p.tga",
					"disable_image" : "yamato_helpboard/wide_button_d.tga",
					"horizontal_align" : "center",
					"text" : "Change!",
						
				},
				{
					"name" : "raceSelectDropDownBoard",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 8,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : 18 * 4,

					"horizontal_align" : "center",					
				
				
					"children" : (
						{
							"name" : "raceSelectListBox",
							"type" : "listbox",
							
							"x" : 0,
							"y" : 0,
							
							"width" : WINDOW_WIDTH - 11,
							"height" : 17 * 4,
						},
					
					),
				
				},
				{
					"name" : "sexSelectDropDownBoard",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 8 + 22,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : 18 * 2,

					"horizontal_align" : "center",					
				
				
					"children" : (
						{
							"name" : "sexSelectListBox",
							"type" : "listbox",
							
							"x" : 0,
							"y" : 0,
							
							"width" : WINDOW_WIDTH - 11,
							"height" : 17 * 2,
						},
					
					),
				
				},
				{
					"name" : "skillGroupSelectDropDownBoard",
					"type" : "thinboard_circle",
					
					"x" : 0,
					"y" : 8 + 22 + 22,
					
					"width" : WINDOW_WIDTH - 10,
					"height" : 18 * 2,

					"horizontal_align" : "center",					
				
				
					"children" : (
						{
							"name" : "skillGroupSelectListBox",
							"type" : "listbox",
							
							"x" : 0,
							"y" : 0,
							
							"width" : WINDOW_WIDTH - 11,
							"height" : 17 * 2,
						},
					
					),
				
				},				
			),
		},
	),
}

