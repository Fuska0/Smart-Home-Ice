import sys
import Ice
from SmartHome import *
from Ice import TwowayOnlyException

def get_rgb_input(line3):
    while not line3.isdigit():
        print("Give red: ")
        line3 = input()

    nums_int = [int(line3)]
    line3 = "t"

    while not line3.isdigit():
        print("Give green: ")
        line3 = input()

    nums_int.append(int(line3))
    line3 = "t"

    while not line3.isdigit():
        print("Give blue: ")
        line3 = input()

    nums_int.append(int(line3))

    return RGB(*nums_int)

def light_worker(obj1):
    line2 = "t"
    line3 = "t"
    while line2 != "return":
        print("Options: setRGB, getRGB, turnOn, turnOff, status")
        line2 = input(">: ")
        try:
            if line2 == "setRGB":
                obj1.setRGB(get_rgb_input(line3))
            elif line2 == "getRGB":
                print(obj1.getRGB())
            elif line2 == "turnOn":
                obj1.turnOn()
            elif line2 == "turnOff":
                obj1.turnOFF()
            elif line2 == "status":
                print(obj1.getStatus())
            elif line2 == "return":
                print("")
                line2 = "return"
            else:
                print("???")
        except (IOError, TwowayOnlyException) as ex:
            print(ex)
        except DeviceIsArleadyOFF:
            print("Device you try to off is already off")
        except DeviceIsArleadyON:
            print("Device you try to off is already on")
        except DeviceIsOFF:
            print("Device you try to use is off")
        except RGBIsIncorrect:
            print("Your wrote bad RGB")
        except BrightnessIsIncorrect:
            print("Your wrote bad brightness")
        except TmperatureIsTooHigh:
            print("Your wrote bad temperature")

def led_worker(obj1):
    line2 = "t"
    line3 = "t"
    while line2 != "return":
        print("Options: setRGB, getRGB, turnOn, turnOff, status, setBrightness, getBrightness")
        line2 = input(">: ")
        try:
            if line2 == "setRGB":
                obj1.setRGB(get_rgb_input(line3))
            elif line2 == "getRGB":
                print(obj1.getRGB())
            elif line2 == "turnOn":
                obj1.turnOn()
            elif line2 == "turnOff":
                obj1.turnOFF()
            elif line2 == "status":
                print(obj1.getStatus())
            elif line2 == "setBrightness":
                line3 = input("Give number (0-10): ")
                obj1.setBrightness(int(line3))
            elif line2 == "getBrightness":
                print(obj1.getBrightness())
            elif line2 == "return":
                print("")
                line2 = "return"
            else:
                print("???")
        except (IOError, TwowayOnlyException) as ex:
            print(ex)
        except DeviceIsArleadyOFF:
            print("Device you try to off is already off")
        except DeviceIsArleadyON:
            print("Device you try to off is already on")
        except DeviceIsOFF:
            print("Device you try to use is off")
        except RGBIsIncorrect:
            print("Your wrote bad RGB")
        except BrightnessIsIncorrect:
            print("Your wrote bad brightness")
        except TmperatureIsTooHigh:
            print("Your wrote bad temperature")

def fridge_worker(obj1):
    line2 = "t"
    line3 = "t"
    while line2 != "return":
        print("Options: turnOn, turnOff, status, setTemperature, getTemperature")
        line2 = input(">: ")
        try:
            if line2 == "turnOn":
                obj1.turnOn()
            elif line2 == "turnOff":
                obj1.turnOFF()
            elif line2 == "status":
                print(obj1.getStatus())
            elif line2 == "setTemperature":
                line3 = input("Give number (-5 - 20): ")
                obj1.setTemperature(float(line3))
            elif line2 == "getTemperature":
                print("{:.2f}".format(obj1.getTemperature()))
            elif line2 == "return":
                print("")
                line2 = "return"
            else:
                print("???")
        except (IOError, TwowayOnlyException) as ex:
            print(ex)
        except DeviceIsArleadyOFF:
            print("Device you try to off is already off")
        except DeviceIsArleadyON:
            print("Device you try to off is already on")
        except DeviceIsOFF:
            print("Device you try to use is off")
        except RGBIsIncorrect:
            print("Your wrote bad RGB")
        except BrightnessIsIncorrect:
            print("Your wrote bad brightness")
        except TmperatureIsTooHigh:
            print("Your wrote bad temperature")

def two_light_worker(obj1):
    line2 = "t"
    line3 = "t"
    while line2 != "return":
        print("Options: turnOn, turnOff, status, setRGB, setFirstPointRGB, setSecondPointRGB, getFirstPointRGB, getSecondPointRGB")
        line2 = input(">: ")
        try:
            if line2 == "turnOn":
                obj1.turnOn()
            elif line2 == "turnOff":
                obj1.turnOFF()
            elif line2 == "status":
                print(obj1.getStatus())
            elif line2 == "setRGB":
                obj1.setRGB(get_rgb_input(line3))
            elif line2 == "setFirstPointRGB":
                obj1.setFirstPointRGB(get_rgb_input(line3))
            elif line2 == "setSecondPointRGB":
                obj1.setSceondPointRGB(get_rgb_input(line3))
            elif line2 == "getFirstPointRGB":
                print(obj1.getFirstPointRGB())
            elif line2 == "getSecondPointRGB":
                print(obj1.getSecondPointRGB())
            elif line2 == "return":
                print("")
                line2 = "return"
            else:
                print("???")
        except (IOError, TwowayOnlyException) as ex:
            print(ex)
        except DeviceIsArleadyOFF:
            print("Device you try to off is already off")
        except DeviceIsArleadyON:
            print("Device you try to off is already on")
        except DeviceIsOFF:
            print("Device you try to use is off")
        except RGBIsIncorrect:
            print("Your wrote bad RGB")
        except BrightnessIsIncorrect:
            print("Your wrote bad brightness")
        except TmperatureIsTooHigh:
            print("Your wrote bad temperature")

def main():
    status = 0
    communicator = None
    light_map = {}
    led_map = {}
    two_light_map = {}
    fridge_map = {}

    try:
        communicator = Ice.initialize(sys.argv)
        base6 = communicator.stringToProxy("devicesList/devicesList1:tcp -h 127.0.0.2 -p 10000 -z : udp -h 127.0.0.2 -p 10000 -z")
        obj6 = DeviceListPrx.checkedCast(base6)
        if not obj6:
            raise RuntimeError("Invalid proxy")

        for obj in obj6.getDeviceList():
            proxy = f"{obj.type}/{obj.name}:tcp -h 127.0.0.2 -p 10000 -z : udp -h 127.0.0.2 -p 10000 -z"
            base = communicator.stringToProxy(proxy)

            if obj.type == "light":
                object1 = LightPrx.checkedCast(base)
                if object1:
                    light_map[obj.name] = object1
                else:
                    raise RuntimeError("Invalid proxy")
            elif obj.type == "led":
                object2 = LedLighttPrx.checkedCast(base)
                if object2:
                    led_map[obj.name] = object2
                else:
                    raise RuntimeError("Invalid proxy")
            elif obj.type == "twoPointLight":
                object3 = TwoPointLightPrx.checkedCast(base)
                if object3:
                    two_light_map[obj.name] = object3
                else:
                    raise RuntimeError("Invalid proxy")
            elif obj.type == "fridge":
                object4 = FridgePrx.checkedCast(base)
                if object4:
                    fridge_map[obj.name] = object4
                else:
                    raise RuntimeError("Invalid proxy")
            else:
                print("unexpected device")

        line = None

        print("Write devices to check active ones")
        while line != "x":
            try:
                line = input("==> ")
                if line == "devices":
                    for obj in obj6.getDeviceList():
                        print(obj.name)
                elif line in light_map:
                    light_worker(light_map[line])
                elif line in led_map:
                    led_worker(led_map[line])
                elif line in two_light_map:
                    two_light_worker(two_light_map[line])
                elif line in fridge_map:
                    fridge_worker(fridge_map[line])
                else:
                    print("????")
            except Exception as ex:
                print(ex)

    except Ice.LocalException as e:
        print(e)
        status = 1
    except Exception as e:
        print(e)
        status = 1
    if communicator:
        try:
            communicator.destroy()
        except Exception as e:
            print(e)
            status = 1
    sys.exit(status)

if __name__ == "__main__":
    main()
