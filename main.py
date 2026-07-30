import matplotlib.pyplot as plt

from analyzer import analyze_logs

print("Security Log Analyzer Started")

failed_attempts, successful_logins, access_denied = analyze_logs(
    "test_logs/sample.log"
)

print("Total Failed Login Attempts:", failed_attempts)
print("Total Successful Logins:", successful_logins)
print("Total Access Denied Events:", access_denied)



if failed_attempts >= 3:
    print("🚨 ALERT: Multiple Failed Login Attempts Detected!")

if access_denied >= 0:
    print("⚠️ ALERT: Unauthorized Access Detected!")

    with open("security_report.txt", "w") as report:
        report.write("===== SECURITY REPORT =====\n")
        report.write(f"Total Failed Login Attempts: {failed_attempts}\n")
        report.write(f"Total Successful Logins: {successful_logins}\n")
        report.write(f"Total Access Denied Events: {access_denied}\n")
        if failed_attempts >= 3:
                    report.write("ALERT: Multiple Failed Login Attempts Detected!\n")

        if access_denied > 0:
                    report.write("ALERT: Unauthorized Access Detected!\n")

        labels = ["Failed", "Successful", "Access Denied"]
        values = [failed_attempts, successful_logins, access_denied]

        
        plt.bar(labels, values, color=["red", "green", "orange"])
        plt.title("Security Log Analyzer Dashboard", fontsize=16, fontweight="bold")
        plt.xlabel("Events")
        plt.ylabel("Count")
        plt.savefig("dashboard.png")

        plt.figure(figsize=(6,6))
        plt.pie(values,
        labels=labels,
        autopct="%1.1f%%",
        colors=["red","green","orange"])
        plt.title("Security Events Distribution")
        plt.savefig("piechart.png")
        plt.show()
        plt.show()              