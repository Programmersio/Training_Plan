package modern_java;

import java.util.List;
import java.util.OptionalInt;
import java.util.stream.Collectors;

/**
 * A modernised version of the Example class using generics and streams.
 *
 * This class demonstrates best practices in Java 17: type safety, immutable
 * operations and functional programming constructs.  Unlike the legacy
 * implementation, methods return new collections rather than mutating
 * inputs.
 */
public class Example {

    /**
     * Return a new list containing only even numbers from the input list.
     *
     * @param numbers a list of integers
     * @return a list of even integers
     */
    public List<Integer> filterEvenNumbers(List<Integer> numbers) {
        return numbers.stream()
                .filter(n -> n % 2 == 0)
                .collect(Collectors.toList());
    }

    /**
     * Compute the sum of the numbers in the list.
     *
     * @param numbers a list of integers
     * @return the sum of all numbers
     */
    public int sum(List<Integer> numbers) {
        return numbers.stream()
                .mapToInt(Integer::intValue)
                .sum();
    }

    /**
     * Find the maximum value in the list.
     *
     * @param numbers a list of integers
     * @return an OptionalInt containing the maximum value, or empty if the list is empty
     */
    public OptionalInt max(List<Integer> numbers) {
        return numbers.stream()
                .mapToInt(Integer::intValue)
                .max();
    }
}