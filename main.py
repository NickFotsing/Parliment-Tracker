import customtkinter as ctk
from tkinter import *   
from PIL import Image, ImageTk
import requests
import tempfile


# Fetch all MPs
def fetch_all_mps():
    all_members, page_size, skip = [], 20, 0
    while True:
        response = requests.get(
            f"https://members-api.parliament.uk/api/Members/Search?House=1&IsCurrentMember=true&skip={skip}")
        if response.status_code != 200: break
        members = response.json().get('items', [])
        if not members: break
        all_members.extend([{
            "id": m["value"]["id"],
            "name": m["value"]["nameDisplayAs"],
            "full_title": m["value"]["nameFullTitle"],
            "party": m["value"]["latestParty"]["name"],
            "party_color": f"#{m['value']['latestParty'].get('backgroundColour') or '808080'}",
            # Defaults straight to Grey if colour not found :(
            "gender": m["value"]["gender"],
            "photo_url": f"https://members-api.parliament.uk/api/Members/{m['value']['id']}/Thumbnail"
        } for m in members])
        skip += page_size
    return all_members


# Display MP info
def show_mp_info(mp):
    info_window = Toplevel(bg="#f0f0f0")
    info_window.title(f"{mp['name']} - MP Information")
    info_window.geometry("300x400")

    # Attempt to fetch and display the MP's image
    try:
        response = requests.get(mp["photo_url"])
        response.raise_for_status()

        # Save the image temporarily to disk
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name

        # Load the image from the saved file
        mp_image = Image.open(temp_file_path).resize((100, 100), Image.LANCZOS)
        mp_photo = ImageTk.PhotoImage(mp_image)

        # Display the image and retain a reference to avoid garbage collection
        image_label = Label(info_window, image=mp_photo, bg="#f0f0f0")
        image_label.image = mp_photo
        image_label.pack(pady=(20, 10))
    except Exception as e:
        print(f"Failed to load image for {mp['name']}: {e}")
        Label(info_window, text="No Image Available", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=(20, 10))

    # Display MP info
    Label(info_window, text=f"Name: {mp['name']}", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=(10, 5))
    Label(info_window, text=f"Title: {mp['full_title']}", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
    Label(info_window, text=f"Party: {mp['party']}", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=5)
    Label(info_window, text=f"Gender: {mp['gender']}", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=20)

    # Close
    ctk.CTkButton(info_window, text="Close", command=info_window.destroy).pack(pady=10)


# Main Tkinter App
class ParliamentApp(ctk.CTk):
    def __init__(self, mp_data):
        super().__init__()
        self.title("UK Parliament Seats")
        self.geometry("1200x800")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        ctk.CTkLabel(self, text="UK Parliament Seat Viewer", font=("Helvetica", 24, "bold")).pack(pady=10)

        canvas = Canvas(self, width=800, height=600)
        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar_y = Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar_y.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar_y.set)

        grid_frame = ctk.CTkFrame(canvas)
        canvas.create_window((0, 0), window=grid_frame, anchor="nw")

        circle_size, padding_x, padding_y = 15, 2, 2
        columns = 50
        for i, mp in enumerate(mp_data):
            row, col = divmod(i, columns)
            ctk.CTkButton(
                grid_frame,
                text="",
                width=circle_size, height=circle_size,
                fg_color=mp["party_color"],
                corner_radius=circle_size // 2,
                command=lambda m=mp: show_mp_info(m)
            ).grid(row=row, column=col, padx=padding_x, pady=padding_y)

        grid_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        ctk.CTkButton(self, text="Exit", command=self.quit, fg_color="red").pack(pady=10)


if __name__ == "__main__": # checks if the script is being run directly
    mp_data = fetch_all_mps() # Retrive MP data
    if mp_data:
        app = ParliamentApp(mp_data) #
        app.mainloop()
