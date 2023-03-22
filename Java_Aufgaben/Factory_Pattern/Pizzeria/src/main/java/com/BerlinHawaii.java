package main.java.com;

public class BerlinHawaii extends Pizza {

    @Override
    void bake() {
        System.out.println("Pizza Hawaii baked in Berlin style!");
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
