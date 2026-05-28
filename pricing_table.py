services = {
    "api_latency": "$150",
    "security_vulnerabilities": "$300",
    "memory_leaks": "$200",
    "database_migration": "$500"
}

with open("client_report.txt", "a") as f:
    f.write("\n\n--- QUOTE FOR SERVICES ---\n")
    for service, price in services.items():
        f.write(f"{service.replace('_', ' ').title()}: {price}\n")
    f.write("\nPayment Link: [INSERT YOUR PAYPAL LINK HERE]\n")
