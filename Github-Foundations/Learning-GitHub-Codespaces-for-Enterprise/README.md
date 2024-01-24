# [Learning GitHub Codespaces for Enterprise](https://www.linkedin.com/learning/learning-github-codespaces-for-enterprise)
Started: January 23th, 2023
Completed: January 23th, 2023

## LinkedIn Learning path course work

## Notes
- Codespaces is not a free feature.
  - Signup requires
    - Organization account
    - Paid plan (Team or Enterprise)

## Links
- [Intro to devcontainers](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
- []()
- []()

## Required for course
- Basic understanding of code
- Some experience as a developer
- Familiar with foundational git
- Docker Exp (optional)

## Getting started with Codespaces
- Cloud based development environment
- Runs in a VM in the cloud
- Team collaboration features
- Configurable with development environment for teams

### Requirements
- Must be an Organization
- Must be on the Team or Enterprise plan

## Configuring your Codespaces
- Codespaces run in a container
  - Isolated environment containing the resources, software, and sometimes the startup instructions needed for an app to run
  - Ran on a VM
- `devcontainer.json`
  - File for defining container configuration
  - Updates to file will require a rebuild of the container
- Logs are available in the workspace logs
  - Ability to review logs from the codespace
    - Browser session logs
    - Environment logs

## Developing in a Codespace
- Pretty much the same as VSCode
- Create a public url for the running application by changing it from private to public
  - Right click on the port inside the `port` tab
- Push/Pull works the same as VSCode.
  - Staging, commits, etc

## Advanced Concepts
- Large library of predefined containers that are available for use
- CLIs are supported as can be installed as needed
  - Example: `aws` cli
- Environment Variables are supported
  - `echo $ENV_VARIABLE_NAME` to view the variables available in the codespace
- Storing sensitive data is possible with GitHub Secrets
  - Rules
    - Org level secret can be used by any repo in the org
    - Repo level secret is self explanitory
    - Unable to use `GITHUB` prefix
  - Access in Codespaces Secrets in the GitHub settings => codespaces page
  - Codespace will need to be stopped/restarted when a Secret has been created before it can be consumed
