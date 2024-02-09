# [Advanced GitHub Actions](https://www.linkedin.com/learning/advanced-github-actions)

## LinkedIn Learning path course work

## Intro
- Basic git knowledge
- Scripting language knowledge
- GitHub Actions knowledge

### Advanced Workflows
- Service Continers
  - Service contianers help to replicate the enviroment with the neccessary dependencies
  - Job runner must be linux based
  - Self-hosted uses linux and Docker
- Scheduled Triggers
  - Scheduled triggers can be used to run workflows at a specific time and interval
  - cron syntax to describe the schedule
  - UTC time
- Caching
  - Caching can be used to store files and dependencies to speed up the workflow
  - `setup-node` for npm package manager
  - Key Creation - recommends to hash the file name

### GitHub Actions Matrix Strategy
- Matrix strategy can be used to run the same job with different configurations
- `matrix: -> key: [<value>, <value>, ...]`
- `include: ` - Includes a combination with
- `exclude: ` - Excludes a combination with

### Publishing Packages
- Built in controls for permissions and visibility
- Auth is required for software package interaction
- Release events are best for publishing packages

### Self-Hosted Runners
- Allows you to configure your compute needs
- Queued jobs limited to 24 hours
- Security is a major consideration
  - Only use self hosted running with private repositories

### JavaScript Actions
- JavaScript actions can be used to create custom actions
  - Bundled with dependencies
  - Runs directly on the runner system
  - All supported runners
  - faster than docker
- Repository for the code is required
- Node runtime needs installed
- Install `@actions/core and @actions/github` for the action to work
- Action Metadata files
  - `action.yml` - Describes the action
    - inputs
    - outputs
    - runtime
    - author
    - description
- README.md is required if shared in the GH Marketplace
- Needs to updated `.gitignore` to **not ignore** `dist`
- GitHub actions toolkit
  - `/core` package
    - functionality for working with GH Actions front-end and internals
    - read inputs, set outputs
    - set exit codes
    - create annotations
  - `/github` package
    - exposes the workflow-action context as JSON
    - provides auth client