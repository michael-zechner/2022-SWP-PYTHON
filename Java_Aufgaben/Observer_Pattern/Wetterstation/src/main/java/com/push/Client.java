package main.java.com.push;

public class Client {
    
    public static void main(String[] args) {
        WeahtherStation ws = new WeahtherStation();
        ColorSignal signal = new ColorSignal(ws);
        ws.setHumidity(73.8);
        ws.setTemp(32.9);
    }

}
