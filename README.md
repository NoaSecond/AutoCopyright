# AutoCopyright
[AutoCopyright](https://github.com/YoruKiwi/AutoCopyright/) is an open-source Continuous Integration (CI) project designed to automate the addition of copyright notices in code files.

<a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=githubactions"/></a>

## Description
[AutoCopyright](https://github.com/YoruKiwi/AutoCopyright/) is a lightweight tool that seamlessly integrates with GitHub Actions. It utilizes YAML (YML) configuration files and automatically add a copyright notice at the end of each files.

## Setup
To set up [AutoCopyright](https://github.com/YoruKiwi/AutoCopyright/) for your project, follow these steps:

### Project Setup
1. Place the `utils` folder and the `.github` folder at the root of your project.
2. Configure the list of files and folders to `exclude` inside `utils/addCopyright.py`.
3. Ensure to set the copyright_comment var inside `utils/addCopyright.py`.

### Repository Setup
1. On [GitHub](https://github.com/), open your repository.
2. Go to `Settings`.
3. Then drop `Actions` to open `General`.
4. In `Workflow permissions`, toggle `Read and write permissions`.
5. Then, enable `Allow GitHub Actions to create and approve pull requests`.
6. Don't forget to click on `Save` button below.

That's it! With these simple setup instructions, [AutoCopyright](https://github.com/YoruKiwi/AutoCopyright/) will handle the rest, keeping your file up to date with each commit.

## Contributing
If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository
2. Create a new branch: `git checkout -b my-feature`
3. Make your changes and commit them: `git commit -am 'Add some feature'`
4. Push the branch to your forked repository: `git push origin my-feature`
5. Submit a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
