using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ClassesAggregationCards
{
    public partial class Form1 : Form
    {
        Deck d; // deck of cards
        public Form1()
        {
            InitializeComponent();
        }

        // generate deck of cards and display 
        private void Form1_Load(object sender, EventArgs e)
        {
            d = new Deck(); // create a deck of cards
            DisplayDeck(d); // display it
        }

        // display deck of cards in a list box, one card  per line
        private void DisplayDeck(Deck d)
        {
            lstOutput.Items.Clear(); // clear the list box
            for (int i = 0; i < Deck.NR_CARDS; i++)
            {
                lstOutput.Items.Add(d.GetCard(i));// implicitly calls ToString() from Card
            }
        }

        // shuffle the deck and display
        private void btnShuffle_Click(object sender, EventArgs e)
        {
            d.Shuffle(); // shuffle the deck 
            DisplayDeck(d); // display it
        }

      
    }
}
