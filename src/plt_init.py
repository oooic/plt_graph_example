from matplotlib import pyplot as plt
import yaml
from pathlib import Path
from matplotlib.ticker import ScalarFormatter
SRC_DIR = Path(__file__).parent.resolve()
PLT_CONFIG_PATH = SRC_DIR / "plt.cfg.yml"
with open(PLT_CONFIG_PATH, "r") as yml:
    cfg = yaml.safe_load(yml)
plt.rcParams.update(cfg)


def subplot(xlabel=None, ylabel=None, title=None):
    fig, ax = plt.subplots()
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.minorticks_on()
    ax.grid(which="major", color="black", alpha=0.4)
    ax.grid(which="minor", color="gray", linestyle=":")
    return fig, ax
