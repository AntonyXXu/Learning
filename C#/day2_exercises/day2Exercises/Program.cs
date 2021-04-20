using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace day2Exercises
{
    static class Program
    {
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.SetHighDpiMode(HighDpiMode.SystemAware);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
            string customerType = "R";
            int subtotal = 100;
            decimal discountPercent;

            switch (customerType)
            {
                case "R":
                    if (subtotal < 100)
                    {
                        discountPercent = .0m;
                    }
                    else if (subtotal >= 100 && subtotal < 250)
                    {
                        discountPercent = .1m;
                    }
                    else
                    {
                        discountPercent = .25m;
                    }
                    break;
                case "C":

                    if (subtotal < 250)
                    { discountPercent = .2m; }
                    else
                    {
                        discountPercent = .3m;
                    }
                    break;
                default:
                    discountPercent = .4m;
                    break;
            }
        }
    }
}
