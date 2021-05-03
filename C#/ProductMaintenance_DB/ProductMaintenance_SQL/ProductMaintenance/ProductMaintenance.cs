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
using System.Configuration;

namespace ProductMaintenance
{
    public partial class frmProductMaintenance : Form
    {
        TechSupportContext contextTS;
        
        public frmProductMaintenance()
        {
            InitializeComponent();
        }

        private void frmProductMaintenance_Load(object sender, EventArgs e)
        {
            contextTS = new TechSupportContext();
            TechSupportContext.connectString =
                ConfigurationManager.ConnectionStrings["TechSupport"].ConnectionString;
            display();
        }

        private void display()
        {
            lstbxProducts.DataSource = contextTS.Products.ToList();
        }

        private Product getCurrent()
        {
            string ProdID = lstbxProducts.SelectedItem.ToString().Substring(0, 15).Trim();
            return contextTS.Products.Find(ProdID);
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            Product selectedProd = getCurrent();
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
