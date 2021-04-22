using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tshirts2Darray
{
    public partial class Form1 : Form
    {
        // #Sold of Tshirts
        //Color/Size  S      M       L     XL
        // Black     345   564   1245   1690
        // White    1232  1534    795     238
        // Red      1189  1387    987     546
        int[,] nrSold = { { 345,   564,   1245,   1690},
                          { 1232,  1534,    795,   238},
                          { 1189,  1387,    987,   546}};
        string [] colors = { "Black", "White", "Red" }; // colour names for display
        const int nrColors = 3;
        string[] sizes = { "S", "M", "L", "XL" }; // size names for display
        const int nrSizes = 4;
        int[] colorTotal = new int[nrColors]; // total number of T-shirts sold in each colour
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            CalculateColorTotals();
            DisplaySales();
           
        }

        // for each colour, sum up the sales in various sizes
        private void CalculateColorTotals()
        {
            int sum;
            for(int c =0; c< nrColors; c++) // for each color
            {
                sum = 0;
                for (int s = 0; s < nrSizes; s++)
                    sum += nrSold[c, s];
                colorTotal[c] = sum;
            }
        }

        // returns index of the winning colour
        private int FindWinningColor()
        {
            int winner = 0; // suppose the first color wins
            for (int i = 1; i < nrColors; i++)
                if (colorTotal[i] > colorTotal[winner])
                    winner = i;
            return winner;
        }
        private void DisplaySales()
        {
            string line;
            lstSales.Items.Clear();
            // display the initial data
            lstSales.Items.Add("Sales data");
            lstSales.Items.Add("\tS\tM\tL\tXL");
            for(int c =0; c< nrColors; c++)// for each color
            {
                line = colors[c] + "\t";
                for(int s=0; s < nrSizes; s++) // for each size
                {
                    line += nrSold[c, s].ToString() + "\t";                 
                }
                lstSales.Items.Add(line);
            }
            lstSales.Items.Add("");
            lstSales.Items.Add("Sales summary:");
            // display colour totals
            for(int c=0; c< nrColors;c++)
            {
                line = colors[c] + ":\t " + colorTotal[c];
                lstSales.Items.Add(line);
            }
            // find and display the winning colour
            lstSales.Items.Add("The winning color is " + colors[FindWinningColor()]);
        }
    }
}
