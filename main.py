from tkinter import ttk
import tkinter as tk  # Import necessary modules for user interface
import networkx as nx  # Import necessary modules for graph creation and short path calculation
from networkx.algorithms import bellman_ford_path  # Import bellman ford short path algorithim.

# ================================================= Variables ==============================================================================================

Town_list = ['Nairobi', 'Athi River', 'Kikuyu', 'Ongata Rongai', 'Ruiru', 'Kiambu', 'Tala', 'Kitengela', 'Juja', 'Thika', 'Machakos', 'Kiserian', '']
Back_Ground_color = 'gray'


# ================================================== Functions =============================================================================================
def short_path_search(starting_location, destination):
            if starting_location == '':
                u = tk.Label(root_window, text='X', bg=Back_Ground_color, font=('Agency FB', 14, 'bold'), fg='red', anchor='center')
                u.place(relheight=0.05, relwidth=0.04, rely=0.4, relx=0.84)
                u.after(2000, lambda: u.destroy())

            if destination == '':
                d = tk.Label(root_window, text='X', bg=Back_Ground_color, font=('Agency FB', 14, 'bold'), fg='red', anchor='center')
                d.place(relheight=0.05, relwidth=0.04, rely=0.5, relx=0.84)
                d.after(2000, lambda: d.destroy())

            print(starting_location)
            print(destination)
            if (destination and starting_location) != '':
                    # Define the graph representing the network
                    G = nx.Graph()

                    # Add edges to the graph, representing the roads or routes between locations
                    G.add_edge('Nairobi', 'Athi River', weight=10)
                    G.add_edge('Nairobi', 'Kikuyu', weight=7)
                    G.add_edge('Nairobi', 'Ongata Rongai', weight=6)
                    G.add_edge('Nairobi', 'Ruiru', weight=16)
                    G.add_edge('Nairobi', 'Kiambu', weight=18)
                    G.add_edge('Nairobi', 'Tala', weight=55)
                    G.add_edge('Athi River', 'Kitengela', weight=8)
                    G.add_edge('Athi River', 'Ongata Rongai', weight=5)
                    G.add_edge('Athi River', 'Machakos', weight=20)
                    G.add_edge('Kikuyu', 'Ongata Rongai', weight=9)
                    G.add_edge('Machakos', 'Tala', weight=11)
                    G.add_edge('Ruiru', 'Juja', weight=7)
                    G.add_edge('Ruiru', 'Kiambu', weight=12)
                    G.add_edge('Juja', 'Thika', weight=4)
                    G.add_edge('Ongata Rongai', 'Kiserian', weight=11)

                    # Calculate the shortest path from the starting location to the destination
                    p = bellman_ford_path(G, starting_location, destination, weight='weight')
                    s = '> '
                    for i in range(len(p) - 1):
                        s = s + p[i] + " -> "
                    s = s + p[-1]
                    message = f'Shortest Route To Your Destination\n \n {s}'
                    text_box.config(state='normal')
                    text_box.delete(1.0, 'end')
                    text_box.insert('end', message)
                    text_box.config(state='disabled')


# ====================================== User InterFace =================================================================================================================
root_window = tk.Tk()
root_window.minsize(900, 850)
root_window.maxsize(900, 850)
root_window.config(bg=Back_Ground_color)
root_window.title("Nangulu Hezron Wekesa")
tk.Label(root_window, text='best route for a driver', bg=Back_Ground_color,font=('Algerian', 30)).place(relheight=0.1, relwidth=0.8, relx=0.1, rely=0.1)

S_location = tk.StringVar()  # start location variable
E_destination = tk.StringVar()  # End location variable

Start_Location_Entry = tk.Label(root_window, text='Start Location :', bg=Back_Ground_color, font=('Algerian', 14, 'bold'), anchor='e')
Start_Location_Entry.place(relheight=0.05, relwidth=0.25, rely=0.4, relx=0.15)
Start_Location_Entry = ttk.Combobox(state="readonly", values=Town_list, font=('Courier New', 14))
Start_Location_Entry.place(relheight=0.05, relwidth=0.38, rely=0.4, relx=0.45)

End_Location_Lable = tk.Label(root_window, text='End Location :', bg=Back_Ground_color, font=('Algerian', 14, 'bold'), anchor='e')
End_Location_Lable.place(relheight=0.05, relwidth=0.25, rely=0.5, relx=0.15)
End_Location_Entry = ttk.Combobox(state="readonly", values=Town_list, font=('Courier New', 14))
End_Location_Entry.place(relheight=0.05, relwidth=0.38, rely=0.5, relx=0.45)

tk.Button(root_window, text='SEARCH', activebackground='green', activeforeground='black', bg=Back_Ground_color, font=('Agency FB', 14, 'bold'), anchor='center',  command=lambda: short_path_search(Town_list[Start_Location_Entry.current()], Town_list[End_Location_Entry.current()])).place(relheight=0.05, relwidth=0.2, rely=0.57, relx=0.45)

text_box = tk.Text( root_window, font=('Consolas', 12, 'bold'), bg=Back_Ground_color)
text_box.place(relheight=0.25, relwidth=0.7, rely=0.65, relx=0.15)
text_box.config(state='disabled')

root_window.mainloop()
# ====================================== End ========================================================================================================================




