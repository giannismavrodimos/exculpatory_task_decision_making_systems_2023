import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

# Λίστα με τις ημερομηνίες των εκδόσεων
dates = [
    datetime(2022, 1, 1),
    datetime(2022, 4, 1),
    datetime(2022, 7, 1),
    datetime(2023, 1, 1),
    datetime(2023, 4, 1),
    datetime(2023, 7, 1),
    datetime(2024, 1, 1),
    datetime(2024, 4, 1),
    datetime(2024, 7, 1)
]

# Λίστα με τις εκδόσεις
versions = [
    "Version 1.0",
    "Version 1.1",
    "Version 1.2",
    "Version 2.0",
    "Version 2.1",
    "Version 2.2",
    "Version 3.0",
    "Version 3.1",
    "Version 3.2"
]

# Ορισμός επιπέδων για την απεικόνιση των εκδόσεων
levels = np.arange(1, len(versions) + 1)

# Δημιουργία του σχήματος και απεικόνιση του stem plot
fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
ax.set(title="Music Artist Versions")

markerline, stemline, baseline = ax.stem(dates, levels, linefmt="C3-", basefmt="k-", use_line_collection=True)

plt.setp(markerline, mec="k", mfc="w", zorder=3)

# Μετατροπή της θέσης των markers στη βάση του γραφήματος αντικαθιστώντας τις τιμές τους με μηδέν
markerline.set_ydata(np.zeros(len(dates)))

# Επισήμανση των γραμμών με τις εκδόσεις
vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
for d, l, r, va in zip(dates, levels, versions, vert):
    ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l) * 3), textcoords="offset points", va=va, ha="right")

# Μορφοποίηση του άξονα x με κανόνες εμφάνισης για μήνες
ax.get_xaxis().set_major_locator(mdates.MonthLocator())
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))

# Αφαίρεση του άξονα y και των πλευρικών πλαισίων
ax.get_yaxis().set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.margins(y=0.1)

plt.show()
