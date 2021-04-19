using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HelloWorld
{
    public partial class frmMain : Form
    {
        /*
         * Our first application: displays personalized greeting
         * Author: Jolanta
         * Date: April 1, 2019
         */
        public frmMain()
        {
            InitializeComponent();
        }

        // Personalize greeting using the name provided
        private void btnGreetMe_Click(object sender, EventArgs e)
        {
            lblMessage.Text = "Hello " + txtName.Text;
        }

        // prepare for next entry
        private void btnClear_Click(object sender, EventArgs e)
        {
            lblMessage.Text = "Hello World";
            txtName.Text = ""; // erase text
            txtName.Focus(); // put focus on the text box
        }

        // close the form and terminate
        private void btnExit_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
