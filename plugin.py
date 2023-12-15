#!/usr/bin/env python
"""
Eastron SDM630-Modbus 100A 3P4W SW:1.3 Smart Meter Three Phase Electrical System. The Python plugin for Domoticz
Author: MFxMF and bbossink and remcovanvugt and GizMoCuz
Requirements: 
    1.Communication module Modbus USB to RS485 converter module
"""
"""
<plugin key="SDM630" name="Eastron SDM630-Modbus" version="2" author="nmakel/MFxMF/gizmocuz">
    <params>
        <param field="SerialPort" label="Modbus Port" width="200px" required="true" default="/dev/ttyUSB0" />
        <param field="Mode1" label="Baud rate" width="40px" required="true" default="9600"  />
        <param field="Mode2" label="Modbus ID" width="60px" required="true" default="1" />
        <param field="Mode3" label="Poll Interval sec." width="60px" required="true" default="30" />
        <param field="Mode4" label="Meter Type" width="80px">
            <options>
                <option label="SDM 72" value="1"/>
                <option label="SDM 72v2" value="2"/>
                <option label="SDM 120" value="3"/>
                <option label="SDM 230" value="4"/>
                <option label="SDM 630" value="5"/>
            </options>
        </param>
        <param field="Mode6" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal" default="true" />
            </options>
        </param>
    </params>
</plugin>

"""

import minimalmodbus
import Domoticz         #tested on Python 3.11.6 in Domoticz 2023.2 and latest beta's
from sdm import *


class BasePlugin:
    def __init__(self):
        self.pollinterval = 30
        self.runInterval = 1
        self.rs485 = "" 
        return

    def onStart(self):
        
        devicecreated = []
        self.pollinterval = int(Parameters["Mode3"]) * 1 
        if self.pollinterval < 30:
            self.pollinterval = 30

        modbusIDs = Parameters["Mode2"].split(',');
        
        self.metertype = int(Parameters["Mode4"])
        if (self.metertype == 1):
            self.meter = SDM72();
        elif (self.metertype == 2):
            self.meter = SDM72V2();
        elif (self.metertype == 3):
            self.meter = SDM120();
        elif (self.metertype == 4):
            self.meter = SDM230();
        elif (self.metertype == 5):
            self.meter = SDM630();

        Domoticz.Log("Eastron Modbus plugin started. Type=" + self.meter.model)

        # create devices
        doffset = 1
        
        for k, v in self.meter.registers.items():
            address, length, label, fmt, batch, sf, child = v

            if doffset not in Devices:
                if (fmt == "V"):
                    Domoticz.Device(Name=label, Unit=doffset,TypeName=fmt,Used=0).Create()
                elif (fmt == "A"):
                    Domoticz.Device(Name=label, Unit=doffset,TypeName="Current (Single)",Used=0).Create()
                elif (fmt == "W"):
                    Domoticz.Device(Name=label, Unit=doffset,TypeName="Usage",Used=0).Create()
                elif (fmt == "kWh"):
                    Domoticz.Device(Name=label, Unit=doffset,TypeName="General",Subtype=0x1D,Used=0).Create()
                else:
                    #custom device
                    #Domoticz.Log("** UNKNOWN format! *** (" + fmt + ")")
                    Options = { "Custom" : "1;" + fmt} 
                    Domoticz.Device(Name=label, Unit=doffset,TypeName="Custom",Used=0,Options=Options).Create()

            doffset+=1

        Domoticz.Heartbeat(5)

    def onStop(self):
        Domoticz.Log("plugin stopped")

    def onHeartbeat(self):
        self.runInterval -=5;
        if self.runInterval <= 0:
            self.runInterval = self.pollinterval
            
            modbusIDs = Parameters["Mode2"].split(',');
            for mbid in modbusIDs:
                try:
                    imbid = int(mbid)
                    #doffset = int(mbid) * 100

                    self.rs485 = minimalmodbus.Instrument(Parameters["SerialPort"], imbid)
                    self.rs485.serial.baudrate = self.meter.baud
                    self.rs485.serial.bytesize = 8
                    self.rs485.serial.parity = minimalmodbus.serial.PARITY_NONE
                    self.rs485.serial.stopbits = 1
                    self.rs485.serial.timeout = 1
                    self.rs485.serial.exclusive = True
                    self.rs485.debug = False
                            
                    self.rs485.mode = minimalmodbus.MODE_RTU
                    self.rs485.close_port_after_each_call = True
                    
                    doffset = 1
                    values = {}
                    for k, v in self.meter.registers.items():
                        name = k;
                        
                        address, length, label, fmt, batch, sf, child = v
                        
                        mvalue  = self.rs485.read_float(address, 4, length)
                        
                        values[k] = mvalue
                        
                        vvalue = ""
                        if (fmt == "kWh"):
                            mvalue*=1000
                            ausage = "{:.1f}".format(values[child])
                            vvalue = "{:.3f}".format(mvalue)
                            Devices[doffset].Update(0,ausage + ";" + vvalue)
                        else:
                            if (fmt == "W"):
                                vvalue = "{:.1f}".format(mvalue)
                            else:
                                vvalue = "{:.2f}".format(mvalue)
                            Devices[doffset].Update(0,vvalue)
                            
                        if Parameters["Mode6"] == 'Debug':
                            Domoticz.Log(label + ": " + vvalue + " " + fmt);
                        
                        doffset+=1

                    self.rs485.serial.close()  #  Close that door !
                except Exception as error:
                    self.rs485.serial.close()  #  Close that door !
                    #Domoticz.Log('**** Connection problem with modbus id: {0:2d} ****'.format(imbid));
                    Domoticz.Log("An exception occurred: " + str(error) + ", line: " + str(error.__traceback__.tb_lineno))

global _plugin
_plugin = BasePlugin()


def onStart():
    global _plugin
    _plugin.onStart()


def onStop():
    global _plugin
    _plugin.onStop()


def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

# Generic helper functions
def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug("'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device nValue:    " + str(Devices[x].nValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return
