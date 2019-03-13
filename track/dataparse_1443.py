import math
import struct
import time
import datetime
import os

def readRadarData(data):
    PointCloudTimeList = []
    while len(data) > 40:
        magic = b'\x02\x01\x04\x03\x06\x05\x08\x07'
        offset = data.find(magic)
        # print('len %d'%len(data))
        # print(data[offset:40])
        syn, version, totalPacketLen, platform, frameNumber, timeCpuCycles, numDetectedObj = struct.unpack('Q6I', data[:32])
        numTLVs, subFrameNumber = struct.unpack('2I', data[32:40])
        # print(version)
        data = data[40:]
        try:
            if numTLVs > 0:
                type , typeLength = struct.unpack('2I',data[:8])
                # print(type, typeLength)
                if type == 6:
                        if typeLength < 2000:
                            tlvData = data[8:typeLength]
                            pointCloud = []
                            xList = []
                            yList = []
                            for index in range(int(len(tlvData)/12)):
                                pointCloud3d = {}
                                rangeIdx, dopplerIdx, peakVal, x, y, z = struct.unpack('HhH3h',tlvData[index*16:index*16+16])
                                pointCloud3d['rangeIdx'] = rangeIdx
                                pointCloud3d['dopplerIdx'] = dopplerIdx
                                pointCloud3d['peakVal'] = peakVal
                                pointCloud3d['x'] = x
                                pointCloud3d['y'] = y
                                pointCloud3d['z'] = z
                                pointCloud.append(pointCloud3d)                        
                            PointCloudTimeList.append(pointCloud)
                            data = data[typeLength:]
                        else:
                            data = data[2000:]
        except:
            continue
    return PointCloudTimeList


if __name__ == '__main__':
    fileName = 'a6650f-2019-03-08.radpts'
    result = {}
    with open(fileName, 'rb') as rawDataFile:
        while True:
            rawData = rawDataFile.read(1000000)
            if rawData:
                len_rawData = len(rawData)
                pointCloud = []
                magic = 'RadRaw'.encode('ascii')

                while len(rawData) > 20:
                    # record header
                    offset = rawData.find(magic)
                    # print(rawData[:20])
                    rawData = rawData[offset:]
                    Magic, mac, time2, length = struct.unpack('>6s6s2I', rawData[:20])
                    time1 = datetime.datetime.fromtimestamp(time2)
                    # len_record = rawData[16:20]
                    print(time1)
                    data = rawData[20:length] #raw data
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
            else:
                break
    sorted(result.keys())
                


