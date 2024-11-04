import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

class calendrierPrevisionnel:
    
    def plot_project_timeline(phases):
        dates = {phase: (datetime.strptime(start, "%Y-%m-%d"), datetime.strptime(end, "%Y-%m-%d")) 
                for phase, (start, end) in phases.items()}

        fig, ax = plt.subplots(figsize=(10, 6))

        for i, (phase, (start, end)) in enumerate(dates.items()):
            ax.barh(i, (end - start).days, left=start, height=0.5, align='center')
            ax.text(start, i, f"{phase} ({start.strftime('%b %Y')} - {end.strftime('%b %Y')})", 
                    va='center', ha='right', fontsize=10)

        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

        ax.set_yticks(range(len(dates)))
        ax.set_yticklabels([])
        ax.set_xlabel("Timeline")
        ax.set_title("Calendrier Prévisionnel pour le Projet ESUP-Sport")

        plt.grid(axis='x', linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()