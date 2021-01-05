# coding:utf-8
'''
@author: Dizzy
'''
#!/usr/bin/env python
 
from tkinter import *
from CDevice_H3C_ER3200G2 import CDevice_H3C_ER3200G2
from CDeviceType import CDeviceVersion, CAPTemplateType
from const import Const

const = Const();
const.ROUTER_MANAGERMENT_URL = "http://172.16.1.203:8080/";#"http://192.168.1.1/";#"http://172.16.1.1/";
const.ROUTER_MANAGERMENT_USERNAME = "admin";#"admin";
const.ROUTER_MANAGERMENT_PASSWORD = "admin";#"admin@123@";

class CMenu:
    
    #构造函数
    def __init__(self, oWindowMain):
        self.m_oWindowMain = oWindowMain;
        self.m_varRadioAccessMode = StringVar();
        self.m_oImage = None;
        self.m_oLine = None;
        self.m_oOval = None;
        self.m_oArc = None;
        self.m_oRect = None;
        
    def InitMainWindow(self, szWindowName, szWindowSize, szFileURL):
        self.GetMainWindow().title(szWindowName);
        self.GetMainWindow().geometry(szWindowSize);

        self.m_oLabelAccessMode = Label(self.GetMainWindow(), text='接入方式', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        self.m_oRadioPPPoEMode = Radiobutton(self.GetMainWindow(), text='PPPoE', variable=self.m_varRadioAccessMode, value='PPPoE', command=self.FnCmd_SelectRadio);
        self.m_oRadioStaticMode = Radiobutton(self.GetMainWindow(), text='Static', variable=self.m_varRadioAccessMode, value='Static', command=self.FnCmd_SelectRadio);
        self.SetVarRadioAccessMode('PPPoE');
        
        self.m_oEntryPPPoEAccount = Entry(self.GetMainWindow(), show=None, font=('Fixdsys', 14), state='disabled');
        self.m_oLabelPPPoEAccount = Label(self.GetMainWindow(), text='PPPoE账号', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryPPPoEPassword = Entry(self.GetMainWindow(), show='*', font=('Fixdsys', 14), state='disabled');
        self.m_oLabelPPPoEPassword = Label(self.GetMainWindow(), text='PPPoE密码', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryIPAddress = Entry(self.GetMainWindow(), show=None, font=('Fixdsys', 14));
        self.m_oLabelIPAddress = Label(self.GetMainWindow(), text='IP地址', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
                
        self.m_oEntryIPMask = Entry(self.GetMainWindow(), show=None, font=('Fixdsys', 14));
        self.m_oLabelIPMask = Label(self.GetMainWindow(), text='掩码', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryIPGateway = Entry(self.GetMainWindow(), show=None, font=('Fixdsys', 14));
        self.m_oLabelIPGateway = Label(self.GetMainWindow(), text='网关', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        
        self.m_oConfirmButton = Button(self.GetMainWindow(), text='确定', bg="lightblue", width=10, command=self.FnCmd_Confirm);
        self.m_oCancelButton = Button(self.GetMainWindow(), text='取消', bg="lightblue", width=10, command=self.FnCmd_Cancel);
        
        ######
        var2 = StringVar();
        var2.set(('LAN1', 'LAN2', 'LAN3', 'LAN4'))
        self.m_oListBoxLANPort = Listbox(self.GetMainWindow(), listvariable=var2);
        self.m_oLabelLANPort = Label(self.GetMainWindow(), text='端口', bg='white', font=('Arial', 12), width=30, height=2);        

    def GetMainWindow(self):
        return self.m_oWindowMain;

    def GetRadioPPPoEMode(self):
        return self.m_oRadioPPPoEMode;
    
    def GetRadioStaticMode(self):
        return self.m_oRadioStaticMode;
    
    def GetVarRadioAccessMode(self):
        return self.m_varRadioAccessMode;
    
    def SetVarRadioAccessMode(self, varAccessMode):
        self.m_varRadioAccessMode.set(varAccessMode);
    
    def GetImageFile(self):
        return self.m_oImageFile;
    
    def GetCanvas(self):
        return self.m_oCanvas;
    
    def GetLabelAccessMode(self):
        return self.m_oLabelAccessMode;
    
    def GetEntryPPPoEAccount(self):
        return self.m_oEntryPPPoEAccount;
    
    def GetEntryPPPoEPassword(self):
        return self.m_oEntryPPPoEPassword;
    
    def GetEntryIPAddress(self):
        return self.m_oEntryIPAddress;
    
    def GetEntryIPMask(self):
        return self.m_oEntryIPMask;
    
    def GetEntryIPGateway(self):
        return self.m_oEntryIPGateway;
            
    def GetLabelPPPoEAccount(self):
        return self.m_oLabelPPPoEAccount;
    
    def GetLabelPPPoEPassword(self):
        return self.m_oLabelPPPoEPassword;
    
    def GetLabelIPAddress(self):
        return self.m_oLabelIPAddress;

    def GetLabelIPMask(self):
        return self.m_oLabelIPMask;
    
    def GetLabelIPGateway(self):
        return self.m_oLabelIPGateway;
            
    def GetButtonConfirm(self):
        return self.m_oConfirmButton;
    
    def GetButtonCancel(self):
        return self.m_oCancelButton;
    
    def GetDevice(self):
        return self.m_oDevice;
    
    def GetListBoxLANPort(self):
        return self.m_oListBoxLANPort;
    
    def GetLabelLANPort(self):
        return self.m_oLabelLANPort;
    
    def MainWindowLoop(self):
        self.GetMainWindow().mainloop();
    
    def CanvasMove(self, oDraw, nVx, nVy):
        self.GetCanvas().move(oDraw, nVx, nVy);
    
    def DrawImageOnCanvas(self, nCoordinateX, nCoordinateY):
        self.m_oImage = self.GetCanvas().create_image(nCoordinateX, nCoordinateY, anchor='n',image=self.GetImageFile());
        
    def DrawLine(self, nCrdX1, nCrdY1, nCrdX2, nCrdY2):
        self.m_oLine = self.GetCanvas().create_line(nCrdX1, nCrdY1, nCrdX2, nCrdY2);
        
    def DrawOval(self, nCrdX1, nCrdY1, nCrdX2, nCrdY2, szFillColor):
        self.m_oOval = self.GetCanvas().create_oval(nCrdX1, nCrdY1, nCrdX2, nCrdY2, fill=szFillColor);
        
    def DrawArc(self, nCrdX1, nCrdY1, nCrdX2, nCrdY2, nStart, nExtent):
        self.m_oArc = self.GetCanvas().create_arc(nCrdX1, nCrdY1, nCrdX2, nCrdY2, start=nStart, extent=nExtent);

    def DrawRect(self, nCrdX1, nCrdY1, nCrdX2, nCrdY2):
        self.m_oRect = self.GetCanvas().create_rectangle(nCrdX1, nCrdY1, nCrdX2, nCrdY2);        
        
    def FnCmd_Confirm(self):
        self.m_oDevice = CDevice_H3C_ER3200G2(CDeviceVersion.H3C_ERHMG2_MNW100_R1118);
        self.GetDevice().LoginPrepare(const.ROUTER_MANAGERMENT_URL, const.ROUTER_MANAGERMENT_USERNAME, const.ROUTER_MANAGERMENT_PASSWORD);
        self.GetDevice().LoginInputUsernamePassword();
        self.GetDevice().LoginSubmit();
        #self.GetDevice().InitConnectToInternet_PPPoE(self.GetEntryPPPoEAccount().get(), self.GetEntryPPPoEPassword().get());
        #self.GetDevice().ConnectToInternet_PPPoE();
        #self.GetDevice().InitConnectToInternet_StaticLine("172.16.1.203", "255.255.255.0", "172.16.1.1", "218.2.135.1", "61.147.37.1");#IP mask gateway DNS1 DNS2
        #self.GetDevice().ConnectToInternet_StaticLine();        
        #self.GetDevice().CloseBrowser();
        self.GetDevice().CloseTab();
        
    def FnCmd_Cancel(self):
        self.GetMainWindow().destroy();
        
    def FnCmd_SelectRadio(self):
        if self.GetVarRadioAccessMode().get() == 'PPPoE':
            (self.GetEntryPPPoEAccount())['state'] = 'normal';
            (self.GetEntryPPPoEPassword())['state'] = 'normal';
            (self.GetEntryIPAddress())['state'] = 'disabled';
            (self.GetEntryIPMask())['state'] = 'disabled';
            (self.GetEntryIPGateway())['state'] = 'disabled';            
        elif self.GetVarRadioAccessMode().get() == 'Static':
            (self.GetEntryPPPoEAccount())['state'] = 'disabled';
            (self.GetEntryPPPoEPassword())['state'] = 'disabled';
            (self.GetEntryIPAddress())['state'] = 'normal';
            (self.GetEntryIPMask())['state'] = 'normal';
            (self.GetEntryIPGateway())['state'] = 'normal';
        
    def TotalPlace(self):
        self.GetLabelAccessMode().place(x = 1, y = 1);
        self.GetRadioPPPoEMode().place(x = 300, y = 1 + 5);
        self.GetRadioStaticMode().place(x = 400, y = 1 + 5);
        
        self.GetLabelPPPoEAccount().place(x = 1, y = 50);
        self.GetEntryPPPoEAccount().place(x = 300, y = 50 + 5);
        
        self.GetLabelPPPoEPassword().place(x = 1, y = 100);
        self.GetEntryPPPoEPassword().place(x = 300, y = 100 + 5);
        
        self.GetLabelIPAddress().place(x = 1, y = 150);
        self.GetEntryIPAddress().place(x = 300, y = 150 + 5);
        
        self.GetLabelIPMask().place(x = 1, y = 200);
        self.GetEntryIPMask().place(x = 300, y = 200 + 5);
        
        self.GetLabelIPGateway().place(x = 1, y = 250);
        self.GetEntryIPGateway().place(x = 300, y = 250 + 5);
              
        self.GetButtonConfirm().place(x = 300, y = 500);
        self.GetButtonCancel().place(x = 500, y = 500);
        #self.GetListBoxLANPort().pack();
        #self.GetLabelLANPort().pack();
        