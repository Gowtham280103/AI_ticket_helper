import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset/cleaned_dataset/cleaned_issues.csv")

df["issue_created"] = pd.to_datetime(
    df["issue_created"],
    errors="coerce"
)

priority_counts = df["issue_priority"].value_counts()
type_counts = df["issue_type"].value_counts()
monthly_tickets = df.groupby(
    df["issue_created"].dt.month
).size()

plt.figure(figsize=(8, 5))
priority_counts.plot(kind="bar")
plt.title("Tickets by Priority")
plt.xlabel("Priority")
plt.ylabel("Number of Tickets")
plt.tight_layout()
plt.savefig(
    "Visualizations/tickets_by_priority.png",
    dpi=150
)
plt.show()

plt.figure(figsize=(8, 5))
type_counts.plot(kind="bar")
plt.title("Tickets by Issue Type")
plt.xlabel("Issue Type")
plt.ylabel("Number of Tickets")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(
    "Visualizations/tickets_by_issue_type.png",
    dpi=150
)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(
    df["resolution_time_hours"].dropna(),
    bins=30
)
plt.title("Resolution Time Distribution")
plt.xlabel("Resolution Time (Hours)")
plt.ylabel("Number of Tickets")
plt.tight_layout()
plt.savefig(
    "Visualizations/resolution_time_distribution.png",
    dpi=150
)
plt.show()

plt.figure(figsize=(8, 5))
df.boxplot(
    column="resolution_time_hours",
    by="issue_priority",
    grid=False
)
plt.suptitle("")
plt.title("Resolution Time by Priority")
plt.xlabel("Priority")
plt.ylabel("Resolution Time (Hours)")
plt.tight_layout()
plt.savefig(
    "Visualizations/resolution_time_by_priority.png",
    dpi=150
)
plt.show()

plt.figure(figsize=(8, 5))
monthly_tickets.sort_index().plot(
    kind="line",
    marker="o"
)
plt.title("Monthly Ticket Trend")
plt.xlabel("Month")
plt.ylabel("Number of Tickets")
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(
    "Visualizations/monthly_ticket_trend.png",
    dpi=150
)
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(
    df["issue_comments_count"],
    df["resolution_time_hours"],
    alpha=0.3
)
plt.title("Comments vs Resolution Time")
plt.xlabel("Number of Comments")
plt.ylabel("Resolution Time (Hours)")
plt.tight_layout()
plt.savefig(
    "Visualizations/comments_vs_resolution_time.png",
    dpi=150
)
plt.show()
