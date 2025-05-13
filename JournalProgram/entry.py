using System;

namespace JournalProgram
{
    [Serializable]  // Enables serialization
    public class Entry
    {
        public string Text { get; set; }
        public string Prompt { get; set; }
        public DateTime Date { get; set; }

        public Entry(string text, string prompt, DateTime date)
        {
            Text = text;
            Prompt = prompt;
            Date = date;
        }

        public override string ToString()
        {
            return $"Date: {Date}\nPrompt: {Prompt}\nEntry: {Text}\n" + new string('-', 20);
        }
    }
}
