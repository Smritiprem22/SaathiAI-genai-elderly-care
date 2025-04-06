import os

# Define the folder and file structure
structure = {
    "agents": [
        "companion_agent.py",
        "reminder_agent.py",
        "health_monitor_agent.py",
        "safety_agent.py",
        "caregiver_agent.py",
        "language_agent.py"
    ],
    "services": [
        "stt_vosk.py",
        "tts_coqui.py",
        "database.py",
        "alert_system.py"
    ],
    "ui": [
        "dashboard.py"
    ],
    "utils": [
        "helper_functions.py"
    ],
    "": [
        "main.py",
        "requirements.txt",
        "README.md"
    ]
}

# Create folders and files
for folder, files in structure.items():
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    for file in files:
        file_path = os.path.join(folder, file) if folder else file
        with open(file_path, "w") as f:
            f.write("# " + file)  # Add a placeholder comment

print("✅ SaathiAI folder structure created successfully.")
