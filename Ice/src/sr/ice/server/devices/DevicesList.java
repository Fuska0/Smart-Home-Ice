package sr.ice.server.devices;

import SmartHome.DeviceList;
import SmartHome.DeviceObject;
import SmartHome.ListIsEmpty;
import com.zeroc.Ice.Current;
import java.util.ArrayList;
import java.util.List;

public class DevicesList implements DeviceList {
    private List<DeviceObject> devicesList;

    public DevicesList() {
        this.devicesList = new ArrayList<>();
    }

    @Override
    public DeviceObject[] getDeviceList(Current current) throws ListIsEmpty {
        if(devicesList.isEmpty()) {
            throw new ListIsEmpty();
        } else {
            return devicesList.toArray(new DeviceObject[0]);
        }
    }

    @Override
    public void addObject(DeviceObject obj, Current current) {
        devicesList.add(obj);
    }

    public void addObjectServer(DeviceObject obj) {
        devicesList.add(obj);
    }
}
