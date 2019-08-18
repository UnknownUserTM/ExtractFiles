import uiScriptLocale

WINDOW_WIDTH = 580
WINDOW_HEIGTH = 430

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
			"style" : ("attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			"children" : 
			(
				{
					"name" : "bottom_tutorial_line",
					"type" : "text",
							
					"x" : 290 + 30,
					"y" : WINDOW_HEIGTH - 18,
							
					"text" : "Klicke auf ein Event um mehr Informationen zu erhalten.",
					
					"text_horizontal_align" : "center",
							
					"outline" : 1,
				},			
				## WeekSlots
				{
					"name" : "week_day_slot_01",
					"type" : "thinboard_circle",
					
					"x" : 25,
					"y" : 15,
					
					"width" : 80,
					"height" : 20,
					
					"children" : 
					(
						{
							"name" : "week_day_slot_01_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "Montag",
							
							"outline" : 1,
						},
					),
				},
				{
					"name" : "week_day_slot_02",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80,
					"y" : 15,
					
					"width" : 80,
					"height" : 20,
					
					"children" : 
					(
						{
							"name" : "week_day_slot_02_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "Dienstag",
							
							"outline" : 1,
						},
					),
				},
				{
					"name" : "week_day_slot_03",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80,
					"y" : 15,
					
					"width" : 80,
					"height" : 20,
					
					"children" : 
					(
						{
							"name" : "week_day_slot_03_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "Mittwoch",
							
							"outline" : 1,
						},
					),
				},				
				{
					"name" : "week_day_slot_04",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80,
					"y" : 15,
					
					"width" : 80,
					"height" : 20,
					
					"children" : 
					(
						{
							"name" : "week_day_slot_04_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "Donnerstag",
							
							"outline" : 1,
						},
					),
				},				
				{
					"name" : "week_day_slot_05",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80,
					"y" : 15,
					
					"width" : 80,
					"height" : 20,
					
					"children" : 
					(
						{
							"name" : "week_day_slot_05_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "Freitag",
							
							"outline" : 1,
						},
					),
				},				
				{
					"name" : "week_day_slot_06",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80,
					"y" : 15,
					
					"width" : 80,
					"height" : 20,
					
					"children" : 
					(
						{
							"name" : "week_day_slot_06_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "Samstag",
							
							"outline" : 1,
						},
					),
				},
				{
					"name" : "week_day_slot_07",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80 + 80,
					"y" : 15,
					
					"width" : 80,
					"height" : 20,
					
					"children" : 
					(
						{
							"name" : "week_day_slot_06_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "Sonntag",
							
							"outline" : 1,
						},
					),
				},				
				## DaySlots Line 1
				{
					"name" : "day_slot_01",
					"type" : "thinboard_circle",
					
					"x" : 25,
					"y" : 35,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_01_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "1",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_01_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_01_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_02",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80,
					"y" : 35,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_02_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "2",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_02_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_02_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_03",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80,
					"y" : 35,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_03_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "3",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_03_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_03_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_04",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80,
					"y" : 35,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_04_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "4",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_04_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_04_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_05",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80,
					"y" : 35,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_05_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "5",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_05_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_05_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_06",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80,
					"y" : 35,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_06_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "6",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_06_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_06_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_07",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80 + 80,
					"y" : 35,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_07_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "7",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_07_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_07_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},

				## DaySlots Line 2
				{
					"name" : "day_slot_08",
					"type" : "thinboard_circle",
					
					"x" : 25,
					"y" : 35 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_08_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "1",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_08_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_08_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_09",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80,
					"y" : 35 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_09_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "9",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_09_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_09_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_010",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80,
					"y" : 35 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_010_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "10",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_010_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_010_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_011",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80,
					"y" : 35 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_011_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "11",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_011_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_011_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_012",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80,
					"y" : 35 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_012_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "12",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_012_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_012_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_013",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_013_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "13",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_013_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_013_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_014",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_014_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "14",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_014_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_014_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},			


				## DaySlots Line 3
				{
					"name" : "day_slot_015",
					"type" : "thinboard_circle",
					
					"x" : 25,
					"y" : 35 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_015_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "15",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_015_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_015_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_016",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80,
					"y" : 35 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_016_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "16",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_016_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_016_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_017",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80,
					"y" : 35 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_017_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "17",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_017_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_017_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_018",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80,
					"y" : 35 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_018_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "18",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_018_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_018_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_019",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_019_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "19",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_019_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_019_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_020",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_020_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "20",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_020_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_020_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_021",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_021_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "21",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_021_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_021_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	

				## DaySlots Line 4
				{
					"name" : "day_slot_022",
					"type" : "thinboard_circle",
					
					"x" : 25,
					"y" : 35 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_022_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "22",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_022_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_022_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_023",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80,
					"y" : 35 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_023_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "16",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_023_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_023_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_024",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80,
					"y" : 35 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_024_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "24",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_024_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_024_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_025",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_025_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "18",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_025_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_025_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_026",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_026_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "26",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_026_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_026_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_027",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_027_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "20",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_027_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_027_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_028",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_028_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "28",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_028_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_028_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},

				## DaySlots Line 5
				{
					"name" : "day_slot_029",
					"type" : "thinboard_circle",
					
					"x" : 25,
					"y" : 35 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_029_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "29",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_029_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_029_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_030",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80,
					"y" : 35 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_030_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "30",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_030_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_030_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_031",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_031_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "31",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_031_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_031_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_032",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_032_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "32",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_032_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_032_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_033",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_033_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "33",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_033_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_033_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_034",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_034_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "34",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_034_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_034_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_035",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_035_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "35",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_035_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_035_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	


				## DaySlots Line 6
				{
					"name" : "day_slot_036",
					"type" : "thinboard_circle",
					
					"x" : 25,
					"y" : 35 + 60 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_036_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "36",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_036_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_036_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_037",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80,
					"y" : 35 + 60 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_037_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "37",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_037_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_037_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_038",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_038_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "38",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_038_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_038_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_039",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_039_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "39",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_039_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_039_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_040",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_040_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "40",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_040_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_040_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},	
				{
					"name" : "day_slot_041",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_041_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "41",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_041_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_041_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				{
					"name" : "day_slot_042",
					"type" : "thinboard_circle",
					
					"x" : 25 + 80 + 80 + 80 + 80 + 80 + 80,
					"y" : 35 + 60 + 60 + 60 + 60 + 60,
					
					"width" : 80,
					"height" : 60,
					
					"children" : 
					(
						{
							"name" : "day_slot_042_text",
							"type" : "text",
							
							"x" : 8,
							"y" : 4,
							
							"text" : "42",
							
							"outline" : 1,
						},
						{
							"name" : "day_slot_042_img",
							"type" : "image",
							
							"x" : 1,
							"y" : 1,
							
							"image" : "event/ox.tga",
						},
						{
							"name" : "day_slot_042_button",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"default_image" : "event/event_button.tga",
							"over_image" : "event/event_button.tga",
							"down_image" : "event/event_button.tga",						
						},

					),
				},
				
			),
		},
		
	),
}
