import customtkinter as ctk


class CalTrackrUI(ctk.CTk):
    def __init__(self, model, color_strategy):
        super().__init__()

        self.model = model
        self.strategy = color_strategy

        # Window Configuration
        self.title("CalTrackr")
        self.geometry("400x700")
        self.configure(fg_color="#F0F2F5")

        self.setup_ui()
        self.refresh_ui()

    def setup_ui(self):
        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color="white", height=50)
        self.header_frame.pack(fill="x", padx=0, pady=0)
        self.header_frame.pack_propagate(False)

        self.title_label = ctk.CTkLabel(self.header_frame, text="CalTrackr", font=("Roboto Medium", 20))
        self.title_label.pack(side="left", padx=20, pady=10)

        self.close_btn = ctk.CTkButton(self.header_frame, text="✕", width=30, height=30,
                                       fg_color="transparent", text_color="#757575",
                                       hover_color="#F0F0F0", font=("Arial", 18),
                                       command=self.close_app)
        self.close_btn.pack(side="right", padx=20)

        # --- Stats Section ---
        self.stats_frame = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.stats_frame.pack(fill="x", padx=0, pady=0)

        self.limit_container = ctk.CTkFrame(self.stats_frame, fg_color="transparent")
        self.limit_container.pack(fill="x", padx=20, pady=(20, 10))

        ctk.CTkLabel(self.limit_container, text="Daily Limit:", font=("Roboto", 12)).pack(side="left")
        self.limit_entry = ctk.CTkEntry(self.limit_container, width=80, justify="right", font=("Roboto", 12))
        self.limit_entry.insert(0, str(self.model.limit))
        self.limit_entry.pack(side="right")
        self.limit_entry.bind("<Return>", self.handle_limit_change)
        self.limit_entry.bind("<FocusOut>", self.handle_limit_change)

        # Calories Display
        self.cal_display_frame = ctk.CTkFrame(self.stats_frame, fg_color="transparent")
        self.cal_display_frame.pack(fill="x", padx=20, pady=5)

        self.consumed_label = ctk.CTkLabel(self.cal_display_frame, text="0", font=("Roboto Black", 36),
                                           text_color="#333")
        self.consumed_label.pack(side="left", anchor="w")
        ctk.CTkLabel(self.cal_display_frame, text="Consumed", font=("Roboto", 12), text_color="#757575").pack(
            side="left", anchor="w", padx=(5, 0))

        self.remaining_label = ctk.CTkLabel(self.cal_display_frame, text="2000", font=("Roboto Medium", 20),
                                            text_color="#757575")
        self.remaining_label.pack(side="right")
        ctk.CTkLabel(self.cal_display_frame, text="Remaining", font=("Roboto", 10), text_color="#757575").pack(
            side="right", padx=(0, 5))

        self.progress_bar = ctk.CTkProgressBar(self.stats_frame, width=350, height=10, corner_radius=5)
        self.progress_bar.set(0)
        self.progress_bar.pack(padx=20, pady=(10, 20))

        # --- Input Section ---
        self.input_frame = ctk.CTkFrame(self, fg_color="white")
        self.input_frame.pack(fill="x", padx=0, pady=0)

        self.food_name_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Food Name")
        self.food_name_entry.pack(padx=20, pady=(20, 10), fill="x")

        self.cal_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Calories (optional)")
        self.cal_entry.pack(padx=20, pady=(0, 10), fill="x")

        self.add_btn = ctk.CTkButton(self.input_frame, text="Add Food", fg_color="#4CAF50", hover_color="#43A047",
                                     font=("Roboto Medium", 14), height=40, command=self.add_food)
        self.add_btn.pack(padx=20, pady=(0, 20), fill="x")

        # --- List Section ---
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="white", label_text="")
        self.scroll_frame.pack(fill="both", expand=True, padx=0, pady=0)

        # --- Footer ---
        self.footer_frame = ctk.CTkFrame(self, fg_color="white", height=60)
        self.footer_frame.pack(fill="x", side="bottom")
        self.footer_frame.pack_propagate(False)

        self.reset_btn = ctk.CTkButton(self.footer_frame, text="Reset", fg_color="#E0E0E0", text_color="#333",
                                       hover_color="#D6D6D6", height=40, command=self.reset_app)
        self.reset_btn.pack(padx=20, pady=10, fill="x")

    def refresh_ui(self):
        # 1. Update Stats Text
        consumed = self.model.get_total_consumed()
        remaining = self.model.get_remaining()

        self.consumed_label.configure(text=f"{consumed}")

        if remaining < 0:
            self.remaining_label.configure(text=f"{remaining}", text_color="#D32F2F")
        else:
            self.remaining_label.configure(text=f"{remaining}", text_color="#757575")

        # 2. Update Progress Bar & Colors using Strategy
        progress_percent = consumed / self.model.limit if self.model.limit > 0 else 0
        self.progress_bar.set(min(progress_percent, 1.0))

        progress_color = self.strategy.get_progress_color(consumed, self.model.limit)
        text_color = self.strategy.get_text_color(consumed, self.model.limit)

        self.progress_bar.configure(progress_color=progress_color)
        self.consumed_label.configure(text_color=text_color)

        # 3. Render List
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        for item in self.model.items:
            row = ctk.CTkFrame(self.scroll_frame, fg_color="white")
            row.pack(fill="x", pady=0, padx=0)

            separator = ctk.CTkFrame(row, height=1, fg_color="#EEEEEE")
            separator.pack(fill="x", side="bottom")

            details_frame = ctk.CTkFrame(row, fg_color="transparent")
            details_frame.pack(side="left", padx=20, pady=15)

            ctk.CTkLabel(details_frame, text=item.name, font=("Roboto Medium", 14), anchor="w").pack(fill="x")
            ctk.CTkLabel(details_frame, text=f"{item.calories} kcal", font=("Roboto", 12), text_color="#757575",
                         anchor="w").pack(fill="x")

            del_btn = ctk.CTkButton(row, text="✕", width=35, height=35, fg_color="transparent",
                                    text_color="#F44336", font=("Arial", 14),
                                    hover_color="#FFEBEE", command=lambda i=item: self.delete_food(i))
            del_btn.pack(side="right", padx=20)

    def add_food(self):
        name = self.food_name_entry.get().strip()
        cal_str = self.cal_entry.get().strip()

        if not name:
            return

        cal = int(cal_str) if cal_str else 0
        self.model.add_item(name, cal)

        self.food_name_entry.delete(0, 'end')
        self.cal_entry.delete(0, 'end')
        self.refresh_ui()

    def delete_food(self, item):
        self.model.remove_item(item)
        self.refresh_ui()

    def handle_limit_change(self, event=None):
        try:
            val = int(self.limit_entry.get())
            if val >= 0:
                self.model.set_limit(val)
                self.refresh_ui()
        except ValueError:
            pass

    def reset_app(self):
        self.model.reset()
        self.refresh_ui()

    def close_app(self):
        self.destroy()