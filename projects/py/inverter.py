from pyscript import display, HTML # type: ignore
import requests
import json

BATTERY_CAPACITY_A = 400

# Requesting data
url = "https://web.dessmonitor.com/public/?sign=0707ee1385d0c8cc7759d136d85146dba9c89c56&salt=1778680104653&token=CNd389eedb-7a64-4288-a1ed-730fb91717b8&action=querySPDeviceLastData&source=1&devcode=6467&pn=F60000220775955158&devaddr=1&sn=F60000220775955158194301&i18n=en_US"
r = requests.get(url)

# Loading Data
data = json.loads(r.text)
gridVoltage = float(data["dat"]["pars"]["gd_"][1]["val"])
gridFrequency = float(data["dat"]["pars"]["gd_"][2]["val"])

solarPower = float(data["dat"]["pars"]["pv_"][4]["val"])

batteryVoltage = float(data["dat"]["pars"]["bt_"][0]["val"])
batteryCapacity = float(data["dat"]["pars"]["bt_"][1]["val"])

loadPower = float(data["dat"]["pars"]["bc_"][0]["val"])
loadPercentage = float(data["dat"]["pars"]["bc_"][1]["val"])
loadCurrent = (loadPower*1000)/230

try:
    remainingTime = (batteryVoltage * BATTERY_CAPACITY_A * batteryCapacity)/(loadPower)
except:
    remainingTime = 0

try:
    solarToLoadPercentage = (solarPower/loadPower)*100
except:
    solarToLoadPercentage = 0

#Display Data
display(HTML("<h2>Grid:</h2>"))
display(f"Grid Voltage: {gridVoltage}V")
display(f"Grid Frequency: {gridFrequency}Hz")
display(HTML("<h2>Solar:</h2>"))
display(f"Solar Power Output: {solarPower}W")
display(HTML("<h2>Battery:</h2>"))
display(f"Battery Voltage: {batteryVoltage}V")
display(f"Battery Capacity: {batteryCapacity}%")
display(f"Battery Runtime (only at night): {remainingTime}h")
display(HTML("<h2>Load:</h2>"))
display(f"Output Load Percentage: {loadPercentage}%")
display(f"Output Load Power: {loadPower}kVA")
display(f"Output Load Current: {loadCurrent}A")
display(f"% Solar to Load: {solarToLoadPercentage}%")