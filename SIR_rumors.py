import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider
from scipy.integrate import solve_ivp


class SystemSolver:

    @staticmethod
    def SIR(t, ISR, a, b, c, d, e):
        I, S, R = ISR
        DI = -a * I * S
        DS = b * a * I * S - a * S * (c * S + d * R) - e * S
        DR = (1 - b) * a * I * S + a * S * (c * S + d * R) + e * S
        return [DI, DS, DR]

    def sol_SIR(self, t, a, b, c, d, e):
        N = 10**6
        I0, S0, R0 = (N - 1) / N, 1 / N, 0
        y0 = [I0, S0, R0]
        cons = (a, b, c, d, e)

        t_span = [0, int(t)]
        t_eval = np.linspace(*t_span, int(t) * 10000)
        sol = solve_ivp(self.SIR, t_span, y0, method="RK45", t_eval=t_eval, args=cons)
        t = sol.t
        I = sol.y[0]
        S = sol.y[1]
        R = sol.y[2]

        print(sol)
        print("valor dos slider:", a, b, c, d, e)
        print("S + I + R", I[-1] + S[-1] + R[-1])
        print("S =", S[-1], "I =", I[-1], "R =", R[-1])
        print("tamanho do t_eval", len(t_eval))
        print("tamanho do h", t_eval[-1] - t_eval[-2])
        return t, I, S, R


class SIRPlotter:

    def __init__(self, ax, solver):
        self.ax = ax
        self.solver = solver
        self.init_plot()

    def init_plot(self):
        self.ax.set_xlabel("t")
        self.ax.set_ylabel("S I R")
        self.ax.set_title("Série Temporal do Sistema SIR")

    def plot(self, t, I, S, R):
        self.ax.clear()
        self.init_plot()
        self.ax.plot(t, I, color="red", label="I(t)")
        self.ax.plot(t, S, color="green", label="S(t)")
        self.ax.plot(t, R, color="blue", label="R(t)")
        self.ax.legend()


class SIRSliders:

    def __init__(self, fig, ax, plotter, solver, init_vals):
        self.fig = fig
        self.ax = ax
        self.plotter = plotter
        self.solver = solver

        self.init_t, self.init_a, self.init_b, self.init_c, self.init_d, self.init_e = (
            init_vals
        )

        # Initialize sliders
        (
            self.a_slider,
            self.b_slider,
            self.c_slider,
            self.d_slider,
            self.e_slider,
            self.t_slider,
        ) = self.create_sliders()

        # Set initial plot
        self.update_plot(None)

        # Connect sliders to the update function
        self.a_slider.on_changed(self.update_plot)
        self.b_slider.on_changed(self.update_plot)
        self.c_slider.on_changed(self.update_plot)
        self.d_slider.on_changed(self.update_plot)
        self.e_slider.on_changed(self.update_plot)
        self.t_slider.on_changed(self.update_plot)

    def create_sliders(self):

        ax_a = self.fig.add_axes([0.15, 0.27, 0.75, 0.03])
        ax_b = self.fig.add_axes([0.15, 0.22, 0.75, 0.03])
        ax_c = self.fig.add_axes([0.15, 0.17, 0.75, 0.03])
        ax_d = self.fig.add_axes([0.15, 0.12, 0.75, 0.03])
        ax_e = self.fig.add_axes([0.15, 0.07, 0.75, 0.03])
        ax_t = self.fig.add_axes([0.15, 0.02, 0.75, 0.03])

        a_slider = Slider(
            ax=ax_a, label=r"$\bar{k}$", valmin=0, valmax=30, valinit=self.init_a
        )
        b_slider = Slider(
            ax=ax_b, label=r"$\lambda$", valmin=0, valmax=1, valinit=self.init_b
        )
        c_slider = Slider(
            ax=ax_c, label=r"$\gamma$", valmin=0, valmax=1, valinit=self.init_c
        )
        d_slider = Slider(
            ax=ax_d, label=r"$\eta$", valmin=0, valmax=1, valinit=self.init_d
        )
        e_slider = Slider(
            ax=ax_e, label=r"$\delta$", valmin=0, valmax=1, valinit=self.init_e
        )
        t_slider = Slider(ax=ax_t, label="t", valmin=0, valmax=10, valinit=self.init_t)

        return a_slider, b_slider, c_slider, d_slider, e_slider, t_slider

    def update_plot(self, val):
        t = self.t_slider.val
        a = self.a_slider.val
        b = self.b_slider.val
        c = self.c_slider.val
        d = self.d_slider.val
        e = self.e_slider.val

        t_vals, I, S, R = self.solver.sol_SIR(t, a, b, c, d, e)
        self.plotter.plot(t_vals, I, S, R)


class SIRApp:

    def __init__(self):
        self.solver = SystemSolver()

        # Create the figure and axes for plotting
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        plt.subplots_adjust(bottom=0.37)

        # Initialize the plotter
        self.plotter = SIRPlotter(self.ax, self.solver)

        # Initial values for parameters a, b, c, d, e, and t
        init_t, init_a, init_b, init_c, init_d, init_e = 10, 10, 0.5, 0.1, 0.2, 0.2

        # Add sliders to control parameters
        self.sliders = SIRSliders(
            self.fig,
            self.ax,
            self.plotter,
            self.solver,
            (init_t, init_a, init_b, init_c, init_d, init_e),
        )

        # Add reset button
        self.add_reset_button()

    def add_reset_button(self):

        resetax = self.fig.add_axes([0.01, 0.15, 0.1, 0.04])
        global button
        button = Button(resetax, "Reset", hovercolor="0.975")

        def reset(event):
            self.sliders.a_slider.reset()
            self.sliders.b_slider.reset()
            self.sliders.c_slider.reset()
            self.sliders.t_slider.reset()

        button.on_clicked(reset)

    def run(self):
        plt.show()


if __name__ == "__main__":

    app = SIRApp()
    app.run()
