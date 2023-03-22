package main.java.com;

public class HamburgPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
        if(type.equals("Salami")){
            return new HamburgSalami();
        }else if(type.equals("Calzone")){
            return new HamburgCalzone();
        }else if(type.equals("QuattroStagioni")){
            return new HamburgQuattroStagioni();
        } else if (type.equals("Hawaii")){
            return new HamburgHawaii();
        }else{
            return null;
        }
    }
}
