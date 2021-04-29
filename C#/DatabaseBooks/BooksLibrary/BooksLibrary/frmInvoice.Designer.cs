
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
            ((System.ComponentModel.ISupportInitialize)(this.dGridInvoice)).BeginInit();
            this.SuspendLayout();
            // 
            // dGridInvoice
            // 
            this.dGridInvoice.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dGridInvoice.Location = new System.Drawing.Point(12, 12);
            this.dGridInvoice.Name = "dGridInvoice";
            this.dGridInvoice.RowTemplate.Height = 25;
            this.dGridInvoice.Size = new System.Drawing.Size(776, 426);
            this.dGridInvoice.TabIndex = 0;
            // 
            // frmInvoice
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.dGridInvoice);
            this.Name = "frmInvoice";
            this.Text = "Invoices";
            ((System.ComponentModel.ISupportInitialize)(this.dGridInvoice)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView dGridInvoice;
    }
}