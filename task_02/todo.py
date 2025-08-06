
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file into the tasks list"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            self.tasks = []
    
    def save_tasks(self):
        """Save current tasks list to file"""
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")
    
    def add_task(self, task):
        """Add a new task to the list"""
        if task.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            formatted_task = f"[{timestamp}] {task.strip()}"
            self.tasks.append(formatted_task)
            self.save_tasks()
            print(f"✅ Added: {task.strip()}")
        else:
            print("❌ Can't add empty task!")
    
    def remove_task(self, index):
        """Remove task by index"""
        try:
            index = int(index) - 1  # Convert to 0-based index
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                self.save_tasks()
                print(f"🗑️  Removed: {removed_task}")
            else:
                print(f"❌ Invalid task number! Pick between 1-{len(self.tasks)}")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_tasks(self):
        """Display all tasks with numbers"""
        if not self.tasks:
            print("📝 Your to-do list is empty! Time to add some tasks.")
            return
        
        print("\n📋 Your Tasks:")
        print("-" * 50)
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("-" * 50)
        print(f"Total tasks: {len(self.tasks)}")
    
    def clear_all_tasks(self):
        """Clear all tasks after confirmation"""
        if not self.tasks:
            print("📝 Nothing to clear - your list is already empty!")
            return
        
        confirm = input("⚠️  Clear ALL tasks? This can't be undone! (y/N): ")
        if confirm.lower() in ['y', 'yes']:
            self.tasks.clear()
            self.save_tasks()
            print("🧹 All tasks cleared!")
        else:
            print("Cancelled - tasks kept safe!")
    
    def show_help(self):
        """Display help menu"""
        print("""
🎯 TO-DO APP COMMANDS:
    add <task>     - Add a new task
    remove <num>   - Remove task by number
    view           - Show all tasks
    clear          - Clear all tasks
    help           - Show this help
    quit/exit      - Exit the app

Examples:
    add Buy groceries
    remove 2
    view
        """)
    
    def run(self):
        """Main application loop"""
        print("🎯 Welcome to Your To-Do List!")
        print("Type 'help' for commands or 'quit' to exit\n")
        
        while True:
            try:
                user_input = input("todo> ").strip()
                
                if not user_input:
                    continue
                
                # Parse command and arguments
                parts = user_input.split(' ', 1)
                command = parts[0].lower()
                
                if command in ['quit', 'exit', 'q']:
                    print("👋 Goodbye! Stay productive!")
                    break
                
                elif command == 'add':
                    if len(parts) > 1:
                        self.add_task(parts[1])
                    else:
                        print("❌ Usage: add <task description>")
                
                elif command in ['remove', 'rm', 'delete']:
                    if len(parts) > 1:
                        self.remove_task(parts[1])
                    else:
                        print("❌ Usage: remove <task number>")
                
                elif command in ['view', 'list', 'show']:
                    self.view_tasks()
                
                elif command == 'clear':
                    self.clear_all_tasks()
                
                elif command == 'help':
                    self.show_help()
                
                else:
                    print(f"❌ Unknown command: '{command}'. Type 'help' for available commands.")
                
                print()  # Add space between commands
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye! Stay productive!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")

def main():
    app = TodoApp()
    app.run()

if __name__ == "__main__":
    main()