import typer
from db import init_db
from monitor import monitor_pid

app = typer.Typer()

@app.command()
def start(pid: int, interval: int = 1, count: int = 60):
    """
    Inicia el monitoreo de un proceso usando pidstat.
    """
    init_db()
    monitor_pid(pid, interval, count)

if __name__ == "__main__":
    app()
