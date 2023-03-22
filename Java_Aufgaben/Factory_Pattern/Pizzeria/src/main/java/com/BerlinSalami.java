package main.java.com;

public class BerlinSalami extends Pizza {

    @Override
    void bake() {
        System.out.println("Pizza Salami baked in Berlin style!");
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
