"""Console script for ati18n."""
from pathlib import Path
import sys, typer
from git import Repo
from shutil import copytree, copy2


main = typer.Typer(help="Awesome CLI user manager.")


bp = Path('.gitOgit')
repo = Repo(bp)
assert not repo.bare


def prepare():
    if not (bp/".git").exists:
        Repo.init(bp)
        typer.echo("创建git仓库")
    else:
        pass


@main.command()
def repo_sync():
    prepare()
    

@main.command()
def repo_add(p=None):
    prepare()
    if Path(p).exists():
        if str(Path(p)).startswith('/'):
            typer.echo(f"{p} not relative path")
        else :
            first_add = not (bp/p).exists()
            (bp/p).parent.mkdir(parents=True)
            if Path(p).is_dir():
                if first_add:
                    typer.echo(f"添加目录 {p}")
                else:
                    typer.echo(f"更新目录 {p}")
                copytree(Path(p), bp/p, dirs_exist_ok=True)
            if Path(p).is_file():
                if first_add:
                    typer.echo(f"添加文件 {p}")
                else:
                    typer.echo(f"更新文件 {p}")
                copy2(Path(p), bp/p)
            if first_add:
                repo.index.add(p)
            repo.index.commit(f"add {p} into gitOgit")
            # typer.echo(repo.untracked_files)        
    else:
        typer.echo(f"{p} not found")
    

@main.command()
def repo_ci():
    prepare()
    


@main.command()
def command(args=None):
    """Console script for gitOgit."""
    typer.echo("Replace this message by putting your code into "
               "gitOgit.cli.main")
    typer.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
