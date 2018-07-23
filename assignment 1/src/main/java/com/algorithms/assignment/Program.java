package com.algorithms.assignment;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Program {

    public static void main(String[] args) throws FileNotFoundException {
        String dataSet = "set1";
        String dataFile = "data_1";

        long[] insertNumbers = getNumbers(new File(BST.class.getResource("/data-sets/insert/" + dataSet + "/" + dataFile + ".txt").getFile()));
        long[] searchNumbers = getNumbers(new File(BST.class.getResource("/data-sets/search/" + dataSet + "/" + dataFile + ".txt").getFile()));
        long[] deleteNumbers = getNumbers(new File(BST.class.getResource("/data-sets/delete/" + dataSet + "/" + dataFile + ".txt").getFile()));

        BST.calculate(insertNumbers, searchNumbers, deleteNumbers);
        SplayBST.calculate(insertNumbers, searchNumbers, deleteNumbers);
        RedBlackBST.calculate(insertNumbers, searchNumbers, deleteNumbers);
    }

    private static long[] getNumbers(File file) throws FileNotFoundException {
        Scanner scanner = new Scanner(file);

        ArrayList<Long> numbers = new ArrayList<>();

        while (scanner.hasNext()) {
            for (String s : scanner.nextLine().split(",")) {
                numbers.add(Long.parseLong(s));
            }
        }

        scanner.close();

        int size = numbers.size();

        long[] numbersFinal = new long[numbers.size()];

        for (int i = 0; i < size; i++) {
            numbersFinal[i] = numbers.get(i);
        }

        return numbersFinal;
    }
}
