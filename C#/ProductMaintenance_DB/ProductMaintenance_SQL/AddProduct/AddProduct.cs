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

namespace AddProduct
{
    public partial class frmAddProduct : Form
    {
        public Product selectedProduct { get; set; }
        public frmAddProduct()
        {
            InitializeComponent();
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

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
    }
}
