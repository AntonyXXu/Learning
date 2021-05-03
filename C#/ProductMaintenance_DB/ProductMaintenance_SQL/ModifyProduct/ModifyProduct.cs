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
            txtName.Text = selectedProduct.Name.Trim();
            txtProductCode.Text = selectedProduct.ProductCode.Trim();
            txtVersion.Text = selectedProduct.Version.ToString("0.0").Trim();
            dateRelease.Value = selectedProduct.ReleaseDate;
        }

        private void btnModify_Click(object sender, EventArgs e)
        {
            selectedProduct.Name = txtName.Text.Trim();
            selectedProduct.ProductCode = txtProductCode.Text.Trim();
            selectedProduct.Version = Convert.ToDecimal(txtVersion.Text.Trim());
            selectedProduct.ReleaseDate = dateRelease.Value;
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void txtProductCode_KeyPress(object sender, KeyPressEventArgs e)
        {
            textLength(sender, e, 10);
        }

        private void txtName_KeyPress(object sender, KeyPressEventArgs e)
        {
            textLength(sender, e, 18);
        }
        private void txtVersion_KeyPress(object sender, KeyPressEventArgs e)
        {
            textLength(sender, e, 18);
        }

        private void textLength(object sender, KeyPressEventArgs e, int limit)
        {
            if (this.Text.Length > limit)
            {
                e.Handled = true;
            }
        }

    }
}
