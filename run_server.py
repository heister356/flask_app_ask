from app import create_app
print("runserver")

from app import models
app = create_app()

print(app)

if __name__ == '__main__':
    # from app import models
    app.run(debug=True, use_reload=False)
    
#