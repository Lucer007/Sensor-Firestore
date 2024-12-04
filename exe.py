from Connecting_to_firestore import monitor_parking_slots

if __name__ == "__main__":
    try:
        monitor_parking_slots()
    except Exception as e:
        print(f"Fatal error: {e}")