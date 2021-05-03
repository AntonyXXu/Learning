﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using ProductMaintenance.Models;

namespace ModifyProduct
{
    public partial class frmModifyProduct : Form
    {
        public Product selectedProduct { get; set; }
        public TechSupportContext context { get; set; }
        public frmModifyProduct()
        {
            InitializeComponent();
            txtMsg.Text ="Modify a product";
        }

        private void frmModifyProduct_Load(object sender, EventArgs e)
        {
            txtName.Text = selectedProduct.Name.Trim();
            txtProductCode.Text = selectedProduct.ProductCode.Trim();
            txtVersion.Text = selectedProduct.Version.ToString("0.0").Trim();
            dateRelease.Value = selectedProduct.ReleaseDate;
        }

        private void btnModify_Click(object sender, EventArgs e)
        {
            selectedProduct.Name = txtName.Text.Trim();
            selectedProduct.Version = Convert.ToDecimal(txtVersion.Text.Trim());
            selectedProduct.ReleaseDate = dateRelease.Value;
            if (selectedProduct.Name == "" || selectedProduct.ProductCode == "" || txtVersion.Text.Trim() == "")
            {
                MessageBox.Show("No Fields can be Empty");
            }
            context.SaveChanges();
            txtMsg.Text = "Product Modified!";
        }

        private void btnCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void txtVersion_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!char.IsDigit(e.KeyChar)
             && e.KeyChar != '.'
             && !char.IsControl(e.KeyChar))
            {
                e.Handled = true;
            }
            else if (e.KeyChar == '.' && txtVersion.Text.Contains('.'))
            {
                e.Handled = true;
            }
        }
    }
}
