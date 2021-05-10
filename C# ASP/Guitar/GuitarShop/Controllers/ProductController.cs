using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using GuitarShop.Models;

namespace GuitarShop.Controllers
{
    public class ProductController : Controller
    {
        public IActionResult Detail(string id)
        {
            ViewBag.Name = "Test";
            Product product = DB.GetProduct(id);
            return View(product);
        }

        public IActionResult List()
        {
            ViewBag.Name = "Test";
            List<Product> products = DB.GetProducts();
            return View(products);
        }
    }
}