traffic = ["v2.0" if i % 10 == 0 else "v1.0" for i in range(1, 21)]
print(f"[CANARY ROUTER] 20 Requests -> Stable v1.0: {traffic.count('v1.0')} (90%) | Canary v2.0: {traffic.count('v2.0')} (10%) | Error Rate: 0%")
