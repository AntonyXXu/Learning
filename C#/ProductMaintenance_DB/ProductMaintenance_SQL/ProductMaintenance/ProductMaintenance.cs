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
            ModifyProduct.frmModifyProduct add = new ModifyProduct.frmModifyProduct();
            add.selectedProduct = getCurrent();
            add.ShowDialog();
        }

        private void btnModify_Click(object sender, EventArgs e)
        {
            ModifyProduct.frmModifyProduct mod = new ModifyProduct.frmModifyProduct();
            mod.selectedProduct = getCurrent();
            mod.ShowDialog();
        }
        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }


    }
}
