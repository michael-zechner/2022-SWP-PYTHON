package main.java.com.push;

import java.util.ArrayList;
import java.util.List;

public class WeahtherStation implements Observable {

    private List<Observer> observerList = new ArrayList<>();

    private double temp;
    private double humidity;    

    @Override
    public void addClient(Observer client) {
        this.observerList.add(client);
    }

    @Override
    public void removeClient(Observer client) {
        this.observerList.remove(client);
    }

    @Override
    public void notifyAllClients() {
        for (Observer observer : observerList){
            observer.update(this.temp,this.humidity);
        }
    }

    public double getTemp() {
        return temp;
    }

    public void setTemp(double temp) {
        this.temp = temp;
        this.notifyAllClients();
    }

    public double getHumidity() {
        return humidity;
    }

    public void setHumidity(double humidity) {
        this.humidity = humidity;
        this.notifyAllClients();
    }
}
