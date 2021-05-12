using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using SportsPro.Models;

namespace SportsPro.Controllers
{
    public class ProductController : Controller
    {
        private SportsProContext context { get; set; }
        public ProductController(SportsProContext ctx)
        {
            context = ctx;

        }

        public IActionResult List()
        {
            List<Product> products = context.Products.ToList();
            return View(products);
        }
    }
}
