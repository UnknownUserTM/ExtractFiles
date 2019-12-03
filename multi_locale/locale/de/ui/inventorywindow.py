import uiScriptLocale
import item
 
EQUIPMENT_START_INDEX = 180
SIDEBAR_WIDTH = 22
window = {
	"name" : "InventoryWindow",

	## Open Inventar Positio
	"x" : SCREEN_WIDTH - 226 + 5 - SIDEBAR_WIDTH,
	"y" : SCREEN_HEIGHT - 715 +	20 - 15,
 
	"style" : ("movable", "float",),
 
	"width" : 236,
	"height" : 400 + 70 + 60 + 15 - 15 + 110 - 10 + 30 + 20 - 20,
 
	"children" :
	(
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8 + SIDEBAR_WIDTH,
			"y" : 7,

			"width" : 236+15-30-5,

		},
		## Inventory, Equipment Slots
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
 
			"x" : 0 + SIDEBAR_WIDTH,
			"y" : 50,
			
			"width" : 236-30-5,
			"height": 400 + 100 + 60 + 15 - 15 + 60 - 10 + 20 - 20,
 
            "children" :
            (
				{
					"name" : "EquipmentBackground",
					"type" : "thinboard_circle",
							
							
					"x" : 20,
					"y" : 10,
							
					"width" : 158,
					"height" : 190,
							
					"children" : (
						{
							"name" : "Equipment_Base",
							"type" : "image",
		 
							"x" : 1,
							"y" : 1,
		 
							"image" : "d:/ymir work/ui/game/windows/equipment_base.sub",
		 
							"children" :
							(
								{
									"name" : "EquipmentSlot",
									"type" : "slot",
		 
									"x" : 3,
									"y" : 3,
		 
									"width" : 150,
									"height" : 182,
		 
									"slot" : (
										{"index":EQUIPMENT_START_INDEX+0, "x":39, "y":37, "width":32, "height":64}, ## Rustung
										{"index":EQUIPMENT_START_INDEX+1, "x":39, "y":2, "width":32, "height":32}, ## Helm
										{"index":EQUIPMENT_START_INDEX+2, "x":39, "y":145, "width":32, "height":32}, ## Schuh
										{"index":EQUIPMENT_START_INDEX+3, "x":75, "y":67, "width":32, "height":32}, ## Armband
										{"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96}, ## Waffe
										{"index":EQUIPMENT_START_INDEX+5, "x":114, "y":77+8, "width":32, "height":32}, ## Halskette
										{"index":EQUIPMENT_START_INDEX+6, "x":114, "y":45+8, "width":32, "height":32}, ## Ohrringe
										{"index":EQUIPMENT_START_INDEX+7, "x":2, "y":115, "width":32, "height":32}, ## Slot Links
										{"index":EQUIPMENT_START_INDEX+8, "x":75, "y":115, "width":32, "height":32}, ## Slot Rechts
										{"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32}, ## Pfeil
										{"index":EQUIPMENT_START_INDEX+10, "x":75, "y":35, "width":32, "height":32}, ## Schild
										{"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
									),
								},
							),
						}, 
                        ## CostumeButton
                        {
                            "name" : "CostumeButton",
                            "type" : "button",
 
                            "x" : 78,
                            "y" : 5,
 
                            "tooltip_text" : uiScriptLocale.COSTUME_TITLE,
 
                            "default_image" : "d:/ymir work/ui/game/taskbar/costume_Button_01.tga",
                            "over_image" : "d:/ymir work/ui/game/taskbar/costume_Button_02.tga",
                            "down_image" : "d:/ymir work/ui/game/taskbar/costume_Button_03.tga",
                        },
					),
				},     
 				# ## Inventar Seite I
				# {
					# "name" : "Inventory_Tab_01",
					# "type" : "radio_button",

					# "x" : 24,
					# # "x" : 10+10+5-1 + 160+2,
					# "y" : 33 + 191-22,
					# # "y" : 33-20-3,
					# # "y" : 33-20-3+20+288+ 5,

					# "default_image" : "yamato_button/tab2_pressed.tga",
					# "over_image" : "yamato_button/tab2_hovered.tga",
					# "down_image" : "yamato_button/tab2_passive.tga",
					# "tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

					# "children" :
					# (
						# {
							# "name" : "Inventory_Tab_01_Print",
							# "type" : "text",

							# "x" : 0,
							# "y" : 0,

							# "all_align" : "center",

							# "text" : "I",
						# },
					# ),
				# },
				# ## Inventar Seite II
				# {
					# "name" : "Inventory_Tab_02",
					# "type" : "radio_button",

					# "x" : 24 + 31,
					# # "x" : 10+10+5-1 + 160 + 31+2,
					# "y" : 33 + 191-22,
					# # "y" : 33-20-3,
					# # "y" : 33-20-3+20+288+ 5,

					# "default_image" : "yamato_button/tab2_pressed.tga",
					# "over_image" : "yamato_button/tab2_hovered.tga",
					# "down_image" : "yamato_button/tab2_passive.tga",
					# "tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

					# "children" :
					# (
						# {
							# "name" : "Inventory_Tab_02_Print",
							# "type" : "text",

							# "x" : 0,
							# "y" : 0,

							# "all_align" : "center",

							# "text" : "II",
						# },
					# ),
				# },
				# ## Inventar Seite III
				# {
					# "name" : "Inventory_Tab_03",
					# "type" : "radio_button",

					# "x" : 24 + 62,
					# # "x" : 10+10+5-1 + 160+31+31+2,
					# "y" : 33 + 191-22,
					# # "y" : 33-20-3,
					# # "y" : 33-20-3+20+288+ 5,

					# "default_image" : "yamato_button/tab2_pressed.tga",
					# "over_image" : "yamato_button/tab2_hovered.tga",
					# "down_image" : "yamato_button/tab2_passive.tga",
					# "tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

					# "children" :
					# (
						# {
							# "name" : "Inventory_Tab_03_Print",
							# "type" : "text",

							# "x" : 0,
							# "y" : 0,

							# "all_align" : "center",

							# "text" : "III",
						# },
					# ),
				# },
				# ## Inventar Seite IV
				# {
					# "name" : "Inventory_Tab_04",
					# "type" : "radio_button",

					# "x" : 24 + 93,
					# # "x" : 10+10+5-1 + 160+31+31+31+2,
					# "y" : 33 + 191-22,
					# # "y" : 33-20-3,
					# # "y" : 33-20-3+20+288+ 5,

					# "default_image" : "yamato_button/tab2_pressed.tga",
					# "over_image" : "yamato_button/tab2_hovered.tga",
					# "down_image" : "yamato_button/tab2_passive.tga",
					# "tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

					# "children" :
					# (
						# {
							# "name" : "Inventory_Tab_04_Print",
							# "type" : "text",

							# "x" : 0,
							# "y" : 0,

							# "all_align" : "center",

							# "text" : "IV",
						# },
					# ),
				# },
				# ## Inventar Seite V
				# {
					# "name" : "Inventory_Tab_05",
					# "type" : "radio_button",
					# # "x" : 10+10+5-1 + 160+31+31+31+31+2,
					# "x" : 24 + 124,
					# "y" : 33 + 191-22,
					# # "y" : 33-20-3,
					# # "y" : 33-20-3+20+288+ 5,

					# "default_image" : "yamato_button/tab2_pressed.tga",
					# "over_image" : "yamato_button/tab2_hovered.tga",
					# "down_image" : "yamato_button/tab2_passive.tga",
					# "tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

					# "children" :
					# (
						# {
							# "name" : "Inventory_Tab_04_Print",
							# "type" : "text",

							# "x" : 0,
							# "y" : 0,

							# "all_align" : "center",

							# "text" : "V",
						# },
					# ),
				# },
				
				{
				
					"name" : "inventoryPage_Background",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 33 + 191-22,
					"width" : 158,
					"height" : 20,	
					
					"children" : (
						{
							"name" : "page_I_Window",
							"type" : "window",
							
							"x" : 1,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_I_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_I_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "I",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_II_Window",
							"type" : "window",
							
							"x" : 1 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_II_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_II_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "II",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_III_Window",
							"type" : "window",
							
							"x" : 1 + 31 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_III_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_III_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "III",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_IV_Window",
							"type" : "window",
							
							"x" : 1 + 31 + 31 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_IV_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_IV_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "IV",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_V_Window",
							"type" : "window",
							
							"x" : 1 + 31 + 31 + 31 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_V_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_V_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "V",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
					),
				},
				
				
				{
				
					"name" : "inventoryPage_Background_EXTRA",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 33 + 191-22 + 20,
					"width" : 158,
					"height" : 20,	
					
					"children" : (
						{
							"name" : "page_VI_Window",
							"type" : "window",
							
							"x" : 1,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_VI_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_VI_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "VI",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_VII_Window",
							"type" : "window",
							
							"x" : 1 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_VII_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_VII_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "VII",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_VIII_Window",
							"type" : "window",
							
							"x" : 1 + 31 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_VIII_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_VIII_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "VIII",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_IX_Window",
							"type" : "window",
							
							"x" : 1 + 31 + 31 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_IX_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_IX_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "IX",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
						{
							"name" : "page_X_Window",
							"type" : "window",
							
							"x" : 1 + 31 + 31 + 31 + 31,
							"y" : 1,
							
							"width" : 31,
							"height" : 18,
							
							"children" : (
								{
									"name" : "page_X_ClickedBG",
									"type" : "thinboard_circle",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 31,
									"height" : 18,
								},
								{
									"name" : "page_X_Button",
									"type" : "button",
									
									"x" : 0,
									"y" : -1, # 0 wenn nicht clicked?
									
									"text" : "X",
									
									"width" : 31,
									"height" : 18,
								},
							),
						},
					),
				},
				
				# {
				
					# "name" : "inventory_sort_bg",
					# "type" : "thinboard_circle",
					
					# "x" : 20,
					# # "y" : 33-20-3+20+288+ 5,
					# "y" : 224+20,
					# "width" : 160,
					# "height" : 20,	

					# "children" : (
						# {
							# "name" : "inventory_sort_textline",
							# "type" : "text",
							# "x" : 0,
							# "y" : 0,
							# "horizontal_align" : "center", 
							# "text_horizontal_align":"center",
							# "vertical_align" : "center",
							# "text_vertical_align" : "center",
							# "color" : 0xffd8a055,
							# "outline" : 1,
							# "text" : "Unsortiert",
						# },	
						# {
							# "name" : "inventory_sort_button",
							# "type" : "button",
							
							# "x" : 0,
							# "y" : 0,
							
							# "width" : 160,
							# "height" : 20,
						# },
					# ),
				# },	


				{
					"name" : "slotBackground",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 224 + 20+20-20,
					
					"width" : 160,
					"height" : 288,
					
					"children" : (
						
						{ "name":"slot_bg_line_0_slot_0", "type":"thinboard_circle", "x":0, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_1", "type":"thinboard_circle", "x":32, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_2", "type":"thinboard_circle", "x":64, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_3", "type":"thinboard_circle", "x":96, "y":0, "width":32, "height":32, },
						{ "name":"slot_bg_line_0_slot_4", "type":"thinboard_circle", "x":128, "y":0, "width":32, "height":32, },
						
						{ "name":"slot_bg_line_1_slot_0", "type":"thinboard_circle", "x":0, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_1", "type":"thinboard_circle", "x":32, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_2", "type":"thinboard_circle", "x":64, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_3", "type":"thinboard_circle", "x":96, "y":32, "width":32, "height":32, },
						{ "name":"slot_bg_line_1_slot_4", "type":"thinboard_circle", "x":128, "y":32, "width":32, "height":32, },

						{ "name":"slot_bg_line_2_slot_0", "type":"thinboard_circle", "x":0, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_1", "type":"thinboard_circle", "x":32, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_2", "type":"thinboard_circle", "x":64, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_3", "type":"thinboard_circle", "x":96, "y":64, "width":32, "height":32, },
						{ "name":"slot_bg_line_2_slot_4", "type":"thinboard_circle", "x":128, "y":64, "width":32, "height":32, },						
						
						{ "name":"slot_bg_line_3_slot_0", "type":"thinboard_circle", "x":0, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_1", "type":"thinboard_circle", "x":32, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_2", "type":"thinboard_circle", "x":64, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_3", "type":"thinboard_circle", "x":96, "y":96, "width":32, "height":32, },
						{ "name":"slot_bg_line_3_slot_4", "type":"thinboard_circle", "x":128, "y":96, "width":32, "height":32, },

						{ "name":"slot_bg_line_4_slot_0", "type":"thinboard_circle", "x":0, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_1", "type":"thinboard_circle", "x":32, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_2", "type":"thinboard_circle", "x":64, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_3", "type":"thinboard_circle", "x":96, "y":128, "width":32, "height":32, },
						{ "name":"slot_bg_line_4_slot_4", "type":"thinboard_circle", "x":128, "y":128, "width":32, "height":32, },

						{ "name":"slot_bg_line_5_slot_0", "type":"thinboard_circle", "x":0, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_1", "type":"thinboard_circle", "x":32, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_2", "type":"thinboard_circle", "x":64, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_3", "type":"thinboard_circle", "x":96, "y":160, "width":32, "height":32, },
						{ "name":"slot_bg_line_5_slot_4", "type":"thinboard_circle", "x":128, "y":160, "width":32, "height":32, },

						{ "name":"slot_bg_line_6_slot_0", "type":"thinboard_circle", "x":0, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_1", "type":"thinboard_circle", "x":32, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_2", "type":"thinboard_circle", "x":64, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_3", "type":"thinboard_circle", "x":96, "y":192, "width":32, "height":32, },
						{ "name":"slot_bg_line_6_slot_4", "type":"thinboard_circle", "x":128, "y":192, "width":32, "height":32, },

						{ "name":"slot_bg_line_7_slot_0", "type":"thinboard_circle", "x":0, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_1", "type":"thinboard_circle", "x":32, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_2", "type":"thinboard_circle", "x":64, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_3", "type":"thinboard_circle", "x":96, "y":224, "width":32, "height":32, },
						{ "name":"slot_bg_line_7_slot_4", "type":"thinboard_circle", "x":128, "y":224, "width":32, "height":32, },
						
						{ "name":"slot_bg_line_8_slot_0", "type":"thinboard_circle", "x":0, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_1", "type":"thinboard_circle", "x":32, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_2", "type":"thinboard_circle", "x":64, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_3", "type":"thinboard_circle", "x":96, "y":256, "width":32, "height":32, },
						{ "name":"slot_bg_line_8_slot_4", "type":"thinboard_circle", "x":128, "y":256, "width":32, "height":32, },						
						
						{
							"name" : "ItemSlot",
							"type" : "grid_table",
							
							"x" : 0,
							"y" : 0,

							"start_index" : 0,
							"x_count" : 5,
							"y_count" : 9,
							"x_step" : 32,
							"y_step" : 32,
						},
					),
				},
				{
					"name" : "goldBackground",
					"type" : "thinboard_circle",
					
					
					"x" : 20,
					"y" : 224+288+ 20+20-20,
					
					"width" : 160,
					"height" : 20,
					
					"children" : (
					
						{
							"name" : "Money_Slot",
							"type" : "button",
							
							"x" : 0,
							"y" : 0,
							
							"width" : 160,
							"height" : 20,
						},
						{
							"name":"Money_Icon",
							"type":"image",
							
							"x":3,
							"y":3,
							
							"image":"yamato_inventory/gold_coin.tga",
						},
						{
							"name" : "Money",
							"type" : "text",
							
							"x" : 3,
							"y" : 3,
							
							"horizontal_align" : "right",
							"text_horizontal_align" : "right",
							
							"text" : "123456789 DC's",
						},					
					),
				},
				{
					"name" : "achievementBackground",
					"type" : "thinboard_circle",
					
					
					"x" : 20,
					"y" : 224+288+ 20 + 20+20-20,
					
					"width" : 160,
					"height" : 20,
					
					"children" : (
						{
							"name":"Achievement_Icon",
							"type":"image",
							
							"x":3,
							"y":2,
							
							"image" : "d:/ymir work/ui/achievement_small.dds",
						},
						{
							"name" : "AchievementPoints",
							"type" : "text",
							
							"x" : 3,
							"y" : 3,
							
							"horizontal_align" : "right",
							"text_horizontal_align" : "right",
							
							"text" : "123456789 DC's",
						},					
					),
				},				
				{
					"name" : "dungeonBackground",
					"type" : "thinboard_circle",
					
					
					"x" : 20,
					"y" : 224+288+ 20 + 20 + 20+20-20,
					
					"width" : 160,
					"height" : 20,
					
					"children" : (
						{
							"name":"Dungeon_Icon",
							"type":"image",
							
							"x":3,
							"y":1,
							
							"image" : "yamato_inventory/dungeon_icon.tga",
						},
						{
							"name" : "DungeonPoints",
							"type" : "text",
							
							"x" : 3,
							"y" : 3,
							
							"horizontal_align" : "right",
							"text_horizontal_align" : "right",
							
							"text" : "0 DP's",
						},					
					),
				},				

				# {
					# "name":"Money_Slot",
					# "type":"button",
					
					# # "x":8,
					# # "y":26+ 15,

					# "x" : 45,
					# "y" : 400 + 33 + 191-22 + 3,
					
					# # "horizontal_align":"center",
					# # "vertical_align":"bottom",
					
					# "default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					# "children" :
					# (
						# {
							# "name":"Money_Icon",
							# "type":"image",
							
							# "x":3,
							# "y":2,
							
							# "image":"yamato_inventory/gold_coin.tga",
						# },
						
						# {
							# "name" : "Money",
							# "type" : "text",
							
							# "x" : 3,
							# "y" : 3,
							
							# "horizontal_align" : "right",
							# "text_horizontal_align" : "right",
							
							# "text" : "123456789 DC's",
						# },
					# ),
				# },
				
				# ##Inventar DC Anzeige
				# {
					# "name":"DC_Slot",
					# "type":"button",
					
					# # "x":8,
					# # "y":46+ 15,
					
					# "x" : 45,
					# "y" : 400 + 33 + 191-22 + 3 + 20 + 20 + 20,
					
					# # "horizontal_align":"center",
					# # "vertical_align":"bottom",
					
					# "default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					# "children" :
					# (
						# {
							# "name":"DC_Icon",
							# "type":"image",
							
							# "x":-18,
							# "y":2,
							
							# "image":"d:/ymir work/ui/drachencoins.dds",
						# },
						
						# {
							# "name" : "DC",
							# "type" : "text",
							
							# "x" : 3,
							# "y" : 3,
							
							# "horizontal_align" : "right",
							# "text_horizontal_align" : "right",
							
							# "text" : "123456789 DC's",
						# },
					# ),
				# },
				# {
					# "name" : "ManageInventorySortButton",
					# "type" : "button",
 
					# "x" : 18,
					# "y" : 33 + 191-22 + 3 + 20 + 20 + 50,
 
					# "text" : "Einstellungen fur Seite I",
 
					# "default_image" : "yamato_helpboard/wide_button_n.tga",
					# "over_image" : "yamato_helpboard/wide_button_h.tga",
					# "down_image" : "yamato_helpboard/wide_button_p.tga",
				# },
						
				# ##Inventar AP Anzeige
				# {
					# "name":"Aps_Slot",
					# "type":"button",
					
					# "x" : 45,
					# "y" : 400 + 33 + 191-22 + 3 + 20,
					
					# # "horizontal_align":"center",
					# # "vertical_align":"bottom",
					
					# "default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					# "children" :
					# (
						# {
							# "name":"Aps_Icon",
							# "type":"image",
							
							# "x":-18,
							# "y":2,
							
							# "image":"d:/ymir work/ui/achievement_small.dds",
						# },
						
						# {
							# "name" : "Aps",
							# "type" : "text",
							
							# "x" : 3,
							# "y" : 3,
							
							# "horizontal_align" : "right",
							# "text_horizontal_align" : "right",
							
							# "text" : "123456789 AP's",
						# },
					# ),
				# },
				# ##Inventar Dailypoint Anzeige
				# {
					# "name":"Dps_Slot",
					# "type":"button",
					
					# # "x":8,
					# # "y":86+ 15,
					# "x" : 45,
					# "y" : 400 + 33 + 191-22 + 3 + 20 + 20,
					
					# # "horizontal_align":"center",
					# # "vertical_align":"bottom",
					
					# "default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					# "down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					# "children" :
					# (
						# {
							# "name":"Dps_Icon",
							# "type":"image",
							
							# "x":-18,
							# "y":2,
							
							# "image":"d:/ymir work/ui/daily.dds",
						# },
						
						# {
							# "name" : "DPs",
							# "type" : "text",
							
							# "x" : 3,
							# "y" : 3,
							
							# "horizontal_align" : "right",
							# "text_horizontal_align" : "right",
							
							# "text" : "123456789 DP's",
						# },
					# ),
				# },
				# {			
					# "name" : "DropDownBoard",
					# "type" : "slotbar",
					# "x" : 120+10-85,
					# "y" : 94,
					# "width" : 80,
					# "height" : 55+20+20+20,
					
					# "children" :
					# (
						# {
							# "name" : "DropDownButton1",
							# "type" : "button",
							# "text" : "I-Lager",
							
							# "x" : 10,
							# "y" : 8,

							# "tooltip_text" : "Itemlager",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },	
						# {
							# "name" : "DropDownButton2",
							# "type" : "button",
							# "text" : "IS-Lager",
							
							# "x" : 10,
							# "y" : 28,

							# "tooltip_text" : "Itemshop-Lager",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },	
						# {
							# "name" : "DropDownButton3",
							# "type" : "button",
							# "text" : "G-Lager",
							
							# "x" : 10,
							# "y" : 48,

							# "tooltip_text" : "Gildenlager",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },	
						
						# {
							# "name" : "DropDownButton4",
							# "type" : "button",
							# "text" : "FB-Lager",
							
							# "x" : 10,
							# "y" : 68,

							# "tooltip_text" : "Fertigkeitsbucher-Lager",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },
						# {
							# "name" : "DropDownButton5",
							# "type" : "button",
							# "text" : "Upp-Lager",
							
							# "x" : 10,
							# "y" : 88,

							# "tooltip_text" : "UppItem-Lager",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },
					# ),
				# },
				
				# {			
					# "name" : "DropDownBoard2",
					# "type" : "slotbar",
					# "x" : 120+10-85,
					# "y" : 94,
					# "width" : 80,
					# "height" : 55+20,
					
					# "children" :
					# (
						# {
							# "name" : "DropDownButton2_1",
							# "type" : "button",
							# "text" : "100kk",
							
							# "x" : 10,
							# "y" : 8,

							# "tooltip_text" : "100kk Yangbarren erstellen",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },	
						# {
							# "name" : "DropDownButton2_2",
							# "type" : "button",
							# "text" : "500kk",
							
							# "x" : 10,
							# "y" : 28,

							# "tooltip_text" : "500kk Yangbarren erstellen",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },	
						# {
							# "name" : "DropDownButton2_3",
							# "type" : "button",
							# "text" : "1kkk",
							
							# "x" : 10,
							# "y" : 48,

							# "tooltip_text" : "1kkk Yangbarren erstellen",
							# "default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						# },						
					# ),
				# },

            ),
        },
    ),
}