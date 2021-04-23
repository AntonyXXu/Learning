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
        private int AccountNumber = 1000000;
        public int CustomerNumber { get; set; }
        public decimal TotalKWH { get; set; }
        public decimal AvgBill { get; set; }


        public ElectricityBill()
        {
            InitializeComponent();
        }

        private void ElectricityBill_Load(object sender, EventArgs e)
        {
            CustomerNumber = 0;
            TotalKWH = AvgBill = 0;
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

        private void txtbxKWHVal_TextChange(object sender, EventArgs e)
        {
            if (txtbxKWHVal.Text == "" || txtbxKWHVal.Text == ".")
            {
                return;
            }
            decimal bill = Customer.ADMINCHARGE + decimal.Parse(txtbxKWHVal.Text) * Customer.USAGECHARGE;
            lblPredictedBillVal.Text = bill.ToString("c");
        }

        private void btnSubmitNewCustomer_Click(object sender, EventArgs e)
        {
            try
            {
                if (checkEmpty(txtbxFirstName) || checkEmpty(txtbxLastName) || checkEmpty(txtbxKWHVal))
                {
                    MessageBox.Show("All Fields must be filled");
                    return;
                }

                int accountNo = Convert.ToInt32(lblAccountNumberValue.Text);
                decimal KWH = decimal.Parse(txtbxKWHVal.Text);
                Customer newCust = new Customer(accountNo, txtbxFirstName.Text, txtbxLastName.Text, KWH);
                AccountNumber++;
                TotalKWH += KWH;
                CustomerNumber++;
                //Realistic way of calculating Average Bill
                AvgBill = (TotalKWH * AvgBill + decimal.Parse(lblPredictedBillVal.Text)) / CustomerNumber;
                //Fast way of calculating due to static costs
                AvgBill = CustomerNumber * Customer.ADMINCHARGE + TotalKWH * Customer.USAGECHARGE;

                btnResetCustomer_Click(sender, e);
            }
            catch
            {
                MessageBox.Show("Input Fields must be valid");
                return;
            }
        }

        private bool checkEmpty(TextBox txtbx)
        {
            return txtbx.Text == "";
        }

        private void txtbxKWHVal_KeyPress(object sender, KeyPressEventArgs e)
        {
                        if (!char.IsDigit(e.KeyChar) && e.KeyChar != '.' && !char.IsControl(e.KeyChar))
            {
                e.Handled = true;
            }
            if (e.KeyChar == '.' && txtbxKWHVal.Text.Contains('.'))
            {
                e.Handled = true;
            }
        }
    }
}
