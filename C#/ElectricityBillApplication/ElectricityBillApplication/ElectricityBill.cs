using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace ElectricityBillApplication
{
    public partial class ElectricityBill : Form
    {
        private long AccountNumber = 1000000000;
        
        public ElectricityBill()
        {
            InitializeComponent();
        }

        private void ElectricityBill_Load(object sender, EventArgs e)
        {
            grpbxAddCustomer.Visible = false;
        }

        private void btnAddCustomer_Click(object sender, EventArgs e)
        {
            grpbxAddCustomer.Visible = true;
            btnAddCustomer.BackColor = Color.White;
            btnResetCustomer_Click(sender, e);
        }

        private void btnResetCustomer_Click(object sender, EventArgs e)
        {
            lblAccountNumberValue.Text = AccountNumber.ToString();
            txtbxFirstName.Text = "";
            txtbxLastName.Text = "";
            txtbxKWHVal.Text = "";
            lblPredictBill.Text = "";
        }
    }
}
