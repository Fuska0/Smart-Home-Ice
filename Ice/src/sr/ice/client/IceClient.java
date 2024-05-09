package sr.ice.client;

import SmartHome.*;
import com.zeroc.Ice.*;

import java.io.IOException;
import java.lang.Exception;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

public class IceClient {
	public static void main(String[] args) {
		int status = 0;
		Communicator communicator = null;
		Map<String, LightPrx> lightMap = new HashMap<>();
		Map<String,LedLighttPrx> ledMap = new HashMap<>();
		Map<String,TwoPointLightPrx> twoLightMap = new HashMap<>();
		Map<String, FridgePrx> fridgeMap = new HashMap<>();

		try {
			communicator = Util.initialize(args);
			ObjectPrx base6 = communicator.stringToProxy("devicesList/devicesList1:tcp -h 127.0.0.2 -p 10000 -z : udp -h 127.0.0.2 -p 10000 -z");
			DeviceListPrx obj6 = DeviceListPrx.checkedCast(base6);
			if (obj6 == null) throw new Error("Invalid proxy");

			for(DeviceObject obj : obj6.getDeviceList()){
				String proxy = obj.type + "/" + obj.name+ ":tcp -h 127.0.0.2 -p 10000 -z : udp -h 127.0.0.2 -p 10000 -z";
				ObjectPrx base = communicator.stringToProxy(proxy);

				switch (obj.type){
					case "light":

						LightPrx object1 = LightPrx.checkedCast(base);
						if (object1 == null) throw new Error("Invalid proxy");
						else lightMap.put(obj.name, object1);
						break;
					case "led":

						LedLighttPrx object2 = LedLighttPrx.checkedCast(base);
						if (object2 == null) throw new Error("Invalid proxy");
						else ledMap.put(obj.name, object2);
						break;
					case "twoPointLight":

						TwoPointLightPrx object3 = TwoPointLightPrx.checkedCast(base);
						if (object3 == null) throw new Error("Invalid proxy");
						else twoLightMap.put(obj.name, object3);
						break;
					case "fridge":

						FridgePrx object4 = FridgePrx.checkedCast(base);
						if (object4 == null) throw new Error("Invalid proxy");
						else fridgeMap.put(obj.name, object4);

						break;
					default:
						System.out.println("unexpected device");
				}
			}


			String line = null;
			String line2 = "t";
			String line3 = "t";
			java.io.BufferedReader in = new java.io.BufferedReader(new java.io.InputStreamReader(System.in));

			System.out.println("Write devices to check active ones");
			do {
				try {
					System.out.print("==> ");
					line = in.readLine();
					if(line.equals("devices")){
						for(DeviceObject obj : obj6.getDeviceList()){
							System.out.println(obj.name);
						}
					}
					else if(lightMap.get(line) != null){
						lightWorker(lightMap.get(line), line2, line3, in);
					}
					else if(ledMap.get(line) != null){
						ledWorker(ledMap.get(line), line2, line3 ,in);
					}
					else if(twoLightMap.get(line) != null){
						twoLightWorker(twoLightMap.get(line), line2, line3, in);
					}
					else if(fridgeMap.get(line) != null){
						fridgeWorker(fridgeMap.get(line), line2, line3, in);
					}
					else {
						System.out.println("????");
					}
				} catch (IOException | TwowayOnlyException ex) {
					ex.printStackTrace(System.err);
				}
				catch (DeviceIsArleadyOFF ex) {
					System.out.println("Device you try to off is already off");
				}
				catch (DeviceIsArleadyON ex) {
					System.out.println("Device you try to off is already on");
				}
				catch (DeviceIsOFF ex) {
					System.out.println("Device you try to use is off");
				}
				catch (RGBIsIncorrect ex) {
					System.out.println("Your wrote bad RGB");
				}
				catch (BrightnessIsIncorrect ex){
					System.out.println("Your wrote bad brightness");
				}
				catch (TmperatureIsTooHigh ex){
					System.out.println("Your wrote bad temperature");
				}
			}
			while (!Objects.equals(line, "x"));


		} catch (LocalException e) {
			e.printStackTrace();
			status = 1;
		} catch (Exception e) {
			System.err.println(e.getMessage());
			status = 1;
		}
		if (communicator != null) { //clean
			try {
				communicator.destroy();
			} catch (Exception e) {
				System.err.println(e.getMessage());
				status = 1;
			}
		}
		System.exit(status);
	}

	public static RGB getRGBInput(String line3, java.io.BufferedReader in) throws IOException {
		while(!line3.matches("[0-9]+")){
			System.out.print("Give red: ");
			line3 = in.readLine();
		}

		int[] numsInt = new int[3];
		numsInt[0] =Integer.parseInt(line3);
		line3 = "t";

		while(!line3.matches("[0-9]+")){
			System.out.print("Give green: ");
			line3 = in.readLine();
		}

		numsInt[1] =Integer.parseInt(line3);
		line3 = "t";

		while(!line3.matches("[0-9]+")){
			System.out.print("Give blue: ");
			line3 = in.readLine();
		}
		numsInt[2] =Integer.parseInt(line3);

		return new RGB(numsInt[0], numsInt[1], numsInt[2]);
	}

	public static void lightWorker(LightPrx obj1, String line2, String line3, java.io.BufferedReader in)
			throws IOException, DeviceIsOFF, RGBIsIncorrect, DeviceIsArleadyON, DeviceIsArleadyOFF {
		while(!line2.equals("return")){
			System.out.println("Options: setRGB, getRGB, turnOn, turnOff, status");
			System.out.print(">: ");
			line2 = in.readLine();
			switch (line2){
				case "setRGB":
					obj1.setRGB(getRGBInput(line3, in));
					break;
				case "getRGB":
					System.out.println(obj1.getRGB().show());
					break;
				case "turnOn":
					obj1.turnOn();
					break;
				case "turnOff":
					obj1.turnOFF();
					break;
				case "status":
					System.out.println(obj1.getStatus().toString());
					break;
				case "return":
					System.out.println("");
					line2 = "return";
					break;
				default:
					System.out.println("???");
			}
		}
	}

	public static void ledWorker(LedLighttPrx obj1, String line2, String line3, java.io.BufferedReader in)
			throws IOException, DeviceIsOFF, RGBIsIncorrect, DeviceIsArleadyON, DeviceIsArleadyOFF, BrightnessIsIncorrect {
		while(!line2.equals("return")){
			System.out.println("Options: setRGB, getRGB, turnOn, turnOff, status, setBrightness, getBrightness");
			System.out.print(">: ");
			line2 = in.readLine();
			switch (line2){
				case "setRGB":
					obj1.setRGB(getRGBInput(line3, in));
					break;
				case "getRGB":
					System.out.println(obj1.getRGB().show());
					break;
				case "turnOn":
					obj1.turnOn();
					break;
				case "turnOff":
					obj1.turnOFF();
					break;
				case "status":
					System.out.println(obj1.getStatus().toString());
					break;
				case "setBrightness":
					while(!line3.matches("[0-9]+")){
						System.out.print("Give number (0-10): ");
						line3 = in.readLine();
					}
					obj1.setBrightness(Integer.parseInt(String.valueOf(line3)));
					break;
				case "getBrightness":
					System.out.println(obj1.getBrightness());
					break;
				case "return":
					System.out.println("");
					line2 = "return";
					break;
				default:
					System.out.println("???");
			}
		}
	}

	public static void fridgeWorker(FridgePrx obj1, String line2, String line3, java.io.BufferedReader in)
			throws IOException, DeviceIsOFF, DeviceIsArleadyON, DeviceIsArleadyOFF, TmperatureIsTooHigh {
		while(!line2.equals("return")){
			System.out.println("Options: turnOn, turnOff, status, setTemperature, getTemperature");
			System.out.print(">: ");
			line2 = in.readLine();
			switch (line2){
				case "turnOn":
					obj1.turnOn();
					break;
				case "turnOff":
					obj1.turnOFF();
					break;
				case "status":
					System.out.println(obj1.getStatus().toString());
					break;
				case "setTemperature":
					while(!line3.matches("-?[0-9]+(\\.[0-9]+)?")){
						System.out.print("Give number (-5 - 20): ");
						line3 = in.readLine();
					}
					obj1.setTemperature(Float.parseFloat(String.valueOf(line3)));
					break;
				case "getTemperature":
					System.out.println(obj1.getTemperature());
					break;
				case "return":
					System.out.println("");
					line2 = "return";
					break;
				default:
					System.out.println("???");
			}
		}
	}
	public static void twoLightWorker(TwoPointLightPrx obj1, String line2, String line3, java.io.BufferedReader in) throws IOException, DeviceIsArleadyON, DeviceIsArleadyOFF, DeviceIsOFF, RGBIsIncorrect {
		while(!line2.equals("return")){
			System.out.println("Options: turnOn, turnOff, status, setRGB, setFirstPointRGB, " +
					"setSceondPointRGB, getFirstPointRGB, getSecondPointRGB");

			System.out.print(">: ");
			line2 = in.readLine();
			switch (line2){
				case "turnOn":
					obj1.turnOn();
					break;
				case "turnOff":
					obj1.turnOFF();
					break;
				case "status":
					System.out.println(obj1.getStatus().toString());
					break;
				case "setRGB":
					obj1.setRGB(getRGBInput(line3, in));
					break;
				case "setFirstPointRGB":
					obj1.setFirstPointRGB(getRGBInput(line3, in));
					break;
				case "setSceondPointRGB":
					obj1.setSceondPointRGB(getRGBInput(line3, in));
					break;
				case "getFirstPointRGB":
					System.out.println(obj1.getFirstPointRGB().show());
					break;
				case "getSecondPointRGB":
					System.out.println(obj1.getSecondPointRGB().show());
					break;
				case "return":
					System.out.println("");
					line2 = "return";
					break;
				default:
					System.out.println("???");
			}
		}
	}
}