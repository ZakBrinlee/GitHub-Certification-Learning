# Prepare for the GitHub Actions Certification

## [X] [Microsoft Learning Collection: GitHub Actions](https://learn.microsoft.com/en-us/collections/n5p4a5z7keznp5)
  - ### [X] Automate development tasks by using GitHub Actions
  - ### [X] Build continuous integration (CI) workflows by using GitHub Actions
  - ### [X] Leverage GitHub Actions to publish to GitHub Packages
  - ### [X] Create and publish custom GitHub actions
  - ### [X] Build and deploy applications to Azure by using GitHub Actions
  - ### [X] Manage GitHub Actions in the enterprise
## [X] [Learning GitHub Actions](https://www.linkedin.com/learning/learning-github-actions-2)
## [X] [Advanced GitHub Actions](https://www.linkedin.com/learning/advanced-github-actions)
## [X] [GitHub Actions for CI/CD](https://www.linkedin.com/learning/github-actions-for-ci-cd)

## Links
- [GitHub MarketPlace - Actions](https://github.com/marketplace?type=actions)
- [GitHub Actions Organization](https://github.com/actions)
- [Workflow Syntax for GH Actions](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions)
- [GH Actions limits](https://docs.github.com/actions/reference/usage-limits-billing-and-administration)
- [Awesome Actions list](https://github.com/sdras/awesome-actions)
- [GitHub Actions Toolkit](https://github.com/actions/toolkit)
- [Github Filter pattern cheat sheet - path, branch, and tag filters](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet)

## Top Notes
- Relationship between CI, Continuous Delivery and Continous Deployment
- ![CI, CD & CD relationship](image.png)
- **Continuous integration (CI)** is a practice where developers integrate tested code into a shared branch several times per day.
- **Continuous delivery (CD)** is the next phase of **continuous integration (CI)** where we also make sure to package the code in a release and store it somewhere - preferably, in an artifact repository.
- **Continuous deployment (CD)** takes **continuous delivery (CD)** to the next level by directly deploying our releases to the world.
- **Docker** is an engine that allows you to run containers.
- **Dockerfile** is a text document that contains all the commands and instructions necessary to build a Docker Image.
- **Docker image** is an executable package comprised of code, dependencies, libraries, a runtime, environment variables, and configuration files.
- **Docker container** is a runtime instance of a Docker Image.
- Action Types (3)
  - Container Actions
    - The environment is part of the action's code. These actions can only be run in a Linux environment that GitHub hosts. Container actions support many different languages.
  - JavaScript Actions
    - Don't include the environment in the code. You'll have to specify the environment to execute these actions. You can run these actions in a VM in the cloud or on-premises. JavaScript actions support Linux, macOS, and Windows environments.
  - Composite Run Steps Actions
    - Allows you to combine multiple workflow steps within one action. For example, you can use this feature to bundle together multiple run commands into an action, and then have a workflow that executes the bundled commands as a single step using that action.
- Action Attributes
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