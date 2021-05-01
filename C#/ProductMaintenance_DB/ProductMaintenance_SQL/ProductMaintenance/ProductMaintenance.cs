using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ProductMaintenance.Models;

namespace ProductMaintenance
{
    public partial class frmProductMaintenance : Form
    {
        TechSupportContext contextTS;
        Product currProduct;

        public frmProductMaintenance()
        {
            InitializeComponent();
        }

        private void frmProductMaintenance_Load(object sender, EventArgs e)
        {
            contextTS = new TechSupportContext();
            currProduct = contextTS.Products.First();   //Select the first customer
            lstbxProducts.DataSource = contextTS.Products.ToList();

        }

        private void lstbxProducts_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
