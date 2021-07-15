# dotnet-core-pre-commit
Cross-platform .NET Core pre-commit hooks


## How to use

Add this to your `.pre-commit-config.yaml`

```
-   repo: https://github.com/juanodicio/dotnet-core-pre-commit.git
    rev: v0.1
    hooks:
    -   id: dotnet-test
```

If your solution/project is not in the project's root directory, you can 
add the `--target` argument to specify the path of you solution or project 

```
-   repo: https://github.com/juanodicio/dotnet-core-pre-commit.git
    rev: v0.1
    hooks:
    -   id: dotnet-test
        args: [ '--target', 'tests/MyApp.Application.UnitTests' ]
```


## License

- [MIT License](LICENSE)