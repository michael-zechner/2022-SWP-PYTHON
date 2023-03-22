package main.java.com.push;

public class Screen implements Observer {

    private WeahtherStation ws;

    public Screen(WeahtherStation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update(double temp, double humidity) {
        double newTemp = temp;
        double newHumidity = humidity;
        System.out.println("Temperatur: " + newTemp + "°C");
        System.out.println("Luffeuchtigkeit: " + newHumidity + "%\n");
    }
    
}
