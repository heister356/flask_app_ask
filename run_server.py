from app import db, create_app
print("runserver")
app=create_app()
print(app)
if __name__ == '__main__':
    app.run(debug=True)
    
