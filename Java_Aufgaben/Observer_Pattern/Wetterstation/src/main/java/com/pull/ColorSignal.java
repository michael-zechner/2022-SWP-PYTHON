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
