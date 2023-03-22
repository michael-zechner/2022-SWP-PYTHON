package main.java.com.push;

public interface Observable {
    public abstract void addClient(Observer client);
    public abstract void removeClient(Observer client);
    public abstract void notifyAllClients();
}
