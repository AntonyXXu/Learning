
namespace maintenance
{
    partial class formAdd
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.radBook = new System.Windows.Forms.RadioButton();
            this.radSoftware = new System.Windows.Forms.RadioButton();
            this.lblCode = new System.Windows.Forms.Label();
            this.lblDescription = new System.Windows.Forms.Label();
            this.lblAuthorVer = new System.Windows.Forms.Label();
            this.lblPrice = new System.Windows.Forms.Label();
            this.btnSave = new System.Windows.Forms.Button();
            this.btnCancel = new System.Windows.Forms.Button();
            this.txtbxCode = new System.Windows.Forms.TextBox();
            this.txtBxDescription = new System.Windows.Forms.TextBox();
            this.txtBxAuthor = new System.Windows.Forms.TextBox();
            this.txtBxprice = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // radBook
            // 
            this.radBook.AutoSize = true;
            this.radBook.Location = new System.Drawing.Point(77, 30);
            this.radBook.Name = "radBook";
            this.radBook.Size = new System.Drawing.Size(52, 19);
            this.radBook.TabIndex = 0;
            this.radBook.TabStop = true;
            this.radBook.Text = "Book";
            this.radBook.UseVisualStyleBackColor = true;
            // 
            // radSoftware
            // 
            this.radSoftware.AutoSize = true;
            this.radSoftware.Location = new System.Drawing.Point(166, 30);
            this.radSoftware.Name = "radSoftware";
            this.radSoftware.Size = new System.Drawing.Size(71, 19);
            this.radSoftware.TabIndex = 0;
            this.radSoftware.TabStop = true;
            this.radSoftware.Text = "Software";
            this.radSoftware.UseVisualStyleBackColor = true;
            // 
            // lblCode
            // 
            this.lblCode.AutoSize = true;
            this.lblCode.Location = new System.Drawing.Point(34, 97);
            this.lblCode.Name = "lblCode";
            this.lblCode.Size = new System.Drawing.Size(35, 15);
            this.lblCode.TabIndex = 1;
            this.lblCode.Text = "Code";
            // 
            // lblDescription
            // 
            this.lblDescription.AutoSize = true;
            this.lblDescription.Location = new System.Drawing.Point(34, 151);
            this.lblDescription.Name = "lblDescription";
            this.lblDescription.Size = new System.Drawing.Size(67, 15);
            this.lblDescription.TabIndex = 1;
            this.lblDescription.Text = "Description";
            // 
            // lblAuthorVer
            // 
            this.lblAuthorVer.AutoSize = true;
            this.lblAuthorVer.Location = new System.Drawing.Point(34, 210);
            this.lblAuthorVer.Name = "lblAuthorVer";
            this.lblAuthorVer.Size = new System.Drawing.Size(44, 15);
            this.lblAuthorVer.TabIndex = 1;
            this.lblAuthorVer.Text = "Author";
            // 
            // lblPrice
            // 
            this.lblPrice.AutoSize = true;
            this.lblPrice.Location = new System.Drawing.Point(34, 271);
            this.lblPrice.Name = "lblPrice";
            this.lblPrice.Size = new System.Drawing.Size(33, 15);
            this.lblPrice.TabIndex = 1;
            this.lblPrice.Text = "Price";
            // 
            // btnSave
            // 
            this.btnSave.Location = new System.Drawing.Point(77, 339);
            this.btnSave.Name = "btnSave";
            this.btnSave.Size = new System.Drawing.Size(133, 46);
            this.btnSave.TabIndex = 2;
            this.btnSave.Text = "Save";
            this.btnSave.UseVisualStyleBackColor = true;
            // 
            // btnCancel
            // 
            this.btnCancel.Location = new System.Drawing.Point(275, 339);
            this.btnCancel.Name = "btnCancel";
            this.btnCancel.Size = new System.Drawing.Size(133, 46);
            this.btnCancel.TabIndex = 2;
            this.btnCancel.Text = "Cancel";
            this.btnCancel.UseVisualStyleBackColor = true;
            // 
            // txtbxCode
            // 
            this.txtbxCode.Location = new System.Drawing.Point(110, 94);
            this.txtbxCode.Name = "txtbxCode";
            this.txtbxCode.Size = new System.Drawing.Size(298, 23);
            this.txtbxCode.TabIndex = 3;
            // 
            // txtBxDescription
            // 
            this.txtBxDescription.Location = new System.Drawing.Point(110, 148);
            this.txtBxDescription.Name = "txtBxDescription";
            this.txtBxDescription.Size = new System.Drawing.Size(298, 23);
            this.txtBxDescription.TabIndex = 3;
            // 
            // txtBxAuthor
            // 
            this.txtBxAuthor.Location = new System.Drawing.Point(110, 207);
            this.txtBxAuthor.Name = "txtBxAuthor";
            this.txtBxAuthor.Size = new System.Drawing.Size(298, 23);
            this.txtBxAuthor.TabIndex = 3;
            // 
            // txtBxprice
            // 
            this.txtBxprice.Location = new System.Drawing.Point(110, 268);
            this.txtBxprice.Name = "txtBxprice";
            this.txtBxprice.Size = new System.Drawing.Size(298, 23);
            this.txtBxprice.TabIndex = 3;
            // 
            // formAdd
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(482, 450);
            this.Controls.Add(this.txtBxprice);
            this.Controls.Add(this.txtBxAuthor);
            this.Controls.Add(this.txtBxDescription);
            this.Controls.Add(this.txtbxCode);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnSave);
            this.Controls.Add(this.lblPrice);
            this.Controls.Add(this.lblAuthorVer);
            this.Controls.Add(this.lblDescription);
            this.Controls.Add(this.lblCode);
            this.Controls.Add(this.radSoftware);
            this.Controls.Add(this.radBook);
            this.Name = "formAdd";
            this.Text = "Add";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.RadioButton radBook;
        private System.Windows.Forms.RadioButton radSoftware;
        private System.Windows.Forms.Label lblCode;
        private System.Windows.Forms.Label lblDescription;
        private System.Windows.Forms.Label lblAuthorVer;
        private System.Windows.Forms.Label lblPrice;
        private System.Windows.Forms.Button btnSave;
        private System.Windows.Forms.Button btnCancel;
        private System.Windows.Forms.TextBox txtbxCode;
        private System.Windows.Forms.TextBox txtBxDescription;
        private System.Windows.Forms.TextBox txtBxAuthor;
        private System.Windows.Forms.TextBox txtBxprice;
    }
}