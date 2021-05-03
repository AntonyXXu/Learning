
namespace AddProduct
{
    partial class frmAddProduct
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
            this.btnCancel = new System.Windows.Forms.Button();
            this.btnAdd = new System.Windows.Forms.Button();
            this.dateRelease = new System.Windows.Forms.DateTimePicker();
            this.txtVersion = new System.Windows.Forms.TextBox();
            this.txtName = new System.Windows.Forms.TextBox();
            this.txtProductCode = new System.Windows.Forms.TextBox();
            this.lblReleaseDate = new System.Windows.Forms.Label();
            this.lblAlternateData = new System.Windows.Forms.Label();
            this.lblName = new System.Windows.Forms.Label();
            this.lblProductCode = new System.Windows.Forms.Label();
            this.txtMsg = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // btnCancel
            // 
            this.btnCancel.Location = new System.Drawing.Point(288, 221);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(75, 23);
            this.btnCancel.TabIndex = 12;
            this.btnCancel.Text = "&Close";
            this.btnCancel.UseVisualStyleBackColor = true;
            this.btnCancel.Click += new System.EventHandler(this.btnCancel_Click);
            // 
            // btnAdd
            // 
            this.btnAdd.Location = new System.Drawing.Point(129, 221);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(75, 23);
            this.btnAdd.TabIndex = 13;
            this.btnAdd.Text = "Add";
            this.btnAdd.UseVisualStyleBackColor = true;
            this.btnAdd.Click += new System.EventHandler(this.btnAdd_Click);
            // 
            // dateRelease
            // 
            this.dateRelease.Location = new System.Drawing.Point(129, 151);
            this.dateRelease.Name = "dateRelease";
            this.dateRelease.Size = new System.Drawing.Size(234, 23);
            this.dateRelease.TabIndex = 11;
            // 
            // txtVersion
            // 
            this.txtVersion.Location = new System.Drawing.Point(129, 108);
            this.txtVersion.MaxLength = 18;
            this.txtVersion.Name = "txtVersion";
            this.txtVersion.Size = new System.Drawing.Size(234, 23);
            this.txtVersion.TabIndex = 8;
            this.txtVersion.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.txtVersion_KeyPress);
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(129, 66);
            this.txtName.MaxLength = 50;
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(234, 23);
            this.txtName.TabIndex = 9;
            // 
            // txtProductCode
            // 
            this.txtProductCode.Location = new System.Drawing.Point(129, 25);
            this.txtProductCode.MaxLength = 10;
            this.txtProductCode.Name = "txtProductCode";
            this.txtProductCode.Size = new System.Drawing.Size(234, 23);
            this.txtProductCode.TabIndex = 10;
            // 
            // lblReleaseDate
            // 
            this.lblReleaseDate.AutoSize = true;
            this.lblReleaseDate.Location = new System.Drawing.Point(25, 157);
            this.lblReleaseDate.Name = "lblReleaseDate";
            this.lblReleaseDate.Size = new System.Drawing.Size(73, 15);
            this.lblReleaseDate.TabIndex = 4;
            this.lblReleaseDate.Text = "Release Date";
            // 
            // lblAlternateData
            // 
            this.lblAlternateData.AutoSize = true;
            this.lblAlternateData.Location = new System.Drawing.Point(25, 111);
            this.lblAlternateData.Name = "lblAlternateData";
            this.lblAlternateData.Size = new System.Drawing.Size(45, 15);
            this.lblAlternateData.TabIndex = 5;
            this.lblAlternateData.Text = "Version";
            // 
            // lblName
            // 
            this.lblName.AutoSize = true;
            this.lblName.Location = new System.Drawing.Point(25, 69);
            this.lblName.Name = "lblName";
            this.lblName.Size = new System.Drawing.Size(39, 15);
            this.lblName.TabIndex = 6;
            this.lblName.Text = "Name";
            // 
            // lblProductCode
            // 
            this.lblProductCode.AutoSize = true;
            this.lblProductCode.Location = new System.Drawing.Point(25, 28);
            this.lblProductCode.Name = "lblProductCode";
            this.lblProductCode.Size = new System.Drawing.Size(80, 15);
            this.lblProductCode.TabIndex = 7;
            this.lblProductCode.Text = "Product Code";
            // 
            // txtMsg
            // 
            this.txtMsg.Location = new System.Drawing.Point(129, 188);
            this.txtMsg.Name = "txtMsg";
            this.txtMsg.ReadOnly = true;
            this.txtMsg.Size = new System.Drawing.Size(234, 23);
            this.txtMsg.TabIndex = 14;
            // 
            // frmAddProduct
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(427, 264);
            this.Controls.Add(this.txtMsg);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnAdd);
            this.Controls.Add(this.dateRelease);
            this.Controls.Add(this.txtVersion);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.txtProductCode);
            this.Controls.Add(this.lblReleaseDate);
            this.Controls.Add(this.lblAlternateData);
            this.Controls.Add(this.lblName);
            this.Controls.Add(this.lblProductCode);
            this.Name = "frmAddProduct";
            this.Text = "Add Product";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.DateTimePicker dateRelease;
        private System.Windows.Forms.TextBox txtVersion;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.TextBox txtProductCode;
        private System.Windows.Forms.Label lblReleaseDate;
        private System.Windows.Forms.Label lblAlternateData;
        private System.Windows.Forms.Label lblName;
        private System.Windows.Forms.Label lblProductCode;
        private System.Windows.Forms.TextBox txtMsg;
    }
}

