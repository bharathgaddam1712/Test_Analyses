import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from config import config

def plot_cumulative_accuracy_over_time(subjects_data, output_base_path):
    colors = {"Maths": "#1f77b4", "Physics": "#ff7f0e", "Chemistry": "#2ca02c"}
    output_paths = {}
    
    for subj in ["Physics", "Chemistry", "Maths"]:  # Fixed order: Physics, Chemistry, Maths
        df = subjects_data[subj]
        plt.figure(figsize=(10, 6))
        if not df.empty:
            plt.plot(df["time"], df["accuracy"], label=subj, marker='o', color=colors[subj])
        else:
            print(f"Info: Skipping plot for '{subj}' as it has no data points")
            plt.plot([], [], label=subj, color=colors[subj])  # Empty plot to maintain legend
        
        plt.title(f'Cumulative Accuracy Over Time for {subj}')
        plt.xlabel('Time Elapsed (seconds, reset for subject)')
        plt.ylabel('Cumulative Accuracy (%)')
        plt.ylim(0, 100)
        plt.legend()
        plt.grid(True)
        save_path = os.path.join(config.OUTPUT_CHARTS_DIR, f"{output_base_path}_{subj.lower()}.png")
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()
        output_paths[subj] = save_path
    
    return list(output_paths.values())

def plot_subject_accuracy(subjects, output_path):
    df = pd.DataFrame(subjects).T
    plt.figure(figsize=(8, 6))
    sns.barplot(x=df.index, y='accuracy', hue=df.index, data=df, palette='Blues', legend=False)
    plt.title('Subject-Wise Accuracy')
    plt.xlabel('Subject')
    plt.ylabel('Accuracy (%)')
    plt.ylim(0, 100)
    save_path = os.path.join(config.OUTPUT_CHARTS_DIR, output_path)
    plt.savefig(save_path)
    plt.close()
    return save_path

def create_chapter_table(chapters):
    table = ["Chapter (Subject) | Attempted | Correct | Accuracy (%) | Avg Time (sec) | Difficulty | Concepts"]
    table.append("-" * 100)
    for chap, stats in chapters.items():
        difficulty_str = ', '.join([f"{k} ({v})" for k, v in stats['difficulty'].items()])
        concepts_str = ', '.join(stats['concepts'])
        table.append(f"{chap} ({stats['subject']}) | {stats['attempted']} | {stats['correct']} | {stats['accuracy']} | {stats['avg_time']} | {difficulty_str} | {concepts_str}")
    return "\n".join(table)