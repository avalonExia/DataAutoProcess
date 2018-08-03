#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 08:36:29 2018

@author: barbatos
"""

import os
import shutil
path = '/home/barbatos/test/original'  ###改成test路徑
new_path = '/home/barbatos/test/target'  ###改成train路徑
logs_train_path =  '/home/barbatos/test/logs/train'  ###改成train路徑
logs_val_path = '/home/barbatos/test/logs/val'  ###改成val路徑
record_filename = list()  ###用於儲存測試過的圖片檔名


###用於移動test內的相片至train
def removeimg():
    for root, dirs, files in os.walk(path):
        if len(dirs) == 0:
            for i in range(len(files)):
                if files[i][-3::1] == 'jpg':  
                    file_path = path +'/'+files[i]
                    new_file_path = new_path + '/'+ files[i]
                    shutil.move(file_path,new_file_path)
                    record_filename.append(files[i])
                    print(record_filename)

                    
###用於移動train內的相片至test
def sendimg():
    for root, dirs, files in os.walk(new_path):
        for j in range(len(files)):
            if files[j] in record_filename:  
                continue
            if files[j][-3::1] == 'jpg':
                file_path = new_path +'/'+files[j]
                new_file_path = path + '/'+ files[j]
                shutil.move(file_path,new_file_path)
                

###用於清除train與val
def rmlogs():
    for root, dirs, files in os.walk(logs_train_path):
        if len(dirs) == 0:
            for k in range(len(files)):
                logstraindata = logs_train_path + '/' + files[k]
                os.remove(logstraindata)
    for root, dirs, files in os.walk(logs_val_path):
        if len(dirs) == 0:
            for k in range(len(files)):
                logsvaldata = logs_val_path + '/' + files[k]
                os.remove(logsvaldata)
    