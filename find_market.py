import requests
import sys

def find_by_slug(slug):
    url = f"https://gamma-api.polymarket.com/events?slug={slug}"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"Error: {e}")
        return

    if isinstance(data, list):
        # Endpoint might return a list or single object?
        # Usually events endpoint returns a list if filtering?
        # Let's check.
        pass
    
    # If data is a list, take first
    if isinstance(data, list):
        if not data:
            print("No event found.")
            return
        event = data[0]
    else:
        event = data

    print(f"Event: {event.get('title')}")
    markets = event.get("markets", [])
    for m in markets:
        print(f"Market: {m.get('question')}")
        print(f"Condition ID: {m.get('conditionId')}")
        print(f"Asset ID: {m.get('asset_id')}") # asset_id might be relevant?
        print("-" * 20)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_market.py <slug>")
        sys.exit(1)
    find_by_slug(sys.argv[1])
