# calendrier_previ.py

"""
Module for plotting a project timeline with different phases using matplotlib.
"""

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class CalendrierPrevisionnel:
    """
    Class to plot the project timeline for different project phases.
    """

    def plot_project_timeline(self, phases):
        """
        Plots a project timeline based on the phases provided.

        Parameters:
            phases (dict): A dictionary where keys are phase names and values are tuples 
                           of start and end dates in the format ('YYYY-MM-DD', 'YYYY-MM-DD').
        """
        # Convert phase dates to datetime objects
        dates = {
            phase: (datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d"))
            for phase, (start, end) in phases.items()
        }

        # Create the figure and axis for plotting
        _, ax = plt.subplots(figsize=(10, 6))

        # Plot each phase as a horizontal bar
        for i, (phase, (start, end)) in enumerate(dates.items()):
            ax.barh(i, (end - start).days, left=start, height=0.5, align='center')
            ax.text(
                start, i, f"{phase} ({start.strftime('%b %Y')} - {end.strftime('%b %Y')})",
                va='center', ha='right', fontsize=10
            )

        # Configure x-axis to show months
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

        # Set y-axis labels and title
        ax.set_yticks(range(len(dates)))
        ax.set_yticklabels([])
        ax.set_xlabel("Timeline")
        ax.set_title("Calendrier Prévisionnel pour le Projet ESUP-Sport")

        # Add gridlines for x-axis
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()
