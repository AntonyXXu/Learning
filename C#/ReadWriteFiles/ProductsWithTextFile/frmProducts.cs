using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ProductsWithTextFile
{
    public partial class frmProducts : Form
    {
        const string path = "products.txt";
        const int MAX_SIZE = 100;
        string[] names = new string[MAX_SIZE];
        decimal[] prices = new decimal[MAX_SIZE];
        int howMany = 0; // actual number of products
        public frmProducts()
        {
            InitializeComponent();
        }


        private void frmProducts_Load(object sender, EventArgs e)
        {
            ReadProducts();
            DisplayProducts();
        }

        private void ReadProducts()
        {
            FileStream fs = null;
            StreamReader sr = null;
            string line;
            string[] parts;
            try
            {
                // open the file for reading (the very first time, the file does not exist)
                fs = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Read);
                sr = new StreamReader(fs);
                // read data
                while(!sr.EndOfStream) // while there is still data
                {
                    line = sr.ReadLine();
                    parts = line.Split(','); // split where commas are
                    // store data in the arrays
                    names[howMany] = parts[0];
                    prices[howMany] = Convert.ToDecimal(parts[1]);
                    howMany++;
                }
                
            }
            catch(Exception ex)
            {
                MessageBox.Show("Error while reading data: " + ex.Message, ex.GetType().ToString());
            }
            finally
            {
                if (sr != null) sr.Close();
            }

        }
         private void SaveProducts()
        {
            FileStream fs = null;
            StreamWriter sw = null;
            string line;
            try
            {
                // open the file for writing; overwrite old content
                fs = new FileStream(path, FileMode.Create, FileAccess.Write);
                sw = new StreamWriter(fs);

                // save data
                for(int i = 0; i < howMany; i++) // for each product
                {
                    line = names[i] + ", " + prices[i].ToString();
                    sw.WriteLine(line);
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show("Error while writing data: " + ex.Message, ex.GetType().ToString());
            }
            finally
            {
                if (sw != null) sw.Close();
            }
        }

        private void DisplayProducts()
        {
            lstProducts.Items.Clear(); // start with empty list box
            for(int i=0; i<howMany; i++) // for each product
            {
                lstProducts.Items.Add(names[i] + ":\t" + prices[i].ToString("c"));
            }
            lblNrProducts.Text = howMany.ToString();
        }

        private void frmProducts_FormClosing(object sender, FormClosingEventArgs e)
        {
            SaveProducts();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            // get inputs and store in the arrays
            names[howMany] = txtName.Text;
            prices[howMany] = Convert.ToDecimal(txtPrice.Text);
            howMany++;
            // re-display products
            DisplayProducts();
        }
    }
}
