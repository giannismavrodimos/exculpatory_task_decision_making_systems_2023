import matplotlib.pyplot as plt

# Δεδομένα για τις κατηγορίες καταστροφών και τις απώλειες
categories = ['Πυρκαγιά', 'Πλημμύρα', 'Σεισμός', 'Καταιγίδα']
losses = [50000, 75000, 30000, 90000]

# Δημιουργία πίνακα δεδομένων
table_data = [['Κατηγορία', 'Απώλεια'],
              [categories[0], losses[0]],
              [categories[1], losses[1]],
              [categories[2], losses[2]],
              [categories[3], losses[3]]]

# Εμφάνιση πίνακα δεδομένων
fig, ax = plt.subplots()
ax.axis('off')
ax.axis('tight')
ax.table(cellText=table_data, loc='center')

# Οπτικοποίηση διαγράμματος
plt.title('Ανάλυση Απωλειών Ασφαλιστικής Εταιρείας')

# Προσθήκη γραφικού διαγράμματος μπάρας
plt.figure()
plt.bar(categories, losses)
plt.title('Απώλειες ανά Κατηγορία Καταστροφής')
plt.xlabel('Κατηγορία')
plt.ylabel('Απώλεια')

plt.show()
