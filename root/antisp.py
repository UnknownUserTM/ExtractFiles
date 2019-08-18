import app,chat,GFHhg54GHGhh45GHGH,locale,settinginfo
# Anti-Spam Metin2Area
class AntiSpam:
	Time = {"LAST":0}
	def SendChatPacket(self, text, type):
		if GFHhg54GHGhh45GHGH.IsChatInsultIn(text):
			chat.AppendChat(chat.CHAT_TYPE_INFO, locale.CHAT_INSULT_STRING)
		else:
			# Antispam Skript
			if not settinginfo.isGM:
				if app.GetGlobalTimeStamp()>=self.Time["LAST"]:
					GFHhg54GHGhh45GHGH.SendChatPacket(text, type)
					self.Time["LAST"] = app.GetGlobalTimeStamp()+2
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "[Anti-Spam System]Du kannst nur eine Nachricht alle 2 Sekunde senden!")
			else:
				GFHhg54GHGhh45GHGH.SendChatPacket(text, type)
				