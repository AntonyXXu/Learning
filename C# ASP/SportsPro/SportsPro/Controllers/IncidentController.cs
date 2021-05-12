using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using SportsPro.Models;

namespace SportsPro.Controllers
{
    public class IncidentController : Controller
    {
        private SportsProContext context { get; set; }
        public IncidentController(SportsProContext ctx)
        {
            context = ctx;
        }

        public IActionResult List()
        {
            List<Incident> incidents = context.Incidents.ToList();
            return View(incidents);
        }


        [HttpGet]
        public IActionResult Add()
        {
            return View(new Incident());
        }

        [HttpGet]
        public IActionResult Edit(int id)
        {
            Incident tech = context.Incidents.Find(id);
            return View(tech);
        }

        [HttpPost]
        public IActionResult Add(Incident incident)
        {
            try
            {
                context.Incidents.Add(incident);
                context.SaveChanges();
                return RedirectToAction("List", "Incident");
            }
            catch
            {
                return View();
            }
        }

        [HttpPost]
        public IActionResult Edit(Incident incident)
        {
            try
            {
                context.Incidents.Update(incident);
                context.SaveChanges();
                return RedirectToAction("List", "Incident");
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
                Incident incident = context.Incidents.Find(id);
                context.Incidents.Remove(incident);
                context.SaveChanges();
                return RedirectToAction("List", "Incident");
            }
            catch
            {
                return View("List");
            }
        }

    }
}
