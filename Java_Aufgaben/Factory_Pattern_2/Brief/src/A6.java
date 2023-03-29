public class A6 implements Envelope {

    private double weight;

    public A6(double weight) {
        this.weight = weight;
    }

    @Override
    public double getWeight() {
        return weight;
    }
    @Override
    public String getSize() {
        return "A6";
    }
}
