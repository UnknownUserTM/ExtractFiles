import uiScriptLocale

# ########################################################## #
# ## QuestWindow @ Metin2Reignited / Code by Exterminatus ## #
# ########################################################## #

IMAGE_PATH = "yamato_questboard/"

window = {
	"name" : "QuestWindow",
	"style" : ("movable", "float",),

	"x" : 20,
	"y" : 170,

	"width" : 710,
	"height" : 560,

	"children" :
	(

		{
			"name":"QuestBase",
			"type":"image",
			"style" : ("attach", "movable",),

			"x" : 20,
			"y" : 55,

			"image" : IMAGE_PATH + "paper_background_texture.tga",
			
			
			"children" :
			(
				{
					"name":"ContentCarve",
					"type":"image",
					"style" : ("attach", "movable",),

					"x" : 22,
					"y" : 20,

					"image" : IMAGE_PATH + "content_carv.tga",
				},			
				{
					"name":"QuestListContentCarve",
					"type":"image",
					"style" : ("attach", "movable",),

					"x" : 28,
					"y" : 25,

					"image" : IMAGE_PATH + "inner_content_carv.tga",
					
					"children" : 
					(
						{
							"name":"QuestList_ContentCarve",
							"type":"image",

							"x" : 15 + 3,
							"y" : 5 + 39 + 39 + 39 + 39 + 50,

							"image" : IMAGE_PATH + "quest_links_holder.tga",
							
							"children" : 
							(
								{
									"name" : "Quest_ListBox",
									"type" : "listbox",

									"x" : 0,
									"y" : 0,
									
									"width" : 265,
									"height" : 159,	
								},
							),
						},
						{
							"name" : "Quest_ScrollBar",
							"type" : "scrollbar",

							"x" : 15 + 3 + 280 - 12,
							"y" : 5 + 39 + 39 + 39 + 39 + 50,
							
							"size" : 159,
						},
						{
							"name" : "MainQuestTab_Button",
							"type" : "button",
							
							"x" : 15,
							"y" : 5,
							
							"default_image" : IMAGE_PATH + "tab_n.tga",
							"over_image" : IMAGE_PATH + "tab_h.tga",
							"down_image" : IMAGE_PATH + "tab_p.tga",
							
							"children" : 
							(
								{
									"name":"MainQuestTab_StatusImage",
									"type":"image",
									"style" : ("attach", "movable",),

									"x" : 5,
									"y" : -1,

									"image" : IMAGE_PATH + "expand_single_n.tga",
								},								
								{
									"name":"MainQuestTab_Title",
									"type":"text",

									"x" : 136,
									"y" : 11,
									
									"outline" : 1,
									
									"text_horizontal_align" : "center",

									"text" : "Mainquests (0)",
								},									
							),
						},
						{
							"name" : "BiologistQuestTab_Button",
							"type" : "button",
							
							"x" : 15,
							"y" : 5 + 39,
							
							"default_image" : IMAGE_PATH + "tab_n.tga",
							"over_image" : IMAGE_PATH + "tab_h.tga",
							"down_image" : IMAGE_PATH + "tab_p.tga",
							
							"children" : 
							(
								{
									"name":"BiologistQuestTab_StatusImage",
									"type":"image",
									"style" : ("attach", "movable",),

									"x" : 5,
									"y" : -1,

									"image" : IMAGE_PATH + "expand_single_n.tga",
								},								
								{
									"name":"BiologistQuestTab_Title",
									"type":"text",

									"x" : 136,
									"y" : 11,
									
									"outline" : 1,
									
									"text_horizontal_align" : "center",

									"text" : "Research of the Biologist (0)",
								},									
							),
						},
						{
							"name" : "HuntQuestTab_Button",
							"type" : "button",
							
							"x" : 15,
							"y" : 5 + 39 + 39,
							
							"default_image" : IMAGE_PATH + "tab_n.tga",
							"over_image" : IMAGE_PATH + "tab_h.tga",
							"down_image" : IMAGE_PATH + "tab_p.tga",
							
							"children" : 
							(
								{
									"name":"HuntQuestTab_StatusImage",
									"type":"image",
									"style" : ("attach", "movable",),

									"x" : 5,
									"y" : -1,

									"image" : IMAGE_PATH + "expand_single_n.tga",
								},								
								{
									"name":"HuntQuestTab_Title",
									"type":"text",

									"x" : 136,
									"y" : 11,
									
									"outline" : 1,
									
									"text_horizontal_align" : "center",

									"text" : "Dungeonquests (0)",
								},									
							),
						},
						{
							"name" : "SideQuestTab_Button",
							"type" : "button",
							
							"x" : 15,
							"y" : 5 + 39 + 39 + 39,
							
							"default_image" : IMAGE_PATH + "tab_n.tga",
							"over_image" : IMAGE_PATH + "tab_h.tga",
							"down_image" : IMAGE_PATH + "tab_p.tga",
							
							"children" : 
							(
								{
									"name":"SideQuestTab_StatusImage",
									"type":"image",
									"style" : ("attach", "movable",),

									"x" : 5,
									"y" : -1,

									"image" : IMAGE_PATH + "expand_single_n.tga",
								},								
								{
									"name":"SideQuestTab_Title",
									"type":"text",

									"x" : 136,
									"y" : 11,
									
									"outline" : 1,
									
									"text_horizontal_align" : "center",

									"text" : "Sidequests (0)",
								},									
							),
						},
						{
							"name" : "QuestBookQuestTab_Button",
							"type" : "button",
							
							"x" : 15,
							"y" : 5 + 39 + 39 + 39 + 39,
							
							"default_image" : IMAGE_PATH + "tab_n.tga",
							"over_image" : IMAGE_PATH + "tab_h.tga",
							"down_image" : IMAGE_PATH + "tab_p.tga",
							
							"children" : 
							(
								{
									"name":"QuestBookQuestTab_StatusImage",
									"type":"image",
									"style" : ("attach", "movable",),

									"x" : 5,
									"y" : -1,

									"image" : IMAGE_PATH + "expand_single_n.tga",
								},								
								{
									"name":"QuestBookQuestTab_Title",
									"type":"text",

									"x" : 136,
									"y" : 11,
									
									"outline" : 1,
									
									"text_horizontal_align" : "center",

									"text" : "Questbooks (0)",
								},									
							),
						},	
						
					),
				},


				## DescriptionSide
				{
					"name":"QuestDescContentCarve",
					"type":"image",
					"style" : ("attach", "movable",),

					"x" : 28 + 5 + 305,
					"y" : 25,

					"image" : IMAGE_PATH + "inner_content_carv.tga",
					
					"children" : 
					(
						# {
						
							# "name":"QuestPaperBackGround",
							# "type":"image",
							# "style" : ("attach", "movable",),

							# "x" : 3,
							# "y" : 3,

							# "image" : IMAGE_PATH + "description_paper.tga",
						
						
						# },
						
						# {
						
							# "name" : "QuestTitleTextLine",
							# "type" : "text",
							
							# "x" : 157,
							# "y" : 15,
							
							# "text" : "Die Bedrohung I",
							# "text_horizontal_align" : "center",
							# "outline" : 1,
						
						
						# },
						# {
						
							# "name" : "QuestDescTitleTextLine",
							# "type" : "text",
							
							# "x" : 25,
							# "y" : 15 + 30,
							
							# "text" : "Beschreibung:",
							# "text_horizontal_align" : "left",
							# "outline" : 1,
						# },
						
						
						# ## QuestDescription BEGIN
						# {
						
							# "name" : "QuestDescTextLine_01",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						# {
						
							# "name" : "QuestDescTextLine_02",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						# {
						
							# "name" : "QuestDescTextLine_03",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						# {
						
							# "name" : "QuestDescTextLine_04",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						# {
						
							# "name" : "QuestDescTextLine_05",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						# {
						
							# "name" : "QuestDescTextLine_06",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						
						# {
						
							# "name" : "QuestDescTextLine_07",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15 + 15 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						# {
						
							# "name" : "QuestDescTextLine_08",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15 + 15 + 15 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },
						# {
						
							# "name" : "QuestDescTextLine_09",
							# "type" : "text",
							
							# "x" : 35,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15 + 15 + 15 + 15 + 15,
							
							
							# "text" : "Die Orks werden immer gefährlicher, wir müssen",
							# "text_horizontal_align" : "left",
							# # "outline" : 1,
						# },

						# ## QuestDescription END
						# {
						
							# "name" : "QuestTargetTextLine01",
							# "type" : "text",
							
							# "x" : 40,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15 + 15 + 15 + 15 +15 + 20,
						
							# "text" : "- Verbleibend: 200",
							# "text_horizontal_align" : "left",
							# "outline" : 1,
						# },
						# {
						
							# "name" : "QuestTargetTextLine02",
							# "type" : "text",
							
							# "x" : 40,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15 + 15 + 15 + 15 +15 + 20 + 15,
							
							# "text" : "- Verbleibend: 8 / 20",
							# "text_horizontal_align" : "left",
							# "outline" : 1,
						# },
						# {
						
							# "name" : "QuestTimerTextLine",
							# "type" : "text",
							
							# "x" : 245,
							# "y" : 15 + 30 + 18 + 15 + 15 + 15 + 15 + 15 + 15 + 15 + 20 + 15,
							
							# "text" : "- Verbl. Zeit: 00:00:00",
							# "text_horizontal_align" : "right",
							# "outline" : 1,
						# },
						
						# {
						
							# "name" : "QuestRewardTitleTextLine",
							# "type" : "text",
							
							# "x" : 25,
							# "y" : 15 + 30 + 200,
							
							# "text" : "Belohnung:",
							# "text_horizontal_align" : "left",
							# "outline" : 1,
						# },
						
						# {
						
							# "name":"QuestRewardHolder_slot0",
							# "type":"image",
							# "style" : ("attach", "movable",),

							# "x" : 25,
							# "y" : 15 + 30 + 200 + 20,

							# "image" : IMAGE_PATH + "item_holder.tga",
							
							# "children" : 
							# (
								# {
								
									# "name":"QuestRewardSlotIMG_slot0",
									# "type":"image",

									# "x" : 2,
									# "y" : 2,

									# "image" : IMAGE_PATH + "big_slot.tga",
								# },
								# {
								
									# "name":"QuestRewardItemIMG_slot0",
									# "type":"image",

									# "x" : 4,
									# "y" : 4,

									# "image" : "icon/item/27003.tga",
								# },								
								# {
								
									# "name" : "QuestRewardSlotItemName_slot0",
									# "type" : "text",
									
									# "x" : 3 + 36 + 4,
									# "y" : 3 + 3,
																		
									# "text" : "Violetter Trank",
									# "text_horizontal_align" : "left",
									# "outline" : 1,
								# },								
								# {
								
									# "name" : "QuestRewardSlotItemCount_slot0",
									# "type" : "text",
									
									# "x" : 3 + 36 + 4,
									# "y" : 3 + 3 + 15,
																		
									# "text" : "Anzahl: 1x",
									# "text_horizontal_align" : "left",
									# "outline" : 1,
								# },							
							# ),
						# },
						# {
						
							# "name":"QuestRewardHolder_slot1",
							# "type":"image",
							# "style" : ("attach", "movable",),

							# "x" : 25,
							# "y" : 15 + 30 + 200 + 20 + 4 + 40,

							# "image" : IMAGE_PATH + "item_holder.tga",
							
							# "children" : 
							# (
								# {
								
									# "name":"QuestRewardSlotIMG_slot1",
									# "type":"image",

									# "x" : 2,
									# "y" : 2,

									# "image" : IMAGE_PATH + "big_slot.tga",
								# },
								# {
								
									# "name":"QuestRewardItemIMG_slot1",
									# "type":"image",

									# "x" : 4,
									# "y" : 4,

									# "image" : "icon/item/27003.tga",
								# },								
								# {
								
									# "name" : "QuestRewardSlotItemName_slot1",
									# "type" : "text",
									
									# "x" : 3 + 36 + 4,
									# "y" : 3 + 3,
																		
									# "text" : "Violetter Trank",
									# "text_horizontal_align" : "left",
									# "outline" : 1,
								# },								
								# {
								
									# "name" : "QuestRewardSlotItemCount_slot1",
									# "type" : "text",
									
									# "x" : 3 + 36 + 4,
									# "y" : 3 + 3 + 15,
																		
									# "text" : "Anzahl: 1x",
									# "text_horizontal_align" : "left",
									# "outline" : 1,
								# },							
							# ),
							
							
						# },	

						# {
						
							# "name" : "QuestGoldRewardTitleTextLine",
							# "type" : "text",
							
							# "x" : 25 + 50 + 218,
							# "y" : 15 + 30 + 200 + 72,
							
							# "fontsize" : "LARGE",
							
							# "text" : "1.000.000 Yang",
							# "text_horizontal_align" : "right",
							# "outline" : 1,
						# },						
						# {
						
							# "name" : "QuestEXPRewardTitleTextLine",
							# "type" : "text",
							
							# "x" : 25 + 50 + 218,
							# "y" : 15 + 30 + 200 + 15 + 72,
							
							# "text" : "100.000.000 XP",
							# "text_horizontal_align" : "right",
							# "outline" : 1,
						# },							
						
						# {
						
							# "name":"QuestTitleHeadingBorder",
							# "type":"image",
							# "style" : ("attach", "movable",),

							# "x" : 25,
							# "y" : 3+20,

							# "image" : IMAGE_PATH + "heading_border.tga",
						# },
					
					
						{
						
							"name":"QuestBottomBar",
							"type":"image",
							"style" : ("attach", "movable",),

							"x" : 3,
							"y" : 3 + 360 + 2,

							"image" : IMAGE_PATH + "bottom_texture_tab.tga",
							
							
							"children" : 
							(
								{
									"name" : "FollowButton",
									"type" : "button",
									
									"x" : 50,
									"y" : 5,
									
									"text" : "Follow",
									# "tooltip_text" : "Quest wird im Questview an der rechten Seite angezeigt.",
									
									"default_image" : IMAGE_PATH + "normal_button_n.tga",
									"over_image" : IMAGE_PATH + "normal_button_h.tga",
									"down_image" : IMAGE_PATH + "normal_button_p.tga",
									"disable_image" : IMAGE_PATH + "normal_button_d.tga",
								},
								{
									"name" : "AbortButton",
									"type" : "button",
									
									"x" : 50 + 95 + 10,
									"y" : 5,
									
									"text" : "Abort",
									# "tooltip_text" : "Klicke hier um die Quest abzubrechen.",
									
									"default_image" : IMAGE_PATH + "normal_button_n.tga",
									"over_image" : IMAGE_PATH + "normal_button_h.tga",
									"down_image" : IMAGE_PATH + "normal_button_p.tga",
									"disable_image" : IMAGE_PATH + "normal_button_d.tga",
								},
							),
						
						},					
					
					),
				},
			),
		},
		{
			"name":"QuestScrollLeft",
			"type":"image",
			"style" : ("attach", "movable",),

			"x" : 0,
			"y" : 0,

			"image" : IMAGE_PATH + "right_scroll_texture.tga",
		},
		{
			"name":"QuestScrollRight",
			"type":"image",
			"style" : ("attach", "movable",),

			"x" : 700 - 30,
			"y" : 0,

			"image" : IMAGE_PATH + "right_scroll_texture2.tga",
			
			"children" : 
			(
				{
					"name" : "Close_Button",
					"type" : "button",
							
					"x" : 10,
					"y" : 56,
							
					"default_image" : IMAGE_PATH + "close_n.tga",
					"over_image" : IMAGE_PATH + "close_h.tga",
					"down_image" : IMAGE_PATH + "close_p.tga",				

				},
			
			),
		},
	),
}
