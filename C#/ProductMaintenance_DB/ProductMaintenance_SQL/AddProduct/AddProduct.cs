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

// Add product form

namespace AddProduct
{

    public partial class frmAddProduct : Form
    {
        //declaration of context
        public TechSupportContext context { get; set; }
        public frmAddProduct()
        {
            InitializeComponent();
            txtMsg.Text = "Add a Product!";
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // version text validator
        private void txtVersion_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsDigit(e.KeyChar)
             && e.KeyChar != '.'
             && !char.IsControl(e.KeyChar))
            {
                e.Handled = true;
            }
            else if (e.KeyChar == '.' && txtVersion.Text.Contains('.'))
            {
                e.Handled = true;
            }
        }

        // save new product into the database
        private void btnAdd_Click(object sender, EventArgs e)
        {
            Product newProd = new Product();
            newProd.Name = txtName.Text.Trim();
            newProd.ProductCode = txtProductCode.Text.Trim();
            newProd.Version = Convert.ToDecimal(txtVersion.Text.Trim());
            newProd.ReleaseDate = dateRelease.Value;
            if (newProd.Name == "" || newProd.ProductCode == "" || txtVersion.Text.Trim() == "")
            {
                MessageBox.Show("No Fields can be Empty");
            }
            
            context.Products.Add(newProd);
            context.SaveChanges();
            txtMsg.Text = "New Product Added!";
        }

    
    }
}
