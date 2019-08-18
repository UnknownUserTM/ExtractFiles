import uiScriptLocale

# ############################################################# #
# ## QuestViewWindow @ Metin2Reignited / Code by Exterminatus ## #
# ############################################################### #

IMAGE_PATH = "yamato_questboard/"

window = {
	"name" : "QuestViewWindow",
	"style" : ("float",),

	"x" : SCREEN_WIDTH - 210,
	"y" : 230,

	"width" : 222,
	"height" : 17,

	"children" :
	(

		{
			"name":"QuestViewBar",
			"type":"image",

			"x" : 0,
			"y" : 0,

			"image" : "questview/quest_tab_01.tga",
			
			"children" : 
			(
				{
					"name" : "QuestIcon",
					"type" : "button",
					
					"x" : 5,
					"y" : 2,
					
					# "image" : "questview/quest_up.tga",
					
					
					"default_image" : "questview/quest_up.tga",
					"over_image" : "questview/quest_over.tga",
					"down_image" : "questview/quest_down.tga",
					"disable_image" : "questview/quest_disable.tga",
					
				},
				{
					"name" : "QuestViewTitleBar",
					"type" : "text",
					
					"x" : 25,
					"y" : 1,
					
					"text" : "Aktive Quests",
				
					"outline" : 1,
				},
			),
		},
		{
			"name" : "NoQuestsTextLine",
			"type" : "text",
			
			"x" : -115,
			"y" : 1,
			
			"outline" : 1,
			
			"text" : "Du folgst keinen Quests.",
			"r" : 1,
			"g" : 0,
			"b" : 0,

			# "horizontal_align" : "right", 
		
		
		},
		{
			"name" : "QuestViewListBox",
			"type" : "questviewlistbox",
			
			"x" : 0,
			"y" : 20,
			
			"width" : 222,
			"height" : 600,
		},
	),
}
