package main.java.com;

public class BerlinQuattroStagioni extends Pizza {

    @Override
    void bake() {
        System.out.println("Pizza Quattro Stagioni baked in Berlin style!");
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
