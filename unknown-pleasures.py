import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


np.random.seed(1)
fig = plt.figure(figsize=(4, 4), facecolor='white')
ax = fig.add_axes([0,0,1,1], frameon=False)

# Generate random data
data = np.random.uniform(0, 1, (64, 100))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X ** 2)

# Generate line plots
lines = []
for i in range(len(data)):
    # Small reduction of the X extents to get a cheap perspective effect
    xscale = 1 - i / 200.
    # Same for linewidth (thicker strokes on bottom)
    lw = 1. - i / 100.0
    line, = ax.plot(xscale * X, i + G * data[i], color="black", lw=lw)
    lines.append(line)

# Set y limit (to avoid cropping because of thickness)
ax.set_ylim(-2, 65)
ax.set_xticks([])
ax.set_yticks([])

def update(*args):
    # Shift all data to the right
    data[:, 1:] = data[:, :-1]

    # Fill-in new values
    data[:, 0] = np.random.uniform(0, 1, len(data))

    # Update data
    for i in range(len(data)):
        lines[i].set_ydata(i + G * data[i])

    # Return modified artists
    return lines

anim = animation.FuncAnimation(fig, update, frames=100, interval=20)
anim.save('unknown-pleasures.gif', writer='imagemagick', fps=60)
plt.show()
