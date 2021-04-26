
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
            this.btnAddCustomer = new System.Windows.Forms.Button();
            this.btnViewCustomer = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.lblAccountNumber = new System.Windows.Forms.Label();
            this.lblKWH = new System.Windows.Forms.Label();
            this.lblPredictBill = new System.Windows.Forms.Label();
            this.lblAccountNumberValue = new System.Windows.Forms.Label();
            this.lblPredictedBillVal = new System.Windows.Forms.Label();
            this.lblFirstName = new System.Windows.Forms.Label();
            this.lblLastName = new System.Windows.Forms.Label();
            this.txtbxLastName = new System.Windows.Forms.TextBox();
            this.txtbxFirstName = new System.Windows.Forms.TextBox();
            this.txtbxKWHVal = new System.Windows.Forms.TextBox();
            this.grpbxData = new System.Windows.Forms.GroupBox();
            this.lstbxCustomers = new System.Windows.Forms.ListBox();
            this.lblAverageBillVal = new System.Windows.Forms.Label();
            this.lblTotalKWHVal = new System.Windows.Forms.Label();
            this.lblTotalCustomerVal = new System.Windows.Forms.Label();
            this.lblAverageBill = new System.Windows.Forms.Label();
            this.lblTotalKWH = new System.Windows.Forms.Label();
            this.lblCustomerList = new System.Windows.Forms.Label();
            this.lblTotalCustomers = new System.Windows.Forms.Label();
            this.btnSubmitNewCustomer = new System.Windows.Forms.Button();
            this.btnResetCustomer = new System.Windows.Forms.Button();
            this.grpbxAddCustomer = new System.Windows.Forms.GroupBox();
            this.lblAddCustomerMsg = new System.Windows.Forms.Label();
            this.grpbxData.SuspendLayout();
            this.grpbxAddCustomer.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnAddCustomer
            // 
            this.btnAddCustomer.BackColor = System.Drawing.SystemColors.Control;
            this.btnAddCustomer.Location = new System.Drawing.Point(107, 28);
            this.btnAddCustomer.Name = "btnAddCustomer";
            this.btnAddCustomer.Size = new System.Drawing.Size(209, 52);
            this.btnAddCustomer.TabIndex = 0;
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
            this.btnViewCustomer.Click += new System.EventHandler(this.btnViewCustomer_Click);
            // 
            // btnExit
            // 
            this.btnExit.Location = new System.Drawing.Point(474, 414);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(209, 52);
            this.btnExit.TabIndex = 5;
            this.btnExit.Text = "Exit";
            this.btnExit.UseVisualStyleBackColor = true;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
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
            // lblKWH
            // 
            this.lblKWH.AutoSize = true;
            this.lblKWH.Location = new System.Drawing.Point(450, 49);
            this.lblKWH.Name = "lblKWH";
            this.lblKWH.Size = new System.Drawing.Size(97, 15);
            this.lblKWH.TabIndex = 0;
            this.lblKWH.Text = "Input kWh Usage";
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
            // lblAccountNumberValue
            // 
            this.lblAccountNumberValue.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblAccountNumberValue.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblAccountNumberValue.Location = new System.Drawing.Point(83, 73);
            this.lblAccountNumberValue.Margin = new System.Windows.Forms.Padding(3);
            this.lblAccountNumberValue.Name = "lblAccountNumberValue";
            this.lblAccountNumberValue.Size = new System.Drawing.Size(209, 23);
            this.lblAccountNumberValue.TabIndex = 2;
            this.lblAccountNumberValue.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
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
            // lblFirstName
            // 
            this.lblFirstName.AutoSize = true;
            this.lblFirstName.Location = new System.Drawing.Point(83, 129);
            this.lblFirstName.Name = "lblFirstName";
            this.lblFirstName.Size = new System.Drawing.Size(64, 15);
            this.lblFirstName.TabIndex = 0;
            this.lblFirstName.Text = "First Name";
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
            // txtbxLastName
            // 
            this.txtbxLastName.Location = new System.Drawing.Point(83, 229);
            this.txtbxLastName.Name = "txtbxLastName";
            this.txtbxLastName.Size = new System.Drawing.Size(209, 23);
            this.txtbxLastName.TabIndex = 3;
            this.txtbxLastName.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtbxFirstName
            // 
            this.txtbxFirstName.Location = new System.Drawing.Point(83, 147);
            this.txtbxFirstName.Name = "txtbxFirstName";
            this.txtbxFirstName.Size = new System.Drawing.Size(209, 23);
            this.txtbxFirstName.TabIndex = 2;
            this.txtbxFirstName.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // txtbxKWHVal
            // 
            this.txtbxKWHVal.Location = new System.Drawing.Point(450, 73);
            this.txtbxKWHVal.Name = "txtbxKWHVal";
            this.txtbxKWHVal.Size = new System.Drawing.Size(209, 23);
            this.txtbxKWHVal.TabIndex = 2;
            this.txtbxKWHVal.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtbxKWHVal.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtbxKWHVal_KeyPress);
            // 
            // grpbxData
            // 
            this.grpbxData.Controls.Add(this.lstbxCustomers);
            this.grpbxData.Controls.Add(this.lblAverageBillVal);
            this.grpbxData.Controls.Add(this.lblTotalKWHVal);
            this.grpbxData.Controls.Add(this.lblTotalCustomerVal);
            this.grpbxData.Controls.Add(this.lblAverageBill);
            this.grpbxData.Controls.Add(this.lblTotalKWH);
            this.grpbxData.Controls.Add(this.lblCustomerList);
            this.grpbxData.Controls.Add(this.lblTotalCustomers);
            this.grpbxData.Location = new System.Drawing.Point(24, 86);
            this.grpbxData.Name = "grpbxData";
            this.grpbxData.Size = new System.Drawing.Size(749, 306);
            this.grpbxData.TabIndex = 0;
            this.grpbxData.TabStop = false;
            // 
            // lstbxCustomers
            // 
            this.lstbxCustomers.FormattingEnabled = true;
            this.lstbxCustomers.ItemHeight = 15;
            this.lstbxCustomers.Location = new System.Drawing.Point(417, 67);
            this.lstbxCustomers.Name = "lstbxCustomers";
            this.lstbxCustomers.Size = new System.Drawing.Size(310, 184);
            this.lstbxCustomers.TabIndex = 6;
            // 
            // lblAverageBillVal
            // 
            this.lblAverageBillVal.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblAverageBillVal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblAverageBillVal.Location = new System.Drawing.Point(83, 228);
            this.lblAverageBillVal.Margin = new System.Windows.Forms.Padding(3);
            this.lblAverageBillVal.Name = "lblAverageBillVal";
            this.lblAverageBillVal.Size = new System.Drawing.Size(209, 23);
            this.lblAverageBillVal.TabIndex = 2;
            this.lblAverageBillVal.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblTotalKWHVal
            // 
            this.lblTotalKWHVal.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblTotalKWHVal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblTotalKWHVal.Location = new System.Drawing.Point(83, 146);
            this.lblTotalKWHVal.Margin = new System.Windows.Forms.Padding(3);
            this.lblTotalKWHVal.Name = "lblTotalKWHVal";
            this.lblTotalKWHVal.Size = new System.Drawing.Size(209, 23);
            this.lblTotalKWHVal.TabIndex = 2;
            this.lblTotalKWHVal.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblTotalCustomerVal
            // 
            this.lblTotalCustomerVal.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblTotalCustomerVal.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.lblTotalCustomerVal.Location = new System.Drawing.Point(83, 73);
            this.lblTotalCustomerVal.Margin = new System.Windows.Forms.Padding(3);
            this.lblTotalCustomerVal.Name = "lblTotalCustomerVal";
            this.lblTotalCustomerVal.Size = new System.Drawing.Size(209, 23);
            this.lblTotalCustomerVal.TabIndex = 2;
            this.lblTotalCustomerVal.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // lblAverageBill
            // 
            this.lblAverageBill.AutoSize = true;
            this.lblAverageBill.Location = new System.Drawing.Point(83, 204);
            this.lblAverageBill.Name = "lblAverageBill";
            this.lblAverageBill.Size = new System.Drawing.Size(69, 15);
            this.lblAverageBill.TabIndex = 0;
            this.lblAverageBill.Text = "Average Bill";
            // 
            // lblTotalKWH
            // 
            this.lblTotalKWH.AutoSize = true;
            this.lblTotalKWH.Location = new System.Drawing.Point(83, 122);
            this.lblTotalKWH.Name = "lblTotalKWH";
            this.lblTotalKWH.Size = new System.Drawing.Size(94, 15);
            this.lblTotalKWH.TabIndex = 0;
            this.lblTotalKWH.Text = "Total kWh Usage";
            // 
            // lblCustomerList
            // 
            this.lblCustomerList.AutoSize = true;
            this.lblCustomerList.Location = new System.Drawing.Point(417, 49);
            this.lblCustomerList.Name = "lblCustomerList";
            this.lblCustomerList.Size = new System.Drawing.Size(99, 15);
            this.lblCustomerList.TabIndex = 0;
            this.lblCustomerList.Text = "List of Customers";
            // 
            // lblTotalCustomers
            // 
            this.lblTotalCustomers.AutoSize = true;
            this.lblTotalCustomers.Location = new System.Drawing.Point(83, 49);
            this.lblTotalCustomers.Name = "lblTotalCustomers";
            this.lblTotalCustomers.Size = new System.Drawing.Size(92, 15);
            this.lblTotalCustomers.TabIndex = 0;
            this.lblTotalCustomers.Text = "Total Customers";
            // 
            // btnSubmitNewCustomer
            // 
            this.btnSubmitNewCustomer.Location = new System.Drawing.Point(572, 200);
            this.btnSubmitNewCustomer.Name = "btnSubmitNewCustomer";
            this.btnSubmitNewCustomer.Size = new System.Drawing.Size(87, 52);
            this.btnSubmitNewCustomer.TabIndex = 6;
            this.btnSubmitNewCustomer.Text = "Submit New Customer";
            this.btnSubmitNewCustomer.UseVisualStyleBackColor = true;
            this.btnSubmitNewCustomer.Click += new System.EventHandler(this.btnSubmitNewCustomer_Click);
            // 
            // btnResetCustomer
            // 
            this.btnResetCustomer.Location = new System.Drawing.Point(450, 200);
            this.btnResetCustomer.Name = "btnResetCustomer";
            this.btnResetCustomer.Size = new System.Drawing.Size(87, 52);
            this.btnResetCustomer.TabIndex = 5;
            this.btnResetCustomer.Text = "Reset Form";
            this.btnResetCustomer.UseVisualStyleBackColor = true;
            this.btnResetCustomer.Click += new System.EventHandler(this.btnResetCustomer_Click);
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
            this.grpbxAddCustomer.Controls.Add(this.lblAddCustomerMsg);
            this.grpbxAddCustomer.Controls.Add(this.lblPredictedBillVal);
            this.grpbxAddCustomer.Controls.Add(this.lblAccountNumberValue);
            this.grpbxAddCustomer.Controls.Add(this.lblPredictBill);
            this.grpbxAddCustomer.Controls.Add(this.lblKWH);
            this.grpbxAddCustomer.Controls.Add(this.lblAccountNumber);
            this.grpbxAddCustomer.Location = new System.Drawing.Point(24, 86);
            this.grpbxAddCustomer.Name = "grpbxAddCustomer";
            this.grpbxAddCustomer.Size = new System.Drawing.Size(749, 306);
            this.grpbxAddCustomer.TabIndex = 0;
            this.grpbxAddCustomer.TabStop = false;
            // 
            // lblAddCustomerMsg
            // 
            this.lblAddCustomerMsg.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.lblAddCustomerMsg.Location = new System.Drawing.Point(450, 258);
            this.lblAddCustomerMsg.Margin = new System.Windows.Forms.Padding(3);
            this.lblAddCustomerMsg.Name = "lblAddCustomerMsg";
            this.lblAddCustomerMsg.Size = new System.Drawing.Size(209, 23);
            this.lblAddCustomerMsg.TabIndex = 0;
            this.lblAddCustomerMsg.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // ElectricityBill
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(802, 509);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.btnViewCustomer);
            this.Controls.Add(this.grpbxData);
            this.Controls.Add(this.btnAddCustomer);
            this.Controls.Add(this.grpbxAddCustomer);
            this.Name = "ElectricityBill";
            this.Text = "Electricity Bills";
            this.Load += new System.EventHandler(this.ElectricityBill_Load);
            this.grpbxData.ResumeLayout(false);
            this.grpbxData.PerformLayout();
            this.grpbxAddCustomer.ResumeLayout(false);
            this.grpbxAddCustomer.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion
        private System.Windows.Forms.Button btnAddCustomer;
        private System.Windows.Forms.Button btnViewCustomer;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.Label lblAccountNumber;
        private System.Windows.Forms.Label lblKWH;
        private System.Windows.Forms.Label lblPredictBill;
        private System.Windows.Forms.Label lblAccountNumberValue;
        private System.Windows.Forms.Label lblPredictedBillVal;
        private System.Windows.Forms.Label lblFirstName;
        private System.Windows.Forms.Label lblLastName;
        private System.Windows.Forms.TextBox txtbxLastName;
        private System.Windows.Forms.TextBox txtbxFirstName;
        private System.Windows.Forms.TextBox txtbxKWHVal;
        private System.Windows.Forms.GroupBox grpbxData;
        private System.Windows.Forms.Label lblAverageBillVal;
        private System.Windows.Forms.Label lblTotalKWHVal;
        private System.Windows.Forms.Label lblTotalCustomerVal;
        private System.Windows.Forms.Label lblAverageBill;
        private System.Windows.Forms.Label lblTotalKWH;
        private System.Windows.Forms.Label lblTotalCustomers;
        private System.Windows.Forms.Button btnSubmitNewCustomer;
        private System.Windows.Forms.Button btnResetCustomer;
        private System.Windows.Forms.GroupBox grpbxAddCustomer;
        private System.Windows.Forms.Label lblAddCustomerMsg;
        private System.Windows.Forms.ListBox lstbxCustomers;
        private System.Windows.Forms.Label lblCustomerList;
    }
}

