import matplotlib.pyplot as plt
import numpy as np

# Approximate run-rate data for RR and SRH, matching the screenshot style
overs = np.arange(1, 21)
rr_run_rate = [0, 14.8, 24.6, 15.2, 13.8, 13.1, 12.9, 13.0, 12.6, 12.4, 12.2, 11.8, 11.6, 11.4, 11.2, 11.0, 10.9, 10.8, 10.7, 10.5]
srh_run_rate = [0, 11.9, 12.4, 13.3, 14.1, 13.9, 13.8, 14.0, 13.7, 13.5, 13.6, 13.4, 13.3, 13.2, 13.2, 13.0, 12.9, 12.8, 12.6, 12.5]

# Wickets markers for RR and SRH
rr_wickets = [3, 5, 11, 12, 15, 19]  # 6 wickets for RR
srh_wickets = [2, 7, 16, 18, 18]  # 5 wickets for SRH, 2 in 18th over

# Smooth the run-rate curves for a Cricbuzz-style appearance
def smooth_curve(x, y, points=220):
    x_smooth = np.linspace(x.min(), x.max(), points)
    y_smooth = np.interp(x_smooth, x, y)
    return x_smooth, y_smooth

overs_smooth, rr_smooth = smooth_curve(overs, rr_run_rate)
_, srh_smooth = smooth_curve(overs, srh_run_rate)

plt.figure(figsize=(10, 6))
ax = plt.gca()
ax.set_facecolor('#f8f8f8')
plt.plot(overs_smooth, rr_smooth, color='#ff4daa', linewidth=3.8, solid_capstyle='round', label='RR', zorder=3)
plt.plot(overs_smooth, srh_smooth, color='#ff9f00', linewidth=3.8, solid_capstyle='round', label='SRH', zorder=3)

# Plot wicket markers as small circles in team colors on the lines
for w in rr_wickets:
    plt.scatter(w, rr_run_rate[w - 1], color='#cc0066', edgecolors='white', linewidth=1.2, s=90, zorder=5)
for w in srh_wickets:
    plt.scatter(w, srh_run_rate[w - 1], color='#cc6600', edgecolors='white', linewidth=1.2, s=90, zorder=5)

# Style the chart to resemble the Cricbuzz run-rate display
plt.xticks(np.arange(1, 21, 1))
plt.yticks(np.arange(0, 26, 5))
plt.xlim(1, 20)
plt.ylim(0, 26)
plt.xlabel('Overs', fontsize=12)
plt.ylabel('Run Rate', fontsize=12)
plt.title('Run Rate vs Overs: RR vs SRH', fontsize=14, fontweight='bold')
ax.grid(True, linestyle='--', linewidth=0.8, alpha=0.45)
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#aaaaaa')
ax.spines['bottom'].set_color('#aaaaaa')
plt.legend(loc='upper right', frameon=False)
plt.tight_layout()
plt.show()