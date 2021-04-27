using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace maintenance
{
    public class Software: Product
    {
        public Software(string code, string desc, string vers, decimal price):
            base (code, desc, price)
        {
            version = vers;
        }
        public string version { get; set; }

        public override string ToString()
        {
            return base.ToString() + "|" + version;
        }
    }
}
