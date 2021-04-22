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

        public frmOrderForm()
        {
            InitializeComponent();
        }

        //Costs for hamburger, pizza, and salad
        private double baseCosts = 6.95;
        private double addOnCosts = 0.75;
        //Costs ordered by subtotal, tax, total
        private bool[] addOns = { false, false, false };
        private double[] costs = { 0, 0, 0 };

        private void btnOrder_Click(object sender, EventArgs e)
        {
            //Check if the form was reset. If it is, allow for submission
            if (lblOrderSubmitted.Text != "Submit your order")
            {
                lblOrderSubmitted.Text = "Click Reset before submitting";
                return;
            }
            lblOrderSubmitted.Text = "Order Submitted!";

        }

        private void frmOrderForm_Load(object sender, EventArgs e)
        {
            //initialize all variables and states
            lblOrderSubmitted.Text = "Submit your order";

            Array.Clear(costs, 0, 3);

            radioBurger.Checked = true;
            radioBurger_CheckedChanged(sender, e);
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            //Close application
            Application.Exit();
        }

        private void radioBurger_CheckedChanged(object sender, EventArgs e)
        {
            //initialize base costs and add on costs. Update the form based on selection
            baseCosts = 6.95;
            addOnCosts = 0.75;
            update_Form(0);
            update_Costs();
        }
        private void radioPizza_CheckedChanged(object sender, EventArgs e)
        {
            //initialize base costs and add on costs. Update the form based on selection
            baseCosts = 5.95;
            addOnCosts = 0.50;
            update_Form(1);
            update_Costs();
        }
        private void radioSalad_CheckedChanged(object sender, EventArgs e)
        {
            //initialize base costs and add on costs. Update the form based on selection
            baseCosts = 4.95;
            addOnCosts = 0.25;
            update_Form(2);
            update_Costs();
        }
        private void update_Form(int radioVal)
        {
            //Update add on form contents based on radio passed var
            chkAddOn1.Checked = chkAddOn2.Checked = chkAddOn3.Checked = false;
            Array.Clear(addOns, 0, 3);
            grpbxAddOn.Text = "Add-On Items (" + addOnCosts.ToString("c") + "/item)";
            chkAddOn1.Text = Options_1[radioVal];
            chkAddOn2.Text = Options_2[radioVal];
            chkAddOn3.Text = Options_3[radioVal];
        }
        private void update_Costs()
        {
            //Update costs based on current selections
            costs[0] = baseCosts;
            for (int i = 0; i < addOns.Length; i++)
            {
                if (addOns[i] == true)
                {
                    costs[0] += addOnCosts;
                }
            }
            //Calculate the tax rate
            costs[1] = Math.Round(costs[0] * 1 / 20, 2);
            //Calculate total cost
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
