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
const.ROUTER_MANAGERMENT_URL = "http://192.168.1.1/";#"http://172.16.1.1/";
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
        #self.m_oButton = Button(self.GetMainWindow(), text='test button', bg="lightblue", width=10, command=self.FnCmd_MoveIt);
        #self.m_oCanvas = Canvas(self.GetMainWindow(), bg='green', height=200, width=500);
        #self.m_oImageFile = PhotoImage(file=szFileURL);
        
        ###############################################
        self.m_oLabelAccessMode = Label(self.GetMainWindow(), text='接入方式', bg='white', font=('Arial', 12), width=30, height=2);
        self.m_oRadioPPPoEMode = Radiobutton(self.GetMainWindow(), text='PPPoE', variable=self.GetVarRadioAccessMode(), value='PPPoE', command=self.FnCmd_SelectRadio);
        self.m_oEntryPPPoEAccount = Entry(self.GetMainWindow(), show=None, font=('Arial', 14));
        self.m_oLabelPPPoEAccount = Label(self.GetMainWindow(), text='PPPoE账号', bg='white', font=('Arial', 12), width=30, height=2);
        self.m_oEntryPPPoEPassword = Entry(self.GetMainWindow(), show='*', font=('Arial', 14));
        self.m_oLabelPPPoEPassword = Label(self.GetMainWindow(), text='PPPoE密码', bg='white', font=('Arial', 12), width=30, height=2);
        self.m_oConfirmButton = Button(self.GetMainWindow(), text='确定', bg="lightblue", width=10, command=self.FnCmd_Confirm);
        self.m_oCancelButton = Button(self.GetMainWindow(), text='取消', bg="lightblue", width=10, command=self.FnCmd_Cancel);
        
    def GetMainWindow(self):
        return self.m_oWindowMain;
    
    def GetRadioPPPoEMode(self):
        return self.m_oRadioPPPoEMode;
    
    def GetVarRadioAccessMode(self):
        return self.m_varRadioAccessMode;
    
    def SetVarRadioAccessMode(self, varAccessMode):
        self.m_varRadioAccessMode = varAccessMode;
    
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
    
    def GetLabelPPPoEAccount(self):
        return self.m_oLabelPPPoEAccount;
    
    def GetLabelPPPoEPassword(self):
        return self.m_oLabelPPPoEPassword;
    
    def GetButtonConfirm(self):
        return self.m_oConfirmButton;
    
    def GetButtonCancel(self):
        return self.m_oCancelButton;
    
    def GetDevice(self):
        return self.m_oDevice;
    
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
        self.GetDevice().InitConnectToInternet_PPPoE(self.GetEntryPPPoEAccount().get(), self.GetEntryPPPoEPassword().get());
        self.GetDevice().ConnectToInternet_PPPoE();
        
    def FnCmd_Cancel(self):
        self.GetMainWindow().destroy();
        
    def FnCmd_SelectRadio(self):
        a=1;
        
    def TotalPack(self):
        self.GetLabelAccessMode().pack();
        self.GetRadioPPPoEMode().pack();
        self.GetLabelPPPoEAccount().pack();
        self.GetEntryPPPoEAccount().pack();
        self.GetLabelPPPoEPassword().pack();
        self.GetEntryPPPoEPassword().pack();
        self.GetButtonConfirm().pack();
        self.GetButtonCancel().pack();
        
    

# 第1步，实例化object，建立窗口window
#window = tk.Tk()
 
# 第2步，给窗口的可视化起名字
#window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
#window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
#canvas = tk.Canvas(window, bg='green', height=200, width=500)
# 说明图片位置，并导入图片到画布上
#image_file = tk.PhotoImage(file='pic.gif')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
#image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
# 定义多边形参数，然后在画布上画出指定图形
#x0, y0, x1, y1 = 100, 100, 150, 150
#line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
#oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 画圆 用黄色填充
#arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
#rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形
#canvas.pack()
 
# 第6步，触发函数，用来一定指定图形
#def moveit():
#    canvas.move(rect, 2, 2) # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动
 
# 第5步，定义一个按钮用来移动指定图形的在画布上的位置
#sb = tk.Button(window, text='move item',command=moveit).pack()
 
# 第7步，主窗口循环显示
#window.mainloop()
#menu = CMenu();
#menu.InitMainWindow('test window', '500x300');

#menu.InitButton('MOVE RECT', CMenu.FnCmd_MoveIt);
#menu.ButtonPack();
#menu.MainWindowLoop();