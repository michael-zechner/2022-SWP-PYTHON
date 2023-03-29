public class A5 implements Envelope{

    private double weight;

    public A5(double weight) {
        this.weight = weight;
    }

    @Override
    public double getWeight() {
        return weight;
    }
    @Override
    public String getSize() {
        return "A5";
    }
}
