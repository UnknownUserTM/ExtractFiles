import uiScriptLocale

WINDOW_WIDTH = 320
WINDOW_HEIGTH = 400
IMAGE_PATH = "yamato_questboard/"

window = {
	"name" : "QuestIntroBoard",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - WINDOW_WIDTH - 250,
	"y" : (SCREEN_HEIGHT - WINDOW_HEIGTH) / 2 - 180,

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
			"style" : ("attach",),

			"x" : 0,
			"y" : 50,

			"width" : WINDOW_WIDTH+30,
			"height" : WINDOW_HEIGTH+30,
			
			"children" : (
			
				# {
						
					# "name":"QuestPaperBackGround",
					# "type":"image",
					# "style" : ("attach", "movable",),

					# "x" : 25,
					# "y" : 15,

					# "image" : IMAGE_PATH + "description_paper.tga",
						
						
				# },
				# {
						
					# "name" : "QuestTitleTextLine",
					# "type" : "text",
							
					# "x" : 0,
					# "y" : 25,
							
					# "text" : "Die Bedrohung I",
					# "horizontal_align" : "center", 
					# "text_horizontal_align":"center",
					# "outline" : 1,
						
						
				# },
				# {
						
					# "name":"QuestTitleHeadingBorder",
					# "type":"image",
					# "style" : ("attach", "movable",),

					# "x" : 25 + 25 - 10,
					# "y" : 15+20,

					# "image" : IMAGE_PATH + "heading_border.tga",
				# },
			
				{
						
					"name":"QuestBottomBar_0",
					"type":"image",
					"style" : ("attach",),

					"x" : 25,
					"y" : 15 + 360 + 2,

					"image" : IMAGE_PATH + "bottom_texture_tab.tga",
							
							
					"children" : 
					(
						{
							"name" : "AcceptButton",
							"type" : "button",
									
							"x" : 50,
							"y" : 5,
									
							"text" : "Accept",
							# "tooltip_text" : "Klicke hier um die Quest anzunehmen.",
									
							"default_image" : IMAGE_PATH + "normal_button_n.tga",
							"over_image" : IMAGE_PATH + "normal_button_h.tga",
							"down_image" : IMAGE_PATH + "normal_button_p.tga",
							"disable_image" : IMAGE_PATH + "normal_button_d.tga",
						},
						{
							"name" : "DeclineButton",
							"type" : "button",
									
							"x" : 50 + 95 + 10,
							"y" : 5,
									
							"text" : "Decline",
							# "tooltip_text" : "Klicke hier um die Quest abzulehnen.",
									
							"default_image" : IMAGE_PATH + "normal_button_n.tga",
							"over_image" : IMAGE_PATH + "normal_button_h.tga",
							"down_image" : IMAGE_PATH + "normal_button_p.tga",
							"disable_image" : IMAGE_PATH + "normal_button_d.tga",
						},
					),
						
				},			
				{
						
					"name":"QuestBottomBar_1",
					"type":"image",
					"style" : ("attach",),

					"x" : 25,
					"y" : 15 + 360 + 2,

					"image" : IMAGE_PATH + "bottom_texture_tab.tga",
							
							
					"children" : 
					(
						{
							"name" : "ContinueButton",
							"type" : "button",
									
							"x" : 70,
							"y" : 5,
									
							"text" : "Continue",
							# "tooltip_text" : "Klicke hier um die Quest anzunehmen.",
									
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
					),
						
				},			
				{
						
					"name":"QuestBottomBar_2",
					"type":"image",
					"style" : ("attach",),

					"x" : 25,
					"y" : 15 + 360 + 2,

					"image" : IMAGE_PATH + "bottom_texture_tab.tga",
							
							
					"children" : 
					(
						{
							"name" : "CompleteButton",
							"type" : "button",
									
							"x" : 70,
							"y" : 5,
									
							"text" : "Complete quest",
							# "tooltip_text" : "Klicke hier um die Quest anzunehmen.",
									
							"default_image" : "yamato_helpboard/wide_button_n.tga",
							"over_image" : "yamato_helpboard/wide_button_h.tga",
							"down_image" : "yamato_helpboard/wide_button_p.tga",
							"disable_image" : "yamato_helpboard/wide_button_d.tga",
						},
					),
				},			
			),
		},
		# {
						
			# "name":"QuestNPCIcon",
			# "type":"image",
			# "style" : ("attach", "movable",),

			# "x" : -8 + ((WINDOW_WIDTH+30+15) - 48) / 2,
			# "y" : 15,

			# "image" : IMAGE_PATH + "npc/trainer.tga",
						
						
		# },
		# {
						
			# "name":"QuestTitle",
			# "type":"text",

			# "x" : -8 + ((WINDOW_WIDTH+30+15) - 48) / 2 + 24,
			# "y" : -5,

			# "text" : "Hauptmann",
			# "outline" : 1,
			
			# "text_horizontal_align" : "center",
						
		# },
	),
}

