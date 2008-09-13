#!/usr/bin/env python
#
# gmaildownloader -- Download gmail attachements and do whatever you want with them!
# author: Juan Manuel Schillaci ska@lanux.org.ar
# Copyright 2008 Juan Manuel Schillaci
# License: GPL 3.0
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.



import libgmail
cuenta=libgmail.GmailAccount(name='theskafiles', pw='nomerompaslaspelotas', state=None, domain=None)
cuenta.login()

unreadThreads = cuenta.getMessagesByQuery("is:" + libgmail.U_AS_SUBSET_UNREAD,
                                                    True)#TODO:True as default?
unreadMsgs = []
for thread in unreadThreads:
    for msg in thread:
        unreadMsgs.append(msg)

filenames={}
 
for mensaje in unreadMsgs:
    for adjunto in mensaje.attachments:
        fileHandler = open(adjunto.filename, "w")
        fileHandler.write(adjunto._getContent())
        fileHandler.close()




#file.mimetype
