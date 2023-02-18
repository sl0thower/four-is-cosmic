from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
from names import number2name, number2namecount

n_range = [0, 16]

# generate dictionary of four-is-cosmic sequences for n_range
sequence_dict = {}
for n_original in range(n_range[0], n_range[1] + 1):
    n = n_original
    sequence = [n]
    while n != 4:
        n = number2namecount(n)
        sequence.append(n)
    sequence_dict[n_original] = sequence

# plot results
fg = Figure()
ax = fg.gca()
for key, item in sequence_dict.items():
    ax.plot(item, range(len(item)), 'o-')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.grid()
ax.set_xlabel("initial value")
ax.set_ylabel("step in sequence")
ax.set_title("Four is Cosmic")
fg.savefig("four_is_cosmic.png", dpi=300)