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
			
			"children" : (
				{
					"name" : "enableWarpWindowButton",
					"type" : "button",
					
					"x" : 35,
					"y" : 20,
					
					"default_image" : "yamato_button/button_small_n.tga",
					"over_image" : "yamato_button/button_small_h.tga",
					"down_image" : "yamato_button/button_small_p.tga",		
					"text" : "GM: Warp",
				
				},
			
			),

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
					# "name" : "warpWindow",
					# "type" : "window",
					# "style" : ("attach",),
					
					# "x" : 0,
					# "y" : 50,

					# "width" : 256 + 15,
					# "height" : 256 + 38,
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
