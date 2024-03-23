import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

app = ttk.Window()
colors = app.style.colors

coldata = [
    {"text": "LicenseNumber", "stretch": False},
    {"text": "Je test", "stretch": False},
    {"text": "UserCount", "stretch": False},
]

rowdata = [
    ('A123', 'IzzyCo', 12),
    ('A136', 'Kimdee Inc.', 45),
    ('A158', 'Farmadding Co.', 36)
]

dt = Tableview(
    master=app,
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, colors.dark),
)
dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

app.mainloop()
