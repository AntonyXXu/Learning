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

// Main Form Module to display all products. 
// Also can delete products, and open add/modify forms

namespace ProductMaintenance
{
    public partial class frmProductMaintenance : Form
    {
        //Context declaration
        TechSupportContext contextTS = new TechSupportContext();

        public frmProductMaintenance()
        {
            InitializeComponent();
        }

        //Initialize loading
        private void frmProductMaintenance_Load(object sender, EventArgs e)
        {
            TechSupportContext.connectString =
                ConfigurationManager.ConnectionStrings["TechSupport"].ConnectionString;
            display();
        }

        // Display DB data
        private void display()
        {
            lstbxProducts.DataSource = contextTS.Products.ToList();
        }

        // Return the current product for editing
        private Product getCurrent()
        {
            string ProdID = lstbxProducts.SelectedItem.ToString().Substring(0, 15).Trim();
            return contextTS.Products.Find(ProdID);
        }

        //Open the add product box. upon close, update the view
        private void btnAdd_Click(object sender, EventArgs e)
        {
            AddProduct.frmAddProduct add = new AddProduct.frmAddProduct();
            add.context = contextTS;
            add.ShowDialog();
            display();
        }

        // open the modify box. upon close, update the view
        private void btnModify_Click(object sender, EventArgs e)
        {
            ModifyProduct.frmModifyProduct mod = new ModifyProduct.frmModifyProduct();
            mod.selectedProduct = getCurrent();
            mod.context = contextTS;
            mod.ShowDialog();
            display();
        }

        // close app
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        // delete from the database, and update view
        private void btnDelete_Click(object sender, EventArgs e)
        {
            Product selected = getCurrent();
            contextTS.Products.Remove(selected);
            contextTS.SaveChanges();
            display();
        }
    }
}
