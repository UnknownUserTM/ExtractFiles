import uiScriptLocale
IMAGE_PATH = "yamato_questboard/"

window = {
	"name" : "QuestPaper",
	"style" : ("float",),

	"x" : 0,
	"y" : 0,

	"width" : 325,
	"height" : 360,

	"children" :
	(				
		{
						
			"name":"QuestPaperBackGround",
			"type":"image",
			"style" : ("attach",),

			"x" : 25,
			"y" : 15,

			"image" : IMAGE_PATH + "description_paper.tga",
						
			"children" : (

				{
						
					"name" : "QuestTitleTextLine",
					"type" : "text",
							
					"x" : 0,
					"y" : 15,
							
					"text" : "Die Bedrohung I",
					"horizontal_align" : "center", 
					"text_horizontal_align":"center",
					"outline" : 1,	
				},
				{
						
					"name":"QuestTitleHeadingBorder",
					"type":"image",
					"style" : ("attach", "movable",),

					"x" : 15,
					"y" : 15+10,

					"image" : IMAGE_PATH + "heading_border.tga",
				},
				{
					"name" : "QuestContentListBox",
					"type" : "questlistbox",
					
					"x" : 15,
					"y" : 45,
					
					"width" : 270,
					"height" : 300,
				},
				{
					"name" : "scrollBar",
					"type" : "small_thin_scrollbar",
					
					"x" : 280,
					"y" : 45,
					
					"size" : 300,
				},
				# {
						
					# "name" : "QuestDescTitleTextLine",
					# "type" : "text",
							
					# "x" : 25,
					# "y" : 15 + 30,
							
					# "text" : "Beschreibung:",
					# "text_horizontal_align" : "left",
					# "outline" : 1,
				# },
				
				# {
						
					# "name" : "CurrencyRewardTextLine",
					# "type" : "text",
							
					# "x" : 25 + 50 + 218,
					# "y" : 15 + 30 + 200 + 15 + 72,
						
					# "fontsize" : "LARGE",
				
					# "text" : "|Eemoji/achievement_small|e 10 |Eemoji/achievement_small|e",
					# "text_horizontal_align" : "right",
					# "outline" : 1,
				# },	

			),
		},

	),
}

