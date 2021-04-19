
namespace OrderForm
{
    partial class frmOrderForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.grpbxAddOn = new System.Windows.Forms.GroupBox();
            this.chkAddOn2 = new System.Windows.Forms.CheckBox();
            this.chkAddOn3 = new System.Windows.Forms.CheckBox();
            this.chkAddOn1 = new System.Windows.Forms.CheckBox();
            this.grpbxOrderTotals = new System.Windows.Forms.GroupBox();
            this.txtTotalCost = new System.Windows.Forms.TextBox();
            this.txtTax = new System.Windows.Forms.TextBox();
            this.txtSubtotal = new System.Windows.Forms.TextBox();
            this.lblTotalCost = new System.Windows.Forms.Label();
            this.lblTax = new System.Windows.Forms.Label();
            this.lblSubtotal = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.btnOrder = new System.Windows.Forms.Button();
            this.btnReset = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.lblOrderSubmitted = new System.Windows.Forms.Label();
            this.radioBurger = new System.Windows.Forms.RadioButton();
            this.radioPizza = new System.Windows.Forms.RadioButton();
            this.radioSalad = new System.Windows.Forms.RadioButton();
            this.grpbxMainCourse = new System.Windows.Forms.GroupBox();
            this.grpbxAddOn.SuspendLayout();
            this.grpbxOrderTotals.SuspendLayout();
            this.grpbxMainCourse.SuspendLayout();
            this.SuspendLayout();
            // 
            // grpbxAddOn
            // 
            this.grpbxAddOn.Controls.Add(this.chkAddOn2);
            this.grpbxAddOn.Controls.Add(this.chkAddOn3);
            this.grpbxAddOn.Controls.Add(this.chkAddOn1);
            this.grpbxAddOn.Location = new System.Drawing.Point(389, 34);
            this.grpbxAddOn.Name = "grpbxAddOn";
            this.grpbxAddOn.Size = new System.Drawing.Size(200, 109);
            this.grpbxAddOn.TabIndex = 0;
            this.grpbxAddOn.TabStop = false;
            this.grpbxAddOn.Text = "Add On Items ($0.75/item)";
            // 
            // chkAddOn2
            // 
            this.chkAddOn2.AutoSize = true;
            this.chkAddOn2.Location = new System.Drawing.Point(6, 47);
            this.chkAddOn2.Name = "chkAddOn2";
            this.chkAddOn2.Size = new System.Drawing.Size(156, 19);
            this.chkAddOn2.TabIndex = 0;
            this.chkAddOn2.Text = "Ketchup, Mayo, Mustard";
            this.chkAddOn2.UseVisualStyleBackColor = true;
            // 
            // chkAddOn3
            // 
            this.chkAddOn3.AutoSize = true;
            this.chkAddOn3.Location = new System.Drawing.Point(6, 72);
            this.chkAddOn3.Name = "chkAddOn3";
            this.chkAddOn3.Size = new System.Drawing.Size(89, 19);
            this.chkAddOn3.TabIndex = 0;
            this.chkAddOn3.Text = "French Fries";
            this.chkAddOn3.UseVisualStyleBackColor = true;
            // 
            // chkAddOn1
            // 
            this.chkAddOn1.AutoSize = true;
            this.chkAddOn1.Location = new System.Drawing.Point(6, 22);
            this.chkAddOn1.Name = "chkAddOn1";
            this.chkAddOn1.Size = new System.Drawing.Size(150, 19);
            this.chkAddOn1.TabIndex = 0;
            this.chkAddOn1.Text = "Lettuce, Tomato, Onion";
            this.chkAddOn1.UseVisualStyleBackColor = true;
            // 
            // grpbxOrderTotals
            // 
            this.grpbxOrderTotals.Controls.Add(this.txtTotalCost);
            this.grpbxOrderTotals.Controls.Add(this.txtTax);
            this.grpbxOrderTotals.Controls.Add(this.txtSubtotal);
            this.grpbxOrderTotals.Controls.Add(this.lblTotalCost);
            this.grpbxOrderTotals.Controls.Add(this.lblTax);
            this.grpbxOrderTotals.Controls.Add(this.lblSubtotal);
            this.grpbxOrderTotals.Location = new System.Drawing.Point(27, 160);
            this.grpbxOrderTotals.Name = "grpbxOrderTotals";
            this.grpbxOrderTotals.Size = new System.Drawing.Size(330, 131);
            this.grpbxOrderTotals.TabIndex = 1;
            this.grpbxOrderTotals.TabStop = false;
            this.grpbxOrderTotals.Text = "Total Costs";
            // 
            // txtTotalCost
            // 
            this.txtTotalCost.Enabled = false;
            this.txtTotalCost.Location = new System.Drawing.Point(209, 94);
            this.txtTotalCost.Name = "txtTotalCost";
            this.txtTotalCost.Size = new System.Drawing.Size(100, 23);
            this.txtTotalCost.TabIndex = 1;
            // 
            // txtTax
            // 
            this.txtTax.Enabled = false;
            this.txtTax.Location = new System.Drawing.Point(209, 59);
            this.txtTax.Name = "txtTax";
            this.txtTax.Size = new System.Drawing.Size(100, 23);
            this.txtTax.TabIndex = 1;
            // 
            // txtSubtotal
            // 
            this.txtSubtotal.Enabled = false;
            this.txtSubtotal.Location = new System.Drawing.Point(209, 25);
            this.txtSubtotal.Name = "txtSubtotal";
            this.txtSubtotal.Size = new System.Drawing.Size(100, 23);
            this.txtSubtotal.TabIndex = 1;
            // 
            // lblTotalCost
            // 
            this.lblTotalCost.AutoSize = true;
            this.lblTotalCost.Location = new System.Drawing.Point(17, 97);
            this.lblTotalCost.Name = "lblTotalCost";
            this.lblTotalCost.Size = new System.Drawing.Size(59, 15);
            this.lblTotalCost.TabIndex = 0;
            this.lblTotalCost.Text = "Total Cost";
            // 
            // lblTax
            // 
            this.lblTax.AutoSize = true;
            this.lblTax.Location = new System.Drawing.Point(17, 62);
            this.lblTax.Name = "lblTax";
            this.lblTax.Size = new System.Drawing.Size(46, 15);
            this.lblTax.TabIndex = 0;
            this.lblTax.Text = "5% GST";
            // 
            // lblSubtotal
            // 
            this.lblSubtotal.AutoSize = true;
            this.lblSubtotal.Location = new System.Drawing.Point(17, 28);
            this.lblSubtotal.Name = "lblSubtotal";
            this.lblSubtotal.Size = new System.Drawing.Size(51, 15);
            this.lblSubtotal.TabIndex = 0;
            this.lblSubtotal.Text = "Subtotal";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(17, 75);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(32, 15);
            this.label3.TabIndex = 0;
            this.label3.Text = "label1";
            // 
            // btnOrder
            // 
            this.btnOrder.Location = new System.Drawing.Point(432, 184);
            this.btnOrder.Name = "btnOrder";
            this.btnOrder.Size = new System.Drawing.Size(116, 23);
            this.btnOrder.TabIndex = 2;
            this.btnOrder.Text = "Place Order";
            this.btnOrder.UseVisualStyleBackColor = true;
            this.btnOrder.Click += new System.EventHandler(this.btnOrder_Click);
            // 
            // btnReset
            // 
            this.btnReset.Location = new System.Drawing.Point(432, 218);
            this.btnReset.Name = "btnReset";
            this.btnReset.Size = new System.Drawing.Size(116, 23);
            this.btnReset.TabIndex = 2;
            this.btnReset.Text = "Reset";
            this.btnReset.UseVisualStyleBackColor = true;
            // 
            // btnExit
            // 
            this.btnExit.Location = new System.Drawing.Point(432, 253);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(116, 23);
            this.btnExit.TabIndex = 2;
            this.btnExit.Text = "Exit";
            this.btnExit.UseVisualStyleBackColor = true;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // lblOrderSubmitted
            // 
            this.lblOrderSubmitted.AutoSize = true;
            this.lblOrderSubmitted.Location = new System.Drawing.Point(285, 313);
            this.lblOrderSubmitted.Name = "lblOrderSubmitted";
            this.lblOrderSubmitted.Size = new System.Drawing.Size(105, 15);
            this.lblOrderSubmitted.TabIndex = 3;
            this.lblOrderSubmitted.Text = "Submit Your Order";
            // 
            // radioBurger
            // 
            this.radioBurger.AutoSize = true;
            this.radioBurger.Location = new System.Drawing.Point(6, 22);
            this.radioBurger.Name = "radioBurger";
            this.radioBurger.Size = new System.Drawing.Size(124, 19);
            this.radioBurger.TabIndex = 0;
            this.radioBurger.TabStop = true;
            this.radioBurger.Text = "Hamburger - $6.95";
            this.radioBurger.UseVisualStyleBackColor = true;
            // 
            // radioPizza
            // 
            this.radioPizza.AutoSize = true;
            this.radioPizza.Location = new System.Drawing.Point(6, 47);
            this.radioPizza.Name = "radioPizza";
            this.radioPizza.Size = new System.Drawing.Size(89, 19);
            this.radioPizza.TabIndex = 0;
            this.radioPizza.TabStop = true;
            this.radioPizza.Text = "Pizza - $5.95";
            this.radioPizza.UseVisualStyleBackColor = true;
            // 
            // radioSalad
            // 
            this.radioSalad.AutoSize = true;
            this.radioSalad.Location = new System.Drawing.Point(6, 72);
            this.radioSalad.Name = "radioSalad";
            this.radioSalad.Size = new System.Drawing.Size(91, 19);
            this.radioSalad.TabIndex = 0;
            this.radioSalad.TabStop = true;
            this.radioSalad.Text = "Salad - $4.95";
            this.radioSalad.UseVisualStyleBackColor = true;
            // 
            // grpbxMainCourse
            // 
            this.grpbxMainCourse.Controls.Add(this.radioSalad);
            this.grpbxMainCourse.Controls.Add(this.radioPizza);
            this.grpbxMainCourse.Controls.Add(this.radioBurger);
            this.grpbxMainCourse.Location = new System.Drawing.Point(27, 34);
            this.grpbxMainCourse.Name = "grpbxMainCourse";
            this.grpbxMainCourse.Size = new System.Drawing.Size(330, 109);
            this.grpbxMainCourse.TabIndex = 0;
            this.grpbxMainCourse.TabStop = false;
            this.grpbxMainCourse.Text = "Main Course";
            // 
            // frmOrderForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(611, 368);
            this.Controls.Add(this.lblOrderSubmitted);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.btnReset);
            this.Controls.Add(this.btnOrder);
            this.Controls.Add(this.grpbxOrderTotals);
            this.Controls.Add(this.grpbxAddOn);
            this.Controls.Add(this.grpbxMainCourse);
            this.Name = "frmOrderForm";
            this.Text = "OrderForm";
            this.Load += new System.EventHandler(this.frmOrderForm_Load);
            this.grpbxAddOn.ResumeLayout(false);
            this.grpbxAddOn.PerformLayout();
            this.grpbxOrderTotals.ResumeLayout(false);
            this.grpbxOrderTotals.PerformLayout();
            this.grpbxMainCourse.ResumeLayout(false);
            this.grpbxMainCourse.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.GroupBox grpbxAddOn;
        private System.Windows.Forms.GroupBox grpbxOrderTotals;
        private System.Windows.Forms.Label lblTotalCost;
        private System.Windows.Forms.Label lblTax;
        private System.Windows.Forms.Label lblSubtotal;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtTotalCost;
        private System.Windows.Forms.TextBox txtTax;
        private System.Windows.Forms.TextBox txtSubtotal;
        private System.Windows.Forms.Button btnOrder;
        private System.Windows.Forms.Button btnReset;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.CheckBox chkAddOn2;
        private System.Windows.Forms.CheckBox chkAddOn3;
        private System.Windows.Forms.CheckBox chkAddOn1;
        private System.Windows.Forms.Label lblOrderSubmitted;
        private System.Windows.Forms.RadioButton radioBurger;
        private System.Windows.Forms.RadioButton radioPizza;
        private System.Windows.Forms.RadioButton radioSalad;
        private System.Windows.Forms.GroupBox grpbxMainCourse;
    }
}

