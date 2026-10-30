from flask import Flask, render_template_string
from datetime import datetime, timezone, timedelta
import socket

app = Flask(__name__)

IST = timezone(timedelta(hours=5, minutes=30))

HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>My First Docker App</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: "Segoe UI", Arial, sans-serif;
      background: linear-gradient(135deg, #0db7ed, #384d54);
      color: #fff;
    }
    .card {
      background: rgba(255, 255, 255, 0.12);
      backdrop-filter: blur(10px);
      border-radius: 20px;
      padding: 40px 50px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
      max-width: 480px;
    }
    .whale { font-size: 64px; animation: float 3s ease-in-out infinite; }
    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-12px); }
    }
    h1 { margin: 10px 0; }
    p { opacity: 0.9; }
    .info {
      margin-top: 20px;
      background: rgba(0, 0, 0, 0.25);
      border-radius: 12px;
      padding: 14px;
      font-family: monospace;
      text-align: left;
    }
    .badge {
      display: inline-block;
      margin-top: 18px;
      padding: 6px 16px;
      border-radius: 999px;
      background: #2ecc71;
      font-size: 14px;
    }
    .flag {
      display: inline-block;
      transform-origin: 70% 80%;
      animation: wave 1.6s ease-in-out infinite;
    }
    @keyframes wave {
      0%, 100% { transform: rotate(0deg); }
      25%      { transform: rotate(14deg) skewX(-4deg); }
      50%      { transform: rotate(-8deg) skewX(4deg); }
      75%      { transform: rotate(10deg) skewX(-3deg); }
    }
    a.link { color: #fff; display: inline-block; margin-top: 16px; }
  </style>
</head>
<body>
  <div class="card">
    <div class="whale">🐳</div>
    <h1>Namasthe from Docker! 🙏</h1>
    <p>My first containerized application is running. 🎉</p>
    <div class="info">
      Container ID : {{ container_id }}<br>
      Server time  : <span class="flag">🇮🇳</span> {{ time }} IST
    </div>
    <span class="badge">● Running</span><br>
    <a class="link" href="/about">About →</a>
  </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HOME_PAGE,
        container_id=socket.gethostname(),
        time=datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S"),
    )


@app.route("/about")
def about():
    return """
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><title>About</title></head>
    <body>
      <h1>About this app</h1>
      <p>A small Flask app running inside a Docker container.</p>
      <a href="/">← Back home</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)