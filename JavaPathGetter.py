import os
def JavaPathGetter():  # 获取JAVA
    cmd = r'''reg query "HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Session Manager\Environment" /v Path'''  # 访问注册表下的path环境变量
    cmd1 = os.popen(cmd)
    cmd_return = cmd1.read()  # 到这一步获得环境变量
    cmd_step1 = cmd_return[106:len(cmd_return)]  # 去除前面没用的信息
    cmd_step2 = cmd_step1.split(";")  # 将一整窜的环境变量分段，变成一个列表
    JavaPath_Object = open(os.getcwd() + "\data\JavaPath.txt", "r+")  # 打开在data文件夹下的JavaPath文件夹，设置为读写模式
    if JavaPath_Object.read() == '':
        for r in range(len(cmd_step2)):
            path_try = cmd_step2[r]

            if os.path.exists(path_try + "/java.exe"):
                JavaPath_Object.write("%s\n" % path_try)
            JavaPath_Object.flush()

    JavaPath_Object.close()