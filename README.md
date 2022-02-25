# A Cookiecutter Style Python Project Template

## Basic Usage

First use cookiecutter to create a specialized instance of your project from the template repository.

```
$ cookeicutter https://github.com/adam-scislowicz/python-project-template
# <answer questions related to cookiecutter paramaterization>
```

After completing the above steps a directory will have been created with your starter project. The directory
name will be the project name as specified by you in response to questions asked by the cookiecutter CLI tool.

You may then want to instantiate a git repository from your generated project. The following commands can be
used to do so. Wherever you see {{PROJECT_SLUG}} type the project name you specified above.

Note that you may want to modify the below statements to specify a remote and it so then also execute a git push after the commit.

```
cd {{PROJECT_SLUG}}
git init
find . -type f -exec git add {} \;
git commit -m 'Initial project commit. This was generated using cookiecutter and the following template: https://github.com/adam-scislowicz/python-project-template.'
```
