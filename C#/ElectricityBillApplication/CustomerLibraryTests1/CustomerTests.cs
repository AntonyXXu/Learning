using Microsoft.VisualStudio.TestTools.UnitTesting;
using ElectricityBillApplication;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ElectricityBillApplication
{
    [TestClass()]
    public class CustomerTests
    {
        [TestMethod()]
        public void CustomerTest()
        {
            //Arrange
            int account = 1;
            string fname = "abc";
            string lname = "def";
            int kwh = 1000;

            //Act
            Customer cust = new Customer(account, fname, lname, kwh);

            //Assert          
            Assert.AreEqual(1000, cust.KWHUsed);
            Assert.AreEqual("abc", cust.FirstName);
            Assert.AreEqual("def", cust.LastName);
            Assert.AreEqual(1, cust.AccountNo);
        }

        [TestMethod()]
        public void calculateChargeTest()
        {
            //Arrange
            int account = 2;
            string fname = "a";
            string lname = "b";
            decimal kwh1 = 1000m;
            decimal kwh2 = 12.3m;
            decimal kwh3 = 0.5m;
            decimal exp1 = 1000m * 0.07m + 12;
            decimal exp2 = 12.3m * 0.07m + 12;
            decimal exp3 = 0.5m * 0.07m + 12;


            //Act
            Customer cust = new Customer(account, fname, lname, kwh1);
            decimal charge1 = cust.calculateCharge();
            cust = new Customer(account, fname, lname, kwh2);
            decimal charge2 = cust.calculateCharge();
            cust = new Customer(account, fname, lname, kwh3);
            decimal charge3 = cust.calculateCharge();

            //Assert
            Assert.AreEqual(1, charge1);
            Assert.AreEqual(exp2, charge2);
            Assert.AreEqual(exp3, charge3);
        }

    }
}