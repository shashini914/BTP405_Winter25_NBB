import matplotlib.pyplot as plt

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
rainfall = [75, 60, 100, 125, 175, 200, 225, 210, 180, 140, 90, 80]

plt.figure(figsize=(10, 6))
plt.bar(months, rainfall, color="skyblue", edgecolor="black")

plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall Distribution", fontsize=14)
plt.xticks(rotation=45)  
plt.tight_layout()

plt.show()