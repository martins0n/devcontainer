import pathlib
from subprocess import run

import typer

app = typer.Typer()


def docker_build(image_path: pathlib.Path, image_tag: str):
    typer.echo(f"Image path: {image_path.name} Tag: {image_tag}")

    cmd = [
        "docker",
        "build",
        ".",
        "--file",
        str(image_path.resolve()),
        "--tag",
        image_tag,
    ]
    typer.echo(f"{' '.join(cmd)}")

    run(" ".join(cmd), shell=True)


@app.command(name="docker_build")
def _docker_build(image_path: pathlib.Path, image_tag: str):
    docker_build(image_path=image_path, image_tag=image_tag)


if __name__ == "__main__":
    app()
