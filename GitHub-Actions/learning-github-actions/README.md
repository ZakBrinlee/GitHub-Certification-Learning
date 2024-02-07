# [Learning GitHub Actions](https://www.linkedin.com/learning/learning-github-actions-2)

## LinkedIn Learning path course work

## What will be covered
- 

## Links
- [Github Filter pattern cheat sheet - path, branch, and tag filters](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet)
- []()

## Intro
- Requires use/knowledge of YAML files


### First Action
- Attributes
  - `name`: Name of the action/workflow, often the same name as the file
  - `on`: Event that triggers the action
  - `jobs`: The work that the action will perform
  - `runs-on`: The environment the action will run in
    - Usually the os the action will run on
  - `steps`: The individual tasks that the action will perform
    - `uses`: The action that will be used
    - `with`: The input parameters for the action
    - `run`: The shell command that will be run
    - `name`: The name of the step
### Connecting Actions with Workflows
- Workflows define the event that triggers actions
- Multiple workflows per repo is permitted
### Using Actions
- GitHub web editor has built in syntax linter for yml files
- Pass arguments to an action with the identifier `with:`
- Environment Variables
  - read at runtime
  - Default env-variables start with `GITHUB_` prefix
- Secrets
  - Encrypted environment variables
  - Stored in the repo settings
  - Accessed with the `${{ secrets.SECRET_NAME }}` context
  - Unabled to be viewed or edited after creation
### Developing a CI/CD Workflow
-
### Building Custom Actions
-