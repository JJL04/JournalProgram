from journal import Journal

def main():
    journal = Journal()
    journal.load()

    while True:
        print("1. Add journal entry")
        print("2. Display journal entries")
        print("3. Save journal")
        print("4. Load journal")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            entry_text = input(f"Your prompt: {journal.get_random_prompt()}\nYour entry: ")
            journal.add_entry(entry_text)
        elif choice == "2":
            journal.display_entries()
        elif choice == "3":
            journal.save()
            print("Journal saved.")
        elif choice == "4":
            journal.load()
            print("Journal loaded.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
