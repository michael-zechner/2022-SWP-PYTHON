package main.java.com;

public class RostockPizzaStore extends PizzaStore {

    @Override
    Pizza createPizza(String type) {
        // if(type.equals("Salami")){
        //     return new RostockSalami();
        // }else if(type.equals("Calzone")){
        //     return new RostockCalzone();
        // }else if(type.equals("QuattroStagioni")){
        //     return new RostockQuattroStagioni();
        // } else if (type.equals("Hawaii")){
        //     return new RostockHawaii();
        // }else{
        //     return null;
        // }
        switch(type){
            case "Salami": return new RostockSalami();
            case "Calzone": return new RostockCalzone();
            case "QuattroStagioni": return new RostockQuattroStagioni();
            case "Hawaii": return new RostockHawaii();
            default: return null;
        }
    }
}