package main.java.com.pull;

public class ColorSignal implements Observer {
    private WeahtherStation ws;

    public ColorSignal(WeahtherStation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update() {
        double newTemp = ws.getTemp();
        double newHumidity = ws.getHumidity();
        if (newTemp <= 30.0){
            System.out.println("Temperatur im grünen Bereich");
        }else{
            System.out.println("Temperatur im roten Bereich");
        }
        if (newHumidity <= 70.0){
            System.out.println("Luffeuchtigkeit im grünen Bereich\n");
        }else{
            System.out.println("Luffeuchtigkeit im roten Bereich\n");
        }
    }
}
