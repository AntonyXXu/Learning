using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace textBoxWithValidationDemo
{
    public partial class TextBoxWithValidation : Form
    {
        public TextBoxWithValidation()
        {
            InitializeComponent();
        }

        private void IntegerInputTextbox_TextChanged(object sender, EventArgs e)
        {
            int value;

            if (int.TryParse(integerInputTextbox.Text, out value))
            {
                integerInputStatusLabel.Text = "GOOD";
                processIntegerButton.Enabled = true;
            }
            else
            {
                integerInputStatusLabel.Text = "BAD";
                processIntegerButton.Enabled = false;
            }
        }
    }
}
