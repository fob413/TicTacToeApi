<h1 align="center">
  TIC TAC TOE
</h1>

Tic-tac-toe (also known as noughts and crosses or Xs and Os) is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. <br>
This API plays the game against the API server.

# Hosted Link
<a href="https://oluwafunso-tic-tac-toe-e4ede6842e36.herokuapp.com/" target="_blank">https://oluwafunso-tic-tac-toe-e4ede6842e36.herokuapp.com/</a>

## How To Play
### Query String
Send a get request with a query string of `board`, which contains a valid game board.

| Field | Type | Description |
| --- | --- | --- |
| board | string | A valid game board e.g `?board=ooxxxoox+`|

### Success 200

| Field | Type | Description |
| --- | --- | --- |
| message | string | Information on the next play e.g `Draw!!!` |
| board | string | A valid game board  e.g `ooxxxooxo`|

### Fail 400
| Field | Type | Description |
| --- | --- | --- |
| message | string | Error message e.g `Invalid board` |
| board | string | The current state of the game board  e.g `xxxxxxxxx`|

## Technology Stack
- Python
- Flask
- Flask-RESTful

## Installation
- Clone this repo and navigate into the project's directory
```
$ git clone https://github.com/fob413/TicTacToeApi.git && cd TICTACTOEAPI
```

- Create a `python3` virtual environment for the project and activate it
  - To install `python3` follow this [link](https://realpython.com/installing-python/).
  - To install and activate a `virtual environment` follow this [link](https://virtualenv.pypa.io/en/stable/installation/)

- Install the project's requirements
```
$ pip install requiremnts.txt
```

- Run the app
```
$ python manage.py run
```

## Running Tests
- Run this command to run all the tests.
```
$ python manage.py test
```
