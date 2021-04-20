using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MoneyChange
{
    public partial class MoneyChangeFrom : Form
    {
        public MoneyChangeFrom()
        {
            InitializeComponent();
        }

        private void MoneyChangeFrom_Load(object sender, EventArgs e)
        {

        }

        private void CalcChange_Click(object sender, EventArgs e)
        {
            if (MoneyIn.Text == "")
            {
               MoneyIn.Text = "0.00";
            }

            if (InPenny.Checked == true)
            {
            double MnyIn = Math.Round(Convert.ToDouble(MoneyIn.Text),2);
            ToonieSh.Text = Math.Floor(MnyIn/2).ToString();
            double Loonie = Math.Floor(Math.Round((MnyIn % 2), 2));
            LoonieSh.Text = Loonie.ToString();
            double Cents = Math.Round(((MnyIn % 2 - Loonie) * 100),0);
            QuarterSh.Text = Math.Floor(Cents / 25).ToString();
            double dimes = Math.Floor((Cents % 25) / 10);
            DimeSh.Text = dimes.ToString();
            double nickels = Math.Floor(((Cents % 25) % 10)/5);
            NickelSh.Text = nickels.ToString();
            double Penny = (((Cents % 25) % 10) % 5);
            PennySh.Text = Penny.ToString();
            }                

            if(NoPenny.Checked == true)
            {
            PennySh.Text = " Penny not included";

            double MnyIn = Math.Round(Convert.ToDouble(MoneyIn.Text), 2);
            ToonieSh.Text = Math.Floor(MnyIn / 2).ToString();
            double Loonie = Math.Floor(Math.Round((MnyIn % 2), 2));
            LoonieSh.Text = Loonie.ToString();
            double Cents = Math.Round(((MnyIn % 2 - Loonie) * 100), 0);
            if((Cents % 25) > 23)
                {
                    QuarterSh.Text = Math.Round((Cents / 25),0).ToString();
                }
            else
                {
                    QuarterSh.Text = Math.Floor(Cents / 25).ToString();
                }

            double QuarterDeducted = Convert.ToDouble(QuarterSh.Text);
            if (((Cents - QuarterDeducted * 25) % 10) > 7)
                {
                    double dimesH = Math.Round(((Cents - QuarterDeducted * 25) / 10), 0);
                    DimeSh.Text = dimesH.ToString();
                }
            else if(((Cents - QuarterDeducted * 25) % 10) <0)
                {
                    DimeSh.Text = "0";
                }
            else
                {
                    double dimesL = Math.Floor((Cents - QuarterDeducted * 25) / 10);
                    DimeSh.Text = dimesL.ToString();
                }

            double DimesDeducted = Convert.ToDouble(DimeSh.Text);
            if (((Cents - QuarterDeducted * 25 - DimesDeducted * 10) % 5) > 3)
                {
                    double nickelsH = Math.Round(((Cents - QuarterDeducted * 25 - DimesDeducted * 10) / 5),0);
                    NickelSh.Text = nickelsH.ToString();
                }
            else if(((Cents - QuarterDeducted * 25 - DimesDeducted * 10) % 5) <0)
                {
                    NickelSh.Text = "0";
                }
            else
                {
                    double nickelsL = Math.Floor((Cents - QuarterDeducted * 25 - DimesDeducted * 10) / 5);
                    NickelSh.Text = nickelsL.ToString();
                }


            }             

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
    
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void MoneyIn_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void label7_Click(object sender, EventArgs e)
        {

        }
    }
}
