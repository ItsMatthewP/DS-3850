import tkinter as tk
from tkinter import ttk
import sqlite3

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Database Viewer")
        self.root.geometry("800x500") # Set a default size

        # Configure the style for the Treeview
        style = ttk.Style()
        style.configure("Treeview", 
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        # Change the selected color
        style.map('Treeview', 
                  background=[('selected', '#347083')])

        # Create a frame to hold the Treeview and scrollbars
        tree_frame = tk.Frame(root)
        tree_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Create scrollbars
        tree_scroll_y = tk.Scrollbar(tree_frame)
        tree_scroll_y.pack(side="right", fill="y")
        tree_scroll_x = tk.Scrollbar(tree_frame, orient='horizontal')
        tree_scroll_x.pack(side="bottom", fill="x")

        # Create the Treeview widget
        self.tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set, selectmode="extended")
        self.tree.pack(fill="both", expand=True)
        
        # Configure scrollbars
        tree_scroll_y.config(command=self.tree.yview)
        tree_scroll_x.config(command=self.tree.xview)

        # Define tags for alternating row colors
        self.tree.tag_configure('oddrow', background="white")
        self.tree.tag_configure('evenrow', background="lightblue")

        # Load the data from the database
        self.load_data()

    def load_data(self):
        db_name = 'customers.db'
        # --- IMPORTANT ---
        # Replace 'customers' with the actual name of your table if it's different.
        table_name = 'customers'

        conn = None
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            # Get column names from the cursor description
            column_names = [description[0] for description in cursor.description]
            
            # Clear the old Treeview data
            self.tree.delete(*self.tree.get_children())
            
            # Set up Treeview columns and headings
            self.tree["columns"] = column_names
            self.tree.column("#0", width=0, stretch=tk.NO) # Phantom column
            self.tree.heading("#0", text="", anchor=tk.W)

            for col in column_names:
                self.tree.column(col, anchor=tk.W, width=120)
                self.tree.heading(col, text=col, anchor=tk.W)
            
            # Insert data into the Treeview with alternating row colors
            for i, row in enumerate(rows):
                if i % 2 == 0:
                    self.tree.insert(parent='', index='end', iid=i, text="", values=row, tags=('evenrow',))
                else:
                    self.tree.insert(parent='', index='end', iid=i, text="", values=row, tags=('oddrow',))

        except sqlite3.Error as e:
            # You could show a pop-up error message here
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

# Main execution block
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()