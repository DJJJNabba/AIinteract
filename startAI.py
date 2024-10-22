import subprocess
import os

def activate_virtualenv():
    # Check for the operating system
    if os.name == 'nt':  # Windows
        subprocess.call('AIenv\\Scripts\\activate && python AIconsoleClient.py', shell=True)
    else:  # Linux/Mac
        subprocess.call('source AIenv/bin/activate && python AIconsoleClient.py', shell=True)

if __name__ == "__main__":
    activate_virtualenv()
