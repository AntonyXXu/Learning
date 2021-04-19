using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace OrderForm
{
    public partial class frmOrderForm : Form
    {
        public frmOrderForm()
        {
            InitializeComponent();
        }

        private void btnOrder_Click(object sender, EventArgs e)
        {
            lblOrderSubmitted.Text = "Order Submitted!";
        }

        private void frmOrderForm_Load(object sender, EventArgs e)
        {
            radioBurger.Checked = true;
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        
    }
}
