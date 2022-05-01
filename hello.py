import click

@click.command(help=="This is just a hello app, that does nothing")
@click.option("--name",prompt="I need name", help="Need name")
@click.option("--color",prompt="I need color", help="Need color")

def hello_tool(name, color):
    if name == "Thor":
        click.echo("Thor, your are always red.")
        click.echo(click.style(f"Hello {name}!",fg="red"))
    else:
        #click.echo(click.style(f"Hello {name}!",fg=f"{color}"))
        click.echo(f"Your color is {color}!")
        click.echo(click.style(f"Hello {name}!", fg=color))

if __name__ == "__main__":
    hello()
