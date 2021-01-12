# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''

from CDevice_H3C_ER3200G2 import CDevice_H3C_ER3200G2
from CDeviceType import CDeviceVersion, CAPTemplateType
from const import Const
from CMenu import CMenu
from tkinter import *

const = Const();
const.ROUTER_MANAGERMENT_URL = "http://172.16.1.203:8080/";#"http://192.168.1.1/";#"http://172.16.1.1/";
const.ROUTER_MANAGERMENT_USERNAME = "admin";#"admin";
const.ROUTER_MANAGERMENT_PASSWORD = "admin";#"admin@123@";

if __name__ == "__main__":
    #device = CDevice_H3C_ER3200G2(CDeviceVersion.H3C_ERHMG2_MNW100_R1118);
    #device.LoginPrepare(const.ROUTER_MANAGERMENT_URL, const.ROUTER_MANAGERMENT_USERNAME, const.ROUTER_MANAGERMENT_PASSWORD);
    #device.LoginInputUsernamePassword();
    #device.LoginSubmit();
    #print(device.GetUsername(), device.GetPassword());

    #configure static line
    #device.InitConnectToInternet_StaticLine("172.16.1.203", "255.255.255.0", "172.16.1.1", "218.2.135.1", "61.147.37.1");#IP mask gateway DNS1 DNS2
    #device.ConnectToInternet_StaticLine();
    #device.CloseBrowser();
    
    #configure PPPoE
    #device.InitConnectToInternet_PPPoE("02584703630", "84703630");
    #device.ConnectToInternet_PPPoE();
    #device.CloseBrowser();
    
    #configure VLAN on LAN-x
    #device.AddVlanInterface("20", "192.168.20.1", "255.255.255.0");
    #device.AddVlanToTrunk(2, "20", ",20");
    #device.CloseBrowser();
    
    #configure DHCP Pool to VLAN-x
    #device.AddDHCPPoolToVlan("20", "192.168.20.2", "192.168.20.254", "218.2.135.1", "61.147.37.1");
    #device.CloseBrowser();
    
    #configure AP management IP
    #device.EnableAPMngIP(True);
    #device.ConfigureAPMngIP("172.17.1.1", "255.255.255.0", "172.17.1.2", "172.17.1.254");
    
    #configure AP Template
    #device.ConfigureAPTemplate("1-149", "1-149", CAPTemplateType.AP_TEMPLATE_1_149, "TEST", "test1234", "test5678");
    #device.ConfigureAPTemplate("6-153", "6-153", CAPTemplateType.AP_TEMPLATE_6_153, "TEST", "test1234", "test5678");
    #device.ConfigureAPTemplate("11-157", "11-157", CAPTemplateType.AP_TEMPLATE_11_157, "TEST", "test1234", "test5678");
    
    #configure rate limit
    #device.QosRateLimit("172.16.1.2", "172.16.1.200", "50000", "50000")
    #device.QosRateLimit("172.16.2.1", "172.16.2.254", "50000", "50000")

    init_window = Tk();
    init_window.iconbitmap('chinatelecom.ico')
   
    menu = CMenu(init_window);
    menu.InitMainWindow('翼企配', '800x600', 'pic.gif');
    menu.TotalPlace();
    menu.MainWindowLoop();
    
    # -*- coding: utf-8 -*-


    #root =tk.Tk()  # 创建窗口对象
    #root.title(string = 'ttk.Notebook演示')  #设置窗口标题
    #root.geometry('400x300+200+200')
    
    #tabControl = ttk.Notebook(root)  #创建Notebook
    
    #tab1 = tk.Frame(tabControl,bg='blue')  #增加新选项卡
    #tabControl.add(tab1, text='信息窗')  #把新选项卡增加到Notebook
    
    #tab2 = tk.Frame(tabControl,bg='yellow')
    #tabControl.add(tab2, text='综合信息')
    
    #tab3 = tk.Frame(tabControl,bg='green')
    #tabControl.add(tab3, text='技术分析')
    
    #tab4 = tk.Frame(tabControl,bg='blue')
    #tabControl.add(tab4, text='编写代码')
    
    #tab5 = tk.Frame(tabControl,bg='blue') 
    #tabControl.add(tab5, text='模拟回测')
    
    #tab6 = ttk.Frame(tabControl) 
    #tabControl.add(tab6, text='双色球')
    
    #tab7 = ttk.Frame(tabControl) 
    #tabControl.add(tab7, text='大乐透')
    #tabControl.pack(expand=1, fill="both")
    
    #tabControl.select(tab1) #选择tab1
    
    #root.mainloop()     # 进入消息循环