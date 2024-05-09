package sr.ice.server.devices;
import SmartHome.Status;
import SmartHome.DeviceIsArleadyOFF;
import SmartHome.DeviceIsArleadyON;
import com.zeroc.Ice.Current;

public class Device implements SmartHome.Device {

    private Status status = Status.On;

    @Override
    public void turnOn(Current current) throws DeviceIsArleadyON {
        if(status == Status.On){
            throw new DeviceIsArleadyON();
        }

        else{
            status = Status.On;

            System.out.println(current.id.name + " is on");
        }
    }

    @Override
    public void turnOFF(Current current) throws DeviceIsArleadyOFF {
        if(status == Status.Off){
            throw new DeviceIsArleadyOFF();
        }

        else{
            status = Status.Off;

            System.out.println(current.id.name + " is off");
        }

    }

    @Override
    public Status getStatus(Current current) {
        System.out.println(current.id.name + " status was returned");

        return status;
    }
}
