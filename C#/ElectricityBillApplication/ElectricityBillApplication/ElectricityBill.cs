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
        public decimal TotalKWH { get; set; }
        public decimal AvgBill { get; set; }

        private List<Customer> m_customerList;

        public ElectricityBill()
        {
            InitializeComponent();
        }

        private void ElectricityBill_Load(object sender, EventArgs e)
        {
            TotalKWH = AvgBill = 0;
            grpbxAddCustomer.Visible = false;
            grpbxData.Visible = false;
            m_customerList = new List<Customer>();
        }

        private void btnAddCustomer_Click(object sender, EventArgs e)
        {
            grpbxAddCustomer.Visible = true;
            grpbxData.Visible = false;
            btnAddCustomer.BackColor = Color.White;
            btnViewCustomer.BackColor = System.Drawing.SystemColors.Control;
            btnResetCustomer_Click(sender, e);
        }

        private void btnResetCustomer_Click(object sender, EventArgs e)
        {
            lblAccountNumberValue.Text = AccountNumber.ToString();
            txtbxFirstName.Text = "";
            txtbxLastName.Text = "";
            txtbxKWHVal.Text = "";
            lblPredictedBillVal.Text = "";
            lblAddCustomerMsg.Text = "";
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
                m_customerList.Add(newCust);
                lstbxCustomers.Items.Add(newCust.ToString());
                AccountNumber++;
                TotalKWH += KWH;

                //Alternate way of calculating Average Bill
                //decimal bill = Customer.ADMINCHARGE + decimal.Parse(txtbxKWHVal.Text) * Customer.USAGECHARGE;
                //AvgBill = (TotalKWH * AvgBill + bill) / Convert.ToDecimal(CustomerNumber);
                //Fast way of calculating due to static costs
                AvgBill = m_customerList.Count * Customer.ADMINCHARGE + TotalKWH * Customer.USAGECHARGE;
                btnResetCustomer_Click(sender, e);
                lblAddCustomerMsg.Text = "Account No " + (AccountNumber - 1).ToString() + " Submitted";
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

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void btnViewCustomer_Click(object sender, EventArgs e)
        {
            grpbxData.Visible = true;
            grpbxAddCustomer.Visible = false;
            btnViewCustomer.BackColor = Color.White;
            btnAddCustomer.BackColor = System.Drawing.SystemColors.Control;

            lblTotalCustomerVal.Text = m_customerList.Count.ToString();
            lblTotalKWHVal.Text = TotalKWH.ToString("F");
            lblAverageBillVal.Text = AvgBill.ToString("C");
        }
    }
}
