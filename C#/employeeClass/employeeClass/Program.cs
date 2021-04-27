using System;

namespace employeeClass
{
    public class Employee
    {
       public Employee(string n, int time, decimal pay)
        {
            name = n;
            hour = time;
            rate = pay;
        }
        public string name { get; set; }
        public int hour { get; set; }
        public decimal rate { get; set; }
        public decimal calcPay()
        {
            return hour * rate;
        }
        public override string ToString()
        {
            return name + " worked " + hour + " at " + rate.ToString("C");
        }
    }

    public class PermanentEmployee : Employee
    {
        public PermanentEmployee(string n, int time, decimal pay, decimal rrsp) :
            base(n, time, pay)
        {
            rrspPercent = rrsp;
        }
        public decimal rrspPercent { get; set; }
        public override string ToString()
        {
            return base.ToString() + " rrsp = " + rrspPercent.ToString("f");
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            PermanentEmployee john = new PermanentEmployee("john", 40, 30.0m, 0.1m);
            Console.WriteLine(john);
            Console.WriteLine(john.calcPay());
            Console.WriteLine(john.rrspPercent);
        }
    }
}
