from fastapi import FastAPI

app=FastAPI()

@app.get("/health",status_code=200)
def health_check():
    return {"Status":"Running"}

app.get("/info",status_code=200)
def information():
    return{"project": "BookmarkVault",
        "version": "1.0.0",
        "author": "Venkata Giridhar"}