import sys, subprocess, os

def get_net_changes(file_path):
    # Use 'git diff HEAD' to compare the file against the last committed version
    # This bypasses the need to 'git add' first, avoiding staging mix-ups.
    result = subprocess.run(
        ['git', 'diff', 'HEAD', '--unified=0', file_path],
        capture_output=True, text=True
    )
    
    added = 0
    removed = 0
    
    for line in result.stdout.splitlines():
        # Only count lines that represent actual content changes
        if line.startswith('+') and not line.startswith('+++'):
            if line[1:].strip():
                added += 1
        elif line.startswith('-') and not line.startswith('---'):
            if line[1:].strip():
                removed += 1
                
    return added, removed

# Main logic remains the same
file_path = sys.argv[1]
added, removed = get_net_changes(file_path)

if added > 0 or removed > 0:
    # 1. Stage the file
    subprocess.run(['git', 'add', file_path], capture_output=True)
    
    # 2. Commit the changes
    import datetime
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    
    # Check if this is a config file (in .vscode or .scripts)
    is_config = '.vscode' in file_path or '.scripts' in file_path
    config_marker = " | config altered" if is_config else ""
    msg = f"Time: {timestamp} | Added: {added} | Removed: {removed}{config_marker}"
    subprocess.run(['git', 'commit', '-m', msg], capture_output=True)