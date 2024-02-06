# [Automate development tasks by using GitHub Actions](https://learn.microsoft.com/en-us/training/modules/github-actions-automate-tasks/)

## Microsoft Learning path course work

## What will be covered
- In this module, you'll be introduced to GitHub Actions and workflows. In subsequent modules, you'll use what you learn here to implement continuous integration, continuous delivery, and infrastructure as code.

## [Course Excercise repo](https://github.com/ZakBrinlee/skills-hello-github-actions)

## Top Notes:
- *GitHub Actions* are packaged scripts to automate tasks in a software-development workflow in GitHub
- *GitHub Actions workflow* is a process that you set up in your repository to automate software-development lifecycle tasks, including GitHub Actions.
- It's important to know that when using conditionals in your workflow, you need to use the specific syntax `${{ <expression> }}`, which tells GitHub to evaluate an expression rather than treat it as a string.
- `on: ` attribute: This is a trigger to specify when this workflow will run
- `schedule: ` event allows you to trigger a workflow to run at specific UTC times using POSIX cron syntax

## Links
- [GitHub MarketPlace - Actions](https://github.com/marketplace?type=actions)
- [GitHub Actions Organization](https://github.com/actions)
- [Workflow Syntax for GH Actions](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions)
- [GH Actions limits](https://docs.github.com/actions/reference/usage-limits-billing-and-administration)
- [Awesome Actions list](https://github.com/sdras/awesome-actions)

## Workflow Automation
- Possible task following code completetion that could be automated:
  - Ensure the code passes all unit tests
  - Perform code quality and compliance checks to make sure the source code meets the organization's standards
  - Check the code and its dependencies for known security issues
  - Build the code integrating new source from (potentially) multiple contributors
  - Ensure the software passes integration tests
  - Version the new build
  - Deliver the new binaries to the appropriate filesystem location
  - Deploy the new binaries to one or more servers
  - If any of these tasks don't pass, report the issue to the proper individual or team for resolution
- Recommendations when using GitHub Actions:
  - Review the action's action.yml file for inputs, outputs, and to make sure the code does what it says it does.
  - Check if the action is in the GitHub Marketplace. This is a good check, even if an action does not have to be on the GitHub Marketplace to be valid.
  - Check if the action is verified in the GitHub Marketplace. This means that GitHub has approved the use of this action. However, you should still review it before using it.
  - Include the version of the action you're using by specifying a Git ref, SHA, or tag.

### Types of GitHub Actions
- 3 types
  - Container Actions
    - The environment is part of the action's code. These actions can only be run in a Linux environment that GitHub hosts. Container actions support many different languages.
  - JavaScript Actions
    - Don't include the environment in the code. You'll have to specify the environment to execute these actions. You can run these actions in a VM in the cloud or on-premises. JavaScript actions support Linux, macOS, and Windows environments.
  - Composite Run Steps Actions
    - Allows you to combine multiple workflow steps within one action. For example, you can use this feature to bundle together multiple run commands into an action, and then have a workflow that executes the bundled commands as a single step using that action.

### GitHub Actions components
- In short, an event triggers the workflow, which contains a job. This job then uses steps to dictate which actions will run within the workflow.
- Event -> Workflow -> Job -> Steps -> Actions
  - Workflows: A workflow is a configurable automated process made up of one or more jobs. You must create a YAML file to define your workflow configuration.
  - Jobs:  A job is a section of the workflow that will be associated with a runner. A runner can be GitHub-hosted or self-hosted, and the job can run on a machine or in a container. You'll specify the runner with the runs-on: attribute.
  - Steps: A step is an individual task that can run commands in a job.
  - Actions: An action is a reusable unit of code that can be used in multiple workflows. You can create your own actions, or use actions created by the GitHub community.