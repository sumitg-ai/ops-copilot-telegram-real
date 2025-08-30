from app.nlp.promise_detector import detect_promises

def test_detect():
    res = detect_promises("I'll finish this by Friday", author="alice")
    assert res and res[0]["owner"] == "alice"
