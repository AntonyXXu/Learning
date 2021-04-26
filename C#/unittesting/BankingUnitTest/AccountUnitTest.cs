using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Banking;

namespace BankingUnitTest
{
    [TestClass]
    public class AccountUnitTest
    {
        // constructor - positive initial balance
        [TestMethod]
        public void TestConstructorPositiveInitial()
        {
            // Arrange
            decimal initial = 100;
            decimal expectedBalance = 100;
            decimal actualBalance;
            Account acct;

            // Act
            acct = new Account(initial);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
        }

        // constructor - negative initial balance
        [TestMethod]
        public void TestConstructorNegativeInitial()
        {
            // Arrange
            decimal initial = -100;
            decimal expectedBalance = 0;
            decimal actualBalance;
            Account acct;

            // Act
            acct = new Account(initial);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
        }

        // constructor - zero initial balance
        [TestMethod]
        public void TestConstructorZeroInitial()
        {
            // Arrange
            decimal initial = 0;
            decimal expectedBalance = 0;
            decimal actualBalance;
            Account acct;

            // Act
            acct = new Account(initial);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
        }


        // Deposit - positive amount
        [TestMethod]
        public void TestDepositPositiveAmount()
        {
            // Arrange
            Account acct = new Account(500);
            decimal amount = 100;
            decimal expectedBalance = 600;
            decimal actualBalance;


            // Act
            acct.Deposit(amount);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
        }


        // Deposit - negative amount 
        [TestMethod]
        public void TestDepositNegativeAmount()
        {
            // Arrange
            Account acct = new Account(500);
            decimal amount = -100;
            decimal expectedBalance = 500;
            decimal actualBalance;


            // Act
            acct.Deposit(amount);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
        }


        // Deposit - zero amount
        [TestMethod]
        public void TestDepositZeroAmount()
        {
            // Arrange
            Account acct = new Account(500);
            decimal amount = 0;
            decimal expectedBalance = 500;
            decimal actualBalance;


            // Act
            acct.Deposit(amount);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
        }

        // Withdraw - positive amount that is <= balance
        [TestMethod]
        public void TestWithdrawPositiveAmountSuccess()
        {
            // Arrange
            Account acct = new Account(500);
            decimal amount = 100;
            decimal expectedBalance = 400;
            bool expectedResult = true;
            decimal actualBalance;
            bool actualResult;

            // Act
            actualResult = acct.Withdraw(amount);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
            Assert.AreEqual(expectedResult, actualResult);
        }

        // Withdraw - positive amount that is > balance
        [TestMethod]
        public void TestWithdrawPositiveAmountFailure()
        {
            // Arrange
            Account acct = new Account(500);
            decimal amount = 600;
            decimal expectedBalance = 500;
            bool expectedResult = false;
            decimal actualBalance;
            bool actualResult;

            // Act
            actualResult = acct.Withdraw(amount);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
            Assert.AreEqual(expectedResult, actualResult);
        }


        // Withdraw - negative amount
        [TestMethod]
        public void TestWithdrawNegativeAmount()
        {
            // Arrange
            Account acct = new Account(500);
            decimal amount = -100;
            decimal expectedBalance = 500;
            bool expectedResult = true;
            decimal actualBalance;
            bool actualResult;

            // Act
            actualResult = acct.Withdraw(amount);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
            Assert.AreEqual(expectedResult, actualResult);
        }


        // Withdraw - zero amount
        [TestMethod]
        public void TestWithdrawZeroAmount()
        {
            // Arrange
            Account acct = new Account(500);
            decimal amount = 0;
            decimal expectedBalance = 500;
            bool expectedResult = true;
            decimal actualBalance;
            bool actualResult;

            // Act
            actualResult = acct.Withdraw(amount);
            actualBalance = acct.Balance;

            // Assert
            Assert.AreEqual(expectedBalance, actualBalance);
            Assert.AreEqual(expectedResult, actualResult);
        }

    }
}
