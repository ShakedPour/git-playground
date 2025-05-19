import requests
import time

def test_visits_counter():
    url = "http://localhost:5000"

    # שליחה של 3 בקשות ל-Flask
    for _ in range(3):
        response = requests.get(url)
        assert response.status_code == 200
        time.sleep(0.5)  # להמתין בין הקריאות כדי לא להתנגש עם Redis

    # הבדיקה: האם ההודעה כוללת את המספר 3?
    final_response = requests.get(url)
    assert "4" in final_response.text  # כי הקריאה הרביעית אמורה להיות 4
