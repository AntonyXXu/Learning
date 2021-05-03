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

namespace ModifyProduct
{
    public partial class frmModifyProduct : Form
    {
        public Product selectedProduct { get; set; }
        public frmModifyProduct()
        {
            InitializeComponent();
        }

        private void frmModifyProduct_Load(object sender, EventArgs e)
        {
            txtName.Text = selectedProduct.Name;
            txtProductCode.Text = selectedProduct.ProductCode;
            txtVersion.Text = selectedProduct.Version.ToString("0.0");
        }
    }
}
