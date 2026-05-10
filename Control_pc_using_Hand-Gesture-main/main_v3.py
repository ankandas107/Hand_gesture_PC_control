import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gesture_v3.core.system import SystemController

if __name__ == "__main__":
    app = SystemController()
    app.run()
