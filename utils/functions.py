import matplotlib.pyplot as plt
import seaborn as sns


def plot_click_distribution(df, selected_employees, baseline_clicks):
    """
    Generates a boxplot showing the click distribution for selected employees.
    """
    # Filter the dataframe for the selected employees
    filtered_df = df[df['name'].isin(selected_employees)].copy()

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 7))

    # Generate the boxplot
    sns.boxplot(
        x='name',
        y='clicks',
        data=filtered_df,
        hue='name',
        palette='viridis',
        legend=False,
        ax=ax
    )

    # Add baseline
    ax.axhline(
        y=baseline_clicks,
        color='r',
        linestyle='--',
        label=f'Baseline ({baseline_clicks} clicks)'
    )

    # Formatting the plot
    ax.set_title('Click Distribution for Selected Employees')
    ax.set_xlabel('Employee Name')
    ax.set_ylabel('Clicks')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.legend()

    fig.tight_layout()

    return fig