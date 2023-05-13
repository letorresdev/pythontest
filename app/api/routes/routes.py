from dataclasses import dataclass
from typing import List
from fastapi import APIRouter
import boto3
import uuid
import requests
import json

from pydantic import BaseModel

class Match(BaseModel):
    date: str
    home_team: str
    away_team: str
    status: str
    score: str

router = APIRouter()

class Matches(BaseModel):
    matches: List[Match]


client = boto3.client('dynamodb')
tableName = "u-project-items-table"

@router.get('/')
async def root():
    return {'nessage' : "MONDAY HAPPY CODDING"}

@router.get('/new')
async def root():
     
    response = {
      'statusCode': 200,
      'body': "THANKS FOR YOUR TIME",
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
    }
    print('response', response)
    return response

@router.get('/get-items')
async def root():

  response_ = client.scan(TableName=tableName)
  items = response_['Items']
  
  response = {
        'data': response_,
        'items': items
    }
    
  return response


@router.get('/footbal')
async def root():
    # Logic to get the
    value = get_team_scores(2002)
    return {'respons' : Matches(matches = value)}



# Define a function to get the scores of a team
def get_team_scores(team_id):
    # Define the URL of the external API
    API_URL = "https://api.football-data.org/v4/"

# Define your API key for authentication
    API_KEY = "1dedb546ed1c4bd4ada5e66f19b814a8"
    # Define the API endpoint for retrieving a team's matches
    endpoint = f"competitions/{team_id}/matches"

    # Define the headers for the API request, including the API key
    headers = {
        "X-Auth-Token": API_KEY
    }

    # Make the API request
    response = requests.get(f"{API_URL}{endpoint}", headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        # print('data', data)
        # Extract the scores from the matches
        scores = []
        for match in data["matches"]:
            if match["status"] == "FINISHED":
                
                date = match["utcDate"]
                home_team = match["homeTeam"]["name"]
                away_team = match["awayTeam"]["name"]
                home_score = match["score"]["fullTime"]["home"]
                away_score = match["score"]["fullTime"]["away"]

                match_info = Match(
                date=match["utcDate"],
                home_team=home_team,
                away_team=away_team,
                status=match["status"],
                score=f"{home_score} - {away_score}"
              )
                scores.append(match_info)
            
            
        return scores
    else:
        # If the request was unsuccessful, raise an exception
        raise Exception(f"API request failed with status code {response.status_code}")


# Post
#  Save Name of User , Email , Footbal or Tenis

# When he register he have access to this options

