using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using SportsPro.Models;
namespace SportsPro.Controllers
{
    public class ProductsController : Controller
    {
        private SportsProContext context { get; set; }
        public IActionResult Index(SportsProContext ctx)
        {
            context = ctx;
            return View();
        }
    }
}
