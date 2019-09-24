import app
import uiScriptLocale

window = {
	"sytle" : ("movable",),
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,
	"children" : (

		{
			"name" : "background", 
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image" : "yamato_login/bg.jpg",
			"children" : (

				{
					"name" : "tbx",
					"type" : "image",
					"x" : 0, "y" : 90,
					"horizontal_align" : "center",
					"vertical_align" : "top",
					"image" : "tbx/loginwindow/tbx.tga",
				},
				{
					"name" : "board",
					"type" : "image",
					"x" : 0, "y" : 50,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : "yamato_login/scroll_bg.tga",
					"children" : (
						{
							"name" : "slotbar_background",
							"type" : "image",
							"x" : 0, "y" : 80,
							"horizontal_align" : "center",
							"image" : "yamato_login/login_form.tga",
							"children" : (
								{
									"name": "id",
									"type": "editline",
									"x": 22,
									"y": 35,
									"width": 284,
									"height": 43,
									"input_limit": 16,
									"enable_codepage": 0,
								},
								{
									"name": "pwd",
									"type": "editline",
									"x": 22,
									"y": 95,
									"width": 284,
									"height": 43,
									"input_limit": 16,
									"enable_codepage": 0,
									"secret_flag" : 1,
								},							
							
							),
						},

						{
							"name" : "enter_button",
							"type" : "button",
							"x" : 0 + 106, "y" : 220,
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							
							"text" : "Einloggen",
						},
						{
							"name" : "exit_button",
							"type" : "button",
							"x" : 100 + 106, "y" : 220,
							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							
							"text" : "Schließen",
						},
						{
							"name" : "save_button",
							"type" : "button",
							"x" : 123, "y" : 250,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "Speichern",
						},
						
						{
							"name" : "channel_background",
							"type" : "image",
							"x" : 106,
							"y" : 290,

							"image" : "yamato_login/channel_box.tga",
						},
						{
							"name" : "LanguageBoard",
							"type" : "window",
							"x" : 156,
							"y" : 450,
							"width" : 375,
							"height" : 40,
							"horizontal_align" : "center",
						},						

						{
							"name" : "delete_main_button",
							"type" : "button",
							"x" : 70, "y" : 120,
							"horizontal_align" : "center",
							"vertical_align" : "center",
							"default_image" : "tbx/loginwindow/delete_main_0.tga", 
							"over_image" : "tbx/loginwindow/delete_main_1.tga",
							"down_image" : "tbx/loginwindow/delete_main_2.tga",
						},


					),
				},
				
				{
					"name" : "pasteBoard",
					"type" : "board",
					
					"x" : 0, 
					"y" : 0,
					
					"width" : 300,
					"height" : 280,
					
					"horizontal_align" : "center",
					"vertical_align" : "center",
					
					"children" : (
						
						{
							"name" : "pasteBoardDescBoard",
							"type" : "thinboard_circle",
							
							"x" : 15 + 3,
							"y" : 5 + 3,
							
							"width" : 300 - 30 - 10 + 3,
							"height" : 22,
							
							"children" : (
								{
									"name" : "pasteBoardDescTextLine",
									"type" : "text",
									
									"x" : 7,
									"y" : 4,
									
									"text" : "Drücke STRG+V um die kopierten Daten in das Feld zu laden, klicke anschließend auf Laden.",
									"outline" : 1,
								
								
								
								},
							
							
							
							),
						},
						{
							"name" : "pasteBoardEditLineBoard",
							"type" : "thinboard_circle",
							
							"x" : 15 + 3,
							"y" : 5 + 3 + 22,
							
							"width" : 300 - 30 - 10 + 3,
							"height" : 210 - 3,
							
							"children" : (
							
								{
									"name" : "pasteBoardEditLine",
									"type" : "editline",
													
									"x" : 7,
									"y" : 4,
									
									"width" : 300 - 30 - 10 + 3,
									"height" : 210 - 3,	
									
									"with_codepage" : 1,
									"input_limit" : 200,	
									"limit_width" : 300,
									# "multi_line" : 1,
													

								},
							
							),
						},					
						{
							"name" : "acceptPasteButton",
							"type" : "button",
							"x" : -50, 
							"y" : 5 + 3 + 22 + 213 - 5,

							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",
							
							"horizontal_align" : "center",
							# "vertical_align" : "center",
					
							"text" : "Laden",
						},						
						{
							"name" : "cancelPasteButton",
							"type" : "button",
							"x" : 50, 
							"y" : 5 + 3 + 22 + 213 - 5,

							"default_image" : "yamato_helpboard/normal_button_n.tga", 
							"over_image" : "yamato_helpboard/normal_button_h.tga",
							"down_image" : "yamato_helpboard/normal_button_p.tga",
							"disable_image" : "yamato_helpboard/normal_button_d.tga",
							
							"horizontal_align" : "center",
							# "vertical_align" : "center",
					
							"text" : "Schließen",
						},						
					),
				},
				{
					"name" : "account_management",
					"type" : "window",
					
					"x" : SCREEN_WIDTH - 220,
					"y" : SCREEN_HEIGHT - 400,
					
					
					"width" : 230,
					"height" : 300,
					
				
					"children" : (
					
					
						{
							"name" : "account_button_textline_0",
							"type" : "text",
							"x" : -25, 
							"y" : 9,
							"text" : "[ F1 ] ",
							"outline" : 1,
						},
						{
							"name" : "account_button_0",
							"type" : "button",
							"x" : 5, "y" : 5,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_0",
							"type" : "button",
							"x" : 145, "y" : 5,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
							
							
						},						
						{
							"name" : "account_button_textline_1",
							"type" : "text",
							"x" : -25, 
							"y" : 9 + 30,
							"text" : "[ F2 ] ",
							"outline" : 1,
						},						
						{
							"name" : "account_button_1",
							"type" : "button",
							"x" : 5, "y" : 5 + 30,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_1",
							"type" : "button",
							"x" : 145, "y" : 5 + 30,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
							
							
						},
						{
							"name" : "account_button_textline_2",
							"type" : "text",
							"x" : -25, 
							"y" : 9 + 60,
							"text" : "[ F3 ] ",
							"outline" : 1,
						},
						{
							"name" : "account_button_2",
							"type" : "button",
							"x" : 5, "y" : 5 + 60,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_2",
							"type" : "button",
							"x" : 145, "y" : 5 + 60,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
							
							
						},	

						{
							"name" : "account_button_textline_3",
							"type" : "text",
							"x" : -25, 
							"y" : 9 + 60 + 30,
							"text" : "[ F4 ] ",
							"outline" : 1,
						},
						{
							"name" : "account_button_3",
							"type" : "button",
							"x" : 5, "y" : 5 + 60 + 30,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_3",
							"type" : "button",
							"x" : 145, "y" : 5 + 60 + 30,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
						},						

						{
							"name" : "account_button_textline_4",
							"type" : "text",
							"x" : -25, 
							"y" : 9 + 60 + 30 + 30,
							"text" : "[ F5 ] ",
							"outline" : 1,
						},
						{
							"name" : "account_button_4",
							"type" : "button",
							"x" : 5, "y" : 5 + 60 + 30 + 30,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_4",
							"type" : "button",
							"x" : 145, "y" : 5 + 60 + 30 + 30,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
						},							

						{
							"name" : "account_button_textline_5",
							"type" : "text",
							"x" : -25, 
							"y" : 9 + 60 + 30 + 30 + 30,
							"text" : "[ F6 ] ",
							"outline" : 1,
						},
						{
							"name" : "account_button_5",
							"type" : "button",
							"x" : 5, "y" : 5 + 60 + 30 + 30 + 30,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_5",
							"type" : "button",
							"x" : 145, "y" : 5 + 60 + 30 + 30 + 30,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
						},


						{
							"name" : "account_button_textline_6",
							"type" : "text",
							"x" : -25, 
							"y" : 9 + 60 + 30 + 30 + 30 + 30,
							"text" : "[ F7 ] ",
							"outline" : 1,
						},
						{
							"name" : "account_button_6",
							"type" : "button",
							"x" : 5, "y" : 5 + 60 + 30 + 30 + 30 + 30,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_6",
							"type" : "button",
							"x" : 145, "y" : 5 + 60 + 30 + 30 + 30 + 30,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
						},
						
						
						{
							"name" : "account_button_textline_7",
							"type" : "text",
							"x" : -25, 
							"y" : 9 + 60 + 30 + 30 + 30 + 30 + 30,
							"text" : "[ F8 ] ",
							"outline" : 1,
						},
						{
							"name" : "account_button_7",
							"type" : "button",
							"x" : 5, "y" : 5 + 60 + 30 + 30 + 30 + 30 + 30,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "leer",
						},						
						{
							"name" : "account_delete_button_7",
							"type" : "button",
							"x" : 145, "y" : 5 + 60 + 30 + 30 + 30 + 30 + 30,

							"default_image" : "yamato_button/close_n.dds", 
							"over_image" : "yamato_button/close_h.dds",
							"down_image" : "yamato_button/close_p.dds",
							"disable_image" : "yamato_button/close_d.dds",
						},
						
						
						{
							"name" : "new_secure_register_button",
							"type" : "button",
							"x" : 5, "y" : 5 + 60 + 30 + 30 + 30 + 30 + 30 + 30 + 15,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
							
							"text" : "Accountdaten einfügen (TEST)",
						},
					
					),
				
				},
			),
		},

	),
}