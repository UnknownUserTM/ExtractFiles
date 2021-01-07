import app
import constInfo
import chat
import app
import localeInfo

MSG_LIST = [
	localeInfo.MSG_BOT_INFO_0,
	localeInfo.MSG_BOT_INFO_1,
	localeInfo.MSG_BOT_INFO_2,
	localeInfo.MSG_BOT_INFO_3,
	localeInfo.MSG_BOT_INFO_4,
]

NEXT_MSG = 0
TIME_TO_NEXT_MESSAGE = 10

CONFIG = {}


def PostMessage():
	random = app.GetRandom(0, len(MSG_LIST))
	chat.AppendChat(chat.CHAT_TYPE_NOTICE, MSG_LIST[random])
	NEXT_MSG = app.GetTime() + TIME_TO_NEXT_MESSAGE

def Update():
	chat.AppendChat(chat.CHAT_TYPE_DEBUG, "Geht das so?")
	if NEXT_MSG < app.GetTime():
		PostMessage()
	
# PostMessage()
	
	





