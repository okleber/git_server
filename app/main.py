from fastapi import FastAPI
import subprocess
import glob

app = FastAPI()

@app.get("/listrepo")
async def listrepo():
    dir_list = glob.glob("/*.git",)
    return {" ": dir_list}

@app.post("/createrepo/{repo_name}")
async def createrepo(repo_name: str):
    try:
        subprocess.check_call(["mkdir", f"/{repo_name}.git"])
        output=subprocess.check_output(["git","init","--bare",f"/{repo_name}.git"])
        return {"output": output}
    except:
        pass

@app.post("/deleterepo/{repo_name}")
async def deleterepo(repo_name: str):
    try:
        subprocess.check_call(["rm", "-rf", f"/{repo_name}.git"])
        return {"output": f"Deleted {repo_name}"}
    except:
        pass
