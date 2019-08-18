import uiScriptLocale

window = {
	"name" : "ShopDialog",

	"x" : SCREEN_WIDTH - 400,
	"y" : 10,

	"style" : ("movable", "float",),

	"width" : 210,
	"height" : 328+50,

	"children" :
	(
		{
			"name" : "TitleBar",
			"type" : "roofbar",
			"style" : ("attach",),

			"x" : -8,
			"y" : 7,

			"width" : 184+30+15-5,
			"color" : "red",

		},
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 50,

			"width" : 210,
			"height" : 328,

			"children" :
			(

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 12+13,
					"y" : 34-10-8,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 8,
					"x_step" : 32,
					"y_step" : 32,

					"image" : "d:/ymir work/ui/public/Slot_Base.sub",
				},

				## Buy
				{
					"name" : "BuyButton",
					"type" : "toggle_button",

					"x" : 21+13,
					"y" : 295-10,

					"width" : 61,
					"height" : 21,

					"text" : uiScriptLocale.SHOP_BUY,

					"default_image" : "yamato_button/button_small_n.tga", 
					"over_image" : "yamato_button/button_small_h.tga", 
					"down_image" : "yamato_button/button_small_p.tga", 
				},

				## Sell
				{
					"name" : "SellButton",
					"type" : "toggle_button",

					"x" : 104+13,
					"y" : 295-10,

					"width" : 61,
					"height" : 21,

					"text" : uiScriptLocale.SHOP_SELL,

					"default_image" : "yamato_button/button_small_n.tga", 
					"over_image" : "yamato_button/button_small_h.tga", 
					"down_image" : "yamato_button/button_small_p.tga", 
				},

				## Close
				{
					"name" : "CloseButton",
					"type" : "button",

					"x" : 13,
					"y" : 295-10,

					"horizontal_align" : "center",

					"text" : uiScriptLocale.PRIVATE_SHOP_CLOSE_BUTTON,

					"default_image" : "yamato_button/button_small_n.tga", 
					"over_image" : "yamato_button/button_small_h.tga", 
					"down_image" : "yamato_button/button_small_p.tga", 
				},

				## MiddleTab1
				{
					"name" : "MiddleTab1",
					"type" : "radio_button",

					"x" : 21,
					"y" : 295,

					"width" : 61,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## MiddleTab2
				{
					"name" : "MiddleTab2",
					"type" : "radio_button",

					"x" : 104,
					"y" : 295,

					"width" : 61,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},

				## SmallTab1
				{
					"name" : "SmallTab1",
					"type" : "radio_button",

					"x" : 21,
					"y" : 295,

					"width" : 43,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},

				## SmallTab2
				{
					"name" : "SmallTab2",
					"type" : "radio_button",

					"x" : 71,
					"y" : 295,

					"width" : 43,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},

				## SmallTab3
				{
					"name" : "SmallTab3",
					"type" : "radio_button",

					"x" : 120,
					"y" : 295,

					"width" : 43,
					"height" : 21,

					"default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				},
			),
		},
	),
}


# import uiScriptLocale

# window = {
	# "name" : "ShopDialog",

	# "x" : SCREEN_WIDTH - 400,
	# "y" : 10,

	# "style" : ("movable", "float",),

	# "width" : 184,
	# "height" : 328,

	# "children" :
	# (
		# {
			# "name" : "board",
			# "type" : "board",
			# "style" : ("attach",),

			# "x" : 0,
			# "y" : 0,

			# "width" : 184,
			# "height" : 328,

			# "children" :
			# (
				# ## Title
				# {
					# "name" : "TitleBar",
					# "type" : "titlebar",
					# "style" : ("attach",),

					# "x" : 8,
					# "y" : 8,

					# "width" : 169,
					# "color" : "gray",

					# "children" :
					# (
						# { "name":"TitleName", "type":"text", "x":84, "y":4, "text":uiScriptLocale.SHOP_TITLE, "text_horizontal_align":"center" },
					# ),
				# },

				# ## Item Slot
				# {
					# "name" : "ItemSlot",
					# "type" : "grid_table",

					# "x" : 12,
					# "y" : 34,

					# "start_index" : 0,
					# "x_count" : 5,
					# "y_count" : 8,
					# "x_step" : 32,
					# "y_step" : 32,

					# "image" : "d:/ymir work/ui/public/Slot_Base.sub",
				# },

				# ## Buy
				# {
					# "name" : "BuyButton",
					# "type" : "toggle_button",

					# "x" : 21,
					# "y" : 295,

					# "width" : 61,
					# "height" : 21,

					# "text" : uiScriptLocale.SHOP_BUY,

					# "default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				# },

				# ## Sell
				# {
					# "name" : "SellButton",
					# "type" : "toggle_button",

					# "x" : 104,
					# "y" : 295,

					# "width" : 61,
					# "height" : 21,

					# "text" : uiScriptLocale.SHOP_SELL,

					# "default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				# },

				# ## Close
				# {
					# "name" : "CloseButton",
					# "type" : "button",

					# "x" : 0,
					# "y" : 295,

					# "horizontal_align" : "center",

					# "text" : uiScriptLocale.PRIVATE_SHOP_CLOSE_BUTTON,

					# "default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				# },

				# ## MiddleTab1
				# {
					# "name" : "MiddleTab1",
					# "type" : "radio_button",

					# "x" : 21,
					# "y" : 295,

					# "width" : 61,
					# "height" : 21,

					# "default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				# },

				# ## MiddleTab2
				# {
					# "name" : "MiddleTab2",
					# "type" : "radio_button",

					# "x" : 104,
					# "y" : 295,

					# "width" : 61,
					# "height" : 21,

					# "default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				# },

				# ## SmallTab1
				# {
					# "name" : "SmallTab1",
					# "type" : "radio_button",

					# "x" : 21,
					# "y" : 295,

					# "width" : 43,
					# "height" : 21,

					# "default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				# },

				# ## SmallTab2
				# {
					# "name" : "SmallTab2",
					# "type" : "radio_button",

					# "x" : 71,
					# "y" : 295,

					# "width" : 43,
					# "height" : 21,

					# "default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				# },

				# ## SmallTab3
				# {
					# "name" : "SmallTab3",
					# "type" : "radio_button",

					# "x" : 120,
					# "y" : 295,

					# "width" : 43,
					# "height" : 21,

					# "default_image" : "d:/ymir work/ui/public/small_button_01.sub",
					# "over_image" : "d:/ymir work/ui/public/small_button_02.sub",
					# "down_image" : "d:/ymir work/ui/public/small_button_03.sub",
				# },
			# ),
		# },
	# ),
# }