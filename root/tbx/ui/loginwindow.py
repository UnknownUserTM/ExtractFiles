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
							
							"text" : "Schlieﬂen",
						},
						{
							"name" : "save_button",
							"type" : "button",
							"x" : 123, "y" : 250,

							"default_image" : "yamato_helpboard/wide_button_n.tga", 
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							
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
					"name" : "account_management",
					"type" : "window",
					
					"x" : SCREEN_WIDTH - 220,
					"y" : SCREEN_HEIGHT - 200,
					
					
					"width" : 190,
					"height" : 120,
					
				
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
						
					
					),
				
				},
			),
		},

	),
}