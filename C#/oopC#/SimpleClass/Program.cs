using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SimpleClass
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("\nCreating one object:");
            Product p1 = new Product(); // all values are defaults
            Console.WriteLine(p1);

            p1.Name = "gadget";
            p1.Price = 9.99m;
            p1.Quantity = 25;

            //Product p1 = new Product("gadget", 9.99m, 25);
            Console.WriteLine(p1); // ToString is called implicitly
            //decimal inventory = p1.InventoryValue();

            //p1.SetName("small gadget");
            p1.Name = "small gadget";
            //Console.WriteLine("Changing name of p1 to " + p1.GetName());
            Console.WriteLine("Changing name of p1 to " + p1.Name);
            Console.WriteLine(p1);

            Console.WriteLine("\nCreating another object:");
            Product p2 = new Product("widget", 7.99m, 30);
            Console.WriteLine(p2);
            //inventory += p2.InventoryValue();

            p1.Price = 12.99m;
            Console.WriteLine("\nChanging price of p1 to " + p1.Price);
            Console.WriteLine(p1);

            //Console.WriteLine("\n\nInventory value: " + inventory.ToString());

            Console.WriteLine("\n\nCreating third product:");
            //Product p3 = p1;
            Product p3 = p1.Clone(); // make a clone of p1
            Console.WriteLine(p1);
            Console.WriteLine(p2);
            Console.WriteLine(p3);

            Console.WriteLine("\n\nChanging price of p3:");
            p3.Price = 5.99m;
            Console.WriteLine(p1);
            Console.WriteLine(p2);
            Console.WriteLine(p3);

            Console.WriteLine("\n\nPutting all products into a list: ");
            List<Product> myProds = new List<Product>(); // makes an empty list
            Console.WriteLine("Empty list has " + myProds.Count + " elements");
            myProds.Add(p1);
            myProds.Add(p2);
            myProds.Add(p3);
            Console.WriteLine("Now the list has " + myProds.Count + " elements");
            foreach (Product p in myProds)
                Console.WriteLine(p);

            decimal totalInventory = 0;
            foreach (Product p in myProds)
            {
                totalInventory += p.InventoryValue();
            }
            Console.WriteLine("\nTotal inventory is " + totalInventory.ToString("c"));

            Console.WriteLine("\n\nPress any key");
            Console.ReadKey();
        }
    }
}
