#Importing Necessary Modules
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import Entry
from tkinter import filedialog
from tkinter import ttk  
import csv





# Initialize main Tkinter window
root = tk.Tk()
root.title("YourChart: V 1.1")
root.geometry("1000x600")  # Increased default size for larger content

#Setting logo of the window
icon_image = tk.PhotoImage(file="/Users/sakethvelagaleti/Documents/logo.png")
root.iconphoto(False, icon_image)

# Create frames for options and main content with original colors
options_frame = tk.Frame(root, bg='#2f3e46')  # Dark teal background for sidebar
main_frame = tk.Frame(root, highlightbackground='red', highlightthickness=4)

# Position frames
options_frame.pack(side=tk.LEFT, fill=tk.Y)
options_frame.pack_propagate(False)
options_frame.configure(width=300, height=600)

main_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
main_frame.pack_propagate(False)
main_frame.configure(height=600, width=600)

# Function to hide all frames in main content area
def hide_all_frames():
    for widget in main_frame.winfo_children():
        widget.pack_forget()

# Function to reset indicator colors to default
def hide_indicator():
   home_ind.config(bg="#2f3e46")
   pie_ind.config(bg="#2f3e46")
   scat_ind.config(bg="#2f3e46")
   bar_ind.config(bg="#2f3e46")
   bar2_ind.config(bg="#2f3e46")
   hist_ind.config(bg="#2f3e46")
   line1_ind.config(bg="#2f3e46")
   line2_ind.config(bg="#2f3e46")
   csv_ind.config(bg="#2f3e46")

# Function to highlight selected button indicator and show corresponding frame
def indicator(lb, page_func):
    hide_indicator()
    lb.config(bg='orange')  # Set indicator color to orange for active page
    hide_all_frames()
    page_func()

#Homepage
def home_page():
    home_frame = tk.Frame(main_frame, bg="#f7f1e3") 
    home_frame.pack(pady=20)
    hide_all_frames()
    hide_indicator()
    home_ind.config(bg='orange')
    home_frame.pack(fill=tk.BOTH, expand=True)
    
    # Welcome Heading
    welcome_label = tk.Label(home_frame, text="Welcome to YourCharts - Simple Steps, Big Results", font=("Arial", 24, "bold"), bg="#4a90e2", fg="white", pady=20)
    welcome_label.pack(fill=tk.X)
    
    # Content Text
    creator_label = tk.Label(home_frame, text="Created by Saketh Velagaleti, a Freshman at Chamblee High School", font=("Arial", 16), bg="#dff9fb", fg="#130f40", pady=10)
    creator_label.pack(fill=tk.X, pady=10)
    
    # Updates Heading
    updates_label = tk.Label(home_frame, text="Updates", font=("Arial", 20, "bold"), bg="#badc58", fg="#30336b", pady=10)
    updates_label.pack(fill=tk.X, pady=(20, 0))
    
    update_message = tk.Label(home_frame, text="YourCharts Version 1.1 is Finally ready! We have gone through Alpha and Beta testing phases!", 
    font=("Arial", 16), bg="#f8c291", fg="#30336b", pady=10)
    update_message.pack(fill=tk.X, pady=10)
# Sidebar Buttons with larger font and size
button_font = ('Bold', 20)
home_btn = tk.Button(options_frame, text="Homepage", font=button_font, fg='blue', bd=0, command=home_page)
home_btn.place(x=20, y=30, width=250, height=50)
home_ind = tk.Label(options_frame, text='', bg='#c3c3c3')
home_ind.place(x=10, y=30, width=10, height=50)


# Pie Chart Page
def pie_page():
    pie_frame = tk.Frame(main_frame, bg="#e8eaf6")
    pie_frame.pack(pady=20)
    hide_all_frames()
    hide_indicator()
    pie_ind.config(bg='blue')
    pie_frame.pack(fill=tk.BOTH, expand=True)

    def pie_graph():
        
        for widget in pie_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
            
        labels = label_entry.get().split(",")
        sizes = list(map(float, num_entry.get().split(",")))
        title = title_entry.get()
        
        fig, ax = plt.subplots(figsize=(11,9))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title(title)
        plt.legend(labels, loc="best")
        ax.axis('equal')
        
        # Clear existing canvas widgets
        for widget in pie_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
        
        # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=pie_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        download_btn = tk.Button(pie_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
        
        
        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")

    # Input fields and button for pie chart with larger font
    font_large = ('Arial', 20)
    tk.Label(pie_frame, text="Please Enter the following information to create your pie chart", font=font_large).pack(pady=10)
    tk.Label(pie_frame, text="Enter your labels", font=font_large).pack(pady=5)
    label_entry = Entry(pie_frame, font=font_large, width=30)
    label_entry.pack()
    tk.Label(pie_frame, text="Enter your section sizes (corresponding to labels)", font=font_large).pack(pady=5)
    num_entry = Entry(pie_frame, font=font_large, width=30)
    num_entry.pack()
    tk.Label(pie_frame, text="Enter a title", font=font_large).pack(pady=5)
    title_entry = Entry(pie_frame, font=font_large, width=30)
    title_entry.pack()
    tk.Button(pie_frame, text="Generate Pie Chart", font=('Bold', 22), fg='blue', bd=0, command=pie_graph).pack(pady=20)

# Scatterplot Page
def scat_page():
    scat_frame = tk.Frame(main_frame, bg="#e0f7fa")
    scat_frame.pack(pady=20)
    hide_all_frames()
    hide_indicator()
    scat_ind.config(bg='blue')
    scat_frame.pack(fill=tk.BOTH, expand=True)

    def scat_graph():
        
        for widget in scat_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
        xs = list(map(float, x_entry.get().split(",")))
        ys = list(map(float, y_entry.get().split(",")))
        title = t_entry.get()
        xlab = p_entry.get()
        ylab = i_entry.get()
        color = col_entry.get()
        
        fig, ax = plt.subplots(figsize=(11,9))
        ax.scatter(xs, ys, color=color)
        ax.set_xlabel(xlab)
        ax.set_ylabel(ylab)
        ax.set_title(title)
        
        # Clear existing canvas widgets
        for widget in scat_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
        
        # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=scat_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        download_btn = tk.Button(scat_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
        
        
        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")

    # Input fields and button for scatterplot with larger font
    font_large = ('Arial', 20)
    tk.Label(scat_frame, text="Please Enter the following information to create your scatterplot", font=font_large).pack(pady=10)
    tk.Label(scat_frame, text="Enter your x-axis values", font=font_large).pack(pady=5)
    x_entry = Entry(scat_frame, font=font_large, width=30)
    x_entry.pack()
    tk.Label(scat_frame, text="Enter your y-axis values (corresponding to x-axis values)", font=font_large).pack(pady=5)
    y_entry = Entry(scat_frame, font=font_large, width=30)
    y_entry.pack()
    tk.Label(scat_frame, text="Enter a title", font=font_large).pack(pady=5)
    t_entry = Entry(scat_frame, font=font_large, width=30)
    t_entry.pack()
    tk.Label(scat_frame, text="Enter an x-axis label", font=font_large).pack(pady=5)
    p_entry = Entry(scat_frame, font=font_large, width=30)
    p_entry.pack()
    tk.Label(scat_frame, text="Enter a y-axis label", font=font_large).pack(pady=5)
    i_entry = Entry(scat_frame, font=font_large, width=30)
    i_entry.pack()
    tk.Label(scat_frame, text="Enter a color for your dots", font=font_large).pack(pady=5)
    col_entry = Entry(scat_frame, font=font_large, width=30)
    col_entry.pack()
    tk.Button(scat_frame, text="Generate Scatterplot", font=('Bold', 22), fg='blue', bd=0, command=scat_graph).pack(pady=20)
    
    
#Bargraph Page

def bar_page():
    
    bar_frame = tk.Frame(main_frame, bg="#ffebee")
    bar_frame.pack(pady = 20)
    hide_all_frames()
    hide_indicator()
    bar_ind.config(bg='blue')
    bar_frame.pack(fill=tk.BOTH, expand=True)
    
    def bar_graph():
        
        for widget in bar_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
            
        x = barx_entry.get().split(",")
        y = list(map(float, bary_entry.get().split(",")))
    
        fig, ax = plt.subplots(figsize=(11, 9))
        ax.bar(x, y, color=barcol_entry.get(), width=0.2)
        ax.set_xlabel(barp_entry.get())
        ax.set_ylabel(bari_entry.get())
        ax.set_title(bart_entry.get())
    
    # Clear existing canvas widgets
        for widget in bar_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=bar_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(bar_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
    

        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")
            
            

    
    font_large = ('Arial', 20)
    tk.Label(bar_frame, text="Please Enter the following information to create your bar graph", font=font_large).pack(pady=10)
    tk.Label(bar_frame, text="Enter your x-axis names", font=font_large).pack(pady=5)
    barx_entry = Entry(bar_frame, font=font_large, width=30)
    barx_entry.pack()
    tk.Label(bar_frame, text="Enter your y-axis values (corresponding to x-axis values)", font=font_large).pack(pady=5)
    bary_entry = Entry(bar_frame, font=font_large, width=30)
    bary_entry.pack()
    tk.Label(bar_frame, text="Enter a title", font=font_large).pack(pady=5)
    bart_entry = Entry(bar_frame, font=font_large, width=30)
    bart_entry.pack()
    tk.Label(bar_frame, text="Enter an x-axis label", font=font_large).pack(pady=5)
    barp_entry = Entry(bar_frame, font=font_large, width=30)
    barp_entry.pack()
    tk.Label(bar_frame, text="Enter a y-axis label", font=font_large).pack(pady=5)
    bari_entry = Entry(bar_frame, font=font_large, width=30)
    bari_entry.pack()
    tk.Label(bar_frame, text="Enter a color for your bars", font=font_large).pack(pady=5)
    barcol_entry = Entry(bar_frame, font=font_large, width=30)
    barcol_entry.pack()
    tk.Button(bar_frame, text="Generate Bar Graph", font=('Bold', 22), fg='blue', bd=0, command=bar_graph).pack(pady=20)
    
    
def bar2_page():
    
    bar2_frame = tk.Frame(main_frame, bg="#ffebee")
    bar2_frame.pack(pady = 20)
    hide_all_frames()
    hide_indicator()
    bar2_ind.config(bg='blue')
    bar2_frame.pack(fill=tk.BOTH, expand=True)
    
    def bar_graph():
        
        for widget in bar2_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
            
        x = list(map(float, bar2x_entry.get().split(",")))
        y = list(map(float, bar2y_entry.get().split(",")))
    
        fig, ax = plt.subplots(figsize=(11, 9))
        ax.bar(x, y, color=bar2col_entry.get(), width=0.2)
        ax.set_xlabel(bar2p_entry.get())
        ax.set_ylabel(bar2i_entry.get())
        ax.set_title(bar2t_entry.get())
    
    # Clear existing canvas widgets
        for widget in bar2_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=bar2_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(bar2_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
    

        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")
            
            

    
    font_large = ('Arial', 20)
    tk.Label(bar2_frame, text="Please Enter the following information to create your bar graph", font=font_large).pack(pady=10)
    tk.Label(bar2_frame, text="Enter your x-axis values", font=font_large).pack(pady=5)
    bar2x_entry = Entry(bar2_frame, font=font_large, width=30)
    bar2x_entry.pack()
    tk.Label(bar2_frame, text="Enter your y-axis values (corresponding to x-axis values)", font=font_large).pack(pady=5)
    bar2y_entry = Entry(bar2_frame, font=font_large, width=30)
    bar2y_entry.pack()
    tk.Label(bar2_frame, text="Enter a title", font=font_large).pack(pady=5)
    bar2t_entry = Entry(bar2_frame, font=font_large, width=30)
    bar2t_entry.pack()
    tk.Label(bar2_frame, text="Enter an x-axis label", font=font_large).pack(pady=5)
    bar2p_entry = Entry(bar2_frame, font=font_large, width=30)
    bar2p_entry.pack()
    tk.Label(bar2_frame, text="Enter a y-axis label", font=font_large).pack(pady=5)
    bar2i_entry = Entry(bar2_frame, font=font_large, width=30)
    bar2i_entry.pack()
    tk.Label(bar2_frame, text="Enter a color for your bars", font=font_large).pack(pady=5)
    bar2col_entry = Entry(bar2_frame, font=font_large, width=30)
    bar2col_entry.pack()
    tk.Button(bar2_frame, text="Generate Bar Graph", font=('Bold', 22), fg='blue', bd=0, command=bar_graph).pack(pady=20)
    
    

   
    
def hist_page():
    
    hist_frame = tk.Frame(main_frame, bg="#d4e157")
    hist_frame.pack(pady = 20)
    hide_all_frames()
    hide_indicator()
    hist_ind.config(bg='blue')
    hist_frame.pack(fill=tk.BOTH, expand=True)
    
    def hist_graph():
        
        for widget in hist_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
            
        array_his_1 = hisx_entry.get().split(",")
        array_his_1 = list(map(float, array_his_1))
        
        fig, ax = plt.subplots(figsize=(11,9))

        array_his_sorted = sorted(array_his_1)
        plt.hist(array_his_sorted, edgecolor='black',color=hiscol_entry.get())
        plt.xlabel(hisxl_entry.get())
        plt.ylabel(hisyl_entry.pack())
        plt.title(hist_entry.get())
        plt.show()
    
    # Clear existing canvas widgets
        for widget in hist_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=hist_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(hist_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
    

        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")
            
            
            

    
    font_large = ('Arial', 20)
    tk.Label(hist_frame, text="Please Enter the following information to create your histogram", font=font_large).pack(pady=10)
    tk.Label(hist_frame, text="Enter the data separated by a comma", font=font_large).pack(pady=5)
    hisx_entry = Entry(hist_frame, font=font_large, width=30)
    hisx_entry.pack()
    tk.Label(hist_frame, text="Enter a title", font=font_large).pack(pady=5)
    hist_entry = Entry(hist_frame, font=font_large, width=30)
    hist_entry.pack()
    tk.Label(hist_frame, text="Enter an x-axis label", font=font_large).pack(pady=5)
    hisxl_entry = Entry(hist_frame, font=font_large, width=30)
    hisxl_entry.pack()
    tk.Label(hist_frame, text="Enter a y-axis label", font=font_large).pack(pady=5)
    hisyl_entry = Entry(hist_frame, font=font_large, width=30)
    hisyl_entry.pack()
    tk.Label(hist_frame, text="Enter a color for your bars", font=font_large).pack(pady=5)
    hiscol_entry = Entry(hist_frame, font=font_large, width=30)
    hiscol_entry.pack()
    tk.Button(hist_frame, text="Generate Histogram", font=('Bold', 22), fg='blue', bd=0, command=hist_graph).pack(pady=20)
    
    

def line1_page():
    
    line1_frame = tk.Frame(main_frame, bg="#f4e1d2")
    line1_frame.pack(pady = 20)
    hide_all_frames()
    hide_indicator()
    line1_ind.config(bg='blue')
    line1_frame.pack(fill=tk.BOTH, expand=True)
    
    def line1_graph():
        
        for widget in line1_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
        fig, ax = plt.subplots(figsize=(11,9))
            
        array_lines_1 = linex_entry.get().split(",")
        array_lines_2 = liney_entry.get().split(",")
     

        array_lines_11 = list(map(float, array_lines_1))
        array_lines_12 = list(map(float, array_lines_2))

        plt.plot(array_lines_11, array_lines_12, color=lincol_entry.get())
        plt.grid()
        plt.xlabel(linp_entry.get())
        plt.ylabel(lini_entry.get())
        plt.title(linet_entry.get())
        plt.show()
    # Clear existing canvas widgets
        for widget in line1_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=line1_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(line1_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
    

        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")
            
            

    
    font_large = ('Arial', 20)
    tk.Label(line1_frame, text="Please Enter the following information to create your line graph", font=font_large).pack(pady=10)
    tk.Label(line1_frame, text="Enter your x-axis values", font=font_large).pack(pady=5)
    linex_entry = Entry(line1_frame, font=font_large, width=30)
    linex_entry.pack()
    tk.Label(line1_frame, text="Enter your y-axis values (corresponding to x-axis values)", font=font_large).pack(pady=5)
    liney_entry = Entry(line1_frame, font=font_large, width=30)
    liney_entry.pack()
    tk.Label(line1_frame, text="Enter a title", font=font_large).pack(pady=5)
    linet_entry = Entry(line1_frame, font=font_large, width=30)
    linet_entry.pack()
    tk.Label(line1_frame, text="Enter an x-axis label", font=font_large).pack(pady=5)
    linp_entry = Entry(line1_frame, font=font_large, width=30)
    linp_entry.pack()
    tk.Label(line1_frame, text="Enter a y-axis label", font=font_large).pack(pady=5)
    lini_entry = Entry(line1_frame, font=font_large, width=30)
    lini_entry.pack()
    tk.Label(line1_frame, text="Enter a color for your line", font=font_large).pack(pady=5)
    lincol_entry = Entry(line1_frame, font=font_large, width=30)
    lincol_entry.pack()
    tk.Button(line1_frame, text="Generate Line Graph", font=('Bold', 22), fg='blue', bd=0, command=line1_graph).pack(pady=20)
    
    
    
def line2_page():
    
    line2_frame = tk.Frame(main_frame, bg="#cfe8fc")
    line2_frame.pack(pady = 20)
    hide_all_frames()
    hide_indicator()
    line2_ind.config(bg='blue')
    line2_frame.pack(fill=tk.BOTH, expand=True)
    
    def line2_graph():
        
        for widget in line2_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
        fig, ax = plt.subplots(figsize=(11,9))

        array_lines_1 = line2x_entry.get().split(",")
        array_liness_2 = lin2yb_entry.get().split(",")
        array_lines_2 = line2y_entry.get().split(",")

        array_lines_34 = list(map(float, array_liness_2))


        array_lines_12 = list(map(float, array_lines_2))

        plt.plot(array_lines_1, array_lines_12, color=lin2col_entry.get(), label=lin2lb_entry.get())
        plt.plot(array_lines_1, array_lines_34, color=lin22col_entry.get(), label=lin222col_entry.get())
        plt.grid()
        plt.xlabel(lin2p_entry.get())
        plt.ylabel(lin2i_entry.get())
        plt.title(line2t_entry.get())
        plt.legend()
        plt.show()

        
    # Clear existing canvas widgets
        for widget in line2_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=line2_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(line2_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
    

        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")
            
            

    
    font_large = ('Arial', 20)
    tk.Label(line2_frame, text="Please Enter the following information to create your line graph", font=font_large).pack(pady=10)
    tk.Label(line2_frame, text="Enter your x-axis values", font=font_large).pack(pady=5)
    line2x_entry = Entry(line2_frame, font=font_large, width=30)
    line2x_entry.pack()
    
    tk.Label(line2_frame, text="Enter your y-axis values for the 1st line", font=font_large).pack(pady=5)
    line2y_entry = Entry(line2_frame, font=font_large, width=30)
    line2y_entry.pack()
    
    tk.Label(line2_frame, text="Enter a title", font=font_large).pack(pady=5)
    line2t_entry = Entry(line2_frame, font=font_large, width=30)
    line2t_entry.pack()
    
    tk.Label(line2_frame, text="Enter an x-axis label", font=font_large).pack(pady=5)
    lin2p_entry = Entry(line2_frame, font=font_large, width=30)
    lin2p_entry.pack()
    
    tk.Label(line2_frame, text="Enter a y-axis label", font=font_large).pack(pady=5)
    lin2i_entry = Entry(line2_frame, font=font_large, width=30)
    lin2i_entry.pack()
    
    tk.Label(line2_frame, text="Enter a color for the 1st line", font=font_large).pack(pady=5)
    lin2col_entry = Entry(line2_frame, font=font_large, width=30)
    lin2col_entry.pack()
    
    tk.Label(line2_frame, text="Enter a label for the 1st line", font=font_large).pack(pady=5)
    lin2lb_entry = Entry(line2_frame, font=font_large, width=30)
    lin2lb_entry.pack()
    
    tk.Label(line2_frame, text="Enter the y-values for your 2nd line", font=font_large).pack(pady=5)
    lin2yb_entry = Entry(line2_frame, font=font_large, width=30)
    lin2yb_entry.pack()
    
    tk.Label(line2_frame, text="Enter a color for the 2nd line", font=font_large).pack(pady=5)
    lin22col_entry = Entry(line2_frame, font=font_large, width=30)
    lin22col_entry.pack()
    
    tk.Label(line2_frame, text="Enter a label for the 2nd line", font=font_large).pack(pady=5)
    lin222col_entry = Entry(line2_frame, font=font_large, width=30)
    lin222col_entry.pack()
    
    
    
    tk.Button(line2_frame, text="Generate Line Graph", font=('Bold', 22), fg='blue', bd=0, command=line2_graph).pack(pady=20)
    
    
def csv_page():
    
    csv_frame = tk.Frame(main_frame, bg="#d4e157")
    csv_frame.pack(pady = 20)
    hide_all_frames()
    hide_indicator()
    csv_ind.config(bg='blue')
    csv_frame.pack(fill=tk.BOTH, expand=True)
    
    def csv_piegraph():
        
        for widget in csv_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
        fig, ax = plt.subplots(figsize=(11,9))
            
            
        Letters = []
        Numbers = []
        
        
        
        with open(str(csv_entry.get()), 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                Letters.append(row[0])
                Numbers.append(int(row[1]))
        
        plt.pie(Numbers,labels = Letters,autopct = '%.2f%%')
        plt.title(csv_title.get(), fontsize=18)
        plt.legend(Letters, loc="best")
        plt.show()
        
    
    # Clear existing canvas widgets
        for widget in csv_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=csv_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(csv_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
    

        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")
            
            
    def csv_scatgraph():
        
        for widget in csv_frame.winfo_children(): #This line of code clears any existing widgets before creating new ones
            widget.pack_forget()
            
        fig, ax = plt.subplots(figsize=(11,9))
            
            
        Letters = []
        Numbers = []
        
        with open(str(csv_entry.get()), 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                Letters.append(row[0])
                Numbers.append(int(row[1]))
        
        
        
        
        
        plt.scatter(Letters, Numbers, color = 'g',s = 100) 
        plt.xticks(rotation = 25) 
        plt.xlabel(csv_x.get()) 
        plt.ylabel(csv_y.get()) 
        ax.set_xticklabels(Letters, fontsize=6)
        plt.title(csv_title.get(), fontsize = 20) 
  
        plt.show() 
    
    # Clear existing canvas widgets
        for widget in csv_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=csv_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(csv_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
    

        plt.close(fig)
        
    def download_plot(fig):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            fig.savefig(file_path)
            print(f"Plot saved to {file_path}")
            
            
            
    def csv_bargraph():
      for widget in csv_frame.winfo_children():
          widget.pack_forget()
          
      fig, ax = plt.subplots(figsize=(14,14))
      

      
      Letters =[]
      Numbers = []
      
      with open(str(csv_entry.get()), 'r') as csvfile:
          lines = csv.reader(csvfile, delimiter=',')
          for row in lines:
              Letters.append(row[0])
              Numbers.append(int(row[1]))
              
      plt.bar(Letters, Numbers, color=csv_color.get(), width=0.72)
      plt.xlabel(csv_x.get())
      plt.ylabel(csv_y.get())
      plt.title(csv_title.get())
      plt.xticks(rotation='vertical')
      ax.set_xticklabels(Letters, fontsize=6)

      plt.show()
      
      for widget in csv_frame.winfo_children():
          if isinstance(widget, FigureCanvasTkAgg):
              widget.get_tk_widget().destroy()
  
  # Display plot in tkinter window
      canvas = FigureCanvasTkAgg(fig, master=csv_frame)
      canvas.draw()
      canvas.get_tk_widget().pack()
      
      
      download_btn = tk.Button(csv_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
      download_btn.pack(pady=10)
      
      
    def csv_bargraph2():
        for widget in csv_frame.winfo_children():
            widget.pack_forget()
            
        fig, ax = plt.subplots(figsize=(14,14))
        

        
        Letters =[]
        Numbers = []
        
        with open(str(csv_entry.get()), 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                Letters.append(int(row[0]))
                Numbers.append(int(row[1]))
                
        plt.bar(Letters, Numbers, color=csv_color.get(), width=0.72)
        plt.xlabel(csv_x.get())
        plt.ylabel(csv_y.get())
        plt.title(csv_title.get())
        plt.xticks(rotation='vertical')
        ax.set_xticklabels(Letters, fontsize=6)

        plt.show()
        
        for widget in csv_frame.winfo_children():
            if isinstance(widget, FigureCanvasTkAgg):
                widget.get_tk_widget().destroy()
    
    # Display plot in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=csv_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
        download_btn = tk.Button(csv_frame, text="Download Plot", font=('Arial', 16), command=lambda: download_plot(fig))
        download_btn.pack(pady=10)
       
              
          
       
            
            
#-------------------------------------------------------------------------------------------------------------------------------
        
       
            
            
            

    
    font_large = ('Arial', 20)
    tk.Label(csv_frame, text="Please enter the name of your CSV file below, and select a graph to be generated", font=font_large).pack(pady=10)
    tk.Label(csv_frame, text="Enter the data separated by a comma", font=font_large).pack(pady=5)
    
    tk.Label(csv_frame, text="Enter CSV File Directory", font=font_large).pack(pady=5)
    csv_entry = Entry(csv_frame, font=font_large, width=30)
    csv_entry.pack()
    
    tk.Label(csv_frame, text="Enter the title", font=font_large).pack(pady=5)
    csv_title = Entry(csv_frame, font=font_large, width=30)
    csv_title.pack()
    
    tk.Label(csv_frame, text="Enter the x-axis label", font=font_large).pack(pady=5)
    csv_x = Entry(csv_frame, font=font_large, width=30)
    csv_x.pack()
    
    tk.Label(csv_frame, text="Enter the y-axis label", font=font_large).pack(pady=5)
    csv_y = Entry(csv_frame, font=font_large, width=30)
    csv_y.pack()
    
    tk.Label(csv_frame, text="Enter a color", font=font_large).pack(pady=5)
    csv_color = Entry(csv_frame, font=font_large, width=30)
    csv_color.pack()
    
    
   
    tk.Button(csv_frame, text="Generate Pie Chart", font=('Bold', 22), fg='blue', bd=0, command=csv_piegraph).pack(pady=20)
    tk.Button(csv_frame, text="Generate Scatterplot", font=('Bold', 22), fg='blue', bd=0, command=csv_scatgraph).pack(pady=20)
    tk.Button(csv_frame, text="Generate Bar Graph (Only 1 Numerical Axis)", font=('Bold', 22), fg='blue', bd=0, command=csv_bargraph).pack(pady=20)
    tk.Button(csv_frame, text="Generate Bar Graph (2 Numerical Axes)", font=('Bold', 22), fg='blue', bd=0, command=csv_bargraph2).pack(pady=20)


    
    
    


    
    

    



# Sidebar Buttons with larger font and size
style = ttk.Style()
style.configure('TButton', font=('Arial', 16, 'bold'), foreground='white', background='#4a90e2')
style.map('TButton', background=[('active', '#357ABD')])  # Active color when clicked

# Adjust button placement and size
button_width = 280
button_height = 70
button_padding_y = 15

# Sidebar Buttons with ttk styling
# Home Button
home_btn = ttk.Button(options_frame, text="Homepage", style='TButton', command=lambda: indicator(home_ind, home_page))
home_btn.place(x=10, y=10, width=button_width, height=button_height)
home_ind = tk.Label(options_frame, text='', bg='#2f3e46')
home_ind.place(x=5, y=10, width=10, height=button_height)

# Pie Chart Button
pie_btn = ttk.Button(options_frame, text="Pie Chart", style='TButton', command=lambda: indicator(pie_ind, pie_page))
pie_btn.place(x=10, y=button_height + button_padding_y, width=button_width, height=button_height)
pie_ind = tk.Label(options_frame, text='', bg='#2f3e46')
pie_ind.place(x=5, y=button_height + button_padding_y, width=10, height=button_height)

# Scatterplot Button
scat_btn = ttk.Button(options_frame, text="Scatterplot", style='TButton', command=lambda: indicator(scat_ind, scat_page))
scat_btn.place(x=10, y=2 * (button_height + button_padding_y), width=button_width, height=button_height)
scat_ind = tk.Label(options_frame, text='', bg='#2f3e46')
scat_ind.place(x=5, y=2 * (button_height + button_padding_y), width=10, height=button_height)

# Bar Graph (1 Numerical Axis) Button
bar_btn = ttk.Button(options_frame, text="Bar Graph (1 Num Axis)", style='TButton', command=lambda: indicator(bar_ind, bar_page))
bar_btn.place(x=10, y=3 * (button_height + button_padding_y), width=button_width, height=button_height)
bar_ind = tk.Label(options_frame, text='', bg='#2f3e46')
bar_ind.place(x=5, y=3 * (button_height + button_padding_y), width=10, height=button_height)

# Bar Graph (2 Numerical Axes) Button
bar2_btn = ttk.Button(options_frame, text="Bar Graph (2 Num Axes)", style='TButton', command=lambda: indicator(bar2_ind, bar2_page))
bar2_btn.place(x=10, y=4 * (button_height + button_padding_y), width=button_width, height=button_height)
bar2_ind = tk.Label(options_frame, text='', bg='#2f3e46')
bar2_ind.place(x=5, y=4 * (button_height + button_padding_y), width=10, height=button_height)

# Histogram Button
hist_btn = ttk.Button(options_frame, text="Histogram", style='TButton', command=lambda: indicator(hist_ind, hist_page))
hist_btn.place(x=10, y=5 * (button_height + button_padding_y), width=button_width, height=button_height)
hist_ind = tk.Label(options_frame, text='', bg='#2f3e46')
hist_ind.place(x=5, y=5 * (button_height + button_padding_y), width=10, height=button_height)

# Line Graph (1 Line) Button
line1_btn = ttk.Button(options_frame, text="Line Graph (1 Line)", style='TButton', command=lambda: indicator(line1_ind, line1_page))
line1_btn.place(x=10, y=6 * (button_height + button_padding_y), width=button_width, height=button_height)
line1_ind = tk.Label(options_frame, text='', bg='#2f3e46')
line1_ind.place(x=5, y=6 * (button_height + button_padding_y), width=10, height=button_height)

# Line Graph (2 Lines) Button
line2_btn = ttk.Button(options_frame, text="Line Graph (2 Lines)", style='TButton', command=lambda: indicator(line2_ind, line2_page))
line2_btn.place(x=10, y=7 * (button_height + button_padding_y), width=button_width, height=button_height)
line2_ind = tk.Label(options_frame, text='', bg='#2f3e46')
line2_ind.place(x=5, y=7 * (button_height + button_padding_y), width=10, height=button_height)

# CSV File Analysis Button
csv_btn = ttk.Button(options_frame, text="CSV File Analysis", style='TButton', command=lambda: indicator(csv_ind, csv_page))
csv_btn.place(x=10, y=8 * (button_height + button_padding_y), width=button_width, height=button_height)
csv_ind = tk.Label(options_frame, text='', bg='#2f3e46')
csv_ind.place(x=5, y=8 * (button_height + button_padding_y), width=10, height=button_height)

# Start the GUI loop
root.mainloop()
