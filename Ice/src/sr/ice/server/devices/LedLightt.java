package sr.ice.server.devices;

import SmartHome.BrightnessIsIncorrect;
import SmartHome.DeviceIsOFF;
import SmartHome.RGBIsIncorrect;
import SmartHome.Status;
import com.zeroc.Ice.Current;

public class LedLightt extends Light implements SmartHome.LedLightt {
    private int maxBrightness;
    private int brightness;

    public LedLightt(){
        this.maxBrightness = 10;
        this.brightness = 5;
    }
    @Override
    public void setBrightness(int brightness, Current current) throws DeviceIsOFF, BrightnessIsIncorrect {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();
        else if(brightness < 0 || brightness > maxBrightness) throw new BrightnessIsIncorrect();
        else {
            this.brightness = brightness;
            System.out.println(current.id.name + " setBrightness");
        }
    }

    @Override
    public int getBrightness(Current current) throws DeviceIsOFF {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();

        else {
            System.out.println(current.id.name + " getBrightness");
            return brightness;
        }
    }
}
