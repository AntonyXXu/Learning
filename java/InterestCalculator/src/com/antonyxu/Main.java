package com.antonyxu;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final int MONTHS = 12;
        final int PERCENT = 100;

        Scanner scanner = new Scanner(System.in);
        System.out.println("Principal: \t");
        int principal = scanner.nextInt();

        System.out.println("Interest: \t");
        double annualInterest = scanner.nextDouble();
        double monthlyInterest = annualInterest / MONTHS;

        System.out.println("Years: \t");
        int years = scanner.nextInt();


        double mortgage = Math.pow(1+monthlyInterest / 100, years) * principal;
        System.out.println("Mortgage: \t " + mortgage);
    }
}
