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
        //Read Only Text for different add on options
        public readonly string[] Options_1 = { "Lettuce, tomato, and onions", "Pepperoni", "Croutons", };
        public readonly string[] Options_2 = { "Ketchup, mustard, and mayo", "Sausage", "Bacon Bits" };
        public readonly string[] Options_3 = { "French fries", "Olives", "Bread sticks" };
        //Costs for hamburger, pizza, and salad
        public double baseCosts = 6.95;
        public double addOnCosts = 0.75;
        //Costs ordered by subtotal, tax, total
        private bool[] addOns = { false, false, false };
        private double[] costs = { 0, 0, 0 };


        public frmOrderForm()
        {
            InitializeComponent();
        }

        private void btnOrder_Click(object sender, EventArgs e)
        {
            if (lblOrderSubmitted.Text != "Submit your order")
            {
                lblOrderSubmitted.Text = "Click Reset before submitting";
                return;
            }
            lblOrderSubmitted.Text = "Order Submitted!";

        }

        private void frmOrderForm_Load(object sender, EventArgs e)
        {
            lblOrderSubmitted.Text = "Submit your order";
            Array.Clear(costs, 0, 3);
            Array.Clear(addOns, 0, 3);
            chkAddOn1.Checked = chkAddOn2.Checked = chkAddOn3.Checked = false;
            radioBurger.Checked = true;
            radioBurger_CheckedChanged(sender, e);
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void radioBurger_CheckedChanged(object sender, EventArgs e)
        {
            baseCosts = 6.95;
            addOnCosts = 0.75;
            update_Form(0);
            update_Costs();
        }
        private void radioPizza_CheckedChanged(object sender, EventArgs e)
        {
            baseCosts = 5.95;
            addOnCosts = 0.50;
            update_Form(1);
            update_Costs();
        }
        private void radioSalad_CheckedChanged(object sender, EventArgs e)
        {
            baseCosts = 4.95;
            addOnCosts = 0.25;
            update_Form(2);
            update_Costs();
        }
        private void update_Form(int radioVal)
        {
            grpbxAddOn.Text = "Add-On Items ($" + addOnCosts + "/item)";
            chkAddOn1.Text = Options_1[radioVal];
            chkAddOn2.Text = Options_2[radioVal];
            chkAddOn3.Text = Options_3[radioVal];
        }
        private void update_Costs()
        {
            costs[0] = baseCosts;
            for (int i = 0; i < addOns.Length; i++)
            {
                if (addOns[i] == true)
                {
                    costs[0] += addOnCosts;
                }
            }
            costs[1] = Math.Round(costs[0] * 1 / 20, 2);
            costs[2] = costs[0] + costs[1];
            lblSubTotalVal.Text = (costs[0]).ToString("C");
            lblTaxVal.Text = (costs[1]).ToString("C");
            lblTotalCostVal.Text = (costs[2]).ToString("C");
        }

        private void chkAddOn1_CheckedChanged(object sender, EventArgs e)
        {
            addOns[0] = !addOns[0];
            update_Costs();
        }
        private void chkAddOn2_CheckedChanged(object sender, EventArgs e)
        {
            addOns[1] = !addOns[1];
            update_Costs();
        }
        private void chkAddOn3_CheckedChanged(object sender, EventArgs e)
        {
            addOns[2] = !addOns[2];
            update_Costs();
        }
    }
}
