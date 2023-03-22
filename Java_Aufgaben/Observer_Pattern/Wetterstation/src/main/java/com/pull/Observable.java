package main.java.com.pull;

public interface Observable {
    public abstract void addClient(Observer client);
    public abstract void removeClient(Observer client);
    public abstract void notifyAllClients();
}
