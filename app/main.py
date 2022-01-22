from fastapi import FastAPI
import subprocess
import glob

app = FastAPI()

@app.get("/repolist")
async def root():
    dir_list = glob.glob("/*.git",)
    return {" ": dir_list}

@app.post("/createrepo/{repo_name}")
async def createrepo(repo_name: str):
    subprocess.check_call(["mkdir", f"/{repo_name}.git"])
    output=subprocess.check_output(["git","init","--bare",f"/{repo_name}.git"])
    return {"output": output}

@app.post("/deleterepo/{repo_name}")
async def deleterepo(repo_name: str):
    output=subprocess.check_output(["rm", "-rf", f"/{repo_name}.git"])
    return {"output": output}
