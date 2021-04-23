
namespace ElectricityBillApplication
{
    partial class ElectricityBill
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
            this.grpbxAddCustomer = new System.Windows.Forms.GroupBox();
            this.btnResetCustomer = new System.Windows.Forms.Button();
            this.btnSubmitNewCustomer = new System.Windows.Forms.Button();
            this.txtbxFirstName = new System.Windows.Forms.TextBox();
            this.txtbxLastName = new System.Windows.Forms.TextBox();
            this.lblLastName = new System.Windows.Forms.Label();
            this.lblFirstName = new System.Windows.Forms.Label();
            this.lblPredictedBillVal = new System.Windows.Forms.Label();
            this.lblAccountNumberValue = new System.Windows.Forms.Label();
            this.lblPredictBill = new System.Windows.Forms.Label();
            this.lblKWH = new System.Windows.Forms.Label();
            this.lblAccountNumber = new System.Windows.Forms.Label();
            this.btnAddCustomer = new System.Windows.Forms.Button();
            this.btnViewCustomer = new System.Windows.Forms.Button();
            this.txtbxKWHVal = new System.Windows.Forms.TextBox();
            this.grpbxAddCustomer.SuspendLayout();
            this.SuspendLayout();
            // 
            // grpbxAddCustomer
            // 
            this.grpbxAddCustomer.Controls.Add(this.btnResetCustomer);
            this.grpbxAddCustomer.Controls.Add(this.btnSubmitNewCustomer);
            this.grpbxAddCustomer.Controls.Add(this.txtbxKWHVal);
            this.grpbxAddCustomer.Controls.Add(this.txtbxFirstName);
            this.grpbxAddCustomer.Controls.Add(this.txtbxLastName);
            this.grpbxAddCustomer.Controls.Add(this.lblLastName);
            this.grpbxAddCustomer.Controls.Add(this.lblFirstName);
            this.grpbxAddCustomer.Controls.Add(this.lblPredictedBillVal);
            this.grpbxAddCustomer.Controls.Add(this.lblAccountNumberValue);
            this.grpbxAddCustomer.Controls.Add(this.lblPredictBill);
            this.grpbxAddCustomer.Controls.Add(this.lblKWH);
            this.grpbxAddCustomer.Controls.Add(this.lblAccountNumber);
            this.grpbxAddCustomer.Location = new System.Drawing.Point(24, 86);
            this.grpbxAddCustomer.Name = "grpbxAddCustomer";
            this.grpbxAddCustomer.Size = new System.Drawing.Size(749, 318);
            this.grpbxAddCustomer.TabIndex = 0;
            this.grpbxAddCustomer.TabStop = false;
            // 
            // btnResetCustomer
            // 
            this.btnResetCustomer.Location = new System.Drawing.Point(450, 213);
            this.btnResetCustomer.Name = "btnResetCustomer";
            this.btnResetCustomer.Size = new System.Drawing.Size(87, 52);
            this.btnResetCustomer.TabIndex = 1;
            this.btnResetCustomer.Text = "Reset Form";
            this.btnResetCustomer.UseVisualStyleBackColor = true;
            this.btnResetCustomer.Click += new System.EventHandler(this.btnResetCustomer_Click);
            // 
            // btnSubmitNewCustomer
            // 
            this.btnSubmitNewCustomer.Location = new System.Drawing.Point(572, 213);
            this.btnSubmitNewCustomer.Name = "btnSubmitNewCustomer";
            this.btnSubmitNewCustomer.Size = new System.Drawing.Size(87, 52);
            this.btnSubmitNewCustomer.TabIndex = 1;
            this.btnSubmitNewCustomer.Text = "Submit New Customer";
            this.btnSubmitNewCustomer.UseVisualStyleBackColor = true;
            // 
            // txtbxFirstName
            // 
            this.txtbxFirstName.Location = new System.Drawing.Point(83, 147);
            this.txtbxFirstName.Name = "txtbxFirstName";
            this.txtbxFirstName.Size = new System.Drawing.Size(209, 23);
            this.txtbxFirstName.TabIndex = 1;
            // 
            // txtbxLastName
            // 
            this.txtbxLastName.Location = new System.Drawing.Point(83, 229);
            this.txtbxLastName.Name = "txtbxLastName";
            this.txtbxLastName.Size = new System.Drawing.Size(209, 23);
            this.txtbxLastName.TabIndex = 1;
            // 
            // lblLastName
            // 
            this.lblLastName.AutoSize = true;
            this.lblLastName.Location = new System.Drawing.Point(83, 211);
            this.lblLastName.Name = "lblLastName";
            this.lblLastName.Size = new System.Drawing.Size(63, 15);
            this.lblLastName.TabIndex = 0;
            this.lblLastName.Text = "Last Name";
            // 
            // lblFirstName
            // 
            this.lblFirstName.AutoSize = true;
            this.lblFirstName.Location = new System.Drawing.Point(83, 129);
            this.lblFirstName.Name = "lblFirstName";
            this.lblFirstName.Size = new System.Drawing.Size(64, 15);
            this.lblFirstName.TabIndex = 0;
            this.lblFirstName.Text = "First Name";
            // 
            // lblPredictedBillVal
            // 
            this.lblPredictedBillVal.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblPredictedBillVal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblPredictedBillVal.Location = new System.Drawing.Point(450, 147);
            this.lblPredictedBillVal.Margin = new System.Windows.Forms.Padding(3);
            this.lblPredictedBillVal.Name = "lblPredictedBillVal";
            this.lblPredictedBillVal.Size = new System.Drawing.Size(209, 23);
            this.lblPredictedBillVal.TabIndex = 0;
            this.lblPredictedBillVal.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblAccountNumberValue
            // 
            this.lblAccountNumberValue.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblAccountNumberValue.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblAccountNumberValue.Location = new System.Drawing.Point(83, 73);
            this.lblAccountNumberValue.Margin = new System.Windows.Forms.Padding(3);
            this.lblAccountNumberValue.Name = "lblAccountNumberValue";
            this.lblAccountNumberValue.Size = new System.Drawing.Size(209, 23);
            this.lblAccountNumberValue.TabIndex = 0;
            this.lblAccountNumberValue.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblPredictBill
            // 
            this.lblPredictBill.AutoSize = true;
            this.lblPredictBill.Location = new System.Drawing.Point(450, 129);
            this.lblPredictBill.Name = "lblPredictBill";
            this.lblPredictBill.Size = new System.Drawing.Size(76, 15);
            this.lblPredictBill.TabIndex = 0;
            this.lblPredictBill.Text = "Predicted Bill";
            // 
            // lblKWH
            // 
            this.lblKWH.AutoSize = true;
            this.lblKWH.Location = new System.Drawing.Point(450, 49);
            this.lblKWH.Name = "lblKWH";
            this.lblKWH.Size = new System.Drawing.Size(97, 15);
            this.lblKWH.TabIndex = 0;
            this.lblKWH.Text = "Input kWh Usage";
            // 
            // lblAccountNumber
            // 
            this.lblAccountNumber.AutoSize = true;
            this.lblAccountNumber.Location = new System.Drawing.Point(83, 49);
            this.lblAccountNumber.Name = "lblAccountNumber";
            this.lblAccountNumber.Size = new System.Drawing.Size(99, 15);
            this.lblAccountNumber.TabIndex = 0;
            this.lblAccountNumber.Text = "Account Number";
            // 
            // btnAddCustomer
            // 
            this.btnAddCustomer.BackColor = System.Drawing.SystemColors.Control;
            this.btnAddCustomer.Location = new System.Drawing.Point(107, 28);
            this.btnAddCustomer.Name = "btnAddCustomer";
            this.btnAddCustomer.Size = new System.Drawing.Size(209, 52);
            this.btnAddCustomer.TabIndex = 1;
            this.btnAddCustomer.Text = "Add A Customer";
            this.btnAddCustomer.UseVisualStyleBackColor = true;
            this.btnAddCustomer.Click += new System.EventHandler(this.btnAddCustomer_Click);
            // 
            // btnViewCustomer
            // 
            this.btnViewCustomer.Location = new System.Drawing.Point(474, 28);
            this.btnViewCustomer.Name = "btnViewCustomer";
            this.btnViewCustomer.Size = new System.Drawing.Size(209, 52);
            this.btnViewCustomer.TabIndex = 1;
            this.btnViewCustomer.Text = "View Customer Data";
            this.btnViewCustomer.UseVisualStyleBackColor = true;
            // 
            // txtbxKWHVal
            // 
            this.txtbxKWHVal.Location = new System.Drawing.Point(450, 73);
            this.txtbxKWHVal.Name = "txtbxKWHVal";
            this.txtbxKWHVal.Size = new System.Drawing.Size(209, 23);
            this.txtbxKWHVal.TabIndex = 1;
            // 
            // ElectricityBill
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(801, 441);
            this.Controls.Add(this.btnViewCustomer);
            this.Controls.Add(this.btnAddCustomer);
            this.Controls.Add(this.grpbxAddCustomer);
            this.Name = "ElectricityBill";
            this.Text = "Electricity Bills";
            this.Load += new System.EventHandler(this.ElectricityBill_Load);
            this.grpbxAddCustomer.ResumeLayout(false);
            this.grpbxAddCustomer.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox grpbxAddCustomer;
        private System.Windows.Forms.Button btnAddCustomer;
        private System.Windows.Forms.Button btnViewCustomer;
        private System.Windows.Forms.Label lblAccountNumber;
        private System.Windows.Forms.Button btnSubmitNewCustomer;
        private System.Windows.Forms.TextBox txtbxFirstName;
        private System.Windows.Forms.TextBox txtbxLastName;
        private System.Windows.Forms.Label lblLastName;
        private System.Windows.Forms.Label lblFirstName;
        private System.Windows.Forms.Label lblAccountNumberValue;
        private System.Windows.Forms.Button btnResetCustomer;
        private System.Windows.Forms.Label lblPredictedBillVal;
        private System.Windows.Forms.Label lblPredictBill;
        private System.Windows.Forms.Label lblKWH;
        private System.Windows.Forms.TextBox txtbxKWHVal;
    }
}

