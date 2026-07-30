def analyze_logs(log_file):

    failed_attempts = 0
    successful_logins = 0
    access_denied = 0

    with open(log_file, "r") as file:
        logs = file.readlines()

    for log in logs:

        date = log.split()[0]
        time = log.split()[1]
        print("Date:", date, "Time:", time)

        if "ip=" in log:
            ip = log.split("ip=")[1]
            print("IP Address:", ip)

            if ip == "10.0.0.5":
                print("Suspicious IP Found:", ip)


        if "LOGIN_FAILED" in log:
            failed_attempts += 1

        elif "LOGIN_SUCCESS" in log:
            successful_logins += 1

        elif "ACCESS_DENIED" in log:
            access_denied += 1

    return failed_attempts, successful_logins, access_denied