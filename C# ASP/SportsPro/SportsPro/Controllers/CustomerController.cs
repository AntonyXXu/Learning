using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using SportsPro.Models;

namespace SportsPro.Controllers
{
    public class CustomerController : Controller
    {
        private SportsProContext context { get; set; }
        public CustomerController(SportsProContext ctx)
        {
            context = ctx;

        }

        public IActionResult List()
        {
            List<Customer> customers = context.Customers.ToList();
            return View(customers);
        }

        [HttpGet]
        public IActionResult Add()
        {
            ViewBag.Country = context.Countries.ToList();
            return View(new Customer());
        }

        [HttpGet]
        public IActionResult Edit(int id)
        {
            Customer cust = context.Customers.Find(id);
            return View(cust);
        }

        [HttpPost]
        public IActionResult Add(Customer cust)
        {
            try
            {
                context.Customers.Add(cust);
                context.SaveChanges();
                return RedirectToAction("List", "Customer");
            }
            catch
            {
                return View();
            }
        }

        [HttpPost]
        public IActionResult Edit(Customer cust)
        {
            try
            {
                context.Customers.Update(cust);
                context.SaveChanges();
                return RedirectToAction("List", "Customer");
            }
            catch
            {
                return View();
            }
        }

        [HttpPost]
        public IActionResult Delete(int id)
        {
            try
            {
                Customer cust = context.Customers.Find(id);
                context.Customers.Remove(cust);
                context.SaveChanges();
                return RedirectToAction("List", "Customer");
            }
            catch
            {
                return View("List");
            }
        }
    }
}
