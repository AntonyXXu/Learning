using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using BooksLibrary.Models;

namespace BooksLibrary
{
    public partial class formCust : Form
    {
        MMABooksContext context;
        public formCust()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            context = new MMABooksContext();
        }

        private void updateView()
        {
            int id = Convert.ToInt32(txtID.Text);
            Customer c1 = context.Customers.Find(id);
            if (c1 == null) return;
            txtName.Text = c1.Name;
            txtAddress.Text = c1.Address;
        }

        private void btnFind_Click(object sender, EventArgs e)
        {
            updateView();
        }

        private void btnSave_Click(object sender, EventArgs e)
        {
            int id = Convert.ToInt32(txtID.Text);
            Customer c1 = context.Customers.Find(id);

            c1.Name = txtName.Text;
            c1.Address = txtAddress.Text;
            context.SaveChanges();
                        
            updateView();
        }
    }
}
