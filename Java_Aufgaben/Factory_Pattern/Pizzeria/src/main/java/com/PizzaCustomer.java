package main.java.com;
import java.util.Scanner;


public class PizzaCustomer {

    public static PizzaStore createPizzaStore(String pizzeria){
        if (pizzeria != null){
            switch(pizzeria){
                    case "Hamburg": return new HamburgPizzaStore();
                    case "Rostock": return new RostockPizzaStore();
                    case "Berlin": return new BerlinPizzaStore();
                    default: return null;
            }
        }
        return null;
    }

    public static Pizza Pizzacreate(PizzaStore store, String pizza_input){
        if(pizza_input != null){
            switch(pizza_input){
                case "Salami": return store.orderPizza(pizza_input);
                case "Calzone": return store.orderPizza(pizza_input);
                case "QuattroStagioni": return store.orderPizza(pizza_input);
                case "Hawaii": return store.orderPizza(pizza_input);
            }
        }
        return null;
    }

    public static void main(String[] args){
        PizzaStore store;
        Pizza pizza;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welche Pizzeria möchten Sie?");
        String pizzeria = scanner.nextLine();

        System.out.println("Welche Pizza möchten Sie?");
        String pizza_input = scanner.nextLine();
        store = createPizzaStore(pizzeria);
        pizza = Pizzacreate(store, pizza_input);
        System.out.println(pizza);

        scanner.close();
    }   
}
