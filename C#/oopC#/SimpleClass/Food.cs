using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SimpleClass
{
    class Food
    {
        public string Name { get; set; }
        public decimal Price { get; set; }
        public DateTime Expiry { get; set; }

        public Food(string name, decimal price, DateTime expiry)
            {
            Name = name;
            Price = price;
            Expiry = expiry;
            Console.WriteLine("constructor called");
        }

        public override string ToString()
        {
            return Name + "," + Price.ToString() + ", " + Expiry.ToString("M");
        }
    }
}
