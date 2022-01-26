from matplotlib import pyplot as plt
import yaml
from pathlib import Path
from matplotlib.ticker import ScalarFormatter
import gc
SRC_DIR = Path(__file__).parent.resolve()
PLT_CONFIG_PATH = SRC_DIR / "plt.cfg.yml"
with open(PLT_CONFIG_PATH, "r") as yml:
    cfg = yaml.safe_load(yml)
plt.rcParams.update(cfg)
plt.ioff()


class Subplot():
    def __init__(self, xlabel=None, ylabel=None, title=None, show_results=True):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.show_results = show_results
        fig, ax = self.subplot(self.xlabel, self.ylabel, self.title)
        self.ax = ax
        self.fig = fig

    def __call__(self,):
        return self.subplot(self.xlabel, self.ylabel, self.title)

    def __enter__(self, ):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.show_results:
            plt.show()
        plt.clf()
        plt.close(self.fig)
        gc.collect()
        return True

    def subplot(self, xlabel=None, ylabel=None, title=None):
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
        return fig, ax


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
    return fig, ax
