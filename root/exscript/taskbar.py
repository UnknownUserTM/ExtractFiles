import uiScriptLocale
import app

ROOT = "d:/ymir work/ui/game/"

Y_ADD_POSITION = 0

window = {
	"name" : "TaskBar",

	"x" : 0,
	"y" : SCREEN_HEIGHT - 44,

	"width" : SCREEN_WIDTH,
	"height" : 45,

	"children" :
	(
		## Board
		{
			"name" : "Base_Board_01",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 23,

			"rect" : (0.0, 0.0, float(SCREEN_WIDTH - 65) / 65.0, 0.0),

			"image" : "yamato_taskbar/right_border_ornament_repeater.tga"
		},
		## Board
		{
			"name" : "Base_Board_02",
			"type" : "expanded_image",

			"x" : (SCREEN_WIDTH / 2) - 270,
			"y" : -26,


			"image" : "yamato_taskbar/main_menu_texture.tga"
		},
		## Gauge
		{
			"name" : "Gauge_Board",
			"type" : "image",

			"x" : 0,
			"y" : -10 + Y_ADD_POSITION,

			"image" : ROOT + "taskbar/gauge.sub",

			"children" :
			(
				{
					"name" : "RampageGauge",
					"type" : "ani_image",

					"x" : 8,
					"y" : 4,
					"width"  : 40,
					"height" : 40,

					"delay" : 6,

					"images" :
					(
						"locale/de/ui/Mall/00.sub",
						"locale/de/ui/Mall/01.sub",
						"locale/de/ui/Mall/02.sub",
						"locale/de/ui/Mall/03.sub",
						"locale/de/ui/Mall/04.sub",
						"locale/de/ui/Mall/05.sub",
						"locale/de/ui/Mall/06.sub",
						"locale/de/ui/Mall/07.sub",
						"locale/de/ui/Mall/08.sub",
						"locale/de/ui/Mall/09.sub",
						"locale/de/ui/Mall/11.sub",
						"locale/de/ui/Mall/12.sub",
						"locale/de/ui/Mall/13.sub",
						"locale/de/ui/Mall/14.sub",
						"locale/de/ui/Mall/15.sub",
						"locale/de/ui/Mall/16.sub",
					)
				},
				{
					"name" : "RampageGauge2",
					"type" : "ani_image",

					"x" : 8,
					"y" : 4,
					"width"  : 40,
					"height" : 40,

					"delay" : 6,

					"images" :
					(
						"locale/de/ui/Mall/00.sub",
						"locale/de/ui/Mall/01.sub",
						"locale/de/ui/Mall/02.sub",
						"locale/de/ui/Mall/03.sub",
						"locale/de/ui/Mall/04.sub",
						"locale/de/ui/Mall/05.sub",
						"locale/de/ui/Mall/06.sub",
						"locale/de/ui/Mall/07.sub",
						"locale/de/ui/Mall/08.sub",
						"locale/de/ui/Mall/09.sub",
						"locale/de/ui/Mall/11.sub",
						"locale/de/ui/Mall/12.sub",
						"locale/de/ui/Mall/13.sub",
						"locale/de/ui/Mall/14.sub",
						"locale/de/ui/Mall/15.sub",
						"locale/de/ui/Mall/16.sub",
					)
				},
				## TP Anzeige
				{
					"name" : "HPGauge_Board",
					"type" : "window",

					"x" : 59,
					"y" : 14,

					"width" : 95,
					"height" : 11,

					"children" :
					(
						{
							"name" : "HPRecoveryGaugeBar",
							"type" : "bar",

							"x" : 0,
							"y" : 0,
							"width" : 95,
							"height" : 13,
							"color" : 0x55ff0000,
						},
						{
							"name" : "HPGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/HPGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/HPGauge/07.tga",
							),
						},
					),
				},
				## MP Anzeige
				{
					"name" : "SPGauge_Board",
					"type" : "window",

					"x" : 59,
					"y" : 24,

					"width" : 95,
					"height" : 11,

					"children" :
					(
						{
							"name" : "SPRecoveryGaugeBar",
							"type" : "bar",

							"x" : 0,
							"y" : 0,
							"width" : 95,
							"height" : 13,
							"color" : 0x550000ff,
						},
						{
							"name" : "SPGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/SPGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/SPGauge/07.tga",
							),
						},
					),
				},
				## AP Anzeige
				{
					"name" : "STGauge_Board",
					"type" : "window",

					"x" : 59,
					"y" : 38,

					"width" : 95,
					"height" : 6,

					"children" :
					(
						{
							"name" : "STGauge",
							"type" : "ani_image",

							"x" : 0,
							"y" : 0,

							"delay" : 6,

							"images" :
							(
								"D:/Ymir Work/UI/Pattern/STGauge/01.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/02.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/03.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/04.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/05.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/06.tga",
								"D:/Ymir Work/UI/Pattern/STGauge/07.tga",
							),
						},
					),
				},
			),
		},
		## EXP Anzeige
		{
			"name" : "EXP_Gauge_Board",
			"type" : "image",

			"x" : 158,
			"y" : 0 + Y_ADD_POSITION,

			"image" : ROOT + "taskbar/exp_gauge.sub",

			"children" :
			(
				{
					"name" : "EXPGauge_01",
					"type" : "expanded_image",

					"x" : 5,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
				{
					"name" : "EXPGauge_02",
					"type" : "expanded_image",

					"x" : 30,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
				{
					"name" : "EXPGauge_03",
					"type" : "expanded_image",

					"x" : 55,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
				{
					"name" : "EXPGauge_04",
					"type" : "expanded_image",

					"x" : 80,
					"y" : 9,

					"image" : ROOT + "TaskBar/EXP_Gauge_Point.sub",
				},
			),
		},
		## Mouse Button
		{
			"name" : "LeftMouseButton",
			"type" : "button",

			"x" : SCREEN_WIDTH/2 - 128 - 95,
			"y" : 3 + Y_ADD_POSITION + 5,

			"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
			"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
			"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
		},
		{
			"name" : "RightMouseButton",
			"type" : "button",

			"x" : SCREEN_WIDTH/2 + 128 + 66 + 11 - 10,
			"y" : 3 + Y_ADD_POSITION + 5,

			"default_image" : ROOT + "TaskBar/Mouse_Button_Move_01.sub",
			"over_image" : ROOT + "TaskBar/Mouse_Button_Move_02.sub",
			"down_image" : ROOT + "TaskBar/Mouse_Button_Move_03.sub",
		},
		## Charakter Button
		{
			"name" : "CharacterButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 144 -6 - 12 - 23 - 45,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_CHARACTER,

			"default_image" : "yamato_taskbar/character_n.tga",
			"over_image" : "yamato_taskbar/character_h.tga",
			"down_image" : "yamato_taskbar/character_p.tga",
		},
		## Quest Button
		{
			"name" : "QuestButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 144 -6 - 12 - 23,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : "Quests [N]",

			"default_image" : "yamato_taskbar/ability1_n.tga",
			"over_image" : "yamato_taskbar/ability1_h.tga",
			"down_image" : "yamato_taskbar/ability1_p.tga",
		},
		## Inventory Button
		{
			"name" : "InventoryButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 110 - 6 - 12 - 13,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_INVENTORY,

			"default_image" : "yamato_taskbar/inventory_n.tga",
			"over_image" : "yamato_taskbar/inventory_h.tga",
			"down_image" : "yamato_taskbar/inventory_p.tga",
		},
		## Freundesliste Button
		{
			"name" : "MessengerButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 76 - 6 - 12 - 5,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_MESSENGER,

			"default_image" : "yamato_taskbar/mail_n.tga",
			"over_image" : "yamato_taskbar/mail_h.tga",
			"down_image" : "yamato_taskbar/mail_p.tga",
		},
		## System Button
		{
			"name" : "SystemButton",
			"type" : "button",

			"x" : SCREEN_WIDTH - 42 - 12,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

			"default_image" : "yamato_taskbar/settings_n.tga",
			"over_image" : "yamato_taskbar/settings_h.tga",
			"down_image" : "yamato_taskbar/settings_p.tga",
		},
		
		## Calender Button
		{
			"name" : "CalenderButton",
			"type" : "button",

			"x" : 15,
			"y" : 3 + Y_ADD_POSITION,

			"default_image" : "yamato_taskbar/calendar_n.tga",
			"over_image" : "yamato_taskbar/calendar_h.tga",
			"down_image" : "yamato_taskbar/calendar_p.tga",
		},
		## Biologist Button
		{
			"name" : "BonusBoardButton",
			"type" : "button",

			"x" : 15 + 42,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

			"default_image" : "yamato_taskbar/ability2_n.tga",
			"over_image" : "yamato_taskbar/ability2_h.tga",
			"down_image" : "yamato_taskbar/ability2_p.tga",
		},
		## Warp Button
		{
			"name" : "WarpButton",
			"type" : "button",

			"x" : 15 + 42 + 42 + 5,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

			"default_image" : "yamato_taskbar/map_n.tga",
			"over_image" : "yamato_taskbar/map_h.tga",
			"down_image" : "yamato_taskbar/map_p.tga",
			"disable_image" : "yamato_taskbar/map_d.tga",
		},	
		## Storage Button
		{
			"name" : "ForgeGuideButton",
			"type" : "button",

			"x" : 15 + 42 + 42 + 42 + 10,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

			"default_image" : "yamato_taskbar/ability1_n.tga",
			"over_image" : "yamato_taskbar/ability1_h.tga",
			"down_image" : "yamato_taskbar/ability1_p.tga",
		},		
		## Storage Button
		{
			"name" : "HallOfFameButton",
			"type" : "button",

			"x" : 15 + 42 + 42 + 42 + 10 + 42,
			"y" : 3 + Y_ADD_POSITION,

			# "tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,

			"default_image" : "yamato_taskbar/ability1_n.tga",
			"over_image" : "yamato_taskbar/ability1_h.tga",
			"down_image" : "yamato_taskbar/ability1_p.tga",
		},	
		## QuickBar
		{
			"name" : "quickslot_board",
			"type" : "window",

			"x" : (SCREEN_WIDTH / 2) - 270 + 40+ 40 + 60 - 5 - 3,
			"y" : 0 + Y_ADD_POSITION + 4,

			"width" : 256 + 14 + 2 + 11 + 10,
			"height" : 37,

			"children" :
			(

				{
					"name" : "ExpandButton",
					"type" : "button",

					"x" : 128 + 3,
					"y" : 1,
					"tooltip_text" : uiScriptLocale.TASKBAR_EXPAND,
					
					
					"default_image" : ROOT + "TaskBar/Chat_Button_01.sub",
					"over_image" : ROOT + "TaskBar/Chat_Button_02.sub",
					"down_image" : ROOT + "TaskBar/Chat_Button_03.sub",
				},
				{
					"name" : "quick_slot_1",
					"type" : "grid_table",

					"start_index" : 0,

					"x" : 0,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/slot_base.sub",
					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,

					"children" :
					(
						{ "name" : "slot_1", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/1.sub", },
						{ "name" : "slot_2", "type" : "image", "x" : 35, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/2.sub", },
						{ "name" : "slot_3", "type" : "image", "x" : 67, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/3.sub", },
						{ "name" : "slot_4", "type" : "image", "x" : 99, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/4.sub", },
					),
				},
				{
					"name" : "quick_slot_2",
					"type" : "grid_table",

					"start_index" : 4,

					"x" : 128 + 15 + 6,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/slot_base.sub",
					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,

					"children" :
					(
						{ "name" : "slot_5", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f1.sub", },
						{ "name" : "slot_6", "type" : "image", "x" : 35, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f2.sub", },
						{ "name" : "slot_7", "type" : "image", "x" : 67, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f3.sub", },
						{ "name" : "slot_8", "type" : "image", "x" : 99, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f4.sub", },
					),
				},
				{
					"name" : "QuickSlotBoard",
					"type" : "window",

					"x" : 128+14+128+2+9,
					"y" : 0,
					"width" : 11,
					"height" : 37,
					"children" :
					(
						{
							"name" : "QuickSlotNumberBox",
							"type" : "image",
							"x" : 1,
							"y" : 15,
							"image" : ROOT + "taskbar/QuickSlot_Button_Board.sub",
						},
						{
							"name" : "QuickPageUpButton",
							"type" : "button",
							"tooltip_text" : uiScriptLocale.TASKBAR_PREV_QUICKSLOT,
							"x" : 1,
							"y" : 9,
							"default_image" : ROOT + "TaskBar/QuickSlot_UpButton_01.sub",
							"over_image" : ROOT + "TaskBar/QuickSlot_UpButton_02.sub",
							"down_image" : ROOT + "TaskBar/QuickSlot_UpButton_03.sub",
						},
						{
							"name" : "QuickPageNumber", 
							"type" : "image",
							"x" : 3, "y" : 15, "image" : "d:/ymir work/ui/game/taskbar/1.sub", 
						},
						{
							"name" : "QuickPageDownButton",
							"type" : "button",
							"tooltip_text" : uiScriptLocale.TASKBAR_NEXT_QUICKSLOT,

							"x" : 1,
							"y" : 24,

							"default_image" : ROOT + "TaskBar/QuickSlot_DownButton_01.sub",
							"over_image" : ROOT + "TaskBar/QuickSlot_DownButton_02.sub",
							"down_image" : ROOT + "TaskBar/QuickSlot_DownButton_03.sub",
						},
					),
				},
			),
		},
	),
}
