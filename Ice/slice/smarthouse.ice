
module SmartHome{

    enum Status{
        On, // device works and actions can be performed
        Off //The device has been turned off and needs to be turned on to do anything
        };

    struct RGB{
        int r;
        int g;
        int bl;
    };

    exception DeviceIsArleadyON {};
    exception DeviceIsArleadyOFF {};
    exception DeviceIsOFF {};

    interface Device{
        idempotent void turnOn() throws DeviceIsArleadyON;
        idempotent void turnOFF() throws DeviceIsArleadyOFF;
        Status getStatus() throws DeviceIsOFF;
    };

    exception TmperatureIsTooHigh {};

    interface Fridge extends Device{
        idempotent void setTemperature(float temperature) throws TmperatureIsTooHigh, DeviceIsOFF;
        float getTemperature() throws DeviceIsOFF;
    };

    exception RGBIsIncorrect {};

    interface Light extends Device{
        idempotent void setRGB(RGB rgb) throws RGBIsIncorrect, DeviceIsOFF;
        RGB getRGB() throws DeviceIsOFF;
    };

    interface TwoPointLight extends Light{
        idempotent void setFirstPointRGB(RGB rgb) throws RGBIsIncorrect, DeviceIsOFF;
        idempotent void setSceondPointRGB(RGB rgb) throws RGBIsIncorrect, DeviceIsOFF;
        RGB getFirstPointRGB() throws DeviceIsOFF;
        RGB getSecondPointRGB() throws DeviceIsOFF;
    };

    exception BrightnessIsIncorrect {};

    interface LedLightt extends Light{
            idempotent void setBrightness(int brightness) throws DeviceIsOFF, BrightnessIsIncorrect;
            int getBrightness() throws DeviceIsOFF;
        };

    struct DeviceObject{
        string name;
        string type;
    };

    sequence<DeviceObject> devicesList;
    exception ListIsEmpty {};

    interface DeviceList{
        idempotent devicesList getDeviceList() throws ListIsEmpty;
        void addObject(DeviceObject obj);
    };
};

