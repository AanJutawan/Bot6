# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
# from imgurpython import ImgurClient
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="EnW8hoj78DLdPyIYenT6.hAcbNzkk2Hr9niP9d4/8PG.aRlc4gksjTuDcmDVLn6HKVGPcJ4W7EJIjjOv6Y4Huo4=")

# client_id = ''
# client_secret = ''
# access_token = ''
# refresh_token = ''

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)

kk = LINETCR.LINE()
kk.login(token="Enks3L0Ooc7N4i4qQ84a.Qnd7vpLJIYVvfAjxfsZq6G.GM4eYbdVgnCh/hayj4U+KgKCvvB9QX/KkLCUT4b0Ffs=")

ki = LINETCR.LINE()
ki.login(token="EnhZPdkDOL3rk89VuwK1.VlqgFyxOJgVh25qsNraEmq./rI5nc7mgUY2ndDt8dsHE/XVmQrLjs47FguNcXbQrD4=")

kc = LINETCR.LINE()
kc.login(token="Eni4gE1GSUy1HCNv6Y72.o4P6eglIZxe9VQn9qUfQaG.4whod/UMndrtB/M5e1abW8el78GWEeyKoYZCgjnOA2I=")

kd = LINETCR.LINE()
kd.login(token="En73b6edG9iy4a12rCD6.zyOsyUbrFfzceeuzW9AFrG.IudLuAlLGvjHfLYfL8yE4NpyYdz6zsrkOq5vY0BYtAk=")

cl

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

# album = None
# image_path = 'tmp/tmp.jpg'

helpMessage =""" ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈

Selfbot by:
ᵗᵉᵅᵐ ᵇᵒᵗ

🐯 Creator = Melihat Pembuat Bot
🐯 Shani say = Mengikuti Apa Yang DiKatakan
🐯 Gcreator = Check Creator Grup

✴Command Creator✴

✴ Admin add @ = Menambahkan Admin
✴ Admin remove @ = Menghapus Admin
✴ Adminlist = Cek Admin

🐯Command Admin🐯

🐯 Id
🐯 Mid
🐯 Mid @
🐯 Me
🐯 K on/off
🐯 Gcancel:
🐯 Leave on/off
🐯 Add on/off
🐯 Share on/off
🐯 Jam on/off
🐯 Up 
🐯 Urloff
🐯 Urlon
🐯 Ginfo
🐯 Cancel
🐯 Gn
🐯 Out/Bye
🐯 Invite
🐯 Cn
🐯 Gift
🐯 My bot
🐯 Backup
🐯 Backup on
🐯 Daftar Bot
🐯 Respon/Responsename
🐯 Tagall/Mention/Ats
🐯 Glist
🐯 My bot
🐯 mayhem
🐯 Spam
🐯 Check > Absen
🐯 Steal + Mid
🐯 Steal @
🐯 Gift @

🔐Command Mimic🔐

🔐 Mimic on/off
🔐 Mimic @
🔐 Mimic:add: @
🔐 Mimic:del: @
🔐 ListTarget

💢CommandPenting💢

💢 Guest On/Off
💢 Mad On/Off
💢 Protect On/Off
💢 Ban @ 
💢 Unban @
💢 Kill Ban
💢 Kill @
💢 Nk
💢 Vk
💢 Cleanse/Fuck

==================================================

Creator : By ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈
http://line.me/ti/p/pjK1Od8ftK"""

KAC=[cl,ki,kk,kc,kd]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid]
admin=["ud354971b4d15bdc0f15fea0e786c7647","u60cf87121057af33190375541f364ff1","u5bcc09ab9cb2b88f26c7e30e5ab3dfcf","u9194e94cead077f0f3354f5b0e8088e7","u6cdb79fd6522bb375b5928d33db4cac9","u3d9f98868f046488d2bff33833d4abf7","u9f2d6c960b82b3d49b498be971279724"]
creator=["u36196ea7137f95585062f8303dbac814"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Owner : http://line.me/ti/p/pjK1Od8ftK",
    "lang":"JP",
    "comment":"Owner : http://line.me/ti/p/pjK1Od8ftK",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"🔥🔐⇲『🅳🅴🅳🅸』⇱🔐🔥",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact= ki.getProfile()
backup = ki.getProfile()
backup = kk.getProfile()
backup = kc.getProfile()
backup = kd.getProfile()
backup = ke.getProfile()
backup = kf.getProfile()
backup = kg.getProfile()
backup = kh.getProfile()
backup = kj.getProfile()
backup = kl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n�9�9" + Name
                wait2['ROM'][op.param1][op.param2] = "�9�9" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              if op.param2 in admin:
                pass
              else:
                try:
                  cl.sendText(op.param1,cl.getContact(op.param2).displayName + "Dilarang Buka Qr Selain Admin")
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  X = cl.getGroup(op.param1)
                  X.preventJoinByTicket = True
                  cl.updateGroup(X)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dilarang Buka Qr Selain Admin")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  Z = random.choice(KAC).getGroup(op.param1)
                  Z.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(Z)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 in Bots:
              pass
            if op.param2 in admin:
              pass
            else:
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
              random.choice(KAC).sendText(op.param1, "Dilarang Mengundang\nSelain Admin\nSori Aku Cancel Undangannya Karena Kak Bukan Admin")
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kimid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kkmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kk.acceptGroupInvitation(op.param1)
                else:
                  kk.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kcmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kc.acceptGroupInvitation(op.param1)
                else:
                  kc.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kdmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  kd.acceptGroupInvitation(op.param1)
                else:
                  kd.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                    
        #------Joined User Kick start------#
        #if op.type == 13:
           #if wait["Protectjoin"] == True:
               #if op.param2 not in admin and Bots : # Awalnya admin doang
                   #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            try:
              G = cl.getGroup(op.param1)
              cl.kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              cl.updateGroup(G)
              Ticket = cl.reissueGroupTicket(op.param1)
              cl.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ki.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kk.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kc.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kd.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ke.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kf.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kg.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kh.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kj.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kl.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              G.preventJoinByTicket = True
              cl.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              G = random.choice(KAC).getGroup(op.param1)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              cl.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ki.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kk.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kc.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kd.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ke.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kf.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kg.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kh.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kj.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kl.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              G.preventJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              wait["blacklist"][op.param2] = True
#--------------------------------
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

            elif msg.text in ["Auto like:on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Auto like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")

            elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")

                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")

            elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")

                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

            elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")

                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")

            elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�9�6�9��\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Shani gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Shani gn ","")
						ki.updateGroup(X)
					else:
						ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Angel gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Angel gn ","")
						kk.updateGroup(X)
					else:
						kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Yona gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Yona gn ","")
						ks.updateGroup(X)
					else:
						kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
            elif "Shani kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Shank kick ","")
					ki.kickoutFromGroup(msg.to,[midd])
            elif "Angel kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Angel kick ","")
					kk.kickoutFromGroup(msg.to,[midd])
            elif "Yona kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Yona kick ","")
					kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","Admin")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Bot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid':kimid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid':kkmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid':kcmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid':kdmid}
                kd.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid':kemid}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid':kfmid}
                kf.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid':kgmid}
                kg.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid':khmid}
                kh.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid':kjmid}
                kj.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid':klmid}
                kl.sendMessage(msg)

            elif "Shani invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Shani invite ","Admin")
					ki.findAndAddContactsByMid(midd)
					ki.inviteIntoGroup(msg.to,[midd])
            elif "Angel invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Angel invite ","Admin")
					kk.findAndAddContactsByMid(midd)
					kk.inviteIntoGroup(msg.to,[midd])
            elif "Yona invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Yona invite ","Admin")
					kc.findAndAddContactsByMid(midd)
					kc.inviteIntoGroup(msg.to,[midd])

            elif msg.text in ["Me"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)
            elif msg.text in ["Shani"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': kimid}
					ki.sendMessage(msg)
            elif msg.text in ["Angel"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': kkmid}
					kk.sendMessage(msg)

            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = kd.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = kf.getGroup(msg.to)
                gs = kg.getGroup(msg.to)
                gs = kh.getGroup(msg.to)
                gs = kj.getGroup(msg.to)
                gs = kl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': 'u36196ea7137f95585062f8303dbac814',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)

            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'u36196ea7137f95585062f8303dbac814',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Shani gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'u36196ea7137f95585062f8303dbac814',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Angel gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'u36196ea7137f95585062f8303dbac814',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kk.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Yona gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'u36196ea7137f95585062f8303dbac814',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'u36196ea7137f95585062f8303dbac814',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					ki.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"No one is inviting")
							else:
								cl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Shani cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = kk.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							kc.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								kk.sendText(msg.to,"No one is inviting")
							else:
								kc.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Shani ourl","Shani link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done")
						else:
							ki.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Angel ourl","Angel link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = False
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done")
						else:
							kk.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yona ourl","Yona link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Shani curl","Shani link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done")
						else:
							ki.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Angel curl","Angel link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done")
						else:
							kk.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yona curl","Yona link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							ks.sendText(msg.to,"Done")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,msg.to)
            elif "All Mid" == msg.text:
              if msg.from_ in admin: 
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                kk.sendText(msg.to,kkmid)
                kc.sendText(msg.to,kcmid)
                kd.sendText(msg.to,kdmid)
                ke.sendText(msg.to,kemid)
                kf.sendText(msg.to,kfmid)
                kg.sendText(msg.to,kgmid)
                kh.sendText(msg.to,khmid)
                kj.sendText(msg.to,kjmid)
            elif "My Mid" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
            elif "Shani Mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Angel Mid" == msg.text:
                kk.sendText(msg.to,kkmid)
            elif "Yona Mid" == msg.text:
                kc.sendText(msg.to,kcmid)
            elif "Melfa Mid" == msg.text:
                kd.sendText(msg.to,kdmid)
            elif "Devi Mid" == msg.text:
                ke.sendText(msg.to,kemid)
            elif "ᵐᵉˡᶠᵃ Mid" == msg.text:
                kf.sendText(msg.to,kfmid)
            elif "Cinhap Mid" == msg.text:
                kg.sendText(msg.to,kgmid)
            elif "Jinan Mid" == msg.text:
                kh.sendText(msg.to,khmid)
            elif "Yupi Mid" == msg.text:
                kj.sendText(msg.to,kjmid)
            elif msg.text in ["Wkwk"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["You"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Please"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
            elif msg.text in ["Wc"]:
				if msg.from_ in admin:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            
            elif "Steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"	

            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Shani rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Shani rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Angel rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Angel rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ1�7","K on","Contact on","é¡¯ç¤ºï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ�1�7�1�7","K off","Contact off","é¡¯ç¤ºï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1�7��1�7�å�1�7�åń1�7 :ã‚ªãƒ1�7","Join on","Auto join:on","è‡ªå�1�7��1�7�åƒåń1�7 ï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1�7��1�7�å�1�7�åń1�7 :ã‚ªãƒ�1�7�1�7","Join off","Auto join:off","è‡ªå�1�7��1�7�åƒåń1�7 ï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"å…³äº�1�7�é�1�7�€è¯·æ‹�1�7�ç»ã€‚è¦æ�1�7�¶å¼€è¯·æŒ‡å®šäººæ�1�7�°å�1�7�é€")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš�1�7�å°ç»�1�7�ç�1�7�¨è�1�7�ªåŠ¨é�1�7�€è¯·æ‹�1�7�ç»1�7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ1�7","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ�1�7�1�7","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ�1�7�1�7:ã‚ªãƒ1�7","Share on","Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["å…±æœ�1�7�1�7:ã‚ªãƒ�1�7�1�7","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif msg.text in ["Set"]:
				if msg.from_ in admin:
					md = ""
					if wait["contact"] == True: md+=" Contact : on\n"
					else: md+=" Contact : off\n"
					if wait["autoJoin"] == True: md+=" Auto join : on\n"
					else: md +=" Auto join : off\n"
					if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+= " Group cancel : off\n"
					if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
					else: md+=" Auto leave : off\n"
					if wait["timeline"] == True: md+=" Share : on\n"
					else:md+=" Share : off\n"
					if wait["autoAdd"] == True: md+=" Auto add : on\n"
					else:md+=" Auto add : off\n"
					if wait["commentOn"] == True: md+=" Comment : on\n"
					else:md+=" Comment : off\n"
					if wait["Protectcancel"] == True: md+="  Mad : on\n"
					else:md+=" Mad : off\n"
					if wait["Protectguest"] == True: md+=" Guest : on\n"
					else:md+=" Guest : off\n"
					cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1�7�Œæ²¡åœ¨ã€ 1�7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1�7�ç�1�7�¸å�1�7�ń1�7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "album " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1�7�Œæ²¡åœ¨ã€ 1�7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1�7�ç�1�7�¸å�1�7�ń1�7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1�7�äº�1�7�çš�1�7�ç�1�7�¸å�1�7�Œã€ 1�7")
            elif msg.text in ["Group id","ç¾¤çµ„å�1�7�¨id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"æ‹�1�7�ç»äº�1�7�å�1�7�¨éƒ¨çš�1�7�é�1�7�€è¯·ã€�1�7�1�7")
            elif "album removeâ†�1�7�1�7" in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album removeâ†�1�7�1�7","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1�7�äº�1�7�çš�1�7�ç�1�7�¸å�1�7�Œã€ 1�7")
            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ1�7","Add on","Auto add:on","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ�1�7�1�7","Add off","Auto add:off","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif "Message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneã€�1�7�1�7")
            elif msg.text in ["Message","è‡ªå�1�7��1�7�è¿½åń1�7 å•å€™èªžç¢ºèª1�7"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsã€�1�7�\n\n" + wait["message"])
            elif "Comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ1�7","Comment on","Comment:on","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ�1�7�1�7","Comment on","Comment off","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª1�7"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Shani gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Angel gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yona gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						cl.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						cl.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "Check":
                    cl.sendText(msg.to, "Check sider"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Ciduk":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal �7�8\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n��set��you can send �7�8 read point will be created �7�8")
#-------------------------------------------------#
            elif msg.text in ["Tagall","Mention","Ats","Begal",]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error

            elif msg.text in ["Shani Tagall","Shani Mention","Shani Ats","Shani Begal",]:
              if msg.from_ in admin:
                group = kk.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    kk.sendMessage(msg)
                except Exception as error:
                    print error

            elif msg.text in ["Angel Tagall","Angel Mention","Angel Ats","Angel Begal",]:
              if msg.from_ in admin:
                group = kc.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    kc.sendMessage(msg)
                except Exception as error:
                    print error
#-------------Fungsi Tag All Finish---------------#

            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                cl.sendText(msg.to,"Kami Siap Like Status Owner\nKami Delay untuk beberapa Detik\nJangan perintah kami dulu sampai kami Selesai Ngelike")
                try:
                  autolike()
                except:
                  pass
#-------------------------------------------------#
            elif msg.text in ["Masuk"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "Sudah Masuk Semua"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["Shani Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Angel Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Yona Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Aya Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kd.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Devi Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Celine Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kf.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Cinhap Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kg.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Jinan Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kh.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Yupi Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kj.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(msg.to)

            elif msg.text in ["Maya Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(msg.to)

#--------------------------------------------------
            elif msg.text.lower() == 'Backup':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() == 'sayang':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["Pulang","Bye"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kf.leaveGroup(msg.to)
                        kg.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)
                        kl.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["shani Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Angel Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Yona Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Aya Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Devi Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kd.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Celine Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cinhap Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kf.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Jinan Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kg.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Boy Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kh.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Yupi Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kj.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kyla Keluar"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kl.leaveGroup(msg.to)
                    except:
                        pass
#--------------------------------------------------
#--------------------------------------------------

            elif "Ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Shani Ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Shani Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Ban","ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Ban")
                    print "[Command]Ban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Unban","unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Unban")
                    print "[Command]Unban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Banlist","banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user(s)")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Banlist executed"

            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Fuck You")
							kc.sendText(msg.to,"Fuck You")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print

            elif "Glist" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "#[List Grup]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "Mayhem" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n ' abort' to abort♪") 
                    ki.sendText(msg.to,"「 Mayhem 」\n 46 victims shall yell hul·la·ba·loo♪\n /ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kc.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[ki,kk,kc,kd,ke,kf,kg,kh,kj,kl]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   kd.sendText(msg.to,"Mayhem done")

            elif "Nk " in msg.text:
				if msg.from_ in admin:
					if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Succes ")
										kk.sendText(msg.to,"Fuck You"),
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki2.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										kk.sendText(msg.to,"Succes ")
									except:
										ki.sendText(msg.to,"error")
#-----------------------[Ban/Unban Section]------------------------
#-----------------------------------------------
#-----------------------------------------------

            elif msg.text in ["kam"]:
              if msg.from_ in admin:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Pemilik Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )   

            elif msg.text in ["Ping"]:
              if msg.from_ in admin:
                kk.sendText(msg.to,"Pong 👍")
                ki.sendText(msg.to,"Pong 👍")
                kc.sendText(msg.to,"Pong 👍")
                kd.sendText(msg.to,"Pong 👍")
                ke.sendText(msg.to,"Pong 👍")
                kf.sendText(msg.to,"Pong 👍")
                kg.sendText(msg.to,"Pong 👍")
                kh.sendText(msg.to,"Pong 👍")
                kj.sendText(msg.to,"Pong 👍")
                kl.sendText(msg.to,"Pong 👍")
                
            elif msg.text in ["Baris"]:
              if msg.from_ in admin:
                kk.sendText(msg.to,"1")
                ki.sendText(msg.to,"2")
                kc.sendText(msg.to,"3")
                kd.sendText(msg.to,"4")
                ke.sendText(msg.to,"5")
                kf.sendText(msg.to,"6")
                kg.sendText(msg.to,"7")
                kh.sendText(msg.to,"8")
                kj.sendText(msg.to,"9")
                kl.sendText(msg.to,"10")
#--------------------------------------------------	
            elif msg.text in ["Shani"]:
              if msg.from_ in admin: 
                kk.sendText(msg.to,"Apa Say?")
            elif msg.text in ["Angel"]:
              if msg.from_ in admin: 
                ki.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Yona"]:
              if msg.from_ in admin: 
                kc.sendText(msg.to,"Apa Say?")
            elif msg.text in ["Melfa"]:
              if msg.from_ in admin: 
                kd.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Devi"]:
              if msg.from_ in admin: 
                ke.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["ᵐᵉˡᶠᵃ"]:
              if msg.from_ in admin: 
                kf.sendText(msg.to,"Iya Kak?")
            elif msg.text in ["Cinhap"]:
              if msg.from_ in admin: 
                kg.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Jinan"]:
              if msg.from_ in admin: 
                kh.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Yupi"]:
              if msg.from_ in admin: 
                kj.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Kyla"]:
              if msg.from_ in admin: 
                kl.sendText(msg.to,"Apa Kak?")
#-----------------------------------------------	
            elif msg.text in ["Owner"]:
              if msg.from_ in admin: 
                cl.sendText(msg.to,"BOT By http://line.me/ti/p/pjK1Od8ftK") 
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u36196ea7137f95585062f8303dbac814'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Owner By  ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ ")                       
#-----------------------------------------------
            elif msg.text in ["Creator"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u36196ea7137f95585062f8303dbac814'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Powered By  ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ ")         
#-----------------------------------------------
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                  bctxt = msg.text.replace("Spam ", "")
                  t = cl.getAllContactIds()
                  t = 10
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
#-----------------------------------------------
            elif msg.text in ["Mimic:on","mimic:on"]:
                wait2["copy"] = True
                cl.sendText(msg.to,"copy on")
	    elif msg.text in ["Mimic:off","mimic off"]:
                wait2["copy"] = False
                cl.sendText(msg.to,"copy off")
#-----------------------------------------------
            #-----------------------------------------------      
            elif "Copy @" in msg.text:
               if msg.from_ in admin: 
                if msg.toType == 2:
                    print "[Copy]"
                    _name = msg.text.replace("Copy @","")
                    _nametarget = _name.rstrip('  ')                    
                    gs = cl.getGroup(msg.to)                    
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:                        
                        cl.sendText(msg.to,"Tidak Ada Target ")                        
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target).statusMessage                                
                                contact2 = cl.getContact(target).displayName
                                contact3 = cl.getContact(target).pictureStatus
                                copy = cl.getProfile()
                                copy.statusMessage = contact                                
                                copy.displayName = contact2
                                copy.pictureStatus = contact3
                                cl.updateProfile(copy)
                                cl.sendText(msg.to, "Copy Done")
                            except:                                
                                pass                                               

#-----------------------------------------------   
            elif "Kagebunshin " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                        cl.CloneContactProfile(mata)
                        cl.sendText(msg.to, "Kagebunshin No Jutsu")
                    except Exception as e:
                                print e                                                

            elif msg.text in ["abackup","Kai"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Bunshin Kai")
                except Exception as e:
                    cl.sendText(msg.to, str(e))

            elif "Byakugan " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                            contact = cl.getContact(mata)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                    except Exception as e:
                                print e   

            elif "Kamui " in msg.text:
                if msg.from_ in admin:
                    midd = eval(msg.contentMetadata["MENTION"])
                    mata = midd["MENTIONEES"][0]["M"]
                    try:
                            contact = cl.getContact(mata)
                            cu = cl.channel.getCover(mata)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                    except Exception as e:
                                print e  
#----------------------------------------------------------------------------

#-----------------------------------------------------------
#--------------------------------------------------
            elif "Stalk " in msg.text:
                 print "[Command]Stalk executing"
                 stalkID = msg.text.replace("Stalk ","")
                 subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
                 files = glob.glob("tmp/*.jpg")
                 for file in files:
                     os.rename(file,"tmp/tmp.jpg")
                 fileTmp = glob.glob("tmp/tmp.jpg")
                 if not fileTmp:
                     cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                     print "[Command]Stalk executed - no image found"
                 else:
                     image = upload_tempimage(client)
                     cl.sendText(msg.to, format(image['link']))
                     subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                     print "[Command]Stalk executed - succes"
            
#--------------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "Group Creator : " + gCreator1)
                    cl.sendMessage(msg)
#--------------------------------------------------

            elif msg.text in ["Clear ban"]:
                 if msg.from_ in admin:
                   wait["blacklist"] = {}
                   cl.sendText(msg.to,"Clear All Ban Done")

            elif msg.text in ["Backup on","backup on"]:
              if msg.from_ in admin:
                if wait["Protectbackup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Backup On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectbackup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Backup On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Backup off","backup off"]:
              if msg.from_ in admin:
                if wait["Protectbackup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Backup Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectbackup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Backup Off")
                    else:
                        cl.sendText(msg.to,"done") 
#-----------------------------------------------
	
            elif "Admin add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kk.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kk.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                kk.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    kk.sendText(msg.to,"Perintah Ditolak")
                    kk.sendText(msg.to,"Butuh Izin Admin")

            elif "Admin remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Perintah Ditolak")
                    cl.sendText(msg.to,"Butuh Izin Admin")

            elif msg.text in ["Daftar Admin"]:
                if admin == [11]:
                    cl.sendText(msg.to,"Daftar Admin Kosong")
                else:
                    cl.sendText(msg.to,"Tunggu")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Staff Dieksekusi"

            elif msg.text in ["Daftar Grup"]:
              if msg.from_ in admin:
            					gid = cl.getGroupIdsJoined()
            					h = ""
            					for i in gid:
            						h += "[➡] %s  \n" % (cl.getGroup(i).name + " | " + msg.to + " : " + str(len (cl.getGroup(i).members)))
            					cl.sendText(msg.to, "⚠「Daftar Grup」⚠\n"+ h +"Total Group : " +str(len(gid)))
                
            elif ("Cn " in msg.text):
              if msg.toType == 2:
                profile = cl.getProfile()
                X = msg.text.replace("Cn ","")
                profile.displayName = X
                cl.updateProfile(profile)
                cl.sendText(msg.to,"Nama " + X + " Berhasil Diubah")
              else:
                cl.sendText(msg.to,"Gagal Mengubah Nama")

            elif "Shani Add @" in msg.text:
                if msg.from_ in owner:
                    print "Menambah Anggota Bot"
                    _name = msg.text.replace("Shani Add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = [8]
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                Bots.append(target)
                                cl.sendText(msg.to,"Berhasil Menambahkan")
                            except:
                                pass
                    print "Bot Ditambahkan"
                else:
                    cl.sendText(msg.to,"Gagal")
                    cl.sendText(msg.to,"Butuh Izin Dari Pemilik")

            elif "Shani Remove @" in msg.text:
                if msg.from_ in admin:
                    print "Staff Bot Dieksekusi"
                    _name = msg.text.replace("Shani Remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                Bots.remove(target)
                                cl.sendText(msg.to,"Berhasil Menghapus Dari Daftar")
                            except:
                                pass
                    print "Bot Dihapus"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Owner permission required.")
            elif msg.text in ["Daftar Bot"]:
              if msg.from_ in admin:
                if Bots == [8]:
                    cl.sendText(msg.to,"Daftar Bot 10")
                else:
                    cl.sendText(msg.to,"Tunggu")
                    mc = ""
                    for mi_d in Bots:
                        mc += "➳" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"「 ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ 」\n" + mc +"Total : "+ str(len(Bots)))
                    print "[Command]Whitelist executed"     
#-----------------------------------------------
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Dont cancel anyone ! cause me angry!")
                     else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif "Steal " in msg.text:
                if msg.from_ in admin:
                    salsa = msg.text.replace("Steal ","")
                    Manis = cl.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = cl.channel.getCover(Manis)
                    except:
                        cover = ""
                    cl.sendText(msg.to,"Gambar Foto Profilenya")
                    cl.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        cl.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        cl.sendText(msg.to,"Gambar Covernya")
                        cl.sendImageWithURL(msg.to,cover)

#--------------------------------------------------
            elif msg.text in ["Responsename","Respon"]:
                ki.sendText(msg.to,"D̴E̴D̴I̴ᵀᴱᴬᴹbøț*քʀօȶɛƈȶ")
                kk.sendText(msg.to,"D̴E̴D̴I̴ᵀᴱᴬᴹbøț*քʀօȶɛƈȶ")
                kc.sendText(msg.to,"D̴E̴D̴I̴ᵀᴱᴬᴹbøț*քʀօȶɛƈȶ")
                kd.sendText(msg.to,"D̴E̴D̴I̴ᵀᴱᴬᴹbøț*քʀօȶɛƈȶ")
                ki.sendText(msg.to,"Semua hadir boss\nsiap menunggu perintah anda Pʀᴏᴛᴇᴄᴛɪᴏɴѕ Group")
#--------------------------------------------------
            elif "Steal home @" in msg.text:      
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
#------------------------------------------------------------------
            elif "Mid @" in msg.text:
            	if msg.from_ in admin:
                  _name = msg.text.replace("Mid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = cl.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          cl.sendText(msg.to, g.mid)
                      else:
                          pass
#-----------------------------------------------
            elif msg.text in ["Sp"]:
              if msg.from_ in admin: 
                start = time.time()
                cl.sendText(msg.to, "Tunggu")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s Detik" % (elapsed_time))          

            elif msg.text in ["Speed Bot","Bot Desah"]:
              if msg.from_ in admin: 
                start = time.time()
                ki.sendText(msg.to, "Pᵉˡᵃⁿ-Pᵉˡᵃⁿ Sᵃʸᵃⁿᵍ...😃")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%s Detik" % (elapsed_time))
                kk.sendText(msg.to, "%s Detik" % (elapsed_time))
                kc.sendText(msg.to, "%s Detik" % (elapsed_time))
                kd.sendText(msg.to, "%s Detik" % (elapsed_time))
                kl.sendText(msg.to, "Tᵘʰ ᵏᵃᵃⁿ Cʳᵒᵗ ˢʸᵍ.. 😃")                    
#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Add Staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove Staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    gs = kl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"

#-----------------------------------------------------------

            elif ("Bunuh " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Vk " in msg.text:                  
                       nk0 = msg.text.replace("Shan ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ki.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Good Bye")

#----------------------------------------------------------------
#-----------------------[Auto cancel Section]------------------------

            elif msg.text in ["Auto Cancel Off","Auto cancel off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == True:
                        cancelinvite["autoCancel"] = False
                        cl.sendText(msg.to, "Auto Cancel turned off")
                        print "[Command]Cancel off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Cancel off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Auto Cancel On","Auto cancel on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == False:
                        cancelinvite["autoCancel"] = True
                        cl.sendText(msg.to, "Auto Cancel turned on")
                        print "[Command]Cancel on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Cancel on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Auto Url Off","Auto url off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Auto Url On","Auto url on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == False:
                        cancelinvite["autoCancelUrl"] = True
                        cl.sendText(msg.to, "Auto Cancel Url turned on")
                        print "[Command]Url on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Url on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Misc Section]-------------------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "�1�7" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.kickoutFromGroup(msg.to,[jj])
						cl.sendText(msg.to,"Bye...")
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						strnum = msg.text.replace("random:","")
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						try:
							num = int(strnum)
							group = cl.getGroup(msg.to)
							for var in range(0,num):
								name = "".join([random.choice(source_str) for x in xrange(10)])
								time.sleep(0.01)
								group.name = name
								cl.updateGroup(group)
						except:
							cl.sendText(msg.to,"Error")
            elif "album" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecâ†�1�7�1�7" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecâ†�1�7�1�7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def autolike():
     for zx in range(0,500):
        hasil = cl.activity(limit=500)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kd.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kd.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kf.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kf.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kg.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kg.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kh.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kh.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kj.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kj.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            kl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \n\nhttp://line.me/ti/p/pjK1Od8ftK")
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"=====Ready=====\n[★]🐯Bot Pʀᴏᴛᴇᴄᴛɪᴏɴѕ For Group\n[★]🐯Tickets Siri\n[★]🐯Sᴇʟꜰʙᴏᴛ in Your Account\n[★]🐯1 Selfbot 1 Bot Assist\n[★]🐯1 Selfbot 2 Bot Assist\n[★]🐯1 Selfbot 3 Bot Assist\n[★]🐯1 Selfbot 4 Bot Assist\n[★]🐯1 Selfbot 5 Bot Assist\n[★]🐯Ready Siri \n[★]🐯Admin Pʀᴏᴛᴇᴄᴛɪᴏɴѕ\n[★]🐯Staff Pʀᴏᴛᴇᴄᴛɪᴏɴѕ\n\nMinat??? PM Id Line http://line.me/ti/p/pjK1Od8ftK\n[★]✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈[★]")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(0.01)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()
#--------------------
def likePost():
    for zx in range(0,500):
        hasil = cl.activity(limit=500)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kd.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kf.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kg.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kh.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kj.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈ \nStatus Anda udah Kita Like,Jangan Lupa Like Back\nOwner Kami :\nhttp://line.me/ti/p/pjK1Od8ftK")
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"=====Ready=====\n[★]🐯Bot Pʀᴏᴛᴇᴄᴛɪᴏɴѕ For Group\n[★]🐯Tickets Siri\n[★]🐯Sᴇʟꜰʙᴏᴛ in Your Account\n[★]🐯1 Selfbot 1 Bot Assist\n[★]🐯1 Selfbot 2 Bot Assist\n[★]🐯1 Selfbot 3 Bot Assist\n[★]🐯1 Selfbot 4 Bot Assist\n[★]🐯1 Selfbot 5 Bot Assist\n[★]🐯Ready Siri \n[★]🐯Admin Pʀᴏᴛᴇᴄᴛɪᴏɴѕ\n[★]🐯Staff Pʀᴏᴛᴇᴄᴛɪᴏɴѕ\n\nMinat??? PM Id Line http://line.me/ti/p/pjK1Od8ftK\n[★]✍D̴E̴D̴I̴ T̴E̴A̴M̴B̴O̴T̴✈[★]")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Boss"

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
