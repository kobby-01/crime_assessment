from crimes import app

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert b"U.S. Metro Areas Violent Crime Rates by Type" in response.data
    assert b"Originating Case Identifier" in response.data