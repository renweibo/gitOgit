![](https://img.shields.io/pypi/v/gitOgit.svg) ![Documentation Status](https://readthedocs.org/projects/gitOgit/badge/?version=latest)

# Introduction 背景介绍

做开发任务久了，非常习惯各种版本管理工具，不论是cvs、git、svn、p4、fossil、hg、Darcs、clearcase，还有一个用了多年，但是回头想想有点痛恨不记得名字的。有一个比较常见的问题，在工作中时不时困扰着我，尤其是多人开发的时候，那就是不能提交到版本库的文件，怎么管理，.gitignore是很实用，对团队也很好，但是这里有些文件我还是想他们也能被版本管理起来，虽然不用提交到项目组的仓库，但是我需要他们在我本地仓库里管理起来。

说几个比较实用的情况，有类似情况的话，欢迎在评论、备注里交流

- 非常习惯某个编辑器，其中有些配置，我想版本控制，但是.gitignore中排除了这些文件
- 非常习惯某个IDE，其中有些配置，我想版本控制，但是.gitignore中排除了这些文件
- 有些非常个性化/环境相关的文件，尤其是安全相关，随项目，但是不适合提交到项目库，举个我自己常用的情况，容器里的ssh key，频繁创建容器时，处理ssh key就是一个麻烦的问题，虽然ssh agent可以部分解决问题，不过解决的不够好
- 有些工具，比如可以做local ci的工具drone，通过这个工具我想在提交之前做些验证的事情，这些需要些配置才可以正常工作，但是它和团队的ci可能有些冲突，不能提交，需要本地管理
- 还有时候，复杂一些的项目，如果是组合类的项目，每个分支差异极大，单个分支开发不需要关注，但是混合在一起有些管理和批处理相关脚本，也需要做版本控制，但是这些文件不适合提交到项目组的库里

其实这个功能通过local history可以解决部分场景，另外做些简单的工具，设置好符号链接也能解决部分场景，总是不够好。

最近有想法要去解决一下这类问题，所以开始开发这个工具，如果你和我遇到同样的问题，欢迎你一起讨论解决方法，并用本工具解决你的问题。

# Usage 用法

本工具还在开发中，基本用法设想如下：

- 第一步，在项目代码里，添加需要本地版本管理的文件和目录，工具会区分不同的项目，分开处理，添加文件或目录均可
- 第二部，需要的时候，在项目代码里，同步一下，针对已经添加过的文件，就可以同步（pull/push）

# Configuration 配置

所有需要做配置管理的文件和目录统一会放到用户的Home目录的.gitOgit下。对于linux系统或macOS系统，基本就是`$HOME/.gitOgit`； On Windows, USERPROFILE will be used if set, otherwise a combination of HOMEPATH and HOMEDRIVE will be used，不再使用HOME变量。


# Reference 参考资料

- [Online Documentation 在线文档](https://gitOgit.readthedocs.io)
- [gitOgit · PyPI](https://pypi.org/project/gitOgit/) 
- [gitogit · Docker Hub](https://hub.docker.com/r/renweibo/gitogit)