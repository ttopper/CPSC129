#---------------------------------------------------------------------------
# Copyright (c) 2007 Christopher Schmidt 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#   * Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
# 
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
# 
#   * Neither the name of Christopher Schmidt nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import  sys, base64
import  wx
import httplib, urlparse

try:
    import wx.lib.delayedresult as delayedresult
except ImportError:
    class delayedresult:
        def _startWorker(self, consumer, producer, **kwargs):
            data = producer()
            consumer(data)
        startWorker = classmethod(_startWorker)   

LICENSE = "BSD" 

VERSION = "$Id$"

DEFAULT_URL = "http://featureserver.org/featureserver.cgi/scribble?maxfeatures=1"

class RESTPanel(wx.Panel):
    """Displays all the boxes and stuff."""
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent, -1)
        self.entered_username = ""
        self.entered_password = ""
        self.job_id = 1
        self.display_response = "data"
        self.data_entry = "data"
        self.states = [] 
        self.send_data = {'data': '', 'headers':'User-Agent: RESTClient-%s' % VERSION.replace(":", "")}
        
        url_label = wx.StaticText(self, -1, "URL:")
        self.url = wx.ComboBox(
                    self, 501, DEFAULT_URL, (90, 80), (-1, -1), [DEFAULT_URL], wx.CB_DROPDOWN)
                    
        wx.CallAfter(self.url.SetInsertionPoint, 0)
        self.url.Bind(wx.EVT_CHAR, self.URLEvtChar)
        self.Bind(wx.EVT_COMBOBOX, self.HistorySelect, self.url)

        
        self.methodList = ['GET', 'POST', 'PUT', 'DELETE']

        self.ch = wx.Choice(self, -1, (100, 50), choices = self.methodList)
        self.ch.Select(0)

        content_label = wx.StaticText(self, -1, "Your Content")
        self.content_entry = wx.TextCtrl(self, -1, "",
                       style=wx.TE_MULTILINE)

        self.content_entry.SetInsertionPoint(0)
        
        remote_content_label = wx.StaticText(self, -1, "Remote Content")
        response_code = wx.StaticText(self, -1, "")
        self.response_code = response_code
        t3 = wx.TextCtrl(self, -1, "",
                       style=wx.TE_MULTILINE)

        t3.SetInsertionPoint(0)
        
        b = wx.Button(self, -1, "Load URL")
        self.Bind(wx.EVT_BUTTON, self.LoadDataEvent, b)
        
        self.headers_button = wx.Button(self, -1, "Show Headers")
        self.Bind(wx.EVT_BUTTON, self.ShowOtherResponse, self.headers_button)
        
        self.entry_headers = wx.Button(self, -1, "Change Headers")
        self.Bind(wx.EVT_BUTTON, self.ShowOtherEntry, self.entry_headers)
        
        self.tc = t3

        basic_auth_button = wx.Button(self, -1, "Enter Basic Auth Info")
        self.Bind(wx.EVT_BUTTON, self.EnterBasicAuthInfo, basic_auth_button)
        
        space = 4
        bsizer = wx.BoxSizer(wx.VERTICAL)
        bsizer.Add(self.ch, 0, wx.GROW|wx.ALL, space)
        bsizer.Add(self.entry_headers, 0, wx.GROW|wx.ALL, space)
        bsizer.Add(basic_auth_button, 0, wx.GROW|wx.ALL, space)
        
        self.gauge = wx.Gauge(self, -1, 50, (110, 50), (200, 25))

        sizer = wx.FlexGridSizer(cols=3, hgap=space, vgap=space)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(4)
        sizer.AddMany(
          [  url_label, (self.url, 0, wx.EXPAND), b,
             (0,0), (self.gauge,0, wx.EXPAND), (0,0),
             content_label, (self.content_entry, 0, wx.EXPAND), bsizer,
             remote_content_label, response_code, self.headers_button,
             (0,0),(t3, 0, wx.EXPAND), (0,0),
          ])
        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(sizer, 1, wx.EXPAND|wx.ALIGN_CENTRE|wx.ALL, 25)
        self.SetSizer(border)
        self.SetAutoLayout(True)

    def SaveState(self):
        history = {}
        self.UpdateContent()
        history['send_headers'] = self.send_data['headers'] 
        history['send_body'] = self.send_data['data'] 
        history['url'] = self.url.GetValue()
        history['method'] = self.GetMethod()
        self.states.insert(0,history)
    
    def HistorySelect(self, event):
        self.url.SetValue(event.GetString())

    def EnterBasicAuthInfo(self,event):
        username = password = None
        dlg = BasicAuthDialog(self, -1, "Sample", size=(500,250))

        if dlg.ShowModal() == wx.ID_OK:
            self.entered_username = username = dlg.username.GetValue()
            self.entered_password = password = dlg.password.GetValue()

        dlg.Destroy()

        if not username or not password: return False    
        headers = self.send_data['headers']
        
        headers = headers.split("\n")
        headers_dict = {}
        for header in headers:
           parts = header.split(":", 1)
           if len(parts) > 1:
               headers_dict[parts[0]] = parts[1].strip() 
        base64string = base64.encodestring('%s:%s' % (username, password))[:-1]    
        headers_dict['Authorization'] = "Basic %s" % base64string    
        headers_string = []
        for key, value in headers_dict.items():
            headers_string.append("%s: %s" % (key, value))
        self.send_data['headers'] = "\n".join(headers_string)
        if self.data_entry != "data":
            self.content_entry.SetValue(self.send_data['headers'])

    def LoadDataEvent(self,event):
        self.DelayedWorkerLoadData()

    def URLEvtChar(self, event):
        """If the user hit enter in the URL box, fire loaddata"""
        if event.GetKeyCode() == 13:
            self.DelayedWorkerLoadData()
        else: 
            self.gauge.SetValue(0)
            event.Skip()
    
    def ShowOtherEntry(self, event):
        """Swap entry boxes from entering data to headers"""
        self.UpdateContent()
        if self.data_entry == "data":
            self.content_entry.SetValue(self.send_data['headers'])
            self.data_entry = "headers"
            self.entry_headers.SetLabel("Change Data")
        else:
            self.content_entry.SetValue(self.send_data['data'])
            self.data_entry = "data"
            self.entry_headers.SetLabel("Change Headers")
   
    def UpdateContent(self):
        """Update local send_data object based on current display""" 
        if self.data_entry == "data":
            self.send_data['data'] = self.content_entry.GetValue()
        else:    
            self.send_data['headers'] = self.content_entry.GetValue()
        
    
    def ShowOtherResponse(self, event):
        """Swaps the response display between data and headers."""
        if self.display_response == "data":
            headers = self.headers
            headers_string = []
            for header in headers:
                headers_string.append("%s: %s" % (header[0], header[1]))
            self.tc.SetValue("\n".join(headers_string))
            self.headers_button.SetLabel("Show Data")
            self.display_response = "headers"
        else:    
            self.tc.SetValue(self.data)
            self.headers_button.SetLabel("Show Headers")
            self.display_response = "data"
    
    def DelayedWorkerLoadData(self):
        if hasattr(self.gauge, "Pulse"):
            self.gauge.Pulse()
        else:
            self.gauge.SetRange(2)
            self.gauge.SetValue(1)
            
        self.tc.SetValue("Loading...")
        self.job_id += 1
        self.url.Insert(self.url.GetValue(),0)
        self.SaveState()
        delayedresult.startWorker(self.LoadComplete, self.LoadData, 
                                          jobID=self.job_id)
    def LoadComplete(self, value):
        if self.display_response == "data":
            self.tc.SetValue(self.data)
        else:    
            headers = self.headers
            headers_string = []
            for header in headers:
                headers_string.append("%s: %s" % (header[0], header[1]))
            self.tc.SetValue("\n".join(headers_string))
        self.gauge.SetRange(1)
        self.gauge.SetValue(1)

    def GetMethod(self):
        selection = self.ch.GetSelection()
        if selection == -1:
            selection = 0 
        method = self.methodList[selection]
        if not method: method = "GET"
        return method

    def LoadData(self):
        """Loads the data from the server, using the current settings""" 
        method = self.GetMethod()
        url = self.url.GetValue()
        self.UpdateContent()
        data = self.send_data['data']
        headers = self.send_data['headers']
        
        headers = headers.split("\n")
        headers_dict = {}
        for header in headers:
           parts = header.split(":")
           if len(parts) > 1:
               headers_dict[parts[0]] = parts[1].strip() 
        urlparts = urlparse.urlparse(url)
        conn = httplib.HTTPConnection(urlparts[1])
        url = "%s?%s" % (urlparts[2], urlparts[4])
        
        if method == "POST" or method == "PUT":
            conn.request(method, url, data, headers_dict)
        else:
            conn.request(method, url, None, headers_dict)
            
        response = conn.getresponse()
        self.response_code.SetLabel("%s %s" % (response.status, response.reason))
        self.data = response.read()
        self.headers = response.getheaders()

class BasicAuthDialog(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE
            ):
        wx.Dialog.__init__(self,parent,ID,title,size=size,pos=pos)
        # Now continue with the normal construction of the dialog
        # contents
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        label = wx.StaticText(self, -1, "Enter Basic Auth Username/Password")
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Username:")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        text = wx.TextCtrl(self, -1, "", size=(300,-1))
        box.Add(text, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        text.SetValue(parent.entered_username)
        self.username = text

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Password:")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        text = wx.TextCtrl(self, -1, "", size=(300,-1), style=wx.TE_PASSWORD)
        box.Add(text, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        text.SetValue(parent.entered_password)
        self.password = text

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()
        
        btn = wx.Button(self, wx.ID_OK)
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL)
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)


class RunRESTApp(wx.App):
    """Built from wxPython examples"""
    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, False, filename)
    def OnInit(self):
        #wx.Log_SetActiveTarget(wx.LogStderr())

        frame = wx.Frame(None, -1, "RESTClient", pos=(50,50), size=(200,100),
                        style=wx.DEFAULT_FRAME_STYLE)
        frame.CreateStatusBar()

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "E&xit\tCtrl-Q", "Exit demo")
        self.Bind(wx.EVT_MENU, self.OnExitApp, item)
        menuBar.Append(menu, "&File")

        frame.SetMenuBar(menuBar)
        frame.Show(True)

        win = RESTPanel(frame)

        # so set the frame to a good size for showing stuff
        frame.SetSize((800,600))
        win.SetFocus()
        self.window = win
        #ns['win'] = win
        frect = frame.GetRect()

        self.SetTopWindow(frame)
        self.frame = frame
        
        return True


    def OnExitApp(self, evt):
        self.frame.Close(True)

#---------------------------------------------------------------------------

if __name__ == '__main__':
    import sys,os
    app = RunRESTApp()
    app.MainLoop()
