import uiScriptLocale

WINDOW_WIDTH = 350
WINDOW_HEIGTH = 405

window = {
	"name" : "ItemMakerWindow",
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
					"name" : "itemMakerBackground",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 30 + 20,
					"height" : WINDOW_HEIGTH - 30  + 40 - 5,
					
					
					"children" : (
					
						{
							"name" : "itemVnumBoard",
							"type" : "thinboard_circle",
							
							
							"x" : 0,
							"y" : 0,
							
							"width" : WINDOW_WIDTH - 30 + 20,
							"height" : 20,
							
							"children" : (
								{
									"name" : "vnumInputEditLine",
									"type" : "editline",
													
									"x" : 7,
									"y" : 4,
													
									"input_limit" : 20,
									
									"text" : "19",
													
									"width" : WINDOW_WIDTH - 30 + 20,
									"height" : 20,
								},
								{
									"name" : "itemVnumInfoTextLine",
									"type" : "text",
									
									"x" : 7,
									"y" : 4,
								
									"text" : "Schwert+9",
									"outline" : 1,
									"text_horizontal_align" : "right",
									"horizontal_align" : "right",								
								
								},
							),						
						
						
						},
						{
							"name" : "socketBoard",
							"type" : "thinboard_circle",
							
							
							"x" : 5,
							"y" : 22 + 4,
							
							"width" : WINDOW_WIDTH - 30 + 20 - 10,
							"height" : 20,
						
							"children" : (
							
							
								{
									"name" : "socketTitle",
									"type" : "text",
									
									"x" : 0,
									"y" : 4,
								
									"text" : "Sockets",
									"outline" : 1,
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",								
								
								},
							
							),
						
						},
						
						# {
							# "name" : "socketBoard_0",
							# "type" : "thinboard_circle",
							
							
							# "x" : 10,
							# "y" : 22 + 4 + 26,
							
							# "width" : WINDOW_WIDTH - 30 + 20 - 20,
							# "height" : 20,
							
							# "children" : (
							
								# {
									# "name" : "socketTextLine_0",
									# "type" : "text",
									
									# "x" : 0,
									# "y" : 4,
								
									# "text" : "0",
									# "outline" : 1,
									# "text_horizontal_align" : "center",
									# "horizontal_align" : "center",								
								# },
							# ),
						# },						
						{
							"name" : "attributeBoard",
							"type" : "thinboard_circle",
							
							
							"x" : 5,
							"y" : 22 + 4 + 180 -18,
							
							"width" : WINDOW_WIDTH - 30 + 20 - 10,
							"height" : 20,
						
							"children" : (
							
							
								{
									"name" : "attrTitle",
									"type" : "text",
									
									"x" : 0,
									"y" : 4,
								
									"text" : "Attributes",
									"outline" : 1,
									"text_horizontal_align" : "center",
									"horizontal_align" : "center",								
								
								},
							
							),
						
						},	

						{
							"name" : "makeItemButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35,
									
							"text" : "Make!",
							
							"vertical_align" : "bottom",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},


						
					),
			
				},
				
				{
					"name" : "socketTypeSelectBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 30 + 20,
					"height" : WINDOW_HEIGTH - 30  + 40 - 5,
					
				
					"children" : (
						{
							"name" : "descSocketType",
							"type" : "text",
									
							"x" : 0,
							"y" : 4 - 100,
								
							"text" : "Was willst du in den Socket einfügen?",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
						},					
						{
							"name" : "socket_ghostStoneButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 - 100,
									
							"text" : "Geiststein",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "socket_timeButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 - 100,
									
							"text" : "Zeit",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},					
						{
							"name" : "socket_valueButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 + 30 - 100,
									
							"text" : "Wert",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},	
						{
							"name" : "socket_closeButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 + 30 + 30 + 15 - 100,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},							
					),
				},
				{
					"name" : "socketVnumSelectBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 30 + 20,
					"height" : WINDOW_HEIGTH - 30  + 40 - 5,
					
				
					"children" : (
						{
							"name" : "descSocketVnum",
							"type" : "text",
									
							"x" : 0,
							"y" : 4 - 100 - 80,
								
							"text" : "Wähle einen Geiststein den du einfügen möchtest.",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
						},		
						{
							"name" : "stoneListBoxBackground",
							"type" : "thinboard_circle",
							
							"x" : 0, 
							"y" : 4 - 100 + 20 + 90 - 80,
						
							"width" : 160,
							"height" : 165,
							"horizontal_align" : "center",								
							"vertical_align" : "center",

							"children" : (
								{	
									"name" : "stoneListBox",
									"type" : "listbox",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 160,
									"height" : 165,
								},
								{
									"name" : "stoneListBoxScrollBar",
									"type" : "small_thin_scrollbar",
											
									"x" : 160 - 15 + 1,
									"y" : 1,
											
									"size" : 164,
								},							
							
							
							
							),
						
						},
						{
							"name" : "socket_AddButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 100 - 80,
									
							"text" : "Einfügen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "socket_vnumCloseButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 + 100 - 80,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
					),
				},
				{
					"name" : "socketTimeBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 30 + 20,
					"height" : WINDOW_HEIGTH - 30  + 40 - 5,
					
				
					"children" : (
						{
							"name" : "descSocketTimeType",
							"type" : "text",
									
							"x" : 0,
							"y" : 4 - 100,
								
							"text" : "Gib an wielange das item laufen soll. (In Minuten)",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
						},					
						
						
						{
							"name" : "socketTimeEditLineBoard",
							"type" : "thinboard_circle",
							
							
							"x" : 0,
							"y" : 4 - 100 + 27,
							
							"width" : 161,
							"height" : 20,
							
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
							
							"children" : (
								{
									"name" : "socketTimeEditLine",
									"type" : "editline",
													
									"x" : 7,
									"y" : 4,
													
									"input_limit" : 20,
									
									"text" : "0",
													
									"width" : WINDOW_WIDTH - 30 + 20,
									"height" : 20,
								},
							),
						},
						
						{
							"name" : "socket_addTimeButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 - 100 + 30,
									
							"text" : "Einfügen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "socket_closeTimeButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 - 100 + 30,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},					
						
					),
				},
				{
					"name" : "socketValueBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 30 + 20,
					"height" : WINDOW_HEIGTH - 30  + 40 - 5,
					
				
					"children" : (
						{
							"name" : "descSocketValueType",
							"type" : "text",
									
							"x" : 0,
							"y" : 4 - 100,
								
							"text" : "Gib einen Wert für den Socket ein.",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
						},					
						
						
						{
							"name" : "socketValueEditLineBoard",
							"type" : "thinboard_circle",
							
							
							"x" : 0,
							"y" : 4 - 100 + 27,
							
							"width" : 161,
							"height" : 20,
							
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
							
							"children" : (
								{
									"name" : "socketValueEditLine",
									"type" : "editline",
													
									"x" : 7,
									"y" : 4,
													
									"input_limit" : 20,
									
									"text" : "0",
													
									"width" : WINDOW_WIDTH - 30 + 20,
									"height" : 20,
								},
							),
						},
						
						{
							"name" : "socket_addValueButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 - 100 + 30,
									
							"text" : "Einfügen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "socket_closeValueButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 - 100 + 30,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},					
						
					),
				},	

				{
					"name" : "attributeSelectBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 30 + 20,
					"height" : WINDOW_HEIGTH - 30  + 40 - 5,
					
				
					"children" : (
						{
							"name" : "descAttr",
							"type" : "text",
									
							"x" : 0,
							"y" : 4 - 100 - 80,
								
							"text" : "Wähle einen Bonus aus der Liste.",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
						},		
						{
							"name" : "attrListBoxBackground",
							"type" : "thinboard_circle",
							
							"x" : 0, 
							"y" : 4 - 100 + 20 + 90 - 80 + 5,
						
							"width" : 190,
							"height" : 165 + 30,
							"horizontal_align" : "center",								
							"vertical_align" : "center",

							"children" : (
								{	
									"name" : "attrListBox",
									"type" : "listbox",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 190,
									"height" : 165 + 30,
								},
								{
									"name" : "attrListBoxScrollBar",
									"type" : "small_thin_scrollbar",
											
									"x" : 190 - 15 + 1,
									"y" : 1,
											
									"size" : 165 + 30 - 1,
								},							
							
							
							
							),
						
						},
						{
							"name" : "specialAttrListBoxBackground",
							"type" : "thinboard_circle",
							
							"x" : 0, 
							"y" : 4 - 100 + 20 + 90 - 80 + 5,
						
							"width" : 190,
							"height" : 165 + 30,
							"horizontal_align" : "center",								
							"vertical_align" : "center",

							"children" : (
								{	
									"name" : "specialAttrListBox",
									"type" : "listbox",
									
									"x" : 0,
									"y" : 0,
									
									"width" : 190,
									"height" : 165 + 30,
								},
								{
									"name" : "specialAttrListBoxScrollBar",
									"type" : "small_thin_scrollbar",
											
									"x" : 190 - 15 + 1,
									"y" : 1,
											
									"size" : 165 + 30 - 1,
								},							
							),
						},
						{
							"name" : "attr_SwitchTo67AttrButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 100 - 80,
									
							"text" : "Zu 6&7 Boni wechseln.",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "attr_BackTo15AttrButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 100 - 80,
									
							"text" : "Zurück",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "attr_AddButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 100 - 80 + 30,
									
							"text" : "Einfügen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "attr_CloseButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 + 100 - 80 + 30,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
					),
				},
				{
					"name" : "attrChangeValueBoard",
					"type" : "thinboard_circle",
					
					"x" : 20,
					"y" : 10,
					
					"width" : WINDOW_WIDTH - 30 + 20,
					"height" : WINDOW_HEIGTH - 30  + 40 - 5,
					
				
					"children" : (
						{
							"name" : "descAttrChangeValueType",
							"type" : "text",
									
							"x" : 0,
							"y" : 4 - 100,
								
							"text" : "Gib einen Wert zwischen 0 und 32.767 ein.",
							"outline" : 1,
							"text_horizontal_align" : "center",
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
						},					
						
						
						{
							"name" : "attrChangeEditLineBoard",
							"type" : "thinboard_circle",
							
							
							"x" : 0,
							"y" : 4 - 100 + 27,
							
							"width" : 161,
							"height" : 20,
							
							"horizontal_align" : "center",								
							"vertical_align" : "center",	
							
							"children" : (
								{
									"name" : "attrChangeEditLine",
									"type" : "editline",
													
									"x" : 7,
									"y" : 4,
													
									"input_limit" : 20,
									
									"text" : "0",
													
									"width" : WINDOW_WIDTH - 30 + 20,
									"height" : 20,
								},
							),
						},
						
						{
							"name" : "attrChange_addValueButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 - 100 + 30,
									
							"text" : "Einfügen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},
						{
							"name" : "attrChange_closeValueButton",
							"type" : "button",
									
							"x" : 0,
							"y" : 35 + 30 - 100 + 30,
									
							"text" : "Schließen",
							
							"vertical_align" : "center",
							"horizontal_align" : "center", 
							
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",			
						},					
						
					),
				},				
			),
		},
	),
}

