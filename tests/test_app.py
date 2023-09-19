from structure.app import app # Flask instance of the API

class TestAppClass:
    
    def test_health_check_endpoint(self):
        response = app.test_client().get('/health/check')
        assert response.status_code == 200
