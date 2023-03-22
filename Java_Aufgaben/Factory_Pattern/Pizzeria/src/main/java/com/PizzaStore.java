package main.java.com;

public abstract class PizzaStore {
    
    public Pizza orderPizza(String type) {
        Pizza pizza = createPizza(type);
        pizza.bake();
        pizza.cut();
        pizza.pack();
        return pizza;
    }

    abstract Pizza createPizza(String type);
}
