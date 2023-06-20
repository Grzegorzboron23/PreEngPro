class Queue:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def remove_command(self):
        if self.commands:
            return self.commands.pop(0)
        else:
            return None

    def get_queue_as_string(self):
        return ', '.join(self.commands)

# Przykładowe użycie
if __name__ == "__main__":

    queue = Queue()
    queue.add_command("Komenda 1")
    queue.add_command("Komenda 2")
    queue.add_command("Komenda 3")

    print(queue.get_queue_as_string())  # Wyświetli: Komenda 1, Komenda 2, Komenda 3

    removed_command = queue.remove_command()
    if removed_command:
        print("Usunięta komenda:", removed_command)  # Wyświetli: Usunięta komenda: Komenda 1

    print(queue.get_queue_as_string())  # Wyświetli: Komenda 2, Komenda 3
