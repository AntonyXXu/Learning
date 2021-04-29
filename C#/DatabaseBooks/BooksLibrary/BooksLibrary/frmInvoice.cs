using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using BooksLibrary.Models;


namespace BooksLibrary
{
    public partial class frmInvoice : Form
    {
        MMABooksContext context;
        public frmInvoice()
        {
            InitializeComponent();
        }

        private void frmInvoice_Load(object sender, EventArgs e)
        {
            context = new MMABooksContext();
            dGridInvoice.AutoGenerateColumns = false;
            context.Invoices.
            //dGridInvoice.DataSource = context.Invoices.
            
        }

        private void dGridInvoice_SelectionChanged(object sender, EventArgs e)
        {
            DataGridView dg = (System.Windows.Forms.DataGridView)sender;
            if (dg.SelectedRows.Count > 0)
            {
                int x = 0;
            }
            
        }
    }
}
