import asyncio
import click
import scripts.license.generate
import scripts.license.get
import uvicorn

@click.group()
def cli():
    pass

@cli.command()
@click.option('--count', default=1, help="Number of un-registered licenses to get")
def get_licenses(count):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scripts.license.get.get_licenses(count))

@cli.command()
@click.option('--count', default=1, help="Number of licenses to generate")
def generate_licenses(count):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scripts.license.generate.generate_licenses(count))

@cli.command()
def runserver():
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    cli()
