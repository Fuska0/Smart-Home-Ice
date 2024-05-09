package sr.ice.server.devices;

import SmartHome.DeviceIsOFF;
import SmartHome.RGB;
import SmartHome.RGBIsIncorrect;
import SmartHome.Status;
import com.zeroc.Ice.Current;

public class Light extends Device implements SmartHome.Light {
    private RGB rgb;

    public Light(){
        this.rgb = new RGB(255,255,255);
    }

    @Override
    public void setRGB(RGB rgb, Current current) throws DeviceIsOFF, RGBIsIncorrect {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();
        else if(rgb.r < 0 || rgb.g < 0 || rgb.bl < 0 || rgb.r > 255 || rgb.g > 255 || rgb.bl > 255) throw new RGBIsIncorrect();
        else{
            this.rgb = rgb;
            System.out.print("new light RGB on " + current.id.name + ": " + this.rgb.toString());
        };
    }

    @Override
    public RGB getRGB(Current current) throws DeviceIsOFF {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();
        else{
            System.out.println("getRGB worked on " + current.id.name);
            return rgb;
        }
    }
}
