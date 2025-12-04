# ChronoWish 🎂🕰️  
A lightweight Tkinter-based birthday manager with SQLite storage.

ChronoWish helps you store birthdays, find birthdays by date, and locate the nearest upcoming birthday.  
It is designed to be simple, modular, and easy to extend — perfect for learning, experimenting, and building clean GUI architecture.

<p align="center">
  <img src="https://img.shields.io/badge/status-active--development-blue" alt="Status Badge">
</p>

---

## ✨ Features

- ✅ Add / Upload birthdays  
- ✅ Find birthday by exact date  
- ✅ Find the nearest upcoming birthday  
- ✅ Clean Tkinter UI with modular components  
- ✅ SQLite database for persistent storage  
- ✅ Reusable input field components (EntryField class)  
- ✅ Real-time date & time display  

---

## 📁 Project Structure

```
chronowish/
├── main.py                # Main Tkinter window
├── ui/
│   ├── input_section.py   # Name + UID fields (EntryField, InputSection)
│   ├── radio_section.py   # Search mode radio buttons
│   └── time_section.py    # Live date/time display
├── db/
│   ├── database.py        # SQLite connection + queries
│   └── birthdays.db       # Auto-created database
└── README.md
```

---

## 🚀 Getting Started

### 1. Install Python dependencies
ChronoWish uses only the standard library:
- `tkinter`
- `sqlite3`


### 2. Run the app
```bash
python main.py
```

The database (`birthdays.db`) will be created automatically on first run.

---

## 🗄️ Database Schema

```
birthdays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    uid TEXT UNIQUE,
    dob TEXT NOT NULL   -- stored as DD-MM-YYYY
)
```

---


## 🧙‍♂️ Philosophy

ChronoWish is intentionally small.  
It focuses on:
- clarity  
- modularity  
- readable code  
- beginner-friendly architecture  

Perfect for learning Tkinter + SQLite while keeping the codebase clean and expandable.

---

## 🌱 Future Ideas (Optional)
- Birthday notifications
- Export/import data
- Sorting & filtering UI
- Small analytics (upcoming birthdays count)



---
## 📜 License

MIT — free to use, modify, and learn from.

---

<br />
<br />

<h2 align="center">Made With ♥ By TheCodedHuman</h2>

