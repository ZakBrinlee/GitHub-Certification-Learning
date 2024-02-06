# [Build continuous integration (CI) workflows by using GitHub Actions](https://learn.microsoft.com/en-us/training/modules/github-actions-ci/)

## Microsoft Learning path course work

## [Course exercise repo](https://github.com/ZakBrinlee/skills-test-with-actions/tree/ci)

## What will be covered
- Learn how to create workflows that enable you to use Continuous Integration (CI) for your projects.
- In this module, you:
  - Build and test a Node.js project by using GitHub Actions and a templated workflow
  - Debug a failed test using the GitHub Actions Log
  - Customize your workflow with GitHub Actions

## Intro
- CI is the practice of using automation to build and test software every time a developer commits changes to version control.

### Customize your workflow with environment variables and artifact data
- Cache dependencies with the cache action
  - To cache dependencies for a job, use GitHub's cache action. This action retrieves a cache identified by a unique key that you provide. When the action finds the cache, it then retrieves the cached files to the path that you configure. To use the cache action, you'll need to set a few specific parameters:
- Pass artifact data between jobs
  - Similar to the idea of caching dependencies within your workflow, you can pass data between jobs within the same workflow. You can do this by using the upload-artifact and download-artifact actions.
- Enable step debug logging in a workflow
  - In some cases, the default workflow logs won't provide enough detail to diagnose why a specific workflow run, job, or step has failed. For these situations, you can enable additional debug logging for two options: runs and steps. Enable this diagnostic logging by setting two repository secrets that require admin access to the repository to true:
    - To enable runner diagnostic logging, set the ACTIONS_RUNNER_DEBUG secret in the repository that contains the workflow to true.
    - To enable step diagnostic logging, set the ACTIONS_STEP_DEBUG secret in the repository that contains the workflow to true.


## CI/CD with GH Actions
- Workflow: A workflow is a unit of automation from its start to finish, including the definition of what triggers the automation, what environment or other aspects should be taken into account during the automation, and what should happen as a result of the trigger.
- Job: A job is a section of the workflow, and is made up of one or more steps. In this section of our workflow, the template defines the steps that make up the build job.
- Step: A step represents one effect of the automation. A step could be defined as a GitHub Action, or another unit, like printing something to the console.
- Action: An action is a piece of automation written in a way that is compatible with workflows. Actions can be written by GitHub, by the open source community, or you can write them yourself!

