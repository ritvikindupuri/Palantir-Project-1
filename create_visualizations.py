#!/usr/bin/env python3
"""
IoT Sensor Pipeline Visualization and ML Analysis
Creates comprehensive visualizations and performs anomaly detection on sensor data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Sample data based on the pipeline output
# In a real scenario, this would be loaded from the Foundry dataset
sensor_data = {
    'sensor_type': ['ECG', 'BodyTemperature', 'Accelerometer', 'BloodPressure', 'PulseOximeter'],
    'avg_efficiency_ratio': [1459.19, 1334.23, 1399.96, 1351.63, 1441.74]
}

# Create more detailed synthetic data for ML analysis
# This simulates the data before aggregation
np.random.seed(42)
detailed_data = []
for sensor in sensor_data['sensor_type']:
    base_efficiency = sensor_data['avg_efficiency_ratio'][sensor_data['sensor_type'].index(sensor)]
    # Generate samples with some variation
    for i in range(100):
        efficiency = np.random.normal(base_efficiency, base_efficiency * 0.1)
        energy_consumption = np.random.uniform(50, 150)
        data_size = np.random.uniform(100, 500)
        transmission_duration = np.random.uniform(1, 10)
        
        detailed_data.append({
            'sensor_type': sensor,
            'energy_efficiency_ratio': efficiency,
            'energy_consumption': energy_consumption,
            'data_size_bytes': data_size,
            'transmission_duration': transmission_duration,
            'bytes_per_duration': data_size / transmission_duration,
            'performance_score': efficiency * (data_size / transmission_duration) / energy_consumption
        })

df_detailed = pd.DataFrame(detailed_data)
df_aggregated = pd.DataFrame(sensor_data)

print("Creating visualizations...")

# 1. Bar chart of average efficiency by sensor type
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(df_aggregated['sensor_type'], df_aggregated['avg_efficiency_ratio'], 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
ax.set_xlabel('Sensor Type', fontsize=12, fontweight='bold')
ax.set_ylabel('Average Efficiency Ratio', fontsize=12, fontweight='bold')
ax.set_title('IoT Sensor Performance: Average Efficiency Ratio by Sensor Type', 
             fontsize=14, fontweight='bold', pad=20)
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/home/ubuntu/sensor_efficiency_bar_chart.png', dpi=300, bbox_inches='tight')
print("✓ Created: sensor_efficiency_bar_chart.png")
plt.close()

# 2. Box plot showing distribution of efficiency ratios
fig, ax = plt.subplots(figsize=(12, 6))
df_detailed.boxplot(column='energy_efficiency_ratio', by='sensor_type', ax=ax, 
                     patch_artist=True, grid=False)
ax.set_xlabel('Sensor Type', fontsize=12, fontweight='bold')
ax.set_ylabel('Energy Efficiency Ratio', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Energy Efficiency Ratios by Sensor Type', 
             fontsize=14, fontweight='bold', pad=20)
plt.suptitle('')  # Remove the automatic title
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/home/ubuntu/efficiency_distribution_boxplot.png', dpi=300, bbox_inches='tight')
print("✓ Created: efficiency_distribution_boxplot.png")
plt.close()

# 3. Heatmap of correlation between metrics
fig, ax = plt.subplots(figsize=(10, 8))
correlation_cols = ['energy_efficiency_ratio', 'energy_consumption', 'data_size_bytes', 
                    'transmission_duration', 'bytes_per_duration', 'performance_score']
correlation_matrix = df_detailed[correlation_cols].corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Correlation Matrix: IoT Sensor Performance Metrics', 
             fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('/home/ubuntu/correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✓ Created: correlation_heatmap.png")
plt.close()

# 4. ML-Based Anomaly Detection using Isolation Forest
print("\nPerforming ML-based anomaly detection...")
features_for_ml = ['energy_efficiency_ratio', 'energy_consumption', 
                   'bytes_per_duration', 'performance_score']
X = df_detailed[features_for_ml].values

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train Isolation Forest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
df_detailed['anomaly'] = iso_forest.fit_predict(X_scaled)
df_detailed['anomaly_score'] = iso_forest.score_samples(X_scaled)

# Convert predictions: -1 (anomaly) to 1, 1 (normal) to 0
df_detailed['is_anomaly'] = (df_detailed['anomaly'] == -1).astype(int)

anomaly_count = df_detailed['is_anomaly'].sum()
print(f"✓ Detected {anomaly_count} anomalies out of {len(df_detailed)} records ({anomaly_count/len(df_detailed)*100:.1f}%)")

# 5. Scatter plot with anomaly detection
fig, ax = plt.subplots(figsize=(12, 8))
normal = df_detailed[df_detailed['is_anomaly'] == 0]
anomalies = df_detailed[df_detailed['is_anomaly'] == 1]

ax.scatter(normal['energy_efficiency_ratio'], normal['performance_score'], 
           c='#4ECDC4', alpha=0.6, s=50, label='Normal', edgecolors='white', linewidth=0.5)
ax.scatter(anomalies['energy_efficiency_ratio'], anomalies['performance_score'], 
           c='#FF6B6B', alpha=0.8, s=100, label='Anomaly', marker='X', edgecolors='darkred', linewidth=1)

ax.set_xlabel('Energy Efficiency Ratio', fontsize=12, fontweight='bold')
ax.set_ylabel('Performance Score', fontsize=12, fontweight='bold')
ax.set_title('ML-Based Anomaly Detection: Isolation Forest Algorithm', 
             fontsize=14, fontweight='bold', pad=20)
ax.legend(fontsize=11, loc='best')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('/home/ubuntu/anomaly_detection_scatter.png', dpi=300, bbox_inches='tight')
print("✓ Created: anomaly_detection_scatter.png")
plt.close()

# 6. Anomaly score distribution
fig, ax = plt.subplots(figsize=(12, 6))
ax.hist(df_detailed['anomaly_score'], bins=50, color='#45B7D1', alpha=0.7, edgecolor='black')
ax.axvline(df_detailed[df_detailed['is_anomaly'] == 1]['anomaly_score'].max(), 
           color='#FF6B6B', linestyle='--', linewidth=2, label='Anomaly Threshold')
ax.set_xlabel('Anomaly Score', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Anomaly Scores (Isolation Forest)', 
             fontsize=14, fontweight='bold', pad=20)
ax.legend(fontsize=11)
ax.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('/home/ubuntu/anomaly_score_distribution.png', dpi=300, bbox_inches='tight')
print("✓ Created: anomaly_score_distribution.png")
plt.close()

# 7. Performance comparison by sensor type
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('IoT Sensor Performance Metrics Dashboard', fontsize=16, fontweight='bold', y=1.00)

# Subplot 1: Average efficiency by sensor
axes[0, 0].bar(df_aggregated['sensor_type'], df_aggregated['avg_efficiency_ratio'], 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
axes[0, 0].set_title('Average Efficiency Ratio', fontweight='bold')
axes[0, 0].set_ylabel('Efficiency Ratio')
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(axis='y', alpha=0.3)

# Subplot 2: Anomaly count by sensor
anomaly_by_sensor = df_detailed.groupby('sensor_type')['is_anomaly'].sum()
axes[0, 1].bar(anomaly_by_sensor.index, anomaly_by_sensor.values, color='#FF6B6B', alpha=0.7)
axes[0, 1].set_title('Anomaly Count by Sensor Type', fontweight='bold')
axes[0, 1].set_ylabel('Number of Anomalies')
axes[0, 1].tick_params(axis='x', rotation=45)
axes[0, 1].grid(axis='y', alpha=0.3)

# Subplot 3: Performance score distribution
df_detailed.boxplot(column='performance_score', by='sensor_type', ax=axes[1, 0], 
                     patch_artist=True, grid=False)
axes[1, 0].set_title('Performance Score Distribution', fontweight='bold')
axes[1, 0].set_xlabel('Sensor Type')
axes[1, 0].set_ylabel('Performance Score')
axes[1, 0].tick_params(axis='x', rotation=45)

# Subplot 4: Energy consumption vs efficiency
for sensor in df_aggregated['sensor_type']:
    sensor_data_subset = df_detailed[df_detailed['sensor_type'] == sensor]
    axes[1, 1].scatter(sensor_data_subset['energy_consumption'], 
                      sensor_data_subset['energy_efficiency_ratio'], 
                      label=sensor, alpha=0.6, s=30)
axes[1, 1].set_title('Energy Consumption vs Efficiency', fontweight='bold')
axes[1, 1].set_xlabel('Energy Consumption')
axes[1, 1].set_ylabel('Efficiency Ratio')
axes[1, 1].legend(fontsize=8, loc='best')
axes[1, 1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('/home/ubuntu/performance_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Created: performance_dashboard.png")
plt.close()

# Save the detailed data with anomaly detection results
df_detailed.to_csv('/home/ubuntu/sensor_data_with_anomalies.csv', index=False)
print("✓ Saved: sensor_data_with_anomalies.csv")

# Generate summary statistics
print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)
print(f"\nTotal Records: {len(df_detailed)}")
print(f"Total Anomalies Detected: {anomaly_count} ({anomaly_count/len(df_detailed)*100:.1f}%)")
print("\nAnomalies by Sensor Type:")
print(df_detailed.groupby('sensor_type')['is_anomaly'].agg(['sum', 'count', lambda x: f"{(x.sum()/len(x)*100):.1f}%"]))
print("\nAverage Metrics by Sensor Type:")
print(df_detailed.groupby('sensor_type')[['energy_efficiency_ratio', 'performance_score']].mean())

print("\n" + "="*60)
print("All visualizations created successfully!")
print("="*60)
