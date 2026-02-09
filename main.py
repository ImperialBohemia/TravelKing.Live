#!/home/q/TravelKing.Live/venv/bin/python3
import sys
import os

# Add root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    print("💎 TRAVELKING.LIVE | ENTERPRISE SUPREMACY")
    print("------------------------------------------")
    
    # Forward all commands to the Enterprise Orchestrator
    from core.enterprise.orchestrator import app as orchestrator_app
    
    if len(sys.argv) < 2:
        # Default to status if no command provided
        sys.argv.append("status")
    
    try:
        orchestrator_app()
    except Exception as e:
        print(f"❌ System Error: {e}")

if __name__ == "__main__":
    main()
