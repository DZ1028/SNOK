# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''

from CDeviceType import CDeviceType
from CDeviceType import CDeviceVersion
from selenium import webdriver
from pip._internal import self_outdated_check

class CDevice:
    '''
    Function: Father Class Of All Devices
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        self.m_DeviceType = CDeviceType.OtherFactory_OtherType;   #property: DeviceType
        self.m_DeviceVersion = CDeviceVersion.OtherFactory_OtherHardware_OtherSoftwareVersion;#property: Device Version
        self.m_Browser = webdriver.Chrome();                      #property: Web Browser
        self.m_szUsername = "";                                   #property: User name
        self.m_szPassword = "";
        self.m_szURL = "";                                        #property: Password
        
    def GetDeviceType(self):                                      #method: get DeviceType
        return self.m_DeviceType;
    
    def SetDeviceType(self, enDeviceType):
        self.m_DeviceType = enDeviceType;
        
    def GetDeviceVersion(self):
        return self.m_DeviceVersion;
    
    def SetDeviceVersion(self, enDeviceVersion):
        self.m_DeviceVersion = enDeviceVersion;
    
    def GetUsername(self):
        return self.m_szUsername;
    
    def SetUsername(self, szUsername):
        self.m_szUsername = szUsername;
        
    def GetPassword(self):
        return self.m_szPassword;
    
    def SetPassword(self, szPassword):
        self.m_szPassword = szPassword;
        
    def GetURL(self):
        return self.m_szURL;
    
    def SetURL(self, szURL):
        self.m_szURL = szURL;
    
    def GetBrowser(self):
        return self.m_Browser;
    
    def LoginPrepare(self, szURL, szUsername, szPassword):
        self.SetURL(szURL);
        self.SetUsername(szUsername);
        self.SetPassword(szPassword);
        self.GetBrowser().get(self.GetURL());
    