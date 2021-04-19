using System;

namespace CLI_day1_project
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Student std = new Student();
            std.ID = 1;
            std.DOB = new DateTime(2000, 5, 15);
            std.fname = "ab";
            std.lname = "ba";
            std.print();
        }
    }
}

