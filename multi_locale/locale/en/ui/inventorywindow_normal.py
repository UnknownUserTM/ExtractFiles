import uiScriptLocale
import item
 
EQUIPMENT_START_INDEX = 180
 
window = {
	"name" : "InventoryWindow",

	## Open Inventar Positio
	"x" : SCREEN_WIDTH - 226,
	"y" : SCREEN_HEIGHT - 37 - 661 - 60 - 15 - 15 + 65,
 
	"style" : ("movable", "float",),
 
	"width" : 236,
	"height" : 661 + 100 + 60 + 15 - 15,
 
	"children" :
	(
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : 236+15-30,

		},
		## Inventory, Equipment Slots
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
 
			"x" : 0,
			"y" : 50,
			
			"width" : 236-30,
			"height": 661-100 + 60 + 15 - 15,
 
            "children" :
            (
 
                ## Equipment Slot
                {
                    "name" : "Equipment_Base",
                    "type" : "image",
 
					"x" : 10+10+5-1,
					"y" : 33-20-3,
 
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
                                        # {"index":EQUIPMENT_START_INDEX+0, "x":39, "y":37, "width":32, "height":64},
                                        # {"index":EQUIPMENT_START_INDEX+1, "x":39, "y":2, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+2, "x":39, "y":145, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+3, "x":75, "y":67, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96},
                                        # {"index":EQUIPMENT_START_INDEX+5, "x":114, "y":67, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+6, "x":114, "y":35, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+7, "x":2, "y":145, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+8, "x":75, "y":145, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32},
                                        # {"index":EQUIPMENT_START_INDEX+10, "x":75, "y":35, "width":32, "height":32},
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
                                        ## 새 반지1
                                        ##{"index":item.EQUIPMENT_RING1, "x":2, "y":106, "width":32, "height":32},
                                        ## 새 반지2
                                        ##{"index":item.EQUIPMENT_RING2, "x":75, "y":106, "width":32, "height":32},
                                        ## 새 벨트
                                        {"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
                                    ),
                        },
						
                        ## Geldspeicher kaufen
                        {
                            "name" : "YangspeicherButton",
                            "type" : "button",
 
                            "x" : 118 - 38,
                            "y" : 33-20-3+115 + 35 - 10 + 2,
 
                            "tooltip_text" : "Geldspeicher kaufen?",
 
                            "default_image" : "locale/de/ui/icons/geldspeicher_invi.tga",
                            "over_image" : "locale/de/ui/icons/geldspeicher_invi_hover.tga",
                            "down_image" : "locale/de/ui/icons/geldspeicher_invi_hover.tga",
                        },
						
                        ## MallButton
                        {
                            "name" : "MallButton",
                            "type" : "button",
 
                            "x" : 118,
                            "y" : 33-20-3+115 + 35 - 10 + 2,
 
                            "tooltip_text" : uiScriptLocale.MALL2_TITLE,
 
                            "default_image" : "locale/de/ui/icons/lager_buttons.tga",
                            "over_image" : "locale/de/ui/icons/lager_buttons_hover.tga",
                            "down_image" : "locale/de/ui/icons/lager_buttons_hover.tga",
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
                        {
                            "name" : "Equipment_Tab_01",
                            "type" : "radio_button",
							
							"x" : 10,
							"y" : 90,
 
                            "default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                            "over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                            "down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
 
                            "children" :
                            (
                                {
                                    "name" : "Equipment_Tab_01_Print",
                                    "type" : "text",
 
                                    "x" : 0,
                                    "y" : 0,
 
                                    "all_align" : "center",
 
                                    "text" : "I",
                                },
                            ),
                        },
                        {
                            "name" : "Equipment_Tab_02",
                            "type" : "radio_button",
 
							"x" : 10+10+5-1+78,
							"y" : 141,
 
                            "default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                            "over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                            "down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
 
                            "children" :
                            (
                                {
                                    "name" : "Equipment_Tab_02_Print",
                                    "type" : "text",
 
                                    "x" : 0,
                                    "y" : 0,
 
                                    "all_align" : "center",
 
                                    "text" : "II",
                                },
                            ),
                        },
 
                    ),
                },
 
                # {
                    # "name" : "Inventory_Tab_01",
                    # "type" : "radio_button",
 
                    # "x" : 24,
                    # "y" : 189 + 10,
 
                    # "default_image" : "yamato_button/button_middle_n.tga",
                    # "over_image" : "yamato_button/button_middle_h.tga",
                    # "down_image" : "yamato_button/button_middle_p.tga",
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
                # {
                    # "name" : "Inventory_Tab_02",
                    # "type" : "radio_button",
 
                    # "x" : 24 + 78,
                    # "y" : 189 + 10,
                    # "default_image" : "yamato_button/button_middle_n.tga",
                    # "over_image" : "yamato_button/button_middle_h.tga",
                    # "down_image" : "yamato_button/button_middle_p.tga",
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
                # {
                    # "name" : "Inventory_Tab_03",
                    # "type" : "radio_button",
 
                    # "x" : 24,
                    # "y" : 189 + 10 + 20,
 
                    # "default_image" : "yamato_button/button_middle_n.tga",
                    # "over_image" : "yamato_button/button_middle_h.tga",
                    # "down_image" : "yamato_button/button_middle_p.tga",
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
                # {
                    # "name" : "Inventory_Tab_04",
                    # "type" : "radio_button",
 
                    # "x" : 24 + 78,
                    # "y" : 189 + 10 + 20,
 
                    # "default_image" : "yamato_button/button_middle_n.tga",
                    # "over_image" : "yamato_button/button_middle_h.tga",
                    # "down_image" : "yamato_button/button_middle_p.tga",
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
 				## Inventar Seite I
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 24,
					"y" : 33 + 191-22,

					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				## Inventar Seite II
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 24 + 31,
					"y" : 33 + 191-22,

					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},
				## Inventar Seite III
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 24 + 62,
					"y" : 33 + 191-22,

					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},
				## Inventar Seite IV
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",

					"x" : 24 + 93,
					"y" : 33 + 191-22,

					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

					"children" :
					(
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "IV",
						},
					),
				},
				## Inventar Seite V
				{
					"name" : "Inventory_Tab_05",
					"type" : "radio_button",

					"x" : 24 + 124,
					"y" : 33 + 191-22,

					"default_image" : "yamato_button/tab2_pressed.tga",
					"over_image" : "yamato_button/tab2_hovered.tga",
					"down_image" : "yamato_button/tab2_passive.tga",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

					"children" :
					(
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "V",
						},
					),
				},
                ## Item Slot
                {
                    "name" : "ItemSlot",
                    "type" : "grid_table",
 
					# "x" : 23,
					# "y" : 244-20 + 20,
					"x" : 23,
					"y" : 244-20,
					
                    "start_index" : 0,
                    "x_count" : 5,
                    "y_count" : 9,
                    "x_step" : 32,
                    "y_step" : 32,
 
                    "image" : "d:/ymir work/ui/public/slot_base.sub",
                    # "image" : "yamato_slot/slot_main.dds"
                },				
				{
					"name":"Money_Slot",
					"type":"button",
					
					"x":8,
					"y":26+ 15,
					
					"horizontal_align":"center",
					"vertical_align":"bottom",
					
					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					"children" :
					(
						{
							"name":"Money_Icon",
							"type":"image",
							
							"x":-18,
							"y":2,
							
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
				
				##Inventar DC Anzeige
				{
					"name":"DC_Slot",
					"type":"button",
					
					"x":8,
					"y":46+ 15,
					
					"horizontal_align":"center",
					"vertical_align":"bottom",
					
					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					"children" :
					(
						{
							"name":"DC_Icon",
							"type":"image",
							
							"x":-18,
							"y":2,
							
							"image":"d:/ymir work/ui/drachencoins.dds",
						},
						
						{
							"name" : "DC",
							"type" : "text",
							
							"x" : 3,
							"y" : 3,
							
							"horizontal_align" : "right",
							"text_horizontal_align" : "right",
							
							"text" : "123456789 DC's",
						},
					),
				},
				##Inventar AP Anzeige
				{
					"name":"Aps_Slot",
					"type":"button",
					
					"x":8,
					"y":66+ 15,
					
					"horizontal_align":"center",
					"vertical_align":"bottom",
					
					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					"children" :
					(
						{
							"name":"Aps_Icon",
							"type":"image",
							
							"x":-18,
							"y":2,
							
							"image":"d:/ymir work/ui/achievement_small.dds",
						},
						
						{
							"name" : "Aps",
							"type" : "text",
							
							"x" : 3,
							"y" : 3,
							
							"horizontal_align" : "right",
							"text_horizontal_align" : "right",
							
							"text" : "123456789 AP's",
						},
					),
				},
				##Inventar Dailypoint Anzeige
				{
					"name":"Dps_Slot",
					"type":"button",
					
					"x":8,
					"y":86+ 15,
					
					"horizontal_align":"center",
					"vertical_align":"bottom",
					
					"default_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_05.sub",
					
					"children" :
					(
						{
							"name":"Dps_Icon",
							"type":"image",
							
							"x":-18,
							"y":2,
							
							"image":"d:/ymir work/ui/daily.dds",
						},
						
						{
							"name" : "DPs",
							"type" : "text",
							
							"x" : 3,
							"y" : 3,
							
							"horizontal_align" : "right",
							"text_horizontal_align" : "right",
							
							"text" : "123456789 DP's",
						},
					),
				},
				{			
					"name" : "DropDownBoard",
					"type" : "slotbar",
					"x" : 120+10-85,
					"y" : 94,
					"width" : 80,
					"height" : 55+20+20+20,
					
					"children" :
					(
						{
							"name" : "DropDownButton1",
							"type" : "button",
							"text" : "I-Lager",
							
							"x" : 10,
							"y" : 8,

							"tooltip_text" : "Itemlager",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},	
						{
							"name" : "DropDownButton2",
							"type" : "button",
							"text" : "IS-Lager",
							
							"x" : 10,
							"y" : 28,

							"tooltip_text" : "Itemshop-Lager",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},	
						{
							"name" : "DropDownButton3",
							"type" : "button",
							"text" : "G-Lager",
							
							"x" : 10,
							"y" : 48,

							"tooltip_text" : "Gildenlager",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},	
						
						{
							"name" : "DropDownButton4",
							"type" : "button",
							"text" : "FB-Lager",
							
							"x" : 10,
							"y" : 68,

							"tooltip_text" : "Fertigkeitsbucher-Lager",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},
						{
							"name" : "DropDownButton5",
							"type" : "button",
							"text" : "Upp-Lager",
							
							"x" : 10,
							"y" : 88,

							"tooltip_text" : "UppItem-Lager",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},
												
						
						
						
						
						
					),
				},
				
				{			
					"name" : "DropDownBoard2",
					"type" : "slotbar",
					"x" : 120+10-85,
					"y" : 94,
					"width" : 80,
					"height" : 55+20,
					
					"children" :
					(
						{
							"name" : "DropDownButton2_1",
							"type" : "button",
							"text" : "100kk",
							
							"x" : 10,
							"y" : 8,

							"tooltip_text" : "100kk Yangbarren erstellen",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},	
						{
							"name" : "DropDownButton2_2",
							"type" : "button",
							"text" : "500kk",
							
							"x" : 10,
							"y" : 28,

							"tooltip_text" : "500kk Yangbarren erstellen",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},	
						{
							"name" : "DropDownButton2_3",
							"type" : "button",
							"text" : "1kkk",
							
							"x" : 10,
							"y" : 48,

							"tooltip_text" : "1kkk Yangbarren erstellen",
							"default_image" : "d:/ymir work/ui/public/Middle_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Middle_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Middle_Button_03.sub",
						},						
					),
				},

            ),
        },
    ),
}