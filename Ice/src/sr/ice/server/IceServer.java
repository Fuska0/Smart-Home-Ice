package sr.ice.server;

import SmartHome.DeviceObject;
import com.zeroc.Ice.Communicator;
import com.zeroc.Ice.Identity;
import com.zeroc.Ice.ObjectAdapter;
import com.zeroc.Ice.Util;
import sr.ice.server.devices.*;

import java.util.ArrayList;
import java.util.List;

public class IceServer {

	public void addToASM(String name, String category, Object obj, ObjectAdapter adapter, DevicesList devicesList){
		adapter.add((com.zeroc.Ice.Object) obj, new Identity(name, category));
		DeviceObject deviceObject = new DeviceObject(name, category);
		devicesList.addObjectServer(deviceObject);
	}
	public void t1(String[] args) {
		int status = 0;
		Communicator communicator = null;

		try {
			// 1. Inicjalizacja ICE - utworzenie communicatora
			communicator = Util.initialize(args);

			// 2. Konfiguracja adaptera
			ObjectAdapter adapter = communicator.createObjectAdapterWithEndpoints("Adapter1", "tcp -h 127.0.0.2 -p 10000 -z : udp -h 127.0.0.2 -p 10000 -z");


			Light light1 = new Light();
			Light light2 = new Light();
			LedLightt led1 = new LedLightt();
			TwoPointLight twoPointLight1 = new TwoPointLight();
			FridgeDevice fridge1 = new FridgeDevice();
			DevicesList devicesList1 = new DevicesList();
			adapter.add(devicesList1, new Identity("devicesList1", "devicesList"));

			// 4. Dodanie wpisów do tablicy ASM, skojarzenie nazwy obiektu (Identity) z serwantem
			addToASM("light11", "light", light1, adapter,devicesList1);
			addToASM("light22", "light", light2, adapter, devicesList1);
			addToASM("led11", "led", led1, adapter,devicesList1);
			addToASM("led22", "led", led1, adapter,devicesList1);
			addToASM("twoPointLight11", "twoPointLight", twoPointLight1, adapter,devicesList1);
			addToASM("fridge11", "fridge", fridge1, adapter,devicesList1);


			// 5. Aktywacja adaptera i wejście w pętlę przetwarzania żądań
			adapter.activate();

			System.out.println("Entering event processing loop...");

			communicator.waitForShutdown();

		} catch (Exception e) {
			e.printStackTrace(System.err);
			status = 1;
		}
		if (communicator != null) {
			try {
				communicator.destroy();
			} catch (Exception e) {
				e.printStackTrace(System.err);
				status = 1;
			}
		}
		System.exit(status);
	}


	public static void main(String[] args) {
		IceServer app = new IceServer();
		app.t1(args);
	}
}