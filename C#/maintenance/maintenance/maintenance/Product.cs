using System;


namespace maintenance
{
    class Product
    {
        public Product(string c, string d, decimal p)
        {
            code = c;
            description = d;
            price = p;
        }
        public string code { get; set; }
        public string description { get; set; }
        public decimal price { get; set; }

        public override string ToString()
        {
            return code + "|" + price.ToString("C") + "|" + description;
        }

    }
}
