using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace maintenance
{
    public class Book :  Product
    {
        public Book (string c, string desc, string auth, decimal price):
            base (c, desc, price)
        {
            author = auth;
        }

        public string author { get; set; }

        public override string ToString()
        {
            return base.ToString() + "|" + author;
        }
    }
}
