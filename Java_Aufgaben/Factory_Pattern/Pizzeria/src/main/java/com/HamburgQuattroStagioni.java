package main.java.com;

public class HamburgQuattroStagioni extends Pizza {

    @Override
    void bake() {
        System.out.println("Pizza Quattro Stagioni baked in Hamburg style!");
    }

    @Override
    void cut() {
        System.out.println("Cut in eight pieces!");
    }

    @Override
    void pack() {
        System.out.println("Pack into box!");
    }
    
}
