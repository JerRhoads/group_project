from shiny import App, ui, render_plot, reactive
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Import your data loading and wrangling code from group_project.py
# For demo, we will just create a placeholder DataFrame
# In your real app, import and use your actual data and wrangling logic


# --- Plot Functions ---
def plot_global_emissions():
    fig, ax = plt.subplots(figsize=(8, 5))
    years = np.arange(2000, 2020)
    values = np.random.randint(100, 200, size=20)
    ax.plot(years, values)
    ax.set_title('Global CO2 Emissions Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Emissions')
    return fig

def plot_peru_emissions():
    fig, ax = plt.subplots(figsize=(8, 5))
    years = np.arange(2000, 2020)
    values = np.random.randint(10, 30, size=20)
    ax.plot(years, values, color='blue')
    ax.set_title('Peru CO2 Emissions Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Emissions')
    return fig

def plot_top10_emissions():
    fig, ax = plt.subplots(figsize=(10, 6))
    countries = [f'Country {i}' for i in range(1, 11)]
    years = np.arange(2000, 2020)
    for i, country in enumerate(countries):
        ax.plot(years, np.random.randint(50, 200, size=20), label=country)
    ax.set_title('Top 10 Emissions-producing Countries')
    ax.set_xlabel('Year')
    ax.set_ylabel('Emissions')
    ax.legend(loc='upper left', fontsize=8)
    return fig

def plot_heatmap():
    fig, ax = plt.subplots(figsize=(10, 6))
    data = np.random.rand(10, 20)
    sns.heatmap(data, cmap="viridis", ax=ax)
    ax.set_title('CO2 Emissions Heatmap (Top 10 Countries)')
    ax.set_xlabel('Year')
    ax.set_ylabel('Country')
    return fig

def plot_facet():
    fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
    years = np.arange(2000, 2020)
    for i, indicator in enumerate(['Emissions', 'GDP Growth', 'Energy Use']):
        for _ in range(3):
            axs[i].plot(years, np.random.randint(10, 100, size=20), alpha=0.3)
        axs[i].plot(years, np.random.randint(20, 80, size=20), color='blue', linewidth=2, label='Peru')
        axs[i].set_title(f'{indicator} by Year')
        axs[i].legend()
    plt.tight_layout()
    return fig

def plot_scatter():
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.random.randint(100, 200, size=30)
    y = x + np.random.normal(0, 10, size=30)
    ax.scatter(x, y, alpha=0.6)
    sns.regplot(x=x, y=y, lowess=True, ci=None, scatter=False, ax=ax)
    ax.set_title('Emissions vs. Temperature (Peru)')
    ax.set_xlabel('Emissions')
    ax.set_ylabel('Temperature')
    return fig

app_ui = ui.page_fluid(
    ui.h2("CO2 Emissions Dashboard"),
    ui.navset_tab(
        ui.nav_panel("Global Emissions", ui.output_plot("global_plot")),
        ui.nav_panel("Peru Emissions", ui.output_plot("peru_plot")),
        ui.nav_panel("Top 10 Countries", ui.output_plot("top10_plot")),
        ui.nav_panel("Heatmap", ui.output_plot("heatmap_plot")),
        ui.nav_panel("Faceted Trends", ui.output_plot("facet_plot")),
        ui.nav_panel("Emissions vs. Temperature", ui.output_plot("scatter_plot")),
    ),
    ui.hr(),
    ui.input_action_button("refresh", "Refresh Plots"),
    ui.p("Select a tab to view different graphs. Click 'Refresh Plots' to update.")
)


def server(input, output, session):
    @output()
    @render_plot
    def global_plot():
        return plot_global_emissions()

    @output()
    @render_plot
    def peru_plot():
        return plot_peru_emissions()

    @output()
    @render_plot
    def top10_plot():
        return plot_top10_emissions()

    @output()
    @render_plot
    def heatmap_plot():
        return plot_heatmap()

    @output()
    @render_plot
    def facet_plot():
        return plot_facet()

    @output()
    @render_plot
    def scatter_plot():
        return plot_scatter()

app = App(app_ui, server)
