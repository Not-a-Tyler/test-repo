import http.client
import json
def webhook_message():
    conn = http.client.HTTPSConnection('discord.com')
    conn.request('POST', '/api/webhooks/1053916989917233242/NE9RKlrK4Ft_j9ffXAsB3kxN1LRH-xhGrnDmA0b_Q1goh1yzoeCzx9_zn6WNwQiRvVdZ', json.dumps({
        'content': 'Hello, this is a test message!'
    }), {
        'Content-Type': 'application/json',
        'User-Agent': 'Python http.client'
    })
    conn.close()
webhook_message()
