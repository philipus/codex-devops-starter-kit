## Web App Scaffold Prompt

**Prompt:** Create a minimal Flask app that returns 'Hello Codex' on the root route.

**Codex Output:**

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Codex'

if __name__ == '__main__':
    app.run(debug=True)
```
