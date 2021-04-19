using System;

namespace CLI_day1_project
{
    class Student
    {
        public int ID;
        public string fname;
        public string lname;
        public DateTime DOB;
        public void print()
        {
            Console.WriteLine(fname + " " + lname + " " + DOB);
        }
    }
}