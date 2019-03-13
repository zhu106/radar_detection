import math
import struct
import time
import datetime
import os
import pickle
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import numpy as np


# from pointCloud import *
def readRadarData(data):
    pointCloudTimeList = []
    while len(data)>52:
        magic = b'\x02\x01\x04\x03\x06\x05\x08\x07'
        offset = data.find(magic)
        data = data[offset:]
        headerLen = 52
        try:
            syn , version , platform , timestamp , packetLength , frameNumber , subframeNumber = struct.unpack('Q6I',data[:32])
            chripMargin , frameMargin , uartSentTime , trackProccessTime , numTLv , checkSum = struct.unpack('4I2h',data[32:52])
            data = data[headerLen:]
            if numTLv>0:
                type , typeLength = struct.unpack('2I',data[:8])
                if type == 6:
                    if typeLength < 2000:
                        tlvData = data[8:typeLength]
                        pointCloud = []
                        xList = []
                        yList = []
                        for index in range(int(len(tlvData)/16)):
                            pointCloud2d = {}
                            Range , azimuth , doppler , snr = struct.unpack('4f',tlvData[index*16:index*16+16])
                            # pointCloud2d = pointCloud2D(Range , azimuth , doppler , snr)
                            pointCloud2d['range'] = Range
                            pointCloud2d['azimuth'] = azimuth
                            pointCloud2d['doppler'] = doppler
                            pointCloud2d['snr'] = snr
                            # xList.append(Range * math.sin(azimuth))
                            # yList.append(Range * math.cos(azimuth))
                            pointCloud.append(pointCloud2d)
                            # print()
                        pointCloudTimeList.append(pointCloud)



                        # plt.figure(1)
                        # plt.clf()
                        # plt.ylim((0, 10))
                        # plt.xlim((-10, 10))
                        # plt.scatter(xList, yList, marker="*")
                        # plt.draw()
                        # plt.show
                        # plt.pause(1)
                        # plt.close(1)
                        # print('len %d' % len(pointCloud))

                        data = data[typeLength:]
                    else:
                        data = data[2000:]

            # print('1')
        except:
            continue
    # print('len %d'%len(pointCloudTimeList))
    return pointCloudTimeList

if __name__ == '__main__':
    file = 'a66d44-2019-03-08'
    fileName =  file + '.radpts'
    # startTime = time.strptime(start , "%Y-%m-%d %H:%M:%S")
    # startTimeStamp = int(time.mktime(startTime))
    # endTime = time.strptime(end, "%Y-%m-%d %H:%M:%S")
    # endTimeStamp = int(time.mktime(endTime))
    # rawDataFile = open(fileName, "rb")
    # fsize = os.path.getsize(fileName)
    result = {}
    with open(fileName, 'rb') as rawDataFile:
        while True:
            rawData = rawDataFile.read(1000000)
            if rawData:
                lenrawdata = len(rawData)
                pointCloud = []
                magic = 'RadRaw'.encode('ascii')
                while len(rawData) > 20:
                    offset = rawData.find(magic)
                    rawData = rawData[offset:]

                    Magic, mac, time2, length = struct.unpack('>6s6s2I', rawData[:20])
                    time1 = datetime.datetime.fromtimestamp(time2)
                    print(time1)
                    timelen = rawData[16:20]
                    test = struct.unpack('>I', timelen)
                    data = rawData[20:length]
                    pointList = []
                    pointCloud = readRadarData(data)
                    if result.get(time2) == None:
                        pointList.append(pointCloud)
                        result[time2] = pointList
                    else:
                        pointList = pointList + result.get(time2)
                        pointList.append(pointCloud)
                        result[time2] = pointList

                    rawData = rawData[length:]

                sorted(result.keys())
                # resultList = {}
                # for i in range(startTimeStamp,endTimeStamp):
                #     Result = result.get(i)
                #              #     if Result != None:
                #         resultList[i] = Result
                # jsonFileName = file + '.txt'
                # f = open(jsonFileName, "r")
                # a = json.dumps(result)
                # b = json.loads(a)
                # with open(jsonFileName, 'a') as outfile:
                #     json.dumps(result, outfile, ensure_ascii=False)
                #     outfile.write('\\n')


                # print(resultList)

                # for i in resultList:
                #     a = 1

                # plt.figure(1)
                # plt.clf()
                # plt.ylim((0, 10))
                # plt.xlim((-10, 10))
                # plt.scatter(xList, yList, marker="*")
                # plt.draw()
                # plt.show
                # plt.pause(1)
                # plt.close(1)
            else:
                break

    # index=0
    # f = open(jsonFileName, 'wb')
    # pickle.dump(result, f)
    # f.close()
    #
    # start1 = "2019-03-06 00:27:00"
    # end1 = "2019-03-06 12:50:00"
    # # interval = 20
    # # fileName = file + '.txt'
    # startTime = time.strptime(start1, "%Y-%m-%d %H:%M:%S")
    # startTimeStamp = int(time.mktime(startTime))
    # endTime = time.strptime(end1, "%Y-%m-%d %H:%M:%S")
    # endTimeStamp = int(time.mktime(endTime))
    #
    #
    # sorted(result.keys())
    # for SecondFrame in range(startTimeStamp,endTimeStamp):
    #     endTime = time.strptime(end1, "%Y-%m-%d %H:%M:%S")
    #     endTimeStamp = int(time.mktime(endTime))
    #     # time1 = datetime.datetime.fromtimestamp(SecondFrame)
    #     print(datetime.datetime.fromtimestamp(SecondFrame))
    #     Result = result.get(SecondFrame)
    #     if Result != None:
    #
    #         for frame in Result:
    #             if len(frame) != 0:
    #                 xList = []
    #                 yList = []
    #                 snrList = []
    #                 for pointCloud in frame:
    #                     index =index + 1
    #                     print(index)
    #                     if index % interval == 0:
    #
    #                         for point in pointCloud:
    #                             xList.append(point['range']*math.sin(point['azimuth']))
    #                             yList.append(point['range'] * math.cos(point['azimuth']))
    #                             snrList.append(point['snr'])
    #
    #
    #                 if  len(xList) != 0:
    #                     #######散点图
    #                     # plt.figure(1)
    #                     # plt.clf()
    #                     # plt.ylim((0, 10))
    #                     # plt.xlim((-10, 10))
    #                     # plt.scatter(xList, yList, marker="*")
    #                     # time1 = datetime.datetime.fromtimestamp(SecondFrame)
    #                     # plt.title(time1)
    #                     # sorted(snrList)
    #                     # # for i in range(len(snrList)):
    #                     # #
    #                     # #     plt.text(xList[i],yList[i],'%f'%snrList[i],ha='center', va= 'bottom',fontsize=7)
    #                     # plt.show
    #                     # plt.pause(0.1)
    #                     # plt.close(1)
    #
    #
    #
    #                     #####三维散点图
    #                     # plt.figure(1)
    #                     fig = plt.figure()
    #                     # ax = plt.subplot()
    #                     time1 = datetime.datetime.fromtimestamp(SecondFrame)
    #                     plt.title(time1)
    #                     plt.ylim((0, 10))
    #                     plt.xlim((-10, 10))
    #                     for i in range(len(snrList)):
    #                         plt.scatter(xList[i], yList[i], s = snrList[i])  # 绘制散点图
    #
    #                     plt.draw()
    #
    #                     plt.pause(0.1)
    #                     plt.close(1)
    #
    #
    fig = plt.figure()
    plt.ion()
    meanx = 0
    meany = 0
    count = 0
    for package in result:
        if len(result[package]) != 0:    
            for frames in result[package]:   # one frame include several points
                # for pointCloud, calculate position x and y, and then cluster into one class.
                xyList = []
                # yList = []
                snrList = []
                for frame in frames:
                    if frame != []:
                        for point in frame:
                            xyList.append([point['range'] * math.sin(point['azimuth']), point['range'] * math.cos(point['azimuth'])])
                            snrList.append(point['snr'])
                        # cluster
                        xyArray = np.array(xyList)
                        snrArray = np.array(snrList)
                        where_are_nan = np.isnan(xyArray)
                        where_are_inf = np.isinf(xyArray)
                        xyArray[where_are_nan] = 0
                        xyArray[where_are_inf] = 0
                        clustering = DBSCAN(eps = 0.8, min_samples = 4).fit(xyArray)
                        labels = clustering.labels_
                        n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
                        Intensity_Sum = []
                        if n_clusters > 1:
                            Intensity_Sum = [ np.mean(snrArray[labels == i]) for i in range(n_clusters)]
                            label = np.argmax(Intensity_Sum)
                            meanx = np.mean(xyArray[labels == label, 0])
                            meany = np.mean(xyArray[labels == label, 1])
                        elif n_clusters == 1:
                            meanx = np.mean(xyArray[labels == 0, 0])
                            meany = np.mean(xyArray[labels == 0, 1])
                    else:
                        n_clusters = 0
                    print(count)
                    count = count + 1
                    plt.scatter(meanx, meany)
                    plt.title(str(n_clusters) )
                    plt.xlabel(datetime.datetime.fromtimestamp(package))
                    plt.show()
                    plt.pause(0.000005)












