import pandas as pd
import typer


app =typer.Typer()


@app.command()
def hello(name: str, iq: int, diaplay_iq: bool = True):
	print(f"Hello {name}!")
	print(f"Your IQ is {iq}")

@app.command()
def goodbye():
	print("Goodbye")

if __name__ == "__main__":
	app()