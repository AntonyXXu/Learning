using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace maintenance
{
    public class ListofProd : List<Product>
    {
        public void add(Product P)
        {
            base.Add(P);
        }

        //public void fill() Get from database
        //{
        //    List<Product> productList = 
        //}

        //public void save() Save to database
        //{

        //}

    }
}
