import java.util.*;

public class AprioriAlgorithm {
    private static final double MIN_SUPPORT = 0.5; // Minimum support threshold
    private static final int MIN_SUPPORT_COUNT = 2; // Minimum support count for frequent itemsets

    public static void main(String[] args) {
        // Sample transactions (Dataset)
        List<Set<String>> transactions = new ArrayList<>();
        transactions.add(new HashSet<>(Arrays.asList("Milk", "Bread", "Butter")));
        transactions.add(new HashSet<>(Arrays.asList("Milk", "Bread")));
        transactions.add(new HashSet<>(Arrays.asList("Milk", "Butter")));
        transactions.add(new HashSet<>(Arrays.asList("Bread", "Butter")));
        transactions.add(new HashSet<>(Arrays.asList("Milk", "Bread", "Butter", "Eggs")));

        // Run Apriori algorithm
        List<Set<String>> frequentItemsets = apriori(transactions);
        
        // Output frequent itemsets
        System.out.println("\nFrequent Itemsets:");
        for (Set<String> itemset : frequentItemsets) {
            System.out.println(itemset);
        }
    }

    public static List<Set<String>> apriori(List<Set<String>> transactions) {
        List<Set<String>> frequentItemsets = new ArrayList<>();
        Map<Set<String>, Integer> itemsetCountMap = new HashMap<>();

        // Generate 1-item frequent sets
        Set<String> allItems = new HashSet<>();
        for (Set<String> transaction : transactions) {
            allItems.addAll(transaction);
        }

        // Create initial candidate itemsets
        List<Set<String>> candidates = new ArrayList<>();
        for (String item : allItems) {
            Set<String> singleItemSet = new HashSet<>();
            singleItemSet.add(item);
            candidates.add(singleItemSet);
        }

        // Iterate to find larger itemsets
        while (!candidates.isEmpty()) {
            itemsetCountMap.clear();

            // Count occurrences of candidate itemsets
            for (Set<String> transaction : transactions) {
                for (Set<String> candidate : candidates) {
                    if (transaction.containsAll(candidate)) {
                        itemsetCountMap.put(candidate, itemsetCountMap.getOrDefault(candidate, 0) + 1);
                    }
                }
            }

            // Filter candidates by support threshold
            candidates.clear();
            for (Map.Entry<Set<String>, Integer> entry : itemsetCountMap.entrySet()) {
                if (entry.getValue() >= MIN_SUPPORT_COUNT) {
                    frequentItemsets.add(entry.getKey());
                    candidates.add(entry.getKey());
                }
            }

            // Generate new candidate itemsets by combining previous frequent itemsets
            candidates = generateNewCandidates(candidates);
        }

        return frequentItemsets;
    }

    private static List<Set<String>> generateNewCandidates(List<Set<String>> previousFrequentItemsets) {
        List<Set<String>> newCandidates = new ArrayList<>();

        for (int i = 0; i < previousFrequentItemsets.size(); i++) {
            for (int j = i + 1; j < previousFrequentItemsets.size(); j++) {
                Set<String> unionSet = new HashSet<>(previousFrequentItemsets.get(i));
                unionSet.addAll(previousFrequentItemsets.get(j));

                if (unionSet.size() == previousFrequentItemsets.get(i).size() + 1) {
                    newCandidates.add(unionSet);
                }
            }
        }

        return newCandidates;
    }
}
