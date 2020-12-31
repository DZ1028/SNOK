# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''
from CDeviceType import *
from CDeviceType import CDeviceVersion
from CDevice import CDevice
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
from selenium.webdriver.support.select import Select
from const import Const
from selenium.webdriver.common.action_chains import ActionChains
import time
from _ast import If

const = Const();
const.NAME_ACCOUNT = "account";
const.NAME_PASSWORD = "password";
const.NAME_SUBMIT = "btnSubmit";
const.LINK_TEXT_CONNECT_TO_INTERNET = "连接到因特网";
const.EXTEND_URL_WAN_NEW = "wan_new.asp";
const.EXTEND_URL_VLAN_ADD = "vlan_intf_set.asp";
const.EXTEND_URL_VLAN_PORT_SET = "vlan_port_set.asp";
const.EXTEND_URL_DHCP_ADD_TO_VLAN = "dhcpd_vlan.asp";
const.EXTEND_URL_CONFIG_AP_MNG_IP = "address_manage.asp";
const.EXTEND_URL_ENABLE_AP_MNG_IP = "ap_manage_set.asp";
const.EXTEND_URL_ADD_AP_TEMPLATE = "config_manage.asp";
const.EXTEND_URL_ADD_AP_TEMPLATE_LIST = "ap_config_comment_list.asp";
const.EXTEND_URL_ADD_SSID = "wlan_ap_ssid_config.asp";

class CDevice_H3C_ER3200G2(CDevice):
    '''
    classdocs
    '''

    def __init__(self, enDeviceVersion):
        '''
        Constructor
        '''
        CDevice.__init__(self);
        CDevice.SetDeviceType(self, CDeviceType.H3C_ER3200G2);
        CDevice.SetDeviceVersion(self, enDeviceVersion);
        
        
    def LoginInputUsernamePassword(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            self.GetBrowser().find_element_by_name(const.NAME_ACCOUNT).send_keys(self.GetUsername());
            self.GetBrowser().find_element_by_name(const.NAME_PASSWORD).send_keys(self.GetPassword());
        
    def LoginSubmit(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            self.GetBrowser().find_element_by_name(const.NAME_SUBMIT).send_keys(Keys.ENTER); 
        
    def ConnectToInternet_StaticLine(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_WAN_NEW);
            Select(self.GetBrowser().find_element_by_name("wan1IPMode")).select_by_index(0);
            self.GetBrowser().find_element_by_name("WAN1_IP").clear();
            self.GetBrowser().find_element_by_name("WAN1_IP").send_keys(CDevice.GetStaticLineIP(self));
            elementNetMask = self.GetBrowser().find_element_by_name("WAN1_NM");
            elementNetMask.clear();
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys(Keys.BACKSPACE);
            elementNetMask.send_keys((CDevice.GetStaticLineMask(self))[1:]);
            self.GetBrowser().find_element_by_name("WAN1_GW").clear();
            self.GetBrowser().find_element_by_name("WAN1_GW").send_keys(CDevice.GetStaticLineGateway(self));
            self.GetBrowser().find_element_by_name("WAN1_DS1").clear();
            self.GetBrowser().find_element_by_name("WAN1_DS1").send_keys(CDevice.GetStaticLineDNS1(self));
            self.GetBrowser().find_element_by_name("WAN1_DS2").clear();
            self.GetBrowser().find_element_by_name("WAN1_DS2").send_keys(CDevice.GetStaticLineDNS2(self));
            self.GetBrowser().find_element_by_xpath("//input[@value='应用'][@type='button']").click();
            time.sleep(1)
            #CDevice.CloseTab(self);
        
    def ConnectToInternet_PPPoE(self):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_WAN_NEW);
            Select(self.GetBrowser().find_element_by_name("wan1IPMode")).select_by_index(2);
            self.GetBrowser().find_element_by_name("WAN1_PUN").clear();
            self.GetBrowser().find_element_by_name("WAN1_PUN").send_keys(CDevice.GetPPPoEAccountName(self));
            self.GetBrowser().find_element_by_name("WAN1_PPW").clear();
            self.GetBrowser().find_element_by_name("WAN1_PPW").send_keys(CDevice.GetPPPoEPassword(self));
            self.GetBrowser().find_element_by_xpath("//input[@value='应用'][@type='button']").click();
            time.sleep(1)
            #CDevice.CloseTab(self);
        
    def AddVlanInterface(self, szVlanId, szInterfaceIp, szMask):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_VLAN_ADD);
            self.GetBrowser().find_element_by_name("op_new").click();
            self.GetBrowser().find_element_by_name("vlan_id").clear();
            self.GetBrowser().find_element_by_name("vlan_id").send_keys(szVlanId);
            self.GetBrowser().find_element_by_name("IP").clear();
            self.GetBrowser().find_element_by_name("IP").send_keys(szInterfaceIp);
            self.GetBrowser().find_element_by_name("mask").clear();
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(Keys.BACKSPACE);
            self.GetBrowser().find_element_by_name("mask").send_keys(szMask[1:]);
            self.GetBrowser().find_element_by_name("amend").click();
            time.sleep(1)
            #CDevice.CloseTab(self);
            
    def AddVlanToTrunk(self, nIndex, szPVID, szAllowedVlan):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_VLAN_PORT_SET);
            frameConfigureVlanPort = self.GetBrowser().find_element_by_tag_name("iframe");
            self.GetBrowser().switch_to_frame(frameConfigureVlanPort);
            #portLanSWElement = self.GetBrowser().find_elements_by_link_text("LAN1");
            #ActionChains(self.GetBrowser()).double_click(portLanSWElement).perform();
            #self.GetBrowser().find_element_by_xpath("//IMG["+ str(nIndex) + "]").click();
            self.GetBrowser().find_element_by_xpath("//table[@id='disableclick']/tbody/tr[" + str(nIndex + 1) + "]/td[1]").click();
            self.GetBrowser().switch_to_default_content();
            selectorPVID = self.GetBrowser().find_element_by_name("pvid_value");
            Select(selectorPVID).select_by_value(szPVID);
            self.GetBrowser().find_element_by_name("permit_vlan").send_keys(szAllowedVlan);
            #time.sleep(3)
            self.GetBrowser().find_element_by_name("permit_vlan").send_keys(Keys.TAB, Keys.ENTER);
            time.sleep(1)
            #self.GetBrowser().find_element_by_name("permit_vlan").send_keys(Keys.ENTER);
            #CDevice.CloseTab(self);
            
    def AddDHCPPoolToVlan(self, szVlanId, szDHCPPoolStartIp, szDHCPPoolEndIp, szDNS1, szDNS2):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_DHCP_ADD_TO_VLAN);
            self.GetBrowser().find_element_by_name("op_new").click();
            selectorVLAN = self.GetBrowser().find_element_by_name("dhcpd_vlan");
            Select(selectorVLAN).select_by_value("VLAN" + szVlanId);
            self.GetBrowser().find_element_by_name("dhcp_en").click();
            self.GetBrowser().find_element_by_name("StartIP").send_keys(szDHCPPoolStartIp);
            self.GetBrowser().find_element_by_name("EndIP").send_keys(szDHCPPoolEndIp);
            self.GetBrowser().find_element_by_name("MainDNS").send_keys(szDNS1);
            self.GetBrowser().find_element_by_name("SecondDNS").send_keys(szDNS2);
            self.GetBrowser().find_element_by_name("amend").click();
            time.sleep(1)
            
    def EnableAPMngIP(self, bIsEnabled):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_ENABLE_AP_MNG_IP);
            if bIsEnabled == True:
                Select(self.GetBrowser().find_element_by_name("manage_set")).select_by_index(1);
            elif bIsEnabled == False:
                Select(self.GetBrowser().find_element_by_name("manage_set")).select_by_index(0); 
            self.GetBrowser().find_element_by_id("amend").click();
            time.sleep(1)
            
    def ConfigureAPMngIP(self, szAPMngIP, szAPMngMask, szAPStartIP, szAPEndIP):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_CONFIG_AP_MNG_IP);
            self.GetBrowser().find_element_by_name("PrivIP").clear();
            self.GetBrowser().find_element_by_name("PrivIP").send_keys(szAPMngIP);
            self.GetBrowser().find_element_by_name("PrivMask").clear();
            self.GetBrowser().find_element_by_name("PrivMask").send_keys(szAPMngMask);
            self.GetBrowser().find_element_by_name("PrivPoolStart").clear();
            self.GetBrowser().find_element_by_name("PrivPoolStart").send_keys(szAPStartIP);
            self.GetBrowser().find_element_by_name("PrivPoolEnd").clear();
            self.GetBrowser().find_element_by_name("PrivPoolEnd").send_keys(szAPEndIP);
            self.GetBrowser().find_element_by_id("id_confirm").click();
            time.sleep(1)
            
    def ConfigureAPTemplate(self, szTemplateName, szTemplateDesc, enApTemplateType, szCustomerSSID, szCustomerKey1, szCustomerKey2):
        if CDevice.GetDeviceType(self) == CDeviceType.H3C_ER3200G2 and CDevice.GetDeviceVersion(self) == CDeviceVersion.H3C_ERHMG2_MNW100_R1118:
            CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_ADD_AP_TEMPLATE);
            self.GetBrowser().find_element_by_name("op_new").click();
            allhandles=self.GetBrowser().window_handles;  #获取当前窗口句柄
            #print(allhandles);
            if self.GetBrowser().current_window_handle==allhandles[1]:  
                pass;
            else:
                self.GetBrowser().switch_to_window(allhandles[1]);#切换窗口
            #CDevice.OpenURL(self, self.GetURL() + const.EXTEND_URL_ADD_AP_TEMPLATE_LIST);
            self.GetBrowser().find_element_by_name("template_name").send_keys(szTemplateName);
            self.GetBrowser().find_element_by_name("template_describe").send_keys(szTemplateDesc);
            #self.GetBrowser().find_element_by_xpath("//tr[@id='Ssidbasicset']/td[1]").click();
            Select(self.GetBrowser().find_element_by_name("swlanMode")).select_by_index(4);
            Select(self.GetBrowser().find_element_by_name("swlanWidth")).select_by_index(1);
            if enApTemplateType == CAPTemplateType.AP_TEMPLATE_1_149:
                Select(self.GetBrowser().find_element_by_name("wlanChannel")).select_by_index(1);
            elif enApTemplateType == CAPTemplateType.AP_TEMPLATE_6_153:    
                Select(self.GetBrowser().find_element_by_name("wlanChannel")).select_by_index(6);
            elif enApTemplateType == CAPTemplateType.AP_TEMPLATE_11_157:
                Select(self.GetBrowser().find_element_by_name("wlanChannel")).select_by_index(11);
            
            self.ConfigureExistSSID(szCustomerSSID + "-2.4G", szCustomerKey1, CFrequencePointType.FREQUENCE_POINT_2Dot4G);
            self.ConfigureNewSSID(szCustomerSSID + "Guest-2.4G", szCustomerKey2);
            self.GetBrowser().find_element_by_xpath("//tr[@id='Ssidbasicset']/td[1]").click();
            time.sleep(1);
            self.GetBrowser().find_element_by_xpath("//tr[@id='Ssidbasicset']/td[1]").click();
            time.sleep(1);  
            self.GetBrowser().find_element_by_xpath("//tr[@id='Ssidbasicset']/td[1]").click();
                
            self.GetBrowser().find_element_by_xpath("//tr[@id='ssidtaile5G']/td[1]").click();
            Select(self.GetBrowser().find_element_by_name("swlanMode_5g")).select_by_index(1);
            Select(self.GetBrowser().find_element_by_name("swlanWidth_5g")).select_by_index(2);
            if enApTemplateType == CAPTemplateType.AP_TEMPLATE_1_149:
                Select(self.GetBrowser().find_element_by_name("wlanChannel_5g")).select_by_index(9);
            elif enApTemplateType == CAPTemplateType.AP_TEMPLATE_6_153:    
                Select(self.GetBrowser().find_element_by_name("wlanChannel_5g")).select_by_index(10);
            elif enApTemplateType == CAPTemplateType.AP_TEMPLATE_11_157:
                Select(self.GetBrowser().find_element_by_name("wlanChannel_5g")).select_by_index(11);
                
            self.ConfigureExistSSID(szCustomerSSID + "-5G", szCustomerKey1, CFrequencePointType.FREQUENCE_POINT_5G);
            self.ConfigureNewSSID(szCustomerSSID + "Guest-5G", szCustomerKey2); 
            self.GetBrowser().find_element_by_xpath("//tr[@id='ssidtaile5G']/td[1]").click();             
            time.sleep(1);
            self.GetBrowser().find_element_by_xpath("//tr[@id='ssidtaile5G']/td[1]").click();
            time.sleep(1);  
            self.GetBrowser().find_element_by_xpath("//tr[@id='ssidtaile5G']/td[1]").click();                 
            self.GetBrowser().find_element_by_id("amend").click();
            
            self.GetBrowser().switch_to_window(allhandles[0]);
            self.GetBrowser().switch_to_default_content();
                   
            time.sleep(1)
            
    def ConfigureExistSSID(self, szSSIDName, szSSIDKey, enFrequencePointType):
        if enFrequencePointType == CFrequencePointType.FREQUENCE_POINT_2Dot4G:
            frameConfigureAPSSID = self.GetBrowser().find_element_by_xpath("//iframe[@id='wlan_ap_ssid_list_page']");
        elif enFrequencePointType == CFrequencePointType.FREQUENCE_POINT_5G:
            frameConfigureAPSSID = self.GetBrowser().find_element_by_xpath("//iframe[@id='wlan_ap_ssid_list_page_5g']");
        self.GetBrowser().switch_to_frame(frameConfigureAPSSID);            
        self.GetBrowser().find_element_by_xpath("//table[@id='disableclick']/tbody/tr[2]/td[1]").click();
        allhandles2=self.GetBrowser().window_handles;  #获取当前窗口句柄
        if self.GetBrowser().current_window_handle==allhandles2[2]:  
            pass;
        else:
            self.GetBrowser().switch_to_window(allhandles2[2]);#切换窗口
        if self.GetBrowser().find_element_by_name("ssid_en").is_selected():
            pass;
        else:
            self.GetBrowser().find_element_by_name("ssid_en").click();
        #self.GetBrowser().find_element_by_name("ssid_en").click();
        self.GetBrowser().find_element_by_name("ssid_name").clear();
        self.GetBrowser().find_element_by_name("ssid_name").send_keys(szSSIDName);
        Select(self.GetBrowser().find_element_by_name("ssid_enc")).select_by_index(1);
        self.GetBrowser().find_element_by_id("wpa_key").clear();
        self.GetBrowser().find_element_by_id("wpa_key").send_keys(szSSIDKey);
        self.GetBrowser().find_element_by_name("amend").click();
        #self.GetBrowser().find_element_by_id("op_new").click();
        #self.GetBrowser().find_element_by_partial_link_text("5G配置").click();
        
        #self.GetBrowser().switch_to.parent_frame();
        self.GetBrowser().switch_to_window(allhandles2[1]);
        self.GetBrowser().switch_to_default_content();
        time.sleep(1);
        
    def ConfigureNewSSID(self, szSSIDName, szSSIDKey):
        self.GetBrowser().find_element_by_id("op_new").click();
        allhandles2=self.GetBrowser().window_handles;  #获取当前窗口句柄
        #print(allhandles);
        if self.GetBrowser().current_window_handle==allhandles2[2]:  
            pass;
        else:
            self.GetBrowser().switch_to_window(allhandles2[2]);#切换窗口
        if self.GetBrowser().find_element_by_name("ssid_en").is_selected():
            pass;
        else:
            self.GetBrowser().find_element_by_name("ssid_en").click();
        self.GetBrowser().find_element_by_name("ssid_name").clear();
        self.GetBrowser().find_element_by_name("ssid_name").send_keys(szSSIDName);
        Select(self.GetBrowser().find_element_by_name("ssid_enc")).select_by_index(1);
        self.GetBrowser().find_element_by_id("wpa_key").clear();
        self.GetBrowser().find_element_by_id("wpa_key").send_keys(szSSIDKey);
        self.GetBrowser().find_element_by_name("amend").click();
        self.GetBrowser().switch_to_window(allhandles2[1]);
        #self.GetBrowser().find_element_by_partial_link_text("5G配置").click();                        
         