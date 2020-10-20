# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''

from CDevice_H3C_ER3200G2 import CDevice_H3C_ER3200G2
from CDeviceType import CDeviceVersion

if __name__ == "__main__":
    device = CDevice_H3C_ER3200G2(CDeviceVersion.H3C_ERHMG2_MNW100_R1118);
    device.LoginPrepare('http://172.16.1.1/', 'admin', 'admin@123@');
    device.LoginInputUsernamePassword();
    device.LoginSubmit();
    print(device.GetUsername(), device.GetPassword());
    