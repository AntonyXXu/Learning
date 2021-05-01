﻿using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.EntityFrameworkCore;

#nullable disable

namespace ProductMaintenance.Models
{
    public partial class Product
    {
        public Product()
        {
            Incidents = new HashSet<Incident>();
            Registrations = new HashSet<Registration>();
        }

        [Key]
        [StringLength(10)]
        public string ProductCode { get; set; }
        [Required]
        [StringLength(50)]
        public string Name { get; set; }
        [Column(TypeName = "decimal(18, 1)")]
        public decimal Version { get; set; }
        [Column(TypeName = "datetime")]
        public DateTime ReleaseDate { get; set; }

        [InverseProperty(nameof(Incident.ProductCodeNavigation))]
        public virtual ICollection<Incident> Incidents { get; set; }
        [InverseProperty(nameof(Registration.ProductCodeNavigation))]
        public virtual ICollection<Registration> Registrations { get; set; }

        public override string ToString()
        {
            return ProductCode.PadRight(15) + Name.PadRight(40) + 
                Version.ToString("0.#").PadRight(8) + ReleaseDate.ToString("d");
        }
    }
}
