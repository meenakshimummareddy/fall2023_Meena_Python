import matplotlib.pyplot as plt
import numpy as np

# Subheading 1: Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Subheading 2: Create a multi-line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="sin(x)", linestyle='--', color='b')
plt.plot(x, y2, label="cos(x)", linestyle='-', color='r')

# Subheading 3: Customize the plot
plt.title("Sine and Cosine Functions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="upper right")

# Subheading 4: Save and display the plot
plt.grid(True)
plt.savefig("sine_cosine_plot.png")
plt.show()
