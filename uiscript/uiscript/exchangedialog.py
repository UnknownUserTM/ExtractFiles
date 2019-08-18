import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"
FACE_SLOT_FILE = "d:/ymir work/ui/game/windows/box_face.sub"

window = {
	"name" : "ExchangeDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 446-25-15+55+35,
	"height" : 250-10-35+35,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 446-25-15+55+39,
			"height" : 250-10-35+35,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,
 
					"width" : 446-12 - 51 + 10 + 92,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":133+215-173+50+8 - 20 - 30 - 25 - 15 + 95, "y":3, "text":uiScriptLocale.EXCHANGE_TITLE, "text_horizontal_align":"center" },
					),
				},

				#karakter bilgileri:
					#Rakibin
				{ "name" : "Face_Slot", "type" : "image", "x" : 15, "y" : 36, "image" : FACE_SLOT_FILE, },
				{
					"name" : "karakter",
					"type" : "image",

					"x" : 18,
					"y" : 36+5,

					"image" : "icon/face/warrior_m.tga",

				},

				{
					"name" : "level",
					"type" : "text",

					"x" : 61+7,
					"y" : 36,

					"text" : "Lv. 0",

				},

				{
					"name" : "name",
					"type" : "text",

					"x" : 104-16+7 + 4,
					"y" : 36,

					"text" : "Fatihbab34",

				},

				{
					"name" : "lonca",
					"type" : "text",

					"x" : 61+7,
					"y" : 50-7+11 - 5,

					"text" : "TURKIYE",

				},
					#benim#
				{ "name" : "Face_Slot2", "type" : "image", "x" : 240-3-15+50, "y" : 36, "image" : FACE_SLOT_FILE, },
				{
					"name" : "benim_karakter",
					"type" : "image",

					"x" : 240-15+50,
					"y" : 36+5,

					"image" : "icon/face/warrior_m.tga",

				},

				{
					"name" : "benim_name",
					"type" : "text",

					"x" : 296 - 4-15+47,
					"y" : 31 + 6,

					"text" : "Sen",

				},

				## MiddleBar
				{
					"name" : "Middle_Bar",
					"type" : "image",

					"x" : 139 + 9000,
					"y" : 31,

					"image" : ROOT + "windows/middlebar.sub",
				},


				{
					"name" : "Middle_Bar2",
					"type" : "image",

					"x" : 139+9000,
					"y" : 95,

					"image" : ROOT + "windows/middlebar.sub",
				},

				

				#yang dialog yeri
				{
					"name" : "Owner_Money",
					"type" : "button",

					"x" : 292-1-15+50,
					"y" : 59+11-3,

					"default_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
					"over_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",
					"down_image" : "d:/ymir work/ui/public/parameter_slot_03.sub",

					"children" :
					(
						{
							"name" : "Owner_Money_Value",
							"type" : "text",

							"x" : 59 + 35 - 6,
							"y" : 2,

							"text" : "1234567",

							"text_horizontal_align" : "right",
						},

						{
							"name" : "Owner_Money_Value2",
							"type" : "text",

							"x" : 59+29 + 28 + 9000,#-
							"y" : 2,

							"text" : "Yang",

							"text_horizontal_align" : "right",
						},
					),
				},

				## Owner
				{
					"name" : "Owner",
					"type" : "window",

					"x" : 234 + 6 + 15 - 15 + 39,
					"y" : 87 + 18 - 10,

					"width" : 130,
					"height" : 130 + 96,

					"children" :
					(
						{
							"name" : "Owner_Slot",
							"type" : "grid_table",

							"x" : 0,
							"y" : 0,

							"start_index" : 0,
							"x_count" : 6,
							"y_count" : 4,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,


							"image" : "d:/ymir work/ui/public/slot_base.sub",
						},
						
					),
				},

				{
					"name" : "Owner_Accept_Light",#aktif hali eklenicek.
					"type" : "button",

					"x" : 292-1 + 92 - 15 + 50,
					"y" : 59+11-3,

					"default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
					"over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
					"down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",
				},

				#{
				#	"name" : "Owner_Accept_Light",#aktif hali eklenicek.
				#	"type" : "toggle_button",

				#	"x" : 234 + 6 + 9000,
				#	"y" : 87 + 15 - 10,

				#	"default_image" : "locale/tr/ui/xd.tga",
				#	"over_image" : "locale/tr/ui/kabuletti.tga",
				#	"down_image" : "locale/tr/ui/kabuletti.tga",
				#},

				
				
				#kabulet
				{
					"name" : "Owner_Accept_Button",
					"type" : "toggle_button",

					"x" : 209 - 7 + 3 - 14 - 9 - 15 + 51,
					"y" : 58+92,

					"text" : "Akzeptieren",

					#"default_image" : "locale/tr/ui/ticaret.tga",
					#"over_image" : "locale/tr/ui/ticaret.tga",
					#"down_image" : "locale/tr/ui/ticaret.tga",
					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				{
					"name" : "Target_Money",
					"type" : "image",

					"x" : 62 + 6,
					"y" : 56 + 9 + 2,

					"image" : "d:/ymir work/ui/public/parameter_slot_03.sub",

					"children" :
					(
						{
							"name" : "Target_Money_Value",
							"type" : "text",

							"x" : 59+35-6,
							"y" : 2,

							"text" : "1234567",

							"text_horizontal_align" : "right",
						},

						{
							"name" : "Target_Money_Value2",
							"type" : "text",

							"x" : 59+29 + 28 + 9000,#-
							"y" : 2,

							"text" : "Yang",

							"text_horizontal_align" : "right",
						},
					),
				},
				
				
				## Target
				{
					"name" : "Target",
					"type" : "window",

					"x" : 10 + 15,
					"y" : 87 + 18 - 10,

					"width" : 130,
					"height" : 130 + 96,

					"children" :
					(
						{
							"name" : "Target_Slot",
							"type" : "grid_table",

							"x" : 0,
							"y" : 0,

							"start_index" : 0,
							"x_count" : 6,
							"y_count" : 4,
							"x_step" : 32,
							"y_step" : 32,
							"x_blank" : 0,
							"y_blank" : 0,

							"image" : "d:/ymir work/ui/public/slot_base.sub",
						},
						
					),
				},

				{
					"name" : "Target_Accept_Light", #aktif koyulcak
					"type" : "button",

					"x" : 62 + 6 + 92,
					"y" : 56 + 9 + 2,

					"default_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
					"over_image" : "d:/ymir work/ui/game/windows/accept_button_off.sub",
					"down_image" : "d:/ymir work/ui/game/windows/accept_button_on.sub",
				},
			),
		},
	),
}