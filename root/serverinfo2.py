import os
import app
import localeInfo
import debugINFO

STATE_NONE = "...."

STATE_DICT = {
				0 : "....",
				1 : "NORM",
				2 : "BUSY",
				3 : "FULL"
}
	
INFO = {
		'MARKADDR': {
					 10: {'tcp_port': 13000, 'ip': '149.202.241.224', 'symbol_path': '10', 'mark': 'mark_0.tga'},
		},
		
		'GAMEADDR': {
					 0: {
						 1: {'name': 'Origins','channel':{
														 1: {'state': STATE_NONE, 'name': 'CH1', 'key': 11, 'ip': '149.202.241.224', 'tcp_port': 10101, 'udp_port': 13000},
														 2: {'state': STATE_NONE, 'name': 'CH2', 'key': 12, 'ip': '149.202.241.224', 'tcp_port': 10201, 'udp_port': 10201},
														 3: {'state': STATE_NONE, 'name': 'CH3', 'key': 13, 'ip': '149.202.241.224', 'tcp_port': 10301, 'udp_port': 10301},
														 4: {'state': STATE_NONE, 'name': 'CH4', 'key': 14, 'ip': '149.202.241.224', 'tcp_port': 10401, 'udp_port': 10401},
														}
							},
						},
		},
		
		'NAME': {0:'ENGLISH'},
		
		'AUTHADDR':{
					0: {
						 1: {'ip': '149.202.241.224', 'port': 99500}, 
						}
		}
}

REGION_DICT = INFO["GAMEADDR"]
REGION_NAME_DICT = INFO["NAME"]
MARKADDR_DICT = INFO["MARKADDR"]
REGION_AUTH_SERVER_DICT = INFO["AUTHADDR"]

