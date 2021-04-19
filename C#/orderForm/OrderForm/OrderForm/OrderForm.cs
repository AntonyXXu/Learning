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
        public readonly string[] Options_1 = { "Lettuce, tomato, and onions", "Pepperoni", "Croutons", };
        public readonly string[] Options_2 = { "Ketchup, mustard, and mayo", "Sausage", "Bacon Bits" };
        public readonly string[] Options_3 = { "French fries", "Olives", "Bread sticks" };
        //Costs for hamburger, pizza, and salad
        public readonly double[] baseCosts = { 6.95, 5.95, 4.95 };
        public readonly double[] addOnCosts = { 0.75, 0.50, 0.25 };
        //Costs ordered by subtotal, tax, total
        public double[] costs = { 0, 0, 0 };
     

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
            lblOrderSubmitted.Text = "Submit your order";
            Array.Clear(costs, 0, 3);
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void radioBurger_CheckedChanged(object sender, EventArgs e)
        {
            costs[0] = baseCosts[0];
            update_Form(0);
            update_Costs();
        }
        private void radioPizza_CheckedChanged(object sender, EventArgs e)
        {
            costs[0] = baseCosts[1];
            update_Form(1);
            update_Costs();
        }
        private void radioSalad_CheckedChanged(object sender, EventArgs e)
        {
            costs[0] = baseCosts[2];
            update_Form(2);
            update_Costs();
        }
        private void update_Form(int radioVal)
        {
            grpbxAddOn.Text = "Add-On Items ($" + addOnCosts[radioVal] + "/item)";
            chkAddOn1.Text = Options_1[radioVal];
            chkAddOn2.Text = Options_2[radioVal];
            chkAddOn3.Text = Options_3[radioVal];
        }
        private void update_Costs()
        {
            costs[1] = Math.Round(costs[0] * 1 / 20, 2);
            costs[2] = costs[0] + costs[1];
            lblSubTotalVal.Text = (costs[0]).ToString("C");
            lblTaxVal.Text = (costs[1]).ToString("C");
            lblTotalCostVal.Text = (costs[2]).ToString("C");
        }

      
    }
}
