def get_max_success_streak(log_codes: list[int]) -> int:
    # --- PHASE 1 & 2: GUARD CLAUSE ---
    if not log_codes:
        return 0
        
    # --- PHASE 2: INITIALIZATION ---
    max_success_streak = 0
    current_streak = 0
    
    # --- PHASE 2: TRAVERSAL MECHANISM ---
    for code in log_codes:
        if 200 <= code < 400:
            current_streak += 1
            max_success_streak = max(max_success_streak, current_streak)
        else:
            # Trigger: Error found, collapse the streak window
            current_streak = 0
            
    # --- PHASE 3: OUTPUT ---
    return max_success_streak

# Example Mock Test Case:
server_logs = [200, 201, 404, 200, 200, 302, 500, 200]
print(get_max_success_streak(server_logs)) 
# Output will be 3 (for the streak: 200, 200, 302)
