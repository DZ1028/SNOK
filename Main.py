# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''

from CDevice_H3C_ER3200G2 import CDevice_H3C_ER3200G2
from CDeviceType import CDeviceVersion
from const import Const

const = Const();
const.ROUTER_MANAGERMENT_URL = "http://192.168.1.1/";#"http://172.16.1.1/";
const.ROUTER_MANAGERMENT_USERNAME = "admin";#"admin";
const.ROUTER_MANAGERMENT_PASSWORD = "@Wjw235689";#"admin@123@";

if __name__ == "__main__":
    device = CDevice_H3C_ER3200G2(CDeviceVersion.H3C_ERHMG2_MNW100_R1118);
    device.LoginPrepare(const.ROUTER_MANAGERMENT_URL, const.ROUTER_MANAGERMENT_USERNAME, const.ROUTER_MANAGERMENT_PASSWORD);
    device.LoginInputUsernamePassword();
    device.LoginSubmit();
    print(device.GetUsername(), device.GetPassword());

    #configure static line
    #device.InitConnectToInternet_StaticLine("10.1.1.3", "255.255.255.0", "10.1.1.1", "218.2.135.1", "61.147.37.1");#IP mask gateway DNS1 DNS2
    #device.ConnectToInternet_StaticLine();
    #device.CloseBrowser();
    
    #configure PPPoE
    #device.InitConnectToInternet_PPPoE("02584703630", "84703630");
    #device.ConnectToInternet_PPPoE();
    #device.CloseBrowser();
    