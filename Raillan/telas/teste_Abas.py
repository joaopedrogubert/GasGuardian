import customtkinter as ctk

app = ctk.CTk()
app.title("Teste")
app.geometry("900x900")


tabview = ctk.CTkTabview(master=app)
tabview.pack(padx=300, pady=100)

tabview.add("BOMBA 01")  # add tab at the end
tabview.add("BOMBA 02")  # add tab at the end
tabview.add("BOMBA 03")  # add tab at the end
tabview.set("BOMBA 02")  # set currently visible tab

button = ctk.CTkButton(master=tabview.tab("BOMBA 02"))
button.pack(padx=20, pady=20)

button2 = ctk.CTkButton(master=tabview.tab("BOMBA 03"))
button2.pack(padx=20, pady=20)


app.mainloop()
