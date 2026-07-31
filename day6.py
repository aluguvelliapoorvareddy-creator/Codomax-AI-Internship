import matplotlib.pyplot as plt

# 1. Prepare Mock Datasets
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
study_hours = [2, 3.5, 5, 4, 6]
test_scores = [65, 72, 88, 80, 95]

# =========================================================================
# PLOT 1: LINE CHART (To show continuous progress of hours over the week)
# =========================================================================
plt.figure(figsize=(7, 4))
plt.plot(days, study_hours, marker='o', color='#1f77b4', linestyle='-', linewidth=2, label='Hours per day')
plt.title('Study Hours Progress Over the Week', fontsize=12, fontweight='bold')
plt.xlabel('Days of the Week', fontsize=10)
plt.ylabel('Hours Studied', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.savefig('line_chart.png', dpi=300)  # Saves file locally
plt.show()

# =========================================================================
# PLOT 2: BAR CHART (To directly compare study volume across categorical values)
# =========================================================================
plt.figure(figsize=(7, 4))
plt.bar(days, study_hours, color='#7ed321', edgecolor='black', width=0.6)
plt.title('Daily Study Hours Breakdown', fontsize=12, fontweight='bold')
plt.xlabel('Days of the Week', fontsize=10)
plt.ylabel('Hours Studied', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('bar_chart.png', dpi=300)   # Saves file locally
plt.show()

# =========================================================================
# PLOT 3: SCATTER PLOT (To visualize correlation between study time and test scores)
# =========================================================================
plt.figure(figsize=(7, 4))
plt.scatter(study_hours, test_scores, color='#d0021b', s=120, edgecolor='black', zorder=3)
plt.title('Correlation: Study Time vs. Test Scores', fontsize=12, fontweight='bold')
plt.xlabel('Hours Studied', fontsize=10)
plt.ylabel('Achieved Test Scores (%)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=300) # Saves file locally
plt.show()