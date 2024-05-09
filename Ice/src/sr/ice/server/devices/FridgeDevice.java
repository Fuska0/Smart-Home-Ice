package sr.ice.server.devices;
import SmartHome.DeviceIsOFF;
import SmartHome.Status;
import com.zeroc.Ice.Current;
import SmartHome.TmperatureIsTooHigh;
import com.zeroc.Ice.Current;

public class FridgeDevice extends Device implements SmartHome.Fridge {
    private float temperature;
    private float maxTemp;
    private float minTemp;

    public FridgeDevice(){
        this.temperature = 5;
        maxTemp = 20;
        minTemp = -5;
    }
    @Override
    public void setTemperature(float temperature, Current current) throws TmperatureIsTooHigh, DeviceIsOFF {
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();
        else if(temperature > maxTemp || temperature < minTemp) throw new TmperatureIsTooHigh();
        else {
            this.temperature = temperature;
            System.out.println(current.id.name + " set Temperature ");
        }
    }

    @Override
    public float getTemperature(Current current) throws DeviceIsOFF{
        if (getStatus(current) == Status.Off) throw new DeviceIsOFF();
        else {
            System.out.println(current.id.name + " getTemperature ");
            return this.temperature;
        }
    }
}
