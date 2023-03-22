package main.java.com.push;

public class ColorSignal implements Observer {
    private WeahtherStation ws;

    public ColorSignal(WeahtherStation ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update(double temp, double humidity) {
        double newTemp = temp;
        double newHumidity = humidity;
        if (newTemp <= 30.0){
            System.out.println("Green");
        }else{
            System.out.println("Red");
        }
        if (newHumidity <= 70.0){
            System.out.println("Green\n");
        }else{
            System.out.println("Red\n");
        }
    }
}
