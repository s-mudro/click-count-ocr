import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

def plot_rolling_average(df, selected_employee, start_date, end_date, baseline, save_path=None):
    # Filter data based on the selected date range
    df_filtered = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))].copy()

    # --- EMPLOYEE 7-DAY ROLLING AVERAGE ---
    emp_df = df_filtered[df_filtered['name'] == selected_employee].copy()
    emp_average_clicks_per_day = emp_df.groupby('date')['clicks'].mean().reset_index()
    emp_average_clicks_per_day['rolling_avg'] = emp_average_clicks_per_day['clicks'].rolling(window=7,
                                                                                             min_periods=1).mean()

    emp_average_clicks_per_day_ra = emp_average_clicks_per_day.copy()
    emp_average_clicks_per_day_ra['clicks'] = emp_average_clicks_per_day_ra['rolling_avg']
    # Dynamic label based on selection
    emp_label = f'{selected_employee} 7-Day Rolling Avg'
    emp_average_clicks_per_day_ra['type'] = emp_label

    # --- COMPANY AVERAGE ---
    overall_average_clicks_per_day = df_filtered.groupby('date')['clicks'].mean().reset_index()
    overall_average_clicks_per_day['rolling_avg'] = overall_average_clicks_per_day['clicks'].rolling(window=7,
                                                                                                     min_periods=1).mean()

    overall_average_clicks_per_day_ra = overall_average_clicks_per_day.copy()
    overall_average_clicks_per_day_ra['clicks'] = overall_average_clicks_per_day_ra['rolling_avg']
    comp_label = 'Company Average 7-Day Rolling Avg'
    overall_average_clicks_per_day_ra['type'] = comp_label

    comparison_daily_df = pd.concat([
        emp_average_clicks_per_day_ra[['date', 'clicks', 'type']],
        overall_average_clicks_per_day_ra[['date', 'clicks', 'type']]
    ])

    # --- PLOTTING ---
    fig, ax = plt.subplots(figsize=(14, 7))
    # Use variables for keys in palette to fix the bug
    sns.lineplot(x='date', y='clicks', hue='type', data=comparison_daily_df,
                 palette={emp_label: 'darkblue', comp_label: 'darkred'},
                 style='type', ax=ax)

    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
    ax.axhline(y=baseline, color='r', linestyle='--', label=f'Baseline ({baseline} Clicks)')

    ax.axvspan(pd.to_datetime('2026-01-01'), pd.to_datetime('2026-02-23'), color='blue', alpha=0.1,
               label='new department launch')
    ax.axvspan(pd.to_datetime('2026-02-28'), pd.to_datetime('2026-03-14'), color='purple', alpha=0.1,
               label='operational pause')

    ax.set_title(f"Performance Analysis: {selected_employee} vs Company Average", fontsize=16, pad=20)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Average Clicks (7-Day Rolling Average)', fontsize=12)
    ax.grid(True, which='major', linestyle='-', alpha=0.6)
    plt.xticks(rotation=0)
    ax.legend(title='Legend', loc='lower left')
    plt.tight_layout()

    # Save the plot locally if save_path is provided
    if save_path:
        # Extract directory from the file path and create it if missing
        dir_name = os.path.dirname(save_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        plt.savefig(save_path)
        plt.close(fig)  # Close fig to prevent duplicate rendering issues

    return fig