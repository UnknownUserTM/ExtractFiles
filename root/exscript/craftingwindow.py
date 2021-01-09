import uiScriptLocale
import localeInfo

WINDOW_WIDTH = 535
WINDOW_HEIGTH = 390

REMOVE_FROM_BOTTOM = 23
window = {
	"name" : "CraftWindow",
	"style" : ("movable", "float",),

	# "x" : (SCREEN_WIDTH/2) - (WINDOW_WIDTH/2),  # SCREEN CENTER SPAWN
	# "y" : (SCREEN_HEIGHT/2) - (WINDOW_HEIGHT/2), # SCREEN CENTER SPAWN

	# "x" : 24,
	# "y" : (SCREEN_HEIGHT - 37 - WINDOW_HEIGTH) / 2,

	"x" : SCREEN_WIDTH - 226 + 5 - 22 - WINDOW_WIDTH - 30,
	"y" : SCREEN_HEIGHT - 715 +	20 - 15,

	"width" : WINDOW_WIDTH+30,
	"height" : WINDOW_HEIGTH+50+30 - REMOVE_FROM_BOTTOM,

	"children" :
	(
		## BOARD
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : WINDOW_WIDTH+30+15 - 15 - 5,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("movable","attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30 - 15 - 5,
			"height" : WINDOW_HEIGTH+30 - 30 + 3 - REMOVE_FROM_BOTTOM,
			
			"children" : (

				
				####################################
				## Navigation
				{
					"name" : "navigationBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 9,
					
					"width" : 250,
					"height" : WINDOW_HEIGTH - 9 - 15 + 3 - REMOVE_FROM_BOTTOM,
				},	

				####################################
				## CraftInfo	
				{
					"name" : "infoBoard",
					"type" : "thinboard_circle",
					
					"x" : 20 + 5 + 250,
					"y" : 9,
					
					"width" : 250,
					"height" : WINDOW_HEIGTH - 20 - 15 + 3 + 10 + 1 - REMOVE_FROM_BOTTOM,
					
					"children" : (
						{
							"name" : "desiredItemSlot",
							"type" : "grid_table",

							"x" : 8,
							"y" : 8,

							"start_index" : 0,
							"x_count" : 1,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							# "image" : "d:/ymir work/ui/public/Slot_Base.sub"						
						
						},
						{
							"name" : "itemNameText",
							"type" : "text",
							
							"x" : 8 + 32 + 10,
							"y" : 8,
							
							"text" : localeInfo.CRAFTING_WINDOW_NAME,
							"outline" : 1,
						},
						{
							"name" : "itemCountText",
							"type" : "text",
							
							"x" : 8 + 32 + 10,
							"y" : 8 + 15,
							
							"text" : localeInfo.CRAFTING_WINDOW_COUNT,
							"outline" : 1,
						},
						{
							"name" : "itemChanceText",
							"type" : "text",
							
							"x" : 8 + 32 + 10,
							"y" : 8 + 15 + 15,
							
							"text" : localeInfo.CRAFTING_WINDOW_CHANCE,
							"outline" : 1,
						},
						# {
							# "name" : "itemExtraChanceText",
							# "type" : "text",
							
							# "x" : 8 + 32 + 10 + 80,
							# "y" : 8 + 15 + 15,
							
							# "text" : "(+10%)",
							# "outline" : 1,
						# },

						{
							"name" : "secondSplitLine",
							"type" : "line",
							
							"x" : 8,
							"y" : 8 + 96 + 10 + 29,
							
							"width" : 250 - 16,
							"height" : 0,
							"color" : 0xFF6C6359,
						},
						
						{
							"name" : "materialTitleTextLIne",
							"type" : "text",
							
							"x" : 9,
							"y" : 8 + 96 + 10 + 29 + 5,
							
							"text" : localeInfo.CRAFTING_WINDOW_MATERIALS,
							"outline" : 1,
						
						
						},
						
						{
							"name" : "materialItemSlots",
							"type" : "slot",

							"x" : 8,
							"y" : 8 + 96 + 10 + 29 + 5 + 15+ 10,

							"width" : 250 - 16,
							"height" : 80,
							
							"image" : "d:/ymir work/ui/game/windows/metin_slot_silver.sub",

							"slot" : (
										{"index":0, "x":0+ 14, "y":0, "width":32, "height":32},
										{"index":1, "x":32 + 10+ 14, "y":0, "width":32, "height":32},
										{"index":2, "x":64 + 20+ 14, "y":0, "width":32, "height":32},
										{"index":3, "x":96 + 30+ 14, "y":0, "width":32, "height":32},
										{"index":3, "x":128 + 40+ 14, "y":0, "width":32, "height":32},

										{"index":0, "x":0+ 14, "y":42, "width":32, "height":32},
										{"index":1, "x":32 + 10+ 14, "y":42, "width":32, "height":32},
										{"index":2, "x":64 + 20+ 14, "y":42, "width":32, "height":32},
										{"index":3, "x":96 + 30+ 14, "y":42, "width":32, "height":32},
										{"index":3, "x":128 + 40+ 14, "y":42, "width":32, "height":32},


									),
						},

						{
							"name" : "thirdSplitLine",
							"type" : "line",
							
							"x" : 8,
							"y" : 8 + 96 + 10 + 29 + 15 + 80 + 30,
							
							"width" : 250 - 16,
							"height" : 0,
							"color" : 0xFF6C6359,
						},
						
						{
							"name" : "bonusSlotBackgroundImage",
							"type" : "image",
							
							"x" : 8 + 14,
							"y" : 8 + 96 + 10 + 29 + 15 + 80 + 30 + 10,
						
							"image" : "d:/ymir work/ui/game/windows/metin_slot_gold.sub",
						},
						
						
						{
							"name" : "bonusSlot",
							"type" : "grid_table",

							"x" : 8 + 14,
							"y" : 8 + 96 + 10 + 29 + 15 + 80 + 30 + 10,

							"start_index" : 0,
							"x_count" : 1,
							"y_count" : 1,
							"x_step" : 32,
							"y_step" : 32,

						},
						
						{
							"name" : "bonusSlotTextLine",
							"type" : "text",
							
							"x" : 8,
							"y" : 8 + 96 + 10 + 29 + 15 + 80 + 30 + 10 + 37,
							
							"text" : localeInfo.CRAFTING_WINDOW_BONUS_CHANCE,
						
						
						},
						
						{ 
							"name" : "craftButton", 
							"type" : "button", 
									
							"x" : 250 - 8 - 88,
							"y" : 8 + 96 + 10 + 29 + 15 + 80 + 30 + 10 + 32,
									
							"text" : localeInfo.CRAFTING_WINDOW_CRAFT_BUTTON,
									
							"default_image" : "d:/ymir work/ui/public/large_button_01.sub", 
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub", 
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub", 
							"disable_image" : "d:/ymir work/ui/public/large_button_03.sub", 
						},
						
						{
							"name" : "goldThinBoard",
							"type" : "thinboard_circle",
							
							"x" : 250 - 8 - 88,
							"y" : 8 + 96 + 10 + 29 + 15 + 80 + 30 + 10 + 32 - 22 - 5,							
							
							"width" : 88,
							"height" : 22,
							
							"children" : (
								{ "name" : "money", "type":"text", "x":0, "y":-1, "text":"1.000.000.000", "all_align":"center" },
							),
						
						},

						
					),
				},	
				{
					"name" : "noItemSelectBoard",
					"type" : "thinboard_circle",
					
					"x" : 20 + 5 + 250,
					"y" : 9,
					
					"width" : 250,
					"height" : WINDOW_HEIGTH - 9 - 15 + 3 - REMOVE_FROM_BOTTOM,
					
					"children" : (
						{ 
							"name" : "noItemInfo", 
							"type":"text", 
							"x":0, 
							"y":-1, 
							"text": localeInfo.CRAFTING_WINDOW_NO_NAV_POINT, 
							"all_align":"center",
						},				
					
					
					),
				},
			),
		},
	),
}
