import uiScriptLocale

ROOT = "d:/ymir work/ui/minimap/"

window = {
	"name" : "AtlasWindow",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 136 - 256 - 10,
	"y" : 0,

	"width" : 256 + 15,
	"height" : 256 + 38+50,

	"children" :
	(
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : 256+30+15,
			"color" : "red",

		},
		## BOARD
		{
			"name" : "board",
			"type" : "board",
			
			"style" : ("attach",),

			"x" : 0,
			"y" : 50,

			"width" : 256 + 15,
			"height" : 256 + 38,
			
			# "children" : (
				# {
					# "name" : "positionToolTip",
					# "type" : "text",
					
					# "x" : 0,
					# "y" : 0,
					
					# "text" : "Hallo?",
					# "outline" : 1,
				
				
				
				# },
			
			# ),

		},
	),
}

# import uiScriptLocale

# ROOT = "d:/ymir work/ui/minimap/"

# window = {
	# "name" : "AtlasWindow",
	# "style" : ("movable", "float",),

	# "x" : SCREEN_WIDTH - 136 - 256 - 10,
	# "y" : 0,

	# "width" : 256 + 15,
	# "height" : 256 + 38,

	# "children" :
	# (
		# ## BOARD
		# {
			# "name" : "board",
			# "type" : "board_with_titlebar",

			# "x" : 0,
			# "y" : 0,

			# "width" : 256 + 15,
			# "height" : 256 + 38,

			# "title" : uiScriptLocale.ZONE_MAP,
		# },
	# ),
# }
