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
- Linting
  - enforce code quality
  - improve code quality
  - catch errors early in the design cycle
- Unit tests
  - First tests that run
  - Fast running
  - Checks code at the component level
- Build step
  - Compile code into binary package
  - Machine-readable format
  - Can be run on different platforms
- Testing
  - Automated testing improves deployment speed
  - checks for errors continuously
  - reduces manual testing
### Building Custom Actions
- Custom Action Checklist
  - Objective
    - What problem does the action solve?
    - Can it be paramaterized?
  - Repository
    - New public repo
    - Helps with managing and versioning code
  - Dockerfile
    - Defines container for the actions
    - install libraries
    - calls the script
  - Script
    - Defines commands that are run by the action
    - interacts with env variables
    - almost any scripting language can be used
    - Use a default shell when possible
  - Action.yml and README.md
    - Action.yml
      - metadata file named action.yml
      - defines inputs, outputs, and entry point
    - README.md file
      - describes the action
      - provides examples
      - explains how to use the action
- 