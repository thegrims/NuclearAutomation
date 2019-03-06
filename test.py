#=====================================================================
#Initialization Start
#The script within Initialization Start and Initialization End
#is needed for properly initializing Command
#Interface for ESP301 instrument.
#The user should copy this code as is and specify correct paths here.
import sys
#Command Interface DLL can be found here.
print("Adding location of Newport.ESP301.CommandInterface.dll to sys.path")
sys.path.append(r'C:\Newport\Motion Control\ESP301\Bin')
# The CLR module provide functions for interacting with the underlying
# .NET runtime
import clr
# Add reference to assembly and import names from namespace 
# ToFile
clr.FindAssembly(r"Newport.ESP301.CommandInterface.dll")
clr.AddReference(r"Newport.ESP301.CommandInterface.dll")

from CommandInterface import *
import System
#=====================================================================
# Instrument Initialization
# The key should have double slashes since
# (one of them is escape character)
instrument="COM15"
BAUDRATE = 921600
print('Instrument Key=>', instrument)
# create an ESP301 instance
ESP301Device = ESP301()

# Open communication
ret = esp301.OpenInstrument(instrument, BAUDRATE)
# Get positive software limit
result, response, errString = ESP301Device.SR_Get(1)
if result == 0 :
    print('positive software limit=>', response)
else:
    print('Error=>',errString)

#Get negative software limit
result, response, errString = ESP301Device.SL_Get(1)
if result == 0 :
    print('negative software limit=>', response)
else:
    print('Error=>',errString)

# Get controller revision information
result, response, errString = ESP301Device.VE()
# if result == 0 : 
