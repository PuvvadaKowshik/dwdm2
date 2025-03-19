import java.util.ArrayList;
import java.util.List;

public class CarsDatasetApp {

    // Car class definition
    public static class Cars_dtset {
        public String car_name;
        public String car_description;
        public int car_no;

        // Constructor
        public Cars_dtset(String car_name, String car_description, int car_no) {
            this.car_name = car_name;
            this.car_description = car_description;
            this.car_no = car_no;
        }
    }

    public static void main(String[] args) {
        // Simulating a dataset of cars
        List<Cars_dtset> carsList = new ArrayList<>();

        // Adding some car instances to the dataset (simulating data rows)
        carsList.add(new Cars_dtset("Toyota Camry", "A mid-size car", 1));
        carsList.add(new Cars_dtset("Honda Civic", "A compact car", 2));
        carsList.add(new Cars_dtset("Ford Mustang", "A sports car", 3));
        carsList.add(new Cars_dtset("Chevrolet Malibu", "A mid-size car", 4));

        // Iterating over the dataset and printing the details of each car
        for (Cars_dtset car : carsList) {
            System.out.println("CarName = " + car.car_name);
            System.out.println("CarDescription = " + car.car_description);
            System.out.println("CarNo = " + car.car_no);
            System.out.println("--------------------------------");
        }
    }
}
