# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `smarthouse.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module SmartHome
_M_SmartHome = Ice.openModule('SmartHome')
__name__ = 'SmartHome'

if 'Status' not in _M_SmartHome.__dict__:
    _M_SmartHome.Status = Ice.createTempClass()
    class Status(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Status.On = Status("On", 0)
    Status.Off = Status("Off", 1)
    Status._enumerators = { 0:Status.On, 1:Status.Off }

    _M_SmartHome._t_Status = IcePy.defineEnum('::SmartHome::Status', Status, (), Status._enumerators)

    _M_SmartHome.Status = Status
    del Status

if 'RGB' not in _M_SmartHome.__dict__:
    _M_SmartHome.RGB = Ice.createTempClass()
    class RGB(object):
        def __init__(self, r=0, g=0, bl=0):
            self.r = r
            self.g = g
            self.bl = bl

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.r)
            _h = 5 * _h + Ice.getHash(self.g)
            _h = 5 * _h + Ice.getHash(self.bl)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_SmartHome.RGB):
                return NotImplemented
            else:
                if self.r is None or other.r is None:
                    if self.r != other.r:
                        return (-1 if self.r is None else 1)
                else:
                    if self.r < other.r:
                        return -1
                    elif self.r > other.r:
                        return 1
                if self.g is None or other.g is None:
                    if self.g != other.g:
                        return (-1 if self.g is None else 1)
                else:
                    if self.g < other.g:
                        return -1
                    elif self.g > other.g:
                        return 1
                if self.bl is None or other.bl is None:
                    if self.bl != other.bl:
                        return (-1 if self.bl is None else 1)
                else:
                    if self.bl < other.bl:
                        return -1
                    elif self.bl > other.bl:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_RGB)

        __repr__ = __str__

    _M_SmartHome._t_RGB = IcePy.defineStruct('::SmartHome::RGB', RGB, (), (
        ('r', (), IcePy._t_int),
        ('g', (), IcePy._t_int),
        ('bl', (), IcePy._t_int)
    ))

    _M_SmartHome.RGB = RGB
    del RGB

if 'DeviceIsArleadyON' not in _M_SmartHome.__dict__:
    _M_SmartHome.DeviceIsArleadyON = Ice.createTempClass()
    class DeviceIsArleadyON(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::SmartHome::DeviceIsArleadyON'

    _M_SmartHome._t_DeviceIsArleadyON = IcePy.defineException('::SmartHome::DeviceIsArleadyON', DeviceIsArleadyON, (), False, None, ())
    DeviceIsArleadyON._ice_type = _M_SmartHome._t_DeviceIsArleadyON

    _M_SmartHome.DeviceIsArleadyON = DeviceIsArleadyON
    del DeviceIsArleadyON

if 'DeviceIsArleadyOFF' not in _M_SmartHome.__dict__:
    _M_SmartHome.DeviceIsArleadyOFF = Ice.createTempClass()
    class DeviceIsArleadyOFF(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::SmartHome::DeviceIsArleadyOFF'

    _M_SmartHome._t_DeviceIsArleadyOFF = IcePy.defineException('::SmartHome::DeviceIsArleadyOFF', DeviceIsArleadyOFF, (), False, None, ())
    DeviceIsArleadyOFF._ice_type = _M_SmartHome._t_DeviceIsArleadyOFF

    _M_SmartHome.DeviceIsArleadyOFF = DeviceIsArleadyOFF
    del DeviceIsArleadyOFF

if 'DeviceIsOFF' not in _M_SmartHome.__dict__:
    _M_SmartHome.DeviceIsOFF = Ice.createTempClass()
    class DeviceIsOFF(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::SmartHome::DeviceIsOFF'

    _M_SmartHome._t_DeviceIsOFF = IcePy.defineException('::SmartHome::DeviceIsOFF', DeviceIsOFF, (), False, None, ())
    DeviceIsOFF._ice_type = _M_SmartHome._t_DeviceIsOFF

    _M_SmartHome.DeviceIsOFF = DeviceIsOFF
    del DeviceIsOFF

_M_SmartHome._t_Device = IcePy.defineValue('::SmartHome::Device', Ice.Value, -1, (), False, True, None, ())

if 'DevicePrx' not in _M_SmartHome.__dict__:
    _M_SmartHome.DevicePrx = Ice.createTempClass()
    class DevicePrx(Ice.ObjectPrx):

        def turnOn(self, context=None):
            return _M_SmartHome.Device._op_turnOn.invoke(self, ((), context))

        def turnOnAsync(self, context=None):
            return _M_SmartHome.Device._op_turnOn.invokeAsync(self, ((), context))

        def begin_turnOn(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.Device._op_turnOn.begin(self, ((), _response, _ex, _sent, context))

        def end_turnOn(self, _r):
            return _M_SmartHome.Device._op_turnOn.end(self, _r)

        def turnOFF(self, context=None):
            return _M_SmartHome.Device._op_turnOFF.invoke(self, ((), context))

        def turnOFFAsync(self, context=None):
            return _M_SmartHome.Device._op_turnOFF.invokeAsync(self, ((), context))

        def begin_turnOFF(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.Device._op_turnOFF.begin(self, ((), _response, _ex, _sent, context))

        def end_turnOFF(self, _r):
            return _M_SmartHome.Device._op_turnOFF.end(self, _r)

        def getStatus(self, context=None):
            return _M_SmartHome.Device._op_getStatus.invoke(self, ((), context))

        def getStatusAsync(self, context=None):
            return _M_SmartHome.Device._op_getStatus.invokeAsync(self, ((), context))

        def begin_getStatus(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.Device._op_getStatus.begin(self, ((), _response, _ex, _sent, context))

        def end_getStatus(self, _r):
            return _M_SmartHome.Device._op_getStatus.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_SmartHome.DevicePrx.ice_checkedCast(proxy, '::SmartHome::Device', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_SmartHome.DevicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::SmartHome::Device'
    _M_SmartHome._t_DevicePrx = IcePy.defineProxy('::SmartHome::Device', DevicePrx)

    _M_SmartHome.DevicePrx = DevicePrx
    del DevicePrx

    _M_SmartHome.Device = Ice.createTempClass()
    class Device(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SmartHome::Device')

        def ice_id(self, current=None):
            return '::SmartHome::Device'

        @staticmethod
        def ice_staticId():
            return '::SmartHome::Device'

        def turnOn(self, current=None):
            raise NotImplementedError("servant method 'turnOn' not implemented")

        def turnOFF(self, current=None):
            raise NotImplementedError("servant method 'turnOFF' not implemented")

        def getStatus(self, current=None):
            raise NotImplementedError("servant method 'getStatus' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_DeviceDisp)

        __repr__ = __str__

    _M_SmartHome._t_DeviceDisp = IcePy.defineClass('::SmartHome::Device', Device, (), None, ())
    Device._ice_type = _M_SmartHome._t_DeviceDisp

    Device._op_turnOn = IcePy.Operation('turnOn', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), None, (_M_SmartHome._t_DeviceIsArleadyON,))
    Device._op_turnOFF = IcePy.Operation('turnOFF', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), None, (_M_SmartHome._t_DeviceIsArleadyOFF,))
    Device._op_getStatus = IcePy.Operation('getStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_SmartHome._t_Status, False, 0), (_M_SmartHome._t_DeviceIsOFF,))

    _M_SmartHome.Device = Device
    del Device

if 'TmperatureIsTooHigh' not in _M_SmartHome.__dict__:
    _M_SmartHome.TmperatureIsTooHigh = Ice.createTempClass()
    class TmperatureIsTooHigh(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::SmartHome::TmperatureIsTooHigh'

    _M_SmartHome._t_TmperatureIsTooHigh = IcePy.defineException('::SmartHome::TmperatureIsTooHigh', TmperatureIsTooHigh, (), False, None, ())
    TmperatureIsTooHigh._ice_type = _M_SmartHome._t_TmperatureIsTooHigh

    _M_SmartHome.TmperatureIsTooHigh = TmperatureIsTooHigh
    del TmperatureIsTooHigh

_M_SmartHome._t_Fridge = IcePy.defineValue('::SmartHome::Fridge', Ice.Value, -1, (), False, True, None, ())

if 'FridgePrx' not in _M_SmartHome.__dict__:
    _M_SmartHome.FridgePrx = Ice.createTempClass()
    class FridgePrx(_M_SmartHome.DevicePrx):

        def setTemperature(self, temperature, context=None):
            return _M_SmartHome.Fridge._op_setTemperature.invoke(self, ((temperature, ), context))

        def setTemperatureAsync(self, temperature, context=None):
            return _M_SmartHome.Fridge._op_setTemperature.invokeAsync(self, ((temperature, ), context))

        def begin_setTemperature(self, temperature, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.Fridge._op_setTemperature.begin(self, ((temperature, ), _response, _ex, _sent, context))

        def end_setTemperature(self, _r):
            return _M_SmartHome.Fridge._op_setTemperature.end(self, _r)

        def getTemperature(self, context=None):
            return _M_SmartHome.Fridge._op_getTemperature.invoke(self, ((), context))

        def getTemperatureAsync(self, context=None):
            return _M_SmartHome.Fridge._op_getTemperature.invokeAsync(self, ((), context))

        def begin_getTemperature(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.Fridge._op_getTemperature.begin(self, ((), _response, _ex, _sent, context))

        def end_getTemperature(self, _r):
            return _M_SmartHome.Fridge._op_getTemperature.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_SmartHome.FridgePrx.ice_checkedCast(proxy, '::SmartHome::Fridge', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_SmartHome.FridgePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::SmartHome::Fridge'
    _M_SmartHome._t_FridgePrx = IcePy.defineProxy('::SmartHome::Fridge', FridgePrx)

    _M_SmartHome.FridgePrx = FridgePrx
    del FridgePrx

    _M_SmartHome.Fridge = Ice.createTempClass()
    class Fridge(_M_SmartHome.Device):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SmartHome::Device', '::SmartHome::Fridge')

        def ice_id(self, current=None):
            return '::SmartHome::Fridge'

        @staticmethod
        def ice_staticId():
            return '::SmartHome::Fridge'

        def setTemperature(self, temperature, current=None):
            raise NotImplementedError("servant method 'setTemperature' not implemented")

        def getTemperature(self, current=None):
            raise NotImplementedError("servant method 'getTemperature' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_FridgeDisp)

        __repr__ = __str__

    _M_SmartHome._t_FridgeDisp = IcePy.defineClass('::SmartHome::Fridge', Fridge, (), None, (_M_SmartHome._t_DeviceDisp,))
    Fridge._ice_type = _M_SmartHome._t_FridgeDisp

    Fridge._op_setTemperature = IcePy.Operation('setTemperature', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (((), IcePy._t_float, False, 0),), (), None, (_M_SmartHome._t_TmperatureIsTooHigh, _M_SmartHome._t_DeviceIsOFF))
    Fridge._op_getTemperature = IcePy.Operation('getTemperature', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_float, False, 0), (_M_SmartHome._t_DeviceIsOFF,))

    _M_SmartHome.Fridge = Fridge
    del Fridge

if 'RGBIsIncorrect' not in _M_SmartHome.__dict__:
    _M_SmartHome.RGBIsIncorrect = Ice.createTempClass()
    class RGBIsIncorrect(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::SmartHome::RGBIsIncorrect'

    _M_SmartHome._t_RGBIsIncorrect = IcePy.defineException('::SmartHome::RGBIsIncorrect', RGBIsIncorrect, (), False, None, ())
    RGBIsIncorrect._ice_type = _M_SmartHome._t_RGBIsIncorrect

    _M_SmartHome.RGBIsIncorrect = RGBIsIncorrect
    del RGBIsIncorrect

_M_SmartHome._t_Light = IcePy.defineValue('::SmartHome::Light', Ice.Value, -1, (), False, True, None, ())

if 'LightPrx' not in _M_SmartHome.__dict__:
    _M_SmartHome.LightPrx = Ice.createTempClass()
    class LightPrx(_M_SmartHome.DevicePrx):

        def setRGB(self, rgb, context=None):
            return _M_SmartHome.Light._op_setRGB.invoke(self, ((rgb, ), context))

        def setRGBAsync(self, rgb, context=None):
            return _M_SmartHome.Light._op_setRGB.invokeAsync(self, ((rgb, ), context))

        def begin_setRGB(self, rgb, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.Light._op_setRGB.begin(self, ((rgb, ), _response, _ex, _sent, context))

        def end_setRGB(self, _r):
            return _M_SmartHome.Light._op_setRGB.end(self, _r)

        def getRGB(self, context=None):
            return _M_SmartHome.Light._op_getRGB.invoke(self, ((), context))

        def getRGBAsync(self, context=None):
            return _M_SmartHome.Light._op_getRGB.invokeAsync(self, ((), context))

        def begin_getRGB(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.Light._op_getRGB.begin(self, ((), _response, _ex, _sent, context))

        def end_getRGB(self, _r):
            return _M_SmartHome.Light._op_getRGB.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_SmartHome.LightPrx.ice_checkedCast(proxy, '::SmartHome::Light', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_SmartHome.LightPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::SmartHome::Light'
    _M_SmartHome._t_LightPrx = IcePy.defineProxy('::SmartHome::Light', LightPrx)

    _M_SmartHome.LightPrx = LightPrx
    del LightPrx

    _M_SmartHome.Light = Ice.createTempClass()
    class Light(_M_SmartHome.Device):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SmartHome::Device', '::SmartHome::Light')

        def ice_id(self, current=None):
            return '::SmartHome::Light'

        @staticmethod
        def ice_staticId():
            return '::SmartHome::Light'

        def setRGB(self, rgb, current=None):
            raise NotImplementedError("servant method 'setRGB' not implemented")

        def getRGB(self, current=None):
            raise NotImplementedError("servant method 'getRGB' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_LightDisp)

        __repr__ = __str__

    _M_SmartHome._t_LightDisp = IcePy.defineClass('::SmartHome::Light', Light, (), None, (_M_SmartHome._t_DeviceDisp,))
    Light._ice_type = _M_SmartHome._t_LightDisp

    Light._op_setRGB = IcePy.Operation('setRGB', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (((), _M_SmartHome._t_RGB, False, 0),), (), None, (_M_SmartHome._t_RGBIsIncorrect, _M_SmartHome._t_DeviceIsOFF))
    Light._op_getRGB = IcePy.Operation('getRGB', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_SmartHome._t_RGB, False, 0), (_M_SmartHome._t_DeviceIsOFF,))

    _M_SmartHome.Light = Light
    del Light

_M_SmartHome._t_TwoPointLight = IcePy.defineValue('::SmartHome::TwoPointLight', Ice.Value, -1, (), False, True, None, ())

if 'TwoPointLightPrx' not in _M_SmartHome.__dict__:
    _M_SmartHome.TwoPointLightPrx = Ice.createTempClass()
    class TwoPointLightPrx(_M_SmartHome.LightPrx):

        def setFirstPointRGB(self, rgb, context=None):
            return _M_SmartHome.TwoPointLight._op_setFirstPointRGB.invoke(self, ((rgb, ), context))

        def setFirstPointRGBAsync(self, rgb, context=None):
            return _M_SmartHome.TwoPointLight._op_setFirstPointRGB.invokeAsync(self, ((rgb, ), context))

        def begin_setFirstPointRGB(self, rgb, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.TwoPointLight._op_setFirstPointRGB.begin(self, ((rgb, ), _response, _ex, _sent, context))

        def end_setFirstPointRGB(self, _r):
            return _M_SmartHome.TwoPointLight._op_setFirstPointRGB.end(self, _r)

        def setSceondPointRGB(self, rgb, context=None):
            return _M_SmartHome.TwoPointLight._op_setSceondPointRGB.invoke(self, ((rgb, ), context))

        def setSceondPointRGBAsync(self, rgb, context=None):
            return _M_SmartHome.TwoPointLight._op_setSceondPointRGB.invokeAsync(self, ((rgb, ), context))

        def begin_setSceondPointRGB(self, rgb, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.TwoPointLight._op_setSceondPointRGB.begin(self, ((rgb, ), _response, _ex, _sent, context))

        def end_setSceondPointRGB(self, _r):
            return _M_SmartHome.TwoPointLight._op_setSceondPointRGB.end(self, _r)

        def getFirstPointRGB(self, context=None):
            return _M_SmartHome.TwoPointLight._op_getFirstPointRGB.invoke(self, ((), context))

        def getFirstPointRGBAsync(self, context=None):
            return _M_SmartHome.TwoPointLight._op_getFirstPointRGB.invokeAsync(self, ((), context))

        def begin_getFirstPointRGB(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.TwoPointLight._op_getFirstPointRGB.begin(self, ((), _response, _ex, _sent, context))

        def end_getFirstPointRGB(self, _r):
            return _M_SmartHome.TwoPointLight._op_getFirstPointRGB.end(self, _r)

        def getSecondPointRGB(self, context=None):
            return _M_SmartHome.TwoPointLight._op_getSecondPointRGB.invoke(self, ((), context))

        def getSecondPointRGBAsync(self, context=None):
            return _M_SmartHome.TwoPointLight._op_getSecondPointRGB.invokeAsync(self, ((), context))

        def begin_getSecondPointRGB(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.TwoPointLight._op_getSecondPointRGB.begin(self, ((), _response, _ex, _sent, context))

        def end_getSecondPointRGB(self, _r):
            return _M_SmartHome.TwoPointLight._op_getSecondPointRGB.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_SmartHome.TwoPointLightPrx.ice_checkedCast(proxy, '::SmartHome::TwoPointLight', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_SmartHome.TwoPointLightPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::SmartHome::TwoPointLight'
    _M_SmartHome._t_TwoPointLightPrx = IcePy.defineProxy('::SmartHome::TwoPointLight', TwoPointLightPrx)

    _M_SmartHome.TwoPointLightPrx = TwoPointLightPrx
    del TwoPointLightPrx

    _M_SmartHome.TwoPointLight = Ice.createTempClass()
    class TwoPointLight(_M_SmartHome.Light):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SmartHome::Device', '::SmartHome::Light', '::SmartHome::TwoPointLight')

        def ice_id(self, current=None):
            return '::SmartHome::TwoPointLight'

        @staticmethod
        def ice_staticId():
            return '::SmartHome::TwoPointLight'

        def setFirstPointRGB(self, rgb, current=None):
            raise NotImplementedError("servant method 'setFirstPointRGB' not implemented")

        def setSceondPointRGB(self, rgb, current=None):
            raise NotImplementedError("servant method 'setSceondPointRGB' not implemented")

        def getFirstPointRGB(self, current=None):
            raise NotImplementedError("servant method 'getFirstPointRGB' not implemented")

        def getSecondPointRGB(self, current=None):
            raise NotImplementedError("servant method 'getSecondPointRGB' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_TwoPointLightDisp)

        __repr__ = __str__

    _M_SmartHome._t_TwoPointLightDisp = IcePy.defineClass('::SmartHome::TwoPointLight', TwoPointLight, (), None, (_M_SmartHome._t_LightDisp,))
    TwoPointLight._ice_type = _M_SmartHome._t_TwoPointLightDisp

    TwoPointLight._op_setFirstPointRGB = IcePy.Operation('setFirstPointRGB', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (((), _M_SmartHome._t_RGB, False, 0),), (), None, (_M_SmartHome._t_RGBIsIncorrect, _M_SmartHome._t_DeviceIsOFF))
    TwoPointLight._op_setSceondPointRGB = IcePy.Operation('setSceondPointRGB', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (((), _M_SmartHome._t_RGB, False, 0),), (), None, (_M_SmartHome._t_RGBIsIncorrect, _M_SmartHome._t_DeviceIsOFF))
    TwoPointLight._op_getFirstPointRGB = IcePy.Operation('getFirstPointRGB', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_SmartHome._t_RGB, False, 0), (_M_SmartHome._t_DeviceIsOFF,))
    TwoPointLight._op_getSecondPointRGB = IcePy.Operation('getSecondPointRGB', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_SmartHome._t_RGB, False, 0), (_M_SmartHome._t_DeviceIsOFF,))

    _M_SmartHome.TwoPointLight = TwoPointLight
    del TwoPointLight

if 'BrightnessIsIncorrect' not in _M_SmartHome.__dict__:
    _M_SmartHome.BrightnessIsIncorrect = Ice.createTempClass()
    class BrightnessIsIncorrect(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::SmartHome::BrightnessIsIncorrect'

    _M_SmartHome._t_BrightnessIsIncorrect = IcePy.defineException('::SmartHome::BrightnessIsIncorrect', BrightnessIsIncorrect, (), False, None, ())
    BrightnessIsIncorrect._ice_type = _M_SmartHome._t_BrightnessIsIncorrect

    _M_SmartHome.BrightnessIsIncorrect = BrightnessIsIncorrect
    del BrightnessIsIncorrect

_M_SmartHome._t_LedLightt = IcePy.defineValue('::SmartHome::LedLightt', Ice.Value, -1, (), False, True, None, ())

if 'LedLighttPrx' not in _M_SmartHome.__dict__:
    _M_SmartHome.LedLighttPrx = Ice.createTempClass()
    class LedLighttPrx(_M_SmartHome.LightPrx):

        def setBrightness(self, brightness, context=None):
            return _M_SmartHome.LedLightt._op_setBrightness.invoke(self, ((brightness, ), context))

        def setBrightnessAsync(self, brightness, context=None):
            return _M_SmartHome.LedLightt._op_setBrightness.invokeAsync(self, ((brightness, ), context))

        def begin_setBrightness(self, brightness, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.LedLightt._op_setBrightness.begin(self, ((brightness, ), _response, _ex, _sent, context))

        def end_setBrightness(self, _r):
            return _M_SmartHome.LedLightt._op_setBrightness.end(self, _r)

        def getBrightness(self, context=None):
            return _M_SmartHome.LedLightt._op_getBrightness.invoke(self, ((), context))

        def getBrightnessAsync(self, context=None):
            return _M_SmartHome.LedLightt._op_getBrightness.invokeAsync(self, ((), context))

        def begin_getBrightness(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.LedLightt._op_getBrightness.begin(self, ((), _response, _ex, _sent, context))

        def end_getBrightness(self, _r):
            return _M_SmartHome.LedLightt._op_getBrightness.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_SmartHome.LedLighttPrx.ice_checkedCast(proxy, '::SmartHome::LedLightt', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_SmartHome.LedLighttPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::SmartHome::LedLightt'
    _M_SmartHome._t_LedLighttPrx = IcePy.defineProxy('::SmartHome::LedLightt', LedLighttPrx)

    _M_SmartHome.LedLighttPrx = LedLighttPrx
    del LedLighttPrx

    _M_SmartHome.LedLightt = Ice.createTempClass()
    class LedLightt(_M_SmartHome.Light):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SmartHome::Device', '::SmartHome::LedLightt', '::SmartHome::Light')

        def ice_id(self, current=None):
            return '::SmartHome::LedLightt'

        @staticmethod
        def ice_staticId():
            return '::SmartHome::LedLightt'

        def setBrightness(self, brightness, current=None):
            raise NotImplementedError("servant method 'setBrightness' not implemented")

        def getBrightness(self, current=None):
            raise NotImplementedError("servant method 'getBrightness' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_LedLighttDisp)

        __repr__ = __str__

    _M_SmartHome._t_LedLighttDisp = IcePy.defineClass('::SmartHome::LedLightt', LedLightt, (), None, (_M_SmartHome._t_LightDisp,))
    LedLightt._ice_type = _M_SmartHome._t_LedLighttDisp

    LedLightt._op_setBrightness = IcePy.Operation('setBrightness', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (((), IcePy._t_int, False, 0),), (), None, (_M_SmartHome._t_DeviceIsOFF, _M_SmartHome._t_BrightnessIsIncorrect))
    LedLightt._op_getBrightness = IcePy.Operation('getBrightness', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), (_M_SmartHome._t_DeviceIsOFF,))

    _M_SmartHome.LedLightt = LedLightt
    del LedLightt

if 'DeviceObject' not in _M_SmartHome.__dict__:
    _M_SmartHome.DeviceObject = Ice.createTempClass()
    class DeviceObject(object):
        def __init__(self, name='', type=''):
            self.name = name
            self.type = type

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            _h = 5 * _h + Ice.getHash(self.type)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_SmartHome.DeviceObject):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return (-1 if self.name is None else 1)
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_DeviceObject)

        __repr__ = __str__

    _M_SmartHome._t_DeviceObject = IcePy.defineStruct('::SmartHome::DeviceObject', DeviceObject, (), (
        ('name', (), IcePy._t_string),
        ('type', (), IcePy._t_string)
    ))

    _M_SmartHome.DeviceObject = DeviceObject
    del DeviceObject

if '_t_devicesList' not in _M_SmartHome.__dict__:
    _M_SmartHome._t_devicesList = IcePy.defineSequence('::SmartHome::devicesList', (), _M_SmartHome._t_DeviceObject)

if 'ListIsEmpty' not in _M_SmartHome.__dict__:
    _M_SmartHome.ListIsEmpty = Ice.createTempClass()
    class ListIsEmpty(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::SmartHome::ListIsEmpty'

    _M_SmartHome._t_ListIsEmpty = IcePy.defineException('::SmartHome::ListIsEmpty', ListIsEmpty, (), False, None, ())
    ListIsEmpty._ice_type = _M_SmartHome._t_ListIsEmpty

    _M_SmartHome.ListIsEmpty = ListIsEmpty
    del ListIsEmpty

_M_SmartHome._t_DeviceList = IcePy.defineValue('::SmartHome::DeviceList', Ice.Value, -1, (), False, True, None, ())

if 'DeviceListPrx' not in _M_SmartHome.__dict__:
    _M_SmartHome.DeviceListPrx = Ice.createTempClass()
    class DeviceListPrx(Ice.ObjectPrx):

        def getDeviceList(self, context=None):
            return _M_SmartHome.DeviceList._op_getDeviceList.invoke(self, ((), context))

        def getDeviceListAsync(self, context=None):
            return _M_SmartHome.DeviceList._op_getDeviceList.invokeAsync(self, ((), context))

        def begin_getDeviceList(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.DeviceList._op_getDeviceList.begin(self, ((), _response, _ex, _sent, context))

        def end_getDeviceList(self, _r):
            return _M_SmartHome.DeviceList._op_getDeviceList.end(self, _r)

        def addObject(self, obj, context=None):
            return _M_SmartHome.DeviceList._op_addObject.invoke(self, ((obj, ), context))

        def addObjectAsync(self, obj, context=None):
            return _M_SmartHome.DeviceList._op_addObject.invokeAsync(self, ((obj, ), context))

        def begin_addObject(self, obj, _response=None, _ex=None, _sent=None, context=None):
            return _M_SmartHome.DeviceList._op_addObject.begin(self, ((obj, ), _response, _ex, _sent, context))

        def end_addObject(self, _r):
            return _M_SmartHome.DeviceList._op_addObject.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_SmartHome.DeviceListPrx.ice_checkedCast(proxy, '::SmartHome::DeviceList', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_SmartHome.DeviceListPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::SmartHome::DeviceList'
    _M_SmartHome._t_DeviceListPrx = IcePy.defineProxy('::SmartHome::DeviceList', DeviceListPrx)

    _M_SmartHome.DeviceListPrx = DeviceListPrx
    del DeviceListPrx

    _M_SmartHome.DeviceList = Ice.createTempClass()
    class DeviceList(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::SmartHome::DeviceList')

        def ice_id(self, current=None):
            return '::SmartHome::DeviceList'

        @staticmethod
        def ice_staticId():
            return '::SmartHome::DeviceList'

        def getDeviceList(self, current=None):
            raise NotImplementedError("servant method 'getDeviceList' not implemented")

        def addObject(self, obj, current=None):
            raise NotImplementedError("servant method 'addObject' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_SmartHome._t_DeviceListDisp)

        __repr__ = __str__

    _M_SmartHome._t_DeviceListDisp = IcePy.defineClass('::SmartHome::DeviceList', DeviceList, (), None, ())
    DeviceList._ice_type = _M_SmartHome._t_DeviceListDisp

    DeviceList._op_getDeviceList = IcePy.Operation('getDeviceList', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, None, (), (), (), ((), _M_SmartHome._t_devicesList, False, 0), (_M_SmartHome._t_ListIsEmpty,))
    DeviceList._op_addObject = IcePy.Operation('addObject', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_SmartHome._t_DeviceObject, False, 0),), (), None, ())

    _M_SmartHome.DeviceList = DeviceList
    del DeviceList

# End of module SmartHome