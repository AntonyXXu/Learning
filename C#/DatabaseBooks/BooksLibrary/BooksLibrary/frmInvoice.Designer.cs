
namespace BooksLibrary
{
    partial class frmInvoice
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
            this.dGridInvoice = new System.Windows.Forms.DataGridView();
            this.InvoiceID = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.CustomerID = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dGridInvoiceDetails = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.dGridInvoice)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dGridInvoiceDetails)).BeginInit();
            this.SuspendLayout();
            // 
            // dGridInvoice
            // 
            this.dGridInvoice.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dGridInvoice.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dGridInvoice.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.InvoiceID,
            this.CustomerID});
            this.dGridInvoice.Location = new System.Drawing.Point(12, 12);
            this.dGridInvoice.Name = "dGridInvoice";
            this.dGridInvoice.RowTemplate.Height = 25;
            this.dGridInvoice.Size = new System.Drawing.Size(776, 154);
            this.dGridInvoice.TabIndex = 0;
            this.dGridInvoice.SelectionChanged += new System.EventHandler(this.dGridInvoice_SelectionChanged);
            // 
            // InvoiceID
            // 
            this.InvoiceID.DataPropertyName = "InvoiceID";
            this.InvoiceID.HeaderText = "ID";
            this.InvoiceID.Name = "InvoiceID";
            // 
            // CustomerID
            // 
            this.CustomerID.DataPropertyName = "CustomerID";
            this.CustomerID.HeaderText = "CustomerID";
            this.CustomerID.Name = "CustomerID";
            this.CustomerID.ReadOnly = true;
            // 
            // dGridInvoiceDetails
            // 
            this.dGridInvoiceDetails.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dGridInvoiceDetails.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dGridInvoiceDetails.Location = new System.Drawing.Point(12, 196);
            this.dGridInvoiceDetails.Name = "dGridInvoiceDetails";
            this.dGridInvoiceDetails.RowTemplate.Height = 25;
            this.dGridInvoiceDetails.Size = new System.Drawing.Size(768, 231);
            this.dGridInvoiceDetails.TabIndex = 1;
            // 
            // frmInvoice
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.dGridInvoiceDetails);
            this.Controls.Add(this.dGridInvoice);
            this.Name = "frmInvoice";
            this.Text = "Invoices";
            ((System.ComponentModel.ISupportInitialize)(this.dGridInvoice)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dGridInvoiceDetails)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView dGridInvoice;
        private System.Windows.Forms.DataGridViewTextBoxColumn InvoiceID;
        private System.Windows.Forms.DataGridViewTextBoxColumn CustomerID;
        private System.Windows.Forms.DataGridView dGridInvoiceDetails;
    }
}