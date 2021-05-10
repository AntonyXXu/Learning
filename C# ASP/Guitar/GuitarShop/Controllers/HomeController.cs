using Microsoft.AspNetCore.Mvc;

namespace GuitarShop.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            ViewBag.Name = "Test";
            return View();
        }

        public IActionResult About()
        {
            ViewBag.Name = "Test";
            return View();
        }
    }
}