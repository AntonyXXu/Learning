﻿using System;

/********************
 * 
 *  Class Declaration for Customer
 * 
********************/


namespace ElectricityBillApplication
{
    public class Customer
    {
        //Initialize static vars
        public static decimal ADMINCHARGE = 12.0m;
        public static decimal USAGECHARGE = 0.07m;

        //Constructor, autocalculate charges
        public Customer(int Account, string Fname, string Lname, decimal kWh)
        {
            AccountNo = Account;
            FirstName = Fname;
            LastName = Lname;
            KWHUsed = kWh;
            BillAmt = calculateCharge();
        }

        public int AccountNo
        {
            get;
            set;
        }

        public string FirstName
        {
            get;
            set;
        }
        public string LastName
        {
            get;
            set;
        }

        public decimal KWHUsed
        {
            get;
            set;
        }
        public decimal BillAmt
        {
            get;
            set;
        }

        public decimal calculateCharge()
        {
            return ADMINCHARGE + KWHUsed * USAGECHARGE;
        }

        public override string ToString()
        {
            return FirstName +" " + LastName + " used " + KWHUsed.ToString("F") + "KWH and spent " + BillAmt.ToString("C");
        }
    }
}
