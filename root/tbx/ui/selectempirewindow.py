window = {
	"name" : "SelectEmpireWindow",
	"x" : 0, "y" : 0,
	"width" : SCREEN_WIDTH,	"height" : SCREEN_HEIGHT,
	"children" : (
		{
			"name" : "BackGround",
			"type" : "expanded_image",
			"x" : 0, "y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1280.0,
			"y_scale" : float(SCREEN_HEIGHT) / 720.0,
			"image" : "tbx/selectempirewindow/background.tga",
			"children" : (
				{
					"name" : "window_name",
					"type" : "image",
					"x" : 0, "y" : 35,
					"horizontal_align" : "center",
					"vertical_align" : "top",
					"image" : "tbx/selectempirewindow/window.tga",
				},
				{
					"name" : "tbx",
					"type" : "image",
					"x" : 120, "y" : 20,
					"horizontal_align" : "right",
					"vertical_align" : "top",
					"image" : "tbx/selectempirewindow/tbx.tga",
				},
				{
					"name" : "board", 
					"type" : "image",
					"x" : -250, "y" : 0,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : "tbx/selectempirewindow/board.tga",
					"children" : (
						{
							"name" : "accept_button",
							"type" : "button",
							"x" : 0, "y" : 190,
							"horizontal_align" : "center",
							"vertical_align" : "center",
							"default_image" : "tbx/selectempirewindow/accept_0.tga",
							"over_image" :  "tbx/selectempirewindow/accept_1.tga",
							"down_image" : "tbx/selectempirewindow/accept_2.tga",
						},
						{
							"name" : "empire_desc",
							"type" : "image",
							"x" : 0, "y" : -50,
							"horizontal_align" : "center",
							"vertical_align" : "center",
							"image" : "tbx/selectempirewindow/shinsoo.tga",
						},
					),
				},
				{
					"name" : "empire_background",
					"type" : "image",
					"x" : 250, "y" : 0,
					"horizontal_align" : "center",
					"vertical_align" : "center",
					"image" : "tbx/selectempirewindow/empire_background.tga",
					"children" : (
						{
							"name" : "shinsoo",
							"type" : "expanded_image",
							"x" : 23, "y" : 137,
							"image" : "tbx/selectempirewindow/shinsoo_active.tga",
						},
						{
							"name" : "jinno",
							"type" : "expanded_image",
							"x" : 223, "y" : 14,
							"image" : "tbx/selectempirewindow/jinno_active.tga",
						},
						{
							"name" : "chunjo",
							"type" : "expanded_image",
							"x" : 7, "y" : 10,
							"image" : "tbx/selectempirewindow/chunjo_active.tga",
						},
					),
				},
			),
		},
	),
}