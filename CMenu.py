# coding:utf-8
'''
@author: Dizzy
'''
#!/usr/bin/env python

from tkinter import *
from CDevice_H3C_ER3200G2 import CDevice_H3C_ER3200G2
from CDeviceType import CDeviceVersion, CAPTemplateType
from const import Const
from pip._internal import self_outdated_check
import threading
from _overlapped import NULL
from tkinter import ttk  #装载tkinter.ttk模块,用于Python3

const = Const();
const.ROUTER_MANAGERMENT_URL = "http://172.16.1.203:8080/";#"http://192.168.1.1/";#"http://172.16.1.1/";
const.ROUTER_MANAGERMENT_USERNAME = "admin";#"admin";
const.ROUTER_MANAGERMENT_PASSWORD = "admin";#"admin@123@";

class CMenu:
    
    #构造函数
    def __init__(self, oWindowMain):
        self.m_oWindowMain = oWindowMain;
        self.m_varRadioAccessMode = StringVar();
        self.m_varVLANInterfaceDHCPIsEnabled = IntVar();
        self.m_varSmartAPTemplateIsEnabled = IntVar();
        self.m_oNoteBook = ttk.Notebook(oWindowMain);
        self.m_otabLineConnection = Frame(self.GetNoteBook(), bg='#F0F0F0');
        self.GetNoteBook().add(self.GetTabLineConnection(), text='有线配置');
        self.m_otabWifiConnection = Frame(self.GetNoteBook(), bg='#F0F0F0');
        self.GetNoteBook().add(self.GetTabWifiConnection(), text='无线配置');
        self.m_oImage = None;
        self.m_oLine = None;
        self.m_oOval = None;
        self.m_oArc = None;
        self.m_oRect = None;
        self.m_threadProgress = None;
        self.m_threadProgressWifi = None;
        
    def InitMainWindow(self, szWindowName, szWindowSize):
        self.GetMainWindow().title(szWindowName);
        self.GetMainWindow().geometry(szWindowSize);
        
        #有线配置
        self.InitLineConnection();
        
        #无线配置
        self.InitWifiConnection();
        #tabLineConnection = self.GetTabWifiConnection();#self.GetTabLineConnection();#self.GetMainWindow();
        
        ######
        #var2 = StringVar();
        #var2.set(('LAN1', 'LAN2', 'LAN3', 'LAN4'))
        #self.m_oListBoxLANPort = Listbox(tabLineConnection, listvariable=var2);
        #self.m_oLabelLANPort = Label(tabLineConnection, text='端口', bg='white', font=('Arial', 12), width=30, height=2);        

    def InitLineConnection(self):
        tabLineConnection = self.GetTabLineConnection();#self.GetTabWifiConnection();#self.GetMainWindow();

        self.m_oLabelAccessMode = Label(tabLineConnection, text='接入方式', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        self.m_oRadioPPPoEMode = Radiobutton(tabLineConnection, text='PPPoE', variable=self.m_varRadioAccessMode, value='PPPoE', command=self.FnCmd_SelectRadio);
        self.m_oRadioStaticMode = Radiobutton(tabLineConnection, text='Static', variable=self.m_varRadioAccessMode, value='Static', command=self.FnCmd_SelectRadio);
        self.SetVarRadioAccessMode('Static');
        
        self.m_oEntryPPPoEAccount = Entry(tabLineConnection, show=None, font=('Fixdsys', 14), state='disabled');
        self.m_oLabelPPPoEAccount = Label(tabLineConnection, text='PPPoE账号', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryPPPoEPassword = Entry(tabLineConnection, show='*', font=('Fixdsys', 14), state='disabled');
        self.m_oLabelPPPoEPassword = Label(tabLineConnection, text='PPPoE密码', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryIPAddress = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelIPAddress = Label(tabLineConnection, text='IP地址', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
                
        self.m_oEntryIPMask = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelIPMask = Label(tabLineConnection, text='掩码', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryIPGateway = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelIPGateway = Label(tabLineConnection, text='网关', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryVLANNew = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelVLANNew = Label(tabLineConnection, text='新增VLAN(无线)', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);        

        self.m_oEntryVLANInterfaceIP = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelVLANInterfaceIP = Label(tabLineConnection, text='新增VLAN接口地址', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
                
        self.m_oEntryVLANInterfaceMask = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelVLANInterfaceMask = Label(tabLineConnection, text='新增VLAN接口掩码', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oCheckButtonVLANInterfaceDHCPIsEnabled = Checkbutton(tabLineConnection, text='开启DHCP', variable=self.m_varVLANInterfaceDHCPIsEnabled, onvalue=1, offvalue=0);
        self.m_oLabelVLANInterfaceDHCPIsEnabled = Label(tabLineConnection, text='VLAN接口开启DHCP', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);         
        
        self.m_oConfirmButton = Button(tabLineConnection, text='确定', bg="lightblue", width=10, command=self.FnCmd_Confirm);
        self.m_oCancelButton = Button(tabLineConnection, text='取消', bg="lightblue", width=10, command=self.FnCmd_Cancel);
                
    def InitWifiConnection(self):
        tabLineConnection = self.GetTabWifiConnection();

        self.m_oEntrySSIDName2Dot4G = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelSSIDName2Dot4G = Label(tabLineConnection, text='2.4G SSID名称', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntrySSIDPassword2Dot4G = Entry(tabLineConnection, show='*', font=('Fixdsys', 14));
        self.m_oLabelSSIDPassword2Dot4G = Label(tabLineConnection, text='2.4G SSID密钥', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntrySSIDName5G = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelSSIDName5G = Label(tabLineConnection, text='5G SSID名称', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntrySSIDPassword5G = Entry(tabLineConnection, show='*', font=('Fixdsys', 14));
        self.m_oLabelSSIDPassword5G = Label(tabLineConnection, text='5G SSID密钥', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryVLANWifi = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelVLANWifi = Label(tabLineConnection, text='业务VLAN(无线)', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);        

        self.m_oEntryAPManagementIPStart = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelAPManagementIPStart = Label(tabLineConnection, text='AP管理IP地址(起始)', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oEntryAPManagementIPEnd = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelAPManagementIPEnd = Label(tabLineConnection, text='AP管理IP地址(结束)', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);

        self.m_oEntrySpeedLimitUpload = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelSpeedLimitUpload = Label(tabLineConnection, text='单终端限速(上行)kbps', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);

        self.m_oEntrySpeedLimitDownload = Entry(tabLineConnection, show=None, font=('Fixdsys', 14));
        self.m_oLabelSpeedLimitDownload = Label(tabLineConnection, text='单终端限速(下行)kbps', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2);
        
        self.m_oCheckButtonSmartAPTemplateIsEnabled = Checkbutton(tabLineConnection, text='开启智能AP频点选择', variable=self.m_varSmartAPTemplateIsEnabled, onvalue=1, offvalue=0);
        self.m_oLabelSmartAPTemplateIsEnabled = Label(tabLineConnection, text='AP频点自动选择开启模式', bg='#F0F0F0', font=('Fixdsys', 12), width=30, height=2); 
        
        self.m_oConfirmButtonWifi = Button(tabLineConnection, text='确定', bg="lightblue", width=10, command=self.FnCmd_ConfirmWifi);
        self.m_oCancelButtonWifi = Button(tabLineConnection, text='取消', bg="lightblue", width=10, command=self.FnCmd_Cancel);
                                
    def GetMainWindow(self):
        return self.m_oWindowMain;

    def GetRadioPPPoEMode(self):
        return self.m_oRadioPPPoEMode;
    
    def GetRadioStaticMode(self):
        return self.m_oRadioStaticMode;
    
    def GetCheckButtonVLANInterfaceDHCPIsEnabled(self):
        return self.m_oCheckButtonVLANInterfaceDHCPIsEnabled;
    
    def GetVarRadioAccessMode(self):
        return self.m_varRadioAccessMode;
    
    def SetVarRadioAccessMode(self, varAccessMode):
        self.m_varRadioAccessMode.set(varAccessMode);
        
    def GetVarVLANInterfaceDHCPIsEnabled(self):
        return self.m_varVLANInterfaceDHCPIsEnabled;
    
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
    
    def GetEntryVLANNew(self):
        return self.m_oEntryVLANNew;
    
    def GetEntryVLANInterfaceIP(self):
        return self.m_oEntryVLANInterfaceIP;
    
    def GetEntryVLANInterfaceMask(self):
        return self.m_oEntryVLANInterfaceMask;
    
    def GetNoteBook(self):
        return self.m_oNoteBook;
    
    def GetTabLineConnection(self):
        return self.m_otabLineConnection;
    
    def GetTabWifiConnection(self):
        return self.m_otabWifiConnection;
      
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
    
    def GetLabelVLANNew(self):
        return self.m_oLabelVLANNew;
    
    def GetLabelVLANInterfaceIP(self):
        return self.m_oLabelVLANInterfaceIP;
    
    def GetLabelVLANInterfaceMask(self):
        return self.m_oLabelVLANInterfaceMask;
    
    def GetLabelVLANInterfaceDHCPIsEnabled(self):
        return self.m_oLabelVLANInterfaceDHCPIsEnabled;
    
    def GetThreadProgress(self):
        return self.m_threadProgress;
            
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
        self.m_threadProgress = threading.Thread(target=self.FnCmd_LineNetwork, args=( ));
        self.GetThreadProgress().setDaemon(True);
        self.GetThreadProgress().start();

    def FnCmd_ConfirmWifi(self):
        self.m_threadProgressWifi = threading.Thread(target=self.FnCmd_WifiNetwork, args=( ));
        self.m_threadProgressWifi.setDaemon(True);
        self.m_threadProgressWifi.start();
        pass;
                
    def FnCmd_LineNetwork(self):
        #login
        self.m_oDevice = CDevice_H3C_ER3200G2(CDeviceVersion.H3C_ERHMG2_MNW100_R1118);
        self.GetDevice().LoginPrepare(const.ROUTER_MANAGERMENT_URL, const.ROUTER_MANAGERMENT_USERNAME, const.ROUTER_MANAGERMENT_PASSWORD);
        self.GetDevice().LoginInputUsernamePassword();
        self.GetDevice().LoginSubmit();
        
        #connect to internet
        if self.GetEntryPPPoEAccount().get() != '' and self.GetEntryPPPoEPassword() != '': 
            self.GetDevice().InitConnectToInternet_PPPoE(self.GetEntryPPPoEAccount().get(), self.GetEntryPPPoEPassword().get());
            self.GetDevice().ConnectToInternet_PPPoE();
        elif self.GetEntryIPAddress() != '' and self.GetEntryIPMask().get() != '' and self.GetEntryIPGateway().get() != '':
            self.GetDevice().InitConnectToInternet_StaticLine(self.GetEntryIPAddress().get(), self.GetEntryIPMask().get(), self.GetEntryIPGateway().get(), "218.2.135.1", "61.147.37.1");#IP mask gateway DNS1 DNS2
            self.GetDevice().ConnectToInternet_StaticLine();        
        
        #add vlan interface
        if self.GetEntryVLANNew().get() != '' and self.GetEntryVLANInterfaceIP().get() != '' and self.GetEntryVLANInterfaceMask().get() != '':
            self.GetDevice().AddVlanInterface(self.GetEntryVLANNew().get(), self.GetEntryVLANInterfaceIP().get(), self.GetEntryVLANInterfaceMask().get());
            #configure DHCP Pool to VLAN-x
            if (self.GetVarVLANInterfaceDHCPIsEnabled()).get() == 1:
                self.GetDevice().AddDHCPPoolToVlan(self.GetEntryVLANNew().get(), self.GetEntryVLANInterfaceIP().get()[0:-1]+'2', self.GetEntryVLANInterfaceIP().get()[0:-1]+'254', "218.2.135.1", "61.147.37.1");
        
        #close the browser
        #self.GetDevice().CloseBrowser();
        self.GetDevice().CloseTab();
        
    def FnCmd_WifiNetwork(self):
        #login
        self.m_oDevice = CDevice_H3C_ER3200G2(CDeviceVersion.H3C_ERHMG2_MNW100_R1118);
        self.GetDevice().LoginPrepare(const.ROUTER_MANAGERMENT_URL, const.ROUTER_MANAGERMENT_USERNAME, const.ROUTER_MANAGERMENT_PASSWORD);
        self.GetDevice().LoginInputUsernamePassword();
        self.GetDevice().LoginSubmit();
        
        #configure AP Template
        if self.m_oEntrySSIDName2Dot4G.get() != '' and self.m_oEntrySSIDName5G.get() != '' and self.m_oEntrySSIDPassword2Dot4G.get() != '' and self.m_oEntrySSIDPassword5G.get() != '':
            self.GetDevice().ConfigureAPTemplate("1-149", "1-149", CAPTemplateType.AP_TEMPLATE_1_149, self.m_oEntrySSIDName2Dot4G.get(), self.m_oEntrySSIDName5G.get(), self.m_oEntrySSIDPassword2Dot4G.get(), self.m_oEntrySSIDPassword5G.get());
            self.GetDevice().ConfigureAPTemplate("6-153", "6-153", CAPTemplateType.AP_TEMPLATE_6_153, self.m_oEntrySSIDName2Dot4G.get(), self.m_oEntrySSIDName5G.get(), self.m_oEntrySSIDPassword2Dot4G.get(), self.m_oEntrySSIDPassword5G.get());
            self.GetDevice().ConfigureAPTemplate("11-157", "11-157", CAPTemplateType.AP_TEMPLATE_11_157, self.m_oEntrySSIDName2Dot4G.get(), self.m_oEntrySSIDName5G.get(), self.m_oEntrySSIDPassword2Dot4G.get(), self.m_oEntrySSIDPassword5G.get());

        #configure speed limits
        if self.GetEntryVLANInterfaceIP().get() != '' and self.m_oEntrySpeedLimitUpload.get() != '' and self.m_oEntrySpeedLimitDownload.get() != '':
            self.GetDevice().QosRateLimit(self.GetEntryVLANInterfaceIP().get()[0:-1]+'2', self.GetEntryVLANInterfaceIP().get()[0:-1]+'254', self.m_oEntrySpeedLimitUpload.get(), self.m_oEntrySpeedLimitDownload.get());
            self.GetDevice().QosRateLimit("192.168.1.2", "192.168.1.254", self.m_oEntrySpeedLimitUpload.get(), self.m_oEntrySpeedLimitDownload.get());
        
        #configure AP management IP
        if self.m_oEntryAPManagementIPStart.get() != '' and self.m_oEntryAPManagementIPEnd.get() != '':
            self.GetDevice().EnableAPMngIP(True);
            self.GetDevice().ConfigureAPMngIP(self.m_oEntryAPManagementIPStart.get()[0:-1]+'1', "255.255.255.0", self.m_oEntryAPManagementIPStart.get(), self.m_oEntryAPManagementIPEnd.get());
    
        #choose Template for AP
        if self.m_varSmartAPTemplateIsEnabled.get() == 1:
            pass;
        else:
            pass;
        #configure VLAN for AP
        
        #close the browser
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
        self.GetNoteBook().pack(expand = 1, fill='both');
        self.GetNoteBook().select(self.GetTabLineConnection());
        
        self.LineConnectionPlace();
        self.WifiConnectionPlace();
        
        #self.GetListBoxLANPort().pack();
        #self.GetLabelLANPort().pack();
        
    def LineConnectionPlace(self):
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
        
        self.GetLabelVLANNew().place(x = 1, y = 300);
        self.GetEntryVLANNew().place(x = 300, y = 300 + 5);
        
        self.GetLabelVLANInterfaceIP().place(x = 1, y = 350);
        self.GetEntryVLANInterfaceIP().place(x = 300, y = 350 + 5);
        
        self.GetLabelVLANInterfaceMask().place(x = 1, y = 400);
        self.GetEntryVLANInterfaceMask().place(x = 300, y = 400 + 5);
        
        self.GetLabelVLANInterfaceDHCPIsEnabled().place(x = 1, y = 450);
        self.GetCheckButtonVLANInterfaceDHCPIsEnabled().place(x = 300, y = 450 + 5);
        
        self.GetButtonConfirm().place(x = 300, y = 500);
        self.GetButtonCancel().place(x = 500, y = 500); 
        
    def WifiConnectionPlace(self):
        self.m_oLabelSSIDName2Dot4G.place(x = 1, y = 1);
        self.m_oEntrySSIDName2Dot4G.place(x = 300, y = 1 + 5);
        
        self.m_oLabelSSIDPassword2Dot4G.place(x = 1, y = 50);
        self.m_oEntrySSIDPassword2Dot4G.place(x = 300, y = 50 + 5);
        
        self.m_oLabelSSIDName5G.place(x = 1, y = 100);
        self.m_oEntrySSIDName5G.place(x = 300, y = 100 + 5);
        
        self.m_oLabelSSIDPassword5G.place(x = 1, y = 150);
        self.m_oEntrySSIDPassword5G.place(x = 300, y = 150 + 5);
        
        self.m_oLabelVLANWifi.place(x = 1, y = 200);
        self.m_oEntryVLANWifi.place(x = 300, y = 200 + 5);
        
        self.m_oLabelAPManagementIPStart.place(x = 1, y = 250);
        self.m_oEntryAPManagementIPStart.place(x = 300, y = 250 + 5);

        self.m_oLabelAPManagementIPEnd.place(x = 1, y = 300);
        self.m_oEntryAPManagementIPEnd.place(x = 300, y = 300 + 5);

        self.m_oLabelSpeedLimitUpload.place(x = 1, y = 350);
        self.m_oEntrySpeedLimitUpload.place(x = 300, y = 350 + 5);
        
        self.m_oLabelSpeedLimitDownload.place(x = 1, y = 400);
        self.m_oEntrySpeedLimitDownload.place(x = 300, y = 400 + 5);
        
        self.m_oLabelSmartAPTemplateIsEnabled.place(x = 1, y = 450);
        self.m_oCheckButtonSmartAPTemplateIsEnabled.place(x = 300, y = 450 + 5);
        
        self.m_oConfirmButtonWifi.place(x = 300, y = 500);
        self.m_oCancelButtonWifi.place(x = 500, y = 500);        