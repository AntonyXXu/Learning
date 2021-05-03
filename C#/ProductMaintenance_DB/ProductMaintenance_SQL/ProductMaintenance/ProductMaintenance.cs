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
        TechSupportContext contextTS = new TechSupportContext();

        public frmProductMaintenance()
        {
            InitializeComponent();
        }

        private void frmProductMaintenance_Load(object sender, EventArgs e)
        {
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
            AddProduct.frmAddProduct add = new AddProduct.frmAddProduct();
            add.context = contextTS;
            add.ShowDialog();
            display();
        }

        private void btnModify_Click(object sender, EventArgs e)
        {
            ModifyProduct.frmModifyProduct mod = new ModifyProduct.frmModifyProduct();
            mod.selectedProduct = getCurrent();
            mod.context = contextTS;
            mod.ShowDialog();
            display();
        }
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            Product selected = getCurrent();
            contextTS.Products.Remove(selected);
            contextTS.SaveChanges();
            display();
        }
    }
}
