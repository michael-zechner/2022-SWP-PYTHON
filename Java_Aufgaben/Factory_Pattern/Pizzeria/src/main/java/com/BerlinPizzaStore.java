package main.java.com;

public class BerlinPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
        if(type.equals("Salami")){
            return new BerlinSalami();
        }else if(type.equals("Calzone")){
            return new BerlinCalzone();
        }else if(type.equals("QuattroStagioni")){
            return new BerlinQuattroStagioni();
        } else if (type.equals("Hawaii")){
            return new BerlinHawaii();
        }else{
            return null;
        }
    }
}
