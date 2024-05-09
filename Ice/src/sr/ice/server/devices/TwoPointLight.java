package sr.ice.server.devices;

import SmartHome.DeviceIsOFF;
import SmartHome.RGB;
import SmartHome.RGBIsIncorrect;
import SmartHome.Status;
import com.zeroc.Ice.Current;

public class TwoPointLight extends Light implements SmartHome.TwoPointLight {

    private RGB firstRGB;
    private RGB secondEGB;

    @Override
    public void setRGB(RGB rgb, Current current) throws DeviceIsOFF, RGBIsIncorrect {
        setFirstPointRGB(rgb,current);
        setSceondPointRGB(rgb,current);
    }

    @Override
    public void setFirstPointRGB(RGB rgb, Current current) throws DeviceIsOFF, RGBIsIncorrect {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();
        else if(rgb.r < 0 || rgb.g < 0 || rgb.bl < 0 || rgb.r > 255 || rgb.g > 255 || rgb.bl > 255) throw new RGBIsIncorrect();
        else {
            firstRGB = rgb;
            System.out.println(current.id.name + " setFirstPointRGB");
        }
    }

    @Override
    public void setSceondPointRGB(RGB rgb, Current current) throws DeviceIsOFF, RGBIsIncorrect {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();
        else if(rgb.r < 0 || rgb.g < 0 || rgb.bl < 0 || rgb.r > 255 || rgb.g > 255 || rgb.bl > 255) throw new RGBIsIncorrect();
        else {
            secondEGB = rgb;
            System.out.println(current.id.name + " setSceondPointRGB");
        }
    }

    @Override
    public RGB getFirstPointRGB(Current current) throws DeviceIsOFF {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();

        else {
            System.out.println(current.id.name + " getFirstPointRGB");
            return firstRGB;
        }
    }

    @Override
    public RGB getSecondPointRGB(Current current) throws DeviceIsOFF {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();

        else {
            System.out.println(current.id.name + " getSecondPointRGB");
            return secondEGB;
        }
    }
}
