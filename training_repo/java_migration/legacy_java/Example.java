package legacy_java;

import java.util.ArrayList;
import java.util.List;

/**
 * A legacy Java class demonstrating old‑style code patterns.
 *
 * This class contains a method that filters even numbers from a list of
 * integers using raw collections and manual iteration.  It modifies the
 * input list in place rather than returning a new list.  Use this file to
 * practise migrating legacy code to modern Java features such as generics,
 * streams and Optional.
 */
public class Example {

    /**
     * Remove all odd numbers from the list.
     *
     * @param numbers a list of integers (raw type to simulate legacy code)
     */
    public void filterEvenNumbers(List numbers) {
        // Use a traditional for loop and cast objects manually
        for (int i = 0; i < numbers.size(); i++) {
            Object obj = numbers.get(i);
            if (obj instanceof Integer) {
                int value = ((Integer) obj).intValue();
                if (value % 2 != 0) {
                    numbers.remove(i);
                    i--; // adjust index after removal
                }
            }
        }
    }

    /**
     * Sum the values in the list.
     *
     * @param numbers a list of integers (raw type)
     * @return the sum of all numbers
     */
    public int sum(List numbers) {
        int total = 0;
        for (int i = 0; i < numbers.size(); i++) {
            Object obj = numbers.get(i);
            if (obj instanceof Integer) {
                total += ((Integer) obj).intValue();
            }
        }
        return total;
    }
}