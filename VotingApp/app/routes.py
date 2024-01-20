from app import app

@app.route('/')
def index():
  return "Welcome to the Manitoba Youth Graceful Crescendo Fest"