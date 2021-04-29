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
            dGridInvoice.DataSource = context.Invoices;
        }

  
    }
}
