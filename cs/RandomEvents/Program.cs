﻿using System;
// See https://aka.ms/new-console-template for more information
Random rnd = new Random();

/*
for (int i = 0; i < 3; i++)
{
    Console.WriteLine(rnd.Next(5, 10) + "\n");
}

for (int i = 0; i < 3; i++)
{
    Console.WriteLine((float)rnd.NextDouble() + "\n");
}

string[] malePetNames = { "Rufus", "Bear", "Dakota", "Fido",
                          "Vanya", "Samuel", "Koani", "Volodya",
                          "Prince", "Yiska" };
string[] femalePetNames = { "Maggie", "Penny", "Saya", "Princess",
                            "Abby", "Laila", "Sadie", "Olivia",
                            "Starlight", "Talla" };

// Generate random indexes for pet names.
int mIndex = rnd.Next(malePetNames.Length);
int fIndex = rnd.Next(femalePetNames.Length);

// Display the result.
Console.WriteLine("Suggested pet name of the day: ");
Console.WriteLine("   For a male:     {0}", malePetNames[mIndex]);
Console.WriteLine("   For a female:   {0}", femalePetNames[fIndex]);
*/

float sum = 0;
int cnt = 30000;
float lambda = 3;

for (int i = 0; i < cnt; i++)
{
    float arrival, U;
    U = (float)rnd.NextDouble();
    arrival = (float)(-1 * Math.Log(U)) / lambda;
    sum += arrival;
    Console.WriteLine(arrival + "\n");
}
Console.WriteLine("avg: " + sum / cnt);