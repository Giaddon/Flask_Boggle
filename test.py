from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    "Tests for our flask app"
    def test_boggle_board(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<table class="boggle-board">', html)
    
    def test_boggle_check_correct(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ['W', 'M', 'D', 'L', 'R'], 
                    ['I', 'X', 'I', 'V', 'H'], 
                    ['N', 'R', 'A', 'G', 'I'], 
                    ['B', 'K', 'R', 'O', 'E'], 
                    ['G', 'P', 'N', 'S', 'V']
                    ] 

            resp = client.post('/check/',
                        json={'guess': 'win'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Cool! Good job Guy", html)
    
    def test_boggle_check_invalid(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ['W', 'M', 'D', 'L', 'R'], 
                    ['I', 'X', 'I', 'V', 'H'], 
                    ['N', 'R', 'A', 'G', 'I'], 
                    ['B', 'K', 'R', 'O', 'E'], 
                    ['G', 'P', 'N', 'S', 'V']
                    ] 

            resp = client.post('/check/',
                        json={'guess': 'tttt'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("This isn't a word", html)
        
    def test_boggle_check_not_there(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['board'] = [
                    ['W', 'M', 'D', 'L', 'R'], 
                    ['I', 'X', 'I', 'V', 'H'], 
                    ['N', 'R', 'A', 'G', 'I'], 
                    ['B', 'K', 'R', 'O', 'E'], 
                    ['G', 'P', 'N', 'S', 'V']
                    ] 

            resp = client.post('/check/',
                        json={'guess': 'triumphant'})
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Word isn't on the board!", html)


