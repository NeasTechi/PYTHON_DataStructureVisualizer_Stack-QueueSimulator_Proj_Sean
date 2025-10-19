import tkinter as tk
from tkinter import ttk, messagebox
import time


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return self.items.copy()


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return self.items.copy()


class DataStructureVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Stack & Queue Visualizer")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        # Initialize data structures
        self.stack = Stack()
        self.queue = Queue()
        self.current_structure = "stack"  # Default to stack

        self.setup_gui()

    def setup_gui(self):
        # Title
        title_label = tk.Label(self.root, text="Stack & Queue Visualizer",
                               font=('Arial', 20, 'bold'), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=10)

        # Structure selection frame
        selection_frame = tk.Frame(self.root, bg='#f0f0f0')
        selection_frame.pack(pady=10)

        tk.Label(selection_frame, text="Select Data Structure:",
                 font=('Arial', 12), bg='#f0f0f0').pack(side=tk.LEFT, padx=5)

        self.structure_var = tk.StringVar(value="stack")
        stack_radio = tk.Radiobutton(selection_frame, text="Stack", variable=self.structure_var,
                                     value="stack", command=self.switch_structure, bg='#f0f0f0')
        queue_radio = tk.Radiobutton(selection_frame, text="Queue", variable=self.structure_var,
                                     value="queue", command=self.switch_structure, bg='#f0f0f0')
        stack_radio.pack(side=tk.LEFT, padx=5)
        queue_radio.pack(side=tk.LEFT, padx=5)

        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter value:", font=(
            'Arial', 12), bg='#f0f0f0').pack(side=tk.LEFT, padx=5)
        self.entry = tk.Entry(input_frame, font=('Arial', 12), width=15)
        self.entry.pack(side=tk.LEFT, padx=5)
        self.entry.bind('<Return>', lambda e: self.add_element())

        # Operations frame
        operations_frame = tk.Frame(self.root, bg='#f0f0f0')
        operations_frame.pack(pady=10)

        # Stack operations
        self.stack_buttons_frame = tk.Frame(operations_frame, bg='#f0f0f0')
        self.stack_buttons_frame.pack()

        tk.Button(self.stack_buttons_frame, text="Push", command=self.push_element,
                  bg='#4CAF50', fg='white', font=('Arial', 11), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.stack_buttons_frame, text="Pop", command=self.pop_element,
                  bg='#f44336', fg='white', font=('Arial', 11), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.stack_buttons_frame, text="Peek", command=self.peek_element,
                  bg='#2196F3', fg='white', font=('Arial', 11), width=10).pack(side=tk.LEFT, padx=5)

        # Queue operations (initially hidden)
        self.queue_buttons_frame = tk.Frame(operations_frame, bg='#f0f0f0')

        tk.Button(self.queue_buttons_frame, text="Enqueue", command=self.enqueue_element,
                  bg='#4CAF50', fg='white', font=('Arial', 11), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.queue_buttons_frame, text="Dequeue", command=self.dequeue_element,
                  bg='#f44336', fg='white', font=('Arial', 11), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(self.queue_buttons_frame, text="Front", command=self.front_element,
                  bg='#2196F3', fg='white', font=('Arial', 11), width=10).pack(side=tk.LEFT, padx=5)

        # Display frame
        display_frame = tk.Frame(self.root, bg='#f0f0f0')
        display_frame.pack(pady=20)

        # Structure visualization
        self.canvas = tk.Canvas(display_frame, width=600, height=300,
                                bg='white', highlightthickness=2, highlightbackground='#ccc')
        self.canvas.pack()

        # Info frame
        info_frame = tk.Frame(self.root, bg='#f0f0f0')
        info_frame.pack(pady=10)

        self.info_label = tk.Label(info_frame, text="Welcome! Select Stack or Queue and start operations.",
                                   font=('Arial', 12), bg='#f0f0f0', fg='#333')
        self.info_label.pack()

        # Status frame
        status_frame = tk.Frame(self.root, bg='#f0f0f0')
        status_frame.pack(pady=5)

        self.status_label = tk.Label(status_frame, text="Stack: Empty | Size: 0",
                                     font=('Arial', 10), bg='#f0f0f0', fg='#666')
        self.status_label.pack()

        # Initialize display
        self.switch_structure()

    def switch_structure(self):
        self.current_structure = self.structure_var.get()

        if self.current_structure == "stack":
            self.stack_buttons_frame.pack()
            self.queue_buttons_frame.pack_forget()
            self.update_display()
            self.update_status()
        else:
            self.stack_buttons_frame.pack_forget()
            self.queue_buttons_frame.pack()
            self.update_display()
            self.update_status()

    def add_element(self):
        value = self.entry.get().strip()
        if value:
            if self.current_structure == "stack":
                self.push_element(value)
            else:
                self.enqueue_element(value)
            self.entry.delete(0, tk.END)

    def push_element(self, value=None):
        if value is None:
            value = self.entry.get().strip()
            if not value:
                messagebox.showwarning(
                    "Input Error", "Please enter a value to push")
                return
            self.entry.delete(0, tk.END)

        self.stack.push(value)
        self.animate_operation("push", value)
        self.update_display()
        self.update_status()
        self.info_label.config(text=f"Pushed '{value}' onto the stack")

    def pop_element(self):
        if self.stack.is_empty():
            messagebox.showwarning(
                "Stack Empty", "Cannot pop from an empty stack!")
            return

        value = self.stack.pop()
        self.animate_operation("pop", value)
        self.update_display()
        self.update_status()
        self.info_label.config(text=f"Popped '{value}' from the stack")

    def peek_element(self):
        if self.stack.is_empty():
            messagebox.showinfo("Stack Empty", "Stack is empty!")
            return

        value = self.stack.peek()
        self.highlight_element("top", value)
        self.info_label.config(text=f"Top element: '{value}'")

    def enqueue_element(self, value=None):
        if value is None:
            value = self.entry.get().strip()
            if not value:
                messagebox.showwarning(
                    "Input Error", "Please enter a value to enqueue")
                return
            self.entry.delete(0, tk.END)

        self.queue.enqueue(value)
        self.animate_operation("enqueue", value)
        self.update_display()
        self.update_status()
        self.info_label.config(text=f"Enqueued '{value}' into the queue")

    def dequeue_element(self):
        if self.queue.is_empty():
            messagebox.showwarning(
                "Queue Empty", "Cannot dequeue from an empty queue!")
            return

        value = self.queue.dequeue()
        self.animate_operation("dequeue", value)
        self.update_display()
        self.update_status()
        self.info_label.config(text=f"Dequeued '{value}' from the queue")

    def front_element(self):
        if self.queue.is_empty():
            messagebox.showinfo("Queue Empty", "Queue is empty!")
            return

        value = self.queue.front()
        self.highlight_element("front", value)
        self.info_label.config(text=f"Front element: '{value}'")

    def animate_operation(self, operation, value):
        # Simple animation by temporarily changing colors
        self.canvas.configure(bg='#e8f5e8')
        self.root.update()
        time.sleep(0.3)
        self.canvas.configure(bg='white')
        self.root.update()

    def highlight_element(self, position, value):
        # Highlight specific element (top/front)
        self.canvas.delete("highlight")
        items = self.stack.display() if self.current_structure == "stack" else self.queue.display()

        if self.current_structure == "stack" and position == "top" and items:
            x = 300
            y = 100 - (len(items) - 1) * 40
            self.canvas.create_rectangle(
                x-40, y-15, x+40, y+15, fill='#FFEB3B', outline='#FFC107', tags="highlight")
        elif self.current_structure == "queue" and position == "front" and items:
            x = 150
            y = 150
            self.canvas.create_rectangle(
                x-40, y-15, x+40, y+15, fill='#FFEB3B', outline='#FFC107', tags="highlight")

    def update_display(self):
        self.canvas.delete("all")

        if self.current_structure == "stack":
            self.draw_stack()
        else:
            self.draw_queue()

    def draw_stack(self):
        items = self.stack.display()

        # Draw stack base
        self.canvas.create_rectangle(
            250, 250, 350, 260, fill='#795548', outline='#5D4037')
        self.canvas.create_text(
            300, 270, text="Stack Base", font=('Arial', 10))

        # Draw stack elements
        for i, item in enumerate(reversed(items)):
            y_pos = 250 - (i * 40)
            # Top element different color
            color = '#4CAF50' if i == len(items) - 1 else '#2196F3'

            # Element rectangle
            self.canvas.create_rectangle(
                260, y_pos-15, 340, y_pos+15, fill=color, outline='#1976D2', width=2)
            self.canvas.create_text(300, y_pos, text=str(
                item), font=('Arial', 12, 'bold'), fill='white')

            # Stack pointer for top element
            if i == 0:
                self.canvas.create_text(350, y_pos, text="↑ TOP", font=(
                    'Arial', 10, 'bold'), fill='#D32F2F', anchor='w')

        # Draw stack info
        if not items:
            self.canvas.create_text(
                300, 150, text="Stack is Empty", font=('Arial', 14), fill='#666')

    def draw_queue(self):
        items = self.queue.display()

        # Draw queue line
        self.canvas.create_line(100, 200, 500, 200, fill='#666', width=3)

        # Draw queue elements
        for i, item in enumerate(items):
            x_pos = 150 + (i * 80)
            color = '#4CAF50' if i == 0 else '#2196F3'  # Front element different color

            # Element rectangle
            self.canvas.create_rectangle(
                x_pos-40, 185, x_pos+40, 215, fill=color, outline='#1976D2', width=2)
            self.canvas.create_text(x_pos, 200, text=str(
                item), font=('Arial', 12, 'bold'), fill='white')

        # Draw front and rear pointers
        if items:
            self.canvas.create_text(150, 170, text="FRONT", font=(
                'Arial', 10, 'bold'), fill='#D32F2F')
            self.canvas.create_text(
                150 + (len(items)-1)*80, 170, text="REAR", font=('Arial', 10, 'bold'), fill='#D32F2F')

        # Draw queue info
        if not items:
            self.canvas.create_text(
                300, 150, text="Queue is Empty", font=('Arial', 14), fill='#666')

        # Draw direction arrow
        self.canvas.create_text(
            300, 230, text="→ Direction of movement →", font=('Arial', 10), fill='#666')

    def update_status(self):
        if self.current_structure == "stack":
            status = f"Stack: {'Empty' if self.stack.is_empty() else f'{self.stack.size()} elements'} | Size: {
                self.stack.size()}"
            if not self.stack.is_empty():
                status += f" | Top: {self.stack.peek()}"
        else:
            status = f"Queue: {'Empty' if self.queue.is_empty() else f'{self.queue.size()} elements'} | Size: {
                self.queue.size()}"
            if not self.queue.is_empty():
                status += f" | Front: {self.queue.front()}"

        self.status_label.config(text=status)


def main():
    root = tk.Tk()
    app = DataStructureVisualizer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
