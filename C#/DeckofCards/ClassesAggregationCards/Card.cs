using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassesAggregationCards
{
    // enumeration types for the card rank and suit
    public enum Rank { Ace = 1, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King }
    public enum Suit { Club, Diamond, Heart, Spade }


    // represents a playing card
    public class Card
    {
        // private data: rank and suit
        private Rank r;
        private Suit s;
        // public readonly properties
        public Rank rank { get { return r; } }
        public Suit suit { get { return s; } }

        // constructor with parameters
        public Card(Suit newSuit, Rank newRank)
        {
            s = newSuit;
            r = newRank;
        }

        // overriden  ToString method
        public override string ToString()
        {
            // return "The " + rank + " of " + suit + "s";
            char[] suitChar = { '\u2663', '\u2666', '\u2665', '\u2660' };
            string[] rankString = { "", " A", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", " J", " Q", " K" };
            return rankString[(int)r] + suitChar[(int)s].ToString();
        }
    }
}
