import os
import time
import multiprocessing
from os import path 
import subprocess
import logging
import logging.handlers
import datetime
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
rf_handler = logging.handlers.TimedRotatingFileHandler('install.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(rf_handler)

#检查设备
def check_adb_devices():
    '''
    检查adb 设备，并返回设备sn list
    
    :return: 设备sn list
    '''
    adb_list=[]
    ret =os.popen('adb devices').readlines()
    # print('ret={}'.format(ret))
    if len(ret) ==1:
        print('未识别到adb 设备...')
        return adb_list
    else:
        for n in ret:
            if '\tdevice\n' in n:
                adb=str(n).strip().split('\tdevice')[0].strip()
                adb_list.append(str(adb))
        return adb_list


def pull_device_0():
    cmd = "adb -s {} push '/home/ts/Documents/lianxiang_xapk_package/Subway Surfers_v2.37.0_apkpure.com.xapk' /sdcard".format(adb_list[0])
    os.system(cmd)
    time.sleep(1)
    downloadPath = '/home/ts/Documents/lianxiang_apk_package'
    file  = os.listdir(downloadPath)
    num = 0
    for f in file:
        print("num {} | {}".format(num,f))
        real_url = path.join (downloadPath , f)
        print('real_url {}'.format(real_url))
        command = 'adb -s {} install "{}"'.format(adb_list[0],real_url)
        os.system(command)
        num = num + 1


def pull_device_1():
    cmd = "adb -s {} push '/home/ts/Documents/lianxiang_xapk_package/Subway Surfers_v2.37.0_apkpure.com.xapk' /sdcard".format(adb_list[1])
    os.system(cmd)
    time.sleep(1)
    downloadPath = '/home/ts/Documents/lianxiang_apk_package'
    file  = os.listdir(downloadPath)
    for f in file:
        real_url = path.join (downloadPath , f)
        print('real_url {}'.format(real_url))
        command = 'adb -s {} install "{}"'.format(adb_list[1],real_url)
        os.system(command)


def pull_device_2():
    cmd = "adb -s {} push '/home/ts/Documents/lianxiang_xapk_package/Subway Surfers_v2.37.0_apkpure.com.xapk' /sdcard".format(adb_list[2])
    os.system(cmd)
    time.sleep(1)
    downloadPath = '/home/ts/Documents/lianxiang_apk_package'
    file  = os.listdir(downloadPath)
    for f in file:
        real_url = path.join (downloadPath , f)
        print('real_url {}'.format(real_url))
        command = 'adb -s {} install "{}"'.format(adb_list[2],real_url)
        os.system(command)

def pull_device_3():
    cmd = "adb -s {} push '/home/ts/Documents/lianxiang_xapk_package/Subway Surfers_v2.37.0_apkpure.com.xapk' /sdcard".format(adb_list[3])
    os.system(cmd)
    time.sleep(1)
    downloadPath = '/home/ts/Documents/lianxiang_apk_package'
    file  = os.listdir(downloadPath)
    for f in file:
        real_url = path.join (downloadPath , f)
        print('real_url {}'.format(real_url))
        command = 'adb -s {} install "{}"'.format(adb_list[3],real_url)
        os.system(command)



def pull_device_4():
    cmd = "adb -s {} push '/home/ts/Documents/lianxiang_xapk_package/Subway Surfers_v2.37.0_apkpure.com.xapk' /sdcard".format(adb_list[4])
    os.system(cmd)
    time.sleep(1)
    downloadPath = '/home/ts/Documents/lianxiang_apk_package'
    file  = os.listdir(downloadPath)
    for f in file:
        real_url = path.join (downloadPath , f)
        print('real_url {}'.format(real_url))
        command = 'adb -s {} install "{}"'.format(adb_list[4],real_url)
        os.system(command)
        


if __name__ == '__main__':
    adb_list = check_adb_devices()
    get_process_0 = multiprocessing.Process(target=pull_device_0)
    get_process_1 = multiprocessing.Process(target=pull_device_1)
    get_process_2 = multiprocessing.Process(target=pull_device_2)
    get_process_3 = multiprocessing.Process(target=pull_device_3)
    get_process_4 = multiprocessing.Process(target=pull_device_4)

    get_process_0.start()
    get_process_1.start()
    # get_process_2.start()
    # get_process_3.start()
    # get_process_4.start()