package main.java.com.pull;

public class Screen implements Observer {

    private WeahtherStation ws;

    public Screen(WeahtherStation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update() {
        double newTemp = ws.getTemp();
        double newHumidity = ws.getHumidity();
        System.out.println("Temperatur: " + newTemp + "°C");
        System.out.println("Luffeuchtigkeit: " + newHumidity + "%\n");
    }
    
}
