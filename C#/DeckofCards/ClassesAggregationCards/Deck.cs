using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassesAggregationCards
{


    // represents a deck of cards
    public class Deck
    {
        // constants
        public int NR_RANKS = 13; // 13 ranks
        public const int NR_SUITS = 4; // 4 suits
        public const int NR_CARDS = 52; // 52 cards in a deck
        private List<Card> cards; // list of cards in the deck

        // constructor
        public Deck()
        {
            cards = new List<Card>(); // empty list
            // generate deck of cards
            for (int suitVal = 0; suitVal < NR_SUITS; suitVal++)
            {
                for (int rankVal = 1; rankVal <= NR_RANKS; rankVal++)
                {
                    cards.Add(new Card((Suit)suitVal, (Rank)rankVal));
                }
            }
        }


        // get a card on position cardNum 
        public Card GetCard(int cardNum)
        {
            if (cardNum >= 0 && cardNum < NR_CARDS)
                return cards[cardNum];
            else
                throw (new System.ArgumentOutOfRangeException("cardNum", cardNum,
                          "Value must be between 0 and " + (NR_CARDS - 1).ToString()));
        }

        // shuffle the deck
        public void Shuffle()
        {
            const int NR_TIMES = 100;
            Random sourceGen = new Random(); // random  number generator
            for(int i=0; i < NR_TIMES; i++) //swap two random cars many times
            {
                int pos1 = sourceGen.Next(NR_CARDS); // random number 0..51
                int pos2 = sourceGen.Next(NR_CARDS); // random number 0..51
                Card temp = cards[pos1]; // you can access list elements like array
                cards[pos1] = cards[pos2];
                cards[pos2] = temp;
            }         
        }
     
    }

}
