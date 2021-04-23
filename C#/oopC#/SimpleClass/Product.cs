using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SimpleClass
{
    public class Product
    {
        // private data
        private string name;
        private decimal price;
        private int quantity;

        // class constructor(s)
        //public Product() { }
        public Product(string n = "unknown", decimal p = 0, int q = 1)
        {
            name = n;
            Price = p;
            Quantity = q;
        }

        // public properties
        public decimal Price
        {
            get
            {
                return price;
            }
            set
            {
                if(value >= 0)
                {
                    price = value;
                }
                else // when negative, take absolute value
                {
                    price = Math.Abs(value);
                }
            }
        }

        public int Quantity
        {
            get
            {
                return quantity;
            }
            set
            {
                if (value >= 0)
                {
                    quantity = value;
                }
                else // when negative, take absolute value
                {
                    quantity = Math.Abs(value);
                }
            }
        }
        public string Name
        {
            get // read access
            {
                return name;
            }
            set // write access
            {
                name = value;
            }
        }
        //public string GetName()
        //{
        //    return name;
        //}

        //public void SetName(string value)
        //{
        //    name = value;
        //}

        // public methods
        public decimal InventoryValue()
        {
            return price * quantity;
        }

        // redefine (override) method ToString that was inheritted from object class
        public override string ToString()
        {
            return name + ": " + price.ToString("c") + ", " + quantity.ToString();
        }

        // create an independent object identical to this one
        public Product Clone()
        {
            return new Product(name, price, quantity);
        }
    }
}
