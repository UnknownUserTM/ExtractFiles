import uiScriptLocale

WINDOW_WIDTH = 505
WINDOW_HEIGTH = 40

window = {
	"name" : "DungeonMakerToolBar",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - WINDOW_WIDTH - 150,
	"y" : 10,

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGTH,

	"children" :
	(			

		{
			"name" : "darkBGBar",
			"type" : "bar",
			
			"x" : 0,
			"y" : 0,
			
			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGTH,
		
		
		},
		{
			"name" : "board",
			"type" : "thinboard",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 0,

			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGTH,
			
			
			"children" : ( 
				{
					"name" : "stageViewToggleButton",
					"type" : "button",
					
					"x" : 12,
					"y" : 10,
					
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",			
				
					"text" : "Ebenen",
				
				},
				{
					"name" : "stageTextLine",
					"type" : "text",
					
					"x" : 12 + 65,
					"y" : 13,
					
					"text" : "Keine Ebene ausgewählt.",
					"outline" : 1,
				},
				
				
				{
					"name" : "editWindowToggleButton",
					"type" : "button",
					
					"x" : 12 + 200,
					"y" : 10,
					
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",			
					"disable_image" : "d:/ymir work/ui/public/middle_button_03.sub",			
				
					"text" : "Bearbeiten",
				
				},
				{
					"name" : "toolsToggleButton",
					"type" : "button",
					
					"x" : 12 + 200 + 65,
					"y" : 10,
					
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",			
				
					"text" : "Regen",
				
				},	
				{
					"name" : "guideButton",
					"type" : "button",
					
					"x" : 12 + 200 + 65 + 65,
					"y" : 10,
					
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",			
				
					"text" : "Anleitung",
				
				},	
				{
					"name" : "exportButton",
					"type" : "button",
					
					"x" : 12 + 200 + 65 + 65 + 65,
					"y" : 10,
					
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",			
					"disable_image" : "d:/ymir work/ui/public/middle_button_03.sub",			
				
					"text" : "Export",
				
				},	
				{
					"name" : "closeButton",
					"type" : "button",
					
					"x" : 12 + 200 + 65 + 65 + 65 + 65 + 5,
					"y" : 13,
					
					"default_image" : "d:/ymir work/ui/public/close_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/close_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/close_button_03.sub",			
								
				},	
				# {
					# "name" : "versionTextLine",
					# "type" : "button",
					
					# "x" : 12 + ,
					# "y" : WINDOW_HEIGTH + 3,
					
					# "text" : "Version: 0.1 (InDEV)",
					# "outline" : 1,		
								
				# },				
			),
		},
	),
}

