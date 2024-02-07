# [Create and publish custom GitHub actions](https://learn.microsoft.com/en-us/training/modules/create-custom-github-actions/)

## [Course excercise repo](https://github.com/ZakBrinlee/skills-write-javascript-actions)

## What will be covered
- Learn how to write your own GitHub actions and identify the metadata, syntax, and workflow commands to create custom workflows. Learn best practices for documenting and versioning your action, and how to publish your action to the GitHub Marketplace.

## Links
- [GitHub Actions Toolkit](https://github.com/actions/toolkit)

## Docker container actions
- Before building a Docker container action, you should have some basic understanding of how to use environment variables and the Docker container filesystem. The steps to take to build a Docker container action are then minimal and straightforward:
  - Create a `Dockerfile` to define the commands to assemble the Docker image.
  - Create an `action.yml` metadata file to define the inputs and outputs of the action. Set the `runs: using:` value to `docker` and the `runs: image:` value to `Dockerfile` in the file.
  - Create an `entrypoint.sh` file to describe the docker image.
  - Commit and push your action to GitHub with the following files: `action.yml`, `entrypoint.sh`, `Dockerfile`, and `README.md`.

### JavaScript actions
- The steps to build a JavaScript action are minimal and straightforward:
  - Create an `action.yml` metadata file to define the inputs and outputs of the action, as well as tell the action runner how to start running this JavaScript action.
  - Create an `index.js` file with context information about the Toolkit packages, routing, and other functions of the action.
  - Commit and push your action to GitHub with the following files: `action.yml`, `index.js`, `node_modules`, `package.json`, `package-lock.json`, and `README.md`.

### Composite run steps actions
- Composite run steps actions allow you to reuse actions by using shell scripts. You can even mix multiple shell languages within the same action. If you have many shell scripts to automate several tasks, you can now easily turn them into an action and reuse them for different workflows. Sometimes it's easier to just write a shell script than using JavaScript or wrapping your code in a Docker container.

### Metadata and syntax needed to create an action
- Inputs
  - Inputs are the parameters that allow you to specify data that the action expects to use during its runtime. GitHub stores these input parameters as environment variables.
- Outputs
  - Outputs are the parameters that allow you to declare data. Keep in mind that actions that run later in a workflow can use the output data that was declared in a previously run action.
- Runs
  - As you learned previously, your action needs to have a runs statement that defines the command necessary to execute your action. Depending on how you're creating your action—whether you're using a Docker container, JavaScript, or composite run steps—the runs syntax is defined differently.
