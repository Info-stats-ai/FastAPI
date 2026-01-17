from typing import ValuesView
from fastapi import FastAPI, Path, HTTPException, Query
import uvicorn
import json
app = FastAPI() # object of fat api

def load_data():
    with open("pateints.json", "r") as f:
        data = json.load(f) 
    return data

@app.get("/")
def hello(): # decorator function
    return {"message": "pateint management system"}


@app.get("/about")
def about():
    
    return {"message": "A full stack pateint records"}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/pateint/{pateint_id}')
def view_pateint(pateint_id: str = Path(..., description="The ID of the pateint to view", example="P001")):
    # three dots meaning is reqired
    data = load_data()

    if pateint_id not in data:
        raise HTTPException(status_code=404, detail="Pateint not found")
    else:
        return data[pateint_id]
@app.get('/sort')
def sort(sort_by: str = Query(..., description="sort on the basis of height, weight,  or bmi", example="170cm"),
    order: str = Query('asc',)):

    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field select from {valid_fields}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order")

    data = load_data()
    sort_order = -1 if order == 'desc' else 1
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)