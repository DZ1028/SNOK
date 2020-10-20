# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''
from CDeviceType import CDeviceType
from CDevice import CDevice
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
from pip._internal import self_outdated_check
from const import Const

const = Const();
const.NAME_ACCOUNT = "account";
const.NAME_PASSWORD = "password";
const.NAME_SUBMIT = "btnSubmit";

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
        self.GetBrowser().find_element_by_name(const.NAME_ACCOUNT).send_keys(self.GetUsername());
        self.GetBrowser().find_element_by_name(const.NAME_PASSWORD).send_keys(self.GetPassword());
        
    def LoginSubmit(self):
        self.GetBrowser().find_element_by_name(const.NAME_SUBMIT).send_keys(Keys.ENTER);        
        