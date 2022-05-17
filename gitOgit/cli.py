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


@main.command("sync")
def repo_sync():
    prepare()
    

@main.command("add")
def repo_add(p: Path = typer.Argument(..., metavar="📁DIRETORY or 📃FILE", help="需要管理的文件或目录")):
    """
    上手可用，进入到需要管理的目录，直接添加需要版本管理的文件或者目录即可，这些添加的文件就会放到统一的地方做好版本管理。

    """
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
    

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
