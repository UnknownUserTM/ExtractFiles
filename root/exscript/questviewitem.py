import uiScriptLocale

# ############################################################# #
# ## QuestViewWindow @ Metin2Reignited / Code by Exterminatus ## #
# ############################################################### #

IMAGE_PATH = "yamato_questboard/"

window = {
	"name" : "QuestViewItem",
	"style" : ("float",),

	"x" : 150,
	"y" : 400,

	"width" : 222,
	"height" : 75,

	"children" :
	(

		{
			"name":"QuestViewDot",
			"type":"image",

			"x" : 0,
			"y" : 4,

			"image" : "questview/quest_new.tga",
		},
		{
			"name" : "QuestViewTitle",
			"type" : "text",
					
			"x" : 15,
			"y" : 1,
					
			"text" : "Titel der Quest",
				
			"outline" : 1,
		},
		{
			"name" : "QuestViewDesc",
			"type" : "text",
					
			"x" : 20,
			"y" : 1 + 15,
					
			"text" : "- Beschreibung der Quest",
				
			"outline" : 1,
		},
		{
			"name" : "QuestViewTimer",
			"type" : "text",
					
			"x" : 20,
			"y" : 1 + 15 + 15,
					
			"text" : "- Keine Zeitbeschränkung",
				
			"outline" : 1,
		},
		{
			"name" : "QuestViewCounter",
			"type" : "text",
					
			"x" : 20,
			"y" : 1 + 15 + 15 + 15,
					
			"text" : "- Verbleibend: 0",
				
			"outline" : 1,
		},
		{
			"name":"QuestViewBottomLine",
			"type":"image",

			"x" : 0,
			"y" : 1 + 15 + 15 + 15 + 15 + 5,

			"image" : "questview/quest_list_line_01.tga",
		},
	),
}
