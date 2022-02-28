using System.Globalization; // for CultureInfo

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

DateTime centuryBegin = new DateTime(2001, 1, 1);
DateTime currentDate = DateTime.Now;

long elapsedTicks = currentDate.Ticks - centuryBegin.Ticks;
TimeSpan elapsedSpan = new TimeSpan(elapsedTicks);

Console.WriteLine("Elapsed from the beginning of the century to {0:f}:",
                   currentDate);
Console.WriteLine("   {0:N0} nanoseconds", elapsedTicks * 100);
Console.WriteLine("   {0:N0} ticks", elapsedTicks);
Console.WriteLine("   {0:N2} seconds", elapsedSpan.TotalSeconds);
Console.WriteLine("   {0:N2} minutes", elapsedSpan.TotalMinutes);
Console.WriteLine("   {0:N0} days, {1} hours, {2} minutes, {3} seconds",
                  elapsedSpan.Days, elapsedSpan.Hours,
                  elapsedSpan.Minutes, elapsedSpan.Seconds);


DateTime gazeDate = new DateTime(1000000457821391053);
Console.WriteLine("Log Date: {0}", gazeDate);

DateTime logDate = new DateTime(63777415019402 * 10000);
Console.WriteLine("Log Date: {0}", logDate);

String logDateString = logDate.ToString("yyyy-MM-dd HH:mm:ss.fff",
                                            CultureInfo.InvariantCulture);
Console.WriteLine("Log Date: {0}", logDateString);