import os
import app
import localeInfo
import debugInfo

CHINA_PORT = 50000
STATE_NONE = "NORM"
STATE_ON = "NORM"
STATE_NONE2 = "hMENTENANTA"
SERVER_NAME = "|cffff0000Origins"                                       
SERVER_IP = "144.91.65.109"
CH1_PORT = 10101
CH2_PORT = 10201
CH3_PORT = 10301
CH4_PORT = 10401
AUTH_PORT = 99803

def BuildServerList(orderList):
	retMarkAddrDict = {}
	retAuthAddrDict = {}
	retRegion0 = {}

	ridx = 1
	for region, auth, mark, channels in orderList:
		cidx = 1
		channelDict = {}
		for channel in channels:
			key = ridx * 10 + cidx
			channel["key"] = key
			channelDict[cidx] = channel
			cidx += 1

		region["channel"] = channelDict

		retRegion0[ridx] = region
		retAuthAddrDict[ridx] = auth
		retMarkAddrDict[ridx*10] = mark
		ridx += 1

	return retRegion0, retAuthAddrDict, retMarkAddrDict

app.ServerName = None

if (localeInfo.IsEUROPE() and app.GetLocalePath() == "locale/tr"):
					
	STATE_DICT = {
		#4 : "|cFFFF0000|hINCHIS",
		0 : "|cFFFF0000|hINCHIS",
		1 : "|cff00ff00|hNORMAL",
		2 : "|cff00ff00|hFULL",
		3 : "|cff00ff00|hBusi"
	}

	SERVER01_CHANNEL_DICT = {
		1:{"key":11,"name":"CH1","ip": SERVER_IP,"tcp_port": CH1_PORT,"udp_port": CH1_PORT,"state":STATE_ON,},
	
		2:{"key":12,"name":"CH2","ip": SERVER_IP,"tcp_port": CH2_PORT,"udp_port": CH2_PORT,"state":STATE_ON,},
	
		3:{"key":13,"name":"CH3","ip": SERVER_IP,"tcp_port": CH3_PORT,"udp_port": CH3_PORT,"state":STATE_ON,},
	
		4:{"key":14,"name":"CH4","ip": SERVER_IP,"tcp_port": CH4_PORT,"udp_port": CH4_PORT,"state":STATE_ON,},		
	}
	
	REGION_NAME_DICT = {
		0 : "Turkey",		
	}

	REGION_AUTH_SERVER_DICT = {
		0 : {
			1 : { "ip": SERVER_IP,"port":AUTH_PORT, },
	
		}		
	}

	REGION_DICT = {
		0 : {
			1 : { "name" : SERVER_NAME,"channel" : SERVER01_CHANNEL_DICT, },						
		},
	}

	MARKADDR_DICT = {
		10 : { "ip" : SERVER_IP,"tcp_port" : CH1_PORT, "mark" : "10.tga", "symbol_path" : "10", },
	}

	TESTADDR = { "ip" : SERVER_IP,"tcp_port" : CHINA_PORT, "udp_port" : CHINA_PORT, }
