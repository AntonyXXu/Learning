using Microsoft.VisualStudio.TestTools.UnitTesting;
using ClassesAggregationCards;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassesAggregationCards.Tests
{
    [TestClass()]
    public class CardTests
    {
        [TestMethod()]
        public void CardTest()
        {
            Card crd;
            Rank rank = (Rank)1;
            Suit suit = (Suit)4;
            crd = new Card(suit, rank);
            Assert.IsNotNull(crd);
        }
    }
}